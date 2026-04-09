# Extract unique items from a list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-unique-items-from-a-list

---

[Skip to main content](https://exceljet.net/formulas/extract-unique-items-from-a-list#main-content)

[](https://exceljet.net/formulas/extract-unique-items-from-a-list#)

*   [Previous](https://exceljet.net/formulas/expense-begins-on-specific-month)
    
*   [Next](https://exceljet.net/formulas/filter-values-in-array-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Extract unique items from a list
================================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")

Summary
-------

To extract only unique values from a list or column, you can use an array formula based on [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, and [COUNTIF](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in D5, copied down, is:

    {=INDEX(list,MATCH(0,COUNTIF($D$4:D4,list),0))}
    

where "list" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B11. This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered using control + shift + enter in Excel 2019 and older.

_Note: In [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2021, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 provides a better, more elegant way to [list unique values](https://exceljet.net/formulas/unique-values)
 and [count unique values](https://exceljet.net/formulas/count-unique-values)
. These formulas can be adapted to [apply logical criteria](https://exceljet.net/formulas/unique-values-with-criteria)
._

Generic formula
---------------

    {=INDEX(list,MATCH(0,COUNTIF(uniques,list),0))}

Explanation 
------------

The core of this formula is a basic lookup with INDEX:

    =INDEX(list,row)
    

In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list.

The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with MATCH and COUNTIF, and the main trick is here:

    COUNTIF($D$4:D4,list)
    

Here, COUNTIF counts how many times items already in the unique list appear in the master list, using an [expanding reference](https://exceljet.net/glossary/expanding-reference)
 for the range, $D$4:D4.

An expanding reference is absolute on one side, and relative on the other. In this case, as the formula is copied down, the reference will expand to include more rows in the unique list.

Note the reference starts in D4, one row _above_ the first unique entry, in the unique list. This is intentional — we want to count items _already_ in the unique list, and we can't include the current cell without creating a circular reference. So, we start on the row above.

_Important: be sure the heading for the unique list does not appear in the master list._

For the criteria in COUNTIF, we are using the master list itself. When given multiple criteria, COUNTIF will return multiple results in an [array](https://exceljet.net/glossary/array)
. At each new row, we have a different array like this:

    {0;0;0;0;0;0;0} // row 5
    {1;0;0;0;1;0;0} // row 6
    {1;1;0;0;1;0;1} // row 7
    {1;1;1;1;1;0;1} // row 8
    

Note: COUNTIF handles multiple criteria with an "OR" relationship (i.e. COUNTIF (range, {"red","blue", "green"}) counts red, blue, or green.

Now we have the arrays we need to find positions (row numbers). For this, we use MATCH, set up for an exact match, to find zero values. If we put the arrays created by COUNTIF above into MATCH, here is what we get:

    MATCH(0,{0;0;0;0;0;0;0},0) // 1 (Joe)
    MATCH(0,{1;0;0;0;1;0;0},0) // 2 (Bob)
    MATCH(0,{1;1;0;0;1;0;1},0) // 3 (Sue)
    MATCH(0,{1;1;1;1;1;0;1},0) // 6 (Aya)
    

MATCH locates items by looking for a count of zero (i.e. looking for items that do not yet appear in the unique list). This works because MATCH always returns the first match when there are duplicates.

Finally, the positions are fed into INDEX as row numbers, and INDEX returns the name at that position.

### Non-array version with LOOKUP

You can build a non-array formula to extract unique items using the flexible LOOKUP function:

    =LOOKUP(2,1/(COUNTIF($D$4:D4,list)=0),list)
    

The formula construction is similar to the INDEX MATCH formula above, but LOOKUP can handle the array operation natively.

*   COUNTIF returns counts of each value from "list" in the [expanding range](https://exceljet.net/glossary/expanding-reference)
     $D$4:D4
*   Comparing to zero creates an array of TRUE and FALSE values
*   The number 1 is divided by the array, creating an array of 1s and #DIV/0 errors
*   This array becomes the lookup\_vector inside LOOKUP
*   The lookup value of 2 is larger than any values in the lookup\_vector
*   LOOKUP will match the last non-error value in the lookup array
*   LOOKUP returns the corresponding value in result\_vector, the named range "list"

### Extract items that appear just once

The LOOKUP formula above is easy to extend with [boolean logic](https://exceljet.net/glossary/boolean-logic)
. To extract a list of unique items that appear just once in the source data, you can use a formula like this:

    =LOOKUP(2,1/((COUNTIF($D$4:D4,list)=0)*(COUNTIF(list,list)=1)),list)
    

The only addition is the second COUNTIF expression:

    COUNTIF(list,list)=1
    

Here, COUNTIF returns an array of item counts like this:

    {2;2;2;2;2;1;2}
    

which are compared to 1, resulting in an array of TRUE/FALSE values:

    {FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE}
    

This array acts as a "filter' to restrict output to items that occur just once in the source data.

### UNIQUE function in Excel 365

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 provides a better, more elegant way to [list unique values](https://exceljet.net/formulas/unique-values)
 and [count unique values](https://exceljet.net/formulas/count-unique-values)
. These formulas can be adapted to [apply logical criteria](https://exceljet.net/formulas/unique-values-with-criteria)
.

Related formulas
----------------

[![Excel formula: Get value of last non-empty cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_value_of_last_non-empty_cell.png "Excel formula: Get value of last non-empty cell")](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

### [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

In this example, the goal is to get the last value in column B, even when data may contain empty cells. A secondary goal is to get the corresponding value in column C. This is useful for analyzing datasets where the most recent or last entry is significant. In the current version of Excel, a good...

[![Excel formula: Lookup latest price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20latest%20price.png "Excel formula: Lookup latest price")](https://exceljet.net/formulas/lookup-latest-price)

### [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)

The LOOKUP function assumes data is sorted, and always does an approximate match. If the lookup value is greater than all values in the lookup array, default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors,...

[![Excel formula: Sort and extract unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20and%20extract%20unique%20values.png "Excel formula: Sort and extract unique values")](https://exceljet.net/formulas/sort-and-extract-unique-values)

### [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)

Note: the core idea of this formula is adapted from an example in Mike Girvin's excellent book Control+Shift+Enter . The example shown uses several formulas, which are described below. At a high level, the MMULT function is used to compute a numeric rank in a helper column (column C), and this rank...

[![Excel formula: COUNTIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20multiple%20criteria%20and%20OR%20logic.png "Excel formula: COUNTIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

### [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to use the COUNTIFS function to count data with "OR logic". The challenge is the COUNTIFS function applies AND logic by default. COUNTIFS function The COUNTIFS function returns the count of cells that meet one or more criteria, and supports logical operators (>,...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    
*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    

### Links

*   [How to extract a unique distinct (Oscar Cronquist, Get Digital Help)](http://www.get-digital-help.com/2009/03/30/how-to-extract-a-unique-list-and-the-duplicates-in-excel-from-one-column/)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)
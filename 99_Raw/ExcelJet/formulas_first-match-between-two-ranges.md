# First match between two ranges - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/first-match-between-two-ranges

---

[Skip to main content](https://exceljet.net/formulas/first-match-between-two-ranges#main-content)

[](https://exceljet.net/formulas/first-match-between-two-ranges#)

*   [Previous](https://exceljet.net/formulas/first-column-number-in-range)
    
*   [Next](https://exceljet.net/formulas/first-row-number-in-range)
    

[Range](https://exceljet.net/formulas#Range)

First match between two ranges
==============================

by Dave Bruns · Updated 22 Aug 2018

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: First match between two ranges](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/first%20match%20between%20two%20ranges.png "Excel formula: First match between two ranges")

Summary
-------

To retrieve the first match in two ranges of values, you can use a formula based on the INDEX, MATCH, and COUNTIF functions. In the example shown, the formula in G5 is:

    =INDEX(range2,MATCH(TRUE,COUNTIF(range1,range2)>0,0))
    

where "range1" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B8, "range2" is the named range D5:D7.

Generic formula
---------------

    =INDEX(range2,MATCH(TRUE,COUNTIF(range1,range2)>0,0))

Explanation 
------------

In this example the named range "range1" refers to cells B5:B8, and the [named range](https://exceljet.net/glossary/named-range)
 "range2" refers to D5:D7. We are using named ranges for convenience and readability only; the formula works fine with regular cell references as well.

The core of this formula is INDEX and MATCH. The INDEX function retrieves a value from range2 that represents the first value in range2 that is found in range1. The INDEX function requires an index (row number) and we generate this value using the MATCH function, which is set to match the value TRUE in this portion of the formula:

    MATCH(TRUE,COUNTIF(range1,range2)>0,0)
    

Here, the match value is TRUE, and the lookup array is created with COUNTIF here:

    COUNTIF(range1,range2)>0
    

COUNTIF returns a count of the range2 values that appear in range1. Because range2 contains multiple values, COUNTIF will return multiple results that look like this:

    {0;0;1}
    

We use ">0" to force all results to either TRUE or FALSE:

    {FALSE;FALSE;TRUE}
    

Then MATCH does its thing and returns the position of the first TRUE (if any) that appears, in this case, the number 3.

Finally, INDEX returns the value at that position, "Red".

Related formulas
----------------

[![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")](https://exceljet.net/formulas/get-first-match-cell-contains)

### [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in...

[![Excel formula: Range contains one of many values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20values.png "Excel formula: Range contains one of many values")](https://exceljet.net/formulas/range-contains-one-of-many-values)

### [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)

Each item in rng is compared to each item in values and the result is an array of TRUE or FALSE values. The double negative will force the TRUE and FALSE values to 1 and 0 respectively. Since SUMPRODUCT receives just one array, it simply adds up the items in the array and returns the result...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    
*   [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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
# XLOOKUP with Boolean OR logic - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-with-boolean-or-logic

---

[Skip to main content](https://exceljet.net/formulas/xlookup-with-boolean-or-logic#main-content)

[](https://exceljet.net/formulas/xlookup-with-boolean-or-logic#)

*   [Previous](https://exceljet.net/formulas/xlookup-wildcard-match-example)
    
*   [Next](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP with Boolean OR logic
=============================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7386/download?token=av_3Lalt)
 (16 KB)

![Excel formula: XLOOKUP with Boolean OR logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20boolean%20OR%20logic.png "Excel formula: XLOOKUP with Boolean OR logic")

Summary
-------

To configure XLOOKUP with Boolean OR logic, use a lookup value of 1 with a logical expression based on addition. In the example shown, the formula in G5 is:

    =XLOOKUP(1,(data[Color]="red")+(data[Color]="pink"),data)
    

where **data** is the name of the [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:E14.

_Note: see below for an equivalent formula based on [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
._

Generic formula
---------------

    =XLOOKUP(1,boolean_expression,data)

Explanation 
------------

In this example, the goal is to use XLOOKUP to find the first "red" or "pink" record in the data as shown. All data is in an Excel Table named **data** in the range B5:E14. This means the formulas below use [structured references](https://exceljet.net/glossary/structured-reference)
. As a result, the formulas will automatically include new data added to the table.

### XLOOKUP function

In the worksheet shown, the formula in cell G5 is:

    =XLOOKUP(1,(data[Color]="red")+(data[Color]="pink"),data)
    

The _lookup\_value_ is provided as 1, for reasons that become clear below. For the _lookup\_array_, we use an expression based on [Boolean logic](https://exceljet.net/glossary/boolean-logic)
:

    (data[Color]="red")+(data[Color]="pink")
    

In the world of [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
, AND logic corresponds to multiplication (\*), and OR logic corresponds to addition (+). Because we want OR logic, we use addition in this case. Notice Excel is not case-sensitive, so we don't need to capitalize the colors.

After the expression is evaluated, we have two [arrays](https://exceljet.net/glossary/array)
 of TRUE and FALSE values like this:

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}+
    {FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE}
    

Notice, in the first array, TRUE values correspond to "red". In the second array, TRUE values correspond to "pink".

The math operation of adding these arrays together converts the TRUE and FALSE values to 1s and 0s, and results in a new array composed only of 1s and 0s:

    {0;0;1;0;1;0;0;0;0;1}
    

Notice the 1s in this array correspond to rows where the color is either "red" or "pink". We can now rewrite the formula like this:

    =XLOOKUP(1,{0;0;1;0;1;0;0;0;0;1},data)
    

The first 1 in the lookup array corresponds to row three of the data, where the color is "red". Since XLOOKUP will by default return the first match, and since the entire table **data** is supplied as the return array, XLOOKUP returns the third row as a final result.

### Not mutually exclusive

In the example above, we are testing for two possible values in a _single_ column of data. This means the values are mutually exclusive — both tests can't return TRUE at the same time. If you are testing _multiple_ columns/fields for values, or if the tests are otherwise not mutually exclusive, the formula logic needs to be adjusted to handle the possibility that more than one logical test will return TRUE. In that case, when the result arrays are added together, the final array will contain a number larger than 1 and the lookup value of 1 will not be found. To guard against this problem, you can adjust the formula as follows:

    =XLOOKUP(1,--((test1)+(test2)>0),array)
    

In this version, we add result arrays together and check to see if the results are greater than 0. This creates a new array containing only TRUE and FALSE values. The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to convert the TRUE and FALSE values to 1s and 0s so the lookup value of 1 will continue to work.

For example, in the worksheet shown, to test for the first record with a color of "green" OR a quantity greater than 15, use a formula like this:

    =XLOOKUP(1,--((data[Color]="green")+(data[Qty]>15)>0),data)
    

You can of course adjust the logic as needed to target the desired data.

Video: [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
.

### INDEX and MATCH

In [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not include the XLOOKUP function, you can perform the same lookup with an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
:

    =INDEX(data,MATCH(1,(data[Color]="red")+(data[Color]="pink"),0),0)
    

In this formula, the [MATCH function](https://exceljet.net/functions/match-function)
 uses the same logic explained above to locate the correct row number, which is returned to INDEX as the _row\_num_ argument. The _column\_num_ argument is hardcoded as 0 to tell the [INDEX function](https://exceljet.net/functions/index-function)
 to return the [entire row](https://exceljet.net/formulas/look-up-entire-row)
.

Because this formula returns 4 values in one row, it must be entered as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. In [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2022, the formula "just works" and all four values [spill](https://exceljet.net/glossary/spill)
 into multiple cells. For more on this behavior, see: [Dynamic Array Formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
.

### FILTER function

If you want to display _all_ "red" or "pink" records, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with exactly the same logic like this:

    =FILTER(data,(data[Color]="red")+(data[Color]="pink"))
    

Boolean logic works well in all the new [Dynamic Array functions](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 and is nicely portable — you can copy the _lookup\_array_ from XLOOKUP into FILTER as the _include_ argument, and it just works.

Related formulas
----------------

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20muliple%20criteria.png "Excel formula: VLOOKUP with multiple criteria")](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

### [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

In the example shown, we want to look up employee departments and groups using VLOOKUP by matching the first and last name of an employee. One limitation of VLOOKUP is that it only handles one condition: the lookup\_value, which is matched against the first column in the table. This makes it...

[![Excel formula: Lookup first negative value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20first%20negative%20value.png "Excel formula: Lookup first negative value")](https://exceljet.net/formulas/lookup-first-negative-value)

### [Lookup first negative value](https://exceljet.net/formulas/lookup-first-negative-value)

In this example, the goal is to lookup the first negative value in a set of data. In addition, we also want to get the corresponding date. All data is in an Excel Table called data, in the range B5:C16. This information represents the low temperature in Fahrenheit (F) for the dates as shown. There...

[![Excel formula: INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20with%20multiple%20criteria.png "Excel formula: INDEX and MATCH with multiple criteria")](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

### [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

This is a more advanced formula. For basics, see How to use INDEX and MATCH . Normally, an INDEX MATCH formula is configured with MATCH set to look through a one-column range and provide a match based on given criteria. Without concatenating values in a helper column , or in the formula itself,...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    
*   [Lookup first negative value](https://exceljet.net/formulas/lookup-first-negative-value)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    

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
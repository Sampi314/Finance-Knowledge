# Count cells not equal to many things - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-not-equal-to-many-things

---

[Skip to main content](https://exceljet.net/formulas/count-cells-not-equal-to-many-things#main-content)

[](https://exceljet.net/formulas/count-cells-not-equal-to-many-things#)

*   [Previous](https://exceljet.net/formulas/count-cells-not-equal-to)
    
*   [Next](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
    

[Count](https://exceljet.net/formulas#Count)

Count cells not equal to many things
====================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[ISNA](https://exceljet.net/functions/isna-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count cells not equal to many things](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20not%20equal%20to%20many.png "Excel formula: Count cells not equal to many things")

Summary
-------

To count cells not equal to any of many things, you can use a formula based on the [MATCH](https://exceljet.net/functions/match-function)
, [ISNA](https://exceljet.net/functions/isna-function)
, and [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 functions. In the example shown, the formula in cell F5 is:

    =SUMPRODUCT(--(ISNA(MATCH(data,exclude,0))))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15 and **exclude** is the named range D5:D7.

Generic formula
---------------

    =SUMPRODUCT(--(ISNA(MATCH(data,exclude,0))))

Explanation 
------------

First, a little context. Normally, if you have just a couple things you don't want to count, you can use [COUNTIFS](https://exceljet.net/functions/countifs-function)
 like this:

    =COUNTIFS(range,"<>apple",range,"<>orange")
    

But this doesn't scale very well if you have a list of many things, because you'll have to add an additional range/criteria pair to each thing you don't want to count. It would be a lot easier to build a list and pass in a reference to this list as part of the criteria. That's exactly what the formula on this page does. The formula in cell F5 is:

    =SUMPRODUCT(--(ISNA(MATCH(data,exclude,0))))
    

### MATCH function

At the core, this formula uses the [MATCH function](https://exceljet.net/functions/match-function)
 to find cells not equal to "a", "b", or "c" with a reversed configuration like this:

    MATCH(data,exclude,0)
    

Note the _lookup\_value_ and _lookup\_array_ are "reversed" from the standard configuration — we provide all values from the named range **data** (B5:B15) as _lookup\_values_, and provide the values we want to exclude as the _lookup\_array_ in the named range **exclude** (D5:D7). Because we give MATCH more than one _lookup\_value_, we get back more than one result in an [array](https://exceljet.net/glossary/array)
 like this:

    {1;2;3;#N/A;#N/A;#N/A;1;2;3;#N/A;1}
    

Essentially, MATCH gives us the position of matching values as a number, and returns #N/A for all other values.

### ISNA function

The #N/A results are the ones we're interested in, since they represent values _not equal_ to "a", "b", or "c". Accordingly, we use the [ISNA function](https://exceljet.net/functions/isna-function)
 to force all values to either TRUE or FALSE:

    --ISNA(MATCH(data,exclude,0)
    

In the resulting array, TRUE values correspond to #N/A errors (values not matched) and FALSE values correspond to the numbers (matched values). Then we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to coerce TRUE to 1 and FALSE to zero.

### SUMPRODUCT function

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 is designed to multiply and then sum multiple arrays. The resulting array inside SUMPRODUCT looks like this:

    =SUMPRODUCT({0;0;0;1;1;1;0;0;0;1;0})
    

With only one array to process, SUMPRODUCT sums and returns a final result, 4.

_Note: This is an [array formula](https://exceljet.net/glossary/array-formula)
 and using SUMPRODUCT instead of SUM avoids the need to enter the formula with control + shift + enter in [legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

### Count minus match

Another way to count cells not equal to any of several things is to count all values, and subtract matches. You can do this with a formula like this:

    =COUNTA(range)-SUMPRODUCT(COUNTIF(range,exclude))
    

Here, [COUNTA](https://exceljet.net/functions/counta-function)
 returns a count of all non-empty cells. The [COUNTIF function](https://exceljet.net/functions/countif-function)
, given the named range **exclude** will return three counts, one for each item in the list. SUMPRODUCT adds up the total, and this number is subtracted from the count of all non-empty cells. The final result is the number of cells that do not equal values in **exclude.**

### Literal contains type logic

The formula on this page counts with "equals to" logic. If you need to count cells that do not _contain_ many strings, where contains means a string may appear anywhere in a cell, you'll need a [more complex formula.](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

Related formulas
----------------

[![Excel formula: Count cells not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to.png "Excel formula: Count cells not equal to")](https://exceljet.net/formulas/count-cells-not-equal-to)

### [Count cells not equal to](https://exceljet.net/formulas/count-cells-not-equal-to)

In this example, the goal is to count the number of cells in column D that are not equal to a given color. The simplest way to do this is with the COUNTIF function , as explained below. Not equal to In Excel, the operator for not equal to is "<>". For example: =A1<>10 // A1 is not equal...

[![Excel formula: Count cells not equal to x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20x%20or%20y_1.png "Excel formula: Count cells not equal to x or y")](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

### [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

In this example, the goal is to count the number of cells in data (B5:B15) that are not equal to "red" or "blue". This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. Not equal to The not equal to operator in Excel is <>. For example, with the...

[![Excel formula: Count not equal to multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20not%20equal%20to%20multiple%20criteria.png "Excel formula: Count not equal to multiple criteria")](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

### [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

In this example, the goal is to count rows in a set of data using multiple criteria and "not equals to" logic. Specifically, we want to count males that are not in group A or B. All data is in an Excel Table named data in the range B5:D15. This problem can be solved with the COUNTIFS function or...

[![Excel formula: Count cells that do not contain many strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain%20many%20strings.png "Excel formula: Count cells that do not contain many strings")](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

### [Count cells that do not contain many strings](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

The goal in this example is to count cells in a range that do not contain a given number of strings. The cells to evaluate are in the named range data (B5:B14) and the strings to exclude are listed in the named range exclude (D5:D7). If your needs are simple, you can use the COUNTIFS function to...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

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

*   [Count cells not equal to](https://exceljet.net/formulas/count-cells-not-equal-to)
    
*   [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
    
*   [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)
    
*   [Count cells that do not contain many strings](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
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
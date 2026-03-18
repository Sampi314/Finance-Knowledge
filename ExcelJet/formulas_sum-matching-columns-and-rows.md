# Sum matching columns and rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-matching-columns-and-rows

---

[Skip to main content](https://exceljet.net/formulas/sum-matching-columns-and-rows#main-content)

[](https://exceljet.net/formulas/sum-matching-columns-and-rows#)

*   [Previous](https://exceljet.net/formulas/sum-matching-columns)
    
*   [Next](https://exceljet.net/formulas/sum-numbers-in-single-cell)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum matching columns and rows
=============================

by Dave Bruns · Updated 18 Jan 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Sum matching columns and rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_matching_columns_and_rows.png "Excel formula: Sum matching columns and rows")

Summary
-------

To sum values in matching columns and rows, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in J6 is:

    =SUMPRODUCT((codes=J4)*(days=J5)*data)
    

where **data** (C5:G14), **days** (B5:B14), and **codes** (C4:G4) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: In the latest version of Excel you can also use the [FILTER function](https://exceljet.net/functions/filter-function)
, as explained below._

Generic formula
---------------

    =SUMPRODUCT((range1=criteria1)*(range2=criteria2)*data)

Explanation 
------------

In this example, the goal is to sum values in matching columns and rows. Specifically, we want to sum values in **data** (C5:G14) where the column code is "A" and the day is "Wed". One way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, which can handle [array operations](https://exceljet.net/glossary/array-operation)
 natively, without requiring control shift enter. In the latest version of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
 is another option. Both approaches are explained below.

### SUMPRODUCT function

In the example shown, the formula in J6 is:

    =SUMPRODUCT((codes=J4)*(days=J5)*data)
    

where **data** (C5:G14), **days** (B5:B14), and **codes** (C4:G4) are [named ranges](https://exceljet.net/glossary/named-range)
. In this case, we are multiplying all values in the named range **data** by two expressions that "zero out" values that should not be included in the final sum:

    (codes=J4)*(days=J5)
    

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

The first expression applies a condition based on codes:

    (codes=J4)
    

Since J4 contains "B", the expression creates an [array](https://exceljet.net/glossary/array)
 of TRUE FALSE values like this:

    {FALSE,TRUE,FALSE,TRUE,FALSE}
    

Each TRUE indicates a column where the code is "B". The second expression tests for day:

    (days=J5)
    

Since J4 contains "Wed", the expression returns an array of TRUE and FALSE values like this:

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}

In this array, each TRUE represents a row where the day in column B is "Wed".

Next, the two arrays are multiplied together. In Excel, TRUE and FALSE values are automatically coerced to 1s and 0s by any math operation, so the multiplication step converts the arrays above to ones and zeros. When the horizontal array from the first expression is multiplied by the vertical array from the second expression, the result is a single two-dimensional array with the same dimensions as the original data:

    {0,0,0,0,0;0,0,0,0,0;0,1,0,1,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,1,0,1,0;0,0,0,0,0;0,0,0,0,0}

The array above is 10 rows by 5 columns.The semi-colons (;) indicate rows, and the commas (,) [indicate columns](https://exceljet.net/glossary/array)
. When this array is multiplied by **data**, the operation effectively "zeros out" the values in **data** that should not be included in the final sum. The process can be visualized as shown below, where the "Filter array" is the array of 1s and 0s above.

![Boolean array multiplication inside SUMPRODUCT](https://exceljet.net/sites/default/files/images/formulas/inline/sum_matching_columns_and_rows_boolean_array_multiplication.png "Boolean array multiplication inside SUMPRODUCT")

After **data** is multiplied by the Boolean array above, the result is a single array like this:

    =SUMPRODUCT({0,0,0,0,0;0,0,0,0,0;0,6,0,7,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,3,0,2,0;0,0,0,0,0;0,0,0,0,0})

With just one array to process, SUMPRODUCT returns the sum of all elements in the final array, 18.

### FILTER function

In the latest version of Excel, you can also use the [FILTER function](https://exceljet.net/functions/filter-function)
 to solve this problem. 

    =SUM(FILTER(FILTER(data,codes=J4,0),days=J5,0))

This formula works in two steps. First, the _inner_ FILTER returns columns where code is "B":

    FILTER(data,codes=J4,0) // filter columns

The resulting array is returned to the _outer_ FILTER function, which returns rows where day is "Wed":

    =SUM(FILTER(array,days=J5,0)) // filter rows

The outer FILTER then returns matching data to the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM({6,7;3,2}) // returns 18

The SUM function then calculates a sum and returns a final result, 18.

Video: [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

### Notes

1.  If you only need to sum matching columns (not rows) you can use a [formula like this](https://exceljet.net/formulas/sum-matching-columns)
    .
2.  To sum matching rows only, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
    .

Related formulas
----------------

[![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

### [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using array constants to hold the values of interest, but the article also shows how to use cell references instead. In simple...

[![Excel formula: SUMPRODUCT case-sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT_case_sensitive_lookup.png "Excel formula: SUMPRODUCT case-sensitive lookup")](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

### [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

The SUMPRODUCT function multiplies arrays together and returns the sum of products. If only one array is supplied, SUMPRODUCT will simply sum the items in the array. For example, if we give SUMPRODUCT one array in the form of the data\[Qty\] column: =SUMPRODUCT(data\[Qty\]) // returns 54 SUMPRODUCT...

[![Excel formula: Sum matching columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20matching%20columns.png "Excel formula: Sum matching columns")](https://exceljet.net/formulas/sum-matching-columns)

### [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)

At the core, this formula relies on the SUMPRODUCT function to sum values in matching columns in the named range data C5:G14. If all data were provided to SUMPRODUCT in a single range, the result would be the sum of all values in the range: =SUMPRODUCT(data) // all data, returns 387 To apply a...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    
*   [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)
    
*   [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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
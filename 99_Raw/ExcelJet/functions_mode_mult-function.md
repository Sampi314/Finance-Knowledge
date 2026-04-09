# Excel MODE.MULT function | Exceljet

**Source:** https://exceljet.net/functions/mode.mult-function

---

[Skip to main content](https://exceljet.net/functions/mode.mult-function#main-content)

[](https://exceljet.net/functions/mode.mult-function#)

*   [Previous](https://exceljet.net/functions/mode-function)
    
*   [Next](https://exceljet.net/functions/mode.sngl-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

MODE.MULT Function
==================

by Dave Bruns · Updated 13 Apr 2022

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[MEDIAN](https://exceljet.net/functions/median-function)

[MODE](https://exceljet.net/functions/mode-function)

[MODE.SNGL](https://exceljet.net/functions/mode.sngl-function)

![Excel MODE.MULT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20mode.mult%20function.png "Excel MODE.MULT function")

Summary
-------

The Excel MODE.MULT function returns an array of the most frequently occurring numbers in a numeric data set. For example, =MODE.MULT(1,2,3,3,4,5,5) returns {3;5}, because there are two modes, 3 and 5.

Purpose 
--------

Get most frequently occurring numbers

Return value 
-------------

Numbers representing mode(s)

Syntax
------

    =MODE.MULT(number1,[number2],...)

*   _number1_ - A number or cell reference that refers to numeric values.
*   _number2_ - \[optional\] A number or cell reference that refers to numeric values.

Using the MODE.MULT function 
-----------------------------

The Excel MODE.MULT function returns a vertical [array](https://exceljet.net/glossary/array)
 of the most frequently occurring number(s) in a numeric data set. The mode is the most frequently occurring number in a set of data. When there is just one mode in a set of data, MODE.MULT will return a single result. If there is more than one mode in supplied data, MODE.MULT will return more than one result. If there are no modes, MODE.MULT will return #N/A.

The MODE.MULT function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. Arguments can be a hardcoded constant, a cell reference, or a range, in any combination. MODE ignores empty cells, text values, and the logical values TRUE and FALSE. The MODE function will accept up to 254 separate arguments. 

### Examples

In the example shown, the formula entered in D5:D9 is:

    =MODE.MULT(B5:B16)
    

In [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports dynamic arrays, multiple results will [spill](https://exceljet.net/glossary/spill)
 onto the worksheet automatically. In earlier versions of Excel, you will need to enter the formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
. See below for more information.

MODE returns the most frequently occurring number(s) in supplied data. For example,

    =MODE.MULT(1,2,4,4,5,5,5,6) // returns 5
    =MODE.MULT(7,8,9,7,9) // returns 7
    

If there are no duplicate numbers, the MODE.MULT function returns the #N/A error:

    =MODE(7,9,6,5,3,1,0) // returns #N/A
    

If there is more than one mode in a set of data, MODE.MULT will return more than one result:

    =MODE.MULT(1,3,3,5,5,7,7,8) // returns {3,5,7}
    

Note: MODE.MULT will not return _any_ duplicated number(s), only mode(s).

### Array formula syntax

The MODE.MULT function returns an array of results and must be entered as a multi-cell array formula if you are _not_ using [Excel 365](https://exceljet.net/glossary/excel-365)
. Here are the steps:

1.  Select a vertical range of cells
2.  Enter MODE.MULT function
3.  Confirm with control + shift + enter

In each selected cell, MODE.MULT will return a mode value, if one exists.

### Horizontal array

The MODE.MULT function returns results in a vertical array. To return a horizontal array, add the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
:

    =TRANSPOSE(MODE.MULT(range))
    

This formula also needs to be entered as an [array formula](https://exceljet.net/glossary/array-formula)
, unless you are using Excel 365, or another version of Excel that supports dynamic arrays.

### Excel 365

In the [Dynamic Array version of Excel](https://exceljet.net/glossary/dynamic-excel)
, MODE.MULT spills the right number of multiple modes automatically with no #N/A errors

### Notes

*   If supplied numbers do not contain duplicates, MODE.MULT will return #N/A
*   The MODE.MULT function ignores empty cells, and cells that contain boolean values or text.
*   Arguments can be numbers, names, [arrays](https://exceljet.net/glossary/array)
    , or references.

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel MEDIAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20median%20function.png "Excel MEDIAN function")](https://exceljet.net/functions/median-function)

### [MEDIAN Function](https://exceljet.net/functions/median-function)

The Excel MEDIAN function returns the median (middle number) in the supplied set of data. For example, =MEDIAN(1,2,3,4,5) returns 3.

[![Excel MODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")](https://exceljet.net/functions/mode-function)

### [MODE Function](https://exceljet.net/functions/mode-function)

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

[![Excel MODE.SNGL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode.sngl%20function.png "Excel MODE.SNGL function")](https://exceljet.net/functions/mode.sngl-function)

### [MODE.SNGL Function](https://exceljet.net/functions/mode.sngl-function)

The Excel MODE.SNGL function returns the most frequently occurring number in a numeric data set. For example, =MODE.SNGL(1,2,4,4,5,5,5,6) returns 5.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [MEDIAN Function](https://exceljet.net/functions/median-function)
    
*   [MODE Function](https://exceljet.net/functions/mode-function)
    
*   [MODE.SNGL Function](https://exceljet.net/functions/mode.sngl-function)
    

### Links

*   [Microsoft MODE.MULT function documentation](https://support.office.com/en-us/article/mode-mult-function-50fd9464-b2ba-4191-b57a-39446689ae8c)
    

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
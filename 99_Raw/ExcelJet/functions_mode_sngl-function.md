# Excel MODE.SNGL function | Exceljet

**Source:** https://exceljet.net/functions/mode.sngl-function

---

[Skip to main content](https://exceljet.net/functions/mode.sngl-function#main-content)

[](https://exceljet.net/functions/mode.sngl-function#)

*   [Previous](https://exceljet.net/functions/mode.mult-function)
    
*   [Next](https://exceljet.net/functions/norm.dist-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

MODE.SNGL Function
==================

by Dave Bruns · Updated 24 Nov 2021

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[MEDIAN](https://exceljet.net/functions/median-function)

[MODE](https://exceljet.net/functions/mode-function)

[MODE.SNGL](https://exceljet.net/functions/mode.sngl-function)

![Excel MODE.SNGL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20mode.sngl%20function.png "Excel MODE.SNGL function")

Summary
-------

The Excel MODE.SNGL function returns the most frequently occurring number in a numeric data set. For example, =MODE.SNGL(1,2,4,4,5,5,5,6) returns 5.

Purpose 
--------

Get most frequently occurring number

Return value 
-------------

A number representing the mode.

Syntax
------

    =MODE.SNGL(number1,[number2],...)

*   _number1_ - A number or cell reference that refers to numeric values.
*   _number2_ - \[optional\] A number or cell reference that refers to numeric values.

Using the MODE.SNGL function 
-----------------------------

The MODE.SNGL function returns the most frequently occurring number in a set of numeric data. If supplied data does not contain any duplicate numbers, the MODE.SNGL function returns a #N/A error.

The MODE.SNGL function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. Arguments can be a hardcoded constant, a cell reference, or a range, in any combination. MODE.SNGL ignores empty cells, text values, and the logical values TRUE and FALSE. The MODE function will accept up to 254 separate arguments. 

### Examples

In the example shown, the formula in D5 is:

    =MODE.SNGL(B5:B14) // returns 95

MODE.SNGL returns the most frequently occurring number in supplied data. For example,

    =MODE.SNGL(1,2,4,4,5,5,5,6) // returns 5
    =MODE.SNGL(7,8,9,7,9) // returns 7
    

If there are no duplicate numbers, the MODE function returns the #N/A error:

    =MODE.SNGL(7,9,6,5,3,1,0) // returns #N/A
    

_Note: MODE will return a single value even when there are multiple modes, to return a list of all modes, see the [MODE.MULT function](https://exceljet.net/functions/mode.mult-function)
_

### Notes

*   If supplied data does not contain duplicate numbers, MODE.SNGL returns #N/A
*   MODE.SNGL ignores empty cells, the logical values TRUE and FALSE, and [text](https://exceljet.net/glossary/text-value)
    .
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

*   [Microsoft MODE.SNGL function documentation](https://support.office.com/en-us/article/mode-sngl-function-f1267c16-66c6-4386-959f-8fba5f8bb7f8)
    

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
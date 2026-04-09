# Excel SQRT function | Exceljet

**Source:** https://exceljet.net/functions/sqrt-function

---

[Skip to main content](https://exceljet.net/functions/sqrt-function#main-content)

[](https://exceljet.net/functions/sqrt-function#)

*   [Previous](https://exceljet.net/functions/sign-function)
    
*   [Next](https://exceljet.net/functions/sqrtpi-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SQRT Function
=============

by Dave Bruns · Updated 26 Aug 2021

Related functions 
------------------

[POWER](https://exceljet.net/functions/power-function)

![Excel SQRT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sqrt%20function.png "Excel SQRT function")

Summary
-------

The Excel SQRT function returns the square root of a positive number. SQRT returns an error if _number_ is negative.

Purpose 
--------

Find the positive square root of a number

Return value 
-------------

Positive square root

Syntax
------

    =SQRT(number)

*   _number_ - The number to get the square root of.

Using the SQRT function 
------------------------

The Excel SQRT function returns the square root of a positive number. SQRT returns an error if _number_ is negative.

The SQRT function takes one argument, _number_, which must be a numeric value. If _number_ is not numeric, SQRT returns a #VALUE! error. If _number_ is negative, SQRT returns a #NUM! error.

### Examples

    =SQRT(9) // returns 3
    =SQRT(81) // returns 9
    =SQRT(144) // returns 12
    =SQRT(0.25) // returns 0.5
    =SQRT(0) // returns 0
    

### Negative numbers

The SQRT function will return a #NUM! error when _number_ is negative:

    =SQRT(-9) // returns #NUM!
    

To get the square root of a negative number (as if the number was positive), wrap the number in the [ABS function](https://exceljet.net/functions/abs-function)
 like this:

    =SQRT(ABS(-9)) // returns 3
    

### Notes

*   If _number_ is not numeric, SQRT returns a #VALUE! error.
*   If _number_ is negative, SQRT returns a #NUM! error.

SQRT function examples
----------------------

[![Excel formula: Distance formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/distance%20formula.png "Excel formula: Distance formula")](https://exceljet.net/formulas/distance-formula)

### [Distance formula](https://exceljet.net/formulas/distance-formula)

The length of a line can be calculated with the distance formula, which looks like this: Distance is the square root of the change in x squared plus the change in y squared, where two points are given in the form (x 1 , y 1 ) and (x 2 , y 2 ). The distance formula is an example of the Pythagorean...

[![Excel formula: Square root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/square%20root.png "Excel formula: Square root of number")](https://exceljet.net/formulas/square-root-of-number)

### [Square root of number](https://exceljet.net/formulas/square-root-of-number)

The SQRT function is fully automatic and will return the square root of any positive number. For example, to get the square root of 25, you can use: =SQRT(25) // returns 5 To get the square root of 16: =SQRT(16) // returns 4 To get the square root of a number in cell A1: =SQRT(A1) // square root of...

Related functions
-----------------

[![Excel POWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20power%20function.png "Excel POWER function")](https://exceljet.net/functions/power-function)

### [POWER Function](https://exceljet.net/functions/power-function)

The Excel POWER function returns a number raised to a given power. The POWER function is an alternative to the [exponent operator](https://exceljet.net/glossary/math-operators)
 (^).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Square root of number](https://exceljet.net/formulas/square-root-of-number)
    
*   [Distance formula](https://exceljet.net/formulas/distance-formula)
    

### Functions

*   [POWER Function](https://exceljet.net/functions/power-function)
    

### Links

*   [Microsoft SQRT function documentation](https://support.office.com/en-us/article/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf)
    

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
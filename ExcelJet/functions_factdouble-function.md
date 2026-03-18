# Excel FACTDOUBLE function | Exceljet

**Source:** https://exceljet.net/functions/factdouble-function

---

[Skip to main content](https://exceljet.net/functions/factdouble-function#main-content)

[](https://exceljet.net/functions/factdouble-function#)

*   [Previous](https://exceljet.net/functions/fact-function)
    
*   [Next](https://exceljet.net/functions/floor-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

FACTDOUBLE Function
===================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[FACT](https://exceljet.net/functions/fact-function)

![Excel FACTDOUBLE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_factdouble_function.png "Excel FACTDOUBLE function")

Summary
-------

The Excel FACTDOUBLE function returns the double factorial of a number. A double factorial is symbolized by two exclamation marks (!!).

Purpose 
--------

Get double factorial of a number

Return value 
-------------

Calculated double factorial

Syntax
------

    =FACTDOUBLE(number)

*   _number_ - A number greater than or equal to -1.

Using the FACTDOUBLE function 
------------------------------

The FACTDOUBLE function returns the double factorial of a number. A double factorial is calculated differently for even and odd numbers. For an even number, **n**, it's the product of all even integers less than or equal to **n** and greater than or equal to 2. For an odd number, the double factorial is the product of all odd integers less than or equal to **n** and greater than or equal to 1. The double factorial for both zero and -1 are defined as 1. For numbers less than -1, a double factorial is not defined.

FACTDOUBLE takes just one [argument](https://exceljet.net/glossary/function-argument)
, _number_, which should be a positive integer. If _number_ is not an integer, the decimal portion of _number_ will be removed before the factorial is calculated.

### Examples

For even numbers, the double factorial is the product of all even integers less than or equal to _number_ and greater than or equal to 2. For example, the double factorial of 8 is 384:

    =FACTDOUBLE(8)
    =8*6*4*2
    =384
    

For odd numbers, the double factorial is the product of all odd integers less than or equal to _number_ and greater than or equal to 1. The double factorial of 7 is 105:

    =FACTDOUBLE(7)
    =7*5*3*1
    =105
    

The double factorial for zero and -1 are defined as 1:

    =FACTDOUBLE(0) // returns 1
    =FACTDOUBLE(-1) // returns 1
    

### Notes

*   If _number_ is negative, FACTDOUBLE will return the #NUM! error.
*   If _number_ is not an integer it will be truncated to an integer, and then solved.
*   If _number_ is not numeric, FACTDOUBLE will return the #VALUE! error.

Related functions
-----------------

[![Excel FACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fact.png "Excel FACT function")](https://exceljet.net/functions/fact-function)

### [FACT Function](https://exceljet.net/functions/fact-function)

The Excel FACT function returns the factorial of a given number. For example, =FACT(3) returns 6, equivalent to 3 x 2 x 1.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FACT Function](https://exceljet.net/functions/fact-function)
    

### Links

*   [Microsoft FACTDOUBLE function documentation](https://support.office.com/en-us/article/factdouble-function-e67697ac-d214-48eb-b7b7-cce2589ecac8)
    

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
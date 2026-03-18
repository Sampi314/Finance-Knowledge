# Excel QUOTIENT function | Exceljet

**Source:** https://exceljet.net/functions/quotient-function

---

[Skip to main content](https://exceljet.net/functions/quotient-function#main-content)

[](https://exceljet.net/functions/quotient-function#)

*   [Previous](https://exceljet.net/functions/product-function)
    
*   [Next](https://exceljet.net/functions/rand-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

QUOTIENT Function
=================

by Kurt Bruns · Updated 15 Sep 2021

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

![Excel QUOTIENT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20quotient%20operator.png "Excel QUOTIENT function")

Summary
-------

The Excel QUOTIENT function returns the integer portion of division _without_ the remainder. Use QUOTIENT to discard the remainder after division.

Purpose 
--------

Returns the quotient without a remainder.

Return value 
-------------

Integer Number

Syntax
------

    =QUOTIENT(numerator,denominator)

*   _numerator_ - The number to be divided.
*   _denominator_ - The number to divide by.

Using the QUOTIENT function 
----------------------------

The QUOTIENT function returns the integer portion of division _without_ the remainder. You can use QUOTIENT to discard the remainder after division. To perform division _with_ a remainder, use the [division operator](https://exceljet.net/glossary/math-operators)
 "/". To return only the remainder, use the [MOD function](https://exceljet.net/functions/mod-function)
.

QUOTIENT function takes two arguments, _numerator_ and _denominator_. _Numerator_ is the number that should be divided, and _denominator_ is the number to divide _numerator_ by.

### Examples

The number 5 divided by 2 returns 2.5, since 2 goes into 5 two and a half times:

    =5/2 // returns 2.5
    

With the QUOTIENT function, the decimal portion is discarded:

    =QUOTIENT(5,2) // returns 2
    

Other examples:

    =QUOTIENT(3,5) // returns 0
    =QUOTIENT(25,5) // returns 5
    =QUOTIENT(10,3) // returns 3
    

### Notes

*   If _denominator_ is zero (0) or a reference to an empty cell, QUOTIENT returns #DIV!
*   To return only the remainder, use the [MOD function](https://exceljet.net/functions/mod-function)
    .

Related functions
-----------------

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    

### Links

*   [Microsoft QUOTIENT function documentation](https://support.office.com/en-us/article/quotient-function-9f7bf099-2a18-4282-8fa4-65290cc99dee)
    

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
# Excel SIGN function | Exceljet

**Source:** https://exceljet.net/functions/sign-function

---

[Skip to main content](https://exceljet.net/functions/sign-function#main-content)

[](https://exceljet.net/functions/sign-function#)

*   [Previous](https://exceljet.net/functions/roundup-function)
    
*   [Next](https://exceljet.net/functions/sqrt-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SIGN Function
=============

by Dave Bruns · Updated 17 Sep 2021

![Excel SIGN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sign%20function.png "Excel SIGN function")

Summary
-------

The Excel SIGN function returns the sign of a number as +1, -1 or 0. If _number_ is positive, SIGN returns 1. If _number_ is negative, sign returns -1. If _number_ is zero, SIGN returns 0.

Purpose 
--------

Get the sign of a number

Return value 
-------------

One if positive. Negative one if negative. Zero if zero.

Syntax
------

    =SIGN(number)

*   _number_ - The number to get the sign of.

Using the SIGN function 
------------------------

The SIGN function returns the sign of a number as +1, -1 or 0. If _number_ is positive, SIGN returns 1. If _number_ is negative, sign returns -1. If _number_ is zero, SIGN returns 0.

The SIGN function takes one argument, _number_, which must be a numeric value. If _number_ is not numeric, SIGN returns a #VALUE! error.

### Examples

    =SIGN(5) // returns 1
    =SIGN(-3) // returns -1
    =SIGN(0) // returns 0
    

SIGN can be used to change negative numbers into positive values like this. For example, with -3 in cell A1, the formula below returns 3:

    =A1*SIGN(A1)
    =-3*-1
    =3
    

The formula above has no effect on positive numbers, since SIGN will return 1. However, the [ABS function](https://exceljet.net/functions/abs-function)
 provides a simpler solution:

    =ABS(A1) // absolute value of A1
    

### Notes

*   If _number_ is in the range (-∞,0) SIGN(number) will return -1.
*   If _number_ is equal to 0 SIGN(number) will return 0.
*   If _number_ is in the range (0,∞)(number) SIGN will return 1.

SIGN function examples
----------------------

[![Excel formula: Calculate retirement date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20retirement%20date.png "Excel formula: Calculate retirement date")](https://exceljet.net/formulas/calculate-retirement-date)

### [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)

In this example, the goal is to calculate a retirement date at age 60, based on a given birthdate. The simplest way to do this is with the EDATE function. The EDATE function will return a date n months in the future or past when given a date and the number of months to traverse. In this case, we...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)
    

### Links

*   [Microsoft SIGN function documentation](https://support.office.com/en-us/article/sign-function-109c932d-fcdc-4023-91f1-2dd0e916a1d8)
    

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
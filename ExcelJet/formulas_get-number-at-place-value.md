# Get number at place value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-number-at-place-value

---

[Skip to main content](https://exceljet.net/formulas/get-number-at-place-value#main-content)

[](https://exceljet.net/formulas/get-number-at-place-value#)

*   [Previous](https://exceljet.net/formulas/get-integer-part-of-a-number)
    
*   [Next](https://exceljet.net/formulas/round-a-number)
    

[Round](https://exceljet.net/formulas#Round)

Get number at place value
=========================

by Dave Bruns · Updated 10 Jun 2016

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Get number at place value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20number%20at%20place%20value.png "Excel formula: Get number at place value")

Summary
-------

To get the number at a specific place value you can use a formula based on the MOD function. By place value, we mean hundred thousands, ten thousands, thousands, hundreds, tens, ones, etc.

In the example shown, the formula in cell D8 is:

    =MOD(B8,C8*10) - MOD(B8,C8)
    

The place is thousands (1000), and the result is 3000.

Generic formula
---------------

    =MOD(number,place*10) - MOD(number,place)

Explanation 
------------

The MOD function performs the modulo operation. It takes a number and a divisor and returns the remainder after division.

In this formula, we subtract one MOD result from another.

For the first MOD, we use the number with a divisor that equals the place value we want times 10. For the second MOD, we use the number with a divisor equals to the place value we seek. The formula is solved like this:

    =MOD(B8,C8*10)-MOD(B8,C8)
    =MOD(123456,1000*10)-MOD(123456,1000)
    =3456-456
    =3000
    

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
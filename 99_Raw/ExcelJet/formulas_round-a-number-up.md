# Round a number up - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-a-number-up

---

[Skip to main content](https://exceljet.net/formulas/round-a-number-up#main-content)

[](https://exceljet.net/formulas/round-a-number-up#)

*   [Previous](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    
*   [Next](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)
    

[Round](https://exceljet.net/formulas#Round)

Round a number up
=================

by Dave Bruns · Updated 24 Sep 2020

Related functions 
------------------

[ROUNDUP](https://exceljet.net/functions/roundup-function)

![Excel formula: Round a number up](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20a%20number%20up.png "Excel formula: Round a number up")

Summary
-------

To round a number to round up, regardless of its value, you can use the [ROUNDUP function](https://exceljet.net/functions/roundup-function)
 with a given number of digits. In the example shown, the formula in cell D7 is:

    =ROUNDUP(B7,C7)
    

Generic formula
---------------

    =ROUNDUP(number,digits)

Explanation 
------------

The [ROUNDUP function](https://exceljet.net/functions/roundup-function)
 rounds a number _up_ to a given number of places. The number of places is controlled by the number of digits provided in the second argument (_num\_digits_). For example, these formulas round the number 5.13 up to 1 and zero places:

    =ROUNDUP(5.13,1) // returns 5.2
    =ROUNDUP(5.13,0) // returns 6
    

In the example, the formula in cell D7 is

    =ROUNDUP(B7,C7)
    

This tells Excel to take the value in B7 (PI) and round it to the number of digits in cell C7 (3) with a result of 3.142 Notice that even though the number in the 4th position to the right of the decimal is 1, it is still rounded up to 2.

In the table, the ROUNDUP function is used to round the same number (pi, created with the [PI function](https://exceljet.net/functions/pi-function)
) to a decreasing number of digits, starting at 4 and moving down past zero to -1. Note that positive numbers round to the right of the decimal point, while digits less than or equal to zero round to the left.

You can see that ROUNDUP is a rather heavy-handed function, so use with care. You can use the [CEILING function](https://exceljet.net/functions/ceiling-function)
 to round a number up to a given multiple. If you want to discard the decimal portion of a number, you can use the [TRUNC function](https://exceljet.net/functions/trunc-function)
.

Related formulas
----------------

[![Excel formula: Round a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20a%20number.png "Excel formula: Round a number")](https://exceljet.net/formulas/round-a-number)

### [Round a number](https://exceljet.net/formulas/round-a-number)

The ROUND function rounds a number to a given number of places. The number of places is set by the number of digits provided in the second argument ( num\_digits ). For example, the formulas below round the number 5.86 to 1 and zero places: =ROUND(5.86,1) // returns 5.9 =ROUND(5.86,0) // returns 6...

Related functions
-----------------

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Round a number](https://exceljet.net/formulas/round-a-number)
    

### Functions

*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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
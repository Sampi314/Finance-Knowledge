# Round a number down - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-a-number-down

---

[Skip to main content](https://exceljet.net/formulas/round-a-number-down#main-content)

[](https://exceljet.net/formulas/round-a-number-down#)

*   [Previous](https://exceljet.net/formulas/round-a-number)
    
*   [Next](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)
    

[Round](https://exceljet.net/formulas#Round)

Round a number down
===================

by Dave Bruns · Updated 24 Sep 2020

Related functions 
------------------

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

![Excel formula: Round a number down](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20a%20number%20down.png "Excel formula: Round a number down")

Summary
-------

To round a number to round down, regardless of its value, you can use the [ROUNDDOWN function](https://exceljet.net/functions/rounddown-function)
 with a specified number of digits. In the example shown, the formula in cell D7 is

    =ROUNDDOWN(B7,C7)
    

Generic formula
---------------

    =ROUNDDOWN(number,digits)

Explanation 
------------

The [ROUNDDOWN function](https://exceljet.net/functions/rounddown-function)
 rounds a number _down_ to a given number of places. The number of places is controlled by the number of digits provided in the second argument (_num\_digits_). For example, these formulas round the number 5.89 down to 1 and zero places:

    =ROUNDDOWN(5.89,1) // returns 5.8
    =ROUNDDOWN(5.86,0) // returns 5
    

In the example shown, the formula in cell D7 is

    =ROUNDDOWN(B7,C7)
    

This tells Excel to take the value in B7 (1999.9985) and round it to the number of digits in cell C7 (2) with a result of 1999.99 Notice that even though the number in the 3rd position to the right of the decimal is 8, it is still rounded _down_.

In the table, the ROUNDDOWN function is used to round the same number (1999.9985) to a decreasing number of digits, starting at 2 and moving down past zero to -3. Note that positive numbers round to the right of the decimal point, while digits specified less than or equal to zero round to the left. At each step, numbers that would normally be rounded up are rounded down.

You can see that ROUNDDOWN is a rather heavy handed function, so use it carefully. You can use the [FLOOR function](https://exceljet.net/functions/floor-function)
 to round a number down to a given multiple. If you want to discard the decimal portion of a number, you can use the [TRUNC function](https://exceljet.net/functions/trunc-function)
.

Related formulas
----------------

[![Excel formula: Round a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20a%20number.png "Excel formula: Round a number")](https://exceljet.net/formulas/round-a-number)

### [Round a number](https://exceljet.net/formulas/round-a-number)

The ROUND function rounds a number to a given number of places. The number of places is set by the number of digits provided in the second argument ( num\_digits ). For example, the formulas below round the number 5.86 to 1 and zero places: =ROUND(5.86,1) // returns 5.9 =ROUND(5.86,0) // returns 6...

[![Excel formula: Round a number up](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up.png "Excel formula: Round a number up")](https://exceljet.net/formulas/round-a-number-up)

### [Round a number up](https://exceljet.net/formulas/round-a-number-up)

The ROUNDUP function rounds a number up to a given number of places. The number of places is controlled by the number of digits provided in the second argument ( num\_digits ). For example, these formulas round the number 5.13 up to 1 and zero places: =ROUNDUP(5.13,1) // returns 5.2 =ROUNDUP(5.13,0...

Related functions
-----------------

[![Excel ROUNDDOWN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rounddown%20function.png "Excel ROUNDDOWN function")](https://exceljet.net/functions/rounddown-function)

### [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)

The Excel ROUNDDOWN function returns a number rounded down to a given number of places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDDOWN rounds _all numbers down_....

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
    
*   [Round a number up](https://exceljet.net/formulas/round-a-number-up)
    

### Functions

*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    

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
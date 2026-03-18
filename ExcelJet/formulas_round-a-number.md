# Round a number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-a-number

---

[Skip to main content](https://exceljet.net/formulas/round-a-number#main-content)

[](https://exceljet.net/formulas/round-a-number#)

*   [Previous](https://exceljet.net/formulas/get-number-at-place-value)
    
*   [Next](https://exceljet.net/formulas/round-a-number-down)
    

[Round](https://exceljet.net/formulas#Round)

Round a number
==============

by Dave Bruns · Updated 23 Sep 2020

Related functions 
------------------

[ROUND](https://exceljet.net/functions/round-function)

![Excel formula: Round a number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Round%20a%20number.png "Excel formula: Round a number")

Summary
-------

To round a number up or down to the nearest specified digit, you can use the [ROUND function](https://exceljet.net/functions/round-function)
 with a specified number of digits. In the example shown, the formula in cell D6, copied down, is:

    =ROUND(B6,C6)
    

Generic formula
---------------

    =ROUND(number,digits)

Explanation 
------------

The [ROUND function](https://exceljet.net/functions/round-function)
 rounds a number to a given number of places. The number of places is set by the number of digits provided in the second argument (_num\_digits_). For example, the formulas below round the number 5.86 to 1 and zero places:

    =ROUND(5.86,1) // returns 5.9
    =ROUND(5.86,0) // returns 6
    

In the example shown, we are rounding the values in column B (which are created with the [PI function](https://exceljet.net/functions/pi-function)
) using the numbers in column B for digits. The formula in cell D6 is

    =ROUND(B6,C6)
    

This tells Excel to take the value in B6 (PI) and round it to the number of digits in cell C6 (4) with a result of 3.1416

In the table, the ROUND function is used to round the same number (PI) to a decreasing number of digits, starting at 4 and moving down past zero to -1. Notice that digits greater than zero round to the right of the decimal point, and digits less than or equal to zero round to the left.

Related formulas
----------------

[![Excel formula: Round a number up](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up.png "Excel formula: Round a number up")](https://exceljet.net/formulas/round-a-number-up)

### [Round a number up](https://exceljet.net/formulas/round-a-number-up)

The ROUNDUP function rounds a number up to a given number of places. The number of places is controlled by the number of digits provided in the second argument ( num\_digits ). For example, these formulas round the number 5.13 up to 1 and zero places: =ROUNDUP(5.13,1) // returns 5.2 =ROUNDUP(5.13,0...

[![Excel formula: Round a number down](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20down.png "Excel formula: Round a number down")](https://exceljet.net/formulas/round-a-number-down)

### [Round a number down](https://exceljet.net/formulas/round-a-number-down)

The ROUNDDOWN function rounds a number down to a given number of places. The number of places is controlled by the number of digits provided in the second argument ( num\_digits ). For example, these formulas round the number 5.89 down to 1 and zero places: =ROUNDDOWN(5.89,1) // returns 5.8 =...

[![Excel formula: Round a number to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20to%20nearest%20multiple.png "Excel formula: Round a number to nearest multiple")](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

### [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

The MROUND function rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the significance argument. If the number is already an exact multiple, no rounding occurs and the original number is returned. You can use MROUND to round prices, times, instrument...

Related functions
-----------------

[![Excel ROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20round%20function.png "Excel ROUND function")](https://exceljet.net/functions/round-function)

### [ROUND Function](https://exceljet.net/functions/round-function)

The Excel ROUND function returns a number rounded to a given number of digits. The ROUND function can round to the right or left of the decimal point.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Round a number up](https://exceljet.net/formulas/round-a-number-up)
    
*   [Round a number down](https://exceljet.net/formulas/round-a-number-down)
    
*   [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    

### Functions

*   [ROUND Function](https://exceljet.net/functions/round-function)
    

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
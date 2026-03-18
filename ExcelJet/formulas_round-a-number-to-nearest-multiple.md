# Round a number to nearest multiple - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-a-number-to-nearest-multiple

---

[Skip to main content](https://exceljet.net/formulas/round-a-number-to-nearest-multiple#main-content)

[](https://exceljet.net/formulas/round-a-number-to-nearest-multiple#)

*   [Previous](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)
    
*   [Next](https://exceljet.net/formulas/round-a-number-up)
    

[Round](https://exceljet.net/formulas#Round)

Round a number to nearest multiple
==================================

by Dave Bruns · Updated 23 Sep 2020

Related functions 
------------------

[MROUND](https://exceljet.net/functions/mround-function)

![Excel formula: Round a number to nearest multiple](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20a%20number%20to%20nearest%20multiple.png "Excel formula: Round a number to nearest multiple")

Summary
-------

To round a number to the nearest given multiple (i.e. nearest dollar, nearest 5 dollars, etc.) you can use the [MROUND function](https://exceljet.net/functions/mround-function)
. In the example  shown, the formula in D6 is:

    =MROUND(B6,C6)
    

Generic formula
---------------

    =MROUND(number,multiple)

Explanation 
------------

The [MROUND function](https://exceljet.net/functions/mround-function)
 rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the _significance_ argument. If the number is already an exact multiple, no rounding occurs and the original number is returned. You can use MROUND to round prices, times, instrument readings or any other numeric value.

In the example shown, we are using MROUND to round the price in column B using the multiple in column C. The formula in cell D6, copied down the table, is:

    =MROUND(B6,C6)
    

This tells Excel to take the value in B6 ($63.39) and round it to the nearest multiple of the value in C6 (5). The result in D5 is $65.00, since 65 is the nearest multiple of 5 to 63.39. In the following rows of the table, the same number is rounded using different multiples.

Note that MROUND always rounds to the nearest value using the specified multiple. If you need to round either up or down using a multiple, use the [CEILING](https://exceljet.net/functions/ceiling-function)
 or [FLOOR](https://exceljet.net/functions/floor-function)
 functions.

Related formulas
----------------

[![Excel formula: Round a number up to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up%20to%20nearest%20multiple.png "Excel formula: Round a number up to nearest multiple")](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

### [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

The Excel CEILING function rounds a number up to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. CEILING works like the MROUND function , but unlike MROUND, which rounds to the...

[![Excel formula: Round a number down to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20down%20to%20nearest%20multiple.png "Excel formula: Round a number down to nearest multiple")](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)

### [Round a number down to nearest multiple](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)

The Excel FLOOR function rounds a number down to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. FLOOR works like the MROUND function , but unlike MROUND, which rounds to the nearest...

Related functions
-----------------

[![Excel MROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mround%20function.png "Excel MROUND function")](https://exceljet.net/functions/mround-function)

### [MROUND Function](https://exceljet.net/functions/mround-function)

The Excel MROUND function returns a number rounded to a given multiple. MROUND will round a number up or down, depending on the nearest multiple.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)
    
*   [Round a number down to nearest multiple](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)
    

### Functions

*   [MROUND Function](https://exceljet.net/functions/mround-function)
    

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
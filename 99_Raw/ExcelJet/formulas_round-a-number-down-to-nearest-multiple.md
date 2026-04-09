# Round a number down to nearest multiple - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple

---

[Skip to main content](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple#main-content)

[](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple#)

*   [Previous](https://exceljet.net/formulas/round-a-number-down)
    
*   [Next](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    

[Round](https://exceljet.net/formulas#Round)

Round a number down to nearest multiple
=======================================

by Dave Bruns · Updated 23 Sep 2020

Related functions 
------------------

[FLOOR](https://exceljet.net/functions/floor-function)

![Excel formula: Round a number down to nearest multiple](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20a%20number%20down%20to%20nearest%20multiple.png "Excel formula: Round a number down to nearest multiple")

Summary
-------

To round a number _down_ to the _nearest specified multiple_ (i.e. round a price down to the nearest dollar) you can use the [FLOOR function](https://exceljet.net/functions/floor-function)
. In the example shown, the formula in cell D6 is:

    =FLOOR(B6,C6)
    

Generic formula
---------------

    =FLOOR(number,multiple)

Explanation 
------------

The Excel [FLOOR function](https://exceljet.net/functions/floor-function)
 rounds a number _down_ to a given multiple. The multiple to use for rounding is given as the second argument (_significance_). If the number is already an exact multiple, no rounding occurs.  FLOOR works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but unlike MROUND, which rounds to the _nearest_ multiple, FLOOR always rounds _down_ to the given multiple.

In the example shown, the formula in cell D6 is

    =FLOOR(B6,C6)
    

This tells Excel to take the value in B6 ($33.39 ) and round it down to the nearest multiple of the value in C6 (5). The result is $30.00, since 30 is nearest multiple of 5 below 33.39. Likewise, in cell D7, we get 30 when rounding down using a multiple of 10.

You can use FLOOR to round prices, times, instrument readings or any other numeric value.

FLOOR rounds _down_ using the multiple supplied. You can use the [MROUND function](https://exceljet.net/functions/mround-function)
 to round to the _nearest multiple_ and the [CEILING function](https://exceljet.net/functions/ceiling-function)
 to round _up_ to a multiple.

Related formulas
----------------

[![Excel formula: Round a number to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20to%20nearest%20multiple.png "Excel formula: Round a number to nearest multiple")](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

### [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

The MROUND function rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the significance argument. If the number is already an exact multiple, no rounding occurs and the original number is returned. You can use MROUND to round prices, times, instrument...

[![Excel formula: Round a number up to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up%20to%20nearest%20multiple.png "Excel formula: Round a number up to nearest multiple")](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

### [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

The Excel CEILING function rounds a number up to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. CEILING works like the MROUND function , but unlike MROUND, which rounds to the...

[![Excel formula: Round a price to end in .99](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20a%20price%20to%20end%20in%20nearest%20.99.png "Excel formula: Round a price to end in .99")](https://exceljet.net/formulas/round-a-price-to-end-in-99)

### [Round a price to end in .99](https://exceljet.net/formulas/round-a-price-to-end-in-99)

In the example shown, the goal is to round a price to the nearest value ending in .99. So, for example, if a price is currently $5.31, the result should be $4.99. The best way to think about the problem is to restate it as "round a price to the nearest whole dollar, less 1 penny". In other words,...

Related functions
-----------------

[![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")](https://exceljet.net/functions/floor-function)

### [FLOOR Function](https://exceljet.net/functions/floor-function)

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    
*   [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)
    
*   [Round a price to end in .99](https://exceljet.net/formulas/round-a-price-to-end-in-99)
    

### Functions

*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    

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
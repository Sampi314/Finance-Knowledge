# Round a number up to nearest multiple - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple

---

[Skip to main content](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple#main-content)

[](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple#)

*   [Previous](https://exceljet.net/formulas/round-a-number-up)
    
*   [Next](https://exceljet.net/formulas/round-a-number-up-to-next-half)
    

[Round](https://exceljet.net/formulas#Round)

Round a number up to nearest multiple
=====================================

by Dave Bruns · Updated 25 Sep 2020

Related functions 
------------------

[CEILING](https://exceljet.net/functions/ceiling-function)

![Excel formula: Round a number up to nearest multiple](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20a%20number%20up%20to%20nearest%20multiple.png "Excel formula: Round a number up to nearest multiple")

Summary
-------

To round a number _up_ to the _nearest specified multiple_ (i.e. round a price up to the nearest dollar) you can use the [CEILING function](https://exceljet.net/functions/ceiling-function)
. In the example shown, the formula in cell D6 is:

    =CEILING(B6,C6)
    

Generic formula
---------------

    =CEILING(number,multiple)

Explanation 
------------

The Excel [CEILING function](https://exceljet.net/functions/ceiling-function)
 rounds a number _up_ to a given multiple. The multiple to use for rounding is given as the second argument (_significance_). If the number is already an exact multiple, no rounding occurs.  CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but unlike MROUND, which rounds to the _nearest_ multiple, CEILING always rounds _up_ to the given multiple.

In the example shown, the formula in cell D6 is

    =CEILING(B6,C6)
    

This tells Excel to take the value in B6 ($33.39 ) and round it to the nearest multiple of the value in C6 (5). The result is $35.00, since 35 is the next multiple of 5 after 33.39. In cell D10, we are rounding the same number, 33.39 up to the nearest multiple of 1 and get 34.00.

You can use CEILING to round prices, times, instrument readings or any other numeric value.

CEILING rounds _up_ using the multiple supplied. You can use the [MROUND function](https://exceljet.net/functions/mround-function)
 to round to the _nearest multiple_ and the [FLOOR function](https://exceljet.net/functions/floor-function)
 to round _down_ to a multiple.

Related formulas
----------------

[![Excel formula: Round by bundle size](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round_by_bundle_size_0.png "Excel formula: Round by bundle size")](https://exceljet.net/formulas/round-by-bundle-size)

### [Round by bundle size](https://exceljet.net/formulas/round-by-bundle-size)

In this example, the context is that a certain number of items are needed and the items are only available in bundles of a set size. The goal is to calculate the number of bundles needed based on the items in each bundle, and the number of items needed. For example: If you need 6 items, and the...

[![Excel formula: Round a number to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20to%20nearest%20multiple.png "Excel formula: Round a number to nearest multiple")](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

### [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

The MROUND function rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the significance argument. If the number is already an exact multiple, no rounding occurs and the original number is returned. You can use MROUND to round prices, times, instrument...

[![Excel formula: Round a number down to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20down%20to%20nearest%20multiple.png "Excel formula: Round a number down to nearest multiple")](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)

### [Round a number down to nearest multiple](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)

The Excel FLOOR function rounds a number down to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. FLOOR works like the MROUND function , but unlike MROUND, which rounds to the nearest...

Related functions
-----------------

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Round by bundle size](https://exceljet.net/formulas/round-by-bundle-size)
    
*   [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    
*   [Round a number down to nearest multiple](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)
    

### Functions

*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    

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
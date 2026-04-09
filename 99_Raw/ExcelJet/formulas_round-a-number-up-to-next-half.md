# Round a number up to next half - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-a-number-up-to-next-half

---

[Skip to main content](https://exceljet.net/formulas/round-a-number-up-to-next-half#main-content)

[](https://exceljet.net/formulas/round-a-number-up-to-next-half#)

*   [Previous](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)
    
*   [Next](https://exceljet.net/formulas/round-a-price-to-end-in-99)
    

[Round](https://exceljet.net/formulas#Round)

Round a number up to next half
==============================

by Dave Bruns · Updated 25 Sep 2020

Related functions 
------------------

[CEILING](https://exceljet.net/functions/ceiling-function)

![Excel formula: Round a number up to next half](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20a%20number%20up%20to%20next%20half.png "Excel formula: Round a number up to next half")

Summary
-------

To round a number _up_ to the next half, you can use the CEILING function, which always rounds up based on a given multiple. In the example shown, the formula in C5 is:

    =CEILING(B5,0.5)

Generic formula
---------------

    =CEILING(number,0.5)

Explanation 
------------

The Excel [CEILING function](https://exceljet.net/functions/ceiling-function)
 rounds a number _up_ to a given multiple. The multiple to use for rounding is given as the second argument (_significance_). If the number is already an exact multiple, no rounding occurs. 

In this example, we want to round up to the nearest half, so we provide 0.5 to CEILING as the multiple. In the example shown, the formula in C5 is:

    =CEILING(B5,0.5) // returns 1.5
    

Even though the value in B5 is 1.1, CEILING rounds up to the next multiple of .5, which is 1.5.

CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but unlike MROUND, which rounds to the _nearest_ multiple, CEILING always rounds _up_ to the given multiple. If you want to round down to the nearest half, you can use the [FLOOR function](https://exceljet.net/functions/floor-function)
.

Related formulas
----------------

[![Excel formula: Round a number up to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up%20to%20nearest%20multiple.png "Excel formula: Round a number up to nearest multiple")](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

### [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

The Excel CEILING function rounds a number up to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. CEILING works like the MROUND function , but unlike MROUND, which rounds to the...

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

*   [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)
    

### Functions

*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    

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
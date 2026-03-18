# Round a price to end in .99 - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-a-price-to-end-in-99

---

[Skip to main content](https://exceljet.net/formulas/round-a-price-to-end-in-99#main-content)

[](https://exceljet.net/formulas/round-a-price-to-end-in-99#)

*   [Previous](https://exceljet.net/formulas/round-a-number-up-to-next-half)
    
*   [Next](https://exceljet.net/formulas/round-by-bundle-size)
    

[Round](https://exceljet.net/formulas#Round)

Round a price to end in .99
===========================

by Dave Bruns · Updated 22 Jul 2020

Related functions 
------------------

[ROUND](https://exceljet.net/functions/round-function)

[MROUND](https://exceljet.net/functions/mround-function)

![Excel formula: Round a price to end in .99](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Round%20a%20price%20to%20end%20in%20nearest%20.99.png "Excel formula: Round a price to end in .99")

Summary
-------

To round prices to end in the nearest, .99 value, you can use the [ROUND function](https://exceljet.net/functions/round-function)
 then subtract .01. In the example shown, the formula in C6 is:

    =ROUND(B6,0)-0.01
    

which rounds the value in B6 to the nearest whole dollar, then subtracts .01.

Generic formula
---------------

    =ROUND(price,0)-0.01

Explanation 
------------

In the example shown, the goal is to round a price to the nearest value ending in .99. So, for example, if a price is currently $5.31, the result should be $4.99. The best way to think about the problem is to restate it as "round a price to the nearest whole dollar, less 1 penny". In other words, the solution works in two parts: (1) round and (2) subtract.

For rounding, we use the ROUND function, with the _num\_digits_ argument set to zero (0) for no decimal places:

    =ROUND(B6,0) // nearest dollar
    

The ROUND function with a zero will round to the nearest whole dollar. Once rounded, the formula simply subtracts 0.01 to get a .99 value. The formula in C6, copied down, is:

    =ROUND(B6,0)-0.01
    

With the value in B6 of 63.39, the formula is solved like this:

    =ROUND(B6,0)-0.01
    =ROUND(63.39,0)-0.01
    =63-0.01
    =62.99
    

### With MROUND

Other option for rounding in this case is the [MROUND function](https://exceljet.net/functions/mround-function)
. Instead of rounding to a specific number of decimal places, the MROUND rounds to the nearest multiple, provided as the _significance_ argument. This means we can use MROUND to round to the nearest dollar by providing a multiple of 1 like this:

    =MROUND(B6,1) // nearest dollar
    

The equivalent formula is then:

    =MROUND(B6,1)-0.01
    

To force rounding _up_ or _down_ to the nearest multiple, see the [CEILING](https://exceljet.net/functions/ceiling-function)
 and [FLOOR](https://exceljet.net/functions/floor-function)
 functions.

Related formulas
----------------

[![Excel formula: Round price to end in .45 or .95](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20price%20to%20end%20in%2045%20or%2095.png "Excel formula: Round price to end in .45 or .95")](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95)

### [Round price to end in .45 or .95](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95)

The key to solving this problem is to realize that the solution requires a specific kind of rounding. We can't just round to the "nearest" .45 or .95 value. In fact, the first step is to round up to the nearest half dollar (.50). The second step is to subtract 5 cents ($0.05). To round up to the...

[![Excel formula: Round a number to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20to%20nearest%20multiple.png "Excel formula: Round a number to nearest multiple")](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

### [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

The MROUND function rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the significance argument. If the number is already an exact multiple, no rounding occurs and the original number is returned. You can use MROUND to round prices, times, instrument...

[![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

### [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value. You can also express 15 minutes in a formula with this...

Related functions
-----------------

[![Excel ROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20round%20function.png "Excel ROUND function")](https://exceljet.net/functions/round-function)

### [ROUND Function](https://exceljet.net/functions/round-function)

The Excel ROUND function returns a number rounded to a given number of digits. The ROUND function can round to the right or left of the decimal point.

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

*   [Round price to end in .45 or .95](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95)
    
*   [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    
*   [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    

### Functions

*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [MROUND Function](https://exceljet.net/functions/mround-function)
    

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
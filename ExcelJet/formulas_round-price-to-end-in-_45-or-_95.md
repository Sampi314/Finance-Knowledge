# Round price to end in .45 or .95 - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95

---

[Skip to main content](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95#main-content)

[](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95#)

*   [Previous](https://exceljet.net/formulas/round-number-to-n-significant-figures)
    
*   [Next](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    

[Round](https://exceljet.net/formulas#Round)

Round price to end in .45 or .95
================================

by Dave Bruns · Updated 23 Jul 2020

Related functions 
------------------

[CEILING](https://exceljet.net/functions/ceiling-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6209/download?token=6dUU_HY4)
 (13.5 KB)

![Excel formula: Round price to end in .45 or .95](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Round%20price%20to%20end%20in%2045%20or%2095.png "Excel formula: Round price to end in .45 or .95")

Summary
-------

To round prices to end in .45 or .95, depending on whether the original price ends above or below .50, you can use the [CEILING function](https://exceljet.net/functions/ceiling-function)
. In the example shown, the formula in C6 is:

    =CEILING(B5,0.5)-0.05
    

which rounds prices as shown in the screenshot.

### Rounding rules

In the example shown, the goal is to round prices to end in either .45 or .95, following these rules:

1.  If a price is already a whole dollar, the result should be the previous whole dollar + .95. For example, $3.00 becomes $2.95.
2.  If a price ends in .50 or less, the result should be the current whole dollar + .45. For example, $4.31 becomes $4.45.
3.  If a price ends in .51 or more, the result should be the current whole dollar + .95. For example, $5.63 becomes $5.95.

Generic formula
---------------

    =CEILING(price,0.5)-0.05

Explanation 
------------

The key to solving this problem is to realize that the solution requires a specific kind of rounding. We can't just round to the "nearest" .45 or .95 value. In fact, the first step is to round _up_ to the nearest _half_ dollar (.50). The second step is to subtract 5 cents ($0.05).

To round up to the nearest half dollar, we use the CEILING function, with the _significance_ argument set to .5:

    =CEILING(B5,0.5) // round up to next half dollar
    

This will round the original price up to the next half dollar. For example, $4.31 will become $4.50, and $5.72 will become $6.00. Importantly, if a price already ends in .00 or .50, it will remain unchanged (i.e. a price of $4.00 or $4.50 is not affected).

Once rounded, the formula simply subtracts 0.05 to get a .45 or .95 result. The formula in C5, copied down, is:

    =CEILING(B5,0.5)-0.05
    

When B5 contains $17.01, the formula is solved like this:

    =CEILING(B5,0.5)-0.05
    =CEILING(17.01,0.5)-0.05
    =17.50-0.05
    =17.45
    

### About CEILING

CEILING is one of 8 rounding functions in Excel. You can use CEILING to do things like:

*   Round numbers up to multiples of 25
*   Round time up to 15 minute multiples
*   Round materials up to the next whole unit

The MROUND function and FLOOR function can also round to a given multiple, but the behavior is different from CEILING:

*   [CEILING](https://exceljet.net/functions/ceiling-function)
     rounds _up_ to the next multiple
*   [FLOOR](https://exceljet.net/functions/floor-function)
     rounds _down_ to the previous multiple
*   [MROUND](https://exceljet.net/functions/mround-function)
     rounds to the _nearest_ multiple

Related formulas
----------------

[![Excel formula: Round a price to end in .99](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20a%20price%20to%20end%20in%20nearest%20.99.png "Excel formula: Round a price to end in .99")](https://exceljet.net/formulas/round-a-price-to-end-in-99)

### [Round a price to end in .99](https://exceljet.net/formulas/round-a-price-to-end-in-99)

In the example shown, the goal is to round a price to the nearest value ending in .99. So, for example, if a price is currently $5.31, the result should be $4.99. The best way to think about the problem is to restate it as "round a price to the nearest whole dollar, less 1 penny". In other words,...

[![Excel formula: Round a number to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20to%20nearest%20multiple.png "Excel formula: Round a number to nearest multiple")](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

### [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

The MROUND function rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the significance argument. If the number is already an exact multiple, no rounding occurs and the original number is returned. You can use MROUND to round prices, times, instrument...

[![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

### [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value. You can also express 15 minutes in a formula with this...

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

*   [Round a price to end in .99](https://exceljet.net/formulas/round-a-price-to-end-in-99)
    
*   [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    
*   [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    

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
# Round to nearest 5 - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-to-nearest-5

---

[Skip to main content](https://exceljet.net/formulas/round-to-nearest-5#main-content)

[](https://exceljet.net/formulas/round-to-nearest-5#)

*   [Previous](https://exceljet.net/formulas/round-to-nearest-1000)
    
*   [Next](https://exceljet.net/formulas/add-business-days-to-date)
    

[Round](https://exceljet.net/formulas#Round)

Round to nearest 5
==================

by Dave Bruns · Updated 30 Aug 2016

Related functions 
------------------

[MROUND](https://exceljet.net/functions/mround-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[FLOOR](https://exceljet.net/functions/floor-function)

![Excel formula: Round to nearest 5](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20to%20nearest%205.png "Excel formula: Round to nearest 5")

Summary
-------

If you need to round a number to the nearest multiple of 5, you can use the MROUND function and supply 5 for number of digits.

Generic formula
---------------

    =MROUND(number,5)

Explanation 
------------

In the example, cell C6 contains this formula:

    =MROUND(B6,5)
    

The value in B6 is 17 and the result is 15 since 15 is the nearest multiple of 5 to 17.

### Other multiples

As you'd expect, you can use MROUND to round to other multiples as well:

    =MROUND(number,10) // nearest multiple of 10
    =MROUND(number,50) // nearest multiple of 50
    =MROUND(number,.05) // nearest 5 cents
    

And so on.

### Force up or down

You can use the [CEILING function](https://exceljet.net/functions/ceiling-function)
 to force rounding up to the nearest multiple and the [FLOOR function](https://exceljet.net/functions/floor-function)
 to force rounding down to the nearest multiple.

Related formulas
----------------

[![Excel formula: Round to nearest 1000](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20to%20nearest%201000.png "Excel formula: Round to nearest 1000")](https://exceljet.net/formulas/round-to-nearest-1000)

### [Round to nearest 1000](https://exceljet.net/formulas/round-to-nearest-1000)

In the example, cell C6 contains this formula: =ROUND(B6,-3) The value in B6 is 1,234,567 and the result is 1,235,000. With the ROUND function, negative numbers for the second argument round to the left of the decimal and positive numbers round to the right of the decimal. In this case, by...

Related functions
-----------------

[![Excel MROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mround%20function.png "Excel MROUND function")](https://exceljet.net/functions/mround-function)

### [MROUND Function](https://exceljet.net/functions/mround-function)

The Excel MROUND function returns a number rounded to a given multiple. MROUND will round a number up or down, depending on the nearest multiple.

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

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

*   [Round to nearest 1000](https://exceljet.net/formulas/round-to-nearest-1000)
    

### Functions

*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    

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
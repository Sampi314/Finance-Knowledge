# Round time to nearest 15 minutes - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-time-to-nearest-15-minutes

---

[Skip to main content](https://exceljet.net/formulas/round-time-to-nearest-15-minutes#main-content)

[](https://exceljet.net/formulas/round-time-to-nearest-15-minutes#)

*   [Previous](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95)
    
*   [Next](https://exceljet.net/formulas/round-to-nearest-1000)
    

[Round](https://exceljet.net/formulas#Round)

Round time to nearest 15 minutes
================================

by Dave Bruns · Updated 16 Oct 2018

Related functions 
------------------

[MROUND](https://exceljet.net/functions/mround-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[FLOOR](https://exceljet.net/functions/floor-function)

![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")

Summary
-------

To round a time to the nearest 15 minute interval, you can use the MROUND function, which rounds based on a supplied multiple. In the example shown, the formula in C6 is:

    =MROUND(B6,"0:15")
    

Generic formula
---------------

    =MROUND(time,"0:15")

Explanation 
------------

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value.

You can also express 15 minutes in a formula with this formula:

    =15/(60*24)
    

The formula above divides 15 by 1440, which is the number of minutes in one day. So, to Excel, these formulas are identical:

    =MROUND(B6,"0:15")
    =MROUND(B6,15/(60*24))
    

### Round to other time intervals

As you would expect, you can use the same formula to round to different time intervals. To round to the nearest 30 minutes, or nearest 1 hour, use these formulas

    =MROUND(time,"0:30") //nearest 30 minutes
    =MROUND(time,"1:00") //nearest 1 hour
    

### Always round up

To always round up to the nearest 15 minutes, you can use the [CEILING function](https://exceljet.net/functions/ceiling-function)
:

    =CEILING(B6,"0:15")
    

Like MROUND, the CEILING function rounds to a nearest multiple. The difference is that CEILING _always_ rounds up. The [FLOOR function](https://exceljet.net/functions/floor-function)
 can be used to always round down

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
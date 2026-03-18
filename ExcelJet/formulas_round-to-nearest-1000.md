# Round to nearest 1000 - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-to-nearest-1000

---

[Skip to main content](https://exceljet.net/formulas/round-to-nearest-1000#main-content)

[](https://exceljet.net/formulas/round-to-nearest-1000#)

*   [Previous](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    
*   [Next](https://exceljet.net/formulas/round-to-nearest-5)
    

[Round](https://exceljet.net/formulas#Round)

Round to nearest 1000
=====================

by Dave Bruns · Updated 13 Jul 2017

Related functions 
------------------

[ROUND](https://exceljet.net/functions/round-function)

![Excel formula: Round to nearest 1000](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round%20to%20nearest%201000.png "Excel formula: Round to nearest 1000")

Summary
-------

If you need to round a number to the nearest 1000, you can use the ROUND function and supply -3 for number of digits.

Generic formula
---------------

    =ROUND(number,-3)

Explanation 
------------

In the example, cell C6 contains this formula:

    =ROUND(B6,-3)
    

The value in B6 is 1,234,567 and the result is 1,235,000.

With the ROUND function, negative numbers for the second argument round to the left of the decimal and positive numbers round to the right of the decimal.

In this case, by supplying -3, we are telling ROUND to round the number to the 3rd place on the left – the 1000's place.

Related formulas
----------------

[![Excel formula: Round a number to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20to%20nearest%20multiple.png "Excel formula: Round a number to nearest multiple")](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

### [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

The MROUND function rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the significance argument. If the number is already an exact multiple, no rounding occurs and the original number is returned. You can use MROUND to round prices, times, instrument...

[![Excel formula: Round a number up to next half](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up%20to%20next%20half.png "Excel formula: Round a number up to next half")](https://exceljet.net/formulas/round-a-number-up-to-next-half)

### [Round a number up to next half](https://exceljet.net/formulas/round-a-number-up-to-next-half)

The Excel CEILING function rounds a number up to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. In this example, we want to round up to the nearest half, so we provide 0.5 to...

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

*   [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    
*   [Round a number up to next half](https://exceljet.net/formulas/round-a-number-up-to-next-half)
    

### Functions

*   [ROUND Function](https://exceljet.net/functions/round-function)
    

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
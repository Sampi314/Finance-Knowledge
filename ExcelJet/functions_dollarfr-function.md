# Excel DOLLARFR function | Exceljet

**Source:** https://exceljet.net/functions/dollarfr-function

---

[Skip to main content](https://exceljet.net/functions/dollarfr-function#main-content)

[](https://exceljet.net/functions/dollarfr-function#)

*   [Previous](https://exceljet.net/functions/dollarde-function)
    
*   [Next](https://exceljet.net/functions/duration-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

DOLLARFR Function
=================

by Dave Bruns · Updated 26 Aug 2021

Related functions 
------------------

[DOLLARDE](https://exceljet.net/functions/dollarde-function)

![Excel DOLLARFR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_dollarfr_function.png "Excel DOLLARFR function")

Summary
-------

The Excel DOLLARFR function converts a dollar price in a regular decimal number format to a dollar price in a particular fractional notation used for securities where pricing is given to the nearest 1/8, 1/16, 1/32, etc. The [DOLLARDE function](https://exceljet.net/functions/dollarde-function)
 does the opposite conversion.

Purpose 
--------

Convert price to fractional notation

Return value 
-------------

Dollar value in fractional notation

Syntax
------

    =DOLLARFR(decimal_dollar,fraction)

*   _decimal\_dollar_ - Pricing as a normal decimal number.
*   _fraction_ - The denominator in the fractional unit. 8 = 1/8, 16 = 1/16, 32 = 1/32, etc.

Using the DOLLARFR function 
----------------------------

The Excel DOLLARFR function converts a dollar price in a regular decimal number format to a dollar price in a particular fractional notation used for securities where pricing is given to the nearest 1/8, 1/16, 1/32, etc. The DOLLARDE  function does the opposite conversion.

For example, to convert the price "1 and 1/16" to decimal notation for pricing given to the nearest 1/16, you can use the DOLLARFR function like this:

    =DOLLARFR(1.0625,16) // returns 1.01
    

Notice the first argument is a normal decimal value. The second argument is used to indicate the denominator of the fractional multiple to use for the conversion, i.e. 8 = 1/8, 16 = 1/16, 32 = 1/32, etc.

In the example shown, the formula column E, copied down, is:

    =DOLLARFR(C6,D6)
    

On each row, the DOLLARDE function picks up the decimal value from column C and the fraction denominator from column D.

### Notes

1.  Both _decimal\_dollar_ and _fraction_ arguments must be numeric values.
2.  The value for _fraction_ must be greater than zero.

Related functions
-----------------

[![Excel DOLLARDE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_dollarde_function.png "Excel DOLLARDE function")](https://exceljet.net/functions/dollarde-function)

### [DOLLARDE Function](https://exceljet.net/functions/dollarde-function)

The Excel DOLLARDE function converts a dollar price entered with a special notation to a dollar price displayed as a decimal number.  The [DOLLARFR function](https://exceljet.net/functions/dollarfr-function)
 does the opposite conversion.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [DOLLARDE Function](https://exceljet.net/functions/dollarde-function)
    

### Links

*   [Microsoft DOLLARFR function documentation](https://support.office.com/en-us/article/dollarfr-function-0835d163-3023-4a33-9824-3042c5d4f495)
    

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
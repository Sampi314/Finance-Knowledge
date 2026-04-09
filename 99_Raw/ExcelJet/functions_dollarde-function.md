# Excel DOLLARDE function | Exceljet

**Source:** https://exceljet.net/functions/dollarde-function

---

[Skip to main content](https://exceljet.net/functions/dollarde-function#main-content)

[](https://exceljet.net/functions/dollarde-function#)

*   [Previous](https://exceljet.net/functions/disc-function)
    
*   [Next](https://exceljet.net/functions/dollarfr-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

DOLLARDE Function
=================

by Dave Bruns · Updated 26 Aug 2021

Related functions 
------------------

[DOLLAR](https://exceljet.net/functions/dollar-function)

![Excel DOLLARDE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_dollarde_function.png "Excel DOLLARDE function")

Summary
-------

The Excel DOLLARDE function converts a dollar price entered with a special notation to a dollar price displayed as a decimal number.  The [DOLLARFR function](https://exceljet.net/functions/dollarfr-function)
 does the opposite conversion.

Purpose 
--------

Convert dollar price as fraction to decimal

Return value 
-------------

Equivalent decimal number

Syntax
------

    =DOLLARDE(fractional_dollar,fraction)

*   _fractional\_dollar_ - Dollar component in special fractional notation.
*   _fraction_ - The denominator in the fractional unit. 8 = 1/8, 16 = 1/16, 32 = 1/32, etc.

Using the DOLLARDE function 
----------------------------

The DOLLARDE function is a financial function which converts values pricing entered with a particular fractional notation into an equivalent decimal number. It can be used for securities where pricing is given to the nearest 1/8, 1/16, 1/32, etc.

For example, to convert the price "3 and 1/16" to an equivalent decimal value, you can use the DOLLARDE function like this:

    =DOLLARDE(3.01,16) // returns 3.0625
    

Notice first argument shows the whole dollar value on the left, and the decimal component is used to express the numerator (.01 = 1, .11 = 11, etc.). The second argument is the denominator.

In the example shown, the formula column E, copied down, is:

    =DOLLARDE(C6,D6)
    

On each row, the DOLLARDE function picks up the fractional dollar notation from column C and the denominator from column D.

### Notes

1.  Both _fractional\_dollar_ and _fraction_ arguments must be numeric values.
2.  The value for _fraction_ must be greater than zero.

Related functions
-----------------

[![Excel DOLLAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20dollar%20function.png "Excel DOLLAR function")](https://exceljet.net/functions/dollar-function)

### [DOLLAR Function](https://exceljet.net/functions/dollar-function)

The Excel DOLLAR function converts a number to text using the Currency number format. The TEXT function can do the same thing, and is much more versatile.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [DOLLAR Function](https://exceljet.net/functions/dollar-function)
    

### Links

*   [Microsoft DOLLARDE function documentation](https://support.office.com/en-us/article/dollarde-function-db85aab0-1677-428a-9dfd-a38476693427)
    

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
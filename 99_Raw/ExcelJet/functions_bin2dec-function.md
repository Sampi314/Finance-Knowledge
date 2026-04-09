# Excel BIN2DEC function | Exceljet

**Source:** https://exceljet.net/functions/bin2dec-function

---

[Skip to main content](https://exceljet.net/functions/bin2dec-function#main-content)

[](https://exceljet.net/functions/bin2dec-function#)

*   [Previous](https://exceljet.net/functions/xmatch-function)
    
*   [Next](https://exceljet.net/functions/bin2hex-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

BIN2DEC Function
================

by Kurt Bruns · Updated 29 Dec 2017

Related functions 
------------------

[DEC2BIN](https://exceljet.net/functions/dec2bin-function)

![Excel BIN2DEC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_bin2dec1.png "Excel BIN2DEC function")

Summary
-------

The Excel BIN2DEC function converts a binary number to the decimal equivalent. The input number must contain only zeros and ones and be less than 10 characters long, otherwise the function returns the #NUM! error value.

Purpose 
--------

Converts a binary number to decimal

Return value 
-------------

Decimal Number

Syntax
------

    =BIN2DEC(number)

*   _number_ - The binary number you want to convert to decimal.

Using the BIN2DEC function 
---------------------------

The first bit of the binary number indicates whether the number is positive or negative. The other nine digits represent the size of the number, the max of which is 511 (2^9 - 1). A negative binary number is expected to use the two's complement notation.

![BIN2DEC Input Range](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_bin2dec_input_range_0.png "BIN2DEC Input Range")

Related functions
-----------------

[![Excel DEC2BIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dec2bin.png "Excel DEC2BIN function")](https://exceljet.net/functions/dec2bin-function)

### [DEC2BIN Function](https://exceljet.net/functions/dec2bin-function)

The Excel DEC2BIN function converts a decimal number to its binary equivalent.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [DEC2BIN Function](https://exceljet.net/functions/dec2bin-function)
    

### Links

*   [Microsoft BIN2DEC function documentation](https://support.office.com/en-us/article/bin2dec-function-63905b57-b3a0-453d-99f4-647bb519cd6c)
    

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
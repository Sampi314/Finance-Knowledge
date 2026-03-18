# Excel HEX2BIN function | Exceljet

**Source:** https://exceljet.net/functions/hex2bin-function

---

[Skip to main content](https://exceljet.net/functions/hex2bin-function#main-content)

[](https://exceljet.net/functions/hex2bin-function#)

*   [Previous](https://exceljet.net/functions/delta-function)
    
*   [Next](https://exceljet.net/functions/hex2dec-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

HEX2BIN Function
================

by Kurt Bruns · Updated 22 Jul 2022

Related functions 
------------------

[BIN2HEX](https://exceljet.net/functions/bin2hex-function)

[DECIMAL](https://exceljet.net/functions/decimal-function)

[DEC2HEX](https://exceljet.net/functions/dec2hex-function)

![Excel HEX2BIN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_hex2bin%20function.png "Excel HEX2BIN function")

Summary
-------

The Excel HEX2BIN function converts a hexadecimal number to its binary equivalent.

Purpose 
--------

Converts a hexadecimal number to binary

Return value 
-------------

Binary number

Syntax
------

    =HEX2BIN(number,[places])

*   _number_ - The hexadecimal number you want to convert to binary.
*   _places_ - \[optional\] Pads the resulting binary number with zeros up to the specified number of digits. If omitted returns the least number of characters required to represent the number.

Using the HEX2BIN function 
---------------------------

*   Excel only converts to binary numbers of 10-digits or less, restricting the input range to \[-512, 511\] (decimal).
*   The input number must be less than or equal to ten alpha-numeric characters, otherwise the function returns the #NUM! error value.
*   The internal (binary) representation of the hexadecimal number uses two's complement notation. The first bit indicates whether the number is positive or negative, and the other 39 bits indicate the magnitude of the number.

Related functions
-----------------

[![Excel BIN2HEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_bin2hex.png "Excel BIN2HEX function")](https://exceljet.net/functions/bin2hex-function)

### [BIN2HEX Function](https://exceljet.net/functions/bin2hex-function)

The Excel BIN2HEX function converts a binary number to its hexadecimal equivalent.

[![Excel DECIMAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20decimal%20function.png "Excel DECIMAL function")](https://exceljet.net/functions/decimal-function)

### [DECIMAL Function](https://exceljet.net/functions/decimal-function)

The Excel DECIMAL function converts a number in a given base into its decimal number equivalent. For example, the DECIMAL function can convert the binary number 1101 into the decimal number 13....

[![Excel DEC2HEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dec2hex.png "Excel DEC2HEX function")](https://exceljet.net/functions/dec2hex-function)

### [DEC2HEX Function](https://exceljet.net/functions/dec2hex-function)

The Excel DEC2HEX function converts a decimal number to its hexadecimal equivalent.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [BIN2HEX Function](https://exceljet.net/functions/bin2hex-function)
    
*   [DECIMAL Function](https://exceljet.net/functions/decimal-function)
    
*   [DEC2HEX Function](https://exceljet.net/functions/dec2hex-function)
    

### Links

*   [Microsoft HEX2BIN function documentation](https://support.office.com/en-us/article/hex2bin-function-a13aafaa-5737-4920-8424-643e581828c1)
    

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
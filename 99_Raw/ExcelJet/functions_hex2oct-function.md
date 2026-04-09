# Excel HEX2OCT function | Exceljet

**Source:** https://exceljet.net/functions/hex2oct-function

---

[Skip to main content](https://exceljet.net/functions/hex2oct-function#main-content)

[](https://exceljet.net/functions/hex2oct-function#)

*   [Previous](https://exceljet.net/functions/hex2dec-function)
    
*   [Next](https://exceljet.net/functions/imabs-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

HEX2OCT Function
================

by Kurt Bruns · Updated 27 Jun 2025

Related functions 
------------------

[OCT2HEX](https://exceljet.net/functions/oct2hex-function)

[HEX2DEC](https://exceljet.net/functions/hex2dec-function)

[HEX2BIN](https://exceljet.net/functions/hex2bin-function)

[DECIMAL](https://exceljet.net/functions/decimal-function)

![Excel HEX2OCT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_hex2oct.png "Excel HEX2OCT function")

Summary
-------

The Excel HEX2OCT function converts a hexadecimal number to its octal equivalent.

Purpose 
--------

Converts a hexadecimal number to octal

Return value 
-------------

Octal number

Syntax
------

    =HEX2OCT(number,[places])

*   _number_ - The hexadecimal number you want to convert to octal.
*   _places_ - \[optional\] Pads the resulting binary number with zeros up to the specified number of digits. If omitted returns the least number of characters required to represent the number.

Using the HEX2OCT function 
---------------------------

*   Excel only converts to octal numbers of 10-digits or less, restricting the range of valid input to \[0, 7777777777\] (octal).
*   The input number must be less than or equal to ten alpha-numeric characters, otherwise the function returns the #NUM! error value.

### Negative Numbers

Excel interprets both octal and hexadecimal numbers using two's complement notation. Two's complement notation is a convention that computers use to represent negative numbers in binary.

![Example of two's complement for HEX2OCT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_hex2oct_negative_numbers.png?itok=eaRejHbT "Example of two's complement for HEX2OCT function")

Related functions
-----------------

[![Excel OCT2HEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oct2hex_main_screenshot_cropped.png "Excel OCT2HEX function")](https://exceljet.net/functions/oct2hex-function)

### [OCT2HEX Function](https://exceljet.net/functions/oct2hex-function)

The Excel OCT2HEX function converts an octal number to its hexadecimal equivalent. For example, the following formula converts the octal number 23 to hexadecimal:

    =OCT2HEX(23) // returns 13

[![Excel HEX2DEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_hex2dec.png "Excel HEX2DEC function")](https://exceljet.net/functions/hex2dec-function)

### [HEX2DEC Function](https://exceljet.net/functions/hex2dec-function)

The Excel HEX2DEC function converts a hexadecimal number to its decimal equivalent.

[![Excel HEX2BIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_hex2bin%20function.png "Excel HEX2BIN function")](https://exceljet.net/functions/hex2bin-function)

### [HEX2BIN Function](https://exceljet.net/functions/hex2bin-function)

The Excel HEX2BIN function converts a hexadecimal number to its binary equivalent.

[![Excel DECIMAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20decimal%20function.png "Excel DECIMAL function")](https://exceljet.net/functions/decimal-function)

### [DECIMAL Function](https://exceljet.net/functions/decimal-function)

The Excel DECIMAL function converts a number in a given base into its decimal number equivalent. For example, the DECIMAL function can convert the binary number 1101 into the decimal number 13....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [OCT2HEX Function](https://exceljet.net/functions/oct2hex-function)
    
*   [HEX2DEC Function](https://exceljet.net/functions/hex2dec-function)
    
*   [HEX2BIN Function](https://exceljet.net/functions/hex2bin-function)
    
*   [DECIMAL Function](https://exceljet.net/functions/decimal-function)
    

### Links

*   [Microsoft HEX2OCT function documentation](https://support.office.com/en-us/article/hex2oct-function-54d52808-5d19-4bd0-8a63-1096a5d11912)
    

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
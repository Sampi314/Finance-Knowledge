# Excel DEC2HEX function | Exceljet

**Source:** https://exceljet.net/functions/dec2hex-function

---

[Skip to main content](https://exceljet.net/functions/dec2hex-function#main-content)

[](https://exceljet.net/functions/dec2hex-function#)

*   [Previous](https://exceljet.net/functions/dec2bin-function)
    
*   [Next](https://exceljet.net/functions/dec2oct-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

DEC2HEX Function
================

by Kurt Bruns · Updated 20 Aug 2021

Related functions 
------------------

[DECIMAL](https://exceljet.net/functions/decimal-function)

![Excel DEC2HEX function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_dec2hex.png "Excel DEC2HEX function")

Summary
-------

The Excel DEC2HEX function converts a decimal number to its hexadecimal equivalent.

Purpose 
--------

Converts a decimal number to hexadecimal

Return value 
-------------

Hexadecimal number

Syntax
------

    =DEC2HEX(number,[places])

*   _number_ - The decimal number you want to convert to hexadecimal.
*   _places_ - \[optional\] Pads the resulting number with zeros up to the specified number of digits. If omitted returns the least number of characters required to represent the number.

Using the DEC2HEX function 
---------------------------

The input must be a valid decimal number within the range \[ -2^39, 2^39 - 1 \].

### Negative Values

Excel internally represents Hexadecimal numbers in binary using 40 bits. The first bit indicates whether the number is positive or negative. The remaining bits indicate the magnitude of the number. Negative numbers are internally represented in binary using two's complement notation. Two's complement notation, when converted to hexadecimal, starts at the highest 10 digit hexadecimal number and goes backwards.

![Range of DEC2HEX function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_dec2hex_range.png?itok=WtNogvTi "Range of DEC2HEX function")

Related functions
-----------------

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

*   [DECIMAL Function](https://exceljet.net/functions/decimal-function)
    

### Links

*   [Microsoft DEC2HEX function documentation](https://support.office.com/en-us/article/dec2hex-function-6344ee8b-b6b5-4c6a-a672-f64666704619)
    

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
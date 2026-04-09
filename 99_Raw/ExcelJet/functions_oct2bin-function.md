# Excel OCT2BIN function | Exceljet

**Source:** https://exceljet.net/functions/oct2bin-function

---

[Skip to main content](https://exceljet.net/functions/oct2bin-function#main-content)

[](https://exceljet.net/functions/oct2bin-function#)

*   [Previous](https://exceljet.net/functions/imtan-function)
    
*   [Next](https://exceljet.net/functions/oct2dec-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

OCT2BIN Function
================

by Kurt Bruns · Updated 26 Jun 2025

Related functions 
------------------

[DEC2OCT](https://exceljet.net/functions/dec2oct-function)

[OCT2DEC](https://exceljet.net/functions/oct2dec-function)

[OCT2HEX](https://exceljet.net/functions/oct2hex-function)

![Excel OCT2BIN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_oct2bin_main_screenshot_cropped.png "Excel OCT2BIN function")

Summary
-------

The Excel OCT2BIN function converts an octal number to its binary equivalent. For example, the following formula converts the octal number 2 to binary:

    =OCT2BIN(2) // returns 10 (binary)

Purpose 
--------

Convert octal number to binary

Return value 
-------------

Binary number

Syntax
------

    =OCT2BIN(number,[places])

*   _number_ - The octal number you want to convert.
*   _places_ - \[optional\] The number of characters to use. If omitted, the function uses the minimum number of characters necessary.

Using the OCT2BIN function 
---------------------------

The OCT2BIN function is used to convert octal numbers (base 8) to binary numbers (base 2). This is useful when working with different number systems, especially in engineering and computer science applications.

### Key features

*   Converts octal numbers to binary numbers
*   Supports optional padding with leading zeros
*   Handles both positive and negative octal numbers (using two's-complement for negatives)
*   Returns a text string representing the binary number

> To get the octal representation of a decimal number, use the DEC2OCT function.

### Table of contents

*   [Example #1 - Basic conversion](https://exceljet.net/functions/oct2bin-function#example-1--basic-conversion)
    
*   [Example #2 - Padding with leading zeros](https://exceljet.net/functions/oct2bin-function#example-2--padding-with-leading-zeros)
    
*   [Example #3 - Negative octal numbers](https://exceljet.net/functions/oct2bin-function#example-3--negative-octal-numbers)
    
*   [Example #4 - Limits and range](https://exceljet.net/functions/oct2bin-function#example-4--limits-and-range)
    
*   [Error handling](https://exceljet.net/functions/oct2bin-function#error-handling)
    

### Example #1 - Basic conversion

To convert the octal number 11 to binary, use the following formula:

    =OCT2BIN(11) // returns 1001 (binary)
    

### Example #2 - Padding with leading zeros

To convert the octal number 11 to binary, padded to 10 characters, use the following formula:

    =OCT2BIN(11, 10) // returns 00000001001 (binary)
    

### Example #3 - Negative octal numbers

Excel represents negative numbers in non-decimal bases (like octal and binary) using two's complement notation with a fixed width of 10 characters. This means that when you use OCT2BIN with a negative octal number, Excel interprets the input as a two's complement value and returns a 10-character binary string.

For example, to represent the decimal number -3 in octal, you would use the octal number `7777777775`. This is because the most significant digit is the sign bit, and the remaining 9 digits represent the magnitude.

    =DEC2OCT(-3) // returns 7777777775
    

Then, when we convert the octal number to binary, we get the following result:

    =OCT2BIN(7777777775) // returns 1111111101
    

This is because the most significant bit is the sign bit, and the remaining 9 digits represent the magnitude.

### Example #4 - Limits and range

The OCT2BIN function is limited to binary numbers with a maximum of 10 digits. If you try to convert an octal number that would require more than 10 binary digits, OCT2BIN returns the `#NUM!` error.

The table below shows what happens at the boundaries:

![Screenshot showing the limits and range of the OCT2BIN function in Excel. The largest positive octal value that can be converted is 777 (decimal 511), and the smallest negative octal value is 7777777000 (decimal -512). Values outside this range return a #NUM! error.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_oct2bin_example_4_limits_and_range_screenshot_cropped.png "OCT2BIN Function Limits and Range in Excel")

The largest positive number you can convert is octal `777` (decimal 511). The smallest negative number you can convert is octal `7777777000` (decimal -512). Any value outside this range returns a `#NUM!` error.

### Error handling

*   If the input is outside the allowed range (e.g., 7777776777 or 1000), OCT2BIN returns the #NUM! error value.
*   If the input is non-numeric (e.g., Text), OCT2BIN returns the #NUM! error value.
*   If the input is not a valid octal number (e.g., 80), OCT2BIN returns the #NUM! error value.
*   If the input is not an integer (e.g., 10.5), OCT2BIN returns the #NUM! error value.
*   If the input is negative (e.g., -4), OCT2BIN returns the #NUM! error value.

Related functions
-----------------

[![Excel DEC2OCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dec2oct.png "Excel DEC2OCT function")](https://exceljet.net/functions/dec2oct-function)

### [DEC2OCT Function](https://exceljet.net/functions/dec2oct-function)

The Excel DEC2OCT function converts a decimal number to its octal equivalent.

[![Excel OCT2DEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oct2dec_main_screenshot_cropped.png "Excel OCT2DEC function")](https://exceljet.net/functions/oct2dec-function)

### [OCT2DEC Function](https://exceljet.net/functions/oct2dec-function)

The Excel OCT2DEC function converts an octal number to its decimal equivalent. For example, the following formula converts the octal number 23 to decimal:

    =OCT2DEC(23) // returns 19

[![Excel OCT2HEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oct2hex_main_screenshot_cropped.png "Excel OCT2HEX function")](https://exceljet.net/functions/oct2hex-function)

### [OCT2HEX Function](https://exceljet.net/functions/oct2hex-function)

The Excel OCT2HEX function converts an octal number to its hexadecimal equivalent. For example, the following formula converts the octal number 23 to hexadecimal:

    =OCT2HEX(23) // returns 13

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [DEC2OCT Function](https://exceljet.net/functions/dec2oct-function)
    
*   [OCT2DEC Function](https://exceljet.net/functions/oct2dec-function)
    
*   [OCT2HEX Function](https://exceljet.net/functions/oct2hex-function)
    

### Links

*   [Microsoft OCT2BIN function documentation](https://support.office.com/en-us/article/oct2bin-function-55383471-3c56-4d27-9522-1a8ec646c589)
    

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
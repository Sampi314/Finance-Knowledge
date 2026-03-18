# Excel OCT2DEC function | Exceljet

**Source:** https://exceljet.net/functions/oct2dec-function

---

[Skip to main content](https://exceljet.net/functions/oct2dec-function#main-content)

[](https://exceljet.net/functions/oct2dec-function#)

*   [Previous](https://exceljet.net/functions/oct2bin-function)
    
*   [Next](https://exceljet.net/functions/oct2hex-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

OCT2DEC Function
================

by Kurt Bruns · Updated 27 Jun 2025

Related functions 
------------------

[DEC2OCT](https://exceljet.net/functions/dec2oct-function)

[OCT2BIN](https://exceljet.net/functions/oct2bin-function)

[OCT2HEX](https://exceljet.net/functions/oct2hex-function)

![Excel OCT2DEC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_oct2dec_main_screenshot_cropped.png "Excel OCT2DEC function")

Summary
-------

The Excel OCT2DEC function converts an octal number to its decimal equivalent. For example, the following formula converts the octal number 23 to decimal:

    =OCT2DEC(23) // returns 19
    

Purpose 
--------

Converts an octal number to its decimal equivalent

Return value 
-------------

A decimal number

Syntax
------

    =OCT2DEC(number)

*   _number_ - The octal number you want to convert.

Using the OCT2DEC function 
---------------------------

The OCT2DEC function is used to convert octal numbers (base 8) to decimal numbers (base 10). This is useful when working with different number systems, especially in engineering and computer science applications.

### Key features

*   Converts octal numbers to decimal numbers
*   Handles both positive and negative octal numbers (using two's-complement for negatives)
*   Returns a decimal number (as a number, not text)

> To get the octal representation of a decimal number, use the [DEC2OCT](https://exceljet.net/functions/dec2oct-function)
>  function.

### Table of contents

*   [Example #1 - Basic conversion](https://exceljet.net/functions/oct2dec-function#example-1--basic-conversion)
    
*   [Example #2 - Negative octal numbers](https://exceljet.net/functions/oct2dec-function#example-2--negative-octal-numbers)
    
*   [Example #3 - Error conditions](https://exceljet.net/functions/oct2dec-function#example-3--error-conditions)
    

### Example #1 - Basic conversion

To convert the octal number 10 to decimal, use the following formula:

    =OCT2DEC(10) // returns 8
    

The spreadsheet below shows some basic conversions of octal numbers to decimal numbers:

![OCT2DEC function basic conversion in Excel, showing octal 10 converting to decimal 8](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_oct2dec_example_1_basic_conversion_screenshot_cropped.png "OCT2DEC function: basic conversion example in Excel")

### Example #2 - Negative octal numbers

Excel represents negative numbers in non-decimal bases (like octal) using two's complement notation with a fixed width of 10 characters. For example, the decimal number -2 is represented as the octal number `7777777776`.

    =OCT2DEC(7777777776) // returns -2
    

This is because Excel represents the number using 30 bits, where the first bit is used for the sign, and the remaining 29 bits represent the value. Octal numbers from `0` to `3777777777` represent positive numbers, and octal numbers from `4000000000` to `7777777777` represent negative numbers.

In other words, the largest positive decimal number you can represent is 2^29 - 1 (536,870,911), and the smallest negative decimal number you can represent is -2^29 (-536,870,912). The spreadsheet below shows the octal numbers corresponding to positive and negative decimal numbers:

![OCT2DEC function negative octal numbers in Excel, showing octal 7777777776 converting to decimal -2](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_oct2dec_example_2_negative_octal_numbers_screenshot_cropped.png "OCT2DEC function: negative octal numbers example in Excel")

### Example #3 - Error conditions

There are several error conditions that can occur when using the OCT2DEC function. For example, if the input contains more than 10 digits, OCT2DEC returns a `#NUM!` error. This behavior and other error conditions are shown in the example below:

![OCT2DEC function error conditions in Excel, showing #NUM! error for octal numbers with more than 10 digits](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_oct2dec_example_3_error_conditions_screenshot_cropped.png "OCT2DEC function: error conditions example in Excel")

Related functions
-----------------

[![Excel DEC2OCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dec2oct.png "Excel DEC2OCT function")](https://exceljet.net/functions/dec2oct-function)

### [DEC2OCT Function](https://exceljet.net/functions/dec2oct-function)

The Excel DEC2OCT function converts a decimal number to its octal equivalent.

[![Excel OCT2BIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oct2bin_main_screenshot_cropped.png "Excel OCT2BIN function")](https://exceljet.net/functions/oct2bin-function)

### [OCT2BIN Function](https://exceljet.net/functions/oct2bin-function)

The Excel OCT2BIN function converts an octal number to its binary equivalent. For example, the following formula converts the octal number 2 to binary:

    =OCT2BIN(2) // returns 10 (binary)

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
    
*   [OCT2BIN Function](https://exceljet.net/functions/oct2bin-function)
    
*   [OCT2HEX Function](https://exceljet.net/functions/oct2hex-function)
    

### Links

*   [Microsoft OCT2DEC function documentation](https://support.office.com/en-us/article/oct2dec-function-87606014-cb98-44b2-8dbb-e48f8ced1554)
    

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
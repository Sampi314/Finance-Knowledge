# Excel OCT2HEX function | Exceljet

**Source:** https://exceljet.net/functions/oct2hex-function

---

[Skip to main content](https://exceljet.net/functions/oct2hex-function#main-content)

[](https://exceljet.net/functions/oct2hex-function#)

*   [Previous](https://exceljet.net/functions/oct2dec-function)
    
*   [Next](https://exceljet.net/functions/accrint-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

OCT2HEX Function
================

by Kurt Bruns · Updated 27 Jun 2025

Related functions 
------------------

[HEX2OCT](https://exceljet.net/functions/hex2oct-function)

[OCT2BIN](https://exceljet.net/functions/oct2bin-function)

[OCT2DEC](https://exceljet.net/functions/oct2dec-function)

![Excel OCT2HEX function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_oct2hex_main_screenshot_cropped.png "Excel OCT2HEX function")

Summary
-------

The Excel OCT2HEX function converts an octal number to its hexadecimal equivalent. For example, the following formula converts the octal number 23 to hexadecimal:

    =OCT2HEX(23) // returns 13
    

Purpose 
--------

Converts an octal number to its hexadecimal equivalent

Return value 
-------------

A hexadecimal number as text

Syntax
------

    =OCT2HEX(number,[places])

*   _number_ - The octal number you want to convert.
*   _places_ - \[optional\] The number of characters to use in the result. If omitted, uses the minimum number of characters necessary.

Using the OCT2HEX function 
---------------------------

The OCT2HEX function is used to convert octal numbers (base 8) to hexadecimal numbers (base 16). This is useful when working with different number systems, especially in engineering and computer science applications.

### Key features

*   Converts octal numbers to hexadecimal numbers
*   Handles both positive and negative octal numbers (using two's-complement for negatives)
*   Returns a hexadecimal number as text

> To get the octal representation of a hexadecimal number, use the [HEX2OCT](https://exceljet.net/functions/hex2oct-function)
>  function.

### Table of contents

*   [Example #1 - Basic conversion](https://exceljet.net/functions/oct2hex-function#example-1--basic-conversion)
    
*   [Example #2 - Using the places argument](https://exceljet.net/functions/oct2hex-function#example-2--using-the-places-argument)
    
*   [Example #3 - Negative octal numbers](https://exceljet.net/functions/oct2hex-function#example-3--negative-octal-numbers)
    
*   [Example #4 - Error conditions](https://exceljet.net/functions/oct2hex-function#example-4--error-conditions)
    

### Example #1 - Basic conversion

To convert the octal number 12 to hexadecimal, use the following formula:

    =OCT2HEX(12) // returns A
    

The spreadsheet below shows some basic conversions of octal numbers to hexadecimal numbers:

![OCT2HEX function basic conversion in Excel, showing octal 12 converting to hexadecimal A](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_oct2hex_example_1_basic_conversion_screenshot_cropped.png "OCT2HEX function: basic conversion example in Excel")

### Example #2 - Using the places argument

The `places` argument in the `OCT2HEX` function specifies the minimum number of characters to use in the result. When the converted hexadecimal number has fewer characters than the value specified for `places`, Excel pads the result with leading zeros. This is useful when you want all results to have a consistent length.

For example, to convert the octal number 12 to hexadecimal and pad the result to 3 characters, use:

    =OCT2HEX(12, 3) // returns 00A
    

Places must be a number between 1 and 10, otherwise Excel will return a `#NUM!` error. If places is not an integer, Excel will truncate the decimal part. If the result is longer than the number specified in `places`, Excel will return a `#NUM!` error.

### Example #3 - Negative octal numbers

Excel represents negative numbers in non-decimal bases (like octal) using two's complement notation with a fixed width of 10 characters. This means octal numbers from `0` to `3777777777` represent positive numbers, and octal numbers from `4000000000` to `7777777777` represent negative numbers.

Shown below is a table of the octal numbers from `0` to `7777777777` and their corresponding hexadecimal and decimal numbers:

![OCT2HEX function negative octal numbers in Excel, showing octal 7777777776 converting to hexadecimal FFFFFFFE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_oct2hex_example_3_negative_numbers_screenshot_cropped.png "OCT2HEX function: negative octal numbers example in Excel")

This means the octal numbers from `4000000000` to `7777777777` are mapped to different hexadecimal numbers, because Excel uses two's complement notation to represent negative numbers. For example, the octal number `4000000000` is mapped to the hexadecimal number `FFE0000000` instead of the hexadecimal number `0020000000`.

    =OCT2HEX(0377777777, 10) // returns 0003FFFFFF
    =OCT2HEX(0400000000, 10) // returns 0004000000
    =OCT2HEX(3777777777, 10) // returns 001FFFFFFF
    =OCT2HEX(4000000000, 10) // returns FFE0000000
    

### Example #4 - Error conditions

There are several error conditions that can occur when using the OCT2HEX function. For example, if the input contains more than 10 digits, OCT2HEX returns a `#NUM!` error. This behavior and other error conditions are shown in the example below:

![OCT2HEX function error conditions in Excel, showing #NUM! error for octal numbers with more than 10 digits](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_oct2hex_example_4_error_conditions_screenshot_cropped.png "OCT2HEX function: error conditions example in Excel")

Related functions
-----------------

[![Excel HEX2OCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_hex2oct.png "Excel HEX2OCT function")](https://exceljet.net/functions/hex2oct-function)

### [HEX2OCT Function](https://exceljet.net/functions/hex2oct-function)

The Excel HEX2OCT function converts a hexadecimal number to its octal equivalent.

[![Excel OCT2BIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oct2bin_main_screenshot_cropped.png "Excel OCT2BIN function")](https://exceljet.net/functions/oct2bin-function)

### [OCT2BIN Function](https://exceljet.net/functions/oct2bin-function)

The Excel OCT2BIN function converts an octal number to its binary equivalent. For example, the following formula converts the octal number 2 to binary:

    =OCT2BIN(2) // returns 10 (binary)

[![Excel OCT2DEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oct2dec_main_screenshot_cropped.png "Excel OCT2DEC function")](https://exceljet.net/functions/oct2dec-function)

### [OCT2DEC Function](https://exceljet.net/functions/oct2dec-function)

The Excel OCT2DEC function converts an octal number to its decimal equivalent. For example, the following formula converts the octal number 23 to decimal:

    =OCT2DEC(23) // returns 19

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [HEX2OCT Function](https://exceljet.net/functions/hex2oct-function)
    
*   [OCT2BIN Function](https://exceljet.net/functions/oct2bin-function)
    
*   [OCT2DEC Function](https://exceljet.net/functions/oct2dec-function)
    

### Links

*   [Microsoft OCT2HEX function documentation](https://support.office.com/en-us/article/oct2hex-function-912175b4-d497-41b4-a029-221f051b858f)
    

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
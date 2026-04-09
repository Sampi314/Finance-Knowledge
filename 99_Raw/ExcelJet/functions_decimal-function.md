# Excel DECIMAL function | Exceljet

**Source:** https://exceljet.net/functions/decimal-function

---

[Skip to main content](https://exceljet.net/functions/decimal-function#main-content)

[](https://exceljet.net/functions/decimal-function#)

*   [Previous](https://exceljet.net/functions/combina-function)
    
*   [Next](https://exceljet.net/functions/even-function)
    

Excel 2013

[Math](https://exceljet.net/functions#Math)

DECIMAL Function
================

by Kurt Bruns · Updated 27 Jun 2025

Related functions 
------------------

[BASE](https://exceljet.net/functions/base-function)

[HEX2DEC](https://exceljet.net/functions/hex2dec-function)

[OCT2DEC](https://exceljet.net/functions/oct2dec-function)

[BIN2DEC](https://exceljet.net/functions/bin2dec-function)

![Excel DECIMAL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20decimal%20function.png "Excel DECIMAL function")

Summary
-------

The Excel DECIMAL function converts a number in a given base into its decimal number equivalent. For example, the DECIMAL function can convert the binary number 1101 into the decimal number 13.

Purpose 
--------

Convert a number in a different base to a decimal number

Return value 
-------------

Decimal number

Syntax
------

    =DECIMAL(number,radix)

*   _number_ - A text string representing a number.
*   _radix_ - The base of the number to be converted, an integer between 2-36.

Using the DECIMAL function 
---------------------------

The DECIMAL function converts a number in a known base into its decimal number equivalent. For example, the DECIMAL function can convert the binary number 1101 into the decimal number 13. The number provided to DECIMAL should be a [text string](https://exceljet.net/glossary/text-value)
.

The DECIMAL function takes two [arguments](https://exceljet.net/glossary/function-argument)
: _number_ and _radix_. _Number_ should be the text representation of a number in a known base. _Radix_ is the number of digits used to represent numbers (i.e. the base) and should be an integer between 2 and 36. The characters given in _number_ need to conform to the [numbering system](https://exceljet.net/functions/decimal-function#number_system_characters)
 specified with _radix_. 

### Examples

In the hexadecimal number system, the number 255 is represented as "FF". To convert the text string "FF" to the decimal number 255, you can use the DECIMAL function like this:

    =DECIMAL("FF",16) // returns 255
    

To convert the binary number 1101 to its decimal number equivalent, 13, use DECIMAL like this:

    =DECIMAL("1101",2) // returns 13
    

In the example shown, the numbers in column B are in different bases, and the base is given in column C. The formula in column D5 is:

    =DECIMAL(B5,C5) // returns 3
    

As the formula is copied down, the DECIMAL function converts each number in column B to its decimal equivalent using the base specified in column C for the _radix_ argument. The decimal numbers in column D are the output from DECIMAL.

### BASE function

The BASE function performs the opposite conversion as the DECIMAL function:

    =BASE(100,2) // returns "1100100"
    =DECIMAL("1100100",2) // returns 100
    

See [more on the BASE function here](https://exceljet.net/functions/base-function)
.

### Number system characters

Different bases use different alphanumeric characters to represent numbers. The table below shows the characters uses for binary, octal, decimal, and hexadecimal number systems.

| Name | Base | Alphanumeric characters |
| --- | --- | --- |
| binary | 2   | 0 - 1 |
| octal | 8   | 0 - 7 |
| decimal | 10  | 0 - 9 |
| hexadecimal | 16  | 0 - 9 and A - F |

### Notes

*   The _number_ argument should be provided as a [text string](https://exceljet.net/glossary/text-value)
    .
*   The result from DECIMAL is a numeric value.
*   If _number_ is negative, DECIMAL returns a #NUM! error.
*   if _number_ contains a decimal value,  DECIMAL returns a #NUM! error.
*   If _number_ is out-of-range for the given base, DECIMAL returns a #NUM! error.

Related functions
-----------------

[![Excel BASE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20base%20function.png "Excel BASE function")](https://exceljet.net/functions/base-function)

### [BASE Function](https://exceljet.net/functions/base-function)

The Excel BASE function converts a number to the text representation of the same number in a given base, where base is provided as the radix argument.

[![Excel HEX2DEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_hex2dec.png "Excel HEX2DEC function")](https://exceljet.net/functions/hex2dec-function)

### [HEX2DEC Function](https://exceljet.net/functions/hex2dec-function)

The Excel HEX2DEC function converts a hexadecimal number to its decimal equivalent.

[![Excel OCT2DEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oct2dec_main_screenshot_cropped.png "Excel OCT2DEC function")](https://exceljet.net/functions/oct2dec-function)

### [OCT2DEC Function](https://exceljet.net/functions/oct2dec-function)

The Excel OCT2DEC function converts an octal number to its decimal equivalent. For example, the following formula converts the octal number 23 to decimal:

    =OCT2DEC(23) // returns 19

[![Excel BIN2DEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_bin2dec1.png "Excel BIN2DEC function")](https://exceljet.net/functions/bin2dec-function)

### [BIN2DEC Function](https://exceljet.net/functions/bin2dec-function)

The Excel BIN2DEC function converts a binary number to the decimal equivalent. The input number must contain only zeros and ones and be less than 10 characters long, otherwise the function returns the #NUM! error value.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [BASE Function](https://exceljet.net/functions/base-function)
    
*   [HEX2DEC Function](https://exceljet.net/functions/hex2dec-function)
    
*   [OCT2DEC Function](https://exceljet.net/functions/oct2dec-function)
    
*   [BIN2DEC Function](https://exceljet.net/functions/bin2dec-function)
    

### Links

*   [Microsoft DECIMAL function documentation](https://support.office.com/en-us/article/decimal-function-ee554665-6176-46ef-82de-0a283658da2e)
    

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
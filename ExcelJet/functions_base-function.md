# Excel BASE function | Exceljet

**Source:** https://exceljet.net/functions/base-function

---

[Skip to main content](https://exceljet.net/functions/base-function#main-content)

[](https://exceljet.net/functions/base-function#)

*   [Previous](https://exceljet.net/functions/arabic-function)
    
*   [Next](https://exceljet.net/functions/ceiling-function)
    

Excel 2013

[Math](https://exceljet.net/functions#Math)

BASE Function
=============

by Kurt Bruns · Updated 10 Sep 2021

Related functions 
------------------

[DEC2BIN](https://exceljet.net/functions/dec2bin-function)

[DEC2OCT](https://exceljet.net/functions/dec2oct-function)

[DEC2HEX](https://exceljet.net/functions/dec2hex-function)

[DECIMAL](https://exceljet.net/functions/decimal-function)

![Excel BASE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20base%20function.png "Excel BASE function")

Summary
-------

The Excel BASE function converts a number to the text representation of the same number in a given base, where base is provided as the radix argument.

Purpose 
--------

Convert number to another base.

Return value 
-------------

The text representation of the converted number.

Syntax
------

    =BASE(number,radix,[min_length])

*   _number_ - The number to convert to a given base.
*   _radix_ - The base to convert to.
*   _min\_length_ - \[optional\] The minimum string length to return, achieved by padding with zeros.

Using the BASE function 
------------------------

The BASE function converts a number to a given base and returns the result as a [text string](https://exceljet.net/glossary/text-value)
. Base is specified with the _radix_ argument. 

The BASE function takes three [arguments](https://exceljet.net/glossary/function-argument)
: _number_, _radix_, and _min\_length_. _Number_ should be an integer between 1 and 2^53. If _number_ is negative, BASE returns a #NUM! error. The _radix_ argument is used to specify base. _Radix_ represents the number of digits used to represent numbers and should be an integer between 2 and 36. The optional _min\_length_ argument is the minimum string length that BASE should return. When _min\_length_ is provided, BASE will pad the output with zeros as needed to achieve the length specified.

### Examples

The _radix_ argument specifies base and the output from the BASE function is a [text string](https://exceljet.net/glossary/text-value)
. For example, the formulas below convert the number 13 into text representations of 13 in base 2 (binary), base 10 (decimal), and base 16 (hexadecimal):

    =BASE(13,2) // returns "1101"
    =BASE(13,10) // returns "13"
    =BASE(13,16) // returns "D"
    

In the worksheet shown, the input numbers are being converted to three different representations: base 2 (binary), base 10 (decimal), and base 16 (hexadecimal). The formulas in D5, E5, and F5 are:

    =BASE(B5,2) // base 2
    =BASE(B5,10) // base 10
    =BASE(B5,16) // base 16
    

The function also offers an optional argument _min\_length_ which will pad the returned string with zeros when its length is less than the given value. For example, the formulas below require a minimum length of 4:

    =BASE(3,2,4) // returns "0011" as text
    =BASE(10,16,4) // returns "000A" as text
    

### DECIMAL function

The DECIMAL function performs the opposite conversion as the BASE function:

    =BASE(100,2) // returns "1100100"
    =DECIMAL("1100100",2) // returns 100
    

See [more on the DECIMAL function here](https://exceljet.net/functions/decimal-function)
.

### Notes

*   The result from BASE is a text string.
*   If _number_ is negative, BASE returns a #NUM! error.
*   BASE expects integers; decimal values are ignored.

BASE function examples
----------------------

[![Excel formula: Get Unicode Sequence from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_unicode_sequence_of_text_main_0.png "Excel formula: Get Unicode Sequence from text")](https://exceljet.net/formulas/get-unicode-sequence-from-text)

### [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)

In this example, the goal is to convert each character in a text string into its corresponding Unicode code point and display the results as a space-separated sequence. This problem can be solved using several Excel functions working together to extract, convert, and format the Unicode values. The...

Related functions
-----------------

[![Excel DEC2BIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dec2bin.png "Excel DEC2BIN function")](https://exceljet.net/functions/dec2bin-function)

### [DEC2BIN Function](https://exceljet.net/functions/dec2bin-function)

The Excel DEC2BIN function converts a decimal number to its binary equivalent.

[![Excel DEC2OCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dec2oct.png "Excel DEC2OCT function")](https://exceljet.net/functions/dec2oct-function)

### [DEC2OCT Function](https://exceljet.net/functions/dec2oct-function)

The Excel DEC2OCT function converts a decimal number to its octal equivalent.

[![Excel DEC2HEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dec2hex.png "Excel DEC2HEX function")](https://exceljet.net/functions/dec2hex-function)

### [DEC2HEX Function](https://exceljet.net/functions/dec2hex-function)

The Excel DEC2HEX function converts a decimal number to its hexadecimal equivalent.

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

### Formulas

*   [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)
    

### Functions

*   [DEC2BIN Function](https://exceljet.net/functions/dec2bin-function)
    
*   [DEC2OCT Function](https://exceljet.net/functions/dec2oct-function)
    
*   [DEC2HEX Function](https://exceljet.net/functions/dec2hex-function)
    
*   [DECIMAL Function](https://exceljet.net/functions/decimal-function)
    

### Links

*   [Microsoft BASE function documentation](https://support.office.com/en-us/article/base-function-2ef61411-aee9-4f29-a811-1c42456c6342)
    

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
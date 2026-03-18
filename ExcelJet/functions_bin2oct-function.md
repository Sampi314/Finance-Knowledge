# Excel BIN2OCT function | Exceljet

**Source:** https://exceljet.net/functions/bin2oct-function

---

[Skip to main content](https://exceljet.net/functions/bin2oct-function#main-content)

[](https://exceljet.net/functions/bin2oct-function#)

*   [Previous](https://exceljet.net/functions/bin2hex-function)
    
*   [Next](https://exceljet.net/functions/bitand-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

BIN2OCT Function
================

by Kurt Bruns · Updated 10 Jan 2018

Related functions 
------------------

[DECIMAL](https://exceljet.net/functions/decimal-function)

![Excel BIN2OCT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_bin2oct1.png "Excel BIN2OCT function")

Summary
-------

The Excel BIN2OCT function converts a binary number to its octal equivalent.

Purpose 
--------

Converts a binary number to octal

Return value 
-------------

Octal number

Syntax
------

    =BIN2OCT(number,[places])

*   _number_ - The binary number you want to convert to octal.
*   _places_ - \[optional\] If omitted uses the least number of characters required to represent the number, otherwise pads the result with zeros up to the specified number of places.

Using the BIN2OCT function 
---------------------------

*   The input number must contain only zeros and ones and be less than 10 characters long, otherwise the function returns the #NUM! error value.
*   The first bit of the binary number indicates whether the number is positive or negative. The other nine digits represent the size of the number, the max of which is 511 (2^9 - 1). A negative binary number is expected to use the two's complement notation.

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

*   [Microsoft BIN2OCT function documentation](https://support.office.com/en-us/article/bin2oct-function-0a4e01ba-ac8d-4158-9b29-16c25c4c23fd)
    

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
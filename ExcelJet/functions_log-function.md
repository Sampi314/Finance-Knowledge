# Excel LOG function | Exceljet

**Source:** https://exceljet.net/functions/log-function

---

[Skip to main content](https://exceljet.net/functions/log-function#main-content)

[](https://exceljet.net/functions/log-function#)

*   [Previous](https://exceljet.net/functions/ln-function)
    
*   [Next](https://exceljet.net/functions/log10-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

LOG Function
============

by Dave Bruns · Updated 13 Sep 2021

Related functions 
------------------

[LOG10](https://exceljet.net/functions/log10-function)

![Excel LOG function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_log_new.png "Excel LOG function")

Summary
-------

The Excel LOG function returns the logarithm of a given number, using a supplied base. The base argument defaults to 10 if not supplied.

Purpose 
--------

Get the logarithm of a number

Return value 
-------------

The logarithm

Syntax
------

    =LOG(number,[base])

*   _number_ - Number for which you want the logarithm.
*   _base_ - \[optional\] Base of the logarithm. Defaults to 10.

Using the LOG function 
-----------------------

The LOG function returns the logarithm of a given number, using the provided base.

The LOG function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _number_ and _base_. The value provided for _number_ should be a positive real number. The _base_ argument represents the base of the logarithm. _Base_ is optional and defaults to 10 if not provided.

### Examples

The logarithm of 16 with base 2 (the power to which 2 must be raised to equal 16) is 4:

    =LOG(16, 2) // returns 4
    

The logarithm of 100 with base 10 (the power to which 10 must be raised to equal 100) is 2:

    =LOG(100,10) // returns 2
    

Because the base argument defaults to 10, the formulas below are equivalent:

    =LOG(100,10) // returns 2
    =LOG(100) // returns 2
    

The [LOG10 function](https://exceljet.net/functions/log10-function)
 also returns the base 10 logarithm of a number:

    =LOG10(100) // returns 2
    =LOG10(1000) // returns 3
    

### Notes

*   If _number_ or _base_ are not numeric, LOG returns #VALUE!
*   The [LOG10 function](https://exceljet.net/functions/log10-function)
     also returns the base 10 logarithm of a number.

Related functions
-----------------

[![Excel LOG10 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_log10_new.png "Excel LOG10 function")](https://exceljet.net/functions/log10-function)

### [LOG10 Function](https://exceljet.net/functions/log10-function)

The Excel LOG10 function returns the base 10 logarithm of a number. For example, LOG10(100) returns 2, and LOG10(1000) returns 3.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [LOG10 Function](https://exceljet.net/functions/log10-function)
    

### Links

*   [Microsoft LOG function documentation](https://support.office.com/en-us/article/log-function-4e82f196-1ca9-4747-8fb0-6c4a3abb3280)
    

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
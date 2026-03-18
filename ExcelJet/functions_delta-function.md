# Excel DELTA function | Exceljet

**Source:** https://exceljet.net/functions/delta-function

---

[Skip to main content](https://exceljet.net/functions/delta-function#main-content)

[](https://exceljet.net/functions/delta-function#)

*   [Previous](https://exceljet.net/functions/dec2oct-function)
    
*   [Next](https://exceljet.net/functions/hex2bin-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

DELTA Function
==============

by Dave Bruns · Updated 22 Oct 2018

![Excel DELTA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_delta_function.png "Excel DELTA function")

Summary
-------

The Excel DELTA function will test if two numeric values are equal. When values are equal, DELTA returns 1, otherwise, DELTA returns zero.

Purpose 
--------

Test two values are equal

Return value 
-------------

The number one or zero

Syntax
------

    =DELTA(number1,[number2])

*   _number1_ - The first number.
*   _number2_ - \[optional\] The second number.

Using the DELTA function 
-------------------------

The DELTA function tests two numeric values for equality. When values are equal, DELTA returns 1. When values are different, DELTA returns zero. As a result, DELTA can be used to easily count pairs of equal numbers.

For example:

    =DELTA(5,4) // returns 0
    =DELTA(3,3) // returns 1
    

In the example shown, the formula in D6, copied down, is:

    =DELTA(B6,C6)
    

Notes:

1.  If number2 is left blank, DELTA assumes number2 equals zero
2.  If either value is text, DELTA returns the #VALUE error.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Links

*   [Microsoft DELTA function documentation](https://support.office.com/en-us/article/delta-function-2f763672-c959-4e07-ac33-fe03220ba432)
    

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
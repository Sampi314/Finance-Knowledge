# Excel IMPOWER function | Exceljet

**Source:** https://exceljet.net/functions/impower-function

---

[Skip to main content](https://exceljet.net/functions/impower-function#main-content)

[](https://exceljet.net/functions/impower-function#)

*   [Previous](https://exceljet.net/functions/imlog2-function)
    
*   [Next](https://exceljet.net/functions/improduct-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMPOWER Function
================

by Dave Bruns · Updated 20 Aug 2021

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

![Excel IMPOWER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_impower_function.png "Excel IMPOWER function")

Summary
-------

The Excel IMPOWER function returns a complex number raised to a given power. The complex number must be in the form x + yi or x + yj. Use the [COMPLEX function](https://exceljet.net/functions/complex-function)
 to create a complex number from real and imaginary parts.

Purpose 
--------

Raise complex number to given power

Return value 
-------------

Complex number as text

Syntax
------

    =IMPOWER(inumber,number)

*   _inumber_ - A complex number.
*   _number_ - Power to raise number.

Using the IMPOWER function 
---------------------------

The Excel IMPOWER function returns a complex number raised to a given power. The complex number is input as text, and must be in the form x + yi or x + yj.

For example:

    =IMPOWER("1+2i",2) // returns "-3+4i"
    
    

In the example shown, the formula in D6, copied down, is:

    =IMPOWER(B6,C6)
    

Notes:

*   Only lowercase "j" and "i" are accepted by IMPOWER. Other values will result in the #NUM error.
*   The **number** argument must be numeric

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMREAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imreal_screenshot_cropped.png "Excel IMREAL function")](https://exceljet.net/functions/imreal-function)

### [IMREAL Function](https://exceljet.net/functions/imreal-function)

The Excel IMREAL function returns the real part of a complex number.

[![Excel IMAGINARY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imaginary_screenshot_cropped.png "Excel IMAGINARY function")](https://exceljet.net/functions/imaginary-function)

### [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)

The Excel IMAGINARY function returns the imaginary part of a complex number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    
*   [IMREAL Function](https://exceljet.net/functions/imreal-function)
    
*   [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)
    

### Links

*   [Microsoft IMPOWER function documentation](https://support.office.com/en-us/article/impower-function-210fd2f5-f8ff-4c6a-9d60-30e34fbdef39)
    

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
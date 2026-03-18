# Excel IMSUB function | Exceljet

**Source:** https://exceljet.net/functions/imsub-function

---

[Skip to main content](https://exceljet.net/functions/imsub-function#main-content)

[](https://exceljet.net/functions/imsub-function#)

*   [Previous](https://exceljet.net/functions/imsqrt-function)
    
*   [Next](https://exceljet.net/functions/imsum-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMSUB Function
==============

by Dave Bruns · Updated 8 Jan 2025

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

[IMSUM](https://exceljet.net/functions/imsum-function)

[IMPRODUCT](https://exceljet.net/functions/improduct-function)

![Excel IMSUB function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imsub_function.png "Excel IMSUB function")

Summary
-------

The Excel IMSUB function returns the difference between two complex numbers.

Purpose 
--------

Get difference between two complex numbers

Return value 
-------------

Difference between complex numbers as text

Syntax
------

    =IMSUB(inumber1,inumber2)

*   _inumber1_ - Complex number 1.
*   _inumber2_ - Complex number 2.

Using the IMSUB function 
-------------------------

The IMSUB function returns the difference between two complex numbers. For example:

    =IMSUB("4+3i","1+2i") // returns "3+i"

> Excel handles complex numbers as strings formatted like "x+yi" or "x+yj". Use the [COMPLEX](https://exceljet.net/functions/complex-function)
>  function to get the string representing a complex number.

### Explanation

The result of the IMSUB function can be visualized by adding the opposite of the second vector tip-to-tail with the first. For example, the result of the subtraction below

    =IMSUB("4+3i","-2+5i") // returns "6-2i"

is visualized like this:

![Visualization of complex subtraction.](https://exceljet.net/sites/default/files/images/functions/inline/ComplexSubtraction.png "Visualization of complex subtraction.")

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

[![Excel IMSUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imsum_function_0.png "Excel IMSUM function")](https://exceljet.net/functions/imsum-function)

### [IMSUM Function](https://exceljet.net/functions/imsum-function)

The Excel IMSUM function returns the sum of two or more complex numbers.

[![Excel IMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_improduct_function_screenshot_cropped_0.png "Excel IMPRODUCT function")](https://exceljet.net/functions/improduct-function)

### [IMPRODUCT Function](https://exceljet.net/functions/improduct-function)

The Excel IMPRODUCT function returns the product of one or more complex numbers.

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
    
*   [IMSUM Function](https://exceljet.net/functions/imsum-function)
    
*   [IMPRODUCT Function](https://exceljet.net/functions/improduct-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMSUB function documentation](https://support.office.com/en-us/article/imsub-function-2e404b4d-4935-4e85-9f52-cb08b9a45054)
    

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
# Excel IMAGINARY function | Exceljet

**Source:** https://exceljet.net/functions/imaginary-function

---

[Skip to main content](https://exceljet.net/functions/imaginary-function#main-content)

[](https://exceljet.net/functions/imaginary-function#)

*   [Previous](https://exceljet.net/functions/imabs-function)
    
*   [Next](https://exceljet.net/functions/imargument-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMAGINARY Function
==================

by Dave Bruns · Updated 28 Nov 2024

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMABS](https://exceljet.net/functions/imabs-function)

[IMARGUMENT](https://exceljet.net/functions/imargument-function)

![Excel IMAGINARY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imaginary_screenshot_cropped.png "Excel IMAGINARY function")

Summary
-------

The Excel IMAGINARY function returns the imaginary part of a complex number.

Purpose 
--------

Get the imaginary part of a complex number

Return value 
-------------

The imaginary part of a complex number

Syntax
------

    =IMAGINARY(inumber)

*   _inumber_ - The string representing a complex number.

Using the IMAGINARY function 
-----------------------------

The Excel IMAGINARY function returns the imaginary part of a complex number. For example:

    =IMAGINARY("4+3i") // returns 3
    

> Excel handles complex numbers as strings formatted like "x+yi" or "x+yj". Use the [COMPLEX](https://exceljet.net/functions/complex-function)
>  function to get the string representing a complex number.

### Explanation

A complex number is drawn as an arrow in the complex plane, where the horizontal axis corresponds to the real part of the number and the vertical axis corresponds to the imaginary part of the number. For example, the complex number "2-5i" is drawn below.

![A complex number is drawn as an arrow in the complex plane.](https://exceljet.net/sites/default/files/images/functions/inline/DrawAsArrow_0.png "A complex number is drawn as an arrow in the complex plane.")

The IMAGINARY function returns the vertical component of the complex number.

    =IMAGINARY("2-5i") // returns -5
    

**Notes:**

*   IMAGINARY returns a #NUM error when the input does not represent a valid complex number.

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMREAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imreal_screenshot_cropped.png "Excel IMREAL function")](https://exceljet.net/functions/imreal-function)

### [IMREAL Function](https://exceljet.net/functions/imreal-function)

The Excel IMREAL function returns the real part of a complex number.

[![Excel IMABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imabs_screenshot_cropped.png "Excel IMABS function")](https://exceljet.net/functions/imabs-function)

### [IMABS Function](https://exceljet.net/functions/imabs-function)

The Excel IMABS function returns the absolute value of a complex number.

[![Excel IMARGUMENT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imargument_function_screenshot_cropped_0.png "Excel IMARGUMENT function")](https://exceljet.net/functions/imargument-function)

### [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)

The Excel IMARGUMENT function returns the angle of a complex number expressed in radians. The **argument**, also known as the phase, is the angle between the positive real axis and the line the complex number lies on in the complex plane.

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
    
*   [IMABS Function](https://exceljet.net/functions/imabs-function)
    
*   [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMAGINARY function documentation](https://support.office.com/en-us/article/imaginary-function-dd5952fd-473d-44d9-95a1-9a17b23e428a)
    

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
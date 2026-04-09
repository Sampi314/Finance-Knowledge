# Excel IMABS function | Exceljet

**Source:** https://exceljet.net/functions/imabs-function

---

[Skip to main content](https://exceljet.net/functions/imabs-function#main-content)

[](https://exceljet.net/functions/imabs-function#)

*   [Previous](https://exceljet.net/functions/hex2oct-function)
    
*   [Next](https://exceljet.net/functions/imaginary-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMABS Function
==============

by Dave Bruns · Updated 28 Nov 2024

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMARGUMENT](https://exceljet.net/functions/imargument-function)

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

![Excel IMABS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imabs_screenshot_cropped.png "Excel IMABS function")

Summary
-------

The Excel IMABS function returns the absolute value of a complex number.

Purpose 
--------

Get the absolute value of a complex number

Return value 
-------------

The absolute value of a complex number

Syntax
------

    =IMABS(inumber)

*   _inumber_ - The string representing a complex number.

Using the IMABS function 
-------------------------

The Excel IMABS function returns the absolute value of a complex number. For example:

    =IMABS("4+3i") // returns 5
    

> Excel handles complex numbers as strings formatted like "x+yi" or "x+yj". Use the [COMPLEX](https://exceljet.net/functions/complex-function)
>  function to get the string representing a complex number.

### Explanation

The absolute value of a complex number goes by several other names: modulus, length, or magnitude. All of them refer to the same thing. When we draw the arrow representing a complex number, the absolute value is equal to the distance from the origin to the tip of the complex number.

![The absolute value of a complex number.](https://exceljet.net/sites/default/files/images/functions/inline/DistanceFromOriginToTip.png "The absolute value of a complex number.")

The IMABS function always returns a positive number. For example, consider the complex number "-12-5i" which points in a different direction.

![The absolute value of a complex number pointing in a different direction.](https://exceljet.net/sites/default/files/images/functions/inline/DistanceFromOriginToTipOtherDirection.png "The absolute value of a complex number pointing in a different direction.")

The absolute value of this complex number is positive 13.

    =IMABS("-12-5i") // returns 13
    

In general, the absolute value of a complex number "z=x+yi" is given by the formula below.

    =SQRT(x^2 + y^2)
    

### Notes

*   IMABS returns a #NUM error when the input does not represent a valid complex number.

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMARGUMENT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imargument_function_screenshot_cropped_0.png "Excel IMARGUMENT function")](https://exceljet.net/functions/imargument-function)

### [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)

The Excel IMARGUMENT function returns the angle of a complex number expressed in radians. The **argument**, also known as the phase, is the angle between the positive real axis and the line the complex number lies on in the complex plane.

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
    
*   [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)
    
*   [IMREAL Function](https://exceljet.net/functions/imreal-function)
    
*   [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMABS function documentation](https://support.office.com/en-us/article/imabs-function-b31e73c6-d90c-4062-90bc-8eb351d765a1)
    

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
# Excel IMSQRT function | Exceljet

**Source:** https://exceljet.net/functions/imsqrt-function

---

[Skip to main content](https://exceljet.net/functions/imsqrt-function#main-content)

[](https://exceljet.net/functions/imsqrt-function#)

*   [Previous](https://exceljet.net/functions/imsinh-function)
    
*   [Next](https://exceljet.net/functions/imsub-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMSQRT Function
===============

by Dave Bruns · Updated 31 Jan 2025

Related functions 
------------------

[IMPOWER](https://exceljet.net/functions/impower-function)

[IMABS](https://exceljet.net/functions/imabs-function)

[IMARGUMENT](https://exceljet.net/functions/imargument-function)

[COMPLEX](https://exceljet.net/functions/complex-function)

![Excel IMSQRT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imsqrt_screenshot_cropped_0.png "Excel IMSQRT function")

Summary
-------

The Excel IMSQRT function returns the square root of a complex number.

Purpose 
--------

Get square root of a complex number

Return value 
-------------

The square root of the complex number.

Syntax
------

    =IMSQRT(inumber)

*   _inumber_ - A string representing a complex number.

Using the IMSQRT function 
--------------------------

The Excel IMSQRT function returns the square root of a complex number. For example:

    =IMSQRT("3+4i") // returns "2+i"

> Excel handles complex numbers as strings formatted like "x+yi" or "x+yj". Use the [COMPLEX](https://exceljet.net/functions/complex-function)
>  function to get the string representing a complex number.

### Basic Example

The IMSQRT function returns the complex number's **principal square root** (the one with a non-negative real part). For example:

    =IMSQRT("2i") // returns "1+i"

The two possible square roots of "2i" are "1+i" and "-1-i", so "1+i" is returned because it has a non-negative real part.

### Square Root of Negative One Example

A fundamental property of complex numbers is that the square root of "-1" is "i". However, when you take the square root of "-1", the result contains a tiny error due to how Excel handles floating-point arithmetic.

    =IMSQRT("-1") // returns "6.12323399573677E-17+i"

The real part of the return value is a very small number close to zero. For practical purposes, it can be interpreted as just "i".

### Explanation

The square root of a complex number is given by:

![Definition of complex square root.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imsqrt_definition_0.png "Definition of complex square root.")

Where "r" is equal to the radius of the complex number and "θ" is equal to the angle of the complex number for the branch cut extending from -π to π (excluding -π).

In Excel, we can write the formula equivalent to the complex square root function like this, where B6 contains a string representing a complex number:

    =LET(
    r, IMABS(B6),
    t, IMARGUMENT(B6),
    COMPLEX(SQRT(r)*COS(t/2),SQRT(r)*SIN(t/2))
    )

### Notes

*   Excel's IMSQRT function always returns the **principal root** with a non-negative real part.
    
*   If the input is not a valid complex number, IMSQRT will return the **#NUM!** Error.
    

Related functions
-----------------

[![Excel IMPOWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_impower_function.png "Excel IMPOWER function")](https://exceljet.net/functions/impower-function)

### [IMPOWER Function](https://exceljet.net/functions/impower-function)

The Excel IMPOWER function returns a complex number raised to a given power. The complex number must be in the form x + yi or x + yj. Use the [COMPLEX function](https://exceljet.net/functions/complex-function)
 to create a complex number from real and imaginary parts.

[![Excel IMABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imabs_screenshot_cropped.png "Excel IMABS function")](https://exceljet.net/functions/imabs-function)

### [IMABS Function](https://exceljet.net/functions/imabs-function)

The Excel IMABS function returns the absolute value of a complex number.

[![Excel IMARGUMENT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imargument_function_screenshot_cropped_0.png "Excel IMARGUMENT function")](https://exceljet.net/functions/imargument-function)

### [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)

The Excel IMARGUMENT function returns the angle of a complex number expressed in radians. The **argument**, also known as the phase, is the angle between the positive real axis and the line the complex number lies on in the complex plane.

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IMPOWER Function](https://exceljet.net/functions/impower-function)
    
*   [IMABS Function](https://exceljet.net/functions/imabs-function)
    
*   [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)
    
*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMSQRT function documentation](https://support.office.com/en-us/article/imsqrt-function-e1753f80-ba11-4664-a10e-e17368396b70)
    

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
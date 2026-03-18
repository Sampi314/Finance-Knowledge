# Excel IMARGUMENT function | Exceljet

**Source:** https://exceljet.net/functions/imargument-function

---

[Skip to main content](https://exceljet.net/functions/imargument-function#main-content)

[](https://exceljet.net/functions/imargument-function#)

*   [Previous](https://exceljet.net/functions/imaginary-function)
    
*   [Next](https://exceljet.net/functions/imconjugate-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMARGUMENT Function
===================

by Dave Bruns · Updated 9 Dec 2024

Related functions 
------------------

[ATAN2](https://exceljet.net/functions/atan2-function)

[IMLN](https://exceljet.net/functions/imln-function)

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

![Excel IMARGUMENT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imargument_function_screenshot_cropped_0.png "Excel IMARGUMENT function")

Summary
-------

The Excel IMARGUMENT function returns the angle of a complex number expressed in radians. The **argument**, also known as the phase, is the angle between the positive real axis and the line the complex number lies on in the complex plane.

Purpose 
--------

Get the angle of a complex number

Return value 
-------------

The angle measured in radians

Syntax
------

    =IMARGUMENT(inumber)

*   _inumber_ - The complex number in the form "x+yi".

Using the IMARGUMENT function 
------------------------------

The Excel IMARGUMENT function returns the angle of a complex number measured in radians. For example, given the complex number "3+4i" the function returns the angle 0.927295218.

    =IMARGUMENT("3+4i") // returns 0.927295218
    

> Excel handles complex numbers as strings formatted like "x+yi" or "x+yj". Use the [COMPLEX](https://exceljet.net/functions/complex-function)
>  function to get the string representing a complex number.

Geometrically, this value represents the angle between the positive real axis and the line on which the complex number lies in the complex plane.

![Angle of the complex number 3+4i.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_imargument_function_angle_of_complex_number.png "Angle of the complex number 3+4i.")

To convert the angle to degrees, use the DEGREES function.

    =DEGREES(IMARGUMENT(COMPLEX(3,4))) // returns 53.13°

### Explanation

Given a complex number, many equivalent angles correspond to the line on which the number lies. For example, consider the complex number "-5-5i" in the complex plane. Starting from the positive real axis, you can rotate 225 degrees in the positive direction, or you can also rotate negative 135 degrees to get to "-5-5i".

![Positive and negative angle of a complex number.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_imargument_function_positive_and_negative_angle.png "Positive and negative angle of a complex number.")

The IMARGUMENT function always returns angles in the range from -π to π radians. For the complex number "-5-5i" the function returns the angle -3/4 π.

    =IMARGUMENT(COMPLEX(-5, -5)) // returns -3/4π

For complex numbers that lie on the negative real axis, the function returns π radians.

    =IMARGUMENT(COMPLEX(-5, 0)) // returns π

In other words, the range excludes -π  and includes π. Given a complex number just below the negative real axis, the function returns an angle really close to, but not quite equal to -π.

    =IMARGUMENT(COMPLEX(-5, -0.01)) // returns -3.131592987
    

### Notes

*   Given zero the function returns a #DIV/0! error.

Related functions
-----------------

[![Excel ATAN2 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_atan2.png "Excel ATAN2 function")](https://exceljet.net/functions/atan2-function)

### [ATAN2 Function](https://exceljet.net/functions/atan2-function)

The Excel ATAN2 function returns the arctangent from x- and y-coordinates. In geometric terms, the function returns the radian angle corresponding to the input point.

[![Excel IMLN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imln_function_screenshot_cropped.png "Excel IMLN function")](https://exceljet.net/functions/imln-function)

### [IMLN Function](https://exceljet.net/functions/imln-function)

The Excel IMLN function returns the natural logarithm of a complex number.

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

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

*   [ATAN2 Function](https://exceljet.net/functions/atan2-function)
    
*   [IMLN Function](https://exceljet.net/functions/imln-function)
    
*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    
*   [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMARGUMENT function documentation](https://support.office.com/en-us/article/imargument-function-eed37ec1-23b3-4f59-b9f3-d340358a034a)
    

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
# Excel IMSINH function | Exceljet

**Source:** https://exceljet.net/functions/imsinh-function

---

[Skip to main content](https://exceljet.net/functions/imsinh-function#main-content)

[](https://exceljet.net/functions/imsinh-function#)

*   [Previous](https://exceljet.net/functions/imsin-function)
    
*   [Next](https://exceljet.net/functions/imsqrt-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

IMSINH Function
===============

by Dave Bruns · Updated 11 Nov 2024

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[SINH](https://exceljet.net/functions/sinh-function)

[SIN](https://exceljet.net/functions/sin-function)

![Excel IMSINH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imsinh_screenshot_cropped.png "Excel IMSINH function")

Summary
-------

The Excel IMSINH function returns the hyperbolic sine of a complex number.

Purpose 
--------

Get hyperbolic sine of the complex number.

Return value 
-------------

The hyperbolic sine of the complex number.

Syntax
------

    =IMSINH(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMSINH function 
--------------------------

The Excel IMSINH function returns the hyperbolic sine of a complex number. For example, given 1+π/2i as input, the function returns -4.10319E-15 + 1.543080635i as output.

    =IMSINH(COMPLEX(1, PI()/2)) // returns -4.10319E-15 + 1.543080635i

When the function's output is plotted over the complex plane, the real output along the real axis traces the shape of the [SINH function](https://exceljet.net/functions/sinh-function)
.

    =IMSINH(COMPLEX(x,0)) // returns SINH(x) + 0i

The imaginary output along the imaginary axis traces the shape of the [SIN function](https://exceljet.net/functions/sin-function)
.

    =IMSINH(COMPLEX(0,y)) // returns 0 + SIN(y)i

### Explanation

The function can be defined for complex input using the [SIN](https://exceljet.net/functions/sin-function)
, [COS](https://exceljet.net/functions/cos-function)
, [SINH](https://exceljet.net/functions/sinh-function)
, and [COSH](https://exceljet.net/functions/cosh-function)
 functions, which take real numbers as input.

![IMSINH function definition.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imsinh_function_definition.png "IMSINH function definition.")

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel SINH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sinh_screenshot_cropped.png "Excel SINH function")](https://exceljet.net/functions/sinh-function)

### [SINH Function](https://exceljet.net/functions/sinh-function)

The Excel SINH function returns the hyperbolic sine of a number.

[![Excel SIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sin_2.png "Excel SIN function")](https://exceljet.net/functions/sin-function)

### [SIN Function](https://exceljet.net/functions/sin-function)

The Excel SIN function returns the sine of an angle given in radians. To supply an angle to SIN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

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
    
*   [SINH Function](https://exceljet.net/functions/sinh-function)
    
*   [SIN Function](https://exceljet.net/functions/sin-function)
    

### Links

*   [Microsoft IMSINH function documentation](https://support.office.com/en-us/article/imsinh-function-dfb9ec9e-8783-4985-8c42-b028e9e8da3d)
    

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
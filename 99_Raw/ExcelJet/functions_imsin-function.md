# Excel IMSIN function | Exceljet

**Source:** https://exceljet.net/functions/imsin-function

---

[Skip to main content](https://exceljet.net/functions/imsin-function#main-content)

[](https://exceljet.net/functions/imsin-function#)

*   [Previous](https://exceljet.net/functions/imsech-function)
    
*   [Next](https://exceljet.net/functions/imsinh-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMSIN Function
==============

by Dave Bruns · Updated 1 Oct 2024

Related functions 
------------------

[IMCOS](https://exceljet.net/functions/imcos-function)

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

[SIN](https://exceljet.net/functions/sin-function)

![Excel IMSIN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imsin_function_screenshot_cropped.png "Excel IMSIN function")

Summary
-------

The Excel IMSIN function returns the sine of a complex number.

Purpose 
--------

Get sine of complex number.

Return value 
-------------

Returns the sine of the complex number.

Syntax
------

    =IMSIN(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMSIN function 
-------------------------

The Excel IMSIN function returns the sine of a complex number. For instance, given "1+1i" as input, the function returns the complex number equal to the sine of the input.

    =IMSIN("1+1i") // returns 1.29845758141598+0.634963914784736i

Given real number input, the function behaves like the sine function. For example, given π + 0i as input the function returns 3.23108914886517E-15 (approximately zero). The sine of π is zero, but due to floating-point precision, it returns a very small number close to zero.

    =IMSIN(COMPLEX(PI(),0)) // returns 3.23108914886517E-15

### Explanation

Mathematically, the sine of a complex number can be represented using a combination of the standard and hyperbolic trigonometric functions.

![Definition of sine for a complex number.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imsin_function_definition.png "Definition of sine for a complex number.")

If B6 contains a complex number in the form "x+yi", this is equivalent to the following formula.

    =COMPLEX(
        SIN(IMREAL(B6))*COSH(IMAGINARY(B6)),
        COS(IMREAL(B6))*SINH(IMAGINARY(B6))
    )

Alternatively, the sine of a complex number can be defined in terms of the exponential function, where "z=x+yi".

![Sine of a complex number in terms of the exponential function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imsin_function_definition_exp.png "Sine of a complex number in terms of the exponential function.")

If B6 contains a complex number in the form "x+yi", this is equivalent to the following formula.

    =IMDIV(
        IMSUB(
            IMEXP(IMPRODUCT(COMPLEX(0,1), B6)), 
            IMEXP(IMPRODUCT(COMPLEX(0,-1), B6))
        ),
        COMPLEX(0, 2)
    )

Related functions
-----------------

[![Excel IMCOS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imcos_function.png "Excel IMCOS function")](https://exceljet.net/functions/imcos-function)

### [IMCOS Function](https://exceljet.net/functions/imcos-function)

The Excel IMCOS function returns the cosine of a complex number.

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMREAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imreal_screenshot_cropped.png "Excel IMREAL function")](https://exceljet.net/functions/imreal-function)

### [IMREAL Function](https://exceljet.net/functions/imreal-function)

The Excel IMREAL function returns the real part of a complex number.

[![Excel IMAGINARY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imaginary_screenshot_cropped.png "Excel IMAGINARY function")](https://exceljet.net/functions/imaginary-function)

### [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)

The Excel IMAGINARY function returns the imaginary part of a complex number.

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

*   [IMCOS Function](https://exceljet.net/functions/imcos-function)
    
*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    
*   [IMREAL Function](https://exceljet.net/functions/imreal-function)
    
*   [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)
    
*   [SIN Function](https://exceljet.net/functions/sin-function)
    

### Links

*   [Microsoft IMSIN function documentation](https://support.office.com/en-us/article/imsin-function-1ab02a39-a721-48de-82ef-f52bf37859f6)
    

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
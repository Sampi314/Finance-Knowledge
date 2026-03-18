# Excel IMCOS function | Exceljet

**Source:** https://exceljet.net/functions/imcos-function

---

[Skip to main content](https://exceljet.net/functions/imcos-function#main-content)

[](https://exceljet.net/functions/imcos-function#)

*   [Previous](https://exceljet.net/functions/imconjugate-function)
    
*   [Next](https://exceljet.net/functions/imcosh-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMCOS Function
==============

by Dave Bruns · Updated 1 Oct 2024

Related functions 
------------------

[IMSIN](https://exceljet.net/functions/imsin-function)

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

[COS](https://exceljet.net/functions/cos-function)

![Excel IMCOS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imcos_function.png "Excel IMCOS function")

Summary
-------

The Excel IMCOS function returns the cosine of a complex number.

Purpose 
--------

Get cosine of complex number.

Return value 
-------------

Returns the cosine of the complex number.

Syntax
------

    =IMCOS(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMCOS function 
-------------------------

The Excel IMCOS function returns the cosine of a complex number. For instance, given “1 + 1i” as input, the function returns a complex number equal to the cosine of the input.

    =IMCOS(COMPLEX(1,1)) // returns 0.833730025131149-0.988897705762865i

Given real number input, the function behaves like the cosine function. For instance, when π/2 + 0i is provided as input, the function returns -3.49148133884313E-15 (approximately zero). The cosine of π/2 is zero, but due to floating-point precision, it returns a very small number close to zero.

    =IMCOS(COMPLEX(PI()/2,0)) // returns approximately 0

### Explanation

Mathematically, the cosine of a complex number can be represented using a combination of the standard and hyperbolic trigonometric functions.

![Cosine of a complex number.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imcos_function_equivalent_version.png)

If B6 contains a complex number in the form "x+yi", this is equivalent to the following formula.

    =COMPLEX(
        COS(IMREAL(B6))*COSH(IMAGINARY(B6)),
        -SIN(IMREAL(B6))*SINH(IMAGINARY(B6))
    )

Alternatively, the cosine of a complex number can also be represented using the exponential function, where "z=x+yi."

![Equivalent form of cosine of a complex number using the exponential function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imcos_function_equivalent_version_alt.png)

If B6 contains a complex number in the form "x+yi", this is equivalent to the following formula.

    =IMDIV(
        IMSUM(
            IMEXP(IMPRODUCT(COMPLEX(0,1), B6)), 
            IMEXP(IMPRODUCT(COMPLEX(0,-1), B6))
        ),
        2
    )

Related functions
-----------------

[![Excel IMSIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imsin_function_screenshot_cropped.png "Excel IMSIN function")](https://exceljet.net/functions/imsin-function)

### [IMSIN Function](https://exceljet.net/functions/imsin-function)

The Excel IMSIN function returns the sine of a complex number.

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMREAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imreal_screenshot_cropped.png "Excel IMREAL function")](https://exceljet.net/functions/imreal-function)

### [IMREAL Function](https://exceljet.net/functions/imreal-function)

The Excel IMREAL function returns the real part of a complex number.

[![Excel IMAGINARY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imaginary_screenshot_cropped.png "Excel IMAGINARY function")](https://exceljet.net/functions/imaginary-function)

### [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)

The Excel IMAGINARY function returns the imaginary part of a complex number.

[![Excel COS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cos_2_0.png "Excel COS function")](https://exceljet.net/functions/cos-function)

### [COS Function](https://exceljet.net/functions/cos-function)

The Excel COS function returns the cosine of an angle given in radians. To supply an angle to COS in degrees, use the RADIANS function to convert to radians.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IMSIN Function](https://exceljet.net/functions/imsin-function)
    
*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    
*   [IMREAL Function](https://exceljet.net/functions/imreal-function)
    
*   [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)
    
*   [COS Function](https://exceljet.net/functions/cos-function)
    

### Links

*   [Microsoft IMCOS function documentation](https://support.office.com/en-us/article/imcos-function-dad75277-f592-4a6b-ad6c-be93a808a53c)
    

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
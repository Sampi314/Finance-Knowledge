# Excel IMTAN function | Exceljet

**Source:** https://exceljet.net/functions/imtan-function

---

[Skip to main content](https://exceljet.net/functions/imtan-function#main-content)

[](https://exceljet.net/functions/imtan-function#)

*   [Previous](https://exceljet.net/functions/imsum-function)
    
*   [Next](https://exceljet.net/functions/oct2bin-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

IMTAN Function
==============

by Dave Bruns · Updated 8 Oct 2024

Related functions 
------------------

[TAN](https://exceljet.net/functions/tan-function)

[TANH](https://exceljet.net/functions/tanh-function)

[IMCOS](https://exceljet.net/functions/imcos-function)

[IMSIN](https://exceljet.net/functions/imsin-function)

[COMPLEX](https://exceljet.net/functions/complex-function)

![Excel IMTAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imtan_function_screenshot_cropped.png "Excel IMTAN function")

Summary
-------

The Excel IMTAN function returns the tangent of a complex number. 

Purpose 
--------

Get the tangent of a complex number.

Return value 
-------------

Returns the tangent of the complex number.

Syntax
------

    =IMTAN(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMTAN function 
-------------------------

The Excel IMTAN function returns the tangent of a complex number. For example, given the complex number "3+4i" as input, the function returns "-0.000187346+0.999355987i"

    =IMTAN("3+4i") // returns -0.000187346+0.999355987i

### Explanation

In math, the tangent of a complex number is defined in terms of complex sine and cosine functions.

![Complex tangent definition.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imtan_function_definition.png "Complex tangent definition.")

In Excel, the tangent of a complex number is equivalent to the following formula.

    =IMDIV(IMSIN(z),IMCOS(z)) // equivalent to IMTAN(z)

The 3D plot below visualizes the function's real output. The horizontal XY plane represents input from the complex plane, and the vertical axis represents the function's real output.

![Real output of the complex tangent function.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imtan_function_real_output_0.png "Real output of the complex tangent function.")

The output along the real axis forms the shape of the regular (circular) [tangent function](https://exceljet.net/functions/tan-function)
.

![Real output of the complex tangent function highlight regular tangent.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imtan_function_real_output_highlight_tan_0.png "Real output of the complex tangent function highlight regular tangent.")

The imaginary output of the function is visualized by the 3D plot below.

![Imaginary output of the complex tangent function.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imtan_function_imaginary_output_0.png "Imaginary output of the complex tangent function.")

The output along the imaginary axis forms the shape of the [hyperbolic tangent function](https://exceljet.net/functions/tanh-function)
.

![Imaginary output of the complex tangent function highlight hyperbolic tangent.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imtan_function_imaginary_output_highlight_tanh_0.png "Imaginary output of the complex tangent function highlight hyperbolic tangent.")

Related functions
-----------------

[![Excel TAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tan_function_screenshot_cropped.png "Excel TAN function")](https://exceljet.net/functions/tan-function)

### [TAN Function](https://exceljet.net/functions/tan-function)

The Excel TAN function returns the tangent of the angle given in radians. To supply an angle to TAN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel TANH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tanh_function_screenshot_cropped.png "Excel TANH function")](https://exceljet.net/functions/tanh-function)

### [TANH Function](https://exceljet.net/functions/tanh-function)

The Excel TANH function returns the hyperbolic tangent of a number.

[![Excel IMCOS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imcos_function.png "Excel IMCOS function")](https://exceljet.net/functions/imcos-function)

### [IMCOS Function](https://exceljet.net/functions/imcos-function)

The Excel IMCOS function returns the cosine of a complex number.

[![Excel IMSIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imsin_function_screenshot_cropped.png "Excel IMSIN function")](https://exceljet.net/functions/imsin-function)

### [IMSIN Function](https://exceljet.net/functions/imsin-function)

The Excel IMSIN function returns the sine of a complex number.

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

*   [TAN Function](https://exceljet.net/functions/tan-function)
    
*   [TANH Function](https://exceljet.net/functions/tanh-function)
    
*   [IMCOS Function](https://exceljet.net/functions/imcos-function)
    
*   [IMSIN Function](https://exceljet.net/functions/imsin-function)
    
*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    

### Links

*   [Microsoft IMTAN function documentation](https://support.office.com/en-us/article/imtan-function-8478f45d-610a-43cf-8544-9fc0b553a132)
    

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
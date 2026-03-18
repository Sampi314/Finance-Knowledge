# Excel TAN function | Exceljet

**Source:** https://exceljet.net/functions/tan-function

---

[Skip to main content](https://exceljet.net/functions/tan-function#main-content)

[](https://exceljet.net/functions/tan-function#)

*   [Previous](https://exceljet.net/functions/sinh-function)
    
*   [Next](https://exceljet.net/functions/tanh-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

TAN Function
============

by Dave Bruns · Updated 9 Oct 2024

Related functions 
------------------

[SIN](https://exceljet.net/functions/sin-function)

[COS](https://exceljet.net/functions/cos-function)

[ATAN](https://exceljet.net/functions/atan-function)

[ATAN2](https://exceljet.net/functions/atan2-function)

![Excel TAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_tan_function_screenshot_cropped.png "Excel TAN function")

Summary
-------

The Excel TAN function returns the tangent of the angle given in radians. To supply an angle to TAN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

Purpose 
--------

Get the tangent of an angle

Return value 
-------------

The tangent value.

Syntax
------

    =TAN(number)

*   _number_ - The angle in radians for which you want the tangent.

Using the TAN function 
-----------------------

The TAN function returns the tangent of an angle provided in [radians](https://exceljet.net/glossary/radians)
. For example, given the π/4 as input, the function returns 1.0 as output.

    =TAN(PI()/4) // Returns 1
    

To supply an angle in degrees, use the radians function.

    =TAN(RADIANS(45)) // Returns 1
    

### Explanation

In math, the tangent of an angle is defined as the ratio of the opposite side to the adjacent side of a right triangle.

![Tangent function definition.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_tangent_function_definition.png "Tangent function definition.")

The definition of tangent is extended to all angles by defining the function in terms of the angle formed by a point on the unit circle.

![Tangent function unit circle definition.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_tangent_function_unit_circle_definition.png "Tangent function unit circle definition.")

The plot below visualizes the output of tangent for angles between -π and π. The red lines represent vertical asymptotes where the function diverges to positive and negative infinity.

![Plot of the tangent function with asymptotes.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_tan_function_plot_with_asymptotes.png "Plot of the tangent function with asymptotes.")

Even though the function is undefined at its vertical asymptotes, Excel does not return an error for input at or near these vertical asymptotes. For example, see the following table for input around and including the location of the asymptote at the angle π/2.

![Tangent function output at vertical asymptote.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_tan_function_input_near_vertical_asymptote_screenshot_cropped.png "Tangent function output at vertical asymptote.")

This is because the tangent function is likely defined in terms of the functions sine and cosine like this:

    =SIN(a)/COS(a) // equivalent to TAN(a)
    

It's reasonable to expect that the output of cosine for the angle π/2 should be zero, meaning you would get a division by zero error for tangent at the same input. However, Excel's formula engine calculates this value as a very small value that is close to, but not quite equal to, zero.

    =COS(PI()/2) // returns 6.12323E-17 instead of zero
    

As a result, the tangent of π/2 does not return an error and instead returns a very large value.

    =TAN(PI()/2) // returns 1.63312E+16
    

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel SIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sin_2.png "Excel SIN function")](https://exceljet.net/functions/sin-function)

### [SIN Function](https://exceljet.net/functions/sin-function)

The Excel SIN function returns the sine of an angle given in radians. To supply an angle to SIN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel COS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cos_2_0.png "Excel COS function")](https://exceljet.net/functions/cos-function)

### [COS Function](https://exceljet.net/functions/cos-function)

The Excel COS function returns the cosine of an angle given in radians. To supply an angle to COS in degrees, use the RADIANS function to convert to radians.

[![Excel ATAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_atan_0.png "Excel ATAN function")](https://exceljet.net/functions/atan-function)

### [ATAN Function](https://exceljet.net/functions/atan-function)

The Excel ATAN function returns the inverse tangent of a number. The function is the inverse of TAN.

[![Excel ATAN2 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_atan2.png "Excel ATAN2 function")](https://exceljet.net/functions/atan2-function)

### [ATAN2 Function](https://exceljet.net/functions/atan2-function)

The Excel ATAN2 function returns the arctangent from x- and y-coordinates. In geometric terms, the function returns the radian angle corresponding to the input point.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SIN Function](https://exceljet.net/functions/sin-function)
    
*   [COS Function](https://exceljet.net/functions/cos-function)
    
*   [ATAN Function](https://exceljet.net/functions/atan-function)
    
*   [ATAN2 Function](https://exceljet.net/functions/atan2-function)
    

### Links

*   [Microsoft TAN function documentation](https://support.office.com/en-us/article/tan-function-08851a40-179f-4052-b789-d7f699447401)
    

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
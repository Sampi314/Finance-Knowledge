# Excel TANH function | Exceljet

**Source:** https://exceljet.net/functions/tanh-function

---

[Skip to main content](https://exceljet.net/functions/tanh-function#main-content)

[](https://exceljet.net/functions/tanh-function#)

*   [Previous](https://exceljet.net/functions/tan-function)
    
*   [Next](https://exceljet.net/functions/avedev-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

TANH Function
=============

by Kurt Bruns · Updated 20 Nov 2024

Related functions 
------------------

[COSH](https://exceljet.net/functions/cosh-function)

[SINH](https://exceljet.net/functions/sinh-function)

[TAN](https://exceljet.net/functions/tan-function)

[ATANH](https://exceljet.net/functions/atanh-function)

![Excel TANH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_tanh_function_screenshot_cropped.png "Excel TANH function")

Summary
-------

The Excel TANH function returns the hyperbolic tangent of a number.

Purpose 
--------

Get hyperbolic tangent of a number.

Return value 
-------------

The hyperbolic tangent of the number.

Syntax
------

    =TANH(number)

*   _number_ - The input number.

Using the TANH function 
------------------------

The TANH function returns a number's hyperbolic tangent. Given input -2, the function returns the number -0.96402758 as output.

    =TANH(-2) // returns -0.96402758
    

### Explanation

Just like the circular tangent, the hyperbolic tangent is defined in terms of the hyperbolic sine and hyperbolic cosine.

    =SINH(a)/COSH(a) // definition of TANH(a)
    

Geometrically, the hyperbolic tangent of a number can be interpreted as the slope of the line from the origin to the point on the unit hyperbola corresponding to the number's hyperbolic angle where the hyperbolic angle is half the area under the hyperbola between the origin and that point.

![Hyperbolic tangent geometry.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_hyperbolic_tangent_geometry.png "Hyperbolic tangent geometry.")

For example, given the input of -1 the function returns -0.761594156.

    =TANH(-1) // returns the slope of -0.761594156
    

This value can be interpreted as the slope of the line from the origin to the point corresponding to the hyperbolic angle of -1.

![Hyperbolic tangent geometry example input.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_unit_hyperbola_tanh_example.png "Hyperbolic tangent geometry example input.")

### Plot of TANH

The plot of the hyperbolic tangent is shown below and visualizes the range of possible output of the function.

![Plot of the hyperbolic tangent function.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_tanh_function_plot.png "Plot of the hyperbolic tangent function.")

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel COSH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cosh_screenshot_cropped.png "Excel COSH function")](https://exceljet.net/functions/cosh-function)

### [COSH Function](https://exceljet.net/functions/cosh-function)

The Excel COSH function returns the hyperbolic cosine of a number.

[![Excel SINH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sinh_screenshot_cropped.png "Excel SINH function")](https://exceljet.net/functions/sinh-function)

### [SINH Function](https://exceljet.net/functions/sinh-function)

The Excel SINH function returns the hyperbolic sine of a number.

[![Excel TAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tan_function_screenshot_cropped.png "Excel TAN function")](https://exceljet.net/functions/tan-function)

### [TAN Function](https://exceljet.net/functions/tan-function)

The Excel TAN function returns the tangent of the angle given in radians. To supply an angle to TAN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel ATANH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_atanh_screenshot_cropped.png "Excel ATANH function")](https://exceljet.net/functions/atanh-function)

### [ATANH Function](https://exceljet.net/functions/atanh-function)

The Excel ATANH function returns the inverse hyperbolic tangent of a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COSH Function](https://exceljet.net/functions/cosh-function)
    
*   [SINH Function](https://exceljet.net/functions/sinh-function)
    
*   [TAN Function](https://exceljet.net/functions/tan-function)
    
*   [ATANH Function](https://exceljet.net/functions/atanh-function)
    

### Links

*   [Microsoft TANH function documentation](https://support.office.com/en-us/article/tanh-function-017222f0-a0c3-4f69-9787-b3202295dc6c)
    

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
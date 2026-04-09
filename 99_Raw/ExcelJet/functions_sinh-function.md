# Excel SINH function | Exceljet

**Source:** https://exceljet.net/functions/sinh-function

---

[Skip to main content](https://exceljet.net/functions/sinh-function#main-content)

[](https://exceljet.net/functions/sinh-function#)

*   [Previous](https://exceljet.net/functions/sin-function)
    
*   [Next](https://exceljet.net/functions/tan-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

SINH Function
=============

by Kurt Bruns · Updated 11 Oct 2024

Related functions 
------------------

[COSH](https://exceljet.net/functions/cosh-function)

[TANH](https://exceljet.net/functions/tanh-function)

[ASINH](https://exceljet.net/functions/asinh-function)

![Excel SINH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_sinh_screenshot_cropped.png "Excel SINH function")

Summary
-------

The Excel SINH function returns the hyperbolic sine of a number.

Purpose 
--------

Get hyperbolic sine of a number.

Return value 
-------------

The hyperbolic sine of a number.

Syntax
------

    =SINH(number)

*   _number_ - The hyperbolic angle.

Using the SINH function 
------------------------

The SINH function returns the hyperbolic sine of a number. Given the input 1, the function returns the value 1.175201194.

    =SINH(0) // returns 1.175201194

### Explanation

The hyperbolic sine function returns the vertical component of the point on the right branch (x ≥ 1) of the unit hyperbola corresponding to the [hyperbolic angle](https://exceljet.net/glossary/hyperbolic-angle)
 given as input.

![The hyperbolic sine returns the vertical component of the point formed by the hyperbolic angle.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_sinh_returns_vertical_component.png "The hyperbolic sine returns the vertical component of the point formed by the hyperbolic angle.")

Together with [hyperbolic cosine](https://exceljet.net/functions/cosh-function)
, the functions parameterize the right branch of the unit hyperbola given by the equation x² - y² = 1. In plain language, this means that the two functions trace out the shape of the right branch of the unit hyperbola.

Given a hyperbolic angle corresponding to a point on the hyperbola's curve, SINH returns the _vertical component_ of the point, while COSH returns the horizontal component of the point. For example, given the hyperbolic angle -1, hyperbolic cosine returns the x-component 1.543080635, and hyperbolic sine returns the y-component -1.175201194.

![Hyperbolic sine and cosine on the unit hyperbola.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_cosh_and_sinh_example_0.png "Hyperbolic sine and cosine on the unit hyperbola.")

Here is a table that shows some points on the unit hyperbola formed by COSH and SINH.

![Example hyperbolic angles and the output of COSH and SINH.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_sinh_and_cosh_screenshot_cropped.png "Example hyperbolic angles and the output of COSH and SINH.")

As the hyperbolic angle increases positively, the vertical component goes to infinity, and as the hyperbolic angle increases negatively, the vertical component goes to negative infinity. This is different from the [sine function](https://exceljet.net/functions/cos-function)
, which is periodic and repeats values.

![Hyperbolic sine plot.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_sinh_plot.png "Hyperbolic sine plot.")

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel COSH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cosh_screenshot_cropped.png "Excel COSH function")](https://exceljet.net/functions/cosh-function)

### [COSH Function](https://exceljet.net/functions/cosh-function)

The Excel COSH function returns the hyperbolic cosine of a number.

[![Excel TANH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tanh_function_screenshot_cropped.png "Excel TANH function")](https://exceljet.net/functions/tanh-function)

### [TANH Function](https://exceljet.net/functions/tanh-function)

The Excel TANH function returns the hyperbolic tangent of a number.

[![Excel ASINH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_asinh_screenshot_cropped.png "Excel ASINH function")](https://exceljet.net/functions/asinh-function)

### [ASINH Function](https://exceljet.net/functions/asinh-function)

The Excel ASINH function returns the inverse hyperbolic sine of a number.

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
    
*   [TANH Function](https://exceljet.net/functions/tanh-function)
    
*   [ASINH Function](https://exceljet.net/functions/asinh-function)
    

### Links

*   [Microsoft SINH function documentation](https://support.office.com/en-us/article/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7)
    

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
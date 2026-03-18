# Excel COSH function | Exceljet

**Source:** https://exceljet.net/functions/cosh-function

---

[Skip to main content](https://exceljet.net/functions/cosh-function#main-content)

[](https://exceljet.net/functions/cosh-function#)

*   [Previous](https://exceljet.net/functions/cos-function)
    
*   [Next](https://exceljet.net/functions/cot-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

COSH Function
=============

by Kurt Bruns · Updated 11 Oct 2024

Related functions 
------------------

[SINH](https://exceljet.net/functions/sinh-function)

[TANH](https://exceljet.net/functions/tanh-function)

[ACOSH](https://exceljet.net/functions/acosh-function)

![Excel COSH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_cosh_screenshot_cropped.png "Excel COSH function")

Summary
-------

The Excel COSH function returns the hyperbolic cosine of a number.

Purpose 
--------

Get hyperbolic cosine of a number

Return value 
-------------

The hyperbolic cosine of the number.

Syntax
------

    =COSH(number)

*   _number_ - The hyperbolic angle.

Using the COSH function 
------------------------

The Excel COSH function returns the hyperbolic cosine of a number, which represents a [hyperbolic angle](https://exceljet.net/glossary/hyperbolic-angle)
. Given the input of 1, the function returns the value 1.543080635.

    =COSH(1) // returns 1.543080635
    

### Explanation

The hyperbolic cosine function returns the horizontal component of the point on the right branch (x ≥ 1) of the unit hyperbola corresponding to the hyperbolic angle given as input. 

![The hyperbolic cosine returns the horizontal component of the point on the unit hyperbola.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_cosh_returns_horizontal_component.png "The hyperbolic cosine returns the horizontal component of the point on the unit hyperbola.")

Together with the [hyperbolic sine function](https://exceljet.net/functions/sinh-function)
, the functions parameterize the right branch of the unit hyperbola given by the equation x² - y² = 1. In plain language, this means that the two functions trace out the shape of the right branch of the unit hyperbola. Given a hyperbolic angle corresponding to a point on the hyperbola's curve, COSH returns the horizontal component of the point, while SINH returns the vertical component of the point.

For example, given the hyperbolic angle -1, hyperbolic cosine returns the x-component 1.543080635, and hyperbolic sine returns the y-component -1.175201194.

![Hyperbolic cosine and sine example.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_cosh_and_sinh_example.png "Hyperbolic cosine and sine example.")

Here is a table that shows some points on the unit hyperbola formed by COSH and SINH.

![Hyperbolic cosine and sine table.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_cosh_and_sinh_table_screenshot_cropped.png "Hyperbolic cosine and sine table.")

As the value of the hyperbolic angle gets larger, the horizontal component diverges to infinity. This is different from the [circular cosine function](https://exceljet.net/functions/cos-function)
, which is periodic and repeats values.

![Hyperbolic cosine plot.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_cosh_plot.png "Hyperbolic cosine plot.")

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel SINH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sinh_screenshot_cropped.png "Excel SINH function")](https://exceljet.net/functions/sinh-function)

### [SINH Function](https://exceljet.net/functions/sinh-function)

The Excel SINH function returns the hyperbolic sine of a number.

[![Excel TANH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tanh_function_screenshot_cropped.png "Excel TANH function")](https://exceljet.net/functions/tanh-function)

### [TANH Function](https://exceljet.net/functions/tanh-function)

The Excel TANH function returns the hyperbolic tangent of a number.

[![Excel ACOSH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excljet_acosh_screenshot_cropped.png "Excel ACOSH function")](https://exceljet.net/functions/acosh-function)

### [ACOSH Function](https://exceljet.net/functions/acosh-function)

The Excel ACOSH function returns the inverse hyperbolic cosine of a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SINH Function](https://exceljet.net/functions/sinh-function)
    
*   [TANH Function](https://exceljet.net/functions/tanh-function)
    
*   [ACOSH Function](https://exceljet.net/functions/acosh-function)
    

### Links

*   [Microsoft COSH function documentation](https://support.office.com/en-us/article/cosh-function-e460d426-c471-43e8-9540-a57ff3b70555)
    

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
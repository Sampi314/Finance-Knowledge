# Excel ACOT function | Exceljet

**Source:** https://exceljet.net/functions/acot-function

---

[Skip to main content](https://exceljet.net/functions/acot-function#main-content)

[](https://exceljet.net/functions/acot-function#)

*   [Previous](https://exceljet.net/functions/acosh-function)
    
*   [Next](https://exceljet.net/functions/acoth-function)
    

Excel 2013

[Trigonometry](https://exceljet.net/functions#Trigonometry)

ACOT Function
=============

by Dave Bruns · Updated 20 Nov 2024

Related functions 
------------------

[COT](https://exceljet.net/functions/cot-function)

[ATAN](https://exceljet.net/functions/atan-function)

![Excel ACOT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_acot_screenshot_cropped.png "Excel ACOT function")

Summary
-------

The Excel ACOT function returns the arc cotangent of a number.

Purpose 
--------

Get arccotangent of a number.

Return value 
-------------

The angle in radians.

Syntax
------

    =ACOT(number)

*   _number_ - The value of the cotangent of an angle.

Using the ACOT function 
------------------------

The Excel ACOT function returns the arc cotangent of a number. Given the input 1, the function returns 0.785398163 [radians](https://exceljet.net/glossary/radians)
 as the output.

    =ACOT(1) // Returns 0.785398163 radians
    

### Explanation

The arc cotangent function is the inverse of the cotangent function, with a branch cut that maps to related angles.

    =ACOT(COT(a)) // returns the angle or a branch cut angle

For example, the angle π/4 is mapped to π/4 with no branch cut.

    =ACOT(COT(PI()/4)) // returns π/4

Where the angle -π/2 is mapped to positive π/2 with a branch cut.

    =ACOT(COT(-PI()/2)) // returns positive π/2

In Excel, when we talk about ACOT as the inverse of [COT](https://exceljet.net/functions/cot-function)
, angles outside the range of 0 to π are mapped with a branch cut. Below is the output of the cotangent function with the branch cut highlighted.

![Cotangent plot with highlighted branch cut.](https://exceljet.net/sites/default/files/images/functions/inline/CotangentPlot.png "Cotangent plot with highlighted branch cut.")

Other implementations of the function may have different branch cuts. Below is the plot of the output of the ACOT function in Excel.

![Arc cotangent plot.](https://exceljet.net/sites/default/files/images/functions/inline/ArcCotangentPlot.png "Arc cotangent plot.")

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel COT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cot.png "Excel COT function")](https://exceljet.net/functions/cot-function)

### [COT Function](https://exceljet.net/functions/cot-function)

The Excel COT function returns the cotangent of an angle provided in radians.

[![Excel ATAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_atan_0.png "Excel ATAN function")](https://exceljet.net/functions/atan-function)

### [ATAN Function](https://exceljet.net/functions/atan-function)

The Excel ATAN function returns the inverse tangent of a number. The function is the inverse of TAN.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COT Function](https://exceljet.net/functions/cot-function)
    
*   [ATAN Function](https://exceljet.net/functions/atan-function)
    

### Links

*   [Microsoft ACOT function documentation](https://support.office.com/en-us/article/acot-function-dc7e5008-fe6b-402e-bdd6-2eea8383d905)
    

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
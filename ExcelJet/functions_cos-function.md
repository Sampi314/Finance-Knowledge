# Excel COS function | Exceljet

**Source:** https://exceljet.net/functions/cos-function

---

[Skip to main content](https://exceljet.net/functions/cos-function#main-content)

[](https://exceljet.net/functions/cos-function#)

*   [Previous](https://exceljet.net/functions/atanh-function)
    
*   [Next](https://exceljet.net/functions/cosh-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

COS Function
============

by Dave Bruns · Updated 9 Oct 2024

Related functions 
------------------

[SIN](https://exceljet.net/functions/sin-function)

[TAN](https://exceljet.net/functions/tan-function)

[ACOS](https://exceljet.net/functions/acos-function)

![Excel COS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_cos_2_0.png "Excel COS function")

Summary
-------

The Excel COS function returns the cosine of an angle given in radians. To supply an angle to COS in degrees, use the RADIANS function to convert to radians.

Purpose 
--------

Get the cosine of an angle provided in radians.

Return value 
-------------

The cosine value

Syntax
------

    =COS(number)

*   _number_ - The angle in radians for which you want the cosine.

Using the COS function 
-----------------------

The COS function returns the cosine of an angle provided in radians. In geometric terms, the cosine of an angle returns the ratio of a right triangle's adjacent side over its hypotenuse. For example, the cosine of PI()/6 radians (30°) returns the ratio 0.866.

    =COS(PI()/6) // Returns 0.886
    

### Using Degrees

To supply an angle to COS in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians. For example, to get the COS of 60 degrees, you can use either formula below:

    =COS(60*PI()/180)
    =COS(RADIANS(60))
    

### Explanation

![Graph of Cosine Function](https://exceljet.net/sites/default/files/images/functions/inline/cosine.png "Graph of Cosine Function")

The graph of cosine above visualizes the output of the function for all angles from 0 to a full rotation. Geometrically, the function returns the _x_\-component of the point corresponding to an angle on the unit circle. Since the cosine of an angle returns a ratio, the output of the function will always be in the range \[-1, 1\].

_Graph courtesy of [wumbo.net](https://wumbo.net/)
_

Related functions
-----------------

[![Excel SIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sin_2.png "Excel SIN function")](https://exceljet.net/functions/sin-function)

### [SIN Function](https://exceljet.net/functions/sin-function)

The Excel SIN function returns the sine of an angle given in radians. To supply an angle to SIN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel TAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tan_function_screenshot_cropped.png "Excel TAN function")](https://exceljet.net/functions/tan-function)

### [TAN Function](https://exceljet.net/functions/tan-function)

The Excel TAN function returns the tangent of the angle given in radians. To supply an angle to TAN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel ACOS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_acos_0.png "Excel ACOS function")](https://exceljet.net/functions/acos-function)

### [ACOS Function](https://exceljet.net/functions/acos-function)

The ACOS function returns the inverse cosine of a number. The function is the inverse of COS and expects input in the range from -1 to 1.

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
    
*   [TAN Function](https://exceljet.net/functions/tan-function)
    
*   [ACOS Function](https://exceljet.net/functions/acos-function)
    

### Links

*   [Microsoft COS function documentation](https://support.office.com/en-us/article/cos-function-0fb808a5-95d6-4553-8148-22aebdce5f05)
    

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
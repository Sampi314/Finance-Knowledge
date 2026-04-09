# Excel SIN function | Exceljet

**Source:** https://exceljet.net/functions/sin-function

---

[Skip to main content](https://exceljet.net/functions/sin-function#main-content)

[](https://exceljet.net/functions/sin-function#)

*   [Previous](https://exceljet.net/functions/sech-function)
    
*   [Next](https://exceljet.net/functions/sinh-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

SIN Function
============

by Dave Bruns · Updated 9 Oct 2024

Related functions 
------------------

[COS](https://exceljet.net/functions/cos-function)

[TAN](https://exceljet.net/functions/tan-function)

[RADIANS](https://exceljet.net/functions/radians-function)

[ASIN](https://exceljet.net/functions/asin-function)

![Excel SIN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_sin_2.png "Excel SIN function")

Summary
-------

The Excel SIN function returns the sine of an angle given in radians. To supply an angle to SIN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

Purpose 
--------

Get the sine of an angle provided in radians.

Return value 
-------------

Sine value

Syntax
------

    =SIN(number)

*   _number_ - The angle in radians for which you want the sine.

Using the SIN function 
-----------------------

The SIN function returns the sine of an angle provided in radians. In geometric terms, the sine of an angle returns the ratio of a right triangle's opposite side over its hypotenuse. For example, the sine of PI()/6 radians (30°) returns the ratio 0.5.

    =SIN(PI()/6) // Returns 0.5
    

### Using Degrees

To supply an angle to SIN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians. For example, to get the SIN of 30 degrees, you can use either formula below:

    =SIN(30*PI()/180)
    =SIN(RADIANS(30))
    

### Explanation

![Graph of Sine Function](https://exceljet.net/sites/default/files/images/functions/inline/sine.png "Graph of Sine Function")

The graph of sine, shown above, visualizes the output of the function for all angles from 0 to a full rotation. The function is periodic, so after a full rotation, the output of the function repeats. Geometrically, the function returns the _y_\-component of the point corresponding to an angle on the unit circle. The function's output will always be in the range \[-1, 1\].

_Graph courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel COS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cos_2_0.png "Excel COS function")](https://exceljet.net/functions/cos-function)

### [COS Function](https://exceljet.net/functions/cos-function)

The Excel COS function returns the cosine of an angle given in radians. To supply an angle to COS in degrees, use the RADIANS function to convert to radians.

[![Excel TAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tan_function_screenshot_cropped.png "Excel TAN function")](https://exceljet.net/functions/tan-function)

### [TAN Function](https://exceljet.net/functions/tan-function)

The Excel TAN function returns the tangent of the angle given in radians. To supply an angle to TAN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel RADIANS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_radians_2.png "Excel RADIANS function")](https://exceljet.net/functions/radians-function)

### [RADIANS Function](https://exceljet.net/functions/radians-function)

The Excel RADIANS function converts degrees to radians. For example, =RADIANS(180) returns 3.1415 or the value of π (pi)....

[![Excel ASIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_asin_2.png "Excel ASIN function")](https://exceljet.net/functions/asin-function)

### [ASIN Function](https://exceljet.net/functions/asin-function)

The Excel ASIN function returns the inverse sine of a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COS Function](https://exceljet.net/functions/cos-function)
    
*   [TAN Function](https://exceljet.net/functions/tan-function)
    
*   [RADIANS Function](https://exceljet.net/functions/radians-function)
    
*   [ASIN Function](https://exceljet.net/functions/asin-function)
    

### Links

*   [Microsoft SIN function documentation](https://support.office.com/en-us/article/sin-function-cf0e3432-8b9e-483c-bc55-a76651c95602)
    

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
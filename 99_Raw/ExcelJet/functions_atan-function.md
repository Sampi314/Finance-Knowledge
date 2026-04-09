# Excel ATAN function | Exceljet

**Source:** https://exceljet.net/functions/atan-function

---

[Skip to main content](https://exceljet.net/functions/atan-function#main-content)

[](https://exceljet.net/functions/atan-function#)

*   [Previous](https://exceljet.net/functions/asinh-function)
    
*   [Next](https://exceljet.net/functions/atan2-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

ATAN Function
=============

by Kurt Bruns · Updated 23 Oct 2020

Related functions 
------------------

[ATAN2](https://exceljet.net/functions/atan2-function)

[TAN](https://exceljet.net/functions/tan-function)

[ACOS](https://exceljet.net/functions/acos-function)

[ASIN](https://exceljet.net/functions/asin-function)

![Excel ATAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_atan_0.png "Excel ATAN function")

Summary
-------

The Excel ATAN function returns the inverse tangent of a number. The function is the inverse of TAN.

Purpose 
--------

Get arctangent of a number

Return value 
-------------

The angle in radians.

Syntax
------

    =ATAN(number)

*   _number_ - The value to get the inverse tangent of.

Using the ATAN function 
------------------------

The Excel ATAN function returns the inverse tangent or arc-tangent of a number. In geometric terms, the function returns the angle of a right-triangle given the ratio of its opposite side over its adjacent side. The ATAN function is the inverse of the TAN function. For example, if the length of a right-triangle's adjacent side is 3 and the length of its opposite side is 3 to find the angle of the triangle the formula is:

    =ATAN(3/3) // Returns 0.785 radians
    

### Convert Result to Degrees

ATAN returns the angle in radians. To convert the result from radians to degrees, multiply the result by 180/PI() or use the [DEGREES function](https://exceljet.net/functions/degrees-function)
. For example, to convert the result of ATAN(1) to degrees, you can use either formula below:

    =ATAN(1)*180/PI() // Returns 45 degrees
    =DEGREES(ATAN(1)) // Returns 45 degrees
    

### Difference Between ATAN and ATAN2

The ATAN2 function is useful for getting the angle corresponding to a point in the Cartesian Coordinate System which forms the shape of a right-triangle. For points in the first and fourth quadrants of the coordinate system, ATAN and ATAN2 will return the same angle as expressed in the formula:

    =ATAN(y/x)=ATAN2(x,y)
    

For points in the second and third quadrants of the coordinate system, the ATAN function will return the angle relative to the negative x-axis direction. The ATAN2 function, by comparison, returns the angle relative to the positive x-axis which is the standard for measuring angles.

![Excel ATAN2 Versus ATAN Function](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_atan2_versus_atan_0.png "Excel ATAN2 Versus ATAN Function")

### Graph

![Graph of ATAN Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/arc-tangent.png?itok=e8OIYgpN "Graph of ATAN Function")

The graph of ATAN, shown above, visualizes the output of the function. Output of the function is limited to the range from -π/2 to π/2.

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel ATAN2 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_atan2.png "Excel ATAN2 function")](https://exceljet.net/functions/atan2-function)

### [ATAN2 Function](https://exceljet.net/functions/atan2-function)

The Excel ATAN2 function returns the arctangent from x- and y-coordinates. In geometric terms, the function returns the radian angle corresponding to the input point.

[![Excel TAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tan_function_screenshot_cropped.png "Excel TAN function")](https://exceljet.net/functions/tan-function)

### [TAN Function](https://exceljet.net/functions/tan-function)

The Excel TAN function returns the tangent of the angle given in radians. To supply an angle to TAN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel ACOS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_acos_0.png "Excel ACOS function")](https://exceljet.net/functions/acos-function)

### [ACOS Function](https://exceljet.net/functions/acos-function)

The ACOS function returns the inverse cosine of a number. The function is the inverse of COS and expects input in the range from -1 to 1.

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

*   [ATAN2 Function](https://exceljet.net/functions/atan2-function)
    
*   [TAN Function](https://exceljet.net/functions/tan-function)
    
*   [ACOS Function](https://exceljet.net/functions/acos-function)
    
*   [ASIN Function](https://exceljet.net/functions/asin-function)
    

### Links

*   [Microsoft ATAN function documentation](https://support.office.com/en-us/article/atan-function-50746fa8-630a-406b-81d0-4a2aed395543)
    

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
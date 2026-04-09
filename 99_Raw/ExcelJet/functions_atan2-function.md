# Excel ATAN2 function | Exceljet

**Source:** https://exceljet.net/functions/atan2-function

---

[Skip to main content](https://exceljet.net/functions/atan2-function#main-content)

[](https://exceljet.net/functions/atan2-function#)

*   [Previous](https://exceljet.net/functions/atan-function)
    
*   [Next](https://exceljet.net/functions/atanh-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

ATAN2 Function
==============

by Kurt Bruns · Updated 22 Sep 2021

Related functions 
------------------

[ATAN](https://exceljet.net/functions/atan-function)

![Excel ATAN2 function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_atan2.png "Excel ATAN2 function")

Summary
-------

The Excel ATAN2 function returns the arctangent from x- and y-coordinates. In geometric terms, the function returns the radian angle corresponding to the input point.

Purpose 
--------

Get arctangent from x- and y-coordinates

Return value 
-------------

The angle in radians of the point.

Syntax
------

    =ATAN2(x_num,y_num)

*   _x\_num_ - The x coordinate of the input point.
*   _y\_num_ - The y coordinate of the input point.

Using the ATAN2 function 
-------------------------

The Excel ATAN2 function returns the arctangent from the x and y coordinates of a point. In geometric terms, the function returns the radian angle corresponding to the coordinates of the input point. If you imagine a ray starting from the origin of the coordinate system and extending outwards, every point along the ray will return the same angle value. A circle of radius one demonstrates all possible return values for the function.

![ATAN2 Function Unit Circle](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_atan2_unit_circle.png "ATAN2 Function Unit Circle")

For negative y-values the function returns a negative angle. An angle is measured from the positive x-axis direction with the positive direction in the counter-clockwise direction and the negative direction in the clockwise direction.

![ATAN2 Negative Y Value](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_atan2_negative-y-value.png "ATAN2 Negative Y Value")

### Convert Output to Degrees

To convert the output of the ATAN2 function from radians to degrees the formula is:

    =ATAN2(x,y)*180/PI() // Returns angle in degrees
    

Alternatively, the degrees formula can be used to convert the angle to degrees.

    =DEGREES(ATAN2(x,y))// Returns angle in degrees
    

### Difference Between ATAN and ATAN2

For points in the first and fourth quadrant, the ATAN2 function returns identical output to the [ATAN](https://exceljet.net/functions/atan-function)
 function. This relationship is expressed in the formula below:

    = ATAN2(x,y) = ATAN(y/x)
    

For points in the second and third quadrant, the ATAN function returns the angle relative to the negative x-direction axis.

![ATAN2 vs ATAN](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_atan2_versus_atan.png "ATAN2 vs ATAN")

Related functions
-----------------

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

*   [ATAN Function](https://exceljet.net/functions/atan-function)
    

### Links

*   [Microsoft ATAN2 function documentation](https://support.office.com/en-us/article/atan2-function-c04592ab-b9e3-4908-b428-c96b3a565033)
    

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
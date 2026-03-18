# Excel ACOS function | Exceljet

**Source:** https://exceljet.net/functions/acos-function

---

[Skip to main content](https://exceljet.net/functions/acos-function#main-content)

[](https://exceljet.net/functions/acos-function#)

*   [Previous](https://exceljet.net/functions/trunc-function)
    
*   [Next](https://exceljet.net/functions/acosh-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

ACOS Function
=============

by Kurt Bruns · Updated 19 Mar 2025

Related functions 
------------------

[COS](https://exceljet.net/functions/cos-function)

[ASIN](https://exceljet.net/functions/asin-function)

[ATAN](https://exceljet.net/functions/atan-function)

[ATAN2](https://exceljet.net/functions/atan2-function)

![Excel ACOS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_acos_0.png "Excel ACOS function")

Summary
-------

The ACOS function returns the inverse cosine of a number. The function is the inverse of COS and expects input in the range from -1 to 1.

Purpose 
--------

Get the inverse cosine of a value, in radians.

Return value 
-------------

Angle in radians.

Syntax
------

    =ACOS(number)

*   _number_ - The value to get the inverse cosine of. The number must be between -1 and 1 inclusive.

Using the ACOS function 
------------------------

The ACOS function returns the inverse cosine of a value. Input to the arc-cosine function must be between -1 and 1, inclusive. Geometrically, given the ratio of a triangle's adjacent side over its hypotenuse, the function returns the angle of the triangle. For example, given a ratio of 0.5, the function returns an angle of 1.047 radians.

    =ACOS(0.5) // Returns 1.047 radians
    

### Convert Result to Degrees

To convert the result from radians to degrees, multiply the result by 180/PI() or use the DEGREES function. For example, to convert the result of ACOS(0.5) to degrees, you can use either formula below:

    =ACOS(0.5)*180/PI() // Returns 60 degrees
    =DEGREES(ACOS(0.5)) // Returns 60 degrees
    

### Explanation

![Graph of ACOS Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/arc-cosine.png?itok=KWwX8Zvg "Graph of ACOS Function")

The graph of ACOS visualizes the output of the function in the range from -1 to 1. ACOS is the inverse of the COS function. However, because COS is a periodic function, the output of ACOS is limited to the range from 0 to π.

_Graph courtesy of_ [_wumbo.net_](https://wumbo.net/)
_._

Related functions
-----------------

[![Excel COS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cos_2_0.png "Excel COS function")](https://exceljet.net/functions/cos-function)

### [COS Function](https://exceljet.net/functions/cos-function)

The Excel COS function returns the cosine of an angle given in radians. To supply an angle to COS in degrees, use the RADIANS function to convert to radians.

[![Excel ASIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_asin_2.png "Excel ASIN function")](https://exceljet.net/functions/asin-function)

### [ASIN Function](https://exceljet.net/functions/asin-function)

The Excel ASIN function returns the inverse sine of a number.

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

*   [COS Function](https://exceljet.net/functions/cos-function)
    
*   [ASIN Function](https://exceljet.net/functions/asin-function)
    
*   [ATAN Function](https://exceljet.net/functions/atan-function)
    
*   [ATAN2 Function](https://exceljet.net/functions/atan2-function)
    

### Links

*   [Microsoft ACOS function documentation](https://support.office.com/en-us/article/acos-function-cb73173f-d089-4582-afa1-76e5524b5d5b)
    

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
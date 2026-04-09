# Excel ASIN function | Exceljet

**Source:** https://exceljet.net/functions/asin-function

---

[Skip to main content](https://exceljet.net/functions/asin-function#main-content)

[](https://exceljet.net/functions/asin-function#)

*   [Previous](https://exceljet.net/functions/acoth-function)
    
*   [Next](https://exceljet.net/functions/asinh-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

ASIN Function
=============

by Kurt Bruns · Updated 13 Apr 2020

Related functions 
------------------

[SIN](https://exceljet.net/functions/sin-function)

[ACOS](https://exceljet.net/functions/acos-function)

[ATAN](https://exceljet.net/functions/atan-function)

![Excel ASIN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_asin_2.png "Excel ASIN function")

Summary
-------

The Excel ASIN function returns the inverse sine of a number.

Purpose 
--------

Return the inverse sine of a value in radians.

Return value 
-------------

Angle in Radians

Syntax
------

    =ASIN(number)

*   _number_ - The value to get the inverse sine of. The number must be between -1 and 1 inclusive.

Using the ASIN function 
------------------------

The ASIN function, also called arc-sine, returns the inverse sine of a value. The input number must be between -1 and 1, inclusive. Geometrically, given the ratio of a triangle's opposite side over its hypotenuse, the function returns the angle of the triangle. For example, given a ratio of 0.5 the function returns the angle of 0.524 radians.

    =ASIN(0.5) // Returns 0.524 radians
    

### Convert Result to Degrees

To convert the result from radians to degrees, multiply the result by 180/[PI()](https://exceljet.net/functions/pi-function)
 or use the [DEGREES](https://exceljet.net/functions/degrees-function)
 function. For example, to convert the result of ASIN(0.5) to degrees, you can use either formula below:

    =ASIN(0.5)*180/PI() // Returns 30 degrees
    =DEGREES(ASIN(0.5)) // Returns 30 degrees
    

### Explanation

![Graph of ASIN Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/arc-sine.png?itok=rDxJBp2Z "Graph of ASIN Function")

The graph of ASIN visualizes the output of the function from -1 to 1. ASIN is the inverse of SIN. However, because SIN is a periodic function, the output of ASIN is limited to the range from -π/2 to π/2.

### Notes

*   ASIN is the inverse of SIN
*   To convert the result from radians to degrees multiply by 180/PI() or use the DEGREES function.

_Graph courtesy of [wumbo.net](https://wumbo.net/)
_

Related functions
-----------------

[![Excel SIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sin_2.png "Excel SIN function")](https://exceljet.net/functions/sin-function)

### [SIN Function](https://exceljet.net/functions/sin-function)

The Excel SIN function returns the sine of an angle given in radians. To supply an angle to SIN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel ACOS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_acos_0.png "Excel ACOS function")](https://exceljet.net/functions/acos-function)

### [ACOS Function](https://exceljet.net/functions/acos-function)

The ACOS function returns the inverse cosine of a number. The function is the inverse of COS and expects input in the range from -1 to 1.

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

*   [SIN Function](https://exceljet.net/functions/sin-function)
    
*   [ACOS Function](https://exceljet.net/functions/acos-function)
    
*   [ATAN Function](https://exceljet.net/functions/atan-function)
    

### Links

*   [Microsoft ASIN function documentation](https://support.office.com/en-us/article/asin-function-81fb95e5-6d6f-48c4-bc45-58f955c6d347)
    

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
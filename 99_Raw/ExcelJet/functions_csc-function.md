# Excel CSC function | Exceljet

**Source:** https://exceljet.net/functions/csc-function

---

[Skip to main content](https://exceljet.net/functions/csc-function#main-content)

[](https://exceljet.net/functions/csc-function#)

*   [Previous](https://exceljet.net/functions/coth-function)
    
*   [Next](https://exceljet.net/functions/csch-function)
    

Excel 2013

[Trigonometry](https://exceljet.net/functions#Trigonometry)

CSC Function
============

by Kurt Bruns · Updated 18 Apr 2020

Related functions 
------------------

[SIN](https://exceljet.net/functions/sin-function)

[SEC](https://exceljet.net/functions/sec-function)

[COT](https://exceljet.net/functions/cot-function)

![Excel CSC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_csc.png "Excel CSC function")

Summary
-------

The Excel CSC function returns the cosecant of an angle provided in radians.

Purpose 
--------

Get cosecant of an angle

Return value 
-------------

placeholder

Syntax
------

    =CSC(number)

*   _number_ - The angle provided in radians.

Using the CSC function 
-----------------------

The CSC function returns the cosecant of an angle provided in radians. In geometric terms, the cosecant of an angle is equal to the ratio of a right triangle's hypotenuse divided by its opposite side. For example, the cosecant of PI()/6 or 30° returns the ratio 2.0.

    =CSC(PI()/6) // Returns 2.0
    

### Using Degrees

The CSC function expects radians. To supply an angle to CSC in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians. For example, to get the CSC of 60 degrees, you can use either formula below:

    =CSC(60*PI()/180)
    =CSC(RADIANS(60))
    

### Explanation

![Graph of Cosecant Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/cosecant.png?itok=58dm0Oc4 "Graph of Cosecant Function")

The graph of cosecant, shown above, visualizes the output of the function for angles from 0 to a full rotation. The function has vertical asymptotes within the range  \[0, 2π\] at the points 0, π and 2π where the output diverges to infinity. CSC is the inverse of SIN and can be equivalently defined in the formula below:

    =CSC(angle)=1/SIN(angle)
    

The relationship between cosecant and sine is visualized by the graph of the two functions shown below:

![Graph of Cosecant and Sine Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/cosecant-and-sine.png?itok=PM5Uq6cr "Graph of Cosecant and Sine Function")

_Graphs courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel SIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sin_2.png "Excel SIN function")](https://exceljet.net/functions/sin-function)

### [SIN Function](https://exceljet.net/functions/sin-function)

The Excel SIN function returns the sine of an angle given in radians. To supply an angle to SIN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel SEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sec.png "Excel SEC function")](https://exceljet.net/functions/sec-function)

### [SEC Function](https://exceljet.net/functions/sec-function)

The Excel SEC function returns the secant of an angle provided in radians.

[![Excel COT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cot.png "Excel COT function")](https://exceljet.net/functions/cot-function)

### [COT Function](https://exceljet.net/functions/cot-function)

The Excel COT function returns the cotangent of an angle provided in radians.

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
    
*   [SEC Function](https://exceljet.net/functions/sec-function)
    
*   [COT Function](https://exceljet.net/functions/cot-function)
    

### Links

*   [Microsoft CSC function documentation](https://support.office.com/en-us/article/csc-function-07379361-219a-4398-8675-07ddc4f135c1)
    

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
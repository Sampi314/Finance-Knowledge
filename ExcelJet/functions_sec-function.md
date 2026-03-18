# Excel SEC function | Exceljet

**Source:** https://exceljet.net/functions/sec-function

---

[Skip to main content](https://exceljet.net/functions/sec-function#main-content)

[](https://exceljet.net/functions/sec-function#)

*   [Previous](https://exceljet.net/functions/radians-function)
    
*   [Next](https://exceljet.net/functions/sech-function)
    

Excel 2013

[Trigonometry](https://exceljet.net/functions#Trigonometry)

SEC Function
============

by Kurt Bruns · Updated 24 Oct 2023

Related functions 
------------------

[COS](https://exceljet.net/functions/cos-function)

[CSC](https://exceljet.net/functions/csc-function)

[COT](https://exceljet.net/functions/cot-function)

![Excel SEC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_sec.png "Excel SEC function")

Summary
-------

The Excel SEC function returns the secant of an angle provided in radians.

Purpose 
--------

Get secant of an angle

Return value 
-------------

The secant value.

Syntax
------

    =SEC(number)

*   _number_ - The angle in radians for which you want the secant.

Using the SEC function 
-----------------------

The SEC function returns the secant of an angle provided in [radians](https://wumbo.net/concepts/radian-angle-system/)
. In geometric terms, the secant of a right-triangle's angle is equal to the ratio of the length of its hypotenuse over the length of its adjacent side. For example, the secant of PI()/6 (30°) returns the ratio 1.514.

    =SEC(PI()/6) // Returns 1.514
    

### Using Degrees

To supply an angle to SEC in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians. For example, to get the COT of 60 degrees, you can use either formula below:

    =SIN(60*PI()/180)
    =SIN(RADIANS(60))
    

### Explanation

![Graph of Secant Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/secant.png?itok=QGS6Q__E "Graph of Secant Function")

The graph of SEC, shown above, visualizes the output of the function for angles from 0 to a full rotation. The function has two vertical asymptotes at π/2 and 3π/2 respectively where the output of the function diverges to infinity. The SEC function is the reciprocal of [COS](https://exceljet.net/functions/cos-function)
 and can be equivalently defined in the formula below:

    =SEC(angle)=1/COS(angle)
    

The relationship between SEC and COS is visualized in the graph of both of the functions shown below:

![Graph of Secant and Cosine Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/secant-and-cosine-3.png?itok=VCzZcShT "Graph of Secant and Cosine Function")

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel COS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cos_2_0.png "Excel COS function")](https://exceljet.net/functions/cos-function)

### [COS Function](https://exceljet.net/functions/cos-function)

The Excel COS function returns the cosine of an angle given in radians. To supply an angle to COS in degrees, use the RADIANS function to convert to radians.

[![Excel CSC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_csc.png "Excel CSC function")](https://exceljet.net/functions/csc-function)

### [CSC Function](https://exceljet.net/functions/csc-function)

The Excel CSC function returns the cosecant of an angle provided in radians.

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

*   [COS Function](https://exceljet.net/functions/cos-function)
    
*   [CSC Function](https://exceljet.net/functions/csc-function)
    
*   [COT Function](https://exceljet.net/functions/cot-function)
    

### Links

*   [Microsoft SEC function documentation](https://support.office.com/en-us/article/sec-function-ff224717-9c87-4170-9b58-d069ced6d5f7)
    

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
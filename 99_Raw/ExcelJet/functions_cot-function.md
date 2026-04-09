# Excel COT function | Exceljet

**Source:** https://exceljet.net/functions/cot-function

---

[Skip to main content](https://exceljet.net/functions/cot-function#main-content)

[](https://exceljet.net/functions/cot-function#)

*   [Previous](https://exceljet.net/functions/cosh-function)
    
*   [Next](https://exceljet.net/functions/coth-function)
    

Excel 2013

[Trigonometry](https://exceljet.net/functions#Trigonometry)

COT Function
============

by Kurt Bruns · Updated 13 Apr 2020

Related functions 
------------------

[TAN](https://exceljet.net/functions/tan-function)

[SEC](https://exceljet.net/functions/sec-function)

[CSC](https://exceljet.net/functions/csc-function)

![Excel COT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_cot.png "Excel COT function")

Summary
-------

The Excel COT function returns the cotangent of an angle provided in radians.

Purpose 
--------

Get the cotangent of an angle.

Return value 
-------------

The cotangent value.

Syntax
------

    =COT(number)

*   _number_ - The angle provided in radians.

Using the COT function 
-----------------------

The Excel COT function returns the cotangent of an angle provided in radians. In geometric terms, the cotangent of an angle returns the ratio of the length of the adjacent side over the length of the opposite side of the corresponding right triangle. For example, the cotangent of PI()/6 (30°) returns the ratio 1.732.

    =COT(PI()/6) // Returns 1.732
    

### Using Degrees

To supply an angle to COT in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians. For example, to get the COT of 60 degrees, you can use either formula below:

    =COT(60*PI()/180)
    =COT(RADIANS(60))
    

### Explanation

![Graph of Cotangent Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/cotangent.png?itok=NMmtDtXi "Graph of Cotangent Function")

The graph of COT, shown above, visualizes the output of the function for angles from 0 to a full rotation. The function has vertical asymptotes at the points 0, π, and 2π where the output of the function diverges to infinity. The COT function is the reciprocal of [TAN](https://exceljet.net/functions/tan-function)
 and can be equivalently defined in the formula below:

    =COT(angle)=1/TAN(angle)
    

The reciprocal relationship between COT and TAN is visualized by the graph shown below of both of the functions plotted together.

![Graph of Cotangent and Tangent Function](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/cotangent-and-tangent.png?itok=VFAbtWOk "Graph of Cotangent and Tangent Function")

_Graphs courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel TAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_tan_function_screenshot_cropped.png "Excel TAN function")](https://exceljet.net/functions/tan-function)

### [TAN Function](https://exceljet.net/functions/tan-function)

The Excel TAN function returns the tangent of the angle given in radians. To supply an angle to TAN in degrees, multiply the angle by PI()/180 or use the RADIANS function to convert to radians.

[![Excel SEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sec.png "Excel SEC function")](https://exceljet.net/functions/sec-function)

### [SEC Function](https://exceljet.net/functions/sec-function)

The Excel SEC function returns the secant of an angle provided in radians.

[![Excel CSC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_csc.png "Excel CSC function")](https://exceljet.net/functions/csc-function)

### [CSC Function](https://exceljet.net/functions/csc-function)

The Excel CSC function returns the cosecant of an angle provided in radians.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [TAN Function](https://exceljet.net/functions/tan-function)
    
*   [SEC Function](https://exceljet.net/functions/sec-function)
    
*   [CSC Function](https://exceljet.net/functions/csc-function)
    

### Links

*   [Microsoft COT function documentation](https://support.office.com/en-us/article/cot-function-c446f34d-6fe4-40dc-84f8-cf59e5f5e31a)
    

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
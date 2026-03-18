# Excel IMCSCH function | Exceljet

**Source:** https://exceljet.net/functions/imcsch-function

---

[Skip to main content](https://exceljet.net/functions/imcsch-function#main-content)

[](https://exceljet.net/functions/imcsch-function#)

*   [Previous](https://exceljet.net/functions/imcsc-function)
    
*   [Next](https://exceljet.net/functions/imdiv-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

IMCSCH Function
===============

by Dave Bruns · Updated 24 Nov 2024

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[CSC](https://exceljet.net/functions/csc-function)

[CSCH](https://exceljet.net/functions/csch-function)

![Excel IMCSCH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imcsch_screenshot_cropped.png "Excel IMCSCH function")

Summary
-------

The Excel IMCSCH function returns the hyperbolic cosecant of a complex number.

Purpose 
--------

Get hyperbolic cosecant of complex number

Return value 
-------------

The hyperbolic cosecant of the complex number.

Syntax
------

    =IMCSCH(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMCSCH function 
--------------------------

The Excel IMCSCH function returns the hyperbolic cosecant of a complex number. Given "1+1.5707963267949i" as input, the function returns "-1.72324E-15-0.648054274i" as output.

    =IMCSC(COMPLEX(1, PI()/2)) // returns -1.72324E-15-0.648054274i

### Explanation

The complex hyperbolic cosecant function is the reciprocal of the complex hyperbolic sine function.

![Reciprocal definition of the complex hyperbolic cosecant function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imcsch_reciprocal_definition.png "Reciprocal definition of the complex hyperbolic cosecant function.")

In Excel, the function's output is equivalent to the following formula.

    =IMDIV(1,IMSINH(z)) // equivalent to IMCSCH(z)

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel CSC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_csc.png "Excel CSC function")](https://exceljet.net/functions/csc-function)

### [CSC Function](https://exceljet.net/functions/csc-function)

The Excel CSC function returns the cosecant of an angle provided in radians.

[![Excel CSCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_csch_screenshot_cropped.png "Excel CSCH function")](https://exceljet.net/functions/csch-function)

### [CSCH Function](https://exceljet.net/functions/csch-function)

The Excel CSCH function returns the hyperbolic cosecant of an angle.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    
*   [CSC Function](https://exceljet.net/functions/csc-function)
    
*   [CSCH Function](https://exceljet.net/functions/csch-function)
    

### Links

*   [Microsoft IMCSCH function documentation](https://support.office.com/en-us/article/imcsch-function-c0ae4f54-5f09-4fef-8da0-dc33ea2c5ca9)
    

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
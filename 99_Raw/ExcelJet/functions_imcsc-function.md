# Excel IMCSC function | Exceljet

**Source:** https://exceljet.net/functions/imcsc-function

---

[Skip to main content](https://exceljet.net/functions/imcsc-function#main-content)

[](https://exceljet.net/functions/imcsc-function#)

*   [Previous](https://exceljet.net/functions/imcot-function)
    
*   [Next](https://exceljet.net/functions/imcsch-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

IMCSC Function
==============

by Dave Bruns · Updated 19 Oct 2024

Related functions 
------------------

[IMSIN](https://exceljet.net/functions/imsin-function)

[CSC](https://exceljet.net/functions/csc-function)

![Excel IMCSC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imcsc_function_screenshot_cropped.png "Excel IMCSC function")

Summary
-------

The Excel IMCSC function returns the cosecant of a complex number. The complex secant function is the reciprocal of the [complex sine function](https://exceljet.net/functions/imsin-function)
.

Purpose 
--------

Get cosecant of complex number

Return value 
-------------

The cosecant of the complex number.

Syntax
------

    =IMCSC(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMCSC function 
-------------------------

The Excel IMCSC function returns the cosecant of a complex number. For example, given "4+3i" as input, the function returns "-0.075489833+0.064877471i" as output.

    =IMCSC("4+3i") // returns -0.075489833+0.064877471i

### Explanation

In math, the complex cosecant function is the reciprocal of the [complex sine function](https://exceljet.net/functions/imsin-function)
.

![The complex cosecant function definition.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imcsc_function_definition.png "The complex cosecant function definition.")

In Excel, the complex cosecant function is equivalent to the following formula.

    =IMDIV(COMPLEX(1,0),IMSIN(z)) // equivalent to IMCSC(z)

Related functions
-----------------

[![Excel IMSIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imsin_function_screenshot_cropped.png "Excel IMSIN function")](https://exceljet.net/functions/imsin-function)

### [IMSIN Function](https://exceljet.net/functions/imsin-function)

The Excel IMSIN function returns the sine of a complex number.

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

*   [IMSIN Function](https://exceljet.net/functions/imsin-function)
    
*   [CSC Function](https://exceljet.net/functions/csc-function)
    

### Links

*   [Microsoft IMCSC function documentation](https://support.office.com/en-us/article/imcsc-function-9e158d8f-2ddf-46cd-9b1d-98e29904a323)
    

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
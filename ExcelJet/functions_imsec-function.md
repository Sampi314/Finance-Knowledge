# Excel IMSEC function | Exceljet

**Source:** https://exceljet.net/functions/imsec-function

---

[Skip to main content](https://exceljet.net/functions/imsec-function#main-content)

[](https://exceljet.net/functions/imsec-function#)

*   [Previous](https://exceljet.net/functions/imreal-function)
    
*   [Next](https://exceljet.net/functions/imsech-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

IMSEC Function
==============

by Dave Bruns · Updated 9 Oct 2024

Related functions 
------------------

[IMCOS](https://exceljet.net/functions/imcos-function)

![Excel IMSEC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imsec_function_screenshot_cropped.png "Excel IMSEC function")

Summary
-------

The Excel IMSEC function returns the secant of a complex number. The secant is the reciprocal of the complex [cosine function](https://exceljet.net/functions/imcos-function)
.

Purpose 
--------

Get secant of complex number

Return value 
-------------

The secant of the complex number.

Syntax
------

    =IMSEC(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMSEC function 
-------------------------

The Excel IMSEC function returns the secant of a complex number. For example, given "4+3i" as input the function returns "-0.065294028-0.07522496i" as output.

    =IMSEC("4+3i") // returns -0.065294028-0.07522496i

### Explanation

In math, the complex secant function is the reciprocal of the complex [cosine function](https://exceljet.net/functions/imcos-function)
.

![The complex secant function definition.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imsec_function_definition.png "The complex secant function definition.")

In Excel, the output of the complex secant function is equivalent to the following formula.

    =IMDIV(COMPLEX(1,0),IMCOS(z)) // equivalent to IMSEC(z)

Related functions
-----------------

[![Excel IMCOS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imcos_function.png "Excel IMCOS function")](https://exceljet.net/functions/imcos-function)

### [IMCOS Function](https://exceljet.net/functions/imcos-function)

The Excel IMCOS function returns the cosine of a complex number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IMCOS Function](https://exceljet.net/functions/imcos-function)
    

### Links

*   [Microsoft IMSEC function documentation](https://support.office.com/en-us/article/imsec-function-6df11132-4411-4df4-a3dc-1f17372459e0)
    

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
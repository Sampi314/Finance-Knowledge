# Excel IMCOT function | Exceljet

**Source:** https://exceljet.net/functions/imcot-function

---

[Skip to main content](https://exceljet.net/functions/imcot-function#main-content)

[](https://exceljet.net/functions/imcot-function#)

*   [Previous](https://exceljet.net/functions/imcosh-function)
    
*   [Next](https://exceljet.net/functions/imcsc-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

IMCOT Function
==============

by Dave Bruns · Updated 9 Oct 2024

Related functions 
------------------

[IMTAN](https://exceljet.net/functions/imtan-function)

[IMCOS](https://exceljet.net/functions/imcos-function)

[IMSIN](https://exceljet.net/functions/imsin-function)

[COMPLEX](https://exceljet.net/functions/complex-function)

![Excel IMCOT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imcot_function_screenshot_cropped.png "Excel IMCOT function")

Summary
-------

The Excel IMCOT function returns the cotangent of a complex number.

Purpose 
--------

Get cotangent of complex number.

Return value 
-------------

The cotangent of the complex number.

Syntax
------

    =IMCOT(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMCOT function 
-------------------------

The Excel IMCOT function returns the cotangent of a complex number. For example, given "3+4i" as input, the function returns "-0.000187588-1.000644392i" as output.

    =IMCOT("3+4i") // returns -0.000187588-1.000644392i

### Explanation

In math, the cotangent of a complex number is defined using the complex sine and cosine functions.

![Definition of the complex cotangent function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imcot_function_definition.png "Definition of the complex cotangent function.")

In Excel, the cotangent of a complex number is equivalent to the following formula.

    =IMDIV(IMCOS(z),IMSIN(z)) // equivalent to IMCOT(z)

The cotangent is the reciprocal of the [complex tangent function](https://exceljet.net/functions/imtan-function)
.

Related functions
-----------------

[![Excel IMTAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imtan_function_screenshot_cropped.png "Excel IMTAN function")](https://exceljet.net/functions/imtan-function)

### [IMTAN Function](https://exceljet.net/functions/imtan-function)

The Excel IMTAN function returns the tangent of a complex number. ...

[![Excel IMCOS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imcos_function.png "Excel IMCOS function")](https://exceljet.net/functions/imcos-function)

### [IMCOS Function](https://exceljet.net/functions/imcos-function)

The Excel IMCOS function returns the cosine of a complex number.

[![Excel IMSIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imsin_function_screenshot_cropped.png "Excel IMSIN function")](https://exceljet.net/functions/imsin-function)

### [IMSIN Function](https://exceljet.net/functions/imsin-function)

The Excel IMSIN function returns the sine of a complex number.

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IMTAN Function](https://exceljet.net/functions/imtan-function)
    
*   [IMCOS Function](https://exceljet.net/functions/imcos-function)
    
*   [IMSIN Function](https://exceljet.net/functions/imsin-function)
    
*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    

### Links

*   [Microsoft IMCOT function documentation](https://support.office.com/en-us/article/imcot-function-dc6a3607-d26a-4d06-8b41-8931da36442c)
    

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
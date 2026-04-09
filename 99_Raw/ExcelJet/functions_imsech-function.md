# Excel IMSECH function | Exceljet

**Source:** https://exceljet.net/functions/imsech-function

---

[Skip to main content](https://exceljet.net/functions/imsech-function#main-content)

[](https://exceljet.net/functions/imsech-function#)

*   [Previous](https://exceljet.net/functions/imsec-function)
    
*   [Next](https://exceljet.net/functions/imsin-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

IMSECH Function
===============

by Dave Bruns · Updated 24 Nov 2024

Related functions 
------------------

[IMCOSH](https://exceljet.net/functions/imcosh-function)

![Excel IMSECH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imsech_screenshot_cropped.png "Excel IMSECH function")

Summary
-------

The Excel IMSECH function returns the hyperbolic secant of a complex number.

Purpose 
--------

Get hyperbolic secant of a complex number

Return value 
-------------

The hyperbolic secant of a complex number

Syntax
------

    =IMSECH(complex_num)

*   _complex\_num_ - The number to get the inverse hyperbolic secant of.

Using the IMSECH function 
--------------------------

The Excel IMSECH function returns the hyperbolic secant of a complex number. Given "1+1.5707963267949i" as input, the function returns "-3.9E-15-0.85092i" as output.

    =IMSECH(COMPLEX(1, PI()/2)) // returns -3.9E-15-0.85092i

### Explanation

The complex hyperbolic secant function is the reciprocal of the complex hyperbolic sine function.

![Definition of complex hyperbolic secant function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imsech_reciprocal_definition.png "Definition of complex hyperbolic secant function.")

In Excel, the function's output is equivalent to the following formula.

    =IMDIV(1,IMCOSH(z)) // equivalent to IMSECH(z) 

Related functions
-----------------

[![Excel IMCOSH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imcosh_screenshot_cropped.png "Excel IMCOSH function")](https://exceljet.net/functions/imcosh-function)

### [IMCOSH Function](https://exceljet.net/functions/imcosh-function)

The Excel IMCOSH function returns the hyperbolic cosine of a complex number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IMCOSH Function](https://exceljet.net/functions/imcosh-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMSECH function documentation](https://support.office.com/en-us/article/imsech-function-f250304f-788b-4505-954e-eb01fa50903b)
    

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
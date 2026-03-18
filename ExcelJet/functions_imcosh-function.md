# Excel IMCOSH function | Exceljet

**Source:** https://exceljet.net/functions/imcosh-function

---

[Skip to main content](https://exceljet.net/functions/imcosh-function#main-content)

[](https://exceljet.net/functions/imcosh-function#)

*   [Previous](https://exceljet.net/functions/imcos-function)
    
*   [Next](https://exceljet.net/functions/imcot-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

IMCOSH Function
===============

by Dave Bruns · Updated 24 Nov 2024

Related functions 
------------------

[COSH](https://exceljet.net/functions/cosh-function)

[IMSINH](https://exceljet.net/functions/imsinh-function)

![Excel IMCOSH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imcosh_screenshot_cropped.png "Excel IMCOSH function")

Summary
-------

The Excel IMCOSH function returns the hyperbolic cosine of a complex number.

Purpose 
--------

Get hyperbolic cosine of complex number

Return value 
-------------

The hyperbolic cosine of a complex number

Syntax
------

    =IMCOSH(complex_num)

*   _complex\_num_ - The number to get the hyperbolic cosine of.

Using the IMCOSH function 
--------------------------

The Excel IMCOSH function returns the hyperbolic cosine of a complex number. Given "1+1.5707963267949i" as input, the function returns "-5.4E-15+1.175201i" as output.

    =IMCOSH(COMPLEX(1, PI()/2)) // returns -5.4E-15+1.175201i

When the function's output is plotted over the complex plane, the real output along the real axis traces the shape of the [COSH](https://exceljet.net/functions/cosh-function)
 function.

    =IMCOSH(COMPLEX(x, 0)) // returns COSH(x)

The imaginary output along the imaginary axis traces the shape of the [COS](https://exceljet.net/functions/cos-function)
 function.

    =IMCOSH(COMPLEX(0, y)) // returns COS(y)

### Explanation

The function can be defined using the [COSH](https://exceljet.net/functions/cosh-function)
, [COS](https://exceljet.net/functions/cos-function)
, [SINH](https://exceljet.net/functions/sinh-function)
, and [SIN](https://exceljet.net/functions/sin-function)
 functions.

![The definition of the complex hyperbolic cosine function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imcosh_function_definition.png "The definition of the complex hyperbolic cosin function.")

Related functions
-----------------

[![Excel COSH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_cosh_screenshot_cropped.png "Excel COSH function")](https://exceljet.net/functions/cosh-function)

### [COSH Function](https://exceljet.net/functions/cosh-function)

The Excel COSH function returns the hyperbolic cosine of a number.

[![Excel IMSINH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imsinh_screenshot_cropped.png "Excel IMSINH function")](https://exceljet.net/functions/imsinh-function)

### [IMSINH Function](https://exceljet.net/functions/imsinh-function)

The Excel IMSINH function returns the hyperbolic sine of a complex number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COSH Function](https://exceljet.net/functions/cosh-function)
    
*   [IMSINH Function](https://exceljet.net/functions/imsinh-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMCOSH function documentation](https://support.office.com/en-us/article/imcosh-function-053e4ddb-4122-458b-be9a-457c405e90ff)
    

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
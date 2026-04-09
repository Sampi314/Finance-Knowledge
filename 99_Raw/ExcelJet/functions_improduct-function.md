# Excel IMPRODUCT function | Exceljet

**Source:** https://exceljet.net/functions/improduct-function

---

[Skip to main content](https://exceljet.net/functions/improduct-function#main-content)

[](https://exceljet.net/functions/improduct-function#)

*   [Previous](https://exceljet.net/functions/impower-function)
    
*   [Next](https://exceljet.net/functions/imreal-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMPRODUCT Function
==================

by Dave Bruns · Updated 5 Feb 2025

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

[IMDIV](https://exceljet.net/functions/imdiv-function)

[IMPOWER](https://exceljet.net/functions/impower-function)

![Excel IMPRODUCT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_improduct_function_screenshot_cropped_0.png "Excel IMPRODUCT function")

Summary
-------

The Excel IMPRODUCT function returns the product of one or more complex numbers.

Purpose 
--------

Get product of complex numbers

Return value 
-------------

Product as complex number

Syntax
------

    =IMPRODUCT(inumber1,[inumber2],...)

*   _inumber1_ - Complex number 1.
*   _inumber2_ - \[optional\] Complex number 2.

Using the IMPRODUCT function 
-----------------------------

The Excel IMPRODUCT function returns the product of one or more complex numbers. For example:

    =IMPRODUCT("1+2i", "3+5i") // returns -7+11i

> Excel handles complex numbers as strings formatted like "x+yi" or "x+yj". Use the [COMPLEX](https://exceljet.net/functions/complex-function)
>  function to get the string representing a complex number.

### Examples

The IMPRODUCT function takes in two or more arguments in the form of _inumber1_, _inumber2_, and so on. Arguments can be hard-coded values, cell references, or a range. To calculate the product of multiple complex numbers in a range, use the function like this:

    =IMPRODUCT(B6:B10) // multiply the complex numbers in B6:B10

If Excel encounters values not recognized as complex numbers, a #NUM! Error is thrown.

    =IMPRODUCT("1+2i", "invalid input") // throws #NUM! error

### Explanation

The product of two complex numbers is visualized by transforming the coordinate system according to one of the numbers and drawing the second number using the transformed coordinate system. For example, the product of "1+2i" and "3+5i" is visualized by transforming the coordinate system (shown in blue) so that one (drawn as the green arrow) goes to the number "3+5i" in the complex plane. When we draw the transformed position of "1+2i" its tip sits at "-7+11i" which is the product of the two numbers.

![Complex multiplication example.](https://exceljet.net/sites/default/files/images/functions/inline/ComplexMultiplication.png "Complex multiplication example.")

    =IMPRODUCT("1+2i", "3+5i") // returns -7+11i

Let's visualize another example. The product of "-3+i" and "4+2i" is visualized by transforming the coordinate system so that one goes to "4+2i". When we draw "-3+i" in the transformed coordinate system, the tip lies at "-14-2i," which is the product of the two numbers.

![Complex multiplication example.](https://exceljet.net/sites/default/files/images/functions/inline/ComplexMultiplicationExample2.png "Complex multiplication example.")

 _Images courtesy of_ [_wumbo.net_](https://wumbo.net/)

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMREAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imreal_screenshot_cropped.png "Excel IMREAL function")](https://exceljet.net/functions/imreal-function)

### [IMREAL Function](https://exceljet.net/functions/imreal-function)

The Excel IMREAL function returns the real part of a complex number.

[![Excel IMAGINARY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imaginary_screenshot_cropped.png "Excel IMAGINARY function")](https://exceljet.net/functions/imaginary-function)

### [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)

The Excel IMAGINARY function returns the imaginary part of a complex number.

[![Excel IMDIV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imdiv_function_screenshot_cropped.png "Excel IMDIV function")](https://exceljet.net/functions/imdiv-function)

### [IMDIV Function](https://exceljet.net/functions/imdiv-function)

The Excel IMDIV function returns the quotient of two complex numbers.

[![Excel IMPOWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_impower_function.png "Excel IMPOWER function")](https://exceljet.net/functions/impower-function)

### [IMPOWER Function](https://exceljet.net/functions/impower-function)

The Excel IMPOWER function returns a complex number raised to a given power. The complex number must be in the form x + yi or x + yj. Use the [COMPLEX function](https://exceljet.net/functions/complex-function)
 to create a complex number from real and imaginary parts.

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
    
*   [IMREAL Function](https://exceljet.net/functions/imreal-function)
    
*   [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)
    
*   [IMDIV Function](https://exceljet.net/functions/imdiv-function)
    
*   [IMPOWER Function](https://exceljet.net/functions/impower-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMPRODUCT function documentation](https://support.office.com/en-us/article/improduct-function-2fb8651a-a4f2-444f-975e-8ba7aab3a5ba)
    

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
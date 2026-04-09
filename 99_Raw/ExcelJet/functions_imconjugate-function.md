# Excel IMCONJUGATE function | Exceljet

**Source:** https://exceljet.net/functions/imconjugate-function

---

[Skip to main content](https://exceljet.net/functions/imconjugate-function#main-content)

[](https://exceljet.net/functions/imconjugate-function#)

*   [Previous](https://exceljet.net/functions/imargument-function)
    
*   [Next](https://exceljet.net/functions/imcos-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMCONJUGATE Function
====================

by Dave Bruns · Updated 9 Dec 2024

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMDIV](https://exceljet.net/functions/imdiv-function)

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

![Excel IMCONJUGATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imconjugate_function_screenshot_cropped.png "Excel IMCONJUGATE function")

Summary
-------

The Excel IMCONJUGATE function returns the conjugate of a complex number. 

Purpose 
--------

Get the complex conjugate of a complex number

Return value 
-------------

The complex number with the sign of the imaginary part flipped

Syntax
------

    =IMCONJUGATE(inumber)

*   _inumber_ - The complex number in the form "x+yi".

Using the IMCONJUGATE function 
-------------------------------

The Excel IMCONJUGATE function returns the conjugate of a complex number. For example, given the complex number "3+4i" as input, the function returns "3-4i" as output.

    =IMCONJUGATE("3+4i") // returns "3-4i"
    

> Excel handles complex numbers as strings formatted like "x+yi" or "x+yj". Use the [COMPLEX](https://exceljet.net/functions/complex-function)
>  function to get the string representing a complex number.

### Explanation

The conjugate of a complex number has the same real part and flips the sign of the imaginary part. If a complex number is written as "x + yi", its conjugate equals "x - yi". Typically, the conjugate appears in text with a horizontal bar over the complex number.

![The conjugate of a complex number.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imconjugate_function_definition.png "The conjugate of a complex number.")

The conjugate is used to divide a complex number by another. For example, let's say you want to divide the complex number "x+yi" by another complex number "a+bi".

![How does one define complex division?](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imconjugate_function_division.png "How does one define complex division?")

We can convert this expression into a multiplication problem by multiplying the numerator and numerator by the conjugate of "a+bi".

![Complex division using the conjugate.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imconjugate_function_division_expressed_using_conjugate.png "Complex division using the conjugate.")

In other words, the divisor is converted into a real number which we know how to divide by. This is equal to the following formula in Excel.

    =IMPRODUCT(
        "x+yi",
        IMCONJUGATE("a+bi"),
        COMPLEX(1/IMREAL(IMPRODUCT("a+bi", IMCONJUGATE("a+bi"))), 0)
    )

In practice, Excel provides the IMDIV function to perform complex division.

    =IMDIV(COMPLEX(-11,29),COMPLEX(2,3)) // returns 5+7i

The conjugate is still useful to know because, aside from being the key to defining complex division, it also appears in other contexts in math, like factoring and solving polynomials.

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMDIV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imdiv_function_screenshot_cropped.png "Excel IMDIV function")](https://exceljet.net/functions/imdiv-function)

### [IMDIV Function](https://exceljet.net/functions/imdiv-function)

The Excel IMDIV function returns the quotient of two complex numbers.

[![Excel IMREAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imreal_screenshot_cropped.png "Excel IMREAL function")](https://exceljet.net/functions/imreal-function)

### [IMREAL Function](https://exceljet.net/functions/imreal-function)

The Excel IMREAL function returns the real part of a complex number.

[![Excel IMAGINARY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imaginary_screenshot_cropped.png "Excel IMAGINARY function")](https://exceljet.net/functions/imaginary-function)

### [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)

The Excel IMAGINARY function returns the imaginary part of a complex number.

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
    
*   [IMDIV Function](https://exceljet.net/functions/imdiv-function)
    
*   [IMREAL Function](https://exceljet.net/functions/imreal-function)
    
*   [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMCONJUGATE function documentation](https://support.office.com/en-us/article/imconjugate-function-2e2fc1ea-f32b-4f9b-9de6-233853bafd42)
    

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
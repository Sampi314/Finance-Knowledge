# Excel COMPLEX function | Exceljet

**Source:** https://exceljet.net/functions/complex-function

---

[Skip to main content](https://exceljet.net/functions/complex-function#main-content)

[](https://exceljet.net/functions/complex-function#)

*   [Previous](https://exceljet.net/functions/bitxor-function)
    
*   [Next](https://exceljet.net/functions/convert-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

COMPLEX Function
================

by Dave Bruns · Updated 14 Mar 2025

Related functions 
------------------

[IMREAL](https://exceljet.net/functions/imreal-function)

[IMAGINARY](https://exceljet.net/functions/imaginary-function)

[IMABS](https://exceljet.net/functions/imabs-function)

[IMARGUMENT](https://exceljet.net/functions/imargument-function)

![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")

Summary
-------

The Excel COMPLEX function returns the string representation of a complex number.

Purpose 
--------

Get the string representation of a complex number

Return value 
-------------

The string representation of a complex number

Syntax
------

    =COMPLEX(real_num,i_num,[suffix])

*   _real\_num_ - The real part of the complex number.
*   _i\_num_ - The imaginary part of the complex number.
*   _suffix_ - \[optional\] The suffix for the imaginary unit, either "i" or "j".

Using the COMPLEX function 
---------------------------

The COMPLEX function returns the string representation of a complex number. For example:

    =COMPLEX(4,3) // returns "4+3i"
    

To use the "j" instead of "i":

    =COMPLEX(4,3,"j") // returns "4+3j"
    

To enter the value of a complex number without using the COMPLEX function, write it in a formula like this:

    ="4+3i"
    

### Explanation

The Excel formula engine handles complex numbers as strings formatted like "x+yi" or "x+yj". For example, when we add two complex numbers together using the [IMSUM](https://exceljet.net/functions/imsum-function)
 function, the complex numbers are passed to the function as strings, and the result is a string representing the complex number that is the sum.

    =IMSUM("4+3i","2-5i") // returns "6-2i"

We can perform the same operation using COMPLEX to get the strings representing the complex numbers.

    =IMSUM(
    COMPLEX(4, 3),
    COMPLEX(2,-5)
    ) // returns "6-2i"

In general, the COMPLEX function is useful when you already have a complex number's real and imaginary values and want its string representation.

To read more about complex numbers in Excel, see [this article](https://exceljet.net/articles/complex-numbers-in-excel)
.

**Notes:**

1.  If omitted, the _suffix_ defaults to "i".
2.  The _suffix_ must be lowercase "i" or "j"; other values result in a #VALUE error.
3.  If _real\_num_ or _i\_num_ are non-numeric, COMPLEX returns the #VALUE! error

Related functions
-----------------

[![Excel IMREAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imreal_screenshot_cropped.png "Excel IMREAL function")](https://exceljet.net/functions/imreal-function)

### [IMREAL Function](https://exceljet.net/functions/imreal-function)

The Excel IMREAL function returns the real part of a complex number.

[![Excel IMAGINARY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imaginary_screenshot_cropped.png "Excel IMAGINARY function")](https://exceljet.net/functions/imaginary-function)

### [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)

The Excel IMAGINARY function returns the imaginary part of a complex number.

[![Excel IMABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imabs_screenshot_cropped.png "Excel IMABS function")](https://exceljet.net/functions/imabs-function)

### [IMABS Function](https://exceljet.net/functions/imabs-function)

The Excel IMABS function returns the absolute value of a complex number.

[![Excel IMARGUMENT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imargument_function_screenshot_cropped_0.png "Excel IMARGUMENT function")](https://exceljet.net/functions/imargument-function)

### [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)

The Excel IMARGUMENT function returns the angle of a complex number expressed in radians. The **argument**, also known as the phase, is the angle between the positive real axis and the line the complex number lies on in the complex plane.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IMREAL Function](https://exceljet.net/functions/imreal-function)
    
*   [IMAGINARY Function](https://exceljet.net/functions/imaginary-function)
    
*   [IMABS Function](https://exceljet.net/functions/imabs-function)
    
*   [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft COMPLEX function documentation](https://support.office.com/en-us/article/complex-function-f0b8f3a9-51cc-4d6d-86fb-3a9362fa4128)
    

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
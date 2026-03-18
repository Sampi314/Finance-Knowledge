# Excel IMLOG10 function | Exceljet

**Source:** https://exceljet.net/functions/imlog10-function

---

[Skip to main content](https://exceljet.net/functions/imlog10-function#main-content)

[](https://exceljet.net/functions/imlog10-function#)

*   [Previous](https://exceljet.net/functions/imln-function)
    
*   [Next](https://exceljet.net/functions/imlog2-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMLOG10 Function
================

by Dave Bruns · Updated 17 Oct 2024

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMLN](https://exceljet.net/functions/imln-function)

[IMLOG2](https://exceljet.net/functions/imlog2-function)

[LOG10](https://exceljet.net/functions/log10-function)

![Excel IMLOG10 function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imlog10_screenshot_cropped.png "Excel IMLOG10 function")

Summary
-------

The Excel IMLOG10 function returns the base-10 logarithm of a complex number.

Purpose 
--------

Returns the base-10 logarithm of a complex number.

Return value 
-------------

The logarithm of the complex number.

Syntax
------

    =IMLOG10(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMLOG10 function 
---------------------------

The Excel IMLOG10 function returns the base-10 logarithm of a complex number. For example, given the number "0-100i" as input, the function returns "2-0.682188176920921i" as output.

    =IMLOG10("0-100i") // returns 2 - 0.682188176920921i
    

The real part of the output is equal to the logarithm (base 10) of the complex number's magnitude.

    =LOG10(IMABS("0-100i")) // returns 2

The imaginary part of the output is equal to the angle (in radians) of the complex number divided by the natural logarithm of 10.

    =IMARGUMENT("0-100i")/LN(10) // returns -0.682188177

### Explanation

In math, the complex logarithm of any base can be described in terms of the natural logarithm using the change of base formula.

![Complex logarithm change of base.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imlog10_function_change_of_base.png "Complex logarithm change of base.")

In Excel, we can define the base-10 logarithm using the following formula.

    =IMDIV(IMLN("x+yi"),IMLN("10"))

See the [IMLN](https://exceljet.net/functions/imln-function)
 function for a more in-depth explanation of the complex logarithm.

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMLN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imln_function_screenshot_cropped.png "Excel IMLN function")](https://exceljet.net/functions/imln-function)

### [IMLN Function](https://exceljet.net/functions/imln-function)

The Excel IMLN function returns the natural logarithm of a complex number.

[![Excel IMLOG2 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imlog2_screenshot_cropped.png "Excel IMLOG2 function")](https://exceljet.net/functions/imlog2-function)

### [IMLOG2 Function](https://exceljet.net/functions/imlog2-function)

The Excel IMLOG2 function returns the base-2 logarithm of a complex number.

[![Excel LOG10 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_log10_new.png "Excel LOG10 function")](https://exceljet.net/functions/log10-function)

### [LOG10 Function](https://exceljet.net/functions/log10-function)

The Excel LOG10 function returns the base 10 logarithm of a number. For example, LOG10(100) returns 2, and LOG10(1000) returns 3.

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
    
*   [IMLN Function](https://exceljet.net/functions/imln-function)
    
*   [IMLOG2 Function](https://exceljet.net/functions/imlog2-function)
    
*   [LOG10 Function](https://exceljet.net/functions/log10-function)
    

### Links

*   [Microsoft IMLOG10 function documentation](https://support.office.com/en-us/article/imlog10-function-58200fca-e2a2-4271-8a98-ccd4360213a5)
    

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
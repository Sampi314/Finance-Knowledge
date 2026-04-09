# Excel SQRTPI function | Exceljet

**Source:** https://exceljet.net/functions/sqrtpi-function

---

[Skip to main content](https://exceljet.net/functions/sqrtpi-function#main-content)

[](https://exceljet.net/functions/sqrtpi-function#)

*   [Previous](https://exceljet.net/functions/sqrt-function)
    
*   [Next](https://exceljet.net/functions/subtotal-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SQRTPI Function
===============

by Kurt Bruns · Updated 15 Jun 2025

Related functions 
------------------

[PI](https://exceljet.net/functions/pi-function)

[SQRT](https://exceljet.net/functions/sqrt-function)

![Excel SQRTPI function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_sqrtpi_function_main_screenshot_cropped_0.png "Excel SQRTPI function")

Summary
-------

The Excel SQRTPI function returns the square root of the product of a number and π (pi).

Purpose 
--------

Get the square root of (number × π)

Return value 
-------------

A positive number.

Syntax
------

    =SQRTPI(number)

*   _number_ - A positive number to multiply by π before taking the square root.

Using the SQRTPI function 
--------------------------

The SQRTPI function calculates the square root of (number × π). This is equivalent to `SQRT(number*PI())` but provides a more direct way to perform this calculation. The function returns a numeric value accurate to 15 digits.

    =SQRTPI(1) // returns 1.77245385090552 (square root of π)

If the number argument is negative, SQRTPI returns a #NUM! error. If the number argument is not numeric, SQRTPI returns a #VALUE! error. 

### Basic Examples

    =SQRTPI(1) // returns 1.772453851 (square root of π)
    =SQRTPI(4) // returns 3.544907702 (square root of 4π)
    

### Comparison with Equivalent Formula

The SQRTPI function provides the same result as combining the [SQRT](https://exceljet.net/functions/sqrt-function)
 and [PI](https://exceljet.net/functions/pi-function)
 functions:

    =SQRTPI(9) // 5.31736155271656
    =SQRT(9*PI()) // 5.31736155271656 (equivalent)
    

### Error Handling

The SQRTPI function will return errors in the following cases:

*   **#NUM!** error: When the number argument is negative
*   **#VALUE!** error: When the number argument is not numeric

    =SQRTPI(-1) // Returns #NUM! error
    =SQRTPI("text") // Returns #VALUE! error
    =SQRTPI(TRUE) // Returns #VALUE! error
    

Related functions
-----------------

[![Excel PI function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pi%20function.png "Excel PI function")](https://exceljet.net/functions/pi-function)

### [PI Function](https://exceljet.net/functions/pi-function)

The Excel PI function returns the value of the geometric constant π (pi). The value represents a half-rotation in the radian angle system. The constant appears in many formulas relating the circle, such as the area of a circle....

[![Excel SQRT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sqrt%20function.png "Excel SQRT function")](https://exceljet.net/functions/sqrt-function)

### [SQRT Function](https://exceljet.net/functions/sqrt-function)

The Excel SQRT function returns the square root of a positive number. SQRT returns an error if _number_ is negative.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [PI Function](https://exceljet.net/functions/pi-function)
    
*   [SQRT Function](https://exceljet.net/functions/sqrt-function)
    

### Links

*   [Microsoft SQRTPI function documentation](https://support.office.com/en-us/article/sqrtpi-function-1fb4e63f-9b51-46d6-ad68-b3e7a8b519b4)
    

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
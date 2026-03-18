# Excel LCM function | Exceljet

**Source:** https://exceljet.net/functions/lcm-function

---

[Skip to main content](https://exceljet.net/functions/lcm-function#main-content)

[](https://exceljet.net/functions/lcm-function#)

*   [Previous](https://exceljet.net/functions/int-function)
    
*   [Next](https://exceljet.net/functions/ln-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

LCM Function
============

by Dave Bruns · Updated 13 Sep 2021

Related functions 
------------------

[GCD](https://exceljet.net/functions/gcd-function)

![Excel LCM function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20lcm%20function.png "Excel LCM function")

Summary
-------

The Excel LCM function returns the least common multiple of integers. The least common multiple is the smallest positive integer that is a multiple of all supplied numbers. For example, =LCM(25,40) returns 200.

Purpose 
--------

Get the least common multiple of numbers

Return value 
-------------

The least common multiple of all numbers

Syntax
------

    =LCM(number1,[number2],...)

*   _number1_ - The first number.
*   _number2_ - \[optional\] The second number.

Using the LCM function 
-----------------------

The LCM function returns the least common multiple of two or more numbers. The least common multiple is the smallest positive integer that is a multiple of all numbers supplied. Least common multiple is also known as the "least common denominator", and the "lowest common denominator". 

The LCM function takes one or more [arguments](https://exceljet.net/glossary/function-argument)
 called _number1_, _number2_, _number3_, etc. All numeric values are expected to be integers. Numbers with decimal values will be truncated to integers before a result is calculated. Each argument can be a hardcoded constant, a cell reference, or a [range](https://exceljet.net/glossary/range)
 that contains multiple values. The LCM function can accept up to 255 arguments total.

### Examples

The least common multiple of 3 and 4 is 12, since 12 is the smallest multiple of both 3 and 4:

    =LCM(3,4) // returns 12
    

The least common multiple of 3, 4, and 5 is 60, since 60 is the smallest multiple of all three numbers:

    =LCM(3,4,5) // returns 60
    

### Worksheet example

In the example worksheet shown above, we are using two slightly different formulas to calculate the lowest common multiple. The first formula provides two separate cell references, and the second formula uses a single range that contains three values. In rows, 5 to 10, there are two values in columns B and C, and the formula in F5:F10 (copied down) is:

    =LCM(B5,C5) // 2 cell references
    

In rows 11 to 15, there are three values in columns B, C, and D. The formula in F11:F15 (copied down) is:

    =LCM(B11:D11) // range with 3 values
    

Because the LCM function evaluates empty cells as zero, the result returned by LCM will be zero if any cell references are empty. Therefore, it's important not to include empty cell references.

### Notes

*   LCM evaluates empty cells as zero.
*   LCM works with integers; decimal values are removed before calculation.
*   If arguments contain a non-numeric value. LCM returns the #VALUE! error.
*   To calculate the greatest common divisor, see the [GCD function](https://exceljet.net/functions/gcd-function)
    .

Related functions
-----------------

[![Excel GCD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20gcd%20function.png "Excel GCD function")](https://exceljet.net/functions/gcd-function)

### [GCD Function](https://exceljet.net/functions/gcd-function)

The Excel GCD function returns the greatest common divisor of two or more integers. The greatest common divisor is the largest integer that goes into all supplied numbers without a remainder. For example, =GCD(60,36) returns 12.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [GCD Function](https://exceljet.net/functions/gcd-function)
    

### Links

*   [Microsoft LCM function documentation](https://support.office.com/en-us/article/lcm-function-7152b67a-8bb5-4075-ae5c-06ede5563c94)
    

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
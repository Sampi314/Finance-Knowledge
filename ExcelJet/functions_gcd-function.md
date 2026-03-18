# Excel GCD function | Exceljet

**Source:** https://exceljet.net/functions/gcd-function

---

[Skip to main content](https://exceljet.net/functions/gcd-function#main-content)

[](https://exceljet.net/functions/gcd-function#)

*   [Previous](https://exceljet.net/functions/floor.precise-function)
    
*   [Next](https://exceljet.net/functions/int-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

GCD Function
============

by Dave Bruns · Updated 13 Sep 2021

Related functions 
------------------

[LCM](https://exceljet.net/functions/lcm-function)

![Excel GCD function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20gcd%20function.png "Excel GCD function")

Summary
-------

The Excel GCD function returns the greatest common divisor of two or more integers. The greatest common divisor is the largest integer that goes into all supplied numbers without a remainder. For example, =GCD(60,36) returns 12.

Purpose 
--------

Get the greatest common divisor of numbers

Return value 
-------------

The largest positive integer that divides the numbers evenly

Syntax
------

    =GCD(number1,[number2],...)

*   _number1_ - The first number.
*   _number2_ - \[optional\] The second number.

Using the GCD function 
-----------------------

The GCD function returns the greatest common divisor of two or more integers. The greatest common divisor is the largest positive integer that divides the numbers without a remainder. In other words, the largest number that goes into all numbers evenly.

The GCD function takes one or more [arguments](https://exceljet.net/glossary/function-argument)
 called _number1_, _number2_, _number3_, etc. All numeric values are expected to be integers. Numbers with decimal values will be truncated to integers before a result is calculated. Each argument can be a hardcoded constant, a cell reference, or a [range](https://exceljet.net/glossary/range)
 that contains multiple values. The GCD function can accept up to 255 arguments total.

### Examples

To return the greatest common divisor of the numbers 60 and 36:

    =GCD(60,36) // returns 12
    

GCD returns the number 12, since 12 is the largest factor that goes into both numbers evenly. To get the greatest common divisor of 12, 16, 48:

    =GCD(12,16,48) // returns 4
    

In the example workbook shown above, the formula in F5 is:

    =GCD(B5:D5)
    

As the formula is copied down, the GCD function returns a new result for each row, based on the values in columns B, C, and D. Empty cells are evaluated as zero.

### Notes

*   GCD evaluates empty cells as zero.
*   GCD works with integers; decimal values are removed before calculation.
*   If arguments contain a non-numeric value. GCD returns the #VALUE! error.
*   To calculate the least common multiple, see the [LCM function](https://exceljet.net/functions/lcm-function)
    .

GCD function examples
---------------------

[![Excel formula: Calculate a ratio from two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_the_ratio_of_two_numbers.png "Excel formula: Calculate a ratio from two numbers")](https://exceljet.net/formulas/calculate-a-ratio-from-two-numbers)

### [Calculate a ratio from two numbers](https://exceljet.net/formulas/calculate-a-ratio-from-two-numbers)

This formula looks complicated, but, at the core, it is quite simple, and created in two parts like so: = (formula for number1)...

Related functions
-----------------

[![Excel LCM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lcm%20function.png "Excel LCM function")](https://exceljet.net/functions/lcm-function)

### [LCM Function](https://exceljet.net/functions/lcm-function)

The Excel LCM function returns the least common multiple of integers. The least common multiple is the smallest positive integer that is a multiple of all supplied numbers. For example, =LCM(25,40) returns 200.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate a ratio from two numbers](https://exceljet.net/formulas/calculate-a-ratio-from-two-numbers)
    

### Functions

*   [LCM Function](https://exceljet.net/functions/lcm-function)
    

### Links

*   [Microsoft GCD function documentation](https://support.office.com/en-us/article/gcd-function-d5107a51-69e3-461f-8e4c-ddfc21b5073a)
    

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
# Excel EVEN function | Exceljet

**Source:** https://exceljet.net/functions/even-function

---

[Skip to main content](https://exceljet.net/functions/even-function#main-content)

[](https://exceljet.net/functions/even-function#)

*   [Previous](https://exceljet.net/functions/decimal-function)
    
*   [Next](https://exceljet.net/functions/exp-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

EVEN Function
=============

by Dave Bruns · Updated 14 Aug 2021

Related functions 
------------------

[ODD](https://exceljet.net/functions/odd-function)

[EVEN](https://exceljet.net/functions/even-function)

[ROUND](https://exceljet.net/functions/round-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[MROUND](https://exceljet.net/functions/mround-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

![Excel EVEN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20even%20function.png "Excel EVEN function")

Summary
-------

The Excel EVEN function rounds numbers up to the next even integer. The EVEN function always rounds numbers away from zero, so positive numbers become larger and negative numbers become smaller (i.e. more negative).

Purpose 
--------

Round a number up to the next even integer

Return value 
-------------

An even integer.

Syntax
------

    =EVEN(number)

*   _number_ - The number to round up to an even integer.

Using the EVEN function 
------------------------

The EVEN function rounds numbers up to the next even integer. EVEN always rounds numbers away from zero, so positive numbers become larger and negative numbers become smaller (i.e. more negative).

EVEN takes just one argument, _number_, which should be a numeric value. With positive numbers, EVEN rounds _number_ up to the next even integer. With negative values, EVEN rounds _number_ down away from zero to the next negative integer. With zero (0) and numbers that are already even integers, _number_ is unchanged.

### Examples

The EVEN function rounds positive numbers up to the next even integer:

    =EVEN(1) // returns 2
    =EVEN(3.1) // returns 4
    

Negative numbers are rounded away from zero to the next even integer:

    =EVEN(-1) // returns -2
    =EVEN(-3.1) // returns -4
    

Zero and numbers that are already even integers are unaffected:

    =EVEN(2) // returns 2
    =EVEN(0) // returns 0
    =EVEN(-2) // returns -2
    

To round numbers up to the next _odd_ integer, see the [ODD function](https://exceljet.net/functions/odd-function)
.

Related functions
-----------------

[![Excel ODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20odd%20function.png "Excel ODD function")](https://exceljet.net/functions/odd-function)

### [ODD Function](https://exceljet.net/functions/odd-function)

The Excel ODD function returns the next odd integer after rounding a given number up. The ODD function always rounds numbers away from zero, so positive numbers become larger and negative numbers become smaller (i.e. more negative).

[![Excel EVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20even%20function.png "Excel EVEN function")](https://exceljet.net/functions/even-function)

### [EVEN Function](https://exceljet.net/functions/even-function)

The Excel EVEN function rounds numbers up to the next even integer. The EVEN function always rounds numbers away from zero, so positive numbers become larger and negative numbers become smaller (i.e. more negative).

[![Excel ROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20round%20function.png "Excel ROUND function")](https://exceljet.net/functions/round-function)

### [ROUND Function](https://exceljet.net/functions/round-function)

The Excel ROUND function returns a number rounded to a given number of digits. The ROUND function can round to the right or left of the decimal point.

[![Excel ROUNDDOWN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rounddown%20function.png "Excel ROUNDDOWN function")](https://exceljet.net/functions/rounddown-function)

### [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)

The Excel ROUNDDOWN function returns a number rounded down to a given number of places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDDOWN rounds _all numbers down_....

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

[![Excel MROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mround%20function.png "Excel MROUND function")](https://exceljet.net/functions/mround-function)

### [MROUND Function](https://exceljet.net/functions/mround-function)

The Excel MROUND function returns a number rounded to a given multiple. MROUND will round a number up or down, depending on the nearest multiple.

[![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")](https://exceljet.net/functions/floor-function)

### [FLOOR Function](https://exceljet.net/functions/floor-function)

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [ODD Function](https://exceljet.net/functions/odd-function)
    
*   [EVEN Function](https://exceljet.net/functions/even-function)
    
*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    

### Links

*   [Microsoft EVEN function documentation](https://support.office.com/en-us/article/even-function-197b5f06-c795-4c1e-8696-3c3b8a646cf9)
    

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
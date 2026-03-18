# Excel FLOOR.MATH function | Exceljet

**Source:** https://exceljet.net/functions/floor.math-function

---

[Skip to main content](https://exceljet.net/functions/floor.math-function#main-content)

[](https://exceljet.net/functions/floor.math-function#)

*   [Previous](https://exceljet.net/functions/floor-function)
    
*   [Next](https://exceljet.net/functions/floor.precise-function)
    

Excel 2013

[Math](https://exceljet.net/functions#Math)

FLOOR.MATH Function
===================

by Dave Bruns · Updated 15 Aug 2021

Related functions 
------------------

[MROUND](https://exceljet.net/functions/mround-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[ROUND](https://exceljet.net/functions/round-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[EVEN](https://exceljet.net/functions/even-function)

[ODD](https://exceljet.net/functions/odd-function)

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

![Excel FLOOR.MATH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20floor.math%20function.png "Excel FLOOR.MATH function")

Summary
-------

The Excel FLOOR.MATH function rounds a number down to a specified multiple. Unlike the [FLOOR function](https://exceljet.net/functions/floor-function)
, FLOOR.MATH defaults to a multiple of 1, and provides explicit support for rounding negative numbers.

Purpose 
--------

Round number down to nearest multiple

Return value 
-------------

A rounded number

Syntax
------

    =FLOOR.MATH(number,[significance],[mode])

*   _number_ - The number that should be rounded.
*   _significance_ - \[optional\] Multiple to use when rounding. Default is 1.
*   _mode_ - \[optional\] For rounding negative numbers toward or away from zero. Default is 0.

Using the FLOOR.MATH function 
------------------------------

The Excel FLOOR.MATH function rounds a number down to a given multiple, where multiple is provided as the _significance_ argument. If the number is already an exact multiple, no rounding occurs and the original number is returned.

The FLOOR.MATH function takes three [arguments](https://exceljet.net/glossary/function-argument)
, _number_, _significance, and mode_. _Number_ is the numeric value to round down, and is the only required argument. With no other input, FLOOR.MATH will round _number_ down to the next integer.

The _significance_ argument is the multiple to which _number_ should be rounded. In most cases, _significance_ is provided as a numeric value, but FLOOR.MATH can also understand [time](https://exceljet.net/glossary/excel-time)
 entered as text like "0:15". The default value of _significance_ is 1.

The _mode_ argument controls the direction negative values are rounded. By default, FLOOR.MATH rounds negative values _away_ from zero. Setting _mode_ to 1 or TRUE changes behavior so that negative values are rounded _toward zero_. The default value of mode is 0 or FALSE, so you can think of _mode_ as a setting that means "round toward zero". _Mode_ has no effect when _number_ is positive.

### Examples

By default, FLOOR.MATH rounds to the nearest integer, using a _significance_ of 1.

    =FLOOR.MATH(5.75) // returns 5
    =FLOOR.MATH(2.55) // returns 2
    

Provide a value for _significance_ to round to a different multiple:

    =FLOOR.MATH(5.75,1) // returns 5
    =FLOOR.MATH(5.75,3) // returns 3
    =FLOOR.MATH(5.75,0.5) // returns 5.5
    

### Rounding negative numbers

Positive numbers with decimal values are rounded down to the nearest integer, and negative numbers with decimal values are rounded away from zero:

    =FLOOR.MATH(6.7) // returns 6
    =FLOOR.MATH(-6.7) // returns -7
    

Control for rounding negative numbers toward zero or away from zero is provided with the (optional) _mode_ argument. _Mode_ defaults to zero or FALSE. When _mode_ is omitted, FLOOR.MATH rounds negative numbers _away_ from zero. When _mode_ is set to TRUE, FLOOR.MATH rounds negative numbers _toward_ zero. _Mode_ has no effect on positive numbers.

    =FLOOR.MATH(-4.1) // returns -5
    =FLOOR.MATH(-4.1,1) // returns -5
    =FLOOR.MATH(-4.1,1,TRUE) // returns -4
    

### FLOOR.MATH vs FLOOR

The FLOOR.MATH function differs from the [FLOOR function](https://exceljet.net/functions/floor-function)
 in these ways:

1.  Rounds down to the next integer by default (i.e. _significance_ defaults to 1)
2.  Provides explicit control for rounding negative numbers (toward zero, away from zero)
3.  Changing the sign of _significance_ has no effect on the result; use _mode_ instead.

### Notes

*   To round to the _nearest_ multiple _(_up or down) see the [MROUND function](https://exceljet.net/functions/mround-function)
    .
*   FLOOR.MATH works like [FLOOR](https://exceljet.net/functions/floor-function)
    , but provides control for rounding negative values. 
*   The _mode_ argument has no effect on positive numbers.
*   If _number_ is an exact multiple of significance, no rounding occurs.

Related functions
-----------------

[![Excel MROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mround%20function.png "Excel MROUND function")](https://exceljet.net/functions/mround-function)

### [MROUND Function](https://exceljet.net/functions/mround-function)

The Excel MROUND function returns a number rounded to a given multiple. MROUND will round a number up or down, depending on the nearest multiple.

[![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")](https://exceljet.net/functions/floor-function)

### [FLOOR Function](https://exceljet.net/functions/floor-function)

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

[![Excel ROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20round%20function.png "Excel ROUND function")](https://exceljet.net/functions/round-function)

### [ROUND Function](https://exceljet.net/functions/round-function)

The Excel ROUND function returns a number rounded to a given number of digits. The ROUND function can round to the right or left of the decimal point.

[![Excel ROUNDDOWN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rounddown%20function.png "Excel ROUNDDOWN function")](https://exceljet.net/functions/rounddown-function)

### [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)

The Excel ROUNDDOWN function returns a number rounded down to a given number of places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDDOWN rounds _all numbers down_....

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

[![Excel EVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20even%20function.png "Excel EVEN function")](https://exceljet.net/functions/even-function)

### [EVEN Function](https://exceljet.net/functions/even-function)

The Excel EVEN function rounds numbers up to the next even integer. The EVEN function always rounds numbers away from zero, so positive numbers become larger and negative numbers become smaller (i.e. more negative).

[![Excel ODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20odd%20function.png "Excel ODD function")](https://exceljet.net/functions/odd-function)

### [ODD Function](https://exceljet.net/functions/odd-function)

The Excel ODD function returns the next odd integer after rounding a given number up. The ODD function always rounds numbers away from zero, so positive numbers become larger and negative numbers become smaller (i.e. more negative).

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [EVEN Function](https://exceljet.net/functions/even-function)
    
*   [ODD Function](https://exceljet.net/functions/odd-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    

### Links

*   [Microsoft FLOOR.MATH function documentation](https://support.office.com/en-us/article/floor-math-function-c302b599-fbdb-4177-ba19-2c2b1249a2f5)
    

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
# Excel FLOOR.PRECISE function | Exceljet

**Source:** https://exceljet.net/functions/floor.precise-function

---

[Skip to main content](https://exceljet.net/functions/floor.precise-function#main-content)

[](https://exceljet.net/functions/floor.precise-function#)

*   [Previous](https://exceljet.net/functions/floor.math-function)
    
*   [Next](https://exceljet.net/functions/gcd-function)
    

Excel 2010

[Math](https://exceljet.net/functions#Math)

FLOOR.PRECISE Function
======================

by Dave Bruns · Updated 17 Aug 2021

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

![Excel FLOOR.PRECISE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20floor.precise%20function.png "Excel FLOOR.PRECISE function")

Summary
-------

The Excel FLOOR.PRECISE function rounds a number down to a given multiple. FLOOR.PRECISE defaults to a multiple of 1, and always rounds negative numbers away from zero.

Purpose 
--------

Round number down to nearest multiple

Return value 
-------------

A rounded number

Syntax
------

    =FLOOR.PRECISE(number,[significance])

*   _number_ - The number that should be rounded.
*   _significance_ - \[optional\] Multiple to use when rounding. Default is 1.

Using the FLOOR.PRECISE function 
---------------------------------

The Excel FLOOR.PRECISE function rounds a number _down_ to a given multiple, where multiple is provided as the _significance_ argument. If the number is already an exact multiple, no rounding occurs and the original number is returned.

The FLOOR.PRECISE function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _number_ and _significance._ The _number_ argument is the numeric value to round down, and is the only required argument. With no other input, CEILING.PRECISE will round _number_ up to the next integer.

The _significance_ argument is the multiple to which _number_ should be rounded. In most cases, _significance_ is provided as a numeric value, but FLOOR.PRECISE can also understand [time](https://exceljet.net/glossary/excel-time)
 entered as text like "0:15". The default value of _significance_ is 1.

### Examples

By default, FLOOR.PRECISE rounds down to the next integer, with a _significance_ of 1.

    =FLOOR.PRECISE(3.75) // returns 3
    =FLOOR.PRECISE(8.9) // returns 8
    

To round to a different multiple, provide a value for _significance_ :

    =FLOOR.PRECISE(5.75,3) // returns 3
    =FLOOR.PRECISE(5.75,2) // returns 4
    =FLOOR.PRECISE(5.75,0.5) // returns 5.5
    

### Rounding negative numbers

The FLOOR.PRECISE function always rounds negative numbers down away from zero, and ignores the sign of significance.

    =FLOOR.PRECISE(-4.1) // returns -5
    =FLOOR.PRECISE(-4.1,1) // returns -5
    =FLOOR.PRECISE(-4.1,-1) // returns -5
    

### FLOOR.PRECISE vs FLOOR

The FLOOR.PRECISE function differs from the [FLOOR function](https://exceljet.net/functions/floor-function)
 in these ways:

1.  Provides a default _significance_ of 1, rounding to nearest integer
2.  Always rounds negative numbers down away from zero
3.  Ignores the sign of _significance_ (uses the absolute value)

### Notes

*   FLOOR.PRECISE always rounds negative down away from zero.
*   If _number_ is an exact multiple of significance, no rounding occurs.
*   To round to the _nearest_ multiple _(_up or down) see the [MROUND function](https://exceljet.net/functions/mround-function)
    .

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

*   [Microsoft FLOOR.PRECISE function documentation](https://support.office.com/en-us/article/floor-precise-function-f769b468-1452-4617-8dc3-02f842a0702e)
    

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
# Excel CEILING.PRECISE function | Exceljet

**Source:** https://exceljet.net/functions/ceiling.precise-function

---

[Skip to main content](https://exceljet.net/functions/ceiling.precise-function#main-content)

[](https://exceljet.net/functions/ceiling.precise-function#)

*   [Previous](https://exceljet.net/functions/ceiling.math-function)
    
*   [Next](https://exceljet.net/functions/combin-function)
    

Excel 2010

[Math](https://exceljet.net/functions#Math)

CEILING.PRECISE Function
========================

by Dave Bruns · Updated 11 Sep 2021

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

![Excel CEILING.PRECISE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20ceiling.precise%20function.png "Excel CEILING.PRECISE function")

Summary
-------

The Excel CEILING.PRECISE function rounds a number up to a given multiple. CEILING.PRECISE defaults to a multiple of 1, and always rounds negative numbers toward zero.

Purpose 
--------

Round a number up to nearest multiple

Return value 
-------------

A rounded number.

Syntax
------

    =CEILING.PRECISE(number,[significance])

*   _number_ - The number that should be rounded.
*   _significance_ - \[optional\] Multiple to use when rounding. Default is 1.

Using the CEILING.PRECISE function 
-----------------------------------

The Excel CEILING.PRECISE function rounds a number up to a given multiple, where multiple is provided as the _significance_ argument. If the number is already an exact multiple, no rounding occurs and the original number is returned.

The CEILING.PRECISE function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _number_ and _significance._ The _number_ argument is the numeric value to round up, and is the only required argument. With no other input, CEILING.PRECISE will round _number_ up to the next integer.

The _significance_ argument is the multiple to which _number_ should be rounded. In most cases, _significance_ is provided as a numeric value, but CEILING.PRECISE can also understand time entered as text like "0:15". The default value of _significance_ is 1.

### Examples

By default, CEILING.PRECISE rounds up to the next integer, with a _significance_ of 1.

    =CEILING.PRECISE(1.25) // returns 2
    =CEILING.PRECISE(8.1) // returns 9
    

To round to a different multiple, provide a value for _significance_ :

    =CEILING.PRECISE(1.25,3) // returns 3
    =CEILING.PRECISE(4.1,3) // returns 6
    =CEILING.PRECISE(4.1,0.5) // returns 4.5
    

### Rounding negative numbers

By default, positive numbers with decimal portions are rounded up to the nearest integer, and negative numbers with decimal portions are rounded toward zero:

    =CEILING.MATH(6.3) // returns 7
    =CEILING.MATH(-6.3) // returns -6
    

The CEILING.PRECISE function always rounds negative numbers toward zero, and ignores the sign of significance.

    =CEILING.PRECISE(-4.1) // returns -4
    =CEILING.PRECISE(-4.1,1) // returns -4
    =CEILING.PRECISE(-4.1,-1) // returns -4
    

If you need control over rounding of negative values up or down, see the [CEILING.MATH function](https://exceljet.net/functions/ceiling.math-function)
.

### CEILING.PRECISE vs CEILING

The  [CEILING.PRECISE function](https://exceljet.net/functions/ceiling.precise-function)
 together with the [CEILING.MATH function](https://exceljet.net/functions/ceiling.math-function)
 replace the original [CEILING function](https://exceljet.net/functions/ceiling-function)
, which is now classified as a "[compatibility function](https://exceljet.net/glossary/compatibility-function)
". The behavior is very similar, but CEILING.PRECISE differs from the [CEILING function](https://exceljet.net/functions/ceiling-function)
 in these key ways:

1.  Defaults to a _significance_ of 1 (i.e. rounds up to nearest integer)
2.  Always rounds negative numbers toward zero
3.  Ignores the sign of significance argument (uses the absolute value)

### Notes

*   CEILING.PRECISE always rounds negative numbers toward zero.
*   If _number_ is an exact multiple of _significance_, no rounding occurs.
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

*   [Microsoft CEILING.PRECISE function documentation](https://support.office.com/en-us/article/ceiling-precise-function-f366a774-527a-4c92-ba49-af0a196e66cb)
    

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
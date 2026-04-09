# Excel ROUNDDOWN function | Exceljet

**Source:** https://exceljet.net/functions/rounddown-function

---

[Skip to main content](https://exceljet.net/functions/rounddown-function#main-content)

[](https://exceljet.net/functions/rounddown-function#)

*   [Previous](https://exceljet.net/functions/round-function)
    
*   [Next](https://exceljet.net/functions/roundup-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

ROUNDDOWN Function
==================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[ROUND](https://exceljet.net/functions/round-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[MROUND](https://exceljet.net/functions/mround-function)

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

![Excel ROUNDDOWN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20rounddown%20function.png "Excel ROUNDDOWN function")

Summary
-------

The Excel ROUNDDOWN function returns a number rounded down to a given number of places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDDOWN rounds _all numbers down_.

Purpose 
--------

Round down to given number of digits

Return value 
-------------

A rounded number.

Syntax
------

    =ROUNDDOWN(number,num_digits)

*   _number_ - The number to round down.
*   _num\_digits_ - The place at which number should be rounded.

Using the ROUNDDOWN function 
-----------------------------

The ROUNDDOWN function rounds numbers _down_. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDDOWN rounds _all numbers down_. For example:

    =ROUNDDOWN(3.999,0) // returns 3
    

ROUNDDOWN takes two arguments, _number_ and _num\_digits_. _Number_ is the number to be rounded, and _num\_digits_ is the place at which _number_ should be rounded. When _num\_digits_ is greater than zero, the ROUNDDOWN function rounds on the _right_ side of the decimal point. When _num\_digits_ is less or equal to zero, the ROUNDDOWN function rounds on the _left_ side of the decimal point. Use zero (0) for _num\_digits_ to round to the nearest integer. The table below summarizes this behavior:

| Digits | Behavior |
| --- | --- |
| \>0 | Round down to the nearest 0.1, 0.01, 0.001, etc. |
| <0  | Round down to the nearest 10, 100, 1000, etc. |
| \=0 | Round down to the nearest whole number |

### How ROUNDDOWN works

The ROUNDDOWN function works like the ROUND function except that it always rounds down. The steps look like this:

1\. Determine the precision. The precision is determined by the number of decimal places provided as the _num\_digits_ argument. For example, =ROUNDDOWN(A1,1) will round a number in A1 down to one decimal place, and =ROUNDDOWN(A1,0) will round down to the nearest whole number.

2\. Determine the rounding digit. This is the number in the place you are rounding to. For example, when rounding to the nearest whole number, the last number to keep is in the 1s position.

3\. Leave the rounding digit alone and treat the remaining digits to the right as zero. For example, to round the number 2.786 to the nearest tenth (i.e. 1 decimal place):

*   The rounding digit is 7 (the first digit after the decimal).
*   Treat the remaining digits as zero (2.700)
*   The number becomes 2.7.

We can get the same result with the ROUNDDOWN function like this:

    =ROUNDDOWN(2.786,0) // returns 2
    =ROUNDDOWN(2.786,1) // returns 2.7
    =ROUNDDOWN(2.786,2) // returns 2.78

> The ROUNDDOWN function is closely related to the [TRUNC function](https://exceljet.net/functions/trunc-function)
> . In fact, I'm not aware of any situation where the two functions return different results. If you know of a case, please [let me know](https://exceljet.net/contact)
> .

### Round to right of the decimal

To round down values to the _right_ of the decimal point, use a positive number for _num\_digits_: 

    =ROUNDDOWN(A1,1) // Round down to nearest tenth (0.1)
    =ROUNDDOWN(A1,2) // Round down to nearest hundredth (0.01)
    =ROUNDDOWN(A1,3) // Round down to nearest thousandth (0.001)
    =ROUNDDOWN(A1,4) // Round down to nearest ten-thousandth (0.0001)

The formulas above round a number in cell A1 down to the nearest 1 decimal place, the nearest 2 decimal places, the nearest 3 decimal places, and the nearest 4 decimal places.

### Round to left of the decimal

To round down values to the _left_ of the decimal point, use zero or a negative number for digits:  

    =ROUNDDOWN(A1,0) // Round down to nearest 1
    =ROUNDDOWN(A1,-1) // Round down to nearest 10
    =ROUNDDOWN(A1,-2) // Round down to nearest 100
    =ROUNDDOWN(A1,-3) // Round down to nearest 1000
    =ROUNDDOWN(A1,-4) // Round down to nearest 10000
    

### ROUNDDOWN with negative numbers

Excel's ROUNDDOWN function always rounds numbers down towards zero. You can see this behavior in the examples below, where the number to round is given as -2.786:

    =ROUNDDOWN(-2.786,0) // returns -2
    =ROUNDDOWN(-2.786,1) // returns -2.7
    =ROUNDDOWN(-2.786,2) // returns -2.78

Although you might think negative numbers should become "more negative",  ROUNDDOWN consistently moves toward zero.

### Nesting calculations inside ROUNDDOWN

Other operations and functions can be [nested](https://exceljet.net/glossary/nesting)
 inside ROUNDDOWN. For example, to round down the result of A1 divided by B1, you can use a formula like this:

    =ROUNDDOWN(A1/B1,0) // round down result to nearest integer
    

### Other rounding functions

Excel provides several rounding functions, each with a different behavior:

*   To round with standard rules, use the [ROUND function](https://exceljet.net/functions/round-function)
    .
*   To round to the nearest multiple, use the [MROUND function](https://exceljet.net/functions/mround-function)
    .
*   To round _down_ to the nearest specified _place_, use the [ROUNDDOWN function](https://exceljet.net/functions/rounddown-function)
    .
*   To round _down_ to the nearest specified _multiple_, use the [FLOOR function](https://exceljet.net/functions/floor-function)
    .
*   To round _up_ to the nearest specified _place_, use the [ROUNDUP function](https://exceljet.net/functions/roundup-function)
    .
*   To round _up_ to the nearest specified _multiple_, use the [CEILING function](https://exceljet.net/functions/ceiling-function)
    .
*   To round _down_ and return an integer only, use the [INT function](https://exceljet.net/functions/int-function)
    .
*   To truncate decimal places, use the [TRUNC function](https://exceljet.net/functions/trunc-function)
    .

### Notes

*   The ROUNDDOWN function rounds a number down to a given place by treating the remaining numbers as zero.
*   If the number is already rounded down to the given number of places, no rounding occurs.
*   If _number_ is not numeric, ROUNDDOWN returns a #VALUE! error.
*   If _num\_digits_ is not numeric, ROUNDDOWN returns a #VALUE! error.
*   ROUNDDOWN always rounds numbers toward zero.

ROUNDDOWN function examples
---------------------------

[![Excel formula: Round a number down](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20down.png "Excel formula: Round a number down")](https://exceljet.net/formulas/round-a-number-down)

### [Round a number down](https://exceljet.net/formulas/round-a-number-down)

The ROUNDDOWN function rounds a number down to a given number of places. The number of places is controlled by the number of digits provided in the second argument ( num\_digits ). For example, these formulas round the number 5.89 down to 1 and zero places: =ROUNDDOWN(5.89,1) // returns 5.8 =...

Related functions
-----------------

[![Excel ROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20round%20function.png "Excel ROUND function")](https://exceljet.net/functions/round-function)

### [ROUND Function](https://exceljet.net/functions/round-function)

The Excel ROUND function returns a number rounded to a given number of digits. The ROUND function can round to the right or left of the decimal point.

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

[![Excel ROUNDDOWN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rounddown%20function.png "Excel ROUNDDOWN function")](https://exceljet.net/functions/rounddown-function)

### [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)

The Excel ROUNDDOWN function returns a number rounded down to a given number of places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDDOWN rounds _all numbers down_....

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

[![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")](https://exceljet.net/functions/floor-function)

### [FLOOR Function](https://exceljet.net/functions/floor-function)

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

[![Excel MROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mround%20function.png "Excel MROUND function")](https://exceljet.net/functions/mround-function)

### [MROUND Function](https://exceljet.net/functions/mround-function)

The Excel MROUND function returns a number rounded to a given multiple. MROUND will round a number up or down, depending on the nearest multiple.

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

### Formulas

*   [Round a number down](https://exceljet.net/formulas/round-a-number-down)
    

### Functions

*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    

### Links

*   [Microsoft ROUNDDOWN function documentation](https://support.office.com/en-us/article/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53)
    

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
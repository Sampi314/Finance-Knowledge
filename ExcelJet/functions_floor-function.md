# Excel FLOOR function | Exceljet

**Source:** https://exceljet.net/functions/floor-function

---

[Skip to main content](https://exceljet.net/functions/floor-function#main-content)

[](https://exceljet.net/functions/floor-function#)

*   [Previous](https://exceljet.net/functions/factdouble-function)
    
*   [Next](https://exceljet.net/functions/floor.math-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

FLOOR Function
==============

by Dave Bruns · Updated 13 Sep 2021

Related functions 
------------------

[MROUND](https://exceljet.net/functions/mround-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[ROUND](https://exceljet.net/functions/round-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")

Summary
-------

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

Purpose 
--------

Round a number down to the nearest specified multiple

Return value 
-------------

A rounded number.

Syntax
------

    =FLOOR(number,significance)

*   _number_ - The number that should be rounded.
*   _significance_ - The multiple to use when rounding.

Using the FLOOR function 
-------------------------

The Excel FLOOR function rounds a number down to a given multiple. The multiple to use for rounding is provided as the _significance_ argument. If the number is already an exact multiple, no rounding occurs and the original number is returned.

The FLOOR function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _number_ and _significance_. _Number_ is the numeric value to round down. The _significance_ argument is the multiple to which _number_ should be rounded. In most cases, _significance_ is provided as a numeric value, but FLOOR can also understand time entered as text like "0:15". See the example below.

FLOOR works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but unlike MROUND, which rounds to the _nearest_ multiple, FLOOR _always rounds down_.

_Note: the FLOOR function is officially listed as a [compatibility function](https://exceljet.net/glossary/compatibility-function)
, replaced by [FLOOR.MATH](https://exceljet.net/functions/floor.math-function)
 and [FLOOR.PRECISE](https://exceljet.net/functions/floor.precise-function)
._

### Examples

The formulas below show how FLOOR rounds down values to a given multiple:

    =FLOOR(10,3) // returns 9
    =FLOOR(40,7) // returns 35
    =FLOOR(320,25) // returns 300
    =FLOOR(610,100) // returns 600
    =FLOOR(-5.4,1) // returns -6
    

To round a number in A1 _down_ to the nearest multiple of 5, you can use a formula like this:

    =FLOOR(A1,5)
    

### Round down to nearest 5

To round a number in A1 down to the nearest multiple of 5:

    =FLOOR(A1,5) // round down to nearest 5
    

### Round pricing down to end with .99

FLOOR can be used to set pricing after currency conversion, discounts, etc. For example, the formula below will round a number in A1 down to the next whole dollar, then subtract 1 cent, to return a price like $2.99, $5.99, $49.99, etc.

    =FLOOR(A1,1)-0.01
    

You can round pricing _up_ to end in .99 with a similar formula based on the [CEILING function](https://exceljet.net/functions/ceiling-function)
:

    =CEILING(A1,1)-0.01
    

### Round time down to nearest 15 minutes

FLOOR understands time formats, and can be used to round time down to a given multiple. For example, to round a time in A1 down to the previous 15 minute unit, you can use FLOOR like this:

    =FLOOR(A1,"0:15") // round time down to nearest 15 min
    

### Other rounding functions in Excel

*   To round normally, use the [ROUND function](https://exceljet.net/functions/round-function)
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

*   FLOOR works like the [MROUND function](https://exceljet.net/functions/mround-function)
    , but FLOOR always rounds down.
*   If a number is already an exact multiple of significance, no rounding occurs.
*   FLOOR rounds positive numbers down _toward zero._
*   If _number_ is negative, and _significance_ is positive, FLOOR rounds _away from zero_.
*   If _number_ and _significance_ are both negative, FLOOR rounds _towards zero_.
*   For more control over how FLOOR rounds negative numbers, see the [FLOOR.MATH function](https://exceljet.net/functions/floor.math-function)
    .

FLOOR function examples
-----------------------

[![Excel formula: Group times into 3 hour buckets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group%20times%20into%203%20hour%20buckets.png "Excel formula: Group times into 3 hour buckets")](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

### [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

If you need to group times into buckets (i.e. group by 6 hours, group by 3 hours, etc.) you can do so with a rounding function called FLOOR. In the example shown, we have a number of transactions, each with a timestamp. Let's say you want to group these transactions into buckets of 3 hours like...

[![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

### [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value. You can also express 15 minutes in a formula with this...

[![Excel formula: Round a number down to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20down%20to%20nearest%20multiple.png "Excel formula: Round a number down to nearest multiple")](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)

### [Round a number down to nearest multiple](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)

The Excel FLOOR function rounds a number down to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. FLOOR works like the MROUND function , but unlike MROUND, which rounds to the nearest...

[![Excel formula: Round to nearest 5](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20to%20nearest%205.png "Excel formula: Round to nearest 5")](https://exceljet.net/formulas/round-to-nearest-5)

### [Round to nearest 5](https://exceljet.net/formulas/round-to-nearest-5)

In the example, cell C6 contains this formula: =MROUND(B6,5) The value in B6 is 17 and the result is 15 since 15 is the nearest multiple of 5 to 17. Other multiples As you'd expect, you can use MROUND to round to other multiples as well: =MROUND(number,10) // nearest multiple of 10 =MROUND(number,...

Related functions
-----------------

[![Excel MROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mround%20function.png "Excel MROUND function")](https://exceljet.net/functions/mround-function)

### [MROUND Function](https://exceljet.net/functions/mround-function)

The Excel MROUND function returns a number rounded to a given multiple. MROUND will round a number up or down, depending on the nearest multiple.

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

[![Excel ROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20round%20function.png "Excel ROUND function")](https://exceljet.net/functions/round-function)

### [ROUND Function](https://exceljet.net/functions/round-function)

The Excel ROUND function returns a number rounded to a given number of digits. The ROUND function can round to the right or left of the decimal point.

[![Excel ROUNDDOWN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rounddown%20function.png "Excel ROUNDDOWN function")](https://exceljet.net/functions/rounddown-function)

### [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)

The Excel ROUNDDOWN function returns a number rounded down to a given number of places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDDOWN rounds _all numbers down_....

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

[![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")](https://exceljet.net/functions/floor-function)

### [FLOOR Function](https://exceljet.net/functions/floor-function)

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

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

*   [Round a number down to nearest multiple](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)
    
*   [Round to nearest 5](https://exceljet.net/formulas/round-to-nearest-5)
    
*   [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)
    
*   [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    

### Functions

*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    

### Links

*   [Microsoft FLOOR function documentation](https://support.office.com/en-us/article/floor-function-14bb497c-24f2-4e04-b327-b0b4de5a8886)
    

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
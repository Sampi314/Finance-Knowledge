# Excel MROUND function | Exceljet

**Source:** https://exceljet.net/functions/mround-function

---

[Skip to main content](https://exceljet.net/functions/mround-function#main-content)

[](https://exceljet.net/functions/mround-function#)

*   [Previous](https://exceljet.net/functions/mod-function)
    
*   [Next](https://exceljet.net/functions/multinomial-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

MROUND Function
===============

by Dave Bruns · Updated 18 Aug 2021

Related functions 
------------------

[CEILING](https://exceljet.net/functions/ceiling-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[ROUND](https://exceljet.net/functions/round-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[MROUND](https://exceljet.net/functions/mround-function)

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

![Excel MROUND function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20mround%20function.png "Excel MROUND function")

Summary
-------

The Excel MROUND function returns a number rounded to a given multiple. MROUND will round a number up or down, depending on the nearest multiple.

Purpose 
--------

Round a number to the nearest specified multiple

Return value 
-------------

A rounded number.

Syntax
------

    =MROUND(number,significance)

*   _number_ - The number that should be rounded.
*   _significance_ - The multiple to use when rounding.

Using the MROUND function 
--------------------------

The MROUND function rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the _significance_ argument. Rounding occurs when the remainder from dividing _number_ by _significance_ is greater than or equal to half the value of _significance._ If the number is already an exact multiple, no rounding occurs and the original number is returned.

The MROUND function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _number_ and _significance_. _Number_ is the numeric value to round. The _significance_ argument is the multiple to which _number_ should be rounded. In most cases, _significance_ is provided as a numeric value, but MROUND can also understand [time](https://exceljet.net/glossary/excel-time)
 entered as text like "0:15" or "0:30". _Number_ and _significance_ must have the same sign, otherwise MROUND will return a #NUM! error.

### Examples

Below are some examples of MROUND formulas with hardcoded values:

    =MROUND(10,3) // returns 9
    =MROUND(10,4) // returns 12
    =MROUND(119,25) // returns 125
    

To round a number in A1 to the nearest multiple of 5, you can use MROUND like this:

    =MROUND(A1,5) // round to nearest 5
    

### Nearest negative number

To round negative numbers with MROUND, use a negative sign for significance:

    =MROUND(-10,-3) // returns -9
    =MROUND(-10,-4) // returns -12
    =MROUND(-119,-25) // returns -125
    

### Nearest .99

MROUND can be used to round pricing to end with .99.  The formula below will round a value in A1 to the nearest 1 dollar, subtract 1 cent, and return a final price like $2.99, $5.99, $49.99, etc.

    =MROUND(A1,1) - 0.01 // round to nearest .99
    
    

### Nearest 15 minutes

MROUND can be used to round time. To round a time in A1 to the nearest 15 minutes, you can use a formula like this:

    =MROUND(A1,"0:15") // round to nearest 15 min
    

### Rounding functions in Excel

Excel provides a number of functions for rounding:

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

*   If a _number_ is already an exact multiple, no rounding occurs.
*   Rounding occurs when the remainder from dividing _number_ by _significance_ is greater than or equal to half the value of _significance._
*   _Number_ and _significance_ must have the same sign.
*   MROUND returns #NUM! if _number_ and _significance_ are not the same sign.
*   MROUND returns #VALUE! if _number_ or _significance_ is not numeric.

MROUND function examples
------------------------

[![Excel formula: Round to nearest 5](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20to%20nearest%205.png "Excel formula: Round to nearest 5")](https://exceljet.net/formulas/round-to-nearest-5)

### [Round to nearest 5](https://exceljet.net/formulas/round-to-nearest-5)

In the example, cell C6 contains this formula: =MROUND(B6,5) The value in B6 is 17 and the result is 15 since 15 is the nearest multiple of 5 to 17. Other multiples As you'd expect, you can use MROUND to round to other multiples as well: =MROUND(number,10) // nearest multiple of 10 =MROUND(number,...

[![Excel formula: Round a price to end in .99](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20a%20price%20to%20end%20in%20nearest%20.99.png "Excel formula: Round a price to end in .99")](https://exceljet.net/formulas/round-a-price-to-end-in-99)

### [Round a price to end in .99](https://exceljet.net/formulas/round-a-price-to-end-in-99)

In the example shown, the goal is to round a price to the nearest value ending in .99. So, for example, if a price is currently $5.31, the result should be $4.99. The best way to think about the problem is to restate it as "round a price to the nearest whole dollar, less 1 penny". In other words,...

[![Excel formula: Round a number to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20to%20nearest%20multiple.png "Excel formula: Round a number to nearest multiple")](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

### [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)

The MROUND function rounds a number to the nearest given multiple. The multiple to use for rounding is provided as the significance argument. If the number is already an exact multiple, no rounding occurs and the original number is returned. You can use MROUND to round prices, times, instrument...

[![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

### [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value. You can also express 15 minutes in a formula with this...

Related functions
-----------------

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

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

*   [Round a number to nearest multiple](https://exceljet.net/formulas/round-a-number-to-nearest-multiple)
    
*   [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    
*   [Round to nearest 5](https://exceljet.net/formulas/round-to-nearest-5)
    
*   [Round a price to end in .99](https://exceljet.net/formulas/round-a-price-to-end-in-99)
    

### Functions

*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    

### Links

*   [Microsoft MROUND function documentation](https://support.office.com/en-us/article/mround-function-c299c3b0-15a5-426d-aa4b-d2d5b3baf427)
    

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
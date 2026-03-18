# Excel TRUNC function | Exceljet

**Source:** https://exceljet.net/functions/trunc-function

---

[Skip to main content](https://exceljet.net/functions/trunc-function#main-content)

[](https://exceljet.net/functions/trunc-function#)

*   [Previous](https://exceljet.net/functions/sumxmy2-function)
    
*   [Next](https://exceljet.net/functions/acos-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

TRUNC Function
==============

by Dave Bruns · Updated 31 Aug 2021

Related functions 
------------------

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

[ROUND](https://exceljet.net/functions/round-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[MROUND](https://exceljet.net/functions/mround-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[ODD](https://exceljet.net/functions/odd-function)

[EVEN](https://exceljet.net/functions/even-function)

![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")

Summary
-------

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

Purpose 
--------

Truncate a number to a given precision

Return value 
-------------

A truncated number

Syntax
------

    =TRUNC(number,[num_digits])

*   _number_ - The number to truncate.
*   _num\_digits_ - \[optional\] The precision of the truncation (default is 0).

Using the TRUNC function 
-------------------------

The TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

The TRUNC function takes two [arguments](https://exceljet.net/glossary/function-argument)
: _number_ and _num\_digits_. _Number_ is the numeric value to truncate. The _num\_digits_ argument is optional and specifies the place at which _number_ should be truncated. _Num\_digits_ defaults to zero (0).

### Examples

By default, TRUNC will return the integer portion of a number:

    =TRUNC(4.9) // returns 4
    =TRUNC(-3.5) // returns -3
    

To control the place at which _number_ is truncated, provide a value for _num\_digits_. 

    =TRUNC(3.141593) // returns 3
    =TRUNC(3.141593,0) // returns 3
    =TRUNC(3.141593,1) // returns 3.1
    =TRUNC(3.141593,2) // returns 3.14
    =TRUNC(3.141593,3) // returns 3.141
    

When _num\_digits_ is negative, the TRUNC function will replace the number at a given place with zero:

    =TRUNC(999.99,0) // returns 999
    =TRUNC(999.99,-1) // returns 990
    =TRUNC(999.99,-2) // returns 900
    

### TRUNC vs. INT

The TRUNC function is similar to the [INT function](https://exceljet.net/functions/int-function)
 because they both can return the integer part of a number. However, TRUNC simply truncates a number, while INT actually rounds a number down to an integer. With positive numbers, and when TRUNC is using the default of 0 for num\_digits, both functions return the same results. With negative numbers, the results can be different. INT(-3.1) returns -4, because INT rounds down to the lower integer. TRUNC(-3.1) returns -3. If you simply want the integer part of a number, you should use TRUNC.

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

TRUNC function examples
-----------------------

[![Excel formula: Remove time from timestamp](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20time%20from%20timestamp.png "Excel formula: Remove time from timestamp")](https://exceljet.net/formulas/remove-time-from-timestamp)

### [Remove time from timestamp](https://exceljet.net/formulas/remove-time-from-timestamp)

In this example, the goal is to use a formula to remove the time value from a timestamp that includes both the date and time. To solve this problem, it's important to understand that Excel handles dates and time using a scheme in which dates are large serial numbers and times are fractional values...

[![Excel formula: Get decimal part of a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20decimal%20part%20of%20a%20number.png "Excel formula: Get decimal part of a number")](https://exceljet.net/formulas/get-decimal-part-of-a-number)

### [Get decimal part of a number](https://exceljet.net/formulas/get-decimal-part-of-a-number)

Excel contains a number of rounding functions. Two of these functions, the INT function and the TRUNC function will return the integer portion of a number that contains a decimal value. The INT function behaves a bit differently with negative values, so in this example we are using the TRUNC...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

[![Excel formula: Get integer part of a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20integer%20part%20of%20a%20number.png "Excel formula: Get integer part of a number")](https://exceljet.net/formulas/get-integer-part-of-a-number)

### [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)

With TRUNC, no rounding takes place. The TRUNC function simply slices off the decimal part of the number with default settings. TRUNC actually takes an optional second argument to specify the precision of truncation, but when you don't supply this optional argument, it is assumed to be zero, and...

[![Excel formula: Number is whole number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/number%20is%20whole%20number.png "Excel formula: Number is whole number")](https://exceljet.net/formulas/number-is-whole-number)

### [Number is whole number](https://exceljet.net/formulas/number-is-whole-number)

In this example, the goal is to test if a numeric value is a whole number. There are several ways to go about this. One of the easiest ways is to use the MOD function with a divisor of 1. Any whole number divided by 1 will result in a remainder of zero: =MOD(5,1)=0 // whole numbers return zero Any...

[![Excel formula: Data validation whole percentage only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20whole%20percentage%20only3.png "Excel formula: Data validation whole percentage only")](https://exceljet.net/formulas/data-validation-whole-percentage-only)

### [Data validation whole percentage only](https://exceljet.net/formulas/data-validation-whole-percentage-only)

The Excel TRUNC function does no rounding, it just returns a truncated number. It has an optional second argument (num\_digits) to specify precision. When num\_digits is not provided, it defaults to zero. In this formula for data validation, we use TRUNC to get the non-decimal part of a percentage,...

TRUNC function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/3%20Basic%20Array%20Formulas-Play.png)](https://exceljet.net/videos/3-basic-array-formulas)

### [3 basic array formulas](https://exceljet.net/videos/3-basic-array-formulas)

In this video we'll look at three basic array formula examples. The latest version of Excel ships with new functions like UNIQUE , SORT, FILTER and so on that make certain array formulas easy. But you can still build traditional array formulas as well, and they can solve some tricky problems. In...

Related functions
-----------------

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

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

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

[![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")](https://exceljet.net/functions/floor-function)

### [FLOOR Function](https://exceljet.net/functions/floor-function)

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

[![Excel ODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20odd%20function.png "Excel ODD function")](https://exceljet.net/functions/odd-function)

### [ODD Function](https://exceljet.net/functions/odd-function)

The Excel ODD function returns the next odd integer after rounding a given number up. The ODD function always rounds numbers away from zero, so positive numbers become larger and negative numbers become smaller (i.e. more negative).

[![Excel EVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20even%20function.png "Excel EVEN function")](https://exceljet.net/functions/even-function)

### [EVEN Function](https://exceljet.net/functions/even-function)

The Excel EVEN function rounds numbers up to the next even integer. The EVEN function always rounds numbers away from zero, so positive numbers become larger and negative numbers become smaller (i.e. more negative).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    
*   [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)
    
*   [Remove time from timestamp](https://exceljet.net/formulas/remove-time-from-timestamp)
    
*   [Number is whole number](https://exceljet.net/formulas/number-is-whole-number)
    
*   [Data validation whole percentage only](https://exceljet.net/formulas/data-validation-whole-percentage-only)
    
*   [Get decimal part of a number](https://exceljet.net/formulas/get-decimal-part-of-a-number)
    
*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    

### Videos

*   [3 basic array formulas](https://exceljet.net/videos/3-basic-array-formulas)
    

### Functions

*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    
*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [ODD Function](https://exceljet.net/functions/odd-function)
    
*   [EVEN Function](https://exceljet.net/functions/even-function)
    

### Links

*   [Microsoft TRUNC function documentation](https://support.office.com/en-us/article/trunc-function-8b86a64c-3127-43db-ba14-aa5ceb292721)
    

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
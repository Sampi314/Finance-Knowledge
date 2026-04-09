# Excel CEILING function | Exceljet

**Source:** https://exceljet.net/functions/ceiling-function

---

[Skip to main content](https://exceljet.net/functions/ceiling-function#main-content)

[](https://exceljet.net/functions/ceiling-function#)

*   [Previous](https://exceljet.net/functions/base-function)
    
*   [Next](https://exceljet.net/functions/ceiling.math-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

CEILING Function
================

by Dave Bruns · Updated 10 Sep 2021

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

![Excel CEILING function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")

Summary
-------

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

Purpose 
--------

Round a number up to nearest multiple

Return value 
-------------

A rounded number.

Syntax
------

    =CEILING(number,significance)

*   _number_ - The number that should be rounded.
*   _significance_ - The multiple to use when rounding.

Using the CEILING function 
---------------------------

The Excel CEILING function rounds a number up to a given multiple. The multiple to use for rounding is provided as the _significance_ argument. If the number is already an exact multiple, no rounding occurs and the original number is returned.

The CEILING function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _number,_ and _significance_. _Number_ is the numeric value to round up. The _significance_ argument is the multiple to which _number_ should be rounded. In most cases, _significance_ is provided as a numeric value, but CEILING can also understand time entered as text like "0:15". See the example below.

CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, which also rounds to a given multiple. However, unlike MROUND, which rounds to the _nearest_ multiple, the CEILING function rounds up to the _next_ multiple.

_Note: the CEILING function is officially listed as a [compatibility function](https://exceljet.net/glossary/compatibility-function)
, replaced by [CEILING.MATH](https://exceljet.net/functions/ceiling.math-function)
 and [CEILING.PRECISE](https://exceljet.net/functions/ceiling.precise-function)
._

### Examples

The formulas below show how CEILING rounds up values to a given multiple:

    =CEILING(10,3) // returns 12
    =CEILING(36,7) // returns 42
    =CEILING(309,25) // returns 325
    =CEILING(610,100) // returns 700
    =CEILING(-5.4,1) // returns -5
    

To round a number in A1 _up_ to the nearest multiple of 5, you can use a formula like this:

    =CEILING(A1,5)
    

### Round pricing up to end with .99

CEILING can be useful to set pricing after currency conversion or discounts are applied. For example, the formula below will round a value in A1 up to the next whole dollar, then subtract 1 cent, to return a price like $2.99, $5.99, $49.99, etc.

    =CEILING(A1,1) - 0.01
    
    

### Round time up to nearest 15 minutes

CEILING understands time formats and can be used to round time up to a given multiple. For example, to round a time in A1 up to the nearest 15 minutes, you can use CEILING like this:

    =CEILING(A1,"0:15") // round up to nearest 15 min
    

### Other rounding functions

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

*   CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
    , but CEILING always rounds up.
*   If _number_ is an exact multiple of significance, no rounding occurs.
*   If _number_ and _significance_ are both negative, CEILING rounds down, _away from zero_.
*   If _number_ is negative, and _significance_ is positive, CEILING rounds up, _towards zero_.
*   For more control over how CEILING rounds negative numbers, see the [CEILING.MATH function](https://exceljet.net/functions/ceiling.math-function)
    .

CEILING function examples
-------------------------

[![Excel formula: Running count group by n size](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20group%20by%20n%20size.png "Excel formula: Running count group by n size")](https://exceljet.net/formulas/running-count-group-by-n-size)

### [Running count group by n size](https://exceljet.net/formulas/running-count-group-by-n-size)

The core of this formula is the COUNTA function, configured with an expanding range like this: COUNTA($B$5:B5) As the formula is copied down the column, the range starting with B5 expands to include each new row, and COUNTA returns a running count of all non-blank entries in the range. The result...

[![Excel formula: Shade alternating groups of n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Shade%20alternating%20groups%20of%20n%20rows.png "Excel formula: Shade alternating groups of n rows")](https://exceljet.net/formulas/shade-alternating-groups-of-n-rows)

### [Shade alternating groups of n rows](https://exceljet.net/formulas/shade-alternating-groups-of-n-rows)

Working from the inside out, we first "normalize" row numbers to begin with 1 using the ROW function and an offset: ROW()-offset In this case, the first row of data is in row 5, so we use an offset of 4: ROW()-4 // 1 in row 5 ROW()-4 // 2 in row 6 ROW()-4 // 3 in row 7 etc. The result goes into the...

[![Excel formula: Round to nearest 5](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20to%20nearest%205.png "Excel formula: Round to nearest 5")](https://exceljet.net/formulas/round-to-nearest-5)

### [Round to nearest 5](https://exceljet.net/formulas/round-to-nearest-5)

In the example, cell C6 contains this formula: =MROUND(B6,5) The value in B6 is 17 and the result is 15 since 15 is the nearest multiple of 5 to 17. Other multiples As you'd expect, you can use MROUND to round to other multiples as well: =MROUND(number,10) // nearest multiple of 10 =MROUND(number,...

[![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

### [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value. You can also express 15 minutes in a formula with this...

[![Excel formula: Round a number up to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up%20to%20nearest%20multiple.png "Excel formula: Round a number up to nearest multiple")](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

### [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

The Excel CEILING function rounds a number up to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. CEILING works like the MROUND function , but unlike MROUND, which rounds to the...

[![Excel formula: Round a number up to next half](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up%20to%20next%20half.png "Excel formula: Round a number up to next half")](https://exceljet.net/formulas/round-a-number-up-to-next-half)

### [Round a number up to next half](https://exceljet.net/formulas/round-a-number-up-to-next-half)

The Excel CEILING function rounds a number up to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. In this example, we want to round up to the nearest half, so we provide 0.5 to...

[![Excel formula: Round price to end in .45 or .95](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20price%20to%20end%20in%2045%20or%2095.png "Excel formula: Round price to end in .45 or .95")](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95)

### [Round price to end in .45 or .95](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95)

The key to solving this problem is to realize that the solution requires a specific kind of rounding. We can't just round to the "nearest" .45 or .95 value. In fact, the first step is to round up to the nearest half dollar (.50). The second step is to subtract 5 cents ($0.05). To round up to the...

[![Excel formula: Next biweekly payday from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20biweekly%20payday%20from%20date.png "Excel formula: Next biweekly payday from date")](https://exceljet.net/formulas/next-biweekly-payday-from-date)

### [Next biweekly payday from date](https://exceljet.net/formulas/next-biweekly-payday-from-date)

This formula depends on the CEILING function , which rounds numbers up to a given multiple. It works because of how dates work in Excel's default 1900 date system, where the first day is the number 1, which is Sunday, January 1, 1900. In this scheme, the first Friday is day number 6, the second...

[![Excel formula: Round by bundle size](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round_by_bundle_size_0.png "Excel formula: Round by bundle size")](https://exceljet.net/formulas/round-by-bundle-size)

### [Round by bundle size](https://exceljet.net/formulas/round-by-bundle-size)

In this example, the context is that a certain number of items are needed and the items are only available in bundles of a set size. The goal is to calculate the number of bundles needed based on the items in each bundle, and the number of items needed. For example: If you need 6 items, and the...

CEILING function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Shade%20groups%20of%20rows%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)

### [Shade groups of rows with conditional formatting](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade alternating groups of rows. For example, you can use this approach to shade groups of 3 rows, groups of 4 rows, and so on. This can be a nice way to make certain tables easier to read. Here we have a table with 3 rows of data...

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

### Formulas

*   [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)
    
*   [Round price to end in .45 or .95](https://exceljet.net/formulas/round-price-to-end-in-.45-or-.95)
    
*   [Running count group by n size](https://exceljet.net/formulas/running-count-group-by-n-size)
    
*   [Round a number up to next half](https://exceljet.net/formulas/round-a-number-up-to-next-half)
    
*   [Shade alternating groups of n rows](https://exceljet.net/formulas/shade-alternating-groups-of-n-rows)
    
*   [Next biweekly payday from date](https://exceljet.net/formulas/next-biweekly-payday-from-date)
    
*   [Round by bundle size](https://exceljet.net/formulas/round-by-bundle-size)
    
*   [Round to nearest 5](https://exceljet.net/formulas/round-to-nearest-5)
    
*   [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    

### Videos

*   [Shade groups of rows with conditional formatting](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)
    

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

*   [Microsoft CEILING function documentation](https://support.office.com/en-us/article/ceiling-function-0a5cd7c8-0720-4f0a-bd2c-c943e510899f)
    

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
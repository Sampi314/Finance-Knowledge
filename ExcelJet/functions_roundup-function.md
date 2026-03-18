# Excel ROUNDUP function | Exceljet

**Source:** https://exceljet.net/functions/roundup-function

---

[Skip to main content](https://exceljet.net/functions/roundup-function#main-content)

[](https://exceljet.net/functions/roundup-function#)

*   [Previous](https://exceljet.net/functions/rounddown-function)
    
*   [Next](https://exceljet.net/functions/sign-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

ROUNDUP Function
================

by Dave Bruns · Updated 17 Apr 2024

Related functions 
------------------

[ROUND](https://exceljet.net/functions/round-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[MROUND](https://exceljet.net/functions/mround-function)

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")

Summary
-------

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_.

Purpose 
--------

Round a number up to a given number of digits

Return value 
-------------

A rounded number.

Syntax
------

    =ROUNDUP(number,num_digits)

*   _number_ - The number to round up.
*   _num\_digits_ - The place at which number should be rounded.

Using the ROUNDUP function 
---------------------------

The ROUNDUP function rounds numbers _up_. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_. For example:

    =ROUNDUP(3.001,0) // returns 4
    

ROUNDUP takes two arguments, _number_ and _num\_digits_. _Number_ is the number to be rounded, and _num\_digits_ is the place at which the number should be rounded. When _num\_digits_ is greater than zero, the ROUNDUP function rounds on the _right_ side of the decimal point. When _num\_digits_ is less or equal to zero, the ROUNDUP function rounds on the _left_ side of the decimal point. Use zero (0) for _num\_digits_ to round to the nearest integer. The table below summarizes this behavior:

| Digits | Behavior |
| --- | --- |
| \>0 | Round up to the nearest 0.1, 0.01, 0.001, etc. |
| <0  | Round up to the nearest 10, 100, 1000, etc. |
| \=0 | Round up to the nearest whole number |

### How ROUNDUP works

The ROUNDUP function works like the ROUND function except that it always rounds up. The steps look like this:

1\. Determine the precision. The precision is determined by the _num\_digits_ argument, which sets the number of decimal places to be returned. For example, =ROUNDUP(A1,1) will round a number in A1 up to one decimal place, and =ROUNDUP(A1,0) will round up to the nearest whole number.

2\. Determine the rounding digit. This is the number in the place you are rounding to. For example, when rounding to the nearest whole number, the last number to keep is in the 1s position.

3\. If any non-zero numbers follow the rounding digit, increment the rounding digit by 1. For example, to round the number 2.123 to up the nearest tenth (i.e. 1 decimal place):

*   The rounding digit is 1 (the first digit after the decimal).
*   The following numbers are non-zero.
*   The 2 is incremented by 1 and the result is 3.

We can get the same result with the ROUNDDOWN function like this:

    =ROUNDUP(2.123,0) // returns 3
    =ROUNDUP(2.123,1) // returns 2.2
    =ROUNDUP(2.123,2) // returns 2.13
    =ROUNDUP(2.123,3) // returns 2.123

### Round to right of the decimal

To round up values to the _right_ of the decimal point, use a positive number for digits: 

    =ROUNDUP(A1,1) // Round up to nearest tenth (0.1)
    =ROUNDUP(A1,2) // Round up to nearest hundredth (0.01)
    =ROUNDUP(A1,3) // Round up to nearest thousandth (0.001)
    =ROUNDUP(A1,4) // Round up to nearest ten-thousandth (0.0001)

The formulas above will round a number in cell A1 up to the nearest 1 decimal place, the nearest 2 decimal places, the nearest 3 decimal places, and the nearest 4 decimal places.

### Round to left of the decimal

To round up values to the _left_ of the decimal point, use zero or a negative number for digits:  

    =ROUNDUP(A1,0) // Round up to nearest whole number
    =ROUNDUP(A1,-1) // Round up to nearest 10
    =ROUNDUP(A1,-2) // Round up to nearest 100
    =ROUNDUP(A1,-3) // Round up to nearest 1000
    =ROUNDUP(A1,-4) // Round up to nearest 10000
    

### ROUNDUP with negative numbers

Excel's ROUNDUP function always rounds numbers up away from zero, to a specified number of digits. You can see this behavior in the examples below:

    =ROUNDUP(-2.123,0) // returns -3
    =ROUNDUP(-2.123,1) // returns -2.2
    =ROUNDUP(-2.123,2) // returns -2.13
    =ROUNDUP(-2.123,3) // returns -2.123

This might seem counterintuitive because the number becomes "larger" as an absolute value, but ROUNDUP consistently moves rounded numbers away from zero.

### Nesting calculations inside ROUNDUP

Other operations and functions can be [nested](https://exceljet.net/glossary/nesting)
 inside the ROUNDUP function. For example, to round the result of A1 divided by B1, you can use a formula like this:

    =ROUNDUP(A1/B1,0) // round up result to nearest integer
    

### Other rounding functions

Excel provides several rounding functions, each with a different behavior:

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

*   The ROUNDUP function rounds a number down to a given place by treating the remaining numbers as zero.
*   If the number is already rounded down to the given number of places, no rounding occurs.
*   If _number_ is not numeric, ROUNDUP returns a #VALUE! error.
*   If _num\_digits_ is not numeric, ROUNDUP returns a #VALUE! error.
*   ROUNDUP always rounds numbers away from zero.

ROUNDUP function examples
-------------------------

[![Excel formula: Randomly assign people to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_people_to_groups.png "Excel formula: Randomly assign people to groups")](https://exceljet.net/formulas/randomly-assign-people-to-groups)

### [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)

In this example, the goal is to randomly assign the names in column B to three groups of equal size. The group names are "A", "B", and "C", and these values appear in the named range groups (F5:F7). The solution should automatically count the number of groups to assign and attempt to generate the...

[![Excel formula: Round a number up](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up.png "Excel formula: Round a number up")](https://exceljet.net/formulas/round-a-number-up)

### [Round a number up](https://exceljet.net/formulas/round-a-number-up)

The ROUNDUP function rounds a number up to a given number of places. The number of places is controlled by the number of digits provided in the second argument ( num\_digits ). For example, these formulas round the number 5.13 up to 1 and zero places: =ROUNDUP(5.13,1) // returns 5.2 =ROUNDUP(5.13,0...

[![Excel formula: Get quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20quarter%20from%20date.png "Excel formula: Get quarter from date")](https://exceljet.net/formulas/get-quarter-from-date)

### [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)

In this example, the goal is to return a number that represents quarter (i.e. 1,2,3,4) for any given date. In other words, we want to return the quarter that the date resides in. ROUNDUP formula solution In the example shown, the formula in cell C5 is: =ROUNDUP(MONTH(B5)/3,0) The ROUNDUP function...

[![Excel formula: Count with repeating values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20with%20repeating%20values.png "Excel formula: Count with repeating values")](https://exceljet.net/formulas/count-with-repeating-values)

### [Count with repeating values](https://exceljet.net/formulas/count-with-repeating-values)

The core of this formula is the ROUNDUP function. The ROUNDUP function works like the ROUND function except that when rounding, the ROUNDUP function will always round the numbers 1-9 up. In this formula, we use that fact to repeat values. To supply a number to ROUNDUP, we are using this expression...

[![Excel formula: Sum by quarter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20quarter.png "Excel formula: Sum by quarter")](https://exceljet.net/formulas/sum-by-quarter)

### [Sum by quarter](https://exceljet.net/formulas/sum-by-quarter)

In this example, the goal is to sum the amounts in column C by quarter in column G. Column D is a helper column , and the formula to calculate quarters from the dates in column B is explained below. All data is in an Excel Table named data in the range B5:E16. This problem can be solved with the...

Related functions
-----------------

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

*   [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)
    
*   [Count with repeating values](https://exceljet.net/formulas/count-with-repeating-values)
    
*   [Sum by quarter](https://exceljet.net/formulas/sum-by-quarter)
    
*   [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)
    
*   [Round a number up](https://exceljet.net/formulas/round-a-number-up)
    

### Functions

*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    

### Links

*   [Microsoft ROUNDUP function documentation](https://support.office.com/en-us/article/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7)
    

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
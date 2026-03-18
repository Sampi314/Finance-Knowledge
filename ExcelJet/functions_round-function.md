# Excel ROUND function | Exceljet

**Source:** https://exceljet.net/functions/round-function

---

[Skip to main content](https://exceljet.net/functions/round-function#main-content)

[](https://exceljet.net/functions/round-function#)

*   [Previous](https://exceljet.net/functions/roman-function)
    
*   [Next](https://exceljet.net/functions/rounddown-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

ROUND Function
==============

by Dave Bruns · Updated 16 Apr 2024

Related functions 
------------------

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[MROUND](https://exceljet.net/functions/mround-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

![Excel ROUND function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20round%20function.png "Excel ROUND function")

Summary
-------

The Excel ROUND function returns a number rounded to a given number of digits. The ROUND function can round to the right or left of the decimal point.

Purpose 
--------

Round a number to a given number of digits

Return value 
-------------

A rounded number.

Syntax
------

    =ROUND(number,num_digits)

*   _number_ - The number to round.
*   _num\_digits_ - The place at which number should be rounded.

Using the ROUND function 
-------------------------

The ROUND function rounds a number to a given number of places. ROUND rounds up when the last significant digit is 5 or greater, and rounds down when the last significant digit is less than 5.

ROUND takes two arguments, _number_ and _num\_digits_. _Number_ is the number to be rounded, and _num\_digits_ is the place at which the number should be rounded. When _num\_digits_ is greater than zero, the ROUND function rounds on the _right_ side of the decimal point. When _num\_digits_ is less or equal to zero, the ROUND function rounds on the _left_ side of the decimal point. Use zero (0) for _num\_digits_ to round to the nearest integer. This behavior is summarized in the table below:  

| Digits | Behavior |
| --- | --- |
| \>0 | Round to the nearest 0.1, 0.01, 0.001, etc. |
| <0  | Round to the nearest 10, 100, 1000, etc. |
| \=0 | Round to the nearest whole number |

### How ROUND works

Rounding simplifies numbers by decreasing the number of digits while keeping the number close to its original value. The result is less accurate, but easier to use. The ROUND function uses a standard rounding process like this:

1\. Determine the precision. The precision is determined by the number of decimal places provided as the _num\_digits_ argument. For example, =ROUND(A1,1) will round a number in A1 to one decimal place, and =ROUND(A1,0) will round to the nearest whole number.

2\. Determine the rounding digit. This is the number in the place you are rounding to. For example, when rounding to the nearest whole number, the last number to keep is in the 1s position.

3\. Round the number based on the _next number to the right_. Leave the rounding digit the same if the next number to the right is less than 5. Increase the rounding digit by 1 if the next number is 5 or more. For example, to round the number 2.786 to the nearest tenth:

*   The rounding digit is 7 (the first digit after the decimal).
*   The next digit is 8.
*   Since 8 is greater than 5, round up the 7 to 8.
*   The number becomes 2.8.

We can get the same result with the ROUND function by providing 1 as _num\_digits_:

    =ROUND(2.786,1) // returns 2.8

### Round to right

To round values to the _right_ of the decimal point, use a _positive_ number for digits:  

    =ROUND(A1,1) // Round to nearest tenth (0.1)
    =ROUND(A1,2) // Round to nearest hundredth (0.01)
    =ROUND(A1,3) // Round to nearest thousandth (0.001)
    =ROUND(A1,4) // Round to nearest ten-thousandth (0.0001)

### Round to left

To round down values to the _left_ of the decimal point, use _zero_ or a _negative_ number for digits:  

    =ROUND(A1,0) // Round to nearest whole number
    =ROUND(A1,-1) // Round to nearest 10
    =ROUND(A1,-2) // Round to nearest 100
    =ROUND(A1,-3) // Round to nearest 1000
    =ROUND(A1,-4) // Round to nearest 10000
    

### Nesting inside ROUND

Other operations and functions can be [nested](https://exceljet.net/glossary/nesting)
 inside the ROUND function. For example, to round down the result of A1 divided by B1, you can ROUND in a formula like this:

    =ROUND(A1/B1,0) // round result to nearest integer
    

Any formula that returns a numeric result can be nested inside the ROUND function.

### Rounding vs. formatting

It's important to understand that Excel can perform "visual rounding" with [number formatting](https://exceljet.net/glossary/number-format)
. When number formatting is applied to a number, Excel will display the number of places specified in the format, rounding as necessary. For example, with the value 2.786 in cell A1:

*   Excel displays 2.786 when the "General" number format is applied to A1.
*   Excel displays 2.79 when the number format "0.00" is applied to A1.
*   Excel displays 2.8 when the number format "0.0" is applied to A1.
*   Excel displays 3 when the number format "0" is applied to A1.

Number formats affect the _display_ of a number only, and the original value is not modified. In contrast, the ROUND function will round a number and return a _modified number_ as a final result. For details on Excel's custom number formatting with many examples, [see this article](https://exceljet.net/articles/custom-number-formats)
.

### Other rounding functions

Excel provides several rounding functions, each with a different behavior:

*   To round with standard rules, use the [ROUND function](https://exceljet.net/functions/round-function)
    .
*   To round to the nearest _multiple_, use the [MROUND function](https://exceljet.net/functions/mround-function)
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

*   The ROUND function rounds a number to a specified level of precision, determined by _num\_digits_.
*   If the number is already rounded to the given number of places, no rounding occurs.
*   If the number is not numeric, ROUND returns a #VALUE! error.
*   If _num\_digits_ is not numeric, ROUND returns a #VALUE! error.

ROUND function examples
-----------------------

[![Excel formula: Round number to n significant figures](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round_number_to_n_significant_figures.png "Excel formula: Round number to n significant figures")](https://exceljet.net/formulas/round-number-to-n-significant-figures)

### [Round number to n significant figures](https://exceljet.net/formulas/round-number-to-n-significant-figures)

In this example, the goal is to round a number to a given number of significant figures while preserving trailing zeros when needed. This is a tricky problem because Excel's rounding functions return numbers, and numbers don't preserve trailing zeros. This article uses "significant figures" and "...

[![Excel formula: Round a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20a%20number.png "Excel formula: Round a number")](https://exceljet.net/formulas/round-a-number)

### [Round a number](https://exceljet.net/formulas/round-a-number)

The ROUND function rounds a number to a given number of places. The number of places is set by the number of digits provided in the second argument ( num\_digits ). For example, the formulas below round the number 5.86 to 1 and zero places: =ROUND(5.86,1) // returns 5.9 =ROUND(5.86,0) // returns 6...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Round a price to end in .99](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round%20a%20price%20to%20end%20in%20nearest%20.99.png "Excel formula: Round a price to end in .99")](https://exceljet.net/formulas/round-a-price-to-end-in-99)

### [Round a price to end in .99](https://exceljet.net/formulas/round-a-price-to-end-in-99)

In the example shown, the goal is to round a price to the nearest value ending in .99. So, for example, if a price is currently $5.31, the result should be $4.99. The best way to think about the problem is to restate it as "round a price to the nearest whole dollar, less 1 penny". In other words,...

[![Excel formula: Round to nearest 1000](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20to%20nearest%201000.png "Excel formula: Round to nearest 1000")](https://exceljet.net/formulas/round-to-nearest-1000)

### [Round to nearest 1000](https://exceljet.net/formulas/round-to-nearest-1000)

In the example, cell C6 contains this formula: =ROUND(B6,-3) The value in B6 is 1,234,567 and the result is 1,235,000. With the ROUND function, negative numbers for the second argument round to the left of the decimal and positive numbers round to the right of the decimal. In this case, by...

Related functions
-----------------

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

[![Excel ROUNDDOWN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rounddown%20function.png "Excel ROUNDDOWN function")](https://exceljet.net/functions/rounddown-function)

### [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)

The Excel ROUNDDOWN function returns a number rounded down to a given number of places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDDOWN rounds _all numbers down_....

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

*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    
*   [Round a price to end in .99](https://exceljet.net/formulas/round-a-price-to-end-in-99)
    
*   [Round to nearest 1000](https://exceljet.net/formulas/round-to-nearest-1000)
    
*   [Round number to n significant figures](https://exceljet.net/formulas/round-number-to-n-significant-figures)
    
*   [Round a number](https://exceljet.net/formulas/round-a-number)
    

### Functions

*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    

### Links

*   [Microsoft ROUND function documentation](https://support.office.com/en-us/article/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c)
    

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
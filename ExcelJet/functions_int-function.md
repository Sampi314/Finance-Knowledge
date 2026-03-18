# Excel INT function | Exceljet

**Source:** https://exceljet.net/functions/int-function

---

[Skip to main content](https://exceljet.net/functions/int-function#main-content)

[](https://exceljet.net/functions/int-function#)

*   [Previous](https://exceljet.net/functions/gcd-function)
    
*   [Next](https://exceljet.net/functions/lcm-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

INT Function
============

by Dave Bruns · Updated 13 Sep 2021

Related functions 
------------------

[TRUNC](https://exceljet.net/functions/trunc-function)

[INT](https://exceljet.net/functions/int-function)

[ROUND](https://exceljet.net/functions/round-function)

[ROUNDDOWN](https://exceljet.net/functions/rounddown-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[MROUND](https://exceljet.net/functions/mround-function)

[FLOOR](https://exceljet.net/functions/floor-function)

[CEILING](https://exceljet.net/functions/ceiling-function)

![Excel INT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")

Summary
-------

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

Purpose 
--------

Get the integer part of a number by rounding down

Return value 
-------------

The integer part of the number after rounding down

Syntax
------

    =INT(number)

*   _number_ - The number from which you want an integer.

Using the INT function 
-----------------------

The INT function returns the integer part of a decimal number by rounding down to the integer. It is important to understand that the INT function returns the integer part of a decimal number, _after rounding down_. One consequence of this behavior is that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11. To return an integer by truncating decimals, see the [TRUNC function](https://exceljet.net/functions/trunc-function)
.

The INT function takes just one argument, _number_, which should be a numeric value. INT returns a #VALUE! error if _number_ is not a numeric value. If _number_ is already a whole number, INT has no effect.

### Examples

When numbers are positive, the INT function rounds _down_ to the next lowest whole number:

    =INT(3.25) // returns 3
    =INT(3.99) // returns 3
    =INT(3.01) // returns 3
    

Notice INT rounds positive numbers down _toward zero_. With negative numbers, INT rounds down _away from zero_:

    =INT(-3.25) // returns -4
    =INT(-3.99) // returns -4
    =INT(-3.01) // returns -4
    

### INT vs. TRUNC

INT is similar to the [TRUNC function](https://exceljet.net/functions/trunc-function)
 because they both can return the integer part of a number. However, TRUNC simply truncates a number, while INT actually rounds a number down to an integer. With positive numbers, and when TRUNC is using the default of 0 for _num\_digits_,  both functions return the same results. With negative numbers, the results can be different. INT(-3.1) returns -4, because INT rounds down to the lower integer. TRUNC(-3.1) returns -3. If you simply want the integer part of a number, you should use TRUNC.

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

*   INT returns a #VALUE! error if _number_ is not a numeric value.
*   Use the INT function to get an integer from a number by rounding.
*   Use the [TRUNC function](https://exceljet.net/functions/trunc-function)
     to return an integer by truncating.

INT function examples
---------------------

[![Excel formula: Get days, hours, and minutes between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20hours%20and%20minutes%20between%20dates2.png "Excel formula: Get days, hours, and minutes between dates")](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

### [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

Most of the work in this formula is done by the TEXT function, which applies a custom number format for hours and minutes to a value created by subtracting the start date from the end date. TEXT(C5-B5,"h"" hrs ""m"" mins """) This is an example of embedding text into a custom number format, and...

[![Excel formula: Remove time from timestamp](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20time%20from%20timestamp.png "Excel formula: Remove time from timestamp")](https://exceljet.net/formulas/remove-time-from-timestamp)

### [Remove time from timestamp](https://exceljet.net/formulas/remove-time-from-timestamp)

In this example, the goal is to use a formula to remove the time value from a timestamp that includes both the date and time. To solve this problem, it's important to understand that Excel handles dates and time using a scheme in which dates are large serial numbers and times are fractional values...

[![Excel formula: Hours that overlap specific time blocks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hours_that_overlap_specific_time_blocks.png "Excel formula: Hours that overlap specific time blocks")](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

### [Hours that overlap specific time blocks](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

In this example, the goal is to calculate exactly how much of a task, shift, or event falls inside one or more defined blocks of time. The formula accepts a start and end time for the overall task or shift, as well as a start and end time for the block of interest. In the worksheet shown, the Start...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Calculate years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate_years_between_dates.png "Excel formula: Calculate years between dates")](https://exceljet.net/formulas/calculate-years-between-dates)

### [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)

In this example, the goal is to calculate the number of years between a start date in column B and an end date in column C. An easy way to solve this problem is to use the YEARFRAC function, which returns the number of years between any two dates as a decimal number. YEARFRAC function The YEARFRAC...

[![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")](https://exceljet.net/formulas/get-age-from-birthday)

### [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)

The DATEDIF function (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the...

[![Excel formula: Number is whole number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/number%20is%20whole%20number.png "Excel formula: Number is whole number")](https://exceljet.net/formulas/number-is-whole-number)

### [Number is whole number](https://exceljet.net/formulas/number-is-whole-number)

In this example, the goal is to test if a numeric value is a whole number. There are several ways to go about this. One of the easiest ways is to use the MOD function with a divisor of 1. Any whole number divided by 1 will result in a remainder of zero: =MOD(5,1)=0 // whole numbers return zero Any...

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

[![Excel formula: Number to words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/number_to_words.png "Excel formula: Number to words")](https://exceljet.net/formulas/number-to-words)

### [Number to words](https://exceljet.net/formulas/number-to-words)

In this example, the goal is to build a custom function that will convert a number like 123 into "One hundred twenty three" or "One hundred twenty three dollars" when currency is specified as USD. In addition, the formula should support multiple currencies and handle decimals. Traditionally, "...

[![Excel formula: Cash denomination calculator](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cash_denomination_calculator.png "Excel formula: Cash denomination calculator")](https://exceljet.net/formulas/cash-denomination-calculator)

### [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)

In this example, the goal is to build a "cash denomination calculator." A cash denomination calculator is a tool for counting and verifying cash amounts. It can calculate the denominations needed to achieve a certain cash value. It can also perform the reverse calculation and determine the cash...

[![Excel formula: Count unique dates ignore time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20dates%20ignore%20time.png "Excel formula: Count unique dates ignore time")](https://exceljet.net/formulas/count-unique-dates-ignore-time)

### [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)

In this example, the goal is to count the unique dates in a range of timestamps (i.e. dates that contain dates and times). In addition, we also want to create the table of results seen in E7:F9. For convenience, data is the named range B5:B16. Basic count To get a count of individual dates that...

[![Excel formula: Convert inches to feet and inches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Convert%20inches%20to%20feet%20and%20inches.png "Excel formula: Convert inches to feet and inches")](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

### [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

In this example, the goal is to create a formula that converts a numeric value in inches to a format that displays inches and feet, as seen in the table below: Input Output 9 0' 9" 12 1' 0" 30 2' 6" 75 6' 3" The math for this problem is fairly simple, but the problem is more complex because we need...

[![Excel formula: Get integer part of a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20integer%20part%20of%20a%20number.png "Excel formula: Get integer part of a number")](https://exceljet.net/formulas/get-integer-part-of-a-number)

### [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)

With TRUNC, no rounding takes place. The TRUNC function simply slices off the decimal part of the number with default settings. TRUNC actually takes an optional second argument to specify the precision of truncation, but when you don't supply this optional argument, it is assumed to be zero, and...

[![Excel formula: Round number to n significant figures](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Round_number_to_n_significant_figures.png "Excel formula: Round number to n significant figures")](https://exceljet.net/formulas/round-number-to-n-significant-figures)

### [Round number to n significant figures](https://exceljet.net/formulas/round-number-to-n-significant-figures)

In this example, the goal is to round a number to a given number of significant figures while preserving trailing zeros when needed. This is a tricky problem because Excel's rounding functions return numbers, and numbers don't preserve trailing zeros. This article uses "significant figures" and "...

INT function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20step%20through%20complex%20formulas%20using%20evaluate-thumb.png)](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)

### [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)

Excel has a handy feature called Evaluate Formula, which solves a formula one step at a time. Each time you click the Evaluate button, Excel will solve the underlined part of the formula and show you the result. Here's the same worksheet we looked at in a previous video when we talked about...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20check%20and%20debug%20a%20formula%20with%20F9.png)](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

### [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

One thing you'll frequently do in Excel is check or debug formulas. In this video, we'll look at how to use the F9 key to quickly break a formula down into pieces that you can understand. Here we have a simple list of names. In addition to names, we have a column for birthdate, a column for age,...

Related functions
-----------------

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

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

[![Excel FLOOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20floor%20function.png "Excel FLOOR function")](https://exceljet.net/functions/floor-function)

### [FLOOR Function](https://exceljet.net/functions/floor-function)

The Excel FLOOR function rounds a given number down to the nearest specified multiple. FLOOR works like the MROUND function, but FLOOR _always rounds down_.

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)
    
*   [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)
    
*   [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)
    
*   [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)
    
*   [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)
    
*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    
*   [Hours that overlap specific time blocks](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)
    
*   [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)
    
*   [Number to words](https://exceljet.net/formulas/number-to-words)
    
*   [Remove time from timestamp](https://exceljet.net/formulas/remove-time-from-timestamp)
    

### Videos

*   [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
    
*   [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)
    

### Functions

*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [ROUNDDOWN Function](https://exceljet.net/functions/rounddown-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [MROUND Function](https://exceljet.net/functions/mround-function)
    
*   [FLOOR Function](https://exceljet.net/functions/floor-function)
    
*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    

### Links

*   [Microsoft INT function documentation](https://support.office.com/en-us/article/int-function-a6c4af9e-356d-4369-ab6a-cb1fd9d343ef)
    

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
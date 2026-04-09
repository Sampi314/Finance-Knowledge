# Excel MOD function | Exceljet

**Source:** https://exceljet.net/functions/mod-function

---

[Skip to main content](https://exceljet.net/functions/mod-function#main-content)

[](https://exceljet.net/functions/mod-function#)

*   [Previous](https://exceljet.net/functions/mmult-function)
    
*   [Next](https://exceljet.net/functions/mround-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

MOD Function
============

by Dave Bruns · Updated 5 Oct 2021

Related functions 
------------------

[QUOTIENT](https://exceljet.net/functions/quotient-function)

![Excel MOD function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")

Summary
-------

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Purpose 
--------

Get the remainder from division

Return value 
-------------

The remainder

Syntax
------

    =MOD(number,divisor)

*   _number_ - The number to be divided.
*   _divisor_ - The number to divide with.

Using the MOD function 
-----------------------

The MOD function returns the remainder after division.  For example, MOD(3,2) returns 1, because 2 goes into 3 once, with a remainder of 1. 

The MOD function takes two arguments: _number_ and _divisor._ _Number_ is the number to be divided, and _divisor_ is the number used to divide. Both arguments are required. If either argument is not numeric, the MOD function returns #VALUE!.

### Equation

The result from the MOD function is calculated with an equation like this:

    =n-d*INT(n/d)
    

where n is _number_, d is _divisor_, and INT is the INT function. This can create some unexpected results because of the way that the [INT function](https://exceljet.net/functions/int-function)
 rounds negative numbers down, way from zero:

    =MOD(7,3) // returns 1
    =MOD(7,-3) // returns -2
    

MOD with negative numbers is [implemented differently](https://torstencurdt.com/tech/posts/modulo-of-negative-numbers/)
 in different languages.

### Examples

Below are some examples of the MOD function with hardcoded values:

    =MOD(12,3) // returns 0
    =MOD(12,5) // returns 2
    =MOD(100,33) // returns 1
    =MOD(6.25,1) // returns 0.25
    

### Negative numbers

The result from MOD carries the same sign as _divisor_. If _divisor_ is positive, the result from MOD is positive, if _divisor_ is negative, the result from MOD is negative:

    =MOD(-3,2) // returns 1
    =MOD(3,-2) // returns -1
    =MOD(-3,-2) // returns -1
    

### Time from datetime

The MOD function can be used to extract the time value from an [Excel date](https://exceljet.net/glossary/excel-date)
 that includes [time](https://exceljet.net/glossary/excel-time)
 (sometimes called a _datetime_). With a datetime in A1, the formula below returns the time only:

    =MOD(A1,1) // return time only
    

[Detailed explanation here](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
.

### Large numbers

With very large numbers, you may see the MOD function return a #NUM error. In that case, you can try an alternative version based on the INT function:

    =number-(INT(number/divisor)*divisor)
    

### Notes

*   MOD is often seen in formulas that deal with "every nth" value
*   MOD is useful for [extracting the time from a date](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    
*   MOD always returns a result in the same sign as the _divisor_.
*   MOD will return a #DIV/0! error if _divisor_ is zero
*   To _discard_ the remainder and keep the integer, see the [QUOTIENT function](https://exceljet.net/functions/quotient-function)
    .

MOD function examples
---------------------

[![Excel formula: Highlight integers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20integers%20only.png "Excel formula: Highlight integers only")](https://exceljet.net/formulas/highlight-integers-only)

### [Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)

The MOD function returns the remainder after division. With a divisor of 1, MOD will return zero for any whole number. We use this fact to construct a simple formula that tests the result of MOD. When the result is zero (i.e. when the number is an integer) the formula returns TRUE, triggering the...

[![Excel formula: Rank with ordinal suffix](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20with%20ordinal%20suffix.png "Excel formula: Rank with ordinal suffix")](https://exceljet.net/formulas/rank-with-ordinal-suffix)

### [Rank with ordinal suffix](https://exceljet.net/formulas/rank-with-ordinal-suffix)

Ordinal numbers represent position or rank in a sequential order. They are normally written using a number + letter suffix: 1st, 2nd, 3rd, etc. To get an ordinal suffix for a small set of numbers, you can use the CHOOSE function like this: =CHOOSE(B5,"st","nd","rd","th","th","th","th","th","th","th...

[![Excel formula: Basic timesheet formula with breaks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20timesheet%20formula%20with%20breaks.png "Excel formula: Basic timesheet formula with breaks")](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)

### [Basic timesheet formula with breaks](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)

At the core, this formula subtracts start time from end time to get duration in hours. This is done to calculate both work time and break time. MOD(C6-B6,1) // get work time MOD(E6-D6,1) // get break time Next, break time is subtracted from work time to get "net" work hours. This formula uses the...

[![Excel formula: Repeat sequence of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat_sequence_of_numbers.png "Excel formula: Repeat sequence of numbers")](https://exceljet.net/formulas/repeat-sequence-of-numbers)

### [Repeat sequence of numbers](https://exceljet.net/formulas/repeat-sequence-of-numbers)

In this example, the goal is to repeat a sequence of numbers. This is a useful way to create repeating sequences of numbers by itself. In addition, this formula is a building block to the more general formula here , which can repeat ranges and arbitrary values that are not sequential numbers...

[![Excel formula: Repeat fixed value every 3 months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat%20value%20every%20n%20months.png "Excel formula: Repeat fixed value every 3 months")](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)

### [Repeat fixed value every 3 months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)

The first thing this formula does is check the date in column B against the start date: =IF(B4>=start If the date is not greater than the start date, the formula returns zero. If the date is greater than or equal to the start date, the IF function runs this snippet: (MOD(DATEDIF(start,B4,"m")+n,...

[![Excel formula: Filter every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20every%20nth%20row.png "Excel formula: Filter every nth row")](https://exceljet.net/formulas/filter-every-nth-row)

### [Filter every nth row](https://exceljet.net/formulas/filter-every-nth-row)

The FILTER function is designed to filter and extract information based on logical criteria. In this example, the goal is to extract every 3rd record from the data shown, but there is no row number information in the data. Working from the inside out, the first step is to generate a set of row...

[![Excel formula: Add decimal minutes to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_minutes_to_time.png "Excel formula: Add decimal minutes to time")](https://exceljet.net/formulas/add-decimal-minutes-to-time)

### [Add decimal minutes to time](https://exceljet.net/formulas/add-decimal-minutes-to-time)

In this example, the goal is to add minutes in decimal format (i.e., 1, 5, 10, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.0104167 makes sense when you consider that 15 minutes is 1/96th of a day, and a day in Excel equals 1. But it...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Highlight every other row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20every%20other%20row.png "Excel formula: Highlight every other row")](https://exceljet.net/formulas/highlight-every-other-row)

### [Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)

When you use a formula to apply conditional formatting, the formula is evaluated for every cell in the selection. In this case, there are no addresses in the formula, so, for every cell in the data, the ROW and ISEVEN functions are run. ROW returns the row number of the cell, and ISEVEN returns...

[![Excel formula: Number is whole number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/number%20is%20whole%20number.png "Excel formula: Number is whole number")](https://exceljet.net/formulas/number-is-whole-number)

### [Number is whole number](https://exceljet.net/formulas/number-is-whole-number)

In this example, the goal is to test if a numeric value is a whole number. There are several ways to go about this. One of the easiest ways is to use the MOD function with a divisor of 1. Any whole number divided by 1 will result in a remainder of zero: =MOD(5,1)=0 // whole numbers return zero Any...

[![Excel formula: Max of every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_of_every_nth_column.png "Excel formula: Max of every nth column")](https://exceljet.net/formulas/max-of-every-nth-column)

### [Max of every nth column](https://exceljet.net/formulas/max-of-every-nth-column)

In this example, the goal is to calculate the maximum value of every "nth" column in a row of data, where n is a variable entered in the named range M2 . This problem can be solved in several ways, as explained below. The explanation below also includes a formula that will work in older versions of...

[![Excel formula: Sequence of leap years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_leap_years.png "Excel formula: Sequence of leap years")](https://exceljet.net/formulas/sequence-of-leap-years)

### [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)

In this example, the goal is to generate a list of leap years between a given start year and end year. The worksheet is set up so that the start year is an input in cell B5 and the end year is an input in cell B8. If either value changes, the formula should generate a new list of leap years. In the...

[![Excel formula: Repeat range of values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat_range_of_values.png "Excel formula: Repeat range of values")](https://exceljet.net/formulas/repeat-range-of-values)

### [Repeat range of values](https://exceljet.net/formulas/repeat-range-of-values)

In this example, the goal is to repeat a range of values. This can be done in various ways in Excel, but I think the CHOOSEROWS/ CHOOSECOLS functions are the easiest way to retrieve values from the range for now. Both functions work natively with two-dimensional ranges and can accept a single array...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Get most recent day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_most_recent_day_of_week.png "Excel formula: Get most recent day of week")](https://exceljet.net/formulas/get-most-recent-day-of-week)

### [Get most recent day of week](https://exceljet.net/formulas/get-most-recent-day-of-week)

In this example, the goal is to create a formula that will return the most recent day of the week, given a date and a target day of the week, abbreviated as "dow" in the generic formula. Excel tracks the day of the week internally as a specific number for each of the seven days. By default, Excel...

MOD function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

Related functions
-----------------

[![Excel QUOTIENT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20quotient%20operator.png "Excel QUOTIENT function")](https://exceljet.net/functions/quotient-function)

### [QUOTIENT Function](https://exceljet.net/functions/quotient-function)

The Excel QUOTIENT function returns the integer portion of division _without_ the remainder. Use QUOTIENT to discard the remainder after division.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get most recent day of week](https://exceljet.net/formulas/get-most-recent-day-of-week)
    
*   [Filter every nth row](https://exceljet.net/formulas/filter-every-nth-row)
    
*   [Time in hundredths of a second](https://exceljet.net/formulas/time-in-hundredths-of-a-second)
    
*   [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)
    
*   [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)
    
*   [Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)
    
*   [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)
    
*   [Repeat fixed value every 3 months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)
    
*   [Fixed value every N columns](https://exceljet.net/formulas/fixed-value-every-n-columns)
    
*   [Rank with ordinal suffix](https://exceljet.net/formulas/rank-with-ordinal-suffix)
    

### Videos

*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    

### Functions

*   [QUOTIENT Function](https://exceljet.net/functions/quotient-function)
    

### Articles

*   [How to use the MOD function to repeat values](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values)
    

### Links

*   [Microsoft MOD function documentation](https://support.office.com/en-us/article/mod-function-9b6cd169-b6ee-406a-a97b-edf2a9dc24f3)
    

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
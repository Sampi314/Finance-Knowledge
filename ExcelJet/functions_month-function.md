# Excel MONTH function | Exceljet

**Source:** https://exceljet.net/functions/month-function

---

[Skip to main content](https://exceljet.net/functions/month-function#main-content)

[](https://exceljet.net/functions/month-function#)

*   [Previous](https://exceljet.net/functions/minute-function)
    
*   [Next](https://exceljet.net/functions/networkdays-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

MONTH Function
==============

by Dave Bruns · Updated 25 Jan 2026

Related functions 
------------------

[YEAR](https://exceljet.net/functions/year-function)

[DAY](https://exceljet.net/functions/day-function)

[DATE](https://exceljet.net/functions/date-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel MONTH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")

Summary
-------

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 

Purpose 
--------

Get month as a number (1-12) from a date

Return value 
-------------

A number between 1 and 12.

Syntax
------

    =MONTH(date)

*   _date_ - A valid Excel date.

Using the MONTH function 
-------------------------

The MONTH function extracts the month from a given date as a number between 1 and 12. For example, given the date "June 12, 2021", the MONTH function returns 6 for June. MONTH takes just one argument, _serial\_number_, which must be a valid [Excel date](https://exceljet.net/glossary/excel-date)
.

The MONTH function returns a _number_. If you need a month's _name_, use the [TEXT function](https://exceljet.net/functions/text-function)
 as shown [below](https://exceljet.net/functions/month-function#get-month-name-from-date)
. The MONTH function "resets" every 12 months (like a calendar or clock). To work with month durations larger than 12, use a formula to [calculate months between dates](https://exceljet.net/formulas/get-months-between-dates)
.

### Key features

*   Returns month as integer 1-12 (1=January, 12=December)
*   Works with dates as text or Excel serial numbers
*   Often combined with YEAR, DAY, and DATE for date manipulation
*   Returns a number, not a month name

### Table of contents

*   [Basic usage](https://exceljet.net/functions/month-function#basic-usage)
    
*   [Get month from date](https://exceljet.net/functions/month-function#get-month-from-date)
    
*   [Get month name from date](https://exceljet.net/functions/month-function#get-month-name-from-date)
    
*   [Get quarter from date](https://exceljet.net/functions/month-function#get-quarter-from-date)
    
*   [Get last day of month](https://exceljet.net/functions/month-function#get-last-day-of-month)
    
*   [Sum by month ignore year](https://exceljet.net/functions/month-function#sum-by-month-ignore-year)
    
*   [Count birthdays by month](https://exceljet.net/functions/month-function#count-birthdays-by-month)
    
*   [Filter by month](https://exceljet.net/functions/month-function#filter-by-month)
    
*   [Related functions](https://exceljet.net/functions/month-function#related-functions)
    
*   [Notes](https://exceljet.net/functions/month-function#notes)
    

### Basic usage

MONTH takes just one argument, which must be a valid date or a text value that Excel can convert into a date. With the date March 15, 2026 in cell A1, all of these formulas will return 3:

    =MONTH(A1) // returns 3
    =MONTH("15-Mar-2026") // returns 3
    =MONTH(DATE(2026,3,15)) // returns 3

Dates can be supplied to the MONTH function as text (e.g., "13-Aug-2021") or as native Excel dates, which are [large serial numbers](https://exceljet.net/glossary/excel-date)
. To create a date value from scratch with separate year, month, and day inputs, use the [DATE function](https://exceljet.net/functions/date-function)
.

### Get month from date

In the worksheet below, the goal is to extract the month number from dates. The formula in C5 is:

    =MONTH(B5)
    

![MONTH function example - get month from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/month_get_month_from_date.png "MONTH function example - get month from date")

The MONTH function takes just one argument, the date from which to extract the month. In this example, with the date April 15, 1912 in cell B5, MONTH returns 4 for April. As the formula is copied down, it returns the month for each date in column B.

> You can use MONTH to extract the month from a date entered as text (e.g., `=MONTH("1/5/2016")`), but using text for dates can produce unpredictable results on computers using different regional date settings. It's better to supply a cell reference that contains a valid date.

For more details, see [Get month from date](https://exceljet.net/formulas/get-month-from-date)
.

### Get month name from date

One thing that confuses new users to Excel is how to get the month name with the MONTH function. Short answer: you can't. The MONTH function returns a number, not a month name. You could use a more complicated formula to perform a lookup, but there is no need. The simplest way to get a month name from a date is to use the TEXT function. In the worksheet below, the goal is to extract the full month name from dates in column B. The formula in C5 is:

    =TEXT(B5,"mmmm")
    

![MONTH function example - get month name from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/month_get_month_name.png "MONTH function example - get month name from date")

The TEXT function converts values to text using the number format you provide. The format "mmmm" returns the full month name (e.g., "January"), while "mmm" returns an abbreviated name (e.g., "Jan"). Note that the date is lost in the conversion — only the text for the month name remains.

> Tip: If you only need to _display_ a month name without converting to text, apply a [custom number format](https://exceljet.net/articles/custom-number-formats)
>  directly to the cell containing the date.

For more details, see [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
.

### Get quarter from date

The MONTH function can be combined with the [ROUNDUP function](https://exceljet.net/functions/roundup-function)
 to calculate the quarter (1, 2, 3, or 4) for any date. In the worksheet below, the goal is to return the quarter number for dates in column B. The formula in C5 is:

    =ROUNDUP(MONTH(B5)/3,0)
    

![MONTH function example - get quarter from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/month_get_quarter.png "MONTH function example - get quarter from date")

This formula works by dividing the month number by 3, then rounding up to the nearest integer. For example, January is month 1, and 1/3 = 0.33, which rounds up to 1 (Q1). June is month 6, and 6/3 = 2, which is already a whole number (Q2). To include "Q" in the result, [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 it to the formula:

    ="Q"&ROUNDUP(MONTH(B5)/3,0)

For more details, see [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)
.

### Get last day of month

The easiest way to get the last day of a month is with the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
. However, you can also use MONTH with [DATE](https://exceljet.net/functions/date-function)
 to achieve the same result. In the worksheet below, the goal is to return the last day of the month for dates in column B. The formula in C5 is:

    =DATE(YEAR(B5),MONTH(B5)+1,0)
    

![MONTH function example - get last day of month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/month_last_day.png "MONTH function example - get last day of month")

This formula works by using the DATE function with day set to zero. When you supply 0 as the day argument, DATE "rolls back" one day to the last day of the previous month. So, by adding 1 to the month and using 0 for day, DATE returns the last day of the original month.

> Note: the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
>  provides a more direct way to solve this problem: `=EOMONTH(B5,0)`, but I include the DATE formula above because it shows that using a day value of 0 can be used to get the last day of the previous month.

For more details, see [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)
.

### Sum by month ignore year

The MONTH function is useful for summarizing data by month while ignoring year values. In the worksheet below, the goal is to sum amounts by month across multiple years. The formula in F5 is:

    =SUMPRODUCT((MONTH($B$5:$B$16)=MONTH(E5&1))*$C$5:$C$16)
    

![MONTH function example - sum by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/month_sum_by_month.png "MONTH function example - sum by month")

This formula uses the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 with MONTH to test each date against a target month number. The expression `MONTH(E5&1)` is a tricky way to convert the month name in E5 (e.g., "Jan") to a month number by concatenating "1" to create a text string like "Jan1", which Excel interprets as a date. See more details [here](https://exceljet.net/formulas/month-number-from-name)
.

When MONTH extracts the month from each date in the range and compares it to the target month, the result is an array of TRUE/FALSE values. Multiplying by the amounts converts TRUE to 1 and FALSE to 0, effectively summing only amounts where the month matches. This is an example using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in an array formula to cancel out the amounts for months that don't match.

For more details, see [Sum by month ignore year](https://exceljet.net/formulas/sum-by-month-ignore-year)
.

> Note: In Excel 2021 and later, you can use the [SUM function](https://exceljet.net/functions/sum-function)
>  instead of the SUMPRODUCT function. However, SUMPRODUCT is a good solution because it works in all versions of Excel. For more information, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)

### Count birthdays by month

The MONTH function can also be used to count dates by month. This is handy for counting birthdays by month. In the worksheet below, the goal is to count how many birthdays fall in each month shown in column E. The formula in F5 is:

    =SUMPRODUCT(--(MONTH($C$5:$C$16)=MONTH(E5&1)))
    

![MONTH function example - count birthdays by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/month_count_birthdays.png "MONTH function example - count birthdays by month")

Like the sum-by-month example above, this formula uses [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in an array formula to cancel out the counts for months that don't match. It also uses the same trick to convert the month name in E5 (e.g., "Jan") to a month number before comparing it to the target month. MONTH extracts the month number from each birthday, and the result is compared to the target month. The result is an array of TRUE/FALSE values. The [double negative](https://exceljet.net/glossary/double-unary)
 (--) converts the TRUE/FALSE values to 1s and 0s, and SUMPRODUCT sums the result to give a count.

> Note: [COUNTIF](https://exceljet.net/functions/countif-function)
>  won't work for this problem because it only accepts ranges, not arrays from expressions like `=MONTH(range)`.

For more details, see [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)
.

### Filter by month

You can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with MONTH to extract rows that match a specific month. In the worksheet below, the goal is to filter the data to show only rows from July (month 7 in cell H2). The formula in F5 is:

    =FILTER(B5:D15,MONTH(C5:C15)=H2,"No data")
    

![MONTH function example - filter by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/month_filter_by_month.png "MONTH function example - filter by month")

Here, `MONTH(C5:C15)=H2` creates an array of TRUE/FALSE values: TRUE for dates in July, FALSE for all others. The FILTER function uses this array to filter the data range, and only rows where the result is TRUE appear in the output. The _if\_empty_ argument is set to "No data" in case no matching data is found.

To filter by both month and year, use Boolean logic:

    =FILTER(B5:D15,(MONTH(C5:C15)=H2)*(YEAR(C5:C15)=2024),"No data")

For more details, see [Filter by date](https://exceljet.net/formulas/filter-by-date)
.

### Notes

*   MONTH returns #VALUE! if the date is not recognized.
*   MONTH returns #NUM! if a date is out of range (e.g., -1).
*   Text dates can cause problems. Use cell references to valid dates when possible.

MONTH function examples
-----------------------

[![Excel formula: Get fiscal quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20quarter%20from%20date.png "Excel formula: Get fiscal quarter from date")](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

### [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

The choose function uses the first argument to "select" remaining elements. For example, in a scheme where 1 = small, 2 = medium, and 3 = large, this formula will "map" the number 2 to "medium". =CHOOSE(2,"small","medium","large") In the case of fiscal quarters, we can use this same idea to map any...

[![Excel formula: FILTER with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20complex%20multiple%20criteria.png "Excel formula: FILTER with complex multiple criteria")](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

### [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

In this example, we need to construct logic that filters data to include: account begins with "x" AND region is "east", and month is NOT April. The filtering logic of this formula (the include argument) is created by chaining together three expressions that use boolean logic on arrays in the data...

[![Excel formula: Month number from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/month%20number%20from%20name.png "Excel formula: Month number from name")](https://exceljet.net/formulas/month-number-from-name)

### [Month number from name](https://exceljet.net/formulas/month-number-from-name)

In this example, the goal is to return a number, 1-12, for any month name of the year. For example, given the string "January" we want to return 1, "February" should return 2, and so on. If we had a valid Excel date , we could use a number format for this task, but because we are starting with a...

[![Excel formula: Happy birthday message](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/happy%20birthday%20message.png "Excel formula: Happy birthday message")](https://exceljet.net/formulas/happy-birthday-message)

### [Happy birthday message](https://exceljet.net/formulas/happy-birthday-message)

In this example, the goal is to display a Happy Birthday message when a birthday in a given cell matches the current date. The core of the problem is to compare the given birthday to the current date while ignoring the year. There are two main ways to approach the problem. The first way is to use...

[![Excel formula: GROUPBY with monthly totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/groupby_with_monthly_totals.png "Excel formula: GROUPBY with monthly totals")](https://exceljet.net/formulas/groupby-with-monthly-totals)

### [GROUPBY with monthly totals](https://exceljet.net/formulas/groupby-with-monthly-totals)

In this example, the goal is to generate monthly totals using the GROUPBY function. This is a tricky problem in Excel because typically, source data contains a regular date field and not a separate field with month names. In addition, the GROUPBY function will, by default, sort everything in...

[![Excel formula: Sum by month ignore year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20month%20ignore%20year.png "Excel formula: Sum by month ignore year")](https://exceljet.net/formulas/sum-by-month-ignore-year)

### [Sum by month ignore year](https://exceljet.net/formulas/sum-by-month-ignore-year)

In this example, the goal is to sum numeric values by month while ignoring the year that contains the date. The solution below is based on the SUMPRODUCT function, the MONTH function, and Boolean algebra . For convenience, amount (C5:C16) and date (B5:B16) are named ranges . Basic concept The basic...

[![Excel formula: Year is a leap year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/year_is_leap_year.png "Excel formula: Year is a leap year")](https://exceljet.net/formulas/year-is-a-leap-year)

### [Year is a leap year](https://exceljet.net/formulas/year-is-a-leap-year)

In this example, the goal is to write a formula that will return TRUE if a year is a leap year and FALSE if not. This is a surprisingly challenging problem in Excel for two reasons: (1) Excel thinks 1900 is a leap year due to a long-standing bug inherited from Lotus 1-2-3 and (2) The logic for...

[![Excel formula: Date is same month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_same_month_and_year.png "Excel formula: Date is same month and year")](https://exceljet.net/formulas/date-is-same-month-and-year)

### [Date is same month and year](https://exceljet.net/formulas/date-is-same-month-and-year)

In this example, the goal is to mark dates in column D with an "x" when they have the same year and month as the date in cell B5. We don't care at all about the day. At a high level, we can easily use the IF function to return "x" for qualifying dates, so the challenge is in creating a logical test...

[![Excel formula: XLOOKUP with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20with%20complex%20multiple%20criteria.png "Excel formula: XLOOKUP with complex multiple criteria")](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)

### [XLOOKUP with complex multiple criteria](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)

Normally, the XLOOKUP function is configured to look for a value in a lookup array that exists on the worksheet. However, when the criteria used to match a value becomes more complex, you can use Boolean logic to create a lookup array on the fly composed only of 1s and 0s, then look for the value 1...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

[![Excel formula: Get month from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_month_from_date.png "Excel formula: Get month from date")](https://exceljet.net/formulas/get-month-from-date)

### [Get month from date](https://exceljet.net/formulas/get-month-from-date)

The MONTH function takes just one argument, the date from which to extract the month. In the example shown, the formula is: =MONTH(B4) where B4 contains the date January 5, 2016. The MONTH function returns the number 1 representing the month( January) of the date. Note that you can use MONTH to...

[![Excel formula: Filter by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_by_date.png "Excel formula: Filter by date")](https://exceljet.net/formulas/filter-by-date)

### [Filter by date](https://exceljet.net/formulas/filter-by-date)

This example shows how to filter dates using Excel's FILTER function. Several common date-based filtering patterns are shown below, including filtering by month, filtering by a specific date, and filtering by month and year. Filter by month In the worksheet below, the goal is to filter the data to...

[![Excel formula: Get nth day of week in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get-nth-day-of-week-in-month_0.png "Excel formula: Get nth day of week in month")](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

### [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

This example demonstrates how to calculate the nth occurrence of a specific day of the week within a month. For instance, you might need to find the 2nd Tuesday, the 4th Wednesday, or the 1st Friday of any given month. The worksheet is structured with the starting date in column B, the target day...

[![Excel formula: Date is same month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Date%20is%20same%20month.png "Excel formula: Date is same month")](https://exceljet.net/formulas/date-is-same-month)

### [Date is same month](https://exceljet.net/formulas/date-is-same-month)

In this case, Excel extracts the month from the date in cell B6 as a number, and the month in the cell C6 as a number, then tests for equivalency using the equal sign. Both dates are in January, so the formula is solved as follows and returns TRUE. =MONTH(B6)=MONTH(C6) =1=1 =TRUE Same month as...

[![Excel formula: Get fiscal year from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20year%20from%20date.png "Excel formula: Get fiscal year from date")](https://exceljet.net/formulas/get-fiscal-year-from-date)

### [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)

In this example, the goal is to return the fiscal year for any given date, where a fiscal year starts in July as seen in the worksheet. By convention a fiscal year is denoted by the year in which it ends. So, if a fiscal year begins in July, then the date August 1, 2018 is in fiscal year 2019. The...

MONTH function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20with%20boolean%20logic-Play.png)](https://exceljet.net/videos/filter-with-boolean-logic)

### [FILTER with boolean logic](https://exceljet.net/videos/filter-with-boolean-logic)

In this video we'll look how to use the FILTER function with Boolean logic to apply multiple criteria. In this worksheet we have some sample order data in a table called "data". Let's use the FILTER function to find all "blue" orders in June. To visualize how this works I'm going to set up the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Examples%20of%20flagged%20errors%20in%20formulas-thumb.png)](https://exceljet.net/videos/examples-of-flagged-errors-in-formulas)

### [Examples of flagged errors in formulas](https://exceljet.net/videos/examples-of-flagged-errors-in-formulas)

In this video, we'll look at a few examples of the kind of errors that Excel will flag on a worksheet and the rules that control these errors. First, to recap, the rules that govern the errors that Excel flags are located at options > formulas > error checking rules Each rule can be disabled...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20date%20and%20time%20series%20with%20formulas-thumb.png)](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

### [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

Although you can use Excel's AutoFill feature to fill in a series of dates and times, you can also do the same thing with formulas. The advantage of using a formula is that you can easily change the starting value and generate a new series. Let's take a look. Often you'll need to generate a series...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20years%20and%20months%20between%20dates-thumb.png)](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)

### [How to calculate years and months between dates](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)

In this video we'll look at how to calculate the number of years or months between dates using a function called DATEDIF and a function called YEARFRAC . The DATEDIF function is a "compatibility" function that comes from Lotus 1-2-3. For reasons that are unknown, it's only documented in Excel 2000...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20work%20with%20dates-thumb.png)](https://exceljet.net/videos/how-to-work-with-dates)

### [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)

Excel contains special functions that will let you extract the day, month, and year from a valid date. Let's take a look. Here we have a set of random dates in column B. First, I'll add a formula to column C to pick up the date values in B and format them with the General format, so we can see the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20CHOOSE%20function-Thumb.png)](https://exceljet.net/videos/how-to-use-the-choose-function)

### [How to use the CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)

In this video we'll look at how you can use the CHOOSE function . Let's look at three examples. In this first example we have some items listed with a numeric color code. We want to bring these names into column D. Now, since I already have a table here, I could just use VLOOKUP and reference the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

Related functions
-----------------

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get month from date](https://exceljet.net/formulas/get-month-from-date)
    
*   [GROUPBY with monthly totals](https://exceljet.net/formulas/groupby-with-monthly-totals)
    
*   [Filter by date](https://exceljet.net/formulas/filter-by-date)
    
*   [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)
    
*   [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)
    
*   [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)
    
*   [Happy birthday message](https://exceljet.net/formulas/happy-birthday-message)
    
*   [Add years to date](https://exceljet.net/formulas/add-years-to-date)
    
*   [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    
*   [Sum by quarter](https://exceljet.net/formulas/sum-by-quarter)
    

### Videos

*   [How to calculate years and months between dates](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)
    
*   [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)
    
*   [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)
    
*   [Examples of flagged errors in formulas](https://exceljet.net/videos/examples-of-flagged-errors-in-formulas)
    
*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to use the CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)
    
*   [FILTER with boolean logic](https://exceljet.net/videos/filter-with-boolean-logic)
    

### Functions

*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [DAY Function](https://exceljet.net/functions/day-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

### Links

*   [Microsoft MONTH function documentation](https://support.office.com/en-us/article/month-function-579a2881-199b-48b2-ab90-ddba0eba86e8)
    

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
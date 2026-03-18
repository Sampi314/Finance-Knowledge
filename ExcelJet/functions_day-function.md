# Excel DAY function | Exceljet

**Source:** https://exceljet.net/functions/day-function

---

[Skip to main content](https://exceljet.net/functions/day-function#main-content)

[](https://exceljet.net/functions/day-function#)

*   [Previous](https://exceljet.net/functions/datevalue-function)
    
*   [Next](https://exceljet.net/functions/days-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

DAY Function
============

by Dave Bruns · Updated 24 Jan 2026

Related functions 
------------------

[YEAR](https://exceljet.net/functions/year-function)

[MONTH](https://exceljet.net/functions/month-function)

[DATE](https://exceljet.net/functions/date-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel DAY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_day_function.png "Excel DAY function")

Summary
-------

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and with the [DATE function](https://exceljet.net/functions/date-function)
 to reassemble dates after making changes.

Purpose 
--------

Get the day of month from a date

Return value 
-------------

The day of month as a number between 1-31

Syntax
------

    =DAY(date)

*   _date_ - A valid Excel date.

Using the DAY function 
-----------------------

The DAY function extracts the day component from any valid Excel date. For example, DAY returns 15 from the date January 15, 2024. This is useful when you need to work with the day of a date separately, for calculations, comparisons, or building new dates.

The DAY function returns a _number_. If you need a day's _name_, use the [TEXT function](https://exceljet.net/functions/text-function)
 as shown [below](https://exceljet.net/functions/day-function#get-day-name-from-date)
.

> Note: The [DAYS function](https://exceljet.net/functions/days-function)
>  has a similar name but serves a different purpose: it calculates the number of days between two dates.

### Key features

*   Returns a number between 1 and 31
*   Works with any valid Excel date
*   Often combined with YEAR, MONTH, and DATE for date manipulation
*   Returns a number, not text
*   Can extract day from dates entered as text (but this is not recommended)

### Table of contents

*   [Basic usage](https://exceljet.net/functions/day-function#basic-usage)
    
*   [Get day from date](https://exceljet.net/functions/day-function#get-day-from-date)
    
*   [Get first day of month](https://exceljet.net/functions/day-function#get-first-day-of-month)
    
*   [Days in month](https://exceljet.net/functions/day-function#days-in-month)
    
*   [Get day name from date](https://exceljet.net/functions/day-function#get-day-name-from-date)
    
*   [Add years to date](https://exceljet.net/functions/day-function#add-years-to-date)
    
*   [Notes](https://exceljet.net/functions/day-function#notes)
    

### Basic usage

The DAY function requires just one argument, a [valid Excel date](https://exceljet.net/glossary/excel-date)
. When given a valid date, it returns the day of the month:

    =DAY("15-Jan-2024") // returns 15
    =DAY(TODAY()) // returns today's day number
    =DAY(A1) // returns day from date in A1
    =DAY("7-Aug-2025") // returns 7
    =DAY("31-Dec-2024") // returns 31
    

> Using text strings for dates (like "1/15/2024") can cause problems due to regional date format differences. A better approach is to create the date with the DATE function or to refer to a cell that already contains a valid date.

A common pattern is to use DAY together with YEAR, MONTH, and DATE to modify dates. For example, to change only the year of a date while keeping the month and day the same, you can "take apart" the date with YEAR, MONTH, and DAY, then reassemble it with DATE:

    =DATE(2025,MONTH(A1),DAY(A1))
    

This returns a new date with the year 2025, but the original month and day from A1.

### Get day from date

In the worksheet below, the goal is to extract the day number from dates in column B. The formula in C5 is:

    =DAY(B5)
    

![DAY function example - get day from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/day_example_get_day_from_date.png "DAY function example - get day from date")

The DAY function takes just one argument: the date from which you want to extract the day. In this example, B5 contains the date January 5, 2016, so DAY returns 5.

> You can use DAY to extract the day from a date entered as text (e.g., `=DAY("1/5/2016")`), but this can produce unpredictable results on computers using different regional date settings. It's better to reference a cell containing a valid date value.

For more details, see [Get day from date](https://exceljet.net/formulas/get-day-from-date)
.

### Get first day of month

Before the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 was introduced, the DAY function was the standard way to get the first day of a month. In the worksheet below, the goal is to find the first day of the month for each date in column B. The formula in C5 is:

    =B5-DAY(B5)+1
    

![DAY function example - get first day in month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/day_example_first_day_of_month.png "DAY function example - get first day in month")

This formula works in three steps:

1.  Get the day number from the date with `DAY(B5)`
2.  Subtract the day from the date (rewinding to day 0, which is the last day of the previous month)
3.  Add 1 to land on the first day of the current month

For example, with the date January 12, 2025 in B5:

    =B5-DAY(B5)+1
    ="12-Jan-2025"-12+1
    ="31-Dec-2024"+1
    ="1-Jan-2025"
    

> Note: The formula `=EOMONTH(B5,-1)+1` provides a more intuitive way to get the first day of a month. See [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
>  for details on both approaches.

### Days in month

Since the last day of any month equals the total number of days in that month, you can combine DAY with EOMONTH to count days in a month. In the worksheet below, the goal is to get the total number of days in the month for each date in column B. The formula in C5 is:

    =DAY(EOMONTH(B5,0))
    

![DAY function example - days in month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/day_example_days_in_month.png "DAY function example - days in month")

Working from the inside out:

1.  EOMONTH returns the last day of the month (with 0 as the second argument, it stays in the same month)
2.  DAY extracts the day number from that end-of-month date

For January 12, 2024:

    =DAY(EOMONTH("12-Jan-2024",0))
    =DAY("31-Jan-2024")
    =31
    

This correctly handles months with different lengths, including February in leap years (returning 29) and non-leap years (returning 28).

For more details, see [Days in month](https://exceljet.net/formulas/days-in-month)
.

### Get day name from date

The DAY function returns a number (1-31), not a day name. To get the day name (like "Monday" or "Tuesday") from a date, use the [TEXT function](https://exceljet.net/functions/text-function)
 with a day name format code. In the worksheet below, the goal is to return the full day name for each date in column B. The formula in C5 is:

    =TEXT(B5,"dddd")
    

![DAY function example - get day name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/day_example_get_day_name.png "DAY function example - get day name")

The TEXT function formats a value using a custom format code. The format code "dddd" returns the full day name. You can also use:

    =TEXT(B5,"ddd")  // abbreviated day name (Mon, Tue, Wed...)
    =TEXT(B5,"dddd") // full day name (Monday, Tuesday, Wednesday...)
    

> Tip: If you only need to _display_ a day name without converting to text, apply a [custom number format](https://exceljet.net/articles/custom-number-formats)
>  like "dddd" directly to the cell containing the date.

### Add years to date

The DAY function is essential when you need to add years to a date while preserving the month and day. In the worksheet below, the goal is to add the number of years in column C to each date in column B. The formula in D5 is:

    =DATE(YEAR(B5)+C5,MONTH(B5),DAY(B5))
    

![DAY function example - add years to date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/day_example_add_years_to_date.png "DAY function example - add years to date")

This formula works by taking apart the date and reassembling it:

1.  YEAR, MONTH, and DAY extract the individual components
2.  The years value (C5) is added to the year
3.  DATE reassembles everything into a new date

For the date March 8, 1960, with 10 years to add:

    =DATE(YEAR(B5)+C5,MONTH(B5),DAY(B5))
    =DATE(1960+10,3,8)
    =DATE(1970,3,8)
    

> Note: The [EDATE function](https://exceljet.net/functions/edate-function)
>  provides a simpler way to add years: `=EDATE(B5,C5*12)`. EDATE also handles leap year edge cases better when the start date is February 29.

For more details, see [Add years to date](https://exceljet.net/formulas/add-years-to-date)
.

### Notes

*   The DAY function returns a #VALUE! error if the date argument is not a valid Excel date.
*   If the result displays as a date (like 1/1/1900) instead of a number, the cell is formatted as a date. Change the format to General or Number.
*   When dates are entered as text, regional date format differences can cause DAY to misinterpret the day and month. For example, "5/6/2024" means May 6 in the US but June 5 in many other countries.
*   Dates before January 1, 1900, are not supported in Excel's standard date system.

DAY function examples
---------------------

[![Excel formula: List all dates in a month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_all_dates_in_a_month.png "Excel formula: List all dates in a month")](https://exceljet.net/formulas/list-all-dates-in-a-month)

### [List all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month)

In this example, we'll use SEQUENCE to generate all dates in a given month. Creating a complete list of dates for a specific month is a common Excel task with many practical applications, from building project timelines and work schedules to generating calendar views and tracking daily data. The...

[![Excel formula: Semimonthly pay schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/semimonthly_pay_schedule.png "Excel formula: Semimonthly pay schedule")](https://exceljet.net/formulas/semimonthly-pay-schedule)

### [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)

In this example, the goal is to create a list of pay dates that follow a semimonthly schedule. A semimonthly pay schedule means employees are paid twice a month, usually on fixed dates such as the 1st and 15th or the 15th and the last day of the month. This results in 24 pay periods over the course...

[![Excel formula: Add years to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_years_to_date.png "Excel formula: Add years to date")](https://exceljet.net/formulas/add-years-to-date)

### [Add years to date](https://exceljet.net/formulas/add-years-to-date)

Ever needed to calculate someone's retirement date? Or figure out when a 30-year mortgage will end? Or maybe you're setting a contract expiration date? In each case, you need a way to add years to a date. Here's something that might surprise you: most Excel users tackle this problem with a formula...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Get day from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_day_from_date.png "Excel formula: Get day from date")](https://exceljet.net/formulas/get-day-from-date)

### [Get day from date](https://exceljet.net/formulas/get-day-from-date)

The DAY function takes just one argument, the date from which you want to extract the day. In the example, the formula is: =DAY(B5) B5 contains a date value for January 5, 2016. The DAY function returns the number 5 representing the day component of the date. Note that you can use DAY to extract...

[![Excel formula: Days in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/days%20in%20month.png "Excel formula: Days in month")](https://exceljet.net/formulas/days-in-month)

### [Days in month](https://exceljet.net/formulas/days-in-month)

In this example, the goal is to get the total number of days in a month based on any date in the month. This problem can be solved by combining the DAY function with the EOMONTH function. The EOMONTH function The EOMONTH function returns the last day of the month, a given number of months in the...

[![Excel formula: Happy birthday message](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/happy%20birthday%20message.png "Excel formula: Happy birthday message")](https://exceljet.net/formulas/happy-birthday-message)

### [Happy birthday message](https://exceljet.net/formulas/happy-birthday-message)

In this example, the goal is to display a Happy Birthday message when a birthday in a given cell matches the current date. The core of the problem is to compare the given birthday to the current date while ignoring the year. There are two main ways to approach the problem. The first way is to use...

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

DAY function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20work%20with%20dates-thumb.png)](https://exceljet.net/videos/how-to-work-with-dates)

### [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)

Excel contains special functions that will let you extract the day, month, and year from a valid date. Let's take a look. Here we have a set of random dates in column B. First, I'll add a formula to column C to pick up the date values in B and format them with the General format, so we can see the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20date%20and%20time%20series%20with%20formulas-thumb.png)](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

### [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

Although you can use Excel's AutoFill feature to fill in a series of dates and times, you can also do the same thing with formulas. The advantage of using a formula is that you can easily change the starting value and generate a new series. Let's take a look. Often you'll need to generate a series...

Related functions
-----------------

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

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

*   [Get day from date](https://exceljet.net/formulas/get-day-from-date)
    
*   [List all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month)
    
*   [Days in month](https://exceljet.net/formulas/days-in-month)
    
*   [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)
    
*   [Happy birthday message](https://exceljet.net/formulas/happy-birthday-message)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [Add years to date](https://exceljet.net/formulas/add-years-to-date)
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    

### Videos

*   [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)
    
*   [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)
    

### Functions

*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

### Links

*   [Microsoft DAY function documentation](https://support.office.com/en-us/article/day-function-8a7d1cbb-6c7d-4ba1-8aea-25c134d03101)
    

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
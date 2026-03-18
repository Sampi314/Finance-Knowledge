# Excel EOMONTH function | Exceljet

**Source:** https://exceljet.net/functions/eomonth-function

---

[Skip to main content](https://exceljet.net/functions/eomonth-function#main-content)

[](https://exceljet.net/functions/eomonth-function#)

*   [Previous](https://exceljet.net/functions/edate-function)
    
*   [Next](https://exceljet.net/functions/hour-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

EOMONTH Function
================

by Dave Bruns · Updated 19 Jun 2024

Related functions 
------------------

[EDATE](https://exceljet.net/functions/edate-function)

![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")

Summary
-------

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number to move back in time.

Purpose 
--------

Get last day of month n months in future or past

Return value 
-------------

Last day of month date

Syntax
------

    =EOMONTH(start_date,months)

*   _start\_date_ - A date that represents the start date in a valid Excel serial number format.
*   _months_ - The number of months before or after start\_date.

Using the EOMONTH function 
---------------------------

The EOMONTH function returns the last day of the month, a given number of months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that must land on the last day of a month. EOMONTH returns a [serial number corresponding to an Excel date](https://exceljet.net/glossary/excel-date)
. To display the result as a date, apply a [number format of your choice](https://exceljet.net/articles/custom-number-formats)
.

The EOMONTH function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _start\_date_ and _months_:

*   _start\_date_ - a valid [Excel date](https://exceljet.net/glossary/excel-date)
     to use as the starting point. The day of the month does not matter. EOMONTH will return the last day of the month regardless.
*   _months_ - a whole number that specifies how many months to move. Use a positive number of months to get a date in the future and a negative number for a date in the past.

_Note: The EOMONTH function returns the last day of the month. If you want the same day of the month, use the [EDATE function](https://exceljet.net/functions/edate-function)
._

### The EOMONTH function explained

With a given start date, EOMONTH returns a new date by adding the number of months provided and returning the last day of the resulting month. To illustrate how this works, assume we want to create dates for the last day of each quarter, starting from January 1, 2024. We can do this with the following formulas:

    =EOMONTH("1-Jan-2024",2) // returns 31-Mar-2024
    =EOMONTH("1-Jan-2024",5) // returns 30-Jun-2024
    =EOMONTH("1-Jan-2024",8) // returns 30-Sep-2024
    =EOMONTH("1-Jan-2024",11) // returns 31-Dec-2024

The first formula adds 2 months, the second adds 5 months, the third adds 8 months, and the fourth adds 11 months to the date. Although the start date is the 1st of the month, EOMONTH returns the last day of the month in all cases after adding months. Of course, hardcoding a date into a formula doesn't make much sense in Excel. A better option is to use a cell reference. If we enter the date January 1, 2024, in cell A1, the same formulas look like this:

    =EOMONTH(A1,2) // returns 31-Mar-2024
    =EOMONTH(A1,5) // returns 30-Jun-2024
    =EOMONTH(A1,8) // returns 30-Sep-2024
    =EOMONTH(A1,11) // returns 31-Dec-2024

The results are the same. And if the date in A1 is changed, EOMONTH will generate new dates. You can use negative numbers for months to create dates _before_ the start date. With the same date in A1 (1-Jan-2024), the formulas below return end-of-quarter dates for the _previous_ year:

    =EOMONTH(A1,-1) // returns 31-Dec-2023
    =EOMONTH(A1,-4) // returns 30-Sep-2023
    =EOMONTH(A1,-7) // returns 30-Jun-2023
    =EOMONTH(A1,-10) // returns 31-Mar-2023

### Example - Basic usage

With the date May 12, 2017, in cell B5, the formulas below will return the dates as noted:

    =EOMONTH(B5,0) // returns May 31, 2017
    =EOMONTH(B5,4) // returns Sep 30, 2017
    =EOMONTH(B5,-3) // returns Feb 28, 2017
    

Notice that although the start date is the 12th of May, the result from EOMONTH is always the last day of the month.

### Example - Move by years

To use the EOMONTH function to move by years, multiply the months by 12. For example, to move a date forward 2 years, you can use either of these formulas:

    =EOMONTH(A1,24) // forward 2 years
    =EOMONTH(A1,2*12) // forward 2 years
    

The second form is handy when you already have a value for years in another cell.

### Example  - Last day of the current month

To get the last day of the current month, combine the [TODAY function](https://exceljet.net/functions/today-function)
 with EOMONTH like this:

    =EOMONTH(TODAY(),0) // last day of current month
    

The TODAY function returns the current date to the EOMONTH function, and the value for months is given as zero. The result is that EOMONTH will return the last day of the current month. Because the TODAY function will continue to recalculate over time, this formula will always return the correct result.

### Example - First day of the current month

Although the EOMONTH function returns the _last_ day of a month, you can easily adjust the formula above to return the _first_ day of the current month like this:

    =EOMONTH(TODAY(),-1)+1 // first day of current month
    

The formula works like this:

1.  The TODAY function returns the current date to EOMONTH.
2.  EOMONTH moves back to the last day of the previous month.
3.  Adding 1 returns the first day of the current month.

See the links below for more examples of how to use the EOMONTH function in formulas.

### Example - Sum by month

The EOMONTH function will often turn up in formulas that perform month-based calculations. For example, in the worksheet below, the goal is to sum amounts by month and by client. The formula in G5 is:

    =SUMIFS(amount,client,$F5,date,">="&G$4,date,"<="&EOMONTH(G$4,0))

![EOMONTH example - Sum values by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/eomonth_example_sum_by_month_in_columns.png "EOMONTH example - Sum values by month")

In this example, the values in G4:I4 are actually first-of-month dates, formatted to display only an abbreviated month name. The [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 is configured to use EOMONTH to create "brackets" for each month that are used to sum the amounts in column D by month and by client. For a full explanation of how this formula works, [see this page](https://exceljet.net/formulas/sum-by-month-in-columns)
.

### Example - Sequence of months

In Excel 2021 and later, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 with EOMONTH to create a list of end-of-month dates. In the worksheet below, the start date is in cell B5. The formula in D5 looks like this:

    =EOMONTH(B5,SEQUENCE(12))

![EOMONTH example - Sequence of months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/eomonth_example_sequence_of_months.png "EOMONTH example - Sequence of months")

The SEQUENCE function returns an array of 12 numbers like {1;2;3;4;5;6;7;8;9;10;11;12} directly to the EOMONTH function:

    =EOMONTH(B5,{1;2;3;4;5;6;7;8;9;10;11;12})

EOMONTH then generates 12 end-of-month dates starting with the month after 15 June 2025. If the date in cell B5 is changed, a new list of dates will be generated. For a more detailed explanation of this idea, see [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
.

### Notes

*   For _months_, use a positive number for future dates and a negative number for past dates.
*   EOMONTH will return the  #VALUE error if the start date is not a valid date.
*   If the start date has a [fractional time](https://exceljet.net/glossary/excel-time)
     attached, it will be removed.
*   If the _months_ argument contains a decimal value, it will be removed.
*   To move any date _n_ months into the future or past, see the [EDATE function](https://exceljet.net/functions/edate-function)
    .
*   EOMONTH returns a [date serial number](https://exceljet.net/glossary/excel-date)
    , which must be [formatted as a date](https://exceljet.net/articles/custom-number-formats)
    .

EOMONTH function examples
-------------------------

[![Excel formula: Get last weekday in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20weekday%20in%20month.png "Excel formula: Get last weekday in month")](https://exceljet.net/formulas/get-last-weekday-in-month)

### [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)

First, this formula determines the first day of the next month \*after\* a given date. It does this my using EOMONTH to get the last day of the month, then adding one day: =EOMONTH(B5,0)+1 Next, the formula calculates the number of days required to "roll back" to the last requested weekday in the...

[![Excel formula: List nth weekdays of the month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_nth_weekdays_of_the_month.png "Excel formula: List nth weekdays of the month")](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

### [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

In this example, the goal is to generate a list of "nth weekdays of the month" with a formula. For example, the formula should be able to create a list of any of the following: 2nd Tuesdays of the month 1st Fridays of the month 3rd Mondays of the month This is a somewhat challenging problem in...

[![Excel formula: List all dates in a month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_all_dates_in_a_month.png "Excel formula: List all dates in a month")](https://exceljet.net/formulas/list-all-dates-in-a-month)

### [List all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month)

In this example, we'll use SEQUENCE to generate all dates in a given month. Creating a complete list of dates for a specific month is a common Excel task with many practical applications, from building project timelines and work schedules to generating calendar views and tracking daily data. The...

[![Excel formula: Sum by month in columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month_in_columns.png "Excel formula: Sum by month in columns")](https://exceljet.net/formulas/sum-by-month-in-columns)

### [Sum by month in columns](https://exceljet.net/formulas/sum-by-month-in-columns)

In this example, the goal is to construct a formula that will subtotal the amounts in column D by client and month as seen in the range G5:I8. A big part of the problem is to set up the proper references so that the formula can be entered once, and copied throughout G5:I8. The solution explained...

[![Excel formula: Add months to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_months_to_date.png "Excel formula: Add months to date")](https://exceljet.net/formulas/add-months-to-date)

### [Add months to date](https://exceljet.net/formulas/add-months-to-date)

In this example, the goal is to add a given number of months to a date. If the number of months is positive, the date should move forward. If the number of months is negative, the date should move backward. The standard solution for this problem in Excel is to use the EDATE function although in...

[![Excel formula: Days in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/days%20in%20month.png "Excel formula: Days in month")](https://exceljet.net/formulas/days-in-month)

### [Days in month](https://exceljet.net/formulas/days-in-month)

In this example, the goal is to get the total number of days in a month based on any date in the month. This problem can be solved by combining the DAY function with the EOMONTH function. The EOMONTH function The EOMONTH function returns the last day of the month, a given number of months in the...

[![Excel formula: Generate quarter dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/generate_quarter_dates.png "Excel formula: Generate quarter dates")](https://exceljet.net/formulas/generate-quarter-dates)

### [Generate quarter dates](https://exceljet.net/formulas/generate-quarter-dates)

In this example, the goal is to generate a list of quarter start and quarter end dates. This can be done by combining the SEQUENCE function with the EDATE and EOMONTH functions, as explained below. The SEQUENCE function The SEQUENCE function generates a list of sequential numbers in an array. For...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")](https://exceljet.net/formulas/get-last-day-of-month)

### [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below. The EOMONTH function The EOMONTH function returns the last day of the...

[![Excel formula: Last n months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20n%20months.png "Excel formula: Last n months")](https://exceljet.net/formulas/last-n-months)

### [Last n months](https://exceljet.net/formulas/last-n-months)

In this example, the goal is to create a formula that will return TRUE if a date is in the last complete 6 month period, starting in the previous month. This means the date must fall between a calculated start date and end date, which requires two logical tests. The formula uses the AND function to...

[![Excel formula: Count dates in current month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20dates%20in%20current%20month.png "Excel formula: Count dates in current month")](https://exceljet.net/formulas/count-dates-in-current-month)

### [Count dates in current month](https://exceljet.net/formulas/count-dates-in-current-month)

At the core, this formula uses the COUNTIFS function to count dates that are greater than or equal to the first day of the current month, and less than the first day of the next month. The EOMONTH function is used to create both dates based on the current date, which is supplied by the TODAY...

[![Excel formula: Get first day of previous month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20first%20day%20of%20previous%20month.png "Excel formula: Get first day of previous month")](https://exceljet.net/formulas/get-first-day-of-previous-month)

### [Get first day of previous month](https://exceljet.net/formulas/get-first-day-of-previous-month)

The EOMONTH function returns the last day of a month based on a given date. The 2nd argument is months , which specifies how many months in the future or past to move before returning the last day. By traveling back 2 months, then adding one day, we can calculate the first day of the previous month...

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Get nth day of week in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get-nth-day-of-week-in-month_0.png "Excel formula: Get nth day of week in month")](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

### [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

This example demonstrates how to calculate the nth occurrence of a specific day of the week within a month. For instance, you might need to find the 2nd Tuesday, the 4th Wednesday, or the 1st Friday of any given month. The worksheet is structured with the starting date in column B, the target day...

[![Excel formula: New customers per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/new%20customers%20per%20month.png "Excel formula: New customers per month")](https://exceljet.net/formulas/new-customers-per-month)

### [New customers per month](https://exceljet.net/formulas/new-customers-per-month)

This formula relies on a helper column, which is column E in the example shown. The formula in E5, copied down, is: =(COUNTIFS($B$5:B5,B5)=1)+0 This formula returns a 1 for new customers and a 0 for repeat customers, and is explained in detail here . Once this formula is in place, the COUNTIFS...

EOMONTH function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/SEQUENCE%20of%20dates-Play.png)](https://exceljet.net/videos/sequence-of-dates)

### [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)

In this video, we'll look at how to generate a sequence of dates with the SEQUENCE function . The SEQUENCE function can be used to generate numeric sequences of all kinds. Since Excel dates are just numbers, SEQUENCE works well for generating dates. In this first worksheet, we have a couple cells...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20expiration%20dates.png)](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)

### [How to calculate and highlight expiration dates](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)

In this video we'll look at how to calculate and highlight expiration dates. Let's say your company has started a membership program of some kind and your boss just sent you a set of data. She's given you a list of 1,000 people that have renewed a membership in the last year or so, and she's...

Related functions
-----------------

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)
    
*   [Last n months](https://exceljet.net/formulas/last-n-months)
    
*   [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
    
*   [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)
    
*   [New customers per month](https://exceljet.net/formulas/new-customers-per-month)
    
*   [Calculate expiration date](https://exceljet.net/formulas/calculate-expiration-date)
    
*   [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)
    
*   [List all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month)
    
*   [Get first day of previous month](https://exceljet.net/formulas/get-first-day-of-previous-month)
    
*   [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)
    

### Videos

*   [How to calculate and highlight expiration dates](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)
    
*   [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)
    

### Functions

*   [EDATE Function](https://exceljet.net/functions/edate-function)
    

### Links

*   [Microsoft EOMONTH function documentation](https://support.office.com/en-us/article/eomonth-function-7314ffa1-2bc9-4005-9d66-f49db127d628)
    

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
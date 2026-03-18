# Excel EDATE function | Exceljet

**Source:** https://exceljet.net/functions/edate-function

---

[Skip to main content](https://exceljet.net/functions/edate-function#main-content)

[](https://exceljet.net/functions/edate-function#)

*   [Previous](https://exceljet.net/functions/days360-function)
    
*   [Next](https://exceljet.net/functions/eomonth-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

EDATE Function
==============

by Dave Bruns · Updated 5 Mar 2026

Related functions 
------------------

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[WORKDAY](https://exceljet.net/functions/workday-function)

[DATEDIF](https://exceljet.net/functions/datedif-function)

![Excel EDATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")

Summary
-------

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

Purpose 
--------

Get date n months in future or past

Return value 
-------------

New date as Excel serial number

Syntax
------

    =EDATE(start_date,months)

*   _start\_date_ - Start date as a valid Excel date.
*   _months_ - Number of months before or after start\_date.

Using the EDATE function 
-------------------------

The EDATE function returns a date on the same day of the month, n months before or after a start date. You can use EDATE to generate expiration dates, contract dates, due dates, anniversary dates, retirement dates, and other dates that derive from a start date. EDATE returns a [serial number corresponding to a date](https://exceljet.net/glossary/excel-date)
. To display the result as a date, apply a [number format of your choice](https://exceljet.net/articles/custom-number-formats)
.

The EDATE function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _start\_date_ and _months_:

*   _start\_date_ - a valid [Excel date](https://exceljet.net/glossary/excel-date)
     to use as the starting point.
*   _months_ - a whole number that specifies how many months to move. Use a positive number of months to get a date in the future and a negative number for a date in the past.

_Note: The EDATE function returns the same day of the month. If you want to get the last day of a month, use the_ [_EOMONTH function_](https://exceljet.net/functions/eomonth-function)
_._

### The EDATE function explained

With a given start date, EDATE returns a new date by adding the number of months provided. To illustrate how EDATE works, assume we want to create dates for the first day of each quarter, starting from January 1, 2024. We can do this with the following formulas:

    =EDATE("1-Jan-2024",0) // returns 1-Jan-2024
    =EDATE("1-Jan-2024",3) // returns 1-Apr-2024
    =EDATE("1-Jan-2024",6) // returns 1-Jul-2024
    =EDATE("1-Jan-2024",9) // returns 1-Oct-2024

The first formula does not change the date since _months_ is zero. The second formula adds 3 months, the third formula adds 6 months, and the fourth formula adds 9 months to the date. In all cases, EDATE returns the 1st of the month since the start date is also the 1st. Of course, in most real-life scenarios, you will not hardcode dates into formulas like this. You will instead use cell references. If we enter the date January 1, 2024, in cell A1, the same formulas look like this:

    =EDATE(A1,0) // returns 1-Jan-2024
    =EDATE(A1,3) // returns 1-Apr-2024
    =EDATE(A1,6) // returns 1-Jul-2024
    =EDATE(A1,9) // returns 1-Oct-2024

The results are the same. And if the date in A1 is changed, EDATE will generate new dates. You can use negative numbers for months to create dates before the start date. With the same date in A1, the formulas below return dates that are 3, 6, 9, and 12 months before January 1, 2024:

    =EDATE(A1,-3) // returns 1-Oct-2023
    =EDATE(A1,-6) // returns 1-Jul-2023
    =EDATE(A1,-9) // returns 1-Apr-2023
    =EDATE(A1,-12) // returns 1-Jan-2023

### Example - Basic usage

If A1 contains the date February 1, 2018, you can use EDATE like this:

    =EDATE(A1,1) // returns March 1, 2018
    =EDATE(A1,3) // returns May 1, 2018
    =EDATE(A1,-1) // returns January 1, 2018
    =EDATE(A1,-2) // returns December 1, 2017
    

### Example - 6 months from today

To use EDATE with today's date, you can combine it with the [TODAY function](https://exceljet.net/functions/today-function)
. For example, to create a date exactly 6 months from today, you can use:

    =EDATE(TODAY(),6) // 6 months from today
    

### Example - Move by years

To use the EDATE function to move by years, multiply by 12. For example, to move a date forward 2 years, you can use either of these formulas:

    =EDATE(A1,24) // forward 2 years
    =EDATE(A1,2*12) // forward 2 years
    

The second form is handy when you already have a value for years in another cell and want to convert it to months inside EDATE.

### Example - Sum by month

The EDATE function can be combined with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 to create a formula to sum values by month. This approach is seen in the worksheet below, where EDATE appears in the last argument. The idea is to sum amounts that fall between the first day of the month and the last day of the month. The formula in cell F5 is:

    =SUMIFS(amount,date,">="&E5,date,"<"&EDATE(E5,1))

![EDATE example - sum amounts in a given month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/edate_example_sum_by_month.png "EDATE example - sum amounts in a given month")

As the formula is copied down it creates a subtotal for each month listed in column E. You can use this same approach to count by month with COUNTIFS and average by month with AVERAGEIFS. For a detailed explanation and to download the workbook, [see this page](https://exceljet.net/formulas/sum-by-month)
.

### Example - Sequence of months

In Excel 2021 and later, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 with EDATE to generate a list of sequential months. In the worksheet below, the start date is in cell B5. The formula in D5 creates a list of the next 12 months, including the start date:

![EDATE example - sequence of 12 months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/edate_example_sequence_of_months.png "EDATE example - sequence of 12 months")

If the date in cell B5 is changed, a new list of dates will be generated. For a more detailed explanation, see [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
.

### Example - EDATE with time

The EDATE function will strip times from dates that include time (sometimes called a "datetime"). This happens because EDATE only works with whole numbers. To preserve the time in a date, you can use a formula like this:

    =EDATE(A1,n)+MOD(A1,1)
    

Here, the MOD function is used to [extract the time from the date](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
 in A1, which is then added back to the result from EDATE.

### End-of-month dates

EDATE is clever about "end of month" dates when the day is 31. Starting with January 31, 2019, notice that EDATE will keep the last day of the month:

    =EDATE("31-Jan-2019",1) // returns 28-Feb-2019
    =EDATE("31-Jan-2019",2) // returns 31-Mar-2019
    =EDATE("31-Jan-2019",3) // returns 30-Apr-2019
    =EDATE("31-Jan-2019",4) // returns 31-May-2019
    =EDATE("31-Jan-2019",5) // returns 30-Jun-2019
    

EDATE will also respect leap years:

    =EDATE("31-Jan-2020",1) // returns 29-Feb-2020
    

However, EDATE will not maintain an end-of-month day when the day is less than 31. For example:

    =EDATE("28-Feb-2019",1) // returns 28-Mar-2019
    

If you need an end-of-month date, switch to the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
.

> Because EDATE properly handles end-of-month boundaries, it can be useful for calculating the duration of time between two dates. See [How to replace Excel's DATEDIF function](https://exceljet.net/articles/how-to-replace-excels-datedif-function)
>  for an example.

### Notes

*   EDATE will return the #VALUE error if the start date is not a valid date.
*   If the start date has a [fractional time](https://exceljet.net/glossary/excel-time)
     attached, it will be removed.
*   If the _months_ argument contains a decimal value, it will be removed.
*   To return an end-of-month date, see the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
    .
*   EDATE returns a [date serial number](https://exceljet.net/glossary/excel-date)
    , which must be [formatted as a date](https://exceljet.net/articles/custom-number-formats)
    .

EDATE function examples
-----------------------

[![Excel formula: Add days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_days_to_date.png "Excel formula: Add days to date")](https://exceljet.net/formulas/add-days-to-date)

### [Add days to date](https://exceljet.net/formulas/add-days-to-date)

In this example, the goal is to add days to a date. This is a frequent task in Excel when you need to calculate a new date by adding a specified number of days to an existing date. Here are some examples of situations where this might be useful: Calculate a due date by adding a given number of days...

[![Excel formula: Next anniversary date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20anniversary%20date.png "Excel formula: Next anniversary date")](https://exceljet.net/formulas/next-anniversary-date)

### [Next anniversary date](https://exceljet.net/formulas/next-anniversary-date)

Working from the inside out, we use the DATEDIF function to calculate how many complete years are between the original anniversary date and the "as of" date, where the as of date is any date after the anniversary date: DATEDIF(B5,C5,"y") Note: in this case, we are arbitrarily fixing the "as of"...

[![Excel formula: Add months to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_months_to_date.png "Excel formula: Add months to date")](https://exceljet.net/formulas/add-months-to-date)

### [Add months to date](https://exceljet.net/formulas/add-months-to-date)

In this example, the goal is to add a given number of months to a date. If the number of months is positive, the date should move forward. If the number of months is negative, the date should move backward. The standard solution for this problem in Excel is to use the EDATE function although in...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Get same date next year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20same%20date%20next%20year.png "Excel formula: Get same date next year")](https://exceljet.net/formulas/get-same-date-next-year)

### [Get same date next year](https://exceljet.net/formulas/get-same-date-next-year)

EDATE can get the "same date" in the future or past, based on the number of months supplied. When 12 is given for months, EDATE gets the same date next year. Same date in previous year To get the same date in a previous month, use -12: =EDATE(date,-12) // prior year

[![Excel formula: Get same date next month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20same%20date%20next%20month.png "Excel formula: Get same date next month")](https://exceljet.net/formulas/get-same-date-next-month)

### [Get same date next month](https://exceljet.net/formulas/get-same-date-next-month)

The EDATE function returns a date on the same day of the month, n months in the past or future. You can use EDATE to calculate expiration dates, maturity dates, and other due dates. When 1 is given for months , EDATE returns the same date in the next month. Notice that EDATE automatically handles...

[![Excel formula: List nth weekdays of the month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_nth_weekdays_of_the_month.png "Excel formula: List nth weekdays of the month")](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

### [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

In this example, the goal is to generate a list of "nth weekdays of the month" with a formula. For example, the formula should be able to create a list of any of the following: 2nd Tuesdays of the month 1st Fridays of the month 3rd Mondays of the month This is a somewhat challenging problem in...

[![Excel formula: Calculate expiration date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20expiration%20date.png "Excel formula: Calculate expiration date")](https://exceljet.net/formulas/calculate-expiration-date)

### [Calculate expiration date](https://exceljet.net/formulas/calculate-expiration-date)

In Excel, dates are simply serial numbers. In the standard date system for windows, based on the year 1900, where January 1, 1900 is the number 1. This means that January 1, 2050 is the serial number 54,789. If you are calculating a date n days in the future, you can add days directly as in the...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Get stock price last n months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20months.png "Excel formula: Get stock price last n months")](https://exceljet.net/formulas/get-stock-price-last-n-months)

### [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)

In this example, the goal is to get monthly closing stock price over the past n months (i.e. last 6 months, last 12 months, last 24 months, etc.) for the list of symbols that appear in column B. In addition, we want a rolling time period, that stays in sync with the current date. This can be done...

[![Excel formula: Average by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_month.png "Excel formula: Average by month")](https://exceljet.net/formulas/average-by-month)

### [Average by month](https://exceljet.net/formulas/average-by-month)

In this example, the goal is to calculate a monthly average for the amounts shown in column C using the dates in column B. The article below explains two approaches. One approach is based on the AVERAGEIFS function , which is designed to calculate averages using multiple criteria. The second...

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Average call time per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_call_time_per_month.png "Excel formula: Average call time per month")](https://exceljet.net/formulas/average-call-time-per-month)

### [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)

In this example, the goal is to calculate the average call time (duration in minutes) for each month listed in column G using the dates in column B and the durations in column E. The article below explains two approaches. The first formula is based on the AVERAGEIFS function , which is designed to...

[![Excel formula: Add years to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_years_to_date.png "Excel formula: Add years to date")](https://exceljet.net/formulas/add-years-to-date)

### [Add years to date](https://exceljet.net/formulas/add-years-to-date)

Ever needed to calculate someone's retirement date? Or figure out when a 30-year mortgage will end? Or maybe you're setting a contract expiration date? In each case, you need a way to add years to a date. Here's something that might surprise you: most Excel users tackle this problem with a formula...

[![Excel formula: Calculate retirement date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20retirement%20date.png "Excel formula: Calculate retirement date")](https://exceljet.net/formulas/calculate-retirement-date)

### [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)

In this example, the goal is to calculate a retirement date at age 60, based on a given birthdate. The simplest way to do this is with the EDATE function. The EDATE function will return a date n months in the future or past when given a date and the number of months to traverse. In this case, we...

EDATE function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20function%20arguments-thumb.png)](https://exceljet.net/videos/how-to-use-function-arguments)

### [How to use function arguments](https://exceljet.net/videos/how-to-use-function-arguments)

You've probably noticed that functions use parentheses, and inside those parentheses are certain inputs. These inputs have a special name: arguments. Let's look at some examples. Arguments can be required or optional. Some functions take three or more arguments, and some functions don't take any...

Related functions
-----------------

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get same date next month](https://exceljet.net/formulas/get-same-date-next-month)
    
*   [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)
    
*   [Average by month](https://exceljet.net/formulas/average-by-month)
    
*   [Add days to date](https://exceljet.net/formulas/add-days-to-date)
    
*   [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
    
*   [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)
    
*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    
*   [Generate quarter dates](https://exceljet.net/formulas/generate-quarter-dates)
    
*   [Add months to date](https://exceljet.net/formulas/add-months-to-date)
    
*   [Add years to date](https://exceljet.net/formulas/add-years-to-date)
    

### Videos

*   [How to use function arguments](https://exceljet.net/videos/how-to-use-function-arguments)
    

### Functions

*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    
*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    

### Articles

*   [How to replace Excel's DATEDIF function](https://exceljet.net/articles/how-to-replace-excels-datedif-function)
    

### Links

*   [Microsoft EDATE function documentation](https://support.office.com/en-us/article/edate-function-3c920eb2-6e66-44e7-a1f5-753ae47ee4f5)
    

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
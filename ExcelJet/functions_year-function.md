# Excel YEAR function | Exceljet

**Source:** https://exceljet.net/functions/year-function

---

[Skip to main content](https://exceljet.net/functions/year-function#main-content)

[](https://exceljet.net/functions/year-function#)

*   [Previous](https://exceljet.net/functions/workday.intl-function)
    
*   [Next](https://exceljet.net/functions/yearfrac-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

YEAR Function
=============

by Dave Bruns · Updated 19 Jan 2026

Related functions 
------------------

[MONTH](https://exceljet.net/functions/month-function)

[DAY](https://exceljet.net/functions/day-function)

[DATE](https://exceljet.net/functions/date-function)

[EDATE](https://exceljet.net/functions/edate-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel YEAR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")

Summary
-------

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

Purpose 
--------

Get the year from a date

Return value 
-------------

Year as 4-digit number

Syntax
------

    =YEAR(date)

*   _date_ - A valid Excel date.

Using the YEAR function 
------------------------

The YEAR function returns the year of a date as a 4-digit number. YEAR takes just one argument, _date_, which must be a valid date. Date can be a cell containing a date, a date string, or a formula that returns a date. Internally, Excel converts dates to serial numbers following its own date system. For example, given the date "23-Aug-2012", YEAR will return 2021:

    =YEAR("23-Aug-2012") // returns 2012

> Note: [dates are serial numbers](https://exceljet.net/glossary/excel-date)
>  in Excel, and begin on January 1, 1900. Dates before 1900 are not supported.

### Key features

*   Returns year as 4-digit number (e.g., 2024, not 24)
*   Works with any valid Excel date
*   Often combined with DATE, MONTH, DAY for date manipulation
*   Returns a number, not a text value
*   Can accept dates as text strings, cell references, or formulas

### Table of contents

*   [Basic examples](https://exceljet.net/functions/year-function#basic-examples)
    
*   [Get year from date](https://exceljet.net/functions/year-function#get-year-from-date)
    
*   [Add years to date](https://exceljet.net/functions/year-function#add-years-to-date)
    
*   [Get fiscal year from date](https://exceljet.net/functions/year-function#get-fiscal-year-from-date)
    
*   [Count dates in given year](https://exceljet.net/functions/year-function#count-dates-in-given-year)
    
*   [Sum by year](https://exceljet.net/functions/year-function#sum-by-year)
    
*   [Year is a leap year](https://exceljet.net/functions/year-function#year-is-a-leap-year)
    
*   [Notes](https://exceljet.net/functions/year-function#notes)
    

### Basic examples

The YEAR function requires just one argument, which must be a valid date or a value that Excel can convert into a valid date. With the date January 20, 2026, in cell A1, the following formula will return 2026:

    =YEAR(A1) // returns 2026

Note that you can use YEAR to extract the year from a date entered as text:

    =YEAR("1/20/2026") // returns 2026
    

However, using text for dates can cause unpredictable results on computers using different regional date settings. In general, it's better to supply a reference to a cell that already contains a valid date. 

You can easily combine the YEAR function with other Excel functions. For example, to get the current year, you can use YEAR with the [TODAY function](https://exceljet.net/functions/today-function)
 like this:

    =YEAR(TODAY()) // returns current year

Using the [DATE function](https://exceljet.net/functions/date-function)
, you can extract a year from cell A1 and use it to create the date January 1 in the same year, like this:

    =DATE(YEAR(A1),1,1) // first day of same year
    

If A1 contains January 20, 2026, the result will be January 1, 2026.

### Get year from date

Use the DATE function to extract just the year from a date. In the worksheet below, the formula in D5 is:

    =YEAR(B5)
    

![YEAR example - get year from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/year_example_get_year_from_date.png "YEAR example - get year from date")

The YEAR function takes just one argument, the date from which you want to extract the year. With a date value for 15-Apr-1912 in B5, the YEAR function returns the number 1912. For more details, see [Get year from date](https://exceljet.net/formulas/get-year-from-date)
.

### Add years to date

In this example, the goal is to add a given number of years to a date. The formula in E5 is:

    =DATE(YEAR(B5)+C5,MONTH(B5),DAY(B5))
    

![YEAR example - add years to date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/year_example_add_years_to_date.png "YEAR example - add years to date")

This formula uses the DATE function together with the YEAR, MONTH, and DAY functions. Working from the inside out, YEAR, MONTH, and DAY "take apart" the date into separate components. The DATE function then reassembles the date, adding the number in C5 to the year value along the way. With the date 8-Mar-1960 in B5, and the number 10 in C5, the result is 8-Mar-1970.

Another approach is to use the [EDATE function](https://exceljet.net/functions/edate-function)
. For more details, see [Add years to date](https://exceljet.net/formulas/add-years-to-date)
.

### Get fiscal year from date

The YEAR function only returns a normal year number, not a fiscal year. However, you can get YEAR to return a fiscal year by combining it with the MONTH function. You can see this approach below, where the fiscal year starts in July. The formula in D5 is:

    =YEAR(B5)+(MONTH(B5)>=7)
    

![YEAR example - get fiscal year](https://exceljet.net/sites/default/files/images/functions/inline/year_example_get_fiscal_year.png "YEAR example - get fiscal year")

By convention, a fiscal year is denoted by the year in which it ends. So if a fiscal year begins in July, then July 1, 2026 is in fiscal year 2027, while June 1, 2026 is in fiscal year 2026. The YEAR function first extracts the year from the date. Then, a [boolean expression](https://exceljet.net/glossary/boolean-logic)
 is added to adjust for the fiscal year:

    +(MONTH(B5)>=7) // returns 0 or 1
    

If the month is greater than or equal to 7 (July), the expression returns TRUE, which Excel evaluates as 1. This increments the year by one. If the month is less than 7, the expression returns FALSE (zero), and the year remains unchanged. 

For more details, see [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)
.

### Count dates in given year

In this example, the goal is to count how many dates fall in a given year. The formula in E5 is:

    =SUMPRODUCT(--(YEAR(dates)=D5))
    

![YEAR example - count dates in a given year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/year_example_count_dates_in_year.png "YEAR example - count dates in a given year")

The YEAR function extracts the year from each date in the [named range](https://exceljet.net/glossary/named-range)
 **dates** (B5:B16). Because B5:B16 contains 12 cells, YEAR returns an [array](https://exceljet.net/glossary/array)
 of 12 year values. This array is compared to the year in D5, creating a new array of TRUE and FALSE values.

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) converts the TRUE/FALSE values to 1s and 0s. Finally, [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 sums the array, returning a count of dates that match the year.

This pattern of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 in array operations is powerful and flexible, and is also used with functions like [FILTER](https://exceljet.net/functions/filter-function)
 and [XLOOKUP](https://exceljet.net/functions/xlookup-function)
.

For more details, see [Count dates in given year](https://exceljet.net/formulas/count-dates-in-given-year)
.

### Sum by year

In this example, the goal is to calculate a total for each year. All data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named "data". The formula in G5 is:

    =SUMPRODUCT((YEAR(data[Date])=F5)*data[Amount])
    

![YEAR example - sum by year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/year_example_sum_by_year.png "YEAR example - sum by year")

Working from the inside out, the YEAR function extracts year values from the dates in the **data** table. These year values are compared to the year in F5, creating an array of TRUE and FALSE values. This array is multiplied by the amounts, which converts TRUE/FALSE to 1/0 and effectively "cancels out" amounts from other years. SUMPRODUCT then sums the resulting array to return the total for the year.

For more details, see [Sum by year](https://exceljet.net/formulas/sum-by-year)
.

### Year is a leap year

Excel doesn't have a function to test for a leap year. However, you can roll your own by combining several functions together. In the worksheet below, the goal is to test whether the year of a date is a leap year for all dates in column B. The formula in D5 is:

    =MONTH(DATE(YEAR(B5),2,29))=2
    

![YEAR example - year is leap year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/year_example_leap_year.png "YEAR example - year is leap year")

This formula exploits a behavior of the DATE function. When you request February 29 in a non-leap year, DATE automatically rolls forward to March 1. The YEAR function extracts the year from the date, and DATE constructs a date for February 29 of that year. Then the MONTH function is used to test the month number of the resulting date. If the month is 2 (February), it's a leap year (TRUE). If the month is 3 (March), it's not a leap year (FALSE).

> Note: Excel incorrectly treats 1900 as a leap year due to a legacy bug from Lotus 1-2-3. To guard against this, you can add an AND condition: `=AND(MONTH(DATE(YEAR(B5),2,29))=2,YEAR(B5)<>1900)`

For more details, see [Year is a leap year](https://exceljet.net/formulas/year-is-a-leap-year)
.

### Notes

*   YEAR returns a #VALUE! error if the date argument is not a valid date.
*   Dates before January 1, 1900 are not supported in Excel's date system.
*   The result is a number, not text. To display just the year from a date, you can apply a [custom number format](https://exceljet.net/articles/custom-number-formats)
     like "yyyy".
*   YEAR can accept dates entered as text strings (e.g., "1/5/2016"), but this can cause issues with different regional date settings.
*   Excel incorrectly treats 1900 as a leap year due to a legacy bug inherited from Lotus 1-2-3.

YEAR function examples
----------------------

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Zodiac sign lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/zodiac%20sign%20lookup_0.png "Excel formula: Zodiac sign lookup")](https://exceljet.net/formulas/zodiac-sign-lookup)

### [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)

The goal of this example is to look up the correct astrological or zodiac sign for a given birthdate, using the table shown in B5:F15. These are based on the Western zodiac signs described here . Zodiac signs are used in horoscopes, which are a kind of forecast of a person's future, based on the...

[![Excel formula: Count birthdays by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20birthdays%20by%20year_0.png "Excel formula: Count birthdays by year")](https://exceljet.net/formulas/count-birthdays-by-year)

### [Count birthdays by year](https://exceljet.net/formulas/count-birthdays-by-year)

In this example, the goal is to count birthdays by year. The source data is an Excel Table named data in the range C5:C16. The birthdays we want to count are in the Birthday column. In column E, the years of interest have been previously entered. The easiest way to solve this problem is with the...

[![Excel formula: Data validation allow weekday only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20weekday%20only.png "Excel formula: Data validation allow weekday only")](https://exceljet.net/formulas/data-validation-allow-weekday-only)

### [Data validation allow weekday only](https://exceljet.net/formulas/data-validation-allow-weekday-only)

Data validation rules are triggered when a user adds or changes a cell value. This custom validation formula uses the WEEKDAY function to get a numeric value, 1-7, corresponding to a week beginning Monday (1) and ending Sunday (7). To get a number for a Monday-based week, the return\_type argument...

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

[![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")](https://exceljet.net/formulas/get-last-day-of-month)

### [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below. The EOMONTH function The EOMONTH function returns the last day of the...

[![Excel formula: Sum by fiscal year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20fiscal%20year.png "Excel formula: Sum by fiscal year")](https://exceljet.net/formulas/sum-by-fiscal-year)

### [Sum by fiscal year](https://exceljet.net/formulas/sum-by-fiscal-year)

The goal of this example is to sum amounts by fiscal year, when the fiscal year begins in July. The first approach is a self-contained formula based on the SUMPRODUCT function. The second method uses SUMIF with column D as a helper column. Either approach will work correctly, and the best option...

[![Excel formula: Date is same month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_same_month_and_year.png "Excel formula: Date is same month and year")](https://exceljet.net/formulas/date-is-same-month-and-year)

### [Date is same month and year](https://exceljet.net/formulas/date-is-same-month-and-year)

In this example, the goal is to mark dates in column D with an "x" when they have the same year and month as the date in cell B5. We don't care at all about the day. At a high level, we can easily use the IF function to return "x" for qualifying dates, so the challenge is in creating a logical test...

[![Excel formula: Get year from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_year_from_date.png "Excel formula: Get year from date")](https://exceljet.net/formulas/get-year-from-date)

### [Get year from date](https://exceljet.net/formulas/get-year-from-date)

In this example, the goal is to extract the year number from a list of dates in column B. This can be easily achieved with the YEAR function . The YEAR function takes just one argument, the date from which you want to extract the year. For example, in the formula below, we pass the "12-Dec-1999"...

[![Excel formula: Filter by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_by_date.png "Excel formula: Filter by date")](https://exceljet.net/formulas/filter-by-date)

### [Filter by date](https://exceljet.net/formulas/filter-by-date)

This example shows how to filter dates using Excel's FILTER function. Several common date-based filtering patterns are shown below, including filtering by month, filtering by a specific date, and filtering by month and year. Filter by month In the worksheet below, the goal is to filter the data to...

[![Excel formula: Data validation date in specific year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20date%20in%20specific%20year.png "Excel formula: Data validation date in specific year")](https://exceljet.net/formulas/data-validation-date-in-specific-year)

### [Data validation date in specific year](https://exceljet.net/formulas/data-validation-date-in-specific-year)

Data validation rules are triggered when a user adds or changes a cell value. This custom validation formula simply checks the year of any date against a hard-coded year value using the YEAR function. When a user enters a value, the YEAR function extracts and compares the year to 2016: =YEAR(C5)=...

[![Excel formula: Get nth day of year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20nth%20day%20of%20year.png "Excel formula: Get nth day of year")](https://exceljet.net/formulas/get-nth-day-of-year)

### [Get nth day of year](https://exceljet.net/formulas/get-nth-day-of-year)

This formula takes advantage of the fact that dates are just sequential numbers in Excel. It determines the last day of the previous year and subtracts that value from the original date with this formula: =B5-DATE(YEAR(B5),1,0) The result is nth day of the year, based on the date in cell B5. Notice...

[![Excel formula: Count dates in given year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20dates%20in%20given%20year.png "Excel formula: Count dates in given year")](https://exceljet.net/formulas/count-dates-in-given-year)

### [Count dates in given year](https://exceljet.net/formulas/count-dates-in-given-year)

The YEAR function extracts the year from a valid Excel date . For example: =YEAR("15-Jun-2021") // returns 2021 In this case, we are giving YEAR and array of dates in the named range dates : YEAR(dates) Because dates contains 11 cells, we get back 11 results in an array like this: {2018;2017;2019;...

[![Excel formula: Get months between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_months_between_dates.png "Excel formula: Get months between dates")](https://exceljet.net/formulas/get-months-between-dates)

### [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)

In this example, the goal is to calculate the number of months between two valid Excel dates . This is a curiously tricky problem in Excel because the number of days in a month varies, and the rules about how a whole month might be calculated are not obvious. In addition, there is not a modern...

[![Excel formula: Get fiscal year from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20year%20from%20date.png "Excel formula: Get fiscal year from date")](https://exceljet.net/formulas/get-fiscal-year-from-date)

### [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)

In this example, the goal is to return the fiscal year for any given date, where a fiscal year starts in July as seen in the worksheet. By convention a fiscal year is denoted by the year in which it ends. So, if a fiscal year begins in July, then the date August 1, 2018 is in fiscal year 2019. The...

YEAR function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20date%20and%20time%20series%20with%20formulas-thumb.png)](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

### [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

Although you can use Excel's AutoFill feature to fill in a series of dates and times, you can also do the same thing with formulas. The advantage of using a formula is that you can easily change the starting value and generate a new series. Let's take a look. Often you'll need to generate a series...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20years%20and%20months%20between%20dates-thumb.png)](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)

### [How to calculate years and months between dates](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)

In this video we'll look at how to calculate the number of years or months between dates using a function called DATEDIF and a function called YEARFRAC . The DATEDIF function is a "compatibility" function that comes from Lotus 1-2-3. For reasons that are unknown, it's only documented in Excel 2000...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20work%20with%20dates-thumb.png)](https://exceljet.net/videos/how-to-work-with-dates)

### [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)

Excel contains special functions that will let you extract the day, month, and year from a valid date. Let's take a look. Here we have a set of random dates in column B. First, I'll add a formula to column C to pick up the date values in B and format them with the General format, so we can see the...

Related functions
-----------------

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

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

*   [Get year from date](https://exceljet.net/formulas/get-year-from-date)
    
*   [Filter by date](https://exceljet.net/formulas/filter-by-date)
    
*   [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)
    
*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)
    
*   [Add years to date](https://exceljet.net/formulas/add-years-to-date)
    
*   [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)
    
*   [Count birthdays by year](https://exceljet.net/formulas/count-birthdays-by-year)
    
*   [Get nth day of year](https://exceljet.net/formulas/get-nth-day-of-year)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    

### Videos

*   [How to calculate years and months between dates](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)
    
*   [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)
    
*   [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)
    

### Functions

*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [DAY Function](https://exceljet.net/functions/day-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

### Links

*   [Microsoft YEAR function documentation](https://support.office.com/en-us/article/year-function-c64f017a-1354-490d-981f-578e8ec8d3b9)
    

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
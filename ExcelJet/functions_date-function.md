# Excel DATE function | Exceljet

**Source:** https://exceljet.net/functions/date-function

---

[Skip to main content](https://exceljet.net/functions/date-function#main-content)

[](https://exceljet.net/functions/date-function#)

*   [Previous](https://exceljet.net/functions/xor-function)
    
*   [Next](https://exceljet.net/functions/datedif-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

DATE Function
=============

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[TIME](https://exceljet.net/functions/time-function)

[YEAR](https://exceljet.net/functions/year-function)

[MONTH](https://exceljet.net/functions/month-function)

[DAY](https://exceljet.net/functions/day-function)

[EDATE](https://exceljet.net/functions/edate-function)

![Excel DATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20date.png "Excel DATE function")

Summary
-------

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

Purpose 
--------

Create a date with year, month, and day

Return value 
-------------

A valid Excel date

Syntax
------

    =DATE(year,month,day)

*   _year_ - Number for year.
*   _month_ - Number for month.
*   _day_ - Number for day.

Using the DATE function 
------------------------

The DATE function creates a date using individual year, month, and day [arguments](https://exceljet.net/glossary/function-argument)
. Each argument is provided as a number, and the result is a [serial number](https://exceljet.net/glossary/excel-date)
 that represents a valid Excel date. Apply a date [number format](https://exceljet.net/glossary/number-format)
 to display the output from the DATE function as a date.

In general, the DATE function is the safest way to create a date in an Excel formula, because year, month, and day values are numeric and unambiguous, in contrast to text representations of dates which can be misinterpreted. 

Note: to _move an existing date_ forward or backward in time, see the [EDATE](https://exceljet.net/functions/edate-function)
 and [EOMONTH](https://exceljet.net/functions/eomonth-function)
.

### Example #1 - hard-coded numbers

For example, you can use the DATE function to create the dates January 1, 1999, and June 1, 2010, with the following syntax:

    =DATE(1999,1,1) // returns Jan 1, 1999
    =DATE(2010,6,1) // returns Jun 1, 2010
    

### Example #2 - cell reference

The DATE function is useful for assembling dates that need to change dynamically based on other inputs in a worksheet. For example, with 2018 in cell A1, the formula below returns the date April 15, 2018:

    =DATE(A1,4,15) // Apr 15, 2018
    

If A1 is then changed to 2019, the DATE function will return a date for April 15, 2019.

### Example #3 - with SUMIFS, COUNTIFS

The DATE function can be used to supply dates as inputs to other functions like [SUMIFS](https://exceljet.net/functions/sumifs-function)
 or [COUNTIFS](https://exceljet.net/functions/countifs-function)
, since you can easily assemble a date using year, month, and day values that come from a cell reference or formula result. For example, to count dates greater than January 1, 2019, in a worksheet where A1, B1, and C1 contain year, month, and day values (respectively), you can use a formula like this:

    =COUNTIF(range,">"&DATE(A1,B1,C1))
    

The result of COUNTIF will update dynamically when A1, B1, or C1 are changed.

### Example #4 - the first day of the current year

To return the first day of the current year, you can use the DATE function like this:

    =DATE(YEAR(TODAY()),1,1) // first of year
    

This is an example of [nesting](https://exceljet.net/glossary/nesting)
. The [TODAY function](https://exceljet.net/functions/today-function)
 returns the current date to the [YEAR function](https://exceljet.net/functions/year-function)
. The YEAR function extracts the year and returns the result to the DATE function as the _year_ argument. The _month_ and _day_ arguments are hard-coded as 1. The result is the first day of the current year, a date like "January 1, 2021".

_Note: the DATE function actually returns a serial number and not a formatted date. In Excel's date system, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. January 1, 1900, is number 1 and later dates are larger numbers. To display date values in a human-readable date format, apply the [number format](https://exceljet.net/articles/custom-number-formats)
 of your choice._

### Notes

*   The DATE function returns a serial number that corresponds to an Excel date.
*   Excel dates begin in the year 1900. If the _year_ is between zero and 1900, Excel will add 1900.
*   The DATE function accepts numeric input only and will return #VALUE if given text.

DATE function examples
----------------------

[![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")](https://exceljet.net/formulas/highlight-dates-between)

### [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and...

[![Excel formula: Add years to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_years_to_date.png "Excel formula: Add years to date")](https://exceljet.net/formulas/add-years-to-date)

### [Add years to date](https://exceljet.net/formulas/add-years-to-date)

Ever needed to calculate someone's retirement date? Or figure out when a 30-year mortgage will end? Or maybe you're setting a contract expiration date? In each case, you need a way to add years to a date. Here's something that might surprise you: most Excel users tackle this problem with a formula...

[![Excel formula: Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20date%20ddmmyy%20to%20mmddyy.png "Excel formula: Convert text date dd/mm/yy to mm/dd/yy")](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

### [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

The core of this formula is the DATE function, which is used to assemble a proper Excel date value. The DATE function requires valid year, month, and day values, so these are parsed out of the original text string as follows: 1. The year value is extracted with the RIGHT function: RIGHT(B5,2)+2000...

[![Excel formula: Convert Unix time stamp to Excel date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20unix%20time%20stamp%20to%20excel%20date.png "Excel formula: Convert Unix time stamp to Excel date")](https://exceljet.net/formulas/convert-unix-time-stamp-to-excel-date)

### [Convert Unix time stamp to Excel date](https://exceljet.net/formulas/convert-unix-time-stamp-to-excel-date)

The Unix time stamp tracks time as a running count of seconds. The count begins at the "Unix Epoch" on January 1st, 1970, so a Unix timestamp is simply the total seconds between any given date and the Unix Epoch. Since a day contains 86400 seconds (24 hours x 60 minutes x 60 seconds), conversion to...

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

[![Excel formula: Highlight rows with dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20rows%20with%20dates%20between.png "Excel formula: Highlight rows with dates between")](https://exceljet.net/formulas/highlight-rows-with-dates-between)

### [Highlight rows with dates between](https://exceljet.net/formulas/highlight-rows-with-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. Dates are just serial numbers in Excel, so earlier dates are always less than later dates. In the above formula, any dates that are greater than or equal to the start date AND less than or equal to the...

[![Excel formula: Highlight dates greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20greater%20than.png "Excel formula: Highlight dates greater than")](https://exceljet.net/formulas/highlight-dates-greater-than)

### [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)

The DATE function creates a proper Excel date with given year, month, and day values. Then, it's simply a matter of comparing each date in the range with the date created with DATE. The reference B4 is fully relative, so will update as the rule is applied to each cell in the range, and any dates...

[![Excel formula: Get nth day of year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20nth%20day%20of%20year.png "Excel formula: Get nth day of year")](https://exceljet.net/formulas/get-nth-day-of-year)

### [Get nth day of year](https://exceljet.net/formulas/get-nth-day-of-year)

This formula takes advantage of the fact that dates are just sequential numbers in Excel. It determines the last day of the previous year and subtracts that value from the original date with this formula: =B5-DATE(YEAR(B5),1,0) The result is nth day of the year, based on the date in cell B5. Notice...

[![Excel formula: Filter data between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_data_between_dates.png "Excel formula: Filter data between dates")](https://exceljet.net/formulas/filter-data-between-dates)

### [Filter data between dates](https://exceljet.net/formulas/filter-data-between-dates)

The goal is to extract records with dates that are greater than or equal to a start date in F5 and less than or equal to an end date in G5. You might think we can use the AND function inside FILTER to solve this problem. However, because AND returns just a single value, this won't work. Instead, we...

[![Excel formula: Data validation only dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20only%20dates%20between.png "Excel formula: Data validation only dates between")](https://exceljet.net/formulas/data-validation-only-dates-between)

### [Data validation only dates between](https://exceljet.net/formulas/data-validation-only-dates-between)

Data validation rules are triggered when a user adds or changes a cell value. The AND function takes multiple arguments (logicals) and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because we want to allow...

[![Excel formula: Dynamic calendar formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula_0.png "Excel formula: Dynamic calendar formula")](https://exceljet.net/formulas/dynamic-calendar-formula)

### [Dynamic calendar formula](https://exceljet.net/formulas/dynamic-calendar-formula)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will automatically return the first day of the current month. In this example, the goal is to generate a dynamic calendar for any given month, based on a start date entered in cell J6...

[![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")](https://exceljet.net/formulas/get-age-from-birthday)

### [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)

The DATEDIF function (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the...

[![Excel formula: Get month from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_month_from_date.png "Excel formula: Get month from date")](https://exceljet.net/formulas/get-month-from-date)

### [Get month from date](https://exceljet.net/formulas/get-month-from-date)

The MONTH function takes just one argument, the date from which to extract the month. In the example shown, the formula is: =MONTH(B4) where B4 contains the date January 5, 2016. The MONTH function returns the number 1 representing the month( January) of the date. Note that you can use MONTH to...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

DATE function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20work%20with%20dates-thumb.png)](https://exceljet.net/videos/how-to-work-with-dates)

### [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)

Excel contains special functions that will let you extract the day, month, and year from a valid date. Let's take a look. Here we have a set of random dates in column B. First, I'll add a formula to column C to pick up the date values in B and format them with the General format, so we can see the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20date%20and%20time%20series%20with%20formulas-thumb.png)](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

### [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

Although you can use Excel's AutoFill feature to fill in a series of dates and times, you can also do the same thing with formulas. The advantage of using a formula is that you can easily change the starting value and generate a new series. Let's take a look. Often you'll need to generate a series...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumif-function)

### [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

In this video we'll look at how to use the SUMIF function to sum cells that meet a single criteria. Let's take a look. The SUMIF function sums cells that satisfy a single condition that you supply. It takes three arguments: range, criteria, and sum range. Note that sum range is optional. If you don...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20data%20between%20two%20dates-Play.png)](https://exceljet.net/videos/filter-data-between-two-dates)

### [FILTER data between two dates](https://exceljet.net/videos/filter-data-between-two-dates)

In this video, we’ll look at a couple ways to use the FILTER function to extract data between dates. In this worksheet, we have sample order data that contains a date field. Let's set up the FILTER function to extract data between two dates. Before we begin, I want to remind you that Excel dates...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20function%20arguments-thumb.png)](https://exceljet.net/videos/how-to-use-function-arguments)

### [How to use function arguments](https://exceljet.net/videos/how-to-use-function-arguments)

You've probably noticed that functions use parentheses, and inside those parentheses are certain inputs. These inputs have a special name: arguments. Let's look at some examples. Arguments can be required or optional. Some functions take three or more arguments, and some functions don't take any...

Related functions
-----------------

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

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

*   [Get month from date](https://exceljet.net/formulas/get-month-from-date)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)
    
*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    
*   [Sum if date is greater than](https://exceljet.net/formulas/sum-if-date-is-greater-than)
    
*   [Convert Unix time stamp to Excel date](https://exceljet.net/formulas/convert-unix-time-stamp-to-excel-date)
    
*   [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)
    
*   [Add years to date](https://exceljet.net/formulas/add-years-to-date)
    
*   [Range contains specific date](https://exceljet.net/formulas/range-contains-specific-date)
    

### Videos

*   [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)
    
*   [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)
    
*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    
*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    
*   [How to use function arguments](https://exceljet.net/videos/how-to-use-function-arguments)
    
*   [FILTER data between two dates](https://exceljet.net/videos/filter-data-between-two-dates)
    

### Functions

*   [TIME Function](https://exceljet.net/functions/time-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [DAY Function](https://exceljet.net/functions/day-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    

### Links

*   [Microsoft DATE function documentation](https://support.office.com/en-us/article/date-function-e36c0c8c-4104-49da-ab83-82328b832349)
    

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
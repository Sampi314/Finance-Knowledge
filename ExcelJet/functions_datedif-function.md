# Excel DATEDIF function | Exceljet

**Source:** https://exceljet.net/functions/datedif-function

---

[Skip to main content](https://exceljet.net/functions/datedif-function#main-content)

[](https://exceljet.net/functions/datedif-function#)

*   [Previous](https://exceljet.net/functions/date-function)
    
*   [Next](https://exceljet.net/functions/datevalue-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

DATEDIF Function
================

by Dave Bruns · Updated 5 Mar 2026

Related functions 
------------------

[DAYS](https://exceljet.net/functions/days-function)

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[YEARFRAC](https://exceljet.net/functions/yearfrac-function)

[TODAY](https://exceljet.net/functions/today-function)

[EDATE](https://exceljet.net/functions/edate-function)

[DATE](https://exceljet.net/functions/date-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9548/download?token=uBiOs65u)
 (52.2 KB)

![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")

Summary
-------

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3. It works in all versions of Excel, but Excel will not autocomplete the function name or help you fill in arguments.

Purpose 
--------

Get days, months, or years between two dates

Return value 
-------------

The time between two dates in a given unit

Syntax
------

    =DATEDIF(start_date,end_date,unit)

*   _start\_date_ - Start date in Excel date serial number format.
*   _end\_date_ - End date in Excel date serial number format.
*   _unit_ - The time unit to use (years, months, or days).

Using the DATEDIF function 
---------------------------

The DATEDIF function calculates the difference between two dates in years, months, or days. The result is always a whole number, because DATEDIF rounds down to the last complete interval. The desired interval is controlled by the _unit_ argument, which supports six text codes as shown in the table below:

| Unit | Result |
| --- | --- |
| "y" | Complete years between dates |
| "m" | Complete months between dates |
| "d" | Total days between dates |
| "ym" | Months remaining after complete years |
| "yd" | Days remaining after complete years |
| "md" | Days remaining after complete months |

The first three units ("y", "m", "d") return _total_ intervals. The last three ("ym", "yd", "md") return _remaining_ intervals, which is useful for breaking elapsed time into components. For example, to express a duration as "X years, Y months, Z days", you would use "y" for years, "ym" for remaining months, and "md" for remaining days.

The status of DATEDIF in Excel is somewhat mysterious. DATEDIF (Date + Dif) is a "compatibility" function that comes from Lotus 1-2-3 way back in the 1990s. Although it's available in all Excel versions since that time, it will not autocomplete in the formula bar, and Excel will not help you fill in [arguments](https://exceljet.net/glossary/function-argument)
. In the [immortal words](http://www.cpearson.com/excel/datedif.aspx)
 of the late, great Chip Pearson: _DATEDIF is treated as the drunk cousin of the Formula family. Excel knows it lives a happy and useful life, but will not speak of it in polite conversation._ Despite this unofficial status, DATEDIF remains an important and widely used function for calculating the time between two dates.

### Key features

*   Calculates the difference between two dates in years, months, or days
*   Supports six unit codes: "y", "m", "d", "ym", "yd", and "md"
*   Always returns a whole number — rounds down to the last complete interval
*   Does not appear in Excel's autocomplete or function wizard
*   Returns #NUM! error if start\_date is greater than end\_date
*   The "md" unit has a [known issue](https://exceljet.net/functions/datedif-function#known-issues-with-md)
    . The other units work as expected.

### Table of contents

*   [Basic usage](https://exceljet.net/functions/datedif-function#basic-usage)
    
*   [Difference in days](https://exceljet.net/functions/datedif-function#difference-in-days)
    
*   [Difference in months](https://exceljet.net/functions/datedif-function#difference-in-months)
    
*   [Difference in years](https://exceljet.net/functions/datedif-function#difference-in-years)
    
*   [Years, months, and days between dates](https://exceljet.net/functions/datedif-function#years-months-and-days-between-dates)
    
*   [Get age from birthday](https://exceljet.net/functions/datedif-function#get-age-from-birthday)
    
*   [Time before expiration date](https://exceljet.net/functions/datedif-function#time-before-expiration-date)
    
*   [Known issues with "md"](https://exceljet.net/functions/datedif-function#known-issues-with-md)
    
*   [Alternative to DATEDIF with "md"](https://exceljet.net/functions/datedif-function#alternative-to-datedif-with-md)
    
*   [Years, months, and days without "md"](https://exceljet.net/functions/datedif-function#years-months-and-days-without-md)
    
*   [Edge cases beyond "md"](https://exceljet.net/functions/datedif-function#edge-cases-beyond-md)
    
*   [Replacing DATEDIF](https://exceljet.net/functions/datedif-function#replacing-datedif)
    
*   [Notes](https://exceljet.net/functions/datedif-function#notes)
    

### Basic usage

    =DATEDIF("1-Jan-2023","1-Mar-2025","y") // returns 2 (complete years)
    =DATEDIF("1-Jan-2023","1-Mar-2025","m") // returns 26 (complete months)
    =DATEDIF("1-Jan-2023","1-Mar-2025","d") // returns 790 (total days)
    =DATEDIF("1-Jan-2023","1-Mar-2025","ym") // returns 2 (months after years)
    =DATEDIF("1-Jan-2023","1-Mar-2025","yd") // returns 59 (days after years)
    =DATEDIF("1-Jan-2023","1-Mar-2025","md") // returns 0 (days after months)
    

> Note: DATEDIF requires the start date to come before the end date. If _start\_date_ is greater than _end\_date_, DATEDIF returns a #NUM! error.

### Difference in days

DATEDIF can calculate the difference between dates in _days_ in three ways, using the "d", "yd", and "md" units. In the worksheet below, the goal is to calculate the day difference between start and end dates using all three day-based unit codes. The formulas in E5, F5, and G5 are:

    =DATEDIF(B5,C5,"d") // total days
    =DATEDIF(B5,C5,"yd") // days ignoring years
    =DATEDIF(B5,C5,"md") // days ignoring months and years
    

![DATEDIF function example - difference in days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_difference_in_days.png "DATEDIF function example - difference in days")

The "d" unit returns the total number of days between the two dates. The "yd" unit returns the number of days remaining after complete years have been taken into account. The "md" unit returns the number of days remaining after complete years and complete months have been taken into account.

> Note: The "md" unit has a [known issue](https://exceljet.net/functions/datedif-function#known-issues-with-md)
>  that can return incorrect results for certain date pairs. For a reliable alternative, see [Alternative to DATEDIF with "md"](https://exceljet.net/functions/datedif-function#alternative-to-datedif-with-md)
>  below.

For more details, see [Get days between dates ignoring years](https://exceljet.net/formulas/get-days-between-dates-ignoring-years)
.

### Difference in months

DATEDIF can calculate the difference between dates in _months_ in two ways, using the "m" and "ym" units. In the worksheet below, the goal is to calculate the month difference between start and end dates. The formulas in E5 and F5 are:

    =DATEDIF(B5,C5,"m") // complete months
    =DATEDIF(B5,C5,"ym") // months ignoring years
    

![DATEDIF function example - difference in months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_difference_in_months.png "DATEDIF function example - difference in months")

The "m" unit returns the total number of complete months between the dates. The "ym" unit returns the number of months remaining after complete years have been counted. This is useful when expressing a duration as years and months.

Note that DATEDIF always rounds months down to the nearest whole month. This means DATEDIF will round a result down even when the interval is very close to the next whole month. In addition, DATEDIF may not work as expected when start and end dates fall at the end of a month.

For a detailed explanation of calculating months between dates, including several alternative formulas, see [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)
.

### Difference in years

DATEDIF calculates the difference between dates in complete _years_ with the "y" unit. In the worksheet below, the goal is to calculate the number of complete years between start and end dates. The formula in E5 is:

    =DATEDIF(B5,C5,"y") // complete years
    

![DATEDIF function example - difference in years](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_difference_in_years.png "DATEDIF function example - difference in years")

DATEDIF only returns complete years — it always rounds down. For example, if two dates are 5 years and 11 months apart, DATEDIF returns 5. If you need fractional years, the [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
 is a better option. Column F shows YEARFRAC results for comparison.

### Years, months, and days between dates

DATEDIF's ability to return different time components makes it ideal for expressing elapsed time as a combination of years, months, and days. In the worksheet below, we use DATEDIF three times in each row, each time with a different unit: "y" for complete years, "ym" for remaining months after years, and "md" for remaining days after months. The formulas in E5, F5, and G5 look like this:

    =DATEDIF(B5,C5,"y") // years
    =DATEDIF(B5,C5,"ym") // months
    =DATEDIF(B5,C5,"md") // days
    

![DATEDIF function example - years, months, and days as separate results](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_years_months_days_separate.png "DATEDIF function example - years, months, and days as separate results")

Together, the three results add up to the total time elapsed between the start date and end date. To display time elapsed as a _single_ result like "X years, Y months, Z days", we need to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the three values together. In the worksheet below, the formula in E5 is:

    =DATEDIF(B5,C5,"y")&" years, "&DATEDIF(B5,C5,"ym")&" months, "&DATEDIF(B5,C5,"md")&" days"
    

![DATEDIF function example - years, months, and days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_years_months_days.png "DATEDIF function example - years, months, and days")

The result in each row is a single text string that indicates the time elapsed in years, months, and days.

> Note: This formula uses the "md" unit, which has a [known issue](https://exceljet.net/functions/datedif-function#known-issues-with-md)
>  that can produce incorrect results for certain date pairs. See below for a more [reliable alternative](https://exceljet.net/functions/datedif-function#years-months-and-days-without-md)
> .

For more details, see [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
.

### Get age from birthday

DATEDIF is commonly used with the [TODAY function](https://exceljet.net/functions/today-function)
 to calculate a person's current age from their birth date. In the worksheet below, the goal is to calculate ages in whole years. The formula in E5 is:

    =DATEDIF(C5,TODAY(),"y")
    

![DATEDIF function example - get age from birthday](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_get_age_from_birthday.png "DATEDIF function example - get age from birthday")

The birth date in column C is the start\_date and TODAY() provides the end\_date. The "y" unit returns complete years, which is exactly how age is typically reported. Because TODAY is a [volatile function](https://exceljet.net/glossary/volatile-function)
, this formula recalculates automatically each time the workbook is opened, so the ages will always be current.

For more details, see [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)
.

### Time before expiration date

DATEDIF can be combined with the [IF function](https://exceljet.net/functions/if-function)
 to calculate how much time remains before an expiration date (or any date in the future). In the worksheet below, the goal is to display the remaining time for each item as years, months, and days, or "Expired" if the expiration date has passed. The formula in E5 is:

    =IF(C5>TODAY(),DATEDIF(TODAY(),C5,"y")&"y "&DATEDIF(TODAY(),C5,"ym")&"m "&DATEDIF(TODAY(),C5,"md")&"d","Expired")
    

![DATEDIF function example - time before expiration](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_time_before_expiration.png "DATEDIF function example - time before expiration")

The IF function first checks whether the expiration date in C5 is in the future. If so, DATEDIF calculates the remaining time in years, months, and days. If the expiration date has already passed, the formula returns "Expired".

For more details and alternative approaches, see [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)
.

### Known issues with "md"

Microsoft's own documentation includes this warning about the "md" unit: "The "MD" argument may result in a negative number, a zero, or an inaccurate result." This warning has caused a lot of confusion, since it's not clear exactly when the problem occurs or how serious it is. You can see an example of the issue in the worksheet below, where the goal is to show the months ("ym") and remaining days ("md") results for start dates of January 27 through February 3, all with an end date of March 1. The formulas in E5 and F5 are:

    =DATEDIF(B5,C5,"ym") // months (column E)
    =DATEDIF(B5,C5,"md") // days (column F)
    

![DATEDIF function example - known issues with md](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_known_issues_md.png "DATEDIF function example - known issues with md")

For start dates of January 29, January 30, and January 31, the "md" unit returns incorrect values (0, -1, and -2). You can see the same problem on row 14, where the start date is March 31, the end date is May 1, and the result from DATEDIF is 0. The cause of the bug is unknown, since the internal algorithm for DATEDIF with "md" isn't documented. However, the "md" unit _should_ return the number of remaining days after complete months have been counted. Before discussing a fix for this problem, it's important to understand that counting months and days is inherently awkward because months have variable lengths.

**Why counting months and days is tricky**

When we calculate a duration in months and days, the standard approach is to count complete months first, then count the remaining days. This works well most of the time, but it produces some surprising results near the end of shorter months. Because February has only 28 days (in a non-leap year), start dates from January 28-31 all "round" to the same month boundary (February 28), leaving the same 1-day remainder. The result is that four different spans, ranging from 29 to 32 actual days, have a time span of "1 month, 1 day" as seen in the table below:

| Start date | End date | Total days | Duration |
| --- | --- | --- | --- |
| Jan 27 | Mar 1 | 33  | 1 month, 2 days |
| Jan 28 | Mar 1 | 32  | 1 month, 1 day |
| Jan 29 | Mar 1 | 31  | 1 month, 1 day |
| Jan 30 | Mar 1 | 30  | 1 month, 1 day |
| Jan 31 | Mar 1 | 29  | 1 month, 1 day |
| Feb 1 | Mar 1 | 28  | 1 month, 0 days |

This can occur whenever the start date falls on a day number that doesn't exist in the last full month of the span. Since "a whole month" can't land on a day that doesn't exist, those dates get capped at the last day of that month, and the remaining days are counted from there. The effect is most noticeable in February because it's the shortest month, but the same thing can happen when the span ends on any shorter month — for example, starting on the 31st when the last full month has only 30 days.

### Alternative to DATEDIF with "md"

One way to avoid the DATEDIF "md" bug explained above is to avoid DATEDIF with "md" altogether and use a workaround based on the [EDATE function](https://exceljet.net/functions/edate-function)
 to calculate remaining days after complete months. The generic version of the formula is:

      =end_date-EDATE(start_date,DATEDIF(start_date,end_date,"m"))
    

This is a drop-in replacement for DATEDIF with "md". Adapting this formula to the worksheet shown, the formula in G5 is:

    =C5-EDATE(B5,DATEDIF(B5,C5,"m"))
    

![DATEDIF function example - EDATE alternative for md](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_edate_alternative_for_md.png "DATEDIF function example - EDATE alternative for md")

Working from the inside out, we use DATEDIF with "m" to calculate the number of complete months between the start and end dates. Then we feed that result into EDATE, effectively "adding" complete months to the start date. Finally, we subtract the result from the end date to get the remaining days. Because EDATE correctly handles month-length differences (for example, January 31 plus one month returns February 28), the result is accurate. The formulas below use the EDATE approach to correctly calculate remaining days.

### Years, months, and days without "md"

To fix the years, months, and days formula shown [above](https://exceljet.net/functions/datedif-function#years-months-and-days-between-dates)
, replace the "md" unit with the EDATE alternative explained above. The original formula is:

    =DATEDIF(B5,C5,"y")&" years, "&DATEDIF(B5,C5,"ym")&" months, "&DATEDIF(B5,C5,"md")&" days"
    

Swapping in the EDATE formula above for the "md" portion yields:

    =DATEDIF(B5,C5,"y")&" years, "&DATEDIF(B5,C5,"ym")&" months, "&C5-EDATE(B5,DATEDIF(B5,C5,"m"))&" days"
    

DATEDIF handles the years and months calculations, which are reliable. For the remaining days, the formula uses EDATE to add all complete months back onto the start date, then subtracts from the end date. Because EDATE correctly handles month-length differences, the result is accurate for all date pairs. In the worksheet below, column E shows the broken result using "md" and column F shows the corrected result using EDATE. The patched formula produces correct results for all date pairs, including those where "md" fails.

![DATEDIF function example - years, months, and days without md](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/datedif_example_years_months_days_without_md.png "DATEDIF function example - years, months, and days without md")

The same formula can be written more clearly with the [LET function](https://exceljet.net/functions/let-function)
:

    =LET(
      start,B5,
      end,C5,
      years,DATEDIF(start,end,"y"),
      months,DATEDIF(start,end,"ym"),
      days,end-EDATE(start,DATEDIF(start,end,"m")),
      years&" years, "&months&" months, "&days&" days"
    )
    

The logic of this formula is the same as above. However, this version uses the LET function to define variables for better readability. Notice that years, months, and days are defined separately, then concatenated together into a single text string as the final result.

### Edge cases beyond "md"

The "md" unit gets the most attention for producing incorrect results, but my testing reveals that other DATEDIF units also have edge cases worth noting. These issues are subtler, but they can affect formulas that require exact date arithmetic.

#### The "m" and "ym" units with end-of-month dates

When the start date falls on the 29th, 30th, or 31st of a month, and the end date lands on the last day of a shorter month, DATEDIF may undercount complete months by one. For example:

    =DATEDIF("2025-01-31","2025-02-28","m")  // returns 0, arguably should be 1
    =DATEDIF("2025-03-31","2025-04-30","m")  // returns 0, arguably should be 1
    =DATEDIF("2025-01-31","2025-04-30","m")  // returns 2, arguably should be 3
    

It appears that a month is only counted when the ending day-of-month is at least as large as the starting day-of-month. In other words, DATEDIF is counting whole-month anniversaries, which is why end-of-month dates can behave oddly when the end month is shorter. This is inconsistent with Excel's own [EDATE function](https://exceljet.net/functions/edate-function)
, which considers January 31 plus one month to be February 28. The bottom line is that DATEDIF and EDATE use different definitions of what "one month" means at month boundaries: DATEDIF uses a day-number comparison, while EDATE uses end-of-month logic. 

**The "yd" unit and leap years**

DATEDIF also has some trouble with the "yd". The "yd" unit returns the number of days remaining after complete years. My testing showed that "yd" can be off by one day when the date span crosses a February 29 leap day boundary. For example:

    =DATEDIF("2015-01-03","2016-07-28","yd")  // returns 206, correct answer is 207
    =DATEDIF("2016-01-21","2023-03-27","yd")  // returns 66, correct answer is 65
    

These errors are not restricted to end-of-month dates; they occur with ordinary dates like January 3 or August 8. The direction of the error varies: DATEDIF sometimes returns one day too many, sometimes one day too few. Without source code to check, it's hard to know why this happens, but perhaps DATEDIF calculates "yd" using a day-of-year approach based on the start year's calendar, rather than counting actual days from the anniversary date to the end date. If you need a more reliable "days after complete years" calculation, you can use the same EDATE approach used to fix "md":

    =end_date-EDATE(start_date,DATEDIF(start_date,end_date,"y")*12)
    

This adds complete years (converted to months) back onto the start date using EDATE, then subtracts from the end date to get the exact remaining days.

#### Summary of unit reliability

| Unit | Status |
| --- | --- |
| "d" | Reliable. Simple date subtraction, no edge cases |
| "y" | Reliable for most purposes |
| "m" | May undercount by 1 at end-of-month boundaries |
| "ym" | Same end-of-month issue as "m" |
| "yd" | May be off by 1 day when the span crosses a leap day |
| "md" | Can produce negative or incorrect values, [avoid](https://exceljet.net/functions/datedif-function#alternative-to-datedif-with-md) |

### Replacing DATEDIF

After documenting the problems above in some detail, my conclusion is that DATEDIF mostly works as expected, but is buggy with specific edge cases. Although you can work around these problems individually, tracking each issue is tricky and time-consuming, because the edge cases are quite specific and the problems, when they appear, can be subtle. In a modern version of Excel, I think a better solution is to [replace DATEDIF altogether with a more reliable formula](https://exceljet.net/articles/how-to-replace-excels-datedif-function)
. This article explains how to build a custom lambda function named DATEDIF2 that mimics the features of DATEDIF but without the bugs.

### Notes

*   DATEDIF does not appear in Excel's autocomplete or function wizard. You must type the full function name manually.
*   DATEDIF returns a #NUM! error if _start\_date_ is greater than _end\_date_. You can trap this error with the [IFERROR function](https://exceljet.net/functions/iferror-function)
    .
*   The "md" unit has a [known issue](https://exceljet.net/functions/datedif-function#known-issues-with-md)
     that can produce negative values or inaccurate results. The other five units are reliable.
*   DATEDIF always rounds down to the last complete interval. For example, 11 months and 29 days returns 0 for the "y" unit.
*   DATEDIF is a "compatibility" function inherited from Lotus 1-2-3. Despite its unofficial status, it is available in all current versions of Excel.
*   Unit codes are not case-sensitive: "ym" is equivalent to "YM".

DATEDIF function examples
-------------------------

[![Excel formula: Repeat fixed value every 3 months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat%20value%20every%20n%20months.png "Excel formula: Repeat fixed value every 3 months")](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)

### [Repeat fixed value every 3 months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)

The first thing this formula does is check the date in column B against the start date: =IF(B4>=start If the date is not greater than the start date, the formula returns zero. If the date is greater than or equal to the start date, the IF function runs this snippet: (MOD(DATEDIF(start,B4,"m")+n,...

[![Excel formula: Get days, months, and years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20months%20and%20years%20between%20dates.png "Excel formula: Get days, months, and years between dates")](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

### [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

In this example, the goal is to output the time between a start date and an end date as a text string that lists years, months, and days separately. For example, given a start date of 1-Jan-2018 and an end date of 1-Jul-2018, the result should be a string like this: "1 years, 6 months, 0 days"...

[![Excel formula: Get months between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_months_between_dates.png "Excel formula: Get months between dates")](https://exceljet.net/formulas/get-months-between-dates)

### [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)

In this example, the goal is to calculate the number of months between two valid Excel dates . This is a curiously tricky problem in Excel because the number of days in a month varies, and the rules about how a whole month might be calculated are not obvious. In addition, there is not a modern...

[![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")](https://exceljet.net/formulas/get-age-from-birthday)

### [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)

The DATEDIF function (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the...

[![Excel formula: Get days between dates ignoring years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20days%20between%20dates%20ignoring%20years.png "Excel formula: Get days between dates ignoring years")](https://exceljet.net/formulas/get-days-between-dates-ignoring-years)

### [Get days between dates ignoring years](https://exceljet.net/formulas/get-days-between-dates-ignoring-years)

The DATEDIF function can handle a variety of "date difference" calculations to calculate the difference between two dates in years, months, and days. DATEDIF takes 3 arguments: start date, end\_date, and "unit", which controls which result is returned. In this case, we want days ignoring years so we...

[![Excel formula: Next anniversary date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20anniversary%20date.png "Excel formula: Next anniversary date")](https://exceljet.net/formulas/next-anniversary-date)

### [Next anniversary date](https://exceljet.net/formulas/next-anniversary-date)

Working from the inside out, we use the DATEDIF function to calculate how many complete years are between the original anniversary date and the "as of" date, where the as of date is any date after the anniversary date: DATEDIF(B5,C5,"y") Note: in this case, we are arbitrarily fixing the "as of"...

[![Excel formula: Calculate time before expiration date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_time_before_expiration_date.png "Excel formula: Calculate time before expiration date")](https://exceljet.net/formulas/calculate-time-before-expiration-date)

### [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)

In this example, the goal is to calculate the time remaining before an expiration date. There are many ways to do something like this in Excel, and in this article, we'll look at three different approaches: Calculating the remaining time in days Calculating the remaining time in years, months, and...

DATEDIF function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20years%20and%20months%20between%20dates-thumb.png)](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)

### [How to calculate years and months between dates](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)

In this video we'll look at how to calculate the number of years or months between dates using a function called DATEDIF and a function called YEARFRAC . The DATEDIF function is a "compatibility" function that comes from Lotus 1-2-3. For reasons that are unknown, it's only documented in Excel 2000...

Related functions
-----------------

[![Excel DAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20days%20function.png "Excel DAYS function")](https://exceljet.net/functions/days-function)

### [DAYS Function](https://exceljet.net/functions/days-function)

The Excel DAYS function returns the number of days between two dates. With a start date in A1 and end date in B1, =DAYS(B1,A1) will return the days between the two dates.

[![Excel NETWORKDAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays%20function.png "Excel NETWORKDAYS function")](https://exceljet.net/functions/networkdays-function)

### [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can _optionally_ exclude a list of holidays supplied as dates. ...

[![Excel YEARFRAC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_yearfrac_function.png "Excel YEARFRAC function")](https://exceljet.net/functions/yearfrac-function)

### [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)

The Excel YEARFRAC function returns a decimal value that represents fractional years between two dates. You can use YEARFRAC to do things like calculate age with a birthdate....

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

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
    
*   [Get days between dates ignoring years](https://exceljet.net/formulas/get-days-between-dates-ignoring-years)
    
*   [Repeat fixed value every 3 months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)
    
*   [Next anniversary date](https://exceljet.net/formulas/next-anniversary-date)
    
*   [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)
    
*   [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    
*   [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)
    

### Videos

*   [How to calculate years and months between dates](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)
    
*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    

### Functions

*   [DAYS Function](https://exceljet.net/functions/days-function)
    
*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    

### Articles

*   [How to replace Excel's DATEDIF function](https://exceljet.net/articles/how-to-replace-excels-datedif-function)
    

### Links

*   [Microsoft DATEDIF function documentation](https://support.office.com/en-us/article/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c)
    

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
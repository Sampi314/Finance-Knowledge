# Calculate hours between two times - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-hours-between-two-times

---

[Skip to main content](https://exceljet.net/formulas/calculate-hours-between-two-times#main-content)

[](https://exceljet.net/formulas/calculate-hours-between-two-times#)

*   [Previous](https://exceljet.net/formulas/calculate-expiration-date)
    
*   [Next](https://exceljet.net/formulas/calculate-retirement-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Calculate hours between two times
=================================

by Dave Bruns · Updated 11 Jun 2025

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[MOD](https://exceljet.net/functions/mod-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8393/download?token=YRo082JO)
 (44.18 KB)

![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")

Summary
-------

To calculate the difference between two times in hours in Excel, you can use a formula that subtracts the start time from the end time, adding conditional logic as needed to handle cases where start and end times cross midnight. In the example shown, the formula in E5 is:

    =IF(C5>B5,C5-B5,1-B5+C5)
    

As the formula is copied down, it returns the number of hours and minutes between the start time in column B and the end time in column C. Note that times that cross midnight are handled correctly. The result is native Excel time, but you can easily convert this value into decimal hours, as explained below.

Generic formula
---------------

    =IF(end>start,end-start,1-start+end)

Explanation 
------------

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways:

*   Calculate elapsed working time in hours.
*   Calculate the duration of an activity in hours.
*   Calculate the hours needed for a task.

Calculating the hours between two times is oddly complicated, partly because Excel stores time as _fractional values_. For example, 0.25 is 6:00 AM or 6:00 hours, depending on formatting. The number 0.25 makes sense when you consider that 6 hours is one-quarter of a day, and a day in Excel equals 1. But it isn't the way most people think about time.

The other reason time is complicated is that it resets to zero again at midnight. If you have a start time and an end time that occur on the same day, you can subtract the start time from the end time and end up with a positive number that represents the hours between the two times. However, if the times cross midnight, the start time can be greater than the end time, and you'll end up with a negative time, which Excel does not support.

When solving this problem in Excel, there are three important factors to consider: (1) Do the times cross midnight? (2) Do time durations exceed 24 hours? (3) Are the times part of a date? The article below describes three formulas for calculating the number of hours between two times. It also explains how to format time and calculate the hours between times as a decimal value.

### Table of Contents

*   [Formula options](https://exceljet.net/formulas/calculate-hours-between-two-times#formula-options)
    
*   [How Excel tracks time](https://exceljet.net/formulas/calculate-hours-between-two-times#how-excel-tracks-time)
    
*   [Formula 1: Simple duration calculation](https://exceljet.net/formulas/calculate-hours-between-two-times#formula-1-simple-duration-calculation)
    
*   [Formula 2: When times cross midnight](https://exceljet.net/formulas/calculate-hours-between-two-times#formula-2-when-times-cross-midnight)
    
*   [Formula 3: Clever MOD alternative](https://exceljet.net/formulas/calculate-hours-between-two-times#formula-3-clever-mod-alternative)
    
*   [Dates with times](https://exceljet.net/formulas/calculate-hours-between-two-times#dates-with-times)
    
*   [Number formatting for time](https://exceljet.net/formulas/calculate-hours-between-two-times#number-formatting-for-time)
    
*   [Calculating decimal hours between times](https://exceljet.net/formulas/calculate-hours-between-two-times#calculating-decimal-hours-between-times)
    

### Formula options

Below are the three formulas explained in this article. The first formula works fine if the times occur on the same day and do not cross midnight. It also works well for _dates that contain time_, which is [explained here](https://exceljet.net/formulas/calculate-hours-between-two-times#working-with-date-and-times)
. The second formula is a traditional formula based on the IF function to handle times on the same day and times that cross midnight. The third formula is an elegant alternative to the second formula.

    =end-start // for times on same day or dates with times
    =IF(end>start,end-start,1-start+end) // for times that cross midnight
    =MOD(end-start,1) // clever alternative

To start, let's review how Excel handles time.

### How Excel tracks time

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
, and one day has a numeric value of 1. Time is a fractional value of 1, and 1 hour = 1/24 = 0.041666667. This means that 6 hours is one-quarter of a day and has a numeric value of 0.25, 12 hours is half a day and has a value of 0.5, 18 hours is three-quarters of a day and is 0.75, and 24 hours is 1 day with time reset to zero. In the same way, 6:00 AM has a numeric value of 0.25, 12:00 PM has a value of 0.5, 6:00 PM has a value of 0.75, and so on, as summarized in the table below:

| Hours | Time | Fraction | Value |
| --- | --- | --- | --- |
| 3   | 3:00 AM | 3/24 | 0.125 |
| 6   | 6:00 AM | 6/24 | 0.25 |
| 4   | 4:00 AM | 4/24 | 0.167 |
| 8   | 8:00 AM | 8/24 | 0.333 |
| 12  | 12:00 PM | 12/24 | 0.5 |
| 18  | 6:00 PM | 18/24 | 0.75 |
| 21  | 9:00 PM | 21/24 | 0.875 |

Back in Excel, the screen below shows the times in the worksheet formatted as regular numbers:

![How Excel tracks time as fractional values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/how_excel_tracks_time_as_fractional_values.png "How Excel tracks time as fractional values")

You can see that 6:00 AM is 0.25, 6:00 PM is 0.75, 12:00 PM is 0.5, midnight is zero, and so on. Because an hour in Excel is 1/24, you can multiply time by 24 to get a decimal hour. For example 0.5 \* 24 = 12 hours, 0.25 \* 24 = 6 hours, etc. [See below for more details](https://exceljet.net/formulas/calculate-hours-between-two-times#calculating-decimal-hours-between-times)
.

Video: [How to use time formatting in Excel](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)

### Formula 1: Simple duration calculation

When start and end times occur on the same day, calculating duration in hours is straightforward because the end time will be a larger number than the start time. In that case, you can use a simple formula like this:

    =end-start

For example, with a start time of 6:00 AM and an end time of 12:00 PM:

    ="12:00 PM"-"6:00 AM"
    =0.5-0.25
    =0.25

When formatted with the number format "h:mm", Excel will display 6:00. This formula works well for times that occur on the same day. However, if times cross midnight, it will fail.

### Formula 2: When times cross midnight

Excel handles time as a 24-hour clock. As a day progresses, the time value increases, approaching 1 toward midnight. However, at midnight, the 24 hours will add up to 1 day, and the time value will reset to zero. If you type a zero into a cell and apply time formatting, Excel will display the time as midnight. This makes sense as a clock, but it makes calculating time more difficult when times cross midnight. For example, if the start time is 9:00 PM one day, and the end time is 6:00 AM the next day, the end time is less than the start time, and the formula above will return a negative value:

    ="6:00 AM"-"9:00 PM"
    =0.25-0.875
    =-0.625

Excel does not support negative time or date values and will display a string of hash characters (########) when time formatting is applied to a negative number. You can see what this looks like in the screen below:

![Example of simple formula failing on times that cross midnight](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/calculate_hours_between_two_times_fail_example.png "Example of simple formula failing on times that cross midnight")

To correct this problem, you can use a formula like this:

    =IF(end>start,end-start,1-start+end)

With cell references added, the formula in cell E5 becomes:

    =IF(C5>B5,C5-B5,1-B5+C5)

This formula is designed to handle both cases: times that occur on the same day and times that cross midnight. The [IF function](https://exceljet.net/functions/if-function)
 checks the times and applies the correct formula. To start, we test the end time against the start time:

    =IF(end>start,

If the end time is greater than the start time, the times belong to the same day, and we run the simple formula above:

    =end-start

If, however, the end time is not greater than the start time, we assume the times cross midnight, and in that case, we run:

    =1-start+end

By subtracting the start time from 1, we get the amount of time on the first day, which we add to the time on the second day, equal to the end time. This works because 24 hours is 1 day, and the point at which time resets to zero. When we subtract the start time from 1, we get the time until midnight. When we add the end time, we add the time from midnight until the end time. The two times together are the total elapsed time. You can see the result in the worksheet below, where the formula in E5 is:

    =IF(C5>B5,C5-B5,1-B5+C5)

![The IF function to calculate hours between times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/calculate_hours_between_two_times_with_if_function.png "The IF function to calculate hours between times")

To recap, if the end time is greater than the start time, the times are on the same day, and the simple formula is used. Otherwise, the times cross midnight, and the second formula is used.

### Formula 3: Clever MOD alternative

One complication of the formula above is that we need to calculate elapsed time with two different formulas. The [MOD function](https://exceljet.net/functions/mod-function)
 provides an elegant way to simplify the problem and apply a single formula that will work for both scenarios:

    =MOD(end-start,1)

Because this formula will handle times that cross midnight, we don't need a conditional IF statement. The way the formula works, however, is more cryptic because it depends on [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)
, a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus.

The MOD function returns the remainder after division. The result has the same sign as the divisor. Inside MOD, we supply the _number_ by subtracting the start time from the end time. For the _divisor_, we provide the number 1. When you divide any number by 1, the result is the number itself. This is because division by 1 does not change the value of the number. However, when MOD calculates a remainder, it handles positive numbers differently from negative numbers. We can use this difference to our advantage with time in Excel.

When times occur on the same day, the end time will be greater than the start time, and the _number_ will be positive and a valid Excel time. For example, with a start time of 9:00 AM and an end time of 3:00 PM, the number after subtraction will be 0.25 (6 hours), which MOD will return unchanged:

    =MOD(0.625-0.375,1)
    =MOD(0.25,1)
    =0.25 // 6 hours
    

However, when times cross midnight, the end time will be less than the start time, and the _number_ will be negative. For example, with a start time of 9:00 PM and an end time of 3:00 AM, the number after subtraction will be -0.75, which is not a valid Excel time. The MOD function takes care of this problem by "flipping" the negative value to the correct positive value 0.25:

    =MOD(0.125-0.875,1)
    =MOD(-0.75,1)
    =0.25 // 6 hours
    

In both examples above, the result is 0.25, or 6 hours, when formatted as an Excel time. To summarize, MOD will return the positive times unchanged and "flip" the negative times to a correct positive time.

    =MOD(0.25,1) // returns 0.25
    =MOD(-0.75,1) // returns 0.25

You can see the MOD formula applied in the worksheet below, where cell E5 contains:

    =MOD(C5-B5,1)

![Using the MOD function calculate hours between times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/calculate_hours_between_two_times_mod_function_option.png "Using the MOD function calculate hours between times")

The MOD function works very well here because a "modulus" has clock-like properties. For a good introduction to modular arithmetic, see this [link on Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)
.

_Note: The formulas above will not handle durations greater than 24 hours. If this is a requirement, see the "Dates with times" section below._

### Date with times

Although it's not obvious, Excel can work with dates _that include a time value_, sometimes called a "datetime." This can greatly simplify calculating elapsed time because we no longer need to worry about times crossing midnight, and we can calculate elapsed times over 24 hours. When a date in Excel has a time component, the date will appear as a whole number, and the time will appear as a decimal value. For example:

1.  The number 45457 is equivalent to "June 14, 2024" in Excel.
2.  The number 45457.5 is equivalent to "June 14, 2024, at 12:00 PM" in Excel.

The whole number to the right of the decimal (45467) is the date (June 24, 2024), and the decimal value (0.5) is the time (12:00 PM). To enter a date with a time, place a single space between time and date like this: "24-Jun-2024 12:00". If you format this date with General format ([keyboard shortcut](https://exceljet.net/shortcuts)
 Control + ~), you'll see a value like this:

    45467.5 // date + time

When calculating the hours between two times, dates with times are ideal because they automatically handle times that cross midnight. Unlike simple time values, there is no danger that the start time will be greater than the end time because, by definition, later dates with times must be _larger_ numbers. As a result, when working with dates that include time, we can revert to the simple formula:

    =end-start

You can see this formula below where start and end values contain both dates and times, and the formula in D5 is:

    =C5-B5 // end-start

![Using dates with times avoids complication](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/calculate_hours_between_dates_with_times.png "Using dates with times avoids complication")

The result is formatted with a custom number format to display elapsed hours:

    [h]:mm

This format will correctly display the hours between two times when the difference is over 24 hours, as seen in the workbook below:

![Dates with times can handle durations over 24 hours](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/calculate_hours_between_dates_with_times_over_24_hours.png "Dates with times can handle durations over 24 hours")

### Number formatting for time

What causes Excel to display 0.5 as "12:00 PM" is [number formatting](https://exceljet.net/articles/custom-number-formats)
. Below are two common number formats for time. The first will display 0.75 as 6:00 PM, and the second will display 0.75 as 18:00:

    h:mm AM/PM // display like 6:00 PM
    h:mm // display like 18:00

By default, Excel may display time with AM/PM. For example, if you have a calculated time of 6 hours, Excel may display this as 6:00 AM. To remove the AM/PM, apply a custom number format like this:

    h:mm

As mentioned above, when elapsed time may exceed 24 hours, add square brackets around the h:

    [h]:mm

The square bracket syntax \[h\] tells Excel to display hour durations greater than 24 hours (e.g., display 36 hours as 36:00). If you don't use the brackets, Excel will reset time to zero when the duration hits 24 hours (like a clock).

### Calculating decimal hours between times

The formulas above all return native Excel time as a result. This is great when you want to display hours and minutes, but it is inconvenient when you want to, for example, multiply calculated hours by an hourly rate. For such calculations, you will want to convert the result to _decimal hours_. To do this, just multiply the Excel time by 24. You can see an example below, where we calculate the hours between two times with the MOD formula above and multiply the result by 24. The formula in cell E5 is:

    =MOD(C5-B5,1)*24

![Alternative formula to calculate decimal hours between two times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/calculate_decimal_hours_between_two_times.png "Alternative formula to calculate decimal hours between two times")

When you convert to decimal hours, change the number format to suit. The number format in the worksheet above is "0:00" to display a number with two decimal places. You can use "0.0" to display a single decimal place.

### Recommendations

*   Using dates with times is the best option because it eliminates the problem of times crossing midnight. As a result, you can use Formula 1, and it will always work. In addition, you can work with time durations over 24 hours.
*   You can also use Formula 1 if times always occur on the same day and don't ever cross midnight.
*   If times do cross midnight, use Formula 2 or Formula 3, depending on your preference. Both formulas will return equivalent results.
*   Pay attention to the number formatting applied to times. Periodically apply the [General format](https://exceljet.net/shortcuts/apply-general-format)
     to time values to check your understanding of the numbers underneath.
*   Convert Excel to decimal hours as needed in order to perform calculations like hours \* pay.

Related formulas
----------------

[![Excel formula: Hours that overlap specific time blocks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hours_that_overlap_specific_time_blocks.png "Excel formula: Hours that overlap specific time blocks")](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

### [Hours that overlap specific time blocks](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

In this example, the goal is to calculate exactly how much of a task, shift, or event falls inside one or more defined blocks of time. The formula accepts a start and end time for the overall task or shift, as well as a start and end time for the block of interest. In the worksheet shown, the Start...

[![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")](https://exceljet.net/formulas/get-work-hours-between-dates)

### [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per...

[![Excel formula: Get work hours between dates custom schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20custom2.png "Excel formula: Get work hours between dates custom schedule")](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

### [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

At the core, this formula uses the WEEKDAY function to figure out the day of week (i.e. Monday, Tuesday, etc.) for every day between the two given dates. WEEKDAY returns a number between 1 and 7. With default settings, Sunday=1 and Saturday = 7. The trick to this formula is assembling an array of...

[![Excel formula: Get days, hours, and minutes between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20hours%20and%20minutes%20between%20dates2.png "Excel formula: Get days, hours, and minutes between dates")](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

### [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

Most of the work in this formula is done by the TEXT function, which applies a custom number format for hours and minutes to a value created by subtracting the start date from the end date. TEXT(C5-B5,"h"" hrs ""m"" mins """) This is an example of embedding text into a custom number format, and...

[![Excel formula: Convert Excel time to decimal hours](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20excel%20time%20to%20decimal%20hours.png "Excel formula: Convert Excel time to decimal hours")](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

### [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

In the Excel time system, one 24-hour day is equal to 1. This means times and hours are fractional values of 1, as shown in the table below: Hours Time Fraction Value 1 1:00 AM 1/24 0.04167 3 3:00 AM 3/24 0.125 6 6:00 AM 6/24 0.25 4 4:00 AM 4/24 0.167 8 8:00 AM 8/24 0.333 12 12:00 PM 12/24 0.5 18 6...

[![Excel formula: Basic timesheet formula with breaks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20timesheet%20formula%20with%20breaks.png "Excel formula: Basic timesheet formula with breaks")](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)

### [Basic timesheet formula with breaks](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)

At the core, this formula subtracts start time from end time to get duration in hours. This is done to calculate both work time and break time. MOD(C6-B6,1) // get work time MOD(E6-D6,1) // get break time Next, break time is subtracted from work time to get "net" work hours. This formula uses the...

[![Excel formula: Timesheet overtime calculation formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20overtime%20calculation.png "Excel formula: Timesheet overtime calculation formula")](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

### [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

Note: it's important to understand that Excel deals with time as fractions of a day . So, 12:00 PM is .5, 6:00 AM is .25, 6 PM is .75, and so on. This works fine for standard time and date calculations, but in many cases you'll want to convert times to decimal hours to make other calculations more...

[![Excel formula: Convert time to time zone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20time%20to%20time%20zone.png "Excel formula: Convert time to time zone")](https://exceljet.net/formulas/convert-time-to-time-zone)

### [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)

Times in Excel are fractional values of the number 1 . So, 12 PM is 12/24 = .5, 6:00 AM is 6/24 = .25, and so on. So, to convert a time by a given number, you need to divide the number of hours by 24 to get required decimal value: E5/24 // convert adjustment to Excel time We add the result to the...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20enter%20times%20in%20Excel-thumb.png)](https://exceljet.net/videos/how-to-enter-times-in-excel)

### [How to enter times in Excel](https://exceljet.net/videos/how-to-enter-times-in-excel)

In this lesson, we'll look at how to enter times in Excel. As with dates, the key to entering a time in Excel is to enter it in a format that Excel will recognize as a time. When checking for a time, Excel will look for hours, minutes, seconds, and the AM or PM designation. Let's take a look. You...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_time_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)

### [How to use time formatting in Excel](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)

In this lesson we'll look at the Time format. Like the Date format, the Time format includes a number of built-in options for displaying time. Let's take a look. Here we have a set of times in column B of our table. Let's start off by copying these times to all columns, then adjust formats to match...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_date_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)

### [How to use date formatting in Excel](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)

In this lesson we'll take a look at the Date format. The Date format is flexible and can display the same date in many different ways. Let's take a look. Here we have a set of dates in column B of our table. Let's start off by copying these dates to all columns. Let's look first at the Short Date...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Hours that overlap specific time blocks](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)
    
*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    
*   [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)
    
*   [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)
    
*   [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
    
*   [Basic timesheet formula with breaks](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)
    
*   [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)
    
*   [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    

### Videos

*   [How to enter times in Excel](https://exceljet.net/videos/how-to-enter-times-in-excel)
    
*   [How to use time formatting in Excel](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)
    
*   [How to use date formatting in Excel](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)
    

### Articles

*   [How to use the MOD function to repeat values](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values)
    

### Links

*   [An Introduction to Modular Math (Khan Academy)](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)
    
*   [Calculating working hours (Chandoo video)](http://chandoo.org/wp/2015/06/22/calculating-billys-total-working-hours/)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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
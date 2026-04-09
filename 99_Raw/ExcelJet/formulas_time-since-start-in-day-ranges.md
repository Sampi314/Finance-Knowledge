# Time since start in day ranges - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/time-since-start-in-day-ranges

---

[Skip to main content](https://exceljet.net/formulas/time-since-start-in-day-ranges#main-content)

[](https://exceljet.net/formulas/time-since-start-in-day-ranges#)

*   [Previous](https://exceljet.net/formulas/time-in-hundredths-of-a-second)
    
*   [Next](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Time since start in day ranges
==============================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[IFS](https://exceljet.net/functions/ifs-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Time since start in day ranges](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/time%20since%20start%20in%20day%20ranges.png "Excel formula: Time since start in day ranges")

Summary
-------

To calculate time durations and display the result in days with custom labels, you can use the [IFS function](https://exceljet.net/functions/ifs-function)
. In the example shown, the formula in E5, copied down, is:

    =IFS(C5<=24,"Day 0",C5<=48,"Day 1",C5<=72,"Day 2",C5>72,"Day 3+")
    

**Start** is the [named range](https://exceljet.net/glossary/named-range)
 G5, which is used by formulas in columns C and D, as explained below.

Explanation 
------------

In this example, the goal is to calculate durations in "days" starting from the start date and time in cell G5 and ending at the dates and times shown in column B. The twist is that we want to classify the durations using the custom labels shown in column E, starting with "Day 0" for the first 24 hours and ending at "Day 3+" for durations greater than 72 hours. 

The first step is to [calculate the decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
 as seen in column C. We could also work with [Excel time](https://exceljet.net/glossary/excel-time)
, but decimal hours are more convenient when we calculate the day labels later below. The formula in C5, copied down, is:

    =(B5-start)*24
    

We subtract the start time from the end time and multiply by 24. This works because [Excel times are fractional values of days](https://exceljet.net/glossary/excel-time)
.

Next, we calculate the decimal days that appear in column D by subtracting the start time from the end time. The formula in D5, copied down, is:

    =B5-start
    

This works because [Excel dates are just serial numbers](https://exceljet.net/glossary/excel-date)
. These values are only for reference, and are not used in any subsequent calculations.

Finally, to calculate the day labels as seen in column E, we use a formula based on the [IFS function](https://exceljet.net/functions/ifs-function)
 with 4 logical conditions:

    =IFS(C5<=24,"Day 0",C5<=48,"Day 1",C5<=72,"Day 2",C5>72,"Day 3+")
    

For each [logical test](https://exceljet.net/glossary/logical-test)
, we supply a text value that works like a bucket to collect times the appropriate day range. The IFS function is new in Excel 2019. If you don't have IFS available in your version of Excel, you can use a formula that "nests" together several [IF functions](https://exceljet.net/videos/the-if-function)
:

    =IF(C5<=24,"Day 0",IF(C5<=48,"Day 1",IF(C5<=72,"Day 2",IF(C5>72,"Day 3+"))))
    

For more information on nesting IFs, see: [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
.

Related formulas
----------------

[![Excel formula: Add decimal hours to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_hours_to_time.png "Excel formula: Add decimal hours to time")](https://exceljet.net/formulas/add-decimal-hours-to-time)

### [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)

In this example, the goal is to add hours in decimal format (i.e. 1, 2, 3, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.25 makes sense when you consider that 6 hours is one-quarter of a day, and a day in Excel equals 1. But it isn't...

[![Excel formula: Add decimal minutes to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_minutes_to_time.png "Excel formula: Add decimal minutes to time")](https://exceljet.net/formulas/add-decimal-minutes-to-time)

### [Add decimal minutes to time](https://exceljet.net/formulas/add-decimal-minutes-to-time)

In this example, the goal is to add minutes in decimal format (i.e., 1, 5, 10, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.0104167 makes sense when you consider that 15 minutes is 1/96th of a day, and a day in Excel equals 1. But it...

[![Excel formula: Convert decimal minutes to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20minutes%20to%20excel%20time.png "Excel formula: Convert decimal minutes to Excel time")](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

### [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Minutes Value Time 1 1/24 60 0.04167 1:00 3 3/24 180 0.125 3:00 6 6/24 360 0.25 6:00 4 4/24 240 0.167 4:00 8 8/24 480 0.333 8:00 12 12/24 720 0.5 12:00 18...

[![Excel formula: Convert decimal hours to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20hours%20to%20excel%20time.png "Excel formula: Convert decimal hours to Excel time")](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

### [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Value Time 1 1/24 0.04167 1:00 3 3/24 0.125 3:00 6 6/24 0.25 6:00 4 4/24 0.167 4:00 8 8/24 0.333 8:00 12 12/24 0.5 12:00 18 18/24 0.75 18:00 21 21/24 0...

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Get days, hours, and minutes between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20hours%20and%20minutes%20between%20dates2.png "Excel formula: Get days, hours, and minutes between dates")](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

### [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

Most of the work in this formula is done by the TEXT function, which applies a custom number format for hours and minutes to a value created by subtracting the start date from the end date. TEXT(C5-B5,"h"" hrs ""m"" mins """) This is an example of embedding text into a custom number format, and...

[![Excel formula: Time duration with days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time%20duration%20with%20days.png "Excel formula: Time duration with days")](https://exceljet.net/formulas/time-duration-with-days)

### [Time duration with days](https://exceljet.net/formulas/time-duration-with-days)

In the example shown, the goal is to enter a valid time based on days, hours, and minutes, then display the result as total hours. The key is to understand that time in Excel is just a number. 1 day = 24 hours , and 1 hour = 0.0412 (1/24). That means 12 hours = 0.5, 6 hours = 0.25, and so on...

Related functions
-----------------

[![Excel IFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ifs.png "Excel IFS function")](https://exceljet.net/functions/ifs-function)

### [IFS Function](https://exceljet.net/functions/ifs-function)

The Excel IFS function can run multiple tests and return a value corresponding to the first TRUE result. Use the IFS function to evaluate multiple conditions without multiple nested IF statements. IFS allows shorter, easier to read formulas....

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)
    
*   [Add decimal minutes to time](https://exceljet.net/formulas/add-decimal-minutes-to-time)
    
*   [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)
    
*   [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)
    
*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)
    
*   [Time duration with days](https://exceljet.net/formulas/time-duration-with-days)
    

### Functions

*   [IFS Function](https://exceljet.net/functions/ifs-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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
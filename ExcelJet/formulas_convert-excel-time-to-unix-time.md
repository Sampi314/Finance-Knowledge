# Convert Excel time to Unix time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-excel-time-to-unix-time

---

[Skip to main content](https://exceljet.net/formulas/convert-excel-time-to-unix-time#main-content)

[](https://exceljet.net/formulas/convert-excel-time-to-unix-time#)

*   [Previous](https://exceljet.net/formulas/convert-excel-time-to-decimal-seconds)
    
*   [Next](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert Excel time to Unix time
===============================

by Dave Bruns · Updated 6 Dec 2021

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

![Excel formula: Convert Excel time to Unix time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20Excel%20time%20to%20Unix%20time%20stamp.png "Excel formula: Convert Excel time to Unix time")

Summary
-------

To convert a time in Excel's format to a Unix time stamp, you can use a formula based on the DATE function. In the example shown, the formula in C5 is:

    =(B5-DATE(1970,1,1))*86400
    

Generic formula
---------------

    =(A1-DATE(1970,1,1))*86400

Explanation 
------------

The [Unix time stamp](http://en.wikipedia.org/wiki/Unix_time)
 tracks time as a running count of seconds. The count begins at the "Unix Epoch" on January 1st, 1970, so a Unix time stamp is simply the total seconds between any given date and the Unix Epoch. Since a day contains 86400 seconds (24 hours x 60 minutes x 60 seconds), conversion to Excel time can be done by subtracting the date value for the Unix Epoch and multiplying days by 86400.

In the example shown, the formula first subtracts the date value for January 1, 1970 from the date value in B5 to get the number of days between the dates, then multiplies the result by 85400 to convert to a Unix time stamp. The formula evaluates like this:

    =(B5-DATE(1970,1,1))*86400
    =(43374-25569)*86400
    =1538352000
    

### How Excel tracks dates and time

The Excel date system starts on January 1, 1900 and counts forward. The table below shows the numeric values associated with a few random dates:

| Date | Raw value |
| --- | --- |
| 1-Jan-1900 | 1   |
| 28-Jul-1914 00:00 | 5323 |
| 1-Jan-1970 00:00 | 25569 |
| 31-Dec-1999 | 36525 |
| 1-Oct-2018 | 43374 |
| 1-Oct-2018 12:00 PM | 43374.5 |

Notice the last date includes a time as well. Since one day equals 1, and one day equals 24 hours, time in Excel can represented as fractional values of 1, as shown in the table below. In order to see the value displayed as a time, a [time format](https://exceljet.net/articles/custom-number-formats)
 needs to be applied.

| Hours | Time | Fraction | Value |
| --- | --- | --- | --- |
| 3   | 3:00 AM | 3/24 | 0.125 |
| 6   | 6:00 AM | 6/24 | 0.25 |
| 4   | 4:00 AM | 4/24 | 0.167 |
| 8   | 8:00 AM | 8/24 | 0.333 |
| 12  | 12:00 PM | 12/24 | 0.5 |
| 18  | 6:00 PM | 18/24 | 0.75 |
| 21  | 9:00 PM | 21/24 | 0.875 |
| 24  | 12:00 AM | 24/24 | 1   |

Related formulas
----------------

[![Excel formula: Convert Unix time stamp to Excel date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20unix%20time%20stamp%20to%20excel%20date.png "Excel formula: Convert Unix time stamp to Excel date")](https://exceljet.net/formulas/convert-unix-time-stamp-to-excel-date)

### [Convert Unix time stamp to Excel date](https://exceljet.net/formulas/convert-unix-time-stamp-to-excel-date)

The Unix time stamp tracks time as a running count of seconds. The count begins at the "Unix Epoch" on January 1st, 1970, so a Unix timestamp is simply the total seconds between any given date and the Unix Epoch. Since a day contains 86400 seconds (24 hours x 60 minutes x 60 seconds), conversion to...

[![Excel formula: Timesheet overtime calculation formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20overtime%20calculation.png "Excel formula: Timesheet overtime calculation formula")](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

### [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

Note: it's important to understand that Excel deals with time as fractions of a day . So, 12:00 PM is .5, 6:00 AM is .25, 6 PM is .75, and so on. This works fine for standard time and date calculations, but in many cases you'll want to convert times to decimal hours to make other calculations more...

[![Excel formula: Convert time to time zone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20time%20to%20time%20zone.png "Excel formula: Convert time to time zone")](https://exceljet.net/formulas/convert-time-to-time-zone)

### [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)

Times in Excel are fractional values of the number 1 . So, 12 PM is 12/24 = .5, 6:00 AM is 6/24 = .25, and so on. So, to convert a time by a given number, you need to divide the number of hours by 24 to get required decimal value: E5/24 // convert adjustment to Excel time We add the result to the...

[![Excel formula: Get days, hours, and minutes between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20hours%20and%20minutes%20between%20dates2.png "Excel formula: Get days, hours, and minutes between dates")](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

### [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

Most of the work in this formula is done by the TEXT function, which applies a custom number format for hours and minutes to a value created by subtracting the start date from the end date. TEXT(C5-B5,"h"" hrs ""m"" mins """) This is an example of embedding text into a custom number format, and...

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Convert Excel time to decimal seconds](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20time%20to%20decimal%20seconds.png "Excel formula: Convert Excel time to decimal seconds")](https://exceljet.net/formulas/convert-excel-time-to-decimal-seconds)

### [Convert Excel time to decimal seconds](https://exceljet.net/formulas/convert-excel-time-to-decimal-seconds)

In the Excel time system, one 24-hour day is equal to 1. This means times and hours are fractional values of 1, as shown in the table below: Hours Time Fraction Value 1 1:00 AM 1/24 0.04167 3 3:00 AM 3/24 0.125 6 6:00 AM 6/24 0.25 4 4:00 AM 4/24 0.167 8 8:00 AM 8/24 0.333 12 12:00 PM 12/24 0.5 18 6...

Related functions
-----------------

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

*   [Convert Unix time stamp to Excel date](https://exceljet.net/formulas/convert-unix-time-stamp-to-excel-date)
    
*   [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)
    
*   [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)
    
*   [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)
    
*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Convert Excel time to decimal seconds](https://exceljet.net/formulas/convert-excel-time-to-decimal-seconds)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    

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
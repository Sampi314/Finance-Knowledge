# Time duration with days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/time-duration-with-days

---

[Skip to main content](https://exceljet.net/formulas/time-duration-with-days#main-content)

[](https://exceljet.net/formulas/time-duration-with-days#)

*   [Previous](https://exceljet.net/formulas/sum-time-with-sumifs)
    
*   [Next](https://exceljet.net/formulas/time-in-hundredths-of-a-second)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Time duration with days
=======================

by Dave Bruns · Updated 11 Jul 2022

Related functions 
------------------

[TIME](https://exceljet.net/functions/time-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6344/download?token=i7xfNOhJ)
 (14.26 KB)

![Excel formula: Time duration with days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/time%20duration%20with%20days.png "Excel formula: Time duration with days")

Summary
-------

To enter a time duration like 2 days 6 hours and 30 minutes into Excel, you can enter days separately as a decimal value, then add the time. In the example shown, the formula in cell F5, copied down, is:

    =B5+TIME(C5,D5,0)
    

Generic formula
---------------

    =days+time

Explanation 
------------

In the example shown, the goal is to enter a valid time based on days, hours, and minutes, then display the result as total hours.

The key is to understand that time in Excel is just a number. [1 day = 24 hours](https://exceljet.net/glossary/excel-time)
, and 1 hour = 0.0412 (1/24). That means 12 hours = 0.5, 6 hours = 0.25, and so on. Because time is just a number, you can add time to days and display the result using a custom number format, or with your own formula, as explained below.

In the example shown, the formula in cell F5 is:

    =B5+TIME(C5,D5,0)
    

On the right side of the formula, the [TIME function](https://exceljet.net/functions/time-function)
 is used to assemble a valid time from its component parts (hours, minutes, seconds). Hours come from column C, minutes from column D, and seconds are hardcoded as zero. TIME returns 0.5, since 12 hours equals one half day:

    TIME(12,0,0) // returns 0.5
    

With the number 1 in C5, we can simplify the formula to:

    =1+0.5
    

which returns 1.5 as a final result. To display this result as total hours, a [custom number format](https://exceljet.net/articles/custom-number-formats)
 is used:

    [h]:mm
    

The square brackets tell Excel to display hours over 24, since by default Excel will reset to zero at each 24 hour interval (like a clock). The result is a time like "36:00", since 1.5 is a day and a half, or 36 hours.

The formula in G5 simply points back to F5:

    =F5
    

The custom number format used to display a result like "1d 12h 0m" is:

    d"d" h"h" m"m"
    

### More than 31 days

Using "d" to display days in a [custom number format](https://exceljet.net/articles/custom-number-formats)
 works fine up to 31 days. However, after 31 days, Excel will reset days to zero. This does not affect hours, which will continue to display properly with the number format \[h\].

Unfortunately, a custom number format like \[d\] is not supported. However, in this example, since days, hours, and minutes are already broken out separately, you can write your own formula to display days, minutes, and hours like this:

    =B5&"d "&C5&"h "&D5&"m"
    

This is an example of [concatenation](https://exceljet.net/glossary/concatenation)
. We are simply embedding all three numeric values into single [text string](https://exceljet.net/glossary/text-value)
, joined together with the ampersand (&) [operator](https://exceljet.net/glossary/math-operators)
.

If you want to display an _existing_ time value as a text string, you can use a formula like this:

    =INT(A1)&" days "&TEXT(A1,"h"" hrs ""m"" mins """)
    

where A1 contains time. The [INT function](https://exceljet.net/functions/int-function)
 simply returns the integer portion of the number (days). The [TEXT function](https://exceljet.net/functions/text-function)
 is used to format hours and minutes. 

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

Related functions
-----------------

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

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
    

### Functions

*   [TIME Function](https://exceljet.net/functions/time-function)
    

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
# Convert Excel time to decimal minutes - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-excel-time-to-decimal-minutes

---

[Skip to main content](https://exceljet.net/formulas/convert-excel-time-to-decimal-minutes#main-content)

[](https://exceljet.net/formulas/convert-excel-time-to-decimal-minutes#)

*   [Previous](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
    
*   [Next](https://exceljet.net/formulas/convert-excel-time-to-decimal-seconds)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert Excel time to decimal minutes
=====================================

by Dave Bruns · Updated 21 Sep 2018

![Excel formula: Convert Excel time to decimal minutes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20time%20to%20decimal%20minutes.png "Excel formula: Convert Excel time to decimal minutes")

Summary
-------

To convert a valid Excel time into decimal minutes, you can multiply by 1440. In the example shown, the formula in C6 is:

    =B6*1440
    

which returns a value of 30.

Generic formula
---------------

    =A1*1440

Explanation 
------------

In the Excel time system, one 24-hour day is equal to 1. This means times and hours are fractional values of 1, as shown in the table below:

| Hours | Time | Fraction | Value |
| --- | --- | --- | --- |
| 1   | 1:00 AM | 1/24 | 0.04167 |
| 3   | 3:00 AM | 3/24 | 0.125 |
| 6   | 6:00 AM | 6/24 | 0.25 |
| 4   | 4:00 AM | 4/24 | 0.167 |
| 8   | 8:00 AM | 8/24 | 0.333 |
| 12  | 12:00 PM | 12/24 | 0.5 |
| 18  | 6:00 PM | 18/24 | 0.75 |
| 21  | 9:00 PM | 21/24 | 0.875 |

Because each hour can be represented as 1/24, you can convert an Excel time into decimal hours by multiplying the value by 24, and convert to decimal minutes by multiplying the value by 1440 (24 \* 60) . With the time value 6:00 cell A1, you can visualize the conversion like this:

    =A1*(24*60)
    =(6/24)*1440
    =0.25*1440
    =360
    

The Excel time 6:00 converts to 360 minutes.

### Format result as number

When you multiply a time value by 1440, Excel may automatically format the result using a time format like h:mm, which will display the value incorrectly. To display the result as a regular number, apply the [General or Number format](https://exceljet.net/articles/custom-number-formats)
.

Related formulas
----------------

[![Excel formula: Convert Excel time to decimal hours](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20excel%20time%20to%20decimal%20hours.png "Excel formula: Convert Excel time to decimal hours")](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

### [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

In the Excel time system, one 24-hour day is equal to 1. This means times and hours are fractional values of 1, as shown in the table below: Hours Time Fraction Value 1 1:00 AM 1/24 0.04167 3 3:00 AM 3/24 0.125 6 6:00 AM 6/24 0.25 4 4:00 AM 4/24 0.167 8 8:00 AM 8/24 0.333 12 12:00 PM 12/24 0.5 18 6...

[![Excel formula: Convert decimal hours to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20hours%20to%20excel%20time.png "Excel formula: Convert decimal hours to Excel time")](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

### [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Value Time 1 1/24 0.04167 1:00 3 3/24 0.125 3:00 6 6/24 0.25 6:00 4 4/24 0.167 4:00 8 8/24 0.333 8:00 12 12/24 0.5 12:00 18 18/24 0.75 18:00 21 21/24 0...

[![Excel formula: Convert decimal minutes to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20minutes%20to%20excel%20time.png "Excel formula: Convert decimal minutes to Excel time")](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

### [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Minutes Value Time 1 1/24 60 0.04167 1:00 3 3/24 180 0.125 3:00 6 6/24 360 0.25 6:00 4 4/24 240 0.167 4:00 8 8/24 480 0.333 8:00 12 12/24 720 0.5 12:00 18...

[![Excel formula: Convert decimal seconds to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20seconds%20to%20excel%20time.png "Excel formula: Convert decimal seconds to Excel time")](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time)

### [Convert decimal seconds to Excel time](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Minutes Seconds Value Time 1 1/24 60 3600 0.04167 1:00 3 3/24 180 10800 0.125 3:00 6 6/24 360 21600 0.25 6:00 12 12/24 720 43200 0.5 12:00 18 18/24 1080...

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Add decimal hours to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_hours_to_time.png "Excel formula: Add decimal hours to time")](https://exceljet.net/formulas/add-decimal-hours-to-time)

### [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)

In this example, the goal is to add hours in decimal format (i.e. 1, 2, 3, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.25 makes sense when you consider that 6 hours is one-quarter of a day, and a day in Excel equals 1. But it isn't...

[![Excel formula: Timesheet overtime calculation formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20overtime%20calculation.png "Excel formula: Timesheet overtime calculation formula")](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

### [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

Note: it's important to understand that Excel deals with time as fractions of a day . So, 12:00 PM is .5, 6:00 AM is .25, 6 PM is .75, and so on. This works fine for standard time and date calculations, but in many cases you'll want to convert times to decimal hours to make other calculations more...

[![Excel formula: Get days, hours, and minutes between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20hours%20and%20minutes%20between%20dates2.png "Excel formula: Get days, hours, and minutes between dates")](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

### [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)

Most of the work in this formula is done by the TEXT function, which applies a custom number format for hours and minutes to a value created by subtracting the start date from the end date. TEXT(C5-B5,"h"" hrs ""m"" mins """) This is an example of embedding text into a custom number format, and...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
    
*   [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)
    
*   [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)
    
*   [Convert decimal seconds to Excel time](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time)
    
*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)
    
*   [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)
    
*   [Get days, hours, and minutes between dates](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates)
    

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
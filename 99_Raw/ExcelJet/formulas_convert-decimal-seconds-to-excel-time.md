# Convert decimal seconds to Excel time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time

---

[Skip to main content](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time#main-content)

[](https://exceljet.net/formulas/convert-decimal-seconds-to-excel-time#)

*   [Previous](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)
    
*   [Next](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert decimal seconds to Excel time
=====================================

by Dave Bruns · Updated 24 Sep 2018

![Excel formula: Convert decimal seconds to Excel time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20decimal%20seconds%20to%20excel%20time.png "Excel formula: Convert decimal seconds to Excel time")

Summary
-------

To convert seconds in decimal format to a proper Excel time, divide by 86400. In the example shown, the formula in C6 is:

    =B6/86400
    

To display the result as time, apply a time format. Column D shows the same result formatted with \[h\]:mm.

Generic formula
---------------

    =seconds/86400

Explanation 
------------

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below:

| Hours | Fraction | Minutes | Seconds | Value | Time |
| --- | --- | --- | --- | --- | --- |
| 1   | 1/24 | 60  | 3600 | 0.04167 | 1:00 |
| 3   | 3/24 | 180 | 10800 | 0.125 | 3:00 |
| 6   | 6/24 | 360 | 21600 | 0.25 | 6:00 |
| 12  | 12/24 | 720 | 43200 | 0.5 | 12:00 |
| 18  | 18/24 | 1080 | 64800 | 0.75 | 18:00 |
| 24  | 24/24 | 1440 | 86400 | 1.0 | 21:00 |

Since there are 24 hours in a day, 60 minutes in each hour, and 60 seconds in each minute, you need to divide by 24 \* 60 \* 60 = 86400 in order to convert decimal seconds to a value that Excel will recognize as time. After dividing by 86400, you can apply a time format of your choice, or use the result in a math operation with other dates or times.

In the example, since B11 contains 43200 (representing 43200 seconds, or a half day) the result is 43200/86400 = 0.5. Once a time format like h:mm or \[h\]:mm is applied, Excel will display 12:00.

### Displaying a time duration

To display hours that represent a duration longer than 24 hours, minutes in durations longer than 60 minutes, or seconds in durations over 60 seconds, you'll need to adjust the number format by adding square brackets.

    [h]  // for hours greater than 24
    [m]  // for minutes greater than 60
    [s]  // for seconds greater than 60
    

The brackets tell to Excel the time is a duration, and not a time of day.

_Note: to use square brackets, you'll need to create and apply a [custom number format](https://exceljet.net/articles/custom-number-formats)
. Select cells, then go to Format Cells (Control + 1) > Number > Custom._

Related formulas
----------------

[![Excel formula: Convert decimal hours to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20hours%20to%20excel%20time.png "Excel formula: Convert decimal hours to Excel time")](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

### [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Value Time 1 1/24 0.04167 1:00 3 3/24 0.125 3:00 6 6/24 0.25 6:00 4 4/24 0.167 4:00 8 8/24 0.333 8:00 12 12/24 0.5 12:00 18 18/24 0.75 18:00 21 21/24 0...

[![Excel formula: Convert decimal minutes to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20minutes%20to%20excel%20time.png "Excel formula: Convert decimal minutes to Excel time")](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

### [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Minutes Value Time 1 1/24 60 0.04167 1:00 3 3/24 180 0.125 3:00 6 6/24 360 0.25 6:00 4 4/24 240 0.167 4:00 8 8/24 480 0.333 8:00 12 12/24 720 0.5 12:00 18...

[![Excel formula: Add decimal hours to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_hours_to_time.png "Excel formula: Add decimal hours to time")](https://exceljet.net/formulas/add-decimal-hours-to-time)

### [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)

In this example, the goal is to add hours in decimal format (i.e. 1, 2, 3, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.25 makes sense when you consider that 6 hours is one-quarter of a day, and a day in Excel equals 1. But it isn't...

[![Excel formula: Add decimal minutes to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_minutes_to_time.png "Excel formula: Add decimal minutes to time")](https://exceljet.net/formulas/add-decimal-minutes-to-time)

### [Add decimal minutes to time](https://exceljet.net/formulas/add-decimal-minutes-to-time)

In this example, the goal is to add minutes in decimal format (i.e., 1, 5, 10, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.0104167 makes sense when you consider that 15 minutes is 1/96th of a day, and a day in Excel equals 1. But it...

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)
    
*   [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)
    
*   [Add decimal hours to time](https://exceljet.net/formulas/add-decimal-hours-to-time)
    
*   [Add decimal minutes to time](https://exceljet.net/formulas/add-decimal-minutes-to-time)
    
*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    

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
# Convert time to money - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-time-to-money

---

[Skip to main content](https://exceljet.net/formulas/convert-time-to-money#main-content)

[](https://exceljet.net/formulas/convert-time-to-money#)

*   [Previous](https://exceljet.net/formulas/convert-text-to-date)
    
*   [Next](https://exceljet.net/formulas/convert-time-to-time-zone)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert time to money
=====================

by Dave Bruns · Updated 3 Apr 2020

![Excel formula: Convert time to money](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20time%20to%20money.png "Excel formula: Convert time to money")

Summary
-------

To convert an [Excel time](https://exceljet.net/glossary/excel-time)
 to money based on an hourly rate, first convert the time to a decimal value. In the formula shown, the formula in D5, copied down the table, is:

    =(B5*24)*C5
    

Generic formula
---------------

    =(time*24)*rate

Explanation 
------------

Excel times are stored as [fractional parts of one day](https://exceljet.net/glossary/excel-time)
. For example, 12 hours is equal to 0.5, and 18 hours is equal to 0.75. This means if you try to multiply an Excel time by an hourly rate, you'll get a total far less than expected.

The trick is to first convert the Excel time to a decimal time by multiplying by 24.

    =(B5*24) // returns 1
    

Then you can multiply by the hourly rate:

    =(B5*24)*C5
    =1*C5
    =1*10
    =10
    

Note: technically, the parentheses in the formula above are not needed and added for clarity only.

### Formatting time durations

By default, Excel may display time, even time that represents a duration, using AM/PM. For example, if you have a calculated time of 6 hours, Excel may display this as 6:00 AM. To remove the AM/PM, apply a [custom number format](https://exceljet.net/articles/custom-number-formats)
 like:

    h:mm // display hours and minutes
    

In cases where calculated time exceeds 24 hours, you may want to use a custom format like:

     [h]:mm // display hours > 24
    

The square bracket syntax \[h\] tells Excel to display hour durations of greater than 24 hours. If you don't use the brackets, Excel will simply "roll over" when the duration hits 24 hours (like a clock). This is the time format used in column B in the above example.

Related formulas
----------------

[![Excel formula: Convert Excel time to decimal hours](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20excel%20time%20to%20decimal%20hours.png "Excel formula: Convert Excel time to decimal hours")](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

### [Convert Excel time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)

In the Excel time system, one 24-hour day is equal to 1. This means times and hours are fractional values of 1, as shown in the table below: Hours Time Fraction Value 1 1:00 AM 1/24 0.04167 3 3:00 AM 3/24 0.125 6 6:00 AM 6/24 0.25 4 4:00 AM 4/24 0.167 8 8:00 AM 8/24 0.333 12 12:00 PM 12/24 0.5 18 6...

[![Excel formula: Convert decimal hours to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20hours%20to%20excel%20time.png "Excel formula: Convert decimal hours to Excel time")](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

### [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Value Time 1 1/24 0.04167 1:00 3 3/24 0.125 3:00 6 6/24 0.25 6:00 4 4/24 0.167 4:00 8 8/24 0.333 8:00 12 12/24 0.5 12:00 18 18/24 0.75 18:00 21 21/24 0...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

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
    
*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    

### Training

*   [Core Excel](https://exceljet.net/training/core-excel)
    

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
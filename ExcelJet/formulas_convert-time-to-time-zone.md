# Convert time to time zone - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-time-to-time-zone

---

[Skip to main content](https://exceljet.net/formulas/convert-time-to-time-zone#main-content)

[](https://exceljet.net/formulas/convert-time-to-time-zone#)

*   [Previous](https://exceljet.net/formulas/convert-time-to-money)
    
*   [Next](https://exceljet.net/formulas/convert-unix-time-stamp-to-excel-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert time to time zone
=========================

by Dave Bruns · Updated 13 Dec 2019

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Convert time to time zone](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20time%20to%20time%20zone.png "Excel formula: Convert time to time zone")

Summary
-------

To convert a time from one time zone to another, you can use a formula that converts hours entered as whole numbers to the decimal values that Excel recognizes as times. In the example shown, the formula in F5 is:

    =MOD(C5+(E5/24),1)
    

This formula returns a number that Excel recognizes as 2:00 AM.

Generic formula
---------------

    =MOD(time+(hours/24),1)

Explanation 
------------

[Times in Excel are fractional values of the number 1](https://exceljet.net/glossary/excel-time)
. So, 12 PM is 12/24 = .5, 6:00 AM is 6/24 = .25, and so on. So, to convert a time by a given number, you need to divide the number of hours by 24 to get required decimal value:

    E5/24 // convert adjustment to Excel time
    

We add the result to the starting time:

    C5+(E5/24)
    

To make sure we have a true time value, we need to ensure that we have only a decimal value. In other words, if we add 12 hours (.5) to 6 PM (.75) we'll get 1.25, but we really only want .25.

To make sure we get just the decimal value, we use the [MOD function](https://exceljet.net/functions/mod-function)
 with a divisor of 1, as a clever way to keep the formula simple.

MOD returns the remainder after division, so returns the decimal value in cases where the result is greater than 1 (i.e. greater than 24 hours).

Even better, if we end up with a negative fractional value, MOD returns the reciprocal. So, if we end up with -.25, MOD returns .75 (equivalent to 6 PM).

This is important, because Excel won't display negative time values.

### Datetimes

Some date values include both a date and time, and are sometimes called "datetimes". These values include both a serial number to represent the date, plus a fractional value to represent time. The table below shows some examples:

| Datetime | Raw value |
| --- | --- |
| 3/6/18 6:00 AM | 43165.25 |
| 1-Jan-1999 21:00 | 36161.875 |
| 4/1/2020 0:00 | 43922 |
| June 3, 1980 12:00 PM | 29375.5 |

When working with dates that include both a date and time (datetimes), you don't need to use MOD, because there's no need to do anything clever as times cross midnight. The operation becomes simple addition, because the date is included, and you can use a formula like this:

    =datetime+(hours/24)
    

This will allow the date value change as needed (forwards or backwards) when time adjustments cross 12:00 AM.

Related formulas
----------------

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

Related functions
-----------------

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    
*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    
*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    

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
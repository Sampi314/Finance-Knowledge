# Add decimal hours to time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-decimal-hours-to-time

---

[Skip to main content](https://exceljet.net/formulas/add-decimal-hours-to-time#main-content)

[](https://exceljet.net/formulas/add-decimal-hours-to-time#)

*   [Previous](https://exceljet.net/formulas/add-days-to-date)
    
*   [Next](https://exceljet.net/formulas/add-decimal-minutes-to-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Add decimal hours to time
=========================

by Dave Bruns · Updated 9 Jul 2024

Related functions 
------------------

[TIME](https://exceljet.net/functions/time-function)

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Add decimal hours to time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add_decimal_hours_to_time.png "Excel formula: Add decimal hours to time")

Summary
-------

To add a given number of hours to an [Excel time](https://exceljet.net/glossary/excel-time)
, you can add the hours divided by 24. In the example shown, the formula in E5 is:

    =B5+(C5/24)
    

As the formula is copied down, it adds the decimal hours in column C to the times in column B. The results in column E are formatted with the custom number format "h:mm AM/PM".

Generic formula
---------------

    =A1+(hours/24)

Explanation 
------------

In this example, the goal is to add hours in decimal format (i.e. 1, 2, 3, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.25 makes sense when you consider that 6 hours is one-quarter of a day, and a day in Excel equals 1. But it isn't the way most people think about time. To add decimal hours to a time, we need to first convert the hours to an equivalent fractional value.

### How Excel tracks time

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
, so a single day has a numeric value of 1. As a result, time is a fractional value of 1 and 1 hour = 1/24 = 0.041666667. This means that 6 hours is one-quarter of a day (0.25), 12 hours is half a day (0.5), 18 hours is three-quarters of a day (0.75), and 24 hours is 1 day. In the same way, 6:00 AM has a numeric value of 0.25, 12:00 PM has a value of 0.5, and 6:00 PM has a value of 0.75. The table below summarizes this relationship:

| Hours | Time | Fraction | Value |
| --- | --- | --- | --- |
| 0   | 12:00 AM | 0/24 | 0   |
| 3   | 3:00 AM | 3/24 | 0.125 |
| 6   | 6:00 AM | 6/24 | 0.25 |
| 4   | 4:00 AM | 4/24 | 0.167 |
| 8   | 8:00 AM | 8/24 | 0.333 |
| 12  | 12:00 PM | 12/24 | 0.5 |
| 18  | 6:00 PM | 18/24 | 0.75 |
| 21  | 9:00 PM | 21/24 | 0.875 |
| 24  | 12:00 AM | 24/24 | 1.0\* |

_\* In Excel, midnight (12:00 AM) has a dual nature: it has a value of 0 when it represents the start of a day, but it can be 1 inside a calculation t_hat completes a full 24-hour cycle. In other words, as we approach midnight, the value of time approaches 1. But as we cross from one day to another, the 1 is added to the date, and time begins again at zero.__

### Adding decimal hours to a time

Because Excel stores time as fractional values, we need to convert decimal hours to a valid time before addition. To do this, we simply divide the hours by 24. For example, with an Excel time in cell A1, we can add 3, 6, 12, and 18 hours like this:

    =A1+(3/24) // add 3 hours
    =A1+(6/24) // add 6 hours
    =A1+(12/24) // add 12 hours
    =A1+(18/24) // add 18 hours

In the example shown, the formula in cell E5 uses the same idea above like this:

    =B5+(C5/24)

As the formula is copied down, it adds the decimal hours in column C to the times in column B. The results in column E are formatted with the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "h:mm AM/PM".

### With the TIME function

You can also add time values with the [TIME function](https://exceljet.net/functions/time-function)
. To add 15 hours to a time in A1, use:

    =A1+TIME(6,0,0)
    

The TIME function saves you from having to remember the formula for converting decimal hours to an Excel time. However, note that the TIME function only supports time spans up to 24 hours. Every 24 hours, the time will reset to zero like a clock. For example, the formulas below show what happens if we use 25 hours:

    =TIME(25,0,0) = 0.041667 = 1:00 AM same day (1 hr)
    =25/24 = 1.041667 = 1:00 AM next day (25 hrs)
    

The TIME function returns the equivalent of 1 hour, while =25/24 returns the full value.

### Subtracting hours from time

You may get an error if you try to subtract hours from a time when the result is negative because Excel doesn't support negative time values. One way to avoid this problem is to use a formula like this:

    =MOD(time-(hours/24),1)
    

Here, the MOD function takes care of the negative problem by using the MOD function to "flip" negative values to the required positive value. Another way to avoid this problem is to start with a time that includes a date. This lets you subtract very large numbers of hours without any danger of getting a negative result. If you don't want to see the date displayed in the result, just apply a time-only number format. For a more detailed discussion of this topic see [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
.

### Working with dates + times

A good way to simplify formulas and avoid negative time values is to use a date that includes a time value, sometimes called a "[datetime](https://exceljet.net/glossary/excel-datetime)
", as the starting value. This lets you subtract a large number of hours without the danger of getting a negative result. You can see how this works in the worksheet below, where the values in column B contain a date and a time. The formula in cell E5 is the same as the original above:

    =B5+(C5/24)

![Adding hours to dates with times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/add_decimal_hours_to_dates_with_times.png "Adding hours to dates with times")

Because values in column B contain a date, the numbers are very large. For example, the numeric value in cell B5 is 45474.3333. As a result, we are able to add or subtract a large number of hours with one simple formula. Notice the results in rows 14-16 are valid and work fine. All values in columns B and E are formatted with the same custom number format:

    d-mmm hh:mm

You can [customize](https://exceljet.net/articles/custom-number-formats)
 this format in any way you like.

Related formulas
----------------

[![Excel formula: Add decimal minutes to time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_decimal_minutes_to_time.png "Excel formula: Add decimal minutes to time")](https://exceljet.net/formulas/add-decimal-minutes-to-time)

### [Add decimal minutes to time](https://exceljet.net/formulas/add-decimal-minutes-to-time)

In this example, the goal is to add minutes in decimal format (i.e., 1, 5, 10, etc.) to an existing Excel time. The complication is that Excel stores time as fractional values. The number 0.0104167 makes sense when you consider that 15 minutes is 1/96th of a day, and a day in Excel equals 1. But it...

[![Excel formula: Convert decimal minutes to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20minutes%20to%20excel%20time.png "Excel formula: Convert decimal minutes to Excel time")](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

### [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Minutes Value Time 1 1/24 60 0.04167 1:00 3 3/24 180 0.125 3:00 6 6/24 360 0.25 6:00 4 4/24 240 0.167 4:00 8 8/24 480 0.333 8:00 12 12/24 720 0.5 12:00 18...

[![Excel formula: Convert decimal hours to Excel time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20decimal%20hours%20to%20excel%20time.png "Excel formula: Convert decimal hours to Excel time")](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

### [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)

In the Excel date system, one day is equal to 1, so you can think of time as fractional values of 1, as shown in the table below: Hours Fraction Value Time 1 1/24 0.04167 1:00 3 3/24 0.125 3:00 6 6/24 0.25 6:00 4 4/24 0.167 4:00 8 8/24 0.333 8:00 12 12/24 0.5 12:00 18 18/24 0.75 18:00 21 21/24 0...

Related functions
-----------------

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_time_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)

### [How to use time formatting in Excel](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)

In this lesson we'll look at the Time format. Like the Date format, the Time format includes a number of built-in options for displaying time. Let's take a look. Here we have a set of times in column B of our table. Let's start off by copying these times to all columns, then adjust formats to match...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add decimal minutes to time](https://exceljet.net/formulas/add-decimal-minutes-to-time)
    
*   [Convert decimal minutes to Excel time](https://exceljet.net/formulas/convert-decimal-minutes-to-excel-time)
    
*   [Convert decimal hours to Excel time](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)
    

### Functions

*   [TIME Function](https://exceljet.net/functions/time-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    

### Videos

*   [How to use time formatting in Excel](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)
    

### Links

*   [An Introduction to Modular Math (Khan Academy)](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)
    

### Training

*   [Core Excel](https://exceljet.net/training/core-excel)
    
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
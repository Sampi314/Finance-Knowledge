# Excel WEEKDAY function | Exceljet

**Source:** https://exceljet.net/functions/weekday-function

---

[Skip to main content](https://exceljet.net/functions/weekday-function#main-content)

[](https://exceljet.net/functions/weekday-function#)

*   [Previous](https://exceljet.net/functions/today-function)
    
*   [Next](https://exceljet.net/functions/weeknum-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

WEEKDAY Function
================

by Dave Bruns · Updated 16 Jul 2021

![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")

Summary
-------

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

Purpose 
--------

Get the day of the week as a number

Return value 
-------------

A number between 0 and 7.

Syntax
------

    =WEEKDAY(serial_number,[return_type])

*   _serial\_number_ - The date for which you want to get the day of week.
*   _return\_type_ - \[optional\] A number representing day of week mapping scheme. Default is 1.

Using the WEEKDAY function 
---------------------------

The WEEKDAY function takes a date and returns a number between 1-7 representing the day of the week. The WEEKDAY function takes two [arguments](https://exceljet.net/glossary/function-argument)
: _serial\_number_ and _return\_type_. _Serial\_number_ should be a [valid Excel date](https://exceljet.net/glossary/excel-date)
 in serial number format. _Return\_type_ is an optional numeric code that controls which day of the week is considered the first day. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, as seen in the table below:

| Result | Meaning |
| --- | --- |
| 1   | Sunday |
| 2   | Monday |
| 3   | Tuesday |
| 4   | Wednesday |
| 5   | Thursday |
| 6   | Friday |
| 7   | Saturday |

WEEKDAY supports several numbering schemes, controlled by the _return\_type_ argument. _Return\_type_ is optional and defaults to 1. The table below shows available _return\_type_ codes, the numeric result of each code, and which day is the first day in the mapping scheme.

| Return type | Numeric result | Day mapping |
| --- | --- | --- |
| none | 1-7 | Sunday-Saturday |
| 1   | 1-7 | Sunday-Saturday |
| 2   | 1-7 | Monday-Sunday |
| 3   | 0-6 | Monday-Sunday |
| 11  | 1-7 | Monday-Sunday |
| 12  | 1-7 | Tuesday-Monday |
| 13  | 1-7 | Wednesday-Tuesday |
| 14  | 1-7 | Thursday-Wednesday |
| 15  | 1-7 | Friday-Thursday |
| 16  | 1-7 | Saturday-Friday |
| 17  | 1-7 | Sunday-Saturday |

_Note: the WEEKDAY function will return a value even when the date is empty. Take care to trap this result if blank dates are possible._

### Examples

By default and without a value fore _return\_type_, WEEKDAY starts counting on Sunday:

    =WEEKDAY("3-Jan-21") // Sunday, returns 1
    =WEEKDAY("4-Jan-21") // Monday, returns 2
    

To configure WEEKDAY to start on Monday, set _return\_type_ to 2_:_

    =WEEKDAY("3-Jan-21",2) // Sunday, returns 7
    =WEEKDAY("4-Jan-21",2) // Monday, returns 1
    

In the example shown above, the formula in D5 (copied down) is:

    =WEEKDAY(B5) // Sunday start
    

The formula in E5 (copied down) is:

    =WEEKDAY(B5,2) // Monday start
    

### Notes

*   By default, WEEKDAY returns 1 for Sunday and 7 for Saturday.
*   WEEKDAY returns a value (7) even if the date is empty.

WEEKDAY function examples
-------------------------

[![Excel formula: Custom weekday abbreviation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Custom%20weekday%20abbreviation.png "Excel formula: Custom weekday abbreviation")](https://exceljet.net/formulas/custom-weekday-abbreviation)

### [Custom weekday abbreviation](https://exceljet.net/formulas/custom-weekday-abbreviation)

Working from the inside-out, the WEEKDAY function takes a date and returns a number between 1 and 7. With default settings, the number 1 corresponds to Sunday and the number 7 corresponds to Saturday. The CHOOSE function simply maps numbers to values. The first argument is the number to map, and...

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

[![Excel formula: Dynamic calendar formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula_0.png "Excel formula: Dynamic calendar formula")](https://exceljet.net/formulas/dynamic-calendar-formula)

### [Dynamic calendar formula](https://exceljet.net/formulas/dynamic-calendar-formula)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will automatically return the first day of the current month. In this example, the goal is to generate a dynamic calendar for any given month, based on a start date entered in cell J6...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

[![Excel formula: Gantt chart with weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20gantt%20chart%20weekends.png "Excel formula: Gantt chart with weekends")](https://exceljet.net/formulas/gantt-chart-with-weekends)

### [Gantt chart with weekends](https://exceljet.net/formulas/gantt-chart-with-weekends)

The key to this approach is the calendar header (row 4), which is just a series of valid dates, formatted with the custom number format "d". With a hardcoded date in D4, you can use =D4+1 to populate the calendar. This allows you to set up a conditional formatting rule that compares the date in row...

[![Excel formula: Get work hours between dates custom schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20custom2.png "Excel formula: Get work hours between dates custom schedule")](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

### [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

At the core, this formula uses the WEEKDAY function to figure out the day of week (i.e. Monday, Tuesday, etc.) for every day between the two given dates. WEEKDAY returns a number between 1 and 7. With default settings, Sunday=1 and Saturday = 7. The trick to this formula is assembling an array of...

[![Excel formula: Get Monday of the week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20monday%20of%20the%20week.png "Excel formula: Get Monday of the week")](https://exceljet.net/formulas/get-monday-of-the-week)

### [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)

Imagine you have a random date and want to find the Monday of the week in which the date appears. You can see you will need to "roll back" a specific number of days, depending on what day of the week the given date is. If the date is a Wednesday, you need to roll back 2 days, if the date is a...

[![Excel formula: Last n weeks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20n%20weeks_0.png "Excel formula: Last n weeks")](https://exceljet.net/formulas/last-n-weeks)

### [Last n weeks](https://exceljet.net/formulas/last-n-weeks)

In the image shown, the current date is August 24, 2019. Excel dates are serial numbers , so they can be manipulated with simple math operations. The TODAY function always returns the current date. Inside the AND function , the first logical test checks to see if the date in B5 is greater than or...

[![Excel formula: Sequence of weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_weekends.png "Excel formula: Sequence of weekends")](https://exceljet.net/formulas/sequence-of-weekends)

### [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)

The goal is to generate a series of sequential weekend days (Saturday and Sunday) with a formula. The start date is entered in cell B5. The number of dates to create (n) is entered in cell B8. If either of these two values are changed, a new list of weekend dates should be generated. In the current...

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

[![Excel formula: If Monday, roll back to Friday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20Monday%20roll%20back%20to%20Friday_0.png "Excel formula: If Monday, roll back to Friday")](https://exceljet.net/formulas/if-monday-roll-back-to-friday)

### [If Monday, roll back to Friday](https://exceljet.net/formulas/if-monday-roll-back-to-friday)

The WEEKDAY function returns a number, 1-7, that corresponds to particular days of the week. By default, WEEKDAY assumes a Sunday-based week, and assigns 1 to Sunday, 2 to Monday, and so on, with 7 assigned to Saturday. In this case, we only want to take action if the date in question is Monday. To...

[![Excel formula: Get last working day in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20working%20day%20in%20month.png "Excel formula: Get last working day in month")](https://exceljet.net/formulas/get-last-working-day-in-month)

### [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)

Working from the inside out, the EOMONTH function gets the last day of month of any date. To this result, we add 1, which results in the first day of the next month. This date goes into WORKDAY function as the "start date", along with -1 for "days". The WORKDAY function automatically steps back 1...

[![Excel formula: Get next day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_next_day_of_week.png "Excel formula: Get next day of week")](https://exceljet.net/formulas/get-next-day-of-week)

### [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)

In this example, the goal is to get the next specified weekday, starting on a given start date. So for example, with a valid start date in column B, we want to be able to ask for the next Monday, the next Tuesday, the next Wednesday, and so on. This article describes two different ways of solving...

[![Excel formula: Get nth day of week in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get-nth-day-of-week-in-month_0.png "Excel formula: Get nth day of week in month")](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

### [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

This example demonstrates how to calculate the nth occurrence of a specific day of the week within a month. For instance, you might need to find the 2nd Tuesday, the 4th Wednesday, or the 1st Friday of any given month. The worksheet is structured with the starting date in column B, the target day...

[![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")](https://exceljet.net/formulas/count-dates-by-day-of-week)

### [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)

You might wonder why we aren't using COUNTIF or COUNTIFS . These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile...

WEEKDAY function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20group%20a%20pivot%20table%20by%20day%20of%20week-thumb.png)](https://exceljet.net/videos/how-to-group-a-pivot-table-by-day-of-week)

### [How to group a pivot table by day of week](https://exceljet.net/videos/how-to-group-a-pivot-table-by-day-of-week)

Pivot tables are very good at grouping dated information. You can group by year, by month, by quarter, and even by day and hour. But if you want to group by something like day of week, you'll need to do a little prep work in the source data first. Let's take a look. Here we have some raw data for...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)
    
*   [If Monday, roll back to Friday](https://exceljet.net/formulas/if-monday-roll-back-to-friday)
    
*   [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)
    
*   [Custom weekday abbreviation](https://exceljet.net/formulas/custom-weekday-abbreviation)
    
*   [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    
*   [Sum by weekday](https://exceljet.net/formulas/sum-by-weekday)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    
*   [Dynamic calendar formula](https://exceljet.net/formulas/dynamic-calendar-formula)
    
*   [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)
    

### Videos

*   [How to group a pivot table by day of week](https://exceljet.net/videos/how-to-group-a-pivot-table-by-day-of-week)
    

### Links

*   [Microsoft WEEKDAY function documentation](https://support.office.com/en-us/article/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a)
    

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
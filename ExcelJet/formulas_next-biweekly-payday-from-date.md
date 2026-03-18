# Next biweekly payday from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/next-biweekly-payday-from-date

---

[Skip to main content](https://exceljet.net/formulas/next-biweekly-payday-from-date#main-content)

[](https://exceljet.net/formulas/next-biweekly-payday-from-date#)

*   [Previous](https://exceljet.net/formulas/next-anniversary-date)
    
*   [Next](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Next biweekly payday from date
==============================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[CEILING](https://exceljet.net/functions/ceiling-function)

![Excel formula: Next biweekly payday from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/next%20biweekly%20payday%20from%20date.png "Excel formula: Next biweekly payday from date")

Summary
-------

To get the next payday in an every-other-Friday system, you can use a formula based on the [CEILING function](https://exceljet.net/functions/ceiling-function)
. In the example shown, the formula in C6 is:

    =CEILING(B6+1,14)-1

_Note: This formula assumes Excel's default 1900 date system._

Generic formula
---------------

    =CEILING(date+1,14)-1

Explanation 
------------

This formula depends on the [CEILING function](https://exceljet.net/functions/ceiling-function)
, which rounds numbers up to a given multiple. It works because of how dates work in Excel's default 1900 date system, where the first day is the number 1, which is Sunday, January 1, 1900.

In this scheme, the first Friday is day number 6, the second Friday is day number 13, and day 14 is the second Saturday. What this means is that all second Saturdays in the future are evenly divisible by 14.

The formula uses this fact to figure out 2nd Saturdays, then subtracts 1 to get the Friday previous.

### The other Friday

If you need to get the alternate Friday in an every-other-Friday scheme, you can use this version of the formula:

    =CEILING(A1+8,14)-8
    

The idea is the same, but the formula needs to roll forward 8 days to get to an even multiple of 14. Once CEILING returns a date, 8 days are subtracted to move back to the Friday previous.

_Note: I ran into this formula as [an answer on stack overflow](https://stackoverflow.com/questions/18132527/calculate-the-biweekly-pay-period-in-excel-2010)
 by the awesome Barry Houdini._

Related formulas
----------------

[![Excel formula: Next working day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next_working_day.png "Excel formula: Next working day")](https://exceljet.net/formulas/next-working-day)

### [Next working day](https://exceljet.net/formulas/next-working-day)

In the worksheet shown, column B contains 12 dates. The goal is to calculate the next working day after each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. In other words, the formula should automatically skip weekends and any dates defined as non-...

[![Excel formula: Next business day 6 months in future](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20business%20day%206%20months%20in%20future.png "Excel formula: Next business day 6 months in future")](https://exceljet.net/formulas/next-business-day-6-months-in-future)

### [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)

Working from the inside out, EDATE first calculates a date 6 months in the future. In the example shown, that date is December 24, 2015. Next, the formula subtracts 1 day to get December 23, 2015, and the result goes into the WORKDAY function as the start date, with days = 1, and the range B9:B11...

[![Excel formula: Biweekly pay schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/biweekly_pay_schedule.png "Excel formula: Biweekly pay schedule")](https://exceljet.net/formulas/biweekly-pay-schedule)

### [Biweekly pay schedule](https://exceljet.net/formulas/biweekly-pay-schedule)

In this example, the goal is to create a list of pay dates that follow a biweekly schedule. A biweekly pay schedule means employees are paid every two weeks on a given day of the week. Each pay period is 14 days, and there are usually 26 pay dates per year, though occasionally 27 depending on the...

Related functions
-----------------

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Next working day](https://exceljet.net/formulas/next-working-day)
    
*   [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    
*   [Biweekly pay schedule](https://exceljet.net/formulas/biweekly-pay-schedule)
    

### Functions

*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    

### Links

*   [Barry Houdini's answer on stackoverflow](http://stackoverflow.com/questions/18132527/calculate-the-biweekly-pay-period-in-excel-2010)
    

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
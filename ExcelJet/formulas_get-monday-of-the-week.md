# Get Monday of the week - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-monday-of-the-week

---

[Skip to main content](https://exceljet.net/formulas/get-monday-of-the-week#main-content)

[](https://exceljet.net/formulas/get-monday-of-the-week#)

*   [Previous](https://exceljet.net/formulas/get-last-working-day-in-month)
    
*   [Next](https://exceljet.net/formulas/get-month-from-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get Monday of the week
======================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

![Excel formula: Get Monday of the week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20monday%20of%20the%20week.png "Excel formula: Get Monday of the week")

Summary
-------

To get the Monday of the week (i.e. the beginning of a week) for any given date, you can use a formula based on the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. In the example shown, the formula in C6 is:

    =B5-WEEKDAY(B5,3)
    

_Note: In Excel's default scheme, weeks begin on Sunday. However, this example assumes the first day of a week is Monday, which is configured with WEEKDAY's second argument as explained below._

Generic formula
---------------

    =date-WEEKDAY(date,3)

Explanation 
------------

Imagine you have a random date and want to find the Monday of the week in which the date appears. You can see you will need to "roll back" a specific number of days, depending on what day of the week the given date is. If the date is a Wednesday, you need to roll back 2 days, if the date is a Friday, roll back 4 days, and so on, as seen in the table below:

|     |     |
| --- | --- |
| Date | Rollback |
| Monday | 0   |
| Tuesday | 1   |
| Wednesday | 2   |
| Thursday | 3   |
| Friday | 4   |
| Saturday | 5   |
| Sunday | 6   |

How can we calculate the rollback number?

It turns out that the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
, with a small adjustment, can give us the rollback number we need. WEEKDAY returns a number, normally 1-7 for each day of the week. By setting the optional second argument (_return\_type_) to 3, WEEKDAY will return numbers 0-6 for a Monday-based week:

    =WEEKDAY(A1,3) // start week at zero Mondays

This configuration allows us to use WEEKDAY to generate the rollback values in the table above for any given date. The formula exploits this behavior directly:

    =B5-WEEKDAY(B5,3)
    =25-Aug-2019-WEEKDAY(25-Aug-2019,3)
    =25-Aug-2019-6
    =19-Aug-2019
    

### Monday of the current week

To get the Monday of the current week, you can use this formula:

    =TODAY()-WEEKDAY(TODAY(),3)
    

Here, we are using the [TODAY function](https://exceljet.net/functions/today-function)
 to inject the current date into the same formula. This formula will be updated on an ongoing basis.

### Custom alternative

If you want to customize behavior based on the day of the week, you use an alternative formula that uses the [CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)
 with hard-coded adjustment values:

    =B5-CHOOSE(WEEKDAY(B5,2),0,1,2,3,4,5,6)
    

This formula uses WEEKDAY to get an index for the day of the week and CHOOSE to fetch a rollback value. The advantage of this approach is that CHOOSE allows arbitrary values for each day of the week so you can customize the behavior as you like.

Related formulas
----------------

[![Excel formula: If Monday, roll back to Friday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20Monday%20roll%20back%20to%20Friday_0.png "Excel formula: If Monday, roll back to Friday")](https://exceljet.net/formulas/if-monday-roll-back-to-friday)

### [If Monday, roll back to Friday](https://exceljet.net/formulas/if-monday-roll-back-to-friday)

The WEEKDAY function returns a number, 1-7, that corresponds to particular days of the week. By default, WEEKDAY assumes a Sunday-based week, and assigns 1 to Sunday, 2 to Monday, and so on, with 7 assigned to Saturday. In this case, we only want to take action if the date in question is Monday. To...

[![Excel formula: Get next day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_next_day_of_week.png "Excel formula: Get next day of week")](https://exceljet.net/formulas/get-next-day-of-week)

### [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)

In this example, the goal is to get the next specified weekday, starting on a given start date. So for example, with a valid start date in column B, we want to be able to ask for the next Monday, the next Tuesday, the next Wednesday, and so on. This article describes two different ways of solving...

[![Excel formula: Get last weekday in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20weekday%20in%20month.png "Excel formula: Get last weekday in month")](https://exceljet.net/formulas/get-last-weekday-in-month)

### [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)

First, this formula determines the first day of the next month \*after\* a given date. It does this my using EOMONTH to get the last day of the month, then adding one day: =EOMONTH(B5,0)+1 Next, the formula calculates the number of days required to "roll back" to the last requested weekday in the...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")](https://exceljet.net/formulas/get-last-day-of-month)

### [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below. The EOMONTH function The EOMONTH function returns the last day of the...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If Monday, roll back to Friday](https://exceljet.net/formulas/if-monday-roll-back-to-friday)
    
*   [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)
    
*   [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    

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
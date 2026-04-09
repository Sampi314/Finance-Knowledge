# If Monday, roll back to Friday - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-monday-roll-back-to-friday

---

[Skip to main content](https://exceljet.net/formulas/if-monday-roll-back-to-friday#main-content)

[](https://exceljet.net/formulas/if-monday-roll-back-to-friday#)

*   [Previous](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)
    
*   [Next](https://exceljet.net/formulas/join-date-and-text)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

If Monday, roll back to Friday
==============================

by Dave Bruns · Updated 4 Sep 2018

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: If Monday, roll back to Friday](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/If%20Monday%20roll%20back%20to%20Friday_0.png "Excel formula: If Monday, roll back to Friday")

Summary
-------

To check the weekday of a date, and roll back to Friday when the date is a Monday, you can use the IF and WEEKDAY functions. In the example shown, the formula in C5 is

    =IF(WEEKDAY(B5)=2,B5-3,B5)
    

Generic formula
---------------

    =IF(WEEKDAY(date)=2,date-3,date)

Explanation 
------------

The WEEKDAY function returns a number, 1-7, that corresponds to particular days of the week. By default, WEEKDAY assumes a Sunday-based week, and assigns 1 to Sunday, 2 to Monday, and so on, with 7 assigned to Saturday.

In this case, we only want to take action if the date in question is Monday. To test, we use this expression inside the IF function:

    WEEKDAY(B5)=2
    

If the logical expression returns TRUE, we know the date is a Monday, so we subtract 3 to "roll back" to Friday. If the expression returns FALSE, we simply return the original date.

Related formulas
----------------

[![Excel formula: Get next day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_next_day_of_week.png "Excel formula: Get next day of week")](https://exceljet.net/formulas/get-next-day-of-week)

### [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)

In this example, the goal is to get the next specified weekday, starting on a given start date. So for example, with a valid start date in column B, we want to be able to ask for the next Monday, the next Tuesday, the next Wednesday, and so on. This article describes two different ways of solving...

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Next business day 6 months in future](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20business%20day%206%20months%20in%20future.png "Excel formula: Next business day 6 months in future")](https://exceljet.net/formulas/next-business-day-6-months-in-future)

### [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)

Working from the inside out, EDATE first calculates a date 6 months in the future. In the example shown, that date is December 24, 2015. Next, the formula subtracts 1 day to get December 23, 2015, and the result goes into the WORKDAY function as the start date, with days = 1, and the range B9:B11...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Date is workday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_workday.png "Excel formula: Date is workday")](https://exceljet.net/formulas/date-is-workday)

### [Date is workday](https://exceljet.net/formulas/date-is-workday)

In this example, the goal is to test a date to determine whether it is a workday. In Excel, you can use either the WORKDAY function or its more flexible sibling WORKDAY.INTL to accomplish this task. WORKDAY function The WORKDAY function calculates a date in the future or past that is, by definition...

[![Excel formula: Get Monday of the week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20monday%20of%20the%20week.png "Excel formula: Get Monday of the week")](https://exceljet.net/formulas/get-monday-of-the-week)

### [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)

Imagine you have a random date and want to find the Monday of the week in which the date appears. You can see you will need to "roll back" a specific number of days, depending on what day of the week the given date is. If the date is a Wednesday, you need to roll back 2 days, if the date is a...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)
    
*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    
*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Date is workday](https://exceljet.net/formulas/date-is-workday)
    
*   [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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
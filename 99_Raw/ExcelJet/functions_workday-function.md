# Excel WORKDAY function | Exceljet

**Source:** https://exceljet.net/functions/workday-function

---

[Skip to main content](https://exceljet.net/functions/workday-function#main-content)

[](https://exceljet.net/functions/workday-function#)

*   [Previous](https://exceljet.net/functions/weeknum-function)
    
*   [Next](https://exceljet.net/functions/workday.intl-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

WORKDAY Function
================

by Dave Bruns · Updated 3 Jun 2024

Related functions 
------------------

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")

Summary
-------

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates that need to factor in working and non-working days.

Purpose 
--------

Get a date n working days in the future or past

Return value 
-------------

A serial number representing a date in Excel.

Syntax
------

    =WORKDAY(start_date,days,[holidays])

*   _start\_date_ - The date from which to start.
*   _days_ - Working days before or after start\_date.
*   _holidays_ - \[optional\] A list of dates that are non-working days.

Using the WORKDAY function 
---------------------------

The WORKDAY function calculates a date that is a given number of working days from a specified start date, automatically excluding weekends and, optionally, holidays. You can use the WORKDAY function to calculate project start dates, delivery dates, due dates, and other dates that must consider both working and non-working days. Note that WORKDAY will _automatically_ exclude Saturdays and Sundays but will only exclude holidays if they are provided.

The WORKDAY function takes three [arguments](https://exceljet.net/glossary/function-argument)
:

*   _start\_date -_ the date from which to start counting. When calculating a result, WORKDAY _does not_ include the start date as a work day. 
*   _days_ - the number of days in the future or past to calculate a workday. Use a positive number for days to calculate dates in the future, and a negative number for past dates. 
*   _holidays_ - an optional argument to specify non-working dates that should be skipped when computing a result. _Holidays_ must be provided as a range or array that contains valid Excel dates. If holidays are not provided, WORKDAY will treat only Saturdays and Sundays as non-working days. 

### The WORKDAY function explained

To illustrate how WORKDAY works, assume we are scheduling a task that takes 5 working days, starting on Monday, July 1, 2024. The goal is to calculate a date that is 5 working days after July 1, 2024. If we simply add 5 to the start date, Excel will return Saturday, July 6:

    ="1-Jul-2024"+5 // returns "6-Jul-2024"

If however, we use WORKDAY to calculate a date 5 days after July 1, it returns Monday, July 8, 2024:

    =WORKDAY("1-Jul-2024",5) // returns "8-Jul-2024"

This is because WORKDAY automatically skips Saturday and Sunday when it calculates a result. If we extend the formula to provide holidays, one of which overlaps the date range, WORKDAY returns Tuesday, July 9, 2024, since Thursday, July 4, 2024 is a non-working day and is also skipped in the calculation:

    =WORKDAY("1-Jul-2024",5,{"4-Jul-2024";"2-Sep-2024"}) // returns "9-Jul-2024"

_Note: the holidays above are provided as an [array constant](https://exceljet.net/glossary/array-constant)
, but more typically holidays are provided as a range. Remember that holidays must be valid Excel dates. The name of the holiday makes no difference._

Of course, in real life, you will not hardcode dates directly into formulas. You will instead refer to dates on the worksheet with cell references. The screen below shows the three formulas above "ported" to a workbook with cell references:

![Basic WORKDAY function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_workday_function_basic_example.png "Basic WORKDAY function example")

The formula in D5 does not use WORKDAY and simply [adds 5 days](https://exceljet.net/formulas/add-days-to-date)
 to the start date:

    =B5+C5 // returns "6-Jul-2024"
    

The formula in D6 uses the WORKDAY function but does not provide any holidays:

    =WORKDAY(B6,C6)// returns "8-Jul-2024"
    

The formula in D7 provides holidays in the range G5:G6:

    =WORKDAY(B7,C7,G5:G6) // returns "9-Jul-2024"
    

In all cases, the start date in column B and the days in column D are the same.

### Worksheet Example

In the worksheet below, Column B contains a variety of different start dates, column C contains the number of days to use, and "holidays" is the [named range](https://exceljet.net/glossary/named-range)
 F5:F13. The formula in cell D5 is:

    =WORKDAY(B5,C5,holidays)
    

![WORKDAY function worksheet example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_workday_function_worksheet_example.png "WORKDAY function worksheet example")

As the formula is copied down, WORKDAY calculates a date n working days from the start date using the value in column C for _days_. Notice that WORKDAY automatically excludes Saturdays, Sundays, and overlapping holidays in the calculated result.

_Note: [named ranges](https://exceljet.net/articles/named-ranges)
 automatically behave like absolute references so there is no need to lock the reference to "holidays" before copying the formula. If you prefer not to use a named range, use an absolute reference like $F$5:$F$13 instead._

### Visualized Example

It can be hard to visualize what days WORKDAY is excluding when it calculates a result. The worksheet below contains a more detailed example that shows non-working days shaded in gray in columns D and E:

![WORKDAY function visualized example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_workday_function_add_business_days_to_date.png "WORKDAY function visualized example")

In the example above, the WORKDAY function is used to calculate a date 5 working days after 23-Dec-2024. The formulas in G5 and G6 show the result with and without the holidays in B11:B13:

    =WORKDAY(start,days)
    =WORKDAY(start,days,holidays)
    

The first formula (G5) excludes weekends only and returns December 30, 2024. The second formula (G6) excludes weekends _and_ holidays and returns January 2, 2025. The dates in columns D and E are not required in this solution, they exist only to help visualize how the WORKDAY function evaluates working and non-working days and arrives at a final result. The shading and highlighting is applied with [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
. For a full explanation with details, [see this page](https://exceljet.net/formulas/add-business-days-to-date)
.

### Example - is this date a workday?

One problem you might run into is how to test a date to determine whether it is a workday. You can use WORKDAY for this task, but the formula is not immediately obvious. Essentially, we need to "trick" WORKDAY into evaluating a given date by shifting the date back one day and then asking for the next workday. You can see this approach in the worksheet below. The formula in cell D5 is:

    =WORKDAY(B5-1,1,holidays)=B5

![WORKDAY function - is this date a workday?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_workday_function_date_is_workday.png "WORKDAY function - is this date a workday?")

For a more detailed explanation, see this example: [Date is Workday](https://exceljet.net/formulas/date-is-workday)
.

### Custom Weekends

By default, WORKDAY will exclude weekends (Saturday and Sunday). If you need to customize which days of the week are considered weekend days, use the more robust [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
 function. WORKDAY.INTL can be configured to treat any day of the week as a working or non-working day.

### Recommendations

*   Use cell references for the start date, days, and holidays to make it easy to adjust the formula quickly.
*   Switch to the more flexible [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
     if you need to customize non-working days.
*   WORKDAY returns a date. If you need to calculate the number of working days between two dates, see the [NETWORKDAYS function](https://exceljet.net/functions/networkdays-function)
     or the more flexible [NETWORKDAYS.INTL function](https://exceljet.net/functions/networkdays.intl-function)
    .

### Notes

*   WORKDAY returns a _date_ that is a given number of working _days_ from a specified _start\_date_
*   Use a positive number for days to calculate dates in the future, and a negative number for past dates. 
*   WORKDAY automatically ignores Saturday and Sunday. Switch to WORKDAY.INTL to customize this behavior.
*   If _days_ is not numeric, WORKDAY will return a #VALUE! error.
*   If days is zero, WORKDAY will return the _start\_date_ unchanged.
*   Holidays must be provided as valid Excel dates, typically in a range.
*   When calculating a result, WORKDAY _does not_ include the start date as a work day.

WORKDAY function examples
-------------------------

[![Excel formula: Due date by category](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/due%20date%20by%20category.png "Excel formula: Due date by category")](https://exceljet.net/formulas/due-date-by-category)

### [Due date by category](https://exceljet.net/formulas/due-date-by-category)

In this example, the goal is to create a due date based on category, where each category has a different number of days allocated to complete a given task, issue, project, etc. The amount of time available to resolve each category is shown in column H, and categories is the named range G5:H7. The...

[![Excel formula: Biweekly pay schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/biweekly_pay_schedule.png "Excel formula: Biweekly pay schedule")](https://exceljet.net/formulas/biweekly-pay-schedule)

### [Biweekly pay schedule](https://exceljet.net/formulas/biweekly-pay-schedule)

In this example, the goal is to create a list of pay dates that follow a biweekly schedule. A biweekly pay schedule means employees are paid every two weeks on a given day of the week. Each pay period is 14 days, and there are usually 26 pay dates per year, though occasionally 27 depending on the...

[![Excel formula: Add days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_days_to_date.png "Excel formula: Add days to date")](https://exceljet.net/formulas/add-days-to-date)

### [Add days to date](https://exceljet.net/formulas/add-days-to-date)

In this example, the goal is to add days to a date. This is a frequent task in Excel when you need to calculate a new date by adding a specified number of days to an existing date. Here are some examples of situations where this might be useful: Calculate a due date by adding a given number of days...

[![Excel formula: Get project start date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20project%20start%20date.png "Excel formula: Get project start date")](https://exceljet.net/formulas/get-project-start-date)

### [Get project start date](https://exceljet.net/formulas/get-project-start-date)

This formula is uses the WORKDAY function, which returns a date in the future or past, based on start date and required work days. WORKDAY automatically excludes weekends, and can also exclude holidays if provided as a range of dates. In the example shown, the project end date is in column C, and...

[![Excel formula: Random date between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20date%20between%20two%20dates.png "Excel formula: Random date between two dates")](https://exceljet.net/formulas/random-date-between-two-dates)

### [Random date between two dates](https://exceljet.net/formulas/random-date-between-two-dates)

The RANDBETWEEN function takes two numbers, a bottom and top number, and generates a random integer in between. Dates in Excel are serial numbers, so you can use the DATE function to create the lower number and the upper number. RANDBETWEEN then generates a number that falls between these two date...

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Semimonthly pay schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/semimonthly_pay_schedule.png "Excel formula: Semimonthly pay schedule")](https://exceljet.net/formulas/semimonthly-pay-schedule)

### [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)

In this example, the goal is to create a list of pay dates that follow a semimonthly schedule. A semimonthly pay schedule means employees are paid twice a month, usually on fixed dates such as the 1st and 15th or the 15th and the last day of the month. This results in 24 pay periods over the course...

[![Excel formula: Next business day 6 months in future](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20business%20day%206%20months%20in%20future.png "Excel formula: Next business day 6 months in future")](https://exceljet.net/formulas/next-business-day-6-months-in-future)

### [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)

Working from the inside out, EDATE first calculates a date 6 months in the future. In the example shown, that date is December 24, 2015. Next, the formula subtracts 1 day to get December 23, 2015, and the result goes into the WORKDAY function as the start date, with days = 1, and the range B9:B11...

[![Excel formula: Add workdays to date custom workweek](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_workdays_to_date_custom_workweek.png "Excel formula: Add workdays to date custom workweek")](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)

### [Add workdays to date custom workweek](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)

In this example, the goal is to calculate a workday n days in the future based on a 4-day workweek and, optionally, holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Get project end date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20project%20end%20date.png "Excel formula: Get project end date")](https://exceljet.net/formulas/get-project-end-date)

### [Get project end date](https://exceljet.net/formulas/get-project-end-date)

This formula uses the WORKDAY function to calculate an end date. WORKDAY can calculate dates in the future or past, and automatically excludes weekends and holidays (if provided). In the example shown, we have the project start date in column C, and days in column D. Days represents the duration of...

[![Excel formula: Previous working day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/previous_working_day.png "Excel formula: Previous working day")](https://exceljet.net/formulas/previous-working-day)

### [Previous working day](https://exceljet.net/formulas/previous-working-day)

In the worksheet shown, column B contains 12 dates. The goal is to calculate the previous working day before each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. The formula should automatically skip weekends and any dates considered non-working days...

[![Excel formula: Get project midpoint](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20project%20midpoint2.png "Excel formula: Get project midpoint")](https://exceljet.net/formulas/get-project-midpoint)

### [Get project midpoint](https://exceljet.net/formulas/get-project-midpoint)

The WORKDAY function returns a date in the future or past, based on a start date, workdays, and optional holidays. WORKDAY automatically excludes weekends, and counts only Monday through Friday as workdays. In the example shown, WORKDAY is configured to get a project midpoint date by adding half of...

[![Excel formula: Next working day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next_working_day.png "Excel formula: Next working day")](https://exceljet.net/formulas/next-working-day)

### [Next working day](https://exceljet.net/formulas/next-working-day)

In the worksheet shown, column B contains 12 dates. The goal is to calculate the next working day after each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. In other words, the formula should automatically skip weekends and any dates defined as non-...

[![Excel formula: Date is workday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_workday.png "Excel formula: Date is workday")](https://exceljet.net/formulas/date-is-workday)

### [Date is workday](https://exceljet.net/formulas/date-is-workday)

In this example, the goal is to test a date to determine whether it is a workday. In Excel, you can use either the WORKDAY function or its more flexible sibling WORKDAY.INTL to accomplish this task. WORKDAY function The WORKDAY function calculates a date in the future or past that is, by definition...

WORKDAY function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20values_Thumb.png)](https://exceljet.net/videos/how-to-generate-random-values)

### [How to generate random values](https://exceljet.net/videos/how-to-generate-random-values)

In this video we'll look at a few ways to generate random values with the RANDBETWEEN function. The RANDBETWEEN function is a simple function you can use to generate random numbers. For example, I can enter RANDBETWEEN with a bottom value of 1 and a top value of 100. When I press Enter, I get a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20due%20dates%20with%20WORKDAY_Thumb.png)](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

### [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

In this video we'll look at how to calculate due dates with the WORKDAY and WORKDAY.INTL functions. The WORKDAY function returns a date in the future or past that takes into account weekends and, optionally, holidays. You can use the WORKDAY function to calculate things like ship dates, delivery...

Related functions
-----------------

[![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")](https://exceljet.net/functions/workday.intl-function)

### [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be...

[![Excel NETWORKDAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays%20function.png "Excel NETWORKDAYS function")](https://exceljet.net/functions/networkdays-function)

### [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can _optionally_ exclude a list of holidays supplied as dates. ...

[![Excel NETWORKDAYS.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays.intl%20function.png "Excel NETWORKDAYS.INTL function")](https://exceljet.net/functions/networkdays.intl-function)

### [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)

The Excel NETWORKDAYS.INTL function calculates the number of working days between two dates. NETWORKDAYS.INTL can optionally exclude a list of holidays and provides a way to specify which days of the week are considered weekends.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Get project end date](https://exceljet.net/formulas/get-project-end-date)
    
*   [Due date by category](https://exceljet.net/formulas/due-date-by-category)
    
*   [Previous working day](https://exceljet.net/formulas/previous-working-day)
    
*   [Get project midpoint](https://exceljet.net/formulas/get-project-midpoint)
    
*   [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    
*   [Add days to date](https://exceljet.net/formulas/add-days-to-date)
    
*   [Next working day](https://exceljet.net/formulas/next-working-day)
    
*   [Add workdays to date custom workweek](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)
    
*   [Biweekly pay schedule](https://exceljet.net/formulas/biweekly-pay-schedule)
    

### Videos

*   [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
    
*   [How to generate random values](https://exceljet.net/videos/how-to-generate-random-values)
    

### Functions

*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    
*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)
    

### Articles

*   [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
    

### Links

*   [Microsoft WORKDAY function documentation](https://support.office.com/en-us/article/workday-function-f764a5b7-05fc-4494-9486-60d494efbf33)
    

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
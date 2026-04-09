# Get first day of month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-day-of-month

---

[Skip to main content](https://exceljet.net/formulas/get-first-day-of-month#main-content)

[](https://exceljet.net/formulas/get-first-day-of-month#)

*   [Previous](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)
    
*   [Next](https://exceljet.net/formulas/get-first-day-of-previous-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get first day of month
======================

by Dave Bruns · Updated 23 Jun 2025

Related functions 
------------------

[DAY](https://exceljet.net/functions/day-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")

Summary
-------

To get the first day of the month for any given date, you can use a formula based on the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
. In the example shown, the formula in cell D5 is:

    =EOMONTH(B5,-1)+1

Since the date in cell B5 is 12-Jan-2025, the result is 1-Jan-2025. As the formula is copied down, it returns the first of the month for each date in column B.

Generic formula
---------------

    =EOMONTH(date,-1)+1

Explanation 
------------

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition.

### The EOMONTH Function

The [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 returns the last day of the month, a given number of months in the past or future. For example, with a start date of January 15, 2025, EOMONTH will return the following results with months set to -1, 0, and 1:

    =EOMONTH("15-Jan-2025",-1) // returns 31-Dec-2024
    =EOMONTH("15-Jan-2025",0)  // returns 31-Jan-2025
    =EOMONTH("15-Jan-2025",1)  // returns 28-Feb-2025

Note that the start date remains the same, but the month varies. Negative months cause EOMONTH to move back in time, and positive months move forward, but the result is always the end of the month.

### How the formula works

The formula `=EOMONTH(B5,-1)+1` works in two steps. First, it moves back to the last day of the previous month, relative to the given date. Next, it adds one day to end up on the first day of the current month. Working from the inside out with a start date of January 12, 2025:

    =EOMONTH("12-Jan-2025",-1)+1  // move back 1 month
    ="31-Dec-2024"+1  // add 1 day
    ="1-Jan-2025"  // final result

The result is always the first day of the month for any given date. As the formula is copied down, the process is repeated for each date in column B.

### First day of current month

To get the first day of the current month, you can use the same approach but replace the date reference with the [TODAY function](https://exceljet.net/functions/today-function)
:

    =EOMONTH(TODAY(),-1)+1

This formula will automatically update each day to show the first day of whatever month it currently is. For example, if today is June 21, 2025, the formula will return June 1, 2025. If you open the same worksheet in July, the result will be July 1, 2025. The formula works exactly the same way as the main example:

    =EOMONTH(TODAY(),-1)+1
    =EOMONTH("21-Jun-2025",-1)+1  // get current date
    ="31-May-2025"+1  // move back 1 month
    ="1-Jun-2025"  // add 1 day

This approach is useful in reports and dashboards that need to display current-month information. Since TODAY recalculates whenever the worksheet recalculates, this formula will always return the first day of the current month.

### Variations

You can easily change how this formula works by changing the number of months used inside the EOMONTH function. The pattern `EOMONTH(date, n-1)+1` will give you the first day of the month that is `n` months away from your reference date:

    =EOMONTH(B5,0)+1 // first day of next month
    =EOMONTH(B5,-1)+1 // first day of current month
    =EOMONTH(B5,-2)+1 // first day of previous month
    =EOMONTH(B5,-7)+1 // first day of month 6 months ago
    =EOMONTH(B5,5)+1 // first day of month 6 months forward
    

> To move forward or backward `n` months without changing the date, see the [EDATE function](https://exceljet.net/functions/edate-function)
> .

### Alternative formula

You can also get the first day of a month using the [DAY function](https://exceljet.net/functions/day-function)
 in a formula like this:

    =B5-DAY(B5)+1

This formula was the standard way to get the first day of the month before the EOMONTH function was introduced to Excel. This formula works in three steps:

1.  Get the day number from the date with `DAY(B5)`.
2.  Subtract the day from the date (rewind to day 0 = last day of the previous month).
3.  Add 1 day to end up on the first day of the current month.

For example, with a start date of January 12, 2025:

    =B5-DAY(B5)+1
    ="12-Jan-2025"-12+1
    ="31-Dec-2024"+1
    ="1-Jan-2025"

Both formulas work reliably, but the EOMONTH formula is slightly easier to understand and configure.

Related formulas
----------------

[![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")](https://exceljet.net/formulas/get-last-day-of-month)

### [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below. The EOMONTH function The EOMONTH function returns the last day of the...

[![Excel formula: Days in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/days%20in%20month.png "Excel formula: Days in month")](https://exceljet.net/formulas/days-in-month)

### [Days in month](https://exceljet.net/formulas/days-in-month)

In this example, the goal is to get the total number of days in a month based on any date in the month. This problem can be solved by combining the DAY function with the EOMONTH function. The EOMONTH function The EOMONTH function returns the last day of the month, a given number of months in the...

[![Excel formula: Get last working day in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20working%20day%20in%20month.png "Excel formula: Get last working day in month")](https://exceljet.net/formulas/get-last-working-day-in-month)

### [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)

Working from the inside out, the EOMONTH function gets the last day of month of any date. To this result, we add 1, which results in the first day of the next month. This date goes into WORKDAY function as the "start date", along with -1 for "days". The WORKDAY function automatically steps back 1...

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

Related functions
-----------------

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)
    
*   [Days in month](https://exceljet.net/formulas/days-in-month)
    
*   [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    

### Functions

*   [DAY Function](https://exceljet.net/functions/day-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

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
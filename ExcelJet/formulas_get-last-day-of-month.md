# Get last day of month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-day-of-month

---

[Skip to main content](https://exceljet.net/formulas/get-last-day-of-month#main-content)

[](https://exceljet.net/formulas/get-last-day-of-month#)

*   [Previous](https://exceljet.net/formulas/get-fiscal-year-from-date)
    
*   [Next](https://exceljet.net/formulas/get-last-weekday-in-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get last day of month
=====================

by Dave Bruns · Updated 22 Jun 2025

Related functions 
------------------

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[DATE](https://exceljet.net/functions/date-function)

[YEAR](https://exceljet.net/functions/year-function)

[MONTH](https://exceljet.net/functions/month-function)

![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")

Summary
-------

To calculate the last day of a month based on a given date, you can use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
. In the example shown, the formula in cell D5 is:

    =EOMONTH(B5,0)
    

Since the date in cell B5 is 12-Jan-2024, the result is 31-Jan-2024. As the formula is copied down, it returns the last day of the month for each date in column B.

Generic formula
---------------

    =EOMONTH(date,0)

Explanation 
------------

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below.

### The EOMONTH function

The [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 returns the last day of the month, a given number of months in the past or future. For example, with a start date of January 15, 2024, EOMONTH will return the following results with months set to -1, 0, and 1:

    =EOMONTH("15-Jan-2024",-1) // returns 31-Dec-2023
    =EOMONTH("15-Jan-2024",0)  // returns 31-Jan-2024
    =EOMONTH("15-Jan-2024",1)  // returns 29-Feb-2024
    

Note that the start date remains the same, but the month varies. Negative months cause EOMONTH to move back in time, and positive months move forward, but the result is always the end of the month. The EOMONTH function automatically handles leap years - for example, February 2024 returns 29-Feb-2024 since 2024 is a [leap year](https://exceljet.net/formulas/year-is-a-leap-year)
.

### How the formula works

The formula `=EOMONTH(B5,0)` works by taking any date and returning the last day of that same month. Working with a start date of January 12, 2024:

    =EOMONTH("12-Jan-2024",0)  // get last day of current month
    ="31-Jan-2024"  // final result
    

The result is always the last day of the month for any given date. As the formula is copied down, the process is repeated for each date in column B.

### Last day of current month

To get the last day of the current month, you can use the same approach but replace the date reference with the [TODAY function](https://exceljet.net/functions/today-function)
:

    =EOMONTH(TODAY(),0)
    

This formula will automatically update each day to show the last day of whatever month it currently is. For example, if today is June 21, 2025, the formula will return June 30, 2025. If you open the same worksheet in July, the result will be July 31, 2025. The formula works exactly the same way as the main example:

    =EOMONTH(TODAY(),0)
    =EOMONTH("21-Jun-2025",0)  // get current date
    ="30-Jun-2025"  // last day of current month
    

This approach is useful in reports and dashboards that need to display current-month information. Since TODAY recalculates whenever the worksheet recalculates, this formula will always return the last day of the current month.

### Variations

You can easily change how this formula works by changing the number of months used inside the EOMONTH function. The pattern `EOMONTH(date, n)` will give you the last day of the month that is `n` months away from your reference date:

    =EOMONTH(B5,-1) // last day of previous month
    =EOMONTH(B5,0)  // last day of current month
    =EOMONTH(B5,1)  // last day of next month
    =EOMONTH(B5,6)  // last day of month 6 months forward
    =EOMONTH(B5,-6) // last day of month 6 months ago
    

> To move forward or backward `n` months without changing the date, see the [EDATE function](https://exceljet.net/functions/edate-function)
> .

### Alternative formula

You can also write a formula using the [DATE](https://exceljet.net/functions/date-function)
, [YEAR](https://exceljet.net/functions/year-function)
, and [MONTH](https://exceljet.net/functions/month-function)
 functions to return the last day of the month:

    =DATE(YEAR(B5),MONTH(B5)+1,0)
    

This formula works in three steps:

1.  Get the year from the date with `YEAR(B5)`.
2.  Get the month from the date with `MONTH(B5)` and add 1 to move to the next month.
3.  Use 0 for the day, which causes DATE to "roll back" one day to the last day of the previous month.

For example, with a start date of January 12, 2024:

    =DATE(YEAR("12-Jan-2024"),MONTH("12-Jan-2024")+1,0)
    =DATE(2024,1+1,0)
    =DATE(2024,2,0)
    ="31-Jan-2024"
    

The trick with this formula is supplying zero for the day. When you supply zero as the day argument to DATE, the date function will "roll back" one day to the last day of the previous month. So, by adding 1 to the month and using zero for day, DATE returns the last day of the "original" month.

> Although EOMONTH is more convenient, this formula shows that there are many ways to solve the same problem in Excel. It also demonstrates that Excel treats day 0 in a month as the _last day of the previous month,_ which can be useful in certain calculations.

Related formulas
----------------

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Get last working day in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20working%20day%20in%20month.png "Excel formula: Get last working day in month")](https://exceljet.net/formulas/get-last-working-day-in-month)

### [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)

Working from the inside out, the EOMONTH function gets the last day of month of any date. To this result, we add 1, which results in the first day of the next month. This date goes into WORKDAY function as the "start date", along with -1 for "days". The WORKDAY function automatically steps back 1...

[![Excel formula: Days in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/days%20in%20month.png "Excel formula: Days in month")](https://exceljet.net/formulas/days-in-month)

### [Days in month](https://exceljet.net/formulas/days-in-month)

In this example, the goal is to get the total number of days in a month based on any date in the month. This problem can be solved by combining the DAY function with the EOMONTH function. The EOMONTH function The EOMONTH function returns the last day of the month, a given number of months in the...

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

Related functions
-----------------

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)
    
*   [Days in month](https://exceljet.net/formulas/days-in-month)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    

### Functions

*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    

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
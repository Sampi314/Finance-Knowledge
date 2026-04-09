# Days in month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/days-in-month

---

[Skip to main content](https://exceljet.net/formulas/days-in-month#main-content)

[](https://exceljet.net/formulas/days-in-month#)

*   [Previous](https://exceljet.net/formulas/date-is-workday)
    
*   [Next](https://exceljet.net/formulas/display-the-current-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Days in month
=============

by Dave Bruns · Updated 21 Jun 2025

Related functions 
------------------

[DAY](https://exceljet.net/functions/day-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: Days in month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/days%20in%20month.png "Excel formula: Days in month")

Summary
-------

To get the number of days in a given month based on a date in the month, you can use a formula based on the [EOMONTH](https://exceljet.net/functions/eomonth-function)
 and [DAY](https://exceljet.net/functions/day-function)
 functions. In the example shown, the formula in cell D5 is:

    =DAY(EOMONTH(B5,0))

Since the date in cell B5 is 12-Jan-2024, and since there are 31 days in January, the result is 31. As the formula is copied down, it returns the total days for each month for each date in column B.

Generic formula
---------------

    =DAY(EOMONTH(date,0))

Explanation 
------------

In this example, the goal is to get the total number of days in a month based on any date in the month. This problem can be solved by combining the DAY function with the EOMONTH function. 

### The EOMONTH function

The [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 returns the last day of the month, a given number of months in the past or future. For example, with a start date of June 15, 2024, EOMONTH will return the following results with _months_ set to -1,0, and 1:

    =EOMONTH("15-Jun-2024",-1) // returns 31-May-2024
    =EOMONTH("15-Jun-2024",0) // returns 30-Jun-2024
    =EOMONTH("15-Jun-2024",1) // returns 31-Jul-2024
    

Note that the start date remains the same, but the month varies. Negative months cause EOMONTH to move back in time, and positive months move forward, but the result is always the end of the month. Providing _months_ as zero (0) will move EOMONTH to the end of the "current" month, relative to the date provided.

### The DAY function

The [DAY function](https://exceljet.net/functions/day-function)
 returns the day component of any date, for example:

    =DAY("15-Jun-2019") // returns 15
    =DAY("7-Aug-2021") // returns 7
    =DAY("23-Nov-2023") // returns 23

Note that in each case DAY returns the day value for the date.

### Combining DAY and EOMONTH

Since, by definition, the last day of a month is equal to the number of days in the month, we can use DAY with EOMONTH to calculate the number of days in a month. In the worksheet shown, the formula in cell D5 looks like this:

    =DAY(EOMONTH(B5,0))

![Using DAY and EOMONTH to calculate total days in any month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/days_in_month_example.png "Using DAY and EOMONTH to calculate total days in any month")

Working from the inside out, the EOMONTH function returns the last day of the month using the date in B5 as a starting point. Notice that the months argument is provided as zero so that we stay in the same month. Next, the shifted date is returned to the DAY function, which returns the day part of the date as a final result. Since the last day in January is the 31st, the final result is 31:

    =DAY(EOMONTH("12-Jan-2024",0))
    =DAY("31-Jan-2024")
    =31

As the formula is copied down, the process is repeated for each date in column B. 

### Days in the Current Month

To get the number of days in the current month (today's month), you can use the same approach but replace the date reference with the [TODAY function](https://exceljet.net/functions/today-function)
:

    =DAY(EOMONTH(TODAY(),0))
    

This formula will automatically update each day to show the total number of days in whatever month it currently is. For example, if today is June 21, 2025, the formula will return 30 (since June has 30 days). If you open the same worksheet in July, it will automatically return 31. The formula works exactly the same way as the main example:

    =DAY(EOMONTH(TODAY(),0))
    =DAY(EOMONTH("21-Jun-2025",0))  // TODAY() returns current date
    =DAY("30-Jun-2025")             // EOMONTH finds last day of June
    =30                             // DAY extracts the day number
    

This approach is useful in reports and dashboards that need to display current-month information. Since TODAY recalculates whenever the worksheet recalculates, this formula will always reflect the correct number of days for the current month.

Related formulas
----------------

[![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")](https://exceljet.net/formulas/get-last-day-of-month)

### [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below. The EOMONTH function The EOMONTH function returns the last day of the...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: List all dates in a month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_all_dates_in_a_month.png "Excel formula: List all dates in a month")](https://exceljet.net/formulas/list-all-dates-in-a-month)

### [List all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month)

In this example, we'll use SEQUENCE to generate all dates in a given month. Creating a complete list of dates for a specific month is a common Excel task with many practical applications, from building project timelines and work schedules to generating calendar views and tracking daily data. The...

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
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [List all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month)
    

### Functions

*   [DAY Function](https://exceljet.net/functions/day-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

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
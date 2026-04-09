# Get last working day in month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-working-day-in-month

---

[Skip to main content](https://exceljet.net/formulas/get-last-working-day-in-month#main-content)

[](https://exceljet.net/formulas/get-last-working-day-in-month#)

*   [Previous](https://exceljet.net/formulas/get-last-weekday-in-month)
    
*   [Next](https://exceljet.net/formulas/get-monday-of-the-week)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get last working day in month
=============================

by Dave Bruns · Updated 19 Feb 2018

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: Get last working day in month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20last%20working%20day%20in%20month.png "Excel formula: Get last working day in month")

Summary
-------

To get the last working day in a month, you can use the WORKDAY function together with the EOMONTH function. In the example, the formula in C4 is:

    =WORKDAY(EOMONTH(B4,0)+1,-1)
    

Generic formula
---------------

    =WORKDAY(EOMONTH(date)+1,-1)

Explanation 
------------

Working from the inside out, the EOMONTH function gets the last day of month of any date. To this result, we add 1, which results in the first day of the next month.

This date goes into WORKDAY function as the "start date", along with -1 for "days". The WORKDAY function automatically steps back 1 day, taking into account any weekends. The result is the last workday of the month.

### Holidays

To get the last working day of the month, taking into account holidays, just add the _range_ that contains holiday dates to the formula like this:

    =WORKDAY(EOMONTH(B4,0)+1,-1,holidays)
    

### Custom weekends

The WEEKDAY function assumes weekends are Saturday and Sunday. If you need to customize weekend days, you can use the [WEEKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
 function.

Related formulas
----------------

[![Excel formula: Get last day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_day_of_month.png "Excel formula: Get last day of month")](https://exceljet.net/formulas/get-last-day-of-month)

### [Get last day of month](https://exceljet.net/formulas/get-last-day-of-month)

In this example, the goal is to get the last day of the month based on any valid date. This problem can be solved most easily with the EOMONTH function. However, it can also be solved with the DATE function as explained below. The EOMONTH function The EOMONTH function returns the last day of the...

[![Excel formula: Get last weekday in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20weekday%20in%20month.png "Excel formula: Get last weekday in month")](https://exceljet.net/formulas/get-last-weekday-in-month)

### [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)

First, this formula determines the first day of the next month \*after\* a given date. It does this my using EOMONTH to get the last day of the month, then adding one day: =EOMONTH(B5,0)+1 Next, the formula calculates the number of days required to "roll back" to the last requested weekday in the...

[![Excel formula: Get nth day of week in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get-nth-day-of-week-in-month_0.png "Excel formula: Get nth day of week in month")](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

### [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

This example demonstrates how to calculate the nth occurrence of a specific day of the week within a month. For instance, you might need to find the 2nd Tuesday, the 4th Wednesday, or the 1st Friday of any given month. The worksheet is structured with the starting date in column B, the target day...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

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
    
*   [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)
    
*   [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

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
# Get last weekday in month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-weekday-in-month

---

[Skip to main content](https://exceljet.net/formulas/get-last-weekday-in-month#main-content)

[](https://exceljet.net/formulas/get-last-weekday-in-month#)

*   [Previous](https://exceljet.net/formulas/get-last-day-of-month)
    
*   [Next](https://exceljet.net/formulas/get-last-working-day-in-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get last weekday in month
=========================

by Dave Bruns · Updated 12 Sep 2016

Related functions 
------------------

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

![Excel formula: Get last weekday in month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20last%20weekday%20in%20month.png "Excel formula: Get last weekday in month")

Summary
-------

To get the last weekday in a month (i.e. the last Saturday, the last Friday, the last Monday, etc) you can use a formula based on the EOMONTH and WEEKDAY functions.

In the example shown, the formula in D5 is:

    =EOMONTH(B5,0)+1-WEEKDAY(EOMONTH(B5,0)+1-C5)
    

Generic formula
---------------

    =EOMONTH(date,0)+1-WEEKDAY(EOMONTH(date,0)+1-dow)

Explanation 
------------

First, this formula determines the first day of the next month \*after\* a given date. It does this my using EOMONTH to get the last day of the month, then adding one day:

    =EOMONTH(B5,0)+1
    

Next, the formula calculates the number of days required to "roll back" to the last requested weekday in the month prior (i.e. the month of the original date):

    WEEKDAY(EOMONTH(B5,0)+1-C5)
    

Inside WEEKDAY, EOMONTH is again used to get the first day of the next month. From this date, the value for day of week is subtracted, and the result is fed into WEEKDAY, which returns the number of days to roll back.

Last, the roll back days are subtracted from the first day of the next month, which yields the final result.

### Other weekdays

In the general form of the formula at the top of the page, day of week is abbreviated "dow". This is a number between 1 (Sunday) and 7 (Saturday) which can be changed to get a different day of week. For example, to get the last Thursday of a month, set dow to 5.

_Note: I ran into this formula in an [answer on the MrExcel forum by Barry Houdini](http://www.mrexcel.com/forum/excel-questions/623932-get-date-last-friday-month.html)
._

Related formulas
----------------

[![Excel formula: Get last working day in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20working%20day%20in%20month.png "Excel formula: Get last working day in month")](https://exceljet.net/formulas/get-last-working-day-in-month)

### [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)

Working from the inside out, the EOMONTH function gets the last day of month of any date. To this result, we add 1, which results in the first day of the next month. This date goes into WORKDAY function as the "start date", along with -1 for "days". The WORKDAY function automatically steps back 1...

[![Excel formula: Get nth day of week in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get-nth-day-of-week-in-month_0.png "Excel formula: Get nth day of week in month")](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

### [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

This example demonstrates how to calculate the nth occurrence of a specific day of the week within a month. For instance, you might need to find the 2nd Tuesday, the 4th Wednesday, or the 1st Friday of any given month. The worksheet is structured with the starting date in column B, the target day...

Related functions
-----------------

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

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

*   [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)
    
*   [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
    

### Functions

*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    

### Links

*   [Barry Houdini's answer at MrExcel forum](http://www.mrexcel.com/forum/excel-questions/623932-get-date-last-friday-month.html)
    

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
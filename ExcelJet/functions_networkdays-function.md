# Excel NETWORKDAYS function | Exceljet

**Source:** https://exceljet.net/functions/networkdays-function

---

[Skip to main content](https://exceljet.net/functions/networkdays-function#main-content)

[](https://exceljet.net/functions/networkdays-function#)

*   [Previous](https://exceljet.net/functions/month-function)
    
*   [Next](https://exceljet.net/functions/networkdays.intl-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

NETWORKDAYS Function
====================

by Dave Bruns · Updated 3 Dec 2022

Related functions 
------------------

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

[WORKDAY](https://exceljet.net/functions/workday-function)

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

[DAYS](https://exceljet.net/functions/days-function)

[DATEDIF](https://exceljet.net/functions/datedif-function)

![Excel NETWORKDAYS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20networkdays%20function.png "Excel NETWORKDAYS function")

Summary
-------

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can _optionally_ exclude a list of holidays supplied as dates. 

Purpose 
--------

Get the number of working days between two dates

Return value 
-------------

A number representing days.

Syntax
------

    =NETWORKDAYS(start_date,end_date,[holidays])

*   _start\_date_ - The start date.
*   _end\_date_ - The end date.
*   _holidays_ - \[optional\] A list of non-work days as dates.

Using the NETWORKDAYS function 
-------------------------------

The NETWORKDAYS function returns the number of working days between two dates, automatically excluding weekends (Saturday and Sunday) and _optionally_ excluding holidays provided as a list of dates. NETWORKDAYS can be used to calculate employee benefits that accrue based on days worked, the number of working days available during a project, the number of working days required to resolve a customer support issue, etc.

NETWORKDAYS takes three [arguments](https://exceljet.net/glossary/function-argument)
: _start\_date_, _end\_date_, and _holidays_. All three arguments must be valid Excel dates. Holidays are optional. To exclude holidays, provide a range of [valid Excel dates](https://exceljet.net/glossary/excel-date)
 for the _holidays_ argument. Holidays are treated as non-working days and will not be included in the result.

NETWORKDAYS includes both the start date and end date when calculating workdays. If you give NETWORKDAYS the same date for start date and end date, and the date is not a weekend or holiday, it will return 1.

### Example

The general form of a NETWORKDAYS formula is as follows:

    =NETWORKDAYS(start,end) // exclude weekends
    =NETWORKDAYS(start,end,holidays) // exclude weekends + holidays
    

In the example shown, **holidays** is the [named range](https://exceljet.net/glossary/named-range)
 H5:H13, which contains non-working days in 2021. Columns E and F show the number of working days in each month of the year. The formula in cell E5 (Result 1) contains the NETWORKDAYS function but _does not_ take into account holidays:

    =NETWORKDAYS(B5,C5) // returns 21
    

The formula in cell F5 (Result 2) _does_ take into account holidays:

    =NETWORKDAYS(B5,C5,holidays) // returns 19
    

NETWORKDAYS will automatically exclude both Saturday and Sunday. This behavior is not configurable. If you need more flexibility, the [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)
 function provides a way to treat any day of the week as a non-working day.

### Notes

*   NETWORKDAYS calculates _whole_ workdays, ignoring any time values.
*   NETWORKDAYS will automatically exclude both Saturday and Sunday.
*   NETWORKDAYS includes _both_ the start date and end date when calculating workdays.
*   To create a custom weekend schedule, see the [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)
     function.

NETWORKDAYS function examples
-----------------------------

[![Excel formula: Working days left in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/working%20days%20left%20in%20month.png "Excel formula: Working days left in month")](https://exceljet.net/formulas/working-days-left-in-month)

### [Working days left in month](https://exceljet.net/formulas/working-days-left-in-month)

NETWORKDAYS is a built in function accepts a start date, end date, and (optionally) a range that contains holiday dates. In this case, the start date is Jan 10, 2018, provided as cell B5. The end date is calculated using the EOMONTH function with an offset of zero, which returns the last day of the...

[![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")](https://exceljet.net/formulas/get-work-hours-between-dates)

### [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Workdays per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/workdays%20per%20month.png "Excel formula: Workdays per month")](https://exceljet.net/formulas/workdays-per-month)

### [Workdays per month](https://exceljet.net/formulas/workdays-per-month)

First, it's important to understand that the values in the Month column (B) are actual dates, formatted with the custom number format "mmm". For example, B4 contains January 1, 2014, but displays only "Jan" per the custom number format. The formula itself is based on the NETWORKDAYS function, which...

[![Excel formula: Working days in year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/working%20days%20in%20year.png "Excel formula: Working days in year")](https://exceljet.net/formulas/working-days-in-year)

### [Working days in year](https://exceljet.net/formulas/working-days-in-year)

NETWORKDAYS is a built-in function accepts a start date, an end date, and (optionally) a range that contains holiday dates. In the example shown, we generate the start and end date using the DATE function like this: DATE(D5,1,1) // first day of year DATE(D5,12,31) // last day of year The DATE...

[![Excel formula: Get work hours between dates and times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20and%20times.png "Excel formula: Get work hours between dates and times")](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)

### [Get work hours between dates and times](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)

This formula calculates total working hours between two dates and times, that occur between a "lower" and "upper" time. In the example shown, the lower time is 9:00 AM and the upper time is 5:00 PM. These appear in the formula as the named ranges "lower" and "upper". The logic of the formula is to...

NETWORKDAYS function videos
---------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20the%20number%20of%20days%20between%20dates-thumb.png)](https://exceljet.net/videos/how-to-calculate-the-number-of-days-between-dates)

### [How to calculate the number of days between dates](https://exceljet.net/videos/how-to-calculate-the-number-of-days-between-dates)

In this video we'll look at how to calculate the number of days between dates. To get started, let's first set up some dates, so we have a visual representation to refer to. In C5, I'll add a start date. Then, I'll add and copy a formula below that simply adds "1" to each date above. The result is...

Related functions
-----------------

[![Excel NETWORKDAYS.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays.intl%20function.png "Excel NETWORKDAYS.INTL function")](https://exceljet.net/functions/networkdays.intl-function)

### [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)

The Excel NETWORKDAYS.INTL function calculates the number of working days between two dates. NETWORKDAYS.INTL can optionally exclude a list of holidays and provides a way to specify which days of the week are considered weekends.

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

[![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")](https://exceljet.net/functions/workday.intl-function)

### [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be...

[![Excel DAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20days%20function.png "Excel DAYS function")](https://exceljet.net/functions/days-function)

### [DAYS Function](https://exceljet.net/functions/days-function)

The Excel DAYS function returns the number of days between two dates. With a start date in A1 and end date in B1, =DAYS(B1,A1) will return the days between the two dates.

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Workdays per month](https://exceljet.net/formulas/workdays-per-month)
    
*   [Working days in year](https://exceljet.net/formulas/working-days-in-year)
    
*   [Get work hours between dates and times](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)
    
*   [Working days left in month](https://exceljet.net/formulas/working-days-left-in-month)
    
*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    

### Videos

*   [How to calculate the number of days between dates](https://exceljet.net/videos/how-to-calculate-the-number-of-days-between-dates)
    
*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    

### Functions

*   [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)
    
*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    
*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    
*   [DAYS Function](https://exceljet.net/functions/days-function)
    
*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    

### Links

*   [Microsoft NETWORKDAYS function documentation](https://support.office.com/en-us/article/networkdays-function-48e717bf-a7a3-495f-969e-5005e3eb18e7)
    

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
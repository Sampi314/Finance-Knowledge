# Get days between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-days-between-dates

---

[Skip to main content](https://exceljet.net/formulas/get-days-between-dates#main-content)

[](https://exceljet.net/formulas/get-days-between-dates#)

*   [Previous](https://exceljet.net/formulas/get-days-before-a-date)
    
*   [Next](https://exceljet.net/formulas/get-days-between-dates-ignoring-years)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get days between dates
======================

by Dave Bruns · Updated 14 May 2025

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

[DAYS](https://exceljet.net/functions/days-function)

![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")

Summary
-------

To count the number of days between two dates you can use the [DAYS function](https://exceljet.net/functions/days-function)
 or just subtract the start date from the end date. In the example shown, the formula in D6 is:

    =C6-B6

The result is the number 365, since there are 365 days between Jan 1, 1999 and Jan 1, 2000.

_Note: To see the result as a number and not a date, format the result with the_ [_General number format_](https://exceljet.net/glossary/number-format)
_._

Generic formula
---------------

    =end_date-start_date

Explanation 
------------

[Dates in Excel are serial numbers](https://exceljet.net/glossary/excel-date)
 that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this:

    =C6-B6
    =36161-36526
    =365
    

### Working with today

To count the number of days between an earlier date and today, you can use the [TODAY function](https://exceljet.net/functions/today-function)
:

    =TODAY()-earlier_date
    

To calculate the number of days between a later date and today, use:

    =later_date-TODAY()
    

Note that TODAY will recalculate on an ongoing basis. If you open the workbook at a later date, the value used for TODAY will update and you will see a new result.

### The DAYS function

The [DAYS function](https://exceljet.net/functions/days-function)
 calculates the number of days between two dates using a start date and an end date. With a start date in A1 and end date in A2:

    =DAYS(A2,A1)
    

Will return the same result as:

    =A2-A1
    

Both dates must be [valid Excel dates](https://exceljet.net/glossary/excel-date)
 or text values that can be coerced to dates. If start and end dates are reversed, DAYS will return a negative number.

### Workdays between dates

The formulas above count _all days_ between two dates, to calculate _working days_ between dates, see the [NETWORKDAYS function](https://exceljet.net/functions/networkdays-function)
 or [NETWORKDAYS.INTL function](https://exceljet.net/functions/networkdays.intl-function)
. See [this article](https://exceljet.net/formulas/get-workdays-between-dates)
 for more details.

Related formulas
----------------

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Calculate days remaining](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20days%20remaining.png "Excel formula: Calculate days remaining")](https://exceljet.net/formulas/calculate-days-remaining)

### [Calculate days remaining](https://exceljet.net/formulas/calculate-days-remaining)

Dates in Excel are just serial numbers that begin on January 1, 1900. If you enter 1/1/1900 in Excel, and format the result with the "General" number format , you'll see the number 1. This means that you can easily calculate the days between two dates by subtracting the earlier date from the later...

[![Excel formula: Get months between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_months_between_dates.png "Excel formula: Get months between dates")](https://exceljet.net/formulas/get-months-between-dates)

### [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)

In this example, the goal is to calculate the number of months between two valid Excel dates . This is a curiously tricky problem in Excel because the number of days in a month varies, and the rules about how a whole month might be calculated are not obvious. In addition, there is not a modern...

[![Excel formula: Calculate date overlap in days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20date%20overlap%20in%20days.png "Excel formula: Calculate date overlap in days")](https://exceljet.net/formulas/calculate-date-overlap-in-days)

### [Calculate date overlap in days](https://exceljet.net/formulas/calculate-date-overlap-in-days)

In this example, the goal is to create a formula that will calculate the number of days between a start date in column B and an end date in column C that overlap a period defined by date 1 and date 2, which are variables that can be easily changed. You can use a formula like this to do things like...

Related functions
-----------------

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel DAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20days%20function.png "Excel DAYS function")](https://exceljet.net/functions/days-function)

### [DAYS Function](https://exceljet.net/functions/days-function)

The Excel DAYS function returns the number of days between two dates. With a start date in A1 and end date in B1, =DAYS(B1,A1) will return the days between the two dates.

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
    
*   [Calculate days remaining](https://exceljet.net/formulas/calculate-days-remaining)
    
*   [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)
    
*   [Calculate date overlap in days](https://exceljet.net/formulas/calculate-date-overlap-in-days)
    

### Functions

*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [DAYS Function](https://exceljet.net/functions/days-function)
    

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
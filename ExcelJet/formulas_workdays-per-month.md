# Workdays per month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/workdays-per-month

---

[Skip to main content](https://exceljet.net/formulas/workdays-per-month#main-content)

[](https://exceljet.net/formulas/workdays-per-month#)

*   [Previous](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)
    
*   [Next](https://exceljet.net/formulas/working-days-in-year)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Workdays per month
==================

by Dave Bruns · Updated 16 Oct 2019

Related functions 
------------------

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: Workdays per month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/workdays%20per%20month.png "Excel formula: Workdays per month")

Summary
-------

To calculate workdays per month, use the EOMONTH function together with the NETWORKDAYS function. In the example shown, the formula in C4 is:

    =NETWORKDAYS(B4,EOMONTH(B4,0),holidays)
    

Where "holidays" is the [named range](https://exceljet.net/glossary/named-range)
 E3:E13.

Generic formula
---------------

    =NETWORKDAYS(date,EOMONTH(date,0),holidays)

Explanation 
------------

First, it's important to understand that the values in the Month column (B) are actual dates, formatted with the custom number format "mmm".

For example, B4 contains January 1, 2014, but displays only "Jan" per the custom number format.

The formula itself is based on the NETWORKDAYS function, which returns the number of working days between a start date and end date, taking into account holidays (if provided).

For each month, the start date comes from column B and the end date is calculated with the EOMONTH function like so:

    EOMONTH(B4,0)
    

EOMONTH takes a date and returns the last day of a month. The month itself is controlled by the 2nd argument. Since in this case we want to stay in the same month, we use zero.

Finally, a list of holidays is provided as the 3rd argument to NETWORKDAYS using the [named range](https://exceljet.net/glossary/named-range)
 holidays (E3:E13).

With this information, NETWORKDAYS calculates the number of working days in each month, automatically excluding weekends and holidays.

If you need more control over which days are treated as weekends, use the [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)
 function.

Related formulas
----------------

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Working days in year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/working%20days%20in%20year.png "Excel formula: Working days in year")](https://exceljet.net/formulas/working-days-in-year)

### [Working days in year](https://exceljet.net/formulas/working-days-in-year)

NETWORKDAYS is a built-in function accepts a start date, an end date, and (optionally) a range that contains holiday dates. In the example shown, we generate the start and end date using the DATE function like this: DATE(D5,1,1) // first day of year DATE(D5,12,31) // last day of year The DATE...

Related functions
-----------------

[![Excel NETWORKDAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays%20function.png "Excel NETWORKDAYS function")](https://exceljet.net/functions/networkdays-function)

### [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can _optionally_ exclude a list of holidays supplied as dates. ...

[![Excel NETWORKDAYS.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays.intl%20function.png "Excel NETWORKDAYS.INTL function")](https://exceljet.net/functions/networkdays.intl-function)

### [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)

The Excel NETWORKDAYS.INTL function calculates the number of working days between two dates. NETWORKDAYS.INTL can optionally exclude a list of holidays and provides a way to specify which days of the week are considered weekends.

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

*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Working days in year](https://exceljet.net/formulas/working-days-in-year)
    

### Functions

*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)
    
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
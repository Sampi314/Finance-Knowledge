# Excel DAYS function | Exceljet

**Source:** https://exceljet.net/functions/days-function

---

[Skip to main content](https://exceljet.net/functions/days-function#main-content)

[](https://exceljet.net/functions/days-function#)

*   [Previous](https://exceljet.net/functions/day-function)
    
*   [Next](https://exceljet.net/functions/days360-function)
    

Excel 2013

[Date and time](https://exceljet.net/functions#Date-and-time)

DAYS Function
=============

by Dave Bruns · Updated 11 Dec 2022

Related functions 
------------------

[YEARFRAC](https://exceljet.net/functions/yearfrac-function)

[DAYS360](https://exceljet.net/functions/days360-function)

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

![Excel DAYS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20days%20function.png "Excel DAYS function")

Summary
-------

The Excel DAYS function returns the number of days between two dates. With a start date in A1 and end date in B1, =DAYS(B1,A1) will return the days between the two dates.

Purpose 
--------

Count days between dates

Return value 
-------------

A number representing days.

Syntax
------

    =DAYS(end_date,start_date)

*   _end\_date_ - The end date.
*   _start\_date_ - The start date.

Using the DAYS function 
------------------------

The DAYS function returns the number of days between two dates. Both dates must be [valid Excel dates](https://exceljet.net/glossary/excel-date)
 or text values that can be coerced to dates. The DAYS function only works with whole numbers, fractional time values that might be [part of a date](https://exceljet.net/glossary/excel-datetime)
 are ignored. If start and end dates are reversed, DAYS returns a negative number. The DAYS function returns _all days_ between two dates, to calculate _working days_ between dates, see the [NETWORKDAYS function](https://exceljet.net/functions/networkdays-function)
.

### Examples

With a start date in A1 and end date in A2:

    =DAYS(A2,A1)
    

Will return the same result as:

    =A2-A1
    

Unlike the simple formula above, the DAYS function can also handle dates in text format, as long as the date is recognized by Excel. For example:

    =DAYS("7/15/2016","7/1/2016") // returns 14
    

The DAYS function returns the number of days _between_ two dates. For example:

    =DAYS("1-Mar-21","2-Mar-21") // returns 1
    

To _include_ the end date in the count, add 1 to the result:

    =DAYS("1-Mar-21","2-Mar-21")+1 // returns 2
    

_Storing and parsing text values that represent dates should be avoided, because it can introduce errors and parsing problems. Working with native [Excel dates](https://exceljet.net/glossary/excel-date)
 (which are numbers) is a better approach. To create a numeric date from scratch in a formula, use the [DATE function](https://exceljet.net/functions/date-function)
._

### Notes

*   The DAYS function only works with whole numbers and ignores time.
*   If dates are not recognized, DAYS returns the #VALUE! error.
*   If dates are out of range, DAYS returns the #NUM! error.

DAYS function examples
----------------------

[![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")](https://exceljet.net/formulas/get-days-between-dates)

### [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)

Dates in Excel are serial numbers that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this: =C6-B6 =...

Related functions
-----------------

[![Excel YEARFRAC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_yearfrac_function.png "Excel YEARFRAC function")](https://exceljet.net/functions/yearfrac-function)

### [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)

The Excel YEARFRAC function returns a decimal value that represents fractional years between two dates. You can use YEARFRAC to do things like calculate age with a birthdate....

[![Excel DAYS360 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20days360%20function.png "Excel DAYS360 function")](https://exceljet.net/functions/days360-function)

### [DAYS360 Function](https://exceljet.net/functions/days360-function)

The Excel DAYS360 function returns the number of days between two dates based on a 360-day year, where all months are assumed to have 30 days. For example, the formula =DAYS360("1-Jan-2021","31-Dec-2021") returns 360 days.

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

*   [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)
    

### Functions

*   [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)
    
*   [DAYS360 Function](https://exceljet.net/functions/days360-function)
    
*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)
    

### Links

*   [Microsoft DAYS function documentation](https://support.office.com/en-us/article/days-function-57740535-d549-4395-8728-0f07bff0b9df)
    

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
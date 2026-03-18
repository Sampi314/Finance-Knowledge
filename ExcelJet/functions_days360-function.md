# Excel DAYS360 function | Exceljet

**Source:** https://exceljet.net/functions/days360-function

---

[Skip to main content](https://exceljet.net/functions/days360-function#main-content)

[](https://exceljet.net/functions/days360-function#)

*   [Previous](https://exceljet.net/functions/days-function)
    
*   [Next](https://exceljet.net/functions/edate-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

DAYS360 Function
================

by Dave Bruns · Updated 13 Jul 2021

Related functions 
------------------

[YEARFRAC](https://exceljet.net/functions/yearfrac-function)

[DAYS](https://exceljet.net/functions/days-function)

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[DATEDIF](https://exceljet.net/functions/datedif-function)

![Excel DAYS360 function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20days360%20function.png "Excel DAYS360 function")

Summary
-------

The Excel DAYS360 function returns the number of days between two dates based on a 360-day year, where all months are assumed to have 30 days. For example, the formula =DAYS360("1-Jan-2021","31-Dec-2021") returns 360 days.

Purpose 
--------

Get days between 2 dates in a 360-day year

Return value 
-------------

A number representing days.

Syntax
------

    =DAYS360(start_date,end_date,[method])

*   _start\_date_ - The start date.
*   _end\_date_ - The end date.
*   _method_ - \[optional\] Day count method. FALSE (default) = US method, TRUE = European method.

Using the DAYS360 function 
---------------------------

The DAYS360 function returns the number of days between two dates, based on a year where all months have 30 days. Both dates must be [valid Excel dates](https://exceljet.net/glossary/excel-date)
 or text values that can be parsed as dates. The DAYS360 function only works with whole numbers, time values are ignored. 

### Method

DAYS360 takes an optional argument called _method_ that can be set to either TRUE or FALSE. When _method_ is FALSE (default) DAYS360 uses a US method to compute days. When the start date is the last day of the month, it is treated like the 30th day of that month. When the end date is the last day of the month, and the start date is less than 30, the end date is treated as the 1st of the _next_ month, otherwise the end date is treated like the 30th of the same month.

If _method_ is set to TRUE, DAYS360 uses a European method to calculate days. In this scheme, start and end dates equal to the 31st of a month are set to the 30th of the same month.

### Examples

In the formula below, DAYS360 returns 360 days with a start date of January 1, 2021 and an end date of December 31, 2021.

    =DAYS360("1-Jan-2021","31-Dec-2021") // returns 360
    

The result of 360 is based on 12 months \* 30 days in each month. 

_Note: In general, storing and parsing text values that represent dates is bad form and should be avoided, because it can introduce errors and parsing problems. Working with native [Excel dates](https://exceljet.net/glossary/excel-date)
 is a better approach._

With a start date of July 1, 2021 in A1, and an end date of December 31, 2021 in B1, the formula below returns 180:

    =DAYS360(A1,B1) // returns 180
    

To create a date from scratch in a formula, use the [DATE function](https://exceljet.net/functions/date-function)
. The formula below returns 90:

    =DAYS360(DATE(2021,1,1),DATE(2021,4,1)) // returns 90
    

### Notes

*   The DAYS360 function only works with whole numbers and ignores time.
*   If dates are not recognized, DAYS360 returns the #VALUE! error.
*   If dates are out of range, DAYS360 returns the #NUM! error.

Related functions
-----------------

[![Excel YEARFRAC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_yearfrac_function.png "Excel YEARFRAC function")](https://exceljet.net/functions/yearfrac-function)

### [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)

The Excel YEARFRAC function returns a decimal value that represents fractional years between two dates. You can use YEARFRAC to do things like calculate age with a birthdate....

[![Excel DAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20days%20function.png "Excel DAYS function")](https://exceljet.net/functions/days-function)

### [DAYS Function](https://exceljet.net/functions/days-function)

The Excel DAYS function returns the number of days between two dates. With a start date in A1 and end date in B1, =DAYS(B1,A1) will return the days between the two dates.

[![Excel NETWORKDAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays%20function.png "Excel NETWORKDAYS function")](https://exceljet.net/functions/networkdays-function)

### [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can _optionally_ exclude a list of holidays supplied as dates. ...

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

### Functions

*   [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)
    
*   [DAYS Function](https://exceljet.net/functions/days-function)
    
*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    

### Links

*   [Microsoft DAYS360 function documentation](https://support.office.com/en-us/article/days360-function-b9a509fd-49ef-407e-94df-0cbda5718c2a)
    

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
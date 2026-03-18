# Get week number from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-week-number-from-date

---

[Skip to main content](https://exceljet.net/formulas/get-week-number-from-date#main-content)

[](https://exceljet.net/formulas/get-week-number-from-date#)

*   [Previous](https://exceljet.net/formulas/get-same-date-next-year)
    
*   [Next](https://exceljet.net/formulas/get-work-hours-between-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get week number from date
=========================

by Dave Bruns · Updated 27 Sep 2020

Related functions 
------------------

[WEEKNUM](https://exceljet.net/functions/weeknum-function)

[ISOWEEKNUM](https://exceljet.net/functions/isoweeknum-function)

![Excel formula: Get week number from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20week%20number%20from%20date.png "Excel formula: Get week number from date")

Summary
-------

To get the week number from a date, you can use the [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
. In the example shown, the formula in C5, copied down, is:

    =WEEKNUM(B5)
    

Generic formula
---------------

    =WEEKNUM(date)

Explanation 
------------

The [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
 takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting with the week that contains January 1. WEEKNUM takes two arguments: a _date_, and (optionally) _return\_type_, which controls the scheme used to calculate the week number. 

By default, the WEEKNUM function uses a scheme where week 1 begins on January 1, and week 2 begins on the next Sunday (when the return\_type argument is omitted, or supplied as 1). With a return\_type of 2, week 1 begins on January 1, and week 2 begins on the next Monday. See the [WEEKNUM page](https://exceljet.net/functions/weeknum-function)
 for more information.

### ISO week number

ISO week numbers, start on the Monday of the first week in a year _with a Thursday_. This means that the first day of the year for ISO weeks is always a Monday in the period between Jan 29 and Jan 4. Starting with Excel 2010, you can generate an ISO week number using 21 as the return\_type:

    =WEEKNUM(date,21)
    

Starting in Excel 2013, there is a new function called [ISOWEEKNUM](https://exceljet.net/functions/isoweeknum-function)
.

For more details, see [Ron de Bruin's nice write-up on Excel week numbers](http://www.rondebruin.nl/win/s8/win001.htm)
.

Related formulas
----------------

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

[![Excel formula: Get month from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_month_from_date.png "Excel formula: Get month from date")](https://exceljet.net/formulas/get-month-from-date)

### [Get month from date](https://exceljet.net/formulas/get-month-from-date)

The MONTH function takes just one argument, the date from which to extract the month. In the example shown, the formula is: =MONTH(B4) where B4 contains the date January 5, 2016. The MONTH function returns the number 1 representing the month( January) of the date. Note that you can use MONTH to...

[![Excel formula: Get year from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_year_from_date.png "Excel formula: Get year from date")](https://exceljet.net/formulas/get-year-from-date)

### [Get year from date](https://exceljet.net/formulas/get-year-from-date)

In this example, the goal is to extract the year number from a list of dates in column B. This can be easily achieved with the YEAR function . The YEAR function takes just one argument, the date from which you want to extract the year. For example, in the formula below, we pass the "12-Dec-1999"...

Related functions
-----------------

[![Excel WEEKNUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weeknum%20function.png "Excel WEEKNUM function")](https://exceljet.net/functions/weeknum-function)

### [WEEKNUM Function](https://exceljet.net/functions/weeknum-function)

The Excel WEEKNUM function takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting on the week that contains January 1. By default, weeks begin on Sunday, but this can be changed.

[![Excel ISOWEEKNUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isoweeknum%20function.png "Excel ISOWEEKNUM function")](https://exceljet.net/functions/isoweeknum-function)

### [ISOWEEKNUM Function](https://exceljet.net/functions/isoweeknum-function)

The Excel ISOWEEKNUM function takes a date and returns a week number (1-54) that follows ISO standards, where weeks begin on Monday and week number 1 is assigned to the first week in a year that contains a Thursday.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)
    
*   [Get month from date](https://exceljet.net/formulas/get-month-from-date)
    
*   [Get year from date](https://exceljet.net/formulas/get-year-from-date)
    

### Functions

*   [WEEKNUM Function](https://exceljet.net/functions/weeknum-function)
    
*   [ISOWEEKNUM Function](https://exceljet.net/functions/isoweeknum-function)
    

### Links

*   [Week numbers in Excel (Ron de Bruin)](http://www.rondebruin.nl/win/s8/win001.htm)
    

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
# Excel ISOWEEKNUM function | Exceljet

**Source:** https://exceljet.net/functions/isoweeknum-function

---

[Skip to main content](https://exceljet.net/functions/isoweeknum-function#main-content)

[](https://exceljet.net/functions/isoweeknum-function#)

*   [Previous](https://exceljet.net/functions/hour-function)
    
*   [Next](https://exceljet.net/functions/minute-function)
    

Excel 2013

[Date and time](https://exceljet.net/functions#Date-and-time)

ISOWEEKNUM Function
===================

by Dave Bruns · Updated 30 May 2021

Related functions 
------------------

[WEEKNUM](https://exceljet.net/functions/weeknum-function)

![Excel ISOWEEKNUM function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20isoweeknum%20function.png "Excel ISOWEEKNUM function")

Summary
-------

The Excel ISOWEEKNUM function takes a date and returns a week number (1-54) that follows ISO standards, where weeks begin on Monday and week number 1 is assigned to the first week in a year that contains a Thursday.

Purpose 
--------

Get ISO week number for a given date

Return value 
-------------

A number between 1 and 54.

Syntax
------

    =ISOWEEKNUM(date)

*   _date_ - A valid Excel date in serial number format.

Using the ISOWEEKNUM function 
------------------------------

The ISOWEEKNUM function returns a week number based on ISO standards. Under this standard, weeks begin on Monday and the week number 1 is assigned to the first week in a year that contains a Thursday, following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Week_dates)
.

ISOWEEKNUM takes just one argument, _date_, which must be a valid Excel date.

### Examples

In the example shown, the formula in D5, copied down, is:

    =WEEKNUM(B5) // default week number
    

The formula in E5, copied down the table, is:

    =ISOWEEKNUM(C5) // ISO week number
    

By default the standard [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
 will start week number 1 on the first day of the year, then increment week numbers on Sundays after that. The ISOWEEKNUM function increments on Mondays, and starts week 1 on the first week that contains a Thursday.

The WEEKNUM function can also be configured to output an ISO week number, by setting the return\_type [argument](https://exceljet.net/glossary/function-argument)
 to 21. The formula below will output the same week numbers seen in column E of the example:

    =WEEKNUM(B5,21) // ISO week number
    

### Notes

*   ISOWEEKNUM returns #VALUE! if _date_ is not recognized as a valid date.
*   ISOWEEKNUM returns #NUM! if _date_ is out of range.

ISOWEEKNUM function examples
----------------------------

[![Excel formula: Get week number from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20week%20number%20from%20date.png "Excel formula: Get week number from date")](https://exceljet.net/formulas/get-week-number-from-date)

### [Get week number from date](https://exceljet.net/formulas/get-week-number-from-date)

The WEEKNUM function takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting with the week that contains January 1. WEEKNUM takes two arguments: a date , and (optionally) return\_type , which controls the scheme used to calculate the...

Related functions
-----------------

[![Excel WEEKNUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weeknum%20function.png "Excel WEEKNUM function")](https://exceljet.net/functions/weeknum-function)

### [WEEKNUM Function](https://exceljet.net/functions/weeknum-function)

The Excel WEEKNUM function takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting on the week that contains January 1. By default, weeks begin on Sunday, but this can be changed.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get week number from date](https://exceljet.net/formulas/get-week-number-from-date)
    

### Functions

*   [WEEKNUM Function](https://exceljet.net/functions/weeknum-function)
    

### Links

*   [Microsoft ISOWEEKNUM function documentation](https://support.office.com/en-us/article/isoweeknum-function-1c2d0afe-d25b-4ab1-8894-8d0520e90e0e)
    

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
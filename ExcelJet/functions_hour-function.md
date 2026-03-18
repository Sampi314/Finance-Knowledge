# Excel HOUR function | Exceljet

**Source:** https://exceljet.net/functions/hour-function

---

[Skip to main content](https://exceljet.net/functions/hour-function#main-content)

[](https://exceljet.net/functions/hour-function#)

*   [Previous](https://exceljet.net/functions/eomonth-function)
    
*   [Next](https://exceljet.net/functions/isoweeknum-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

HOUR Function
=============

by Dave Bruns · Updated 30 May 2021

Related functions 
------------------

[HOUR](https://exceljet.net/functions/hour-function)

[MINUTE](https://exceljet.net/functions/minute-function)

[SECOND](https://exceljet.net/functions/second-function)

[TIME](https://exceljet.net/functions/time-function)

![Excel HOUR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_hour_function.png "Excel HOUR function")

Summary
-------

The Excel HOUR function returns the hour component of a time as a number between 0-23. For example, with a time of 9:30 AM, HOUR will return 9. You can use the HOUR function to extract the hour into a cell, or feed the result into another formula, like the [TIME function](https://exceljet.net/functions/time-function)
.

Purpose 
--------

Get the hour as a number (0-23) from a Time

Return value 
-------------

A number between 0 and 23.

Syntax
------

    =HOUR(serial_number)

*   _serial\_number_ - A valid Excel time.

Using the HOUR function 
------------------------

The HOUR function returns the hour portion of a time as a number between 0-23. For example, with a time of 9:00 AM, HOUR will return 9. HOUR takes just one [argument](https://exceljet.net/glossary/function-argument)
, _serial\_number_, which must be a valid [Excel date](https://exceljet.net/glossary/excel-date)
 or a valid [Excel time](https://exceljet.net/glossary/excel-time)
.

Times can be supplied to the HOUR function as text (e.g. "7:45 PM") or as decimal numbers (e.g. 0.5, which equals 12:00 PM). To create a time value from scratch with separate hour, minute, and second inputs, use the [TIME function](https://exceljet.net/functions/time-function)
.

The HOUR function will "reset" to 0 every 24 hours (like a clock). To work with hour values larger than 24, use a formula to [convert time to decimal hours](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
.

### Example #1 - Hour from time

The HOUR function returns the hour from of a time or date as a number between 0-23. For example:

    =HOUR("9:00 AM") // returns 9
    =HOUR("9:00 PM") // returns 21
    

### Example #2 - Minutes ignored

The HOUR function ignores minutes and seconds. For example, when given the time "6:30 PM", HOUR returns 18:

    =HOUR("6:30 PM") // returns 18
    

### Example #3 - Hour from date

Some Excel dates include time. When given a date that includes time, the HOUR function will extract the hour and ignore the date. For example, with 29-May-2021 6:00 AM in cell A1:

    =HOUR(A1) // returns 6
    

The date portion of the value is ignored completely. If the date contains no time value, HOUR returns 0 (zero) which is midnight.

### Example #4 - with TIME function

You can use the HOUR function to extract the hour and feed the result into another formula, like the TIME function. For example, with the time "8:00 AM" in A1, you could force the time to be on the half-hour with:

    =TIME(HOUR(A1),30,0) // returns 8:30 AM
    

_Note: Excel stores [dates](https://exceljet.net/glossary/excel-date)
 and [times](https://exceljet.net/glossary/excel-time)
 as serial numbers. For example, the date Jan 1, 2000 12:00 PM is equal to the serial number 32526.5 in Excel. To check that Excel is correctly recognizing a date or time, you can temporarily format the date as a number._

### Notes

*   HOUR returns #VALUE! if _serial\_number_ is not recognized as a valid date or time.
*   HOUR returns #NUM! if _serial\_number_ is out of range.

HOUR function examples
----------------------

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

HOUR function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20work%20with%20times-thumb.png)](https://exceljet.net/videos/how-to-work-with-times)

### [How to work with times](https://exceljet.net/videos/how-to-work-with-times)

Excel contains functions that will let you extract the hour, minute, and second values from a time, and a function called TIME that will let you put them back together again. Let's take a look. Here we have a set of random times in column B. First, I'll add a formula to column C to pick up the time...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20date%20and%20time%20series%20with%20formulas-thumb.png)](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

### [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)

Although you can use Excel's AutoFill feature to fill in a series of dates and times, you can also do the same thing with formulas. The advantage of using a formula is that you can easily change the starting value and generate a new series. Let's take a look. Often you'll need to generate a series...

Related functions
-----------------

[![Excel HOUR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_hour_function.png "Excel HOUR function")](https://exceljet.net/functions/hour-function)

### [HOUR Function](https://exceljet.net/functions/hour-function)

The Excel HOUR function returns the hour component of a time as a number between 0-23. For example, with a time of 9:30 AM, HOUR will return 9. You can use the HOUR function to extract the hour into a cell, or feed the result into another formula, like the [TIME](https://exceljet.net/functions/time-function)
...

[![Excel MINUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20minute%20function.png "Excel MINUTE function")](https://exceljet.net/functions/minute-function)

### [MINUTE Function](https://exceljet.net/functions/minute-function)

The Excel MINUTE function extracts the minute component of a time as a number between 0-59. For example, with a time of 9:45 AM, minute will return 45. You can use the MINUTE function to extract the minute into a cell, or feed the result into another function like the ...

[![Excel SECOND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_second_function.png "Excel SECOND function")](https://exceljet.net/functions/second-function)

### [SECOND Function](https://exceljet.net/functions/second-function)

The Excel SECOND function extracts the seconds component of a time as a number between 0-59. For example, when given the time 9:10:15 AM, SECOND will return 15. You can use the SECOND function to extract seconds into another cell.

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    

### Videos

*   [How to create date and time series with formulas](https://exceljet.net/videos/how-to-create-date-and-time-series-with-formulas)
    
*   [How to work with times](https://exceljet.net/videos/how-to-work-with-times)
    

### Functions

*   [HOUR Function](https://exceljet.net/functions/hour-function)
    
*   [MINUTE Function](https://exceljet.net/functions/minute-function)
    
*   [SECOND Function](https://exceljet.net/functions/second-function)
    
*   [TIME Function](https://exceljet.net/functions/time-function)
    

### Links

*   [Microsoft HOUR function documentation](https://support.office.com/en-us/article/hour-function-a3afa879-86cb-4339-b1b5-2dd2d7310ac7)
    

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
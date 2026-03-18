# Excel SECOND function | Exceljet

**Source:** https://exceljet.net/functions/second-function

---

[Skip to main content](https://exceljet.net/functions/second-function#main-content)

[](https://exceljet.net/functions/second-function#)

*   [Previous](https://exceljet.net/functions/now-function)
    
*   [Next](https://exceljet.net/functions/time-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

SECOND Function
===============

by Dave Bruns · Updated 3 May 2024

Related functions 
------------------

[HOUR](https://exceljet.net/functions/hour-function)

[MINUTE](https://exceljet.net/functions/minute-function)

[SECOND](https://exceljet.net/functions/second-function)

[TIME](https://exceljet.net/functions/time-function)

![Excel SECOND function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_second_function.png "Excel SECOND function")

Summary
-------

The Excel SECOND function extracts the seconds component of a time as a number between 0-59. For example, when given the time 9:10:15 AM, SECOND will return 15. You can use the SECOND function to extract seconds into another cell.

Purpose 
--------

Get the Second as a number (0-59) from a Time

Return value 
-------------

A number between 0 and 59

Syntax
------

    =SECOND(serial_number)

*   _serial\_number_ - A valid time in a format Excel recognizes.

Using the SECOND function 
--------------------------

The SECOND function extracts the second component from a time as a number between 0-59. For example, given a time of "12:15:01", SECOND will return 1. The SECOND function takes just one [argument](https://exceljet.net/glossary/function-argument)
, _serial\_number_, which must be a valid [Excel date](https://exceljet.net/glossary/excel-date)
, a valid [Excel time](https://exceljet.net/glossary/excel-time)
, or a text value Excel can interpret as a time (e.g. "7:45:30 PM").

The SECOND function does not convert time into seconds but rather _extracts_ the seconds component from time. For example, given a time duration of 10 minutes (600 seconds) the SECONDS function will return 0 (zero), since seconds are zero in the time 10:00. This means the SECOND function will "reset" to 0 every 60 seconds (like a clock). To convert a time value into decimal seconds, [see this example](https://exceljet.net/formulas/convert-excel-time-to-decimal-seconds)
. To create a time value from scratch with separate hour, minute, and second inputs, use the [TIME function](https://exceljet.net/functions/time-function)
.

### Examples

When given the time "10:45:17 AM", the SECOND function will return 17:

    =SECOND("10:45:17 AM") // returns 17
    

With the time "2:19:36" in cell A1, SECOND will return 36:

    =SECOND(A1) // returns 36

The formula below demonstrates how the TIME function can be used to create the time 9:30:45 in Excel:

    =TIME(9,30,45)
    

If we wrap the SECONDS function around the TIME function, we get 45, as expected:

    =SECOND(TIME(9,30,45)) // returns 45
    

_Note: Excel stores [dates as serial numbers](https://exceljet.net/glossary/excel-date)
 and [times as decimal numbers](https://exceljet.net/glossary/excel-time)
. For example, the time 12:00 PM is equal to 0.5 (one half-day), and the date Jan 1, 2000 12:00 PM is equal to the serial number 32526.5 in Excel._ 

### Fractional seconds

One notable limitation of the SECOND function is that it _rounds_ fractional seconds to the nearest second. You can see this behavior in the worksheet below. The SECOND function is configured to extract seconds from the times in column C, which are recorded in hundredths of a second. During this operation, the fractional part of the number is lost when it is rounded:

![Excel's SECOND function rounds fractional seconds](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/SECOND_function_rounds_fractional_seconds.png "Excel's SECOND function rounds fractional seconds")

To extract fractional seconds while maintaining precision, you can use a formula like this:

    =MOD(C5*1440,1)*60

For a detailed explanation of this formula, see [Time in hundredths of a second](https://exceljet.net/formulas/time-in-hundredths-of-a-second)
.

SECOND function examples
------------------------

[![Excel formula: Time in hundredths of a second](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time_in_hundredths_of_a_second.png "Excel formula: Time in hundredths of a second")](https://exceljet.net/formulas/time-in-hundredths-of-a-second)

### [Time in hundredths of a second](https://exceljet.net/formulas/time-in-hundredths-of-a-second)

In the worksheet shown, we have race results for an 800m race. The goal is to display time in minutes, seconds, and hundredths of a second (centiseconds). Dealing with times that include fractional seconds can be tricky in Excel. The default time format will only show whole seconds and it is not...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

SECOND function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20work%20with%20times-thumb.png)](https://exceljet.net/videos/how-to-work-with-times)

### [How to work with times](https://exceljet.net/videos/how-to-work-with-times)

Excel contains functions that will let you extract the hour, minute, and second values from a time, and a function called TIME that will let you put them back together again. Let's take a look. Here we have a set of random times in column B. First, I'll add a formula to column C to pick up the time...

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
    
*   [Time in hundredths of a second](https://exceljet.net/formulas/time-in-hundredths-of-a-second)
    

### Videos

*   [How to work with times](https://exceljet.net/videos/how-to-work-with-times)
    

### Functions

*   [HOUR Function](https://exceljet.net/functions/hour-function)
    
*   [MINUTE Function](https://exceljet.net/functions/minute-function)
    
*   [SECOND Function](https://exceljet.net/functions/second-function)
    
*   [TIME Function](https://exceljet.net/functions/time-function)
    

### Links

*   [Microsoft SECOND function documentation](https://support.office.com/en-us/article/second-function-740d1cfc-553c-4099-b668-80eaa24e8af1)
    

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
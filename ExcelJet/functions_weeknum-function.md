# Excel WEEKNUM function | Exceljet

**Source:** https://exceljet.net/functions/weeknum-function

---

[Skip to main content](https://exceljet.net/functions/weeknum-function#main-content)

[](https://exceljet.net/functions/weeknum-function#)

*   [Previous](https://exceljet.net/functions/weekday-function)
    
*   [Next](https://exceljet.net/functions/workday-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

WEEKNUM Function
================

by Dave Bruns · Updated 1 Dec 2023

Related functions 
------------------

[ISOWEEKNUM](https://exceljet.net/functions/isoweeknum-function)

![Excel WEEKNUM function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20weeknum%20function.png "Excel WEEKNUM function")

Summary
-------

The Excel WEEKNUM function takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting on the week that contains January 1. By default, weeks begin on Sunday, but this can be changed.

Purpose 
--------

Get the week number for a given date

Return value 
-------------

A number between 1 and 54.

Syntax
------

    =WEEKNUM(serial_num,[return_type])

*   _serial\_num_ - A valid Excel date in serial number format.
*   _return\_type_ - \[optional\] The day the week begins. Default is 1.

Using the WEEKNUM function 
---------------------------

The WEEKNUM function takes a date and returns a number between 1 and 54 that corresponds to the week of the year. By default, the WEEKNUM function starts counting on the week that contains January 1 and increments week numbers on Sunday. Typically the last week number in a year is 53. However, WEEKNUM will return 54 at the end of some years, like 2000 and 2028.

The WEEKNUM function accepts two [arguments](https://exceljet.net/glossary/function-argument)
, _serial\_num_ and _return\_type_. The _serial\_num_ argument must have a [valid Excel date](https://exceljet.net/glossary/excel-date)
. The _return\_type_ argument controls what day of the week begins a new week number. _Return\_type_ is optional and defaults to 1, which sets new week numbers to start on Sunday. When _return\_type_ is set to 2, week numbers begin on Monday. 

With a return\_type of 1-17, week number 1 in a given year is assigned to the week that contains January 1. With _return\_type_ 21, week 1 is the week containing the first Thursday of the year, following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Week_dates)
. The table below summarizes _return\_type_ options_._

| Return\_type | Week begins |
| --- | --- |
| 1 (default) | Sunday |
| 2   | Monday |
| 11  | Monday |
| 12  | Tuesday |
| 13  | Wednesday |
| 14  | Thursday |
| 15  | Friday |
| 16  | Saturday |
| 17  | Sunday |
| 21  | Monday (see note above) |

### Example #1 - basic usage

The formulas below return the week number for the last day of 2020 and the first day of 2021:

    =WEEKNUM("31-Dec-2020") // returns 53
    =WEEKNUM("1-Jan-2021") // returns 1
    

### Example #2 - return type

The _return\_type_ argument controls what day of the week a new week number should begin. By default, _return\_type_ is 1, and numbers increment on Sunday. When _return\_type_ is provided as 2, week numbers begin on Monday. For example, January 3, 2021, is a Sunday and, WEEKNUM will return 2 since new numbers start on Sundays:

    =WEEKNUM("3-Jan-2021") // returns 2
    

However, when _return\_type_ is set to 2, WEEKNUM will return 1 and start week 2 on Monday:

    =WEEKNUM("3-Jan-2021",2) // returns 1
    =WEEKNUM("4-Jan-2021",2) // returns 2
    

_Note: the examples above show dates as [text values](https://exceljet.net/glossary/text-value)
 for readability, but working with native [Excel dates](https://exceljet.net/glossary/excel-date)
 is more reliable. To create a date from scratch in a formula, you can use the [DATE function](https://exceljet.net/functions/date-function)
._

WEEKNUM function examples
-------------------------

[![Excel formula: Pad week numbers with zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20week%20numbers%20with%20zeros.png "Excel formula: Pad week numbers with zeros")](https://exceljet.net/formulas/pad-week-numbers-with-zeros)

### [Pad week numbers with zeros](https://exceljet.net/formulas/pad-week-numbers-with-zeros)

The TEXT function can apply number formats of any kind, including currency, date, percentage, etc. By applying a number format like "00", "000", "0000", you can "pad" numbers with as many zeros as you like. Zeros will only be added where needed. Number format only The TEXT function converts numbers...

[![Excel formula: Get week number from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20week%20number%20from%20date.png "Excel formula: Get week number from date")](https://exceljet.net/formulas/get-week-number-from-date)

### [Get week number from date](https://exceljet.net/formulas/get-week-number-from-date)

The WEEKNUM function takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting with the week that contains January 1. WEEKNUM takes two arguments: a date , and (optionally) return\_type , which controls the scheme used to calculate the...

[![Excel formula: Sum by week number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week%20number.png "Excel formula: Sum by week number")](https://exceljet.net/formulas/sum-by-week-number)

### [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)

In this example, the goal is to sum the amounts in column D by week number, using the dates in column C to determine the week number. The week numbers in column G are manually entered. The final results should appear in column H. All data is in an Excel Table named data in the range B5:E16. This...

Related functions
-----------------

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

*   [Get week number from date](https://exceljet.net/formulas/get-week-number-from-date)
    
*   [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)
    
*   [Pad week numbers with zeros](https://exceljet.net/formulas/pad-week-numbers-with-zeros)
    

### Functions

*   [ISOWEEKNUM Function](https://exceljet.net/functions/isoweeknum-function)
    

### Links

*   [Microsoft WEEKNUM function documentation](https://support.office.com/en-us/article/weeknum-function-e5c43a03-b4ab-426c-b411-b18c13c75340)
    

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
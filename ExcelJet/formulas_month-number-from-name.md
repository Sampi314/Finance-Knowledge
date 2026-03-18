# Month number from name - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/month-number-from-name

---

[Skip to main content](https://exceljet.net/formulas/month-number-from-name#main-content)

[](https://exceljet.net/formulas/month-number-from-name#)

*   [Previous](https://exceljet.net/formulas/list-holidays-between-two-dates)
    
*   [Next](https://exceljet.net/formulas/next-anniversary-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Month number from name
======================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[MONTH](https://exceljet.net/functions/month-function)

[DATEVALUE](https://exceljet.net/functions/datevalue-function)

![Excel formula: Month number from name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/month%20number%20from%20name.png "Excel formula: Month number from name")

Summary
-------

To get a standard month number from a month name (i.e. 1 from "January", 2 from "February", 3 from "March", etc.) you can use the MONTH function and a bit of [concatenation](https://exceljet.net/glossary/concatenation)
. In the example shown, the formula in cell C5 is:

    =MONTH(B5&1)
    

As the formula is copied down the column, it returns the correct number for each month.

Generic formula
---------------

    =MONTH("name"&1)

Explanation 
------------

In this example, the goal is to return a number, 1-12, for any month name of the year. For example, given the string "January" we want to return 1, "February" should return 2, and so on. If we had a valid [Excel date](https://exceljet.net/glossary/excel-date)
, we could use a [number format](https://exceljet.net/glossary/number-format)
 for this task, but because we are starting with a [text string](https://exceljet.net/glossary/text-value)
, we need another way. The approach we take in this example is to create a date fragment that can be correctly interpreted by Excel as a valid date. In the example shown, the formula in cell C5 is:

    =MONTH(B5&1) // returns 1
    

Working from the inside out, we start by [concatenating](https://exceljet.net/glossary/concatenation)
 the name in cell B5 to the number 1:

    B5&1 // returns "January1"
    

This expression returns a string like "January1", "February1", "March1",and so on. It turns out, that if we pass a date fragment like this into the [MONTH function](https://exceljet.net/functions/month-function)
, it will coerce the string to a valid date, using the current year.  As I write this, the year is 2021, so the result for January is the date January 1, 2021, represented in Excel as the serial number 44197.

After this date has been created, the MONTH function returns the correct month number for the date that was created using concatenation. In each case, the actual date value is a "throwaway", used only as a convenient value to pass into the MONTH function. In B5 the evaluation works like this (in the year 2021):

    =MONTH(B5&1)
    =MONTH("January1")
    =MONTH(44197)
    =1
    

### Date evaluation

This example is a bit tricky in that the evaluation of the date inside the MONTH function is automatic. If you use the expression that concatenates the month name to 1 _outside_ the MONTH function, you'll need to add an extra step to get Excel to convert the text to a date.  The [DATEVALUE function](https://exceljet.net/functions/datevalue-function)
 or adding zero are both good options:

    =DATEVALUE(B5&1)
    =(B5&1)+0
    

Both will return a date serial number, which must then be [formatted](https://exceljet.net/glossary/number-format)
 as a date.

Related formulas
----------------

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

[![Excel formula: Get month from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_month_from_date.png "Excel formula: Get month from date")](https://exceljet.net/formulas/get-month-from-date)

### [Get month from date](https://exceljet.net/formulas/get-month-from-date)

The MONTH function takes just one argument, the date from which to extract the month. In the example shown, the formula is: =MONTH(B4) where B4 contains the date January 5, 2016. The MONTH function returns the number 1 representing the month( January) of the date. Note that you can use MONTH to...

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

[![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")](https://exceljet.net/formulas/convert-text-to-date)

### [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)

The DATE function creates a valid date using three arguments: year, month, and day: =DATE(year,month,day) In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function: =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,...

Related functions
-----------------

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel DATEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20datevalue.png "Excel DATEVALUE function")](https://exceljet.net/functions/datevalue-function)

### [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)

The Excel DATEVALUE function converts a date represented as a [text string](https://exceljet.net/glossary/text-value)
 into a [valid Excel date](https://exceljet.net/glossary/excel-date)
. For example, the formula =DATEVALUE("3/10/1975") returns a serial number (27463) in the Excel date system that represents March...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    
*   [Get month from date](https://exceljet.net/formulas/get-month-from-date)
    
*   [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)
    
*   [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)
    
*   [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
    

### Functions

*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)
    

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
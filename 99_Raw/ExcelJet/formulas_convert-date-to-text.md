# Convert date to text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-date-to-text

---

[Skip to main content](https://exceljet.net/formulas/convert-date-to-text#main-content)

[](https://exceljet.net/formulas/convert-date-to-text#)

*   [Previous](https://exceljet.net/formulas/convert-date-to-month-and-year)
    
*   [Next](https://exceljet.net/formulas/convert-decimal-hours-to-excel-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert date to text
====================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")

Summary
-------

To convert dates to text (i.e. date to string conversion), you can use the [TEXT function](https://exceljet.net/functions/text-function)
. The TEXT function can use patterns like "dd/mm/yyyy", "yyyy-mm-dd", etc. to convert a valid date to a text value. See table below for a list of available tokens.

Generic formula
---------------

    =TEXT(date,format)

Explanation 
------------

Dates and times in Excel are stored as [serial numbers](https://exceljet.net/glossary/excel-date)
 and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text in a preferred format. For example, if the date January 9, 2000, is entered in cell A1, you can use TEXT to convert this date into the following text strings as follows:

    =TEXT(A1,"mmm")            // "Jan"
    =TEXT(A1,"dd/mm/yyyy")     // "09/01/2012"
    =TEXT(A1,"dd-mmm-yy")      // "09-Jan-12"
    
    

**Date format codes**

Assuming a date of January 9, 2012, here is a more complete set of formatting codes for a date, along with sample output.

|     |     |
| --- | --- |
| Format code | Output |
| d   | 9   |
| dd  | 09  |
| ddd | Mon |
| dddd | Monday |
| m   | 1   |
| mm  | 01  |
| mmm | Jan |
| mmmm | January |
| mmmmm | J   |
| yy  | 12  |
| yyyy | 2012 |
| mm/dd/yyyy | 01/09/2012 |
| m/d/y | 1/9/12 |
| ddd, mmm d | Mon, Jan 9 |
| mm/dd/yyyy h:mm AM/PM | 01/09/2012 5:15 PM |
| dd/mm/yyyy hh:mm:ss | 09/01/2012 17:15:00 |

You can use the [TEXT function](https://exceljet.net/functions/text-function)
 to convert dates or any numeric value to a fixed text format. You can explore available formats by navigating to Format Cells (Win: Ctrl + 1, Mac: Cmd + 1) and selecting various format categories in the list to the left. Also, see [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
.

Related formulas
----------------

[![Excel formula: Join date and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_date_and_text.png "Excel formula: Join date and text")](https://exceljet.net/formulas/join-date-and-text)

### [Join date and text](https://exceljet.net/formulas/join-date-and-text)

In this example, the goal is to join a text string to a formatted date. The challenge is that numbers lose their formatting in Excel when they are concatenated in a formula. For example, if we have the date 31-Dec-1999 in cell B5, and we join B5 to a text string and don't control the date format...

[![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")](https://exceljet.net/formulas/get-day-name-from-date)

### [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday, etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches: Display date with a custom number format Convert date to day name with TEXT...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

[![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")](https://exceljet.net/formulas/convert-text-to-date)

### [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)

The DATE function creates a valid date using three arguments: year, month, and day: =DATE(year,month,day) In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function: =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Join date and text](https://exceljet.net/formulas/join-date-and-text)
    
*   [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)
    
*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    
*   [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Articles

*   [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
    

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
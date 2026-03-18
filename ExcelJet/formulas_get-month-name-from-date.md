# Get month name from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-month-name-from-date

---

[Skip to main content](https://exceljet.net/formulas/get-month-name-from-date#main-content)

[](https://exceljet.net/formulas/get-month-name-from-date#)

*   [Previous](https://exceljet.net/formulas/get-month-from-date)
    
*   [Next](https://exceljet.net/formulas/get-months-between-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get month name from date
========================

by Dave Bruns · Updated 30 May 2021

Related functions 
------------------

[MONTH](https://exceljet.net/functions/month-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")

Summary
-------

To get the month name (i.e. January, February, March, etc.) from a date as text, you can use the [TEXT function](https://exceljet.net/functions/text-function)
 with a custom [number format](https://exceljet.net/articles/custom-number-formats)
. In the example shown, the formula in cell C5, copied down, is:

    =TEXT(B4,"mmmm")
    

As the formula is copied down, the TEXT function extracts a month name from each date in column B.

Generic formula
---------------

    =TEXT(date,"mmmm")

Explanation 
------------

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a [valid Excel](https://exceljet.net/glossary/excel-date)
 using the month name.

To extract the month name from a date as _text_, you can use the [TEXT function](https://exceljet.net/functions/text-function)
 with a [custom number format](https://exceljet.net/articles/custom-number-formats)
 like "mmmm", or "mmm". In the example shown, the formula in cell C4 is:

    =TEXT(B4,"mmmm") // returns "April"
    

The TEXT function converts values to text using the number format that you provide. Note that the date is lost in the conversion: only the text for the month name remains. To extract an abbreviated month name like "Jan", "Feb", etc. use a slightly different number format:

    =TEXT(B4,"mmm") // returns "Apr"
    

### Display month name

If you only want to _display_ a month name, you don't need a formula – you can use a [custom number format](https://exceljet.net/articles/custom-number-formats)
 to format the date directly. Select the date and navigate to [Format cells](https://exceljet.net/shortcuts/format-almost-anything)
 (Ctrl + 1 or Cmd +1), then select Custom and enter one of these custom formats:

    "mmm"  // "Jan"
    "mmmm" // "January"
    

Excel will display only the month name, but it will leave the date value intact. You can also use a longer date format like this:

    "mmmm d, yyyy" // "January 1, 2021
    

### CHOOSE option

For more flexibility, you create your own month names with the [CHOOSE function](https://exceljet.net/functions/choose-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 like this:

    =CHOOSE(MONTH(date),"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
    

Enter the month names you want to return (customized as you like) as values in CHOOSE, _after_ the first argument, which is entered as MONTH(date). The [MONTH function](https://exceljet.net/functions/month-function)
 will extract a month number, and CHOOSE will use this number to return the "nth" value in the list. This works because MONTH returns a number 1-12 that corresponds to the month name.

CHOOSE is more work to set up, but it is also more flexible, since it allows you to map a date to _any_ values you want (i.e. you can use values that are custom, abbreviated, not abbreviated, in a different language, etc.).

Related formulas
----------------

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

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

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

*   [Get month from date](https://exceljet.net/formulas/get-month-from-date)
    
*   [Get day name from date](https://exceljet.net/formulas/get-day-name-from-date)
    
*   [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)
    
*   [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
    

### Functions

*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

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
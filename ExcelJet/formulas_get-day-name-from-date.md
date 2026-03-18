# Get day name from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-day-name-from-date

---

[Skip to main content](https://exceljet.net/formulas/get-day-name-from-date#main-content)

[](https://exceljet.net/formulas/get-day-name-from-date#)

*   [Previous](https://exceljet.net/formulas/get-day-from-date)
    
*   [Next](https://exceljet.net/formulas/get-days-before-a-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get day name from date
======================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6794/download?token=vPgBNHxX)
 (14.63 KB)

![Excel formula: Get day name from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20day%20name%20from%20date.png "Excel formula: Get day name from date")

Summary
-------

To get the day name (i.e. Monday, Tuesday,Wednesday,  etc.) from a date, you can use the [TEXT function](https://exceljet.net/functions/text-function)
.  In the example shown, the formula in cell C5 is:

    =TEXT(B5,"dddd")
    

With January 1, 2000, in cell B5, the TEXT function returns the [text string](https://exceljet.net/glossary/text-value)
 "Saturday".

Generic formula
---------------

    TEXT(A1,"dddd")

Explanation 
------------

In this example, the goal is to get the day name (i.e. Monday, Tuesday, Wednesday,  etc.) from a given date. There are several ways to go about this in Excel, depending on your needs. This article explains three approaches:

1.  Display date with a custom number format
2.  Convert date to day name with TEXT function
3.  Convert date to day name with CHOOSE function

For all examples, keep in mind that [Excel dates are large serial numbers](https://exceljet.net/glossary/excel-date)
, displayed as dates with number formatting. 

### Day name with custom number format

To _display_ a date using only the day name, you don't need a formula; you can just use a [custom number format](https://exceljet.net/articles/custom-number-formats)
. Select the date, and use the [shortcut Control + 1 to open Format cells](https://exceljet.net/shortcuts/format-almost-anything)
. Then select Number > Custom, and enter one of these custom formats:

    "ddd"  // i.e."Wed"
    "dddd" // i.e."Wednesday"
    

Excel will display only the day name, but it will leave the date intact. If you want to display both the date and the day name in different columns, one option is to use a formula to pick up a date from another cell and change the number format to show only the day name. For example, in the worksheet shown, cell F5 contains the date January 1, 2000. The formula in G5, copied down, is:

    =F5 // get date from F5
    

Cells G5 and G6 have the [number format](https://exceljet.net/glossary/number-format)
 "dddd" applied, and cells in G7:G9 have the number format "ddd" applied.

### Day name with the TEXT function

To _convert_ a date to a [text value](https://exceljet.net/glossary/text-value)
 like "Saturday",  you can use the [TEXT function](https://exceljet.net/functions/text-function)
. The TEXT function is a general function that can be used to convert [numbers of all kinds into text values with formatting](https://exceljet.net/articles/custom-number-formats)
, including date formats. For example, with the date January 1, 2000, in cell A1, you can use TEXT like this:

    =TEXT(A1,"d-mmm-yyyy") // returns "1-Jan-2000"
    =TEXT(A1,"mmmm d, yyyy") // returns "January 1, 2000"
    =TEXT(A1,"mmmm") // returns "January"
    

In the worksheet shown, the goal is to display the day name only, so we use a [custom number format](https://exceljet.net/articles/custom-number-formats)
 like "ddd" or "dddd":

    =TEXT(B5,"dddd") // returns "Saturday"
    =TEXT(B5,"ddd") // returns "Sat"
    

Note: The TEXT function _converts_ a date to a [text value](https://exceljet.net/glossary/text-value)
 using the supplied number format. The date is lost in the conversion and only the text for the day name remains.

### Day name with CHOOSE function

For maximum flexibility, you can create your own day names with the [CHOOSE function](https://exceljet.net/functions/choose-function)
. CHOOSE is a general-purpose function for returning a value based on a numeric index. For example, you can use CHOOSE to return one of three colors with a number like this:

    =CHOOSE(1,"red","blue","green") // returns "red"
    =CHOOSE(2,"red","blue","green") // returns "blue"
    =CHOOSE(3,"red","blue","green") // returns "green"
    

In this example, the goal is to return a day name from a date, so we need to configure CHOOSE to select one of the seven-day names. For example, the formula below would return "Wed" based on a numeric index of 4:

    =CHOOSE(4,"Sun","Mon","Tue","Wed","Thu","Fri","Sat") // "Wed"
    

The challenge, in this case, is to get the right index for a date and for that we need the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. For any given date, WEEKDAY returns a number between 1-7, which corresponds to the day of the week. By default, WEEKDAY returns 1 for Sunday, 2 for Monday, 3 for Tuesday, etc. In the worksheet shown, the formula in C12 is:

    =CHOOSE(WEEKDAY(B12),"Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    

WEEKDAY returns a number between 1-7, and CHOOSE will use this number to select the corresponding value in the list. Since the date in B12 is January 1, 2000, WEEKDAY returns 7, and CHOOSE returns "Sat".

CHOOSE is more work to set up, but it is also more flexible since it allows you to convert a date to a day name using any values you want. For example, you can use custom abbreviations or even abbreviations in a different language. In cell C15, CHOOSE is set up to use one-letter abbreviations that correspond to Spanish day names:

    =CHOOSE(WEEKDAY(B15),"D","L","M","X","J","V","S")
    

### Empty cells

If you use the formulas above on an empty cell, you'll get "Saturday" as the result. This happens because an empty cell is evaluated as zero, and zero in the [Excel date system](https://exceljet.net/glossary/excel-date)
 is the date "0-Jan-1900", which is a Saturday. To work around this issue, you can use the [IF function](https://exceljet.net/videos/the-if-function)
 to return an empty string ("")  for empty cells. For example, if cell A1 may or may not contain a date, you can use IF like this:

    =IF(A1<>"",TEXT(A1,"ddd"),"") // check for empty cells
    

The literal translation of this formula is:  _If A1 [is not empty](https://exceljet.net/glossary/logical-operators)
, return the TEXT formula, otherwise return an [empty string](https://exceljet.net/glossary/empty-string)
 ("")._

Related formulas
----------------

[![Excel formula: Get day from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_day_from_date.png "Excel formula: Get day from date")](https://exceljet.net/formulas/get-day-from-date)

### [Get day from date](https://exceljet.net/formulas/get-day-from-date)

The DAY function takes just one argument, the date from which you want to extract the day. In the example, the formula is: =DAY(B5) B5 contains a date value for January 5, 2016. The DAY function returns the number 5 representing the day component of the date. Note that you can use DAY to extract...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

[![Excel formula: Get quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20quarter%20from%20date.png "Excel formula: Get quarter from date")](https://exceljet.net/formulas/get-quarter-from-date)

### [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)

In this example, the goal is to return a number that represents quarter (i.e. 1,2,3,4) for any given date. In other words, we want to return the quarter that the date resides in. ROUNDUP formula solution In the example shown, the formula in cell C5 is: =ROUNDUP(MONTH(B5)/3,0) The ROUNDUP function...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get day from date](https://exceljet.net/formulas/get-day-from-date)
    
*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    
*   [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

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
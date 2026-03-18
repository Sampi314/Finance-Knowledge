# Dynamic date list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-date-list

---

[Skip to main content](https://exceljet.net/formulas/dynamic-date-list#main-content)

[](https://exceljet.net/formulas/dynamic-date-list#)

*   [Previous](https://exceljet.net/formulas/dynamic-calendar-grid)
    
*   [Next](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Dynamic date list
=================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

[ROWS](https://exceljet.net/functions/rows-function)

![Excel formula: Dynamic date list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20date%20list.png "Excel formula: Dynamic date list")

Summary
-------

To create a dynamic date list, you can use a formula that increments a start date to create and display additional dates. In the example shown, the formula in B5 is:

    =start+ROWS($B$5:B5)-1-offset
    

where "start" is the [named range](https://exceljet.net/glossary/named-range)
 G4, and "offset" is the named range G5.

_Notes: (1) the offset represents days before the start date to display in the list. (2) the shading of the start date is done with conditional formatting as described below._

Generic formula
---------------

    =start+ROWS(exp_rng)-1-offset

Explanation 
------------

Dates in Excel are just [serial numbers](https://exceljet.net/glossary/excel-date)
, formatted to display as dates. This means you can perform math operations on dates to calculate days in the future or past.

In the example shown, the date in the named range "start" is provided by the TODAY function:

    =TODAY() //returns current date
    

The formula in B5 begins with the start date, and increments the date by one using an [expanding range](https://exceljet.net/glossary/expanding-reference)
 inside the ROWS function:

    ROWS($B$5:B5) // returns row count
    

ROWS returns the row count in a range. As the formula is copied down, the range expands and the row count increases by one at each new row. From this value, we subtract 1, so the date is _not incremented_ in the first row.

Next, we subtract the value in the [named range](https://exceljet.net/glossary/named-range)
 "offset" (G5). The offset is simply a way to begin the list of dates earlier than the start date provided. If offset is zero or blank, the first date in the list will equal the start date.

To display a weekday, the formula in C5 is:

    =TEXT(B5,"ddd")
    

To display a month, the formula in D5 is:

    =TEXT(B5,"mmm")
    

See this article for more examples of [custom number formats](https://exceljet.net/articles/custom-number-formats)
 in Excel.

The formulas in B5, C5, and D5 can be copied down as many rows as desired.

### Highlighting the start date

The start date is shaded with a conditional formatting rule based on this formula:

    =$B5=start
    

For more examples of applying conditional formatting with formulas, [see this article](https://exceljet.net/articles/conditional-formatting-with-formulas)
.

Related formulas
----------------

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

Related functions
-----------------

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    

### Functions

*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

### Articles

*   [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
    
*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    

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
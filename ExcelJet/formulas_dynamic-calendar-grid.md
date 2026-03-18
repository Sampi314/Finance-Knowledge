# Dynamic calendar grid - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-calendar-grid

---

[Skip to main content](https://exceljet.net/formulas/dynamic-calendar-grid#main-content)

[](https://exceljet.net/formulas/dynamic-calendar-grid#)

*   [Previous](https://exceljet.net/formulas/dynamic-calendar-formula)
    
*   [Next](https://exceljet.net/formulas/dynamic-date-list)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Dynamic calendar grid
=====================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")

Summary
-------

You can set up dynamic calendar grid on an Excel worksheet with a series of formulas, as explained in this article. In the example shown, the formula in B6 is:

    =start-CHOOSE(WEEKDAY(start),0,1,2,3,4,5,6)
    

where "start" is the [named range](https://exceljet.net/glossary/named-range)
 K5, and contains the date September 1, 2018.

_Note: this example uses a formula technique that will work in older versions of Excel. For a more modern solution based on the [SEQUENCE](https://exceljet.net/functions/sequence-function)
 function, [see this example](https://exceljet.net/formulas/dynamic-calendar-formula)
._

Explanation 
------------

_Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month._

With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This is done with this formula:

    =start-CHOOSE(WEEKDAY(start),0,1,2,3,4,5,6)
    

This formula figures out the Sunday before the first day of the month by using the CHOOSE function to "roll back" the right number of days to the previous Sunday. CHOOSE works perfectly in this situation, because it allows arbitrary values for each day of the week. We use this feature to roll back zero days when the first day of the month is a Sunday. More details about this problem are [provided here](https://exceljet.net/formulas/get-monday-of-the-week)
.

With the first day established in B6, the other formulas in the grid simply increment the previous date by one, beginning with the formula in C6:

    =IF(B6<>"",B6,$H5)+1
    

This formula tests the cell immediately to the left for a value. If no value is found, it pulls a value from column H in the row above. Note that $H5 is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
, to lock the column as the formula is copied throughout the grid. The same formula is used in all cells except B6.

### Conditional formatting rules

The calendar uses conditional formatting formulas to change formatting to shade previous and future months and to highlight the current day. Both rules are applied to the entire grid. For the previous and next months, the formula is:

    =MONTH(B6)<>MONTH(start)
    

For the current day, the formula is:

    =B6=TODAY()
    

![Conditional formatting rules for dynamic calendar](https://exceljet.net/sites/default/files/images/formulas/inline/dynamic%20calendar%20conditional%20formatting%20rules.png "Conditional formatting rules for dynamic calendar")

For more details, see: [Conditional formatting with formulas (10 examples)](https://exceljet.net/articles/conditional-formatting-with-formulas)

### Calendar heading

The calendar title – month and year – are calculated with this formula in cell B4:

    =start
    

Formatted with the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mmmm yyyy". To center the title above the calendar, the range B4:H4 has horizontal alignment set to "center across selection". This is a better option than merging cells since it doesn't alter the grid structure in the worksheet.

### Perpetual calendar with current date

To create a calendar that updates automatically based on the current date, you can use a formula like this in K5:

    =EOMONTH(TODAY(),-1)+1
    

This formula gets the current date with the TODAY function and then gets the first day of the current month using the EOMONTH function. Replace TODAY() with any given date to build a calendar in a different month. [More details on how EOMONTH works here](https://exceljet.net/formulas/get-first-day-of-month)
.

### Steps to create

1.  Hide grid lines (optional)
2.  Add a border to B5:H11 (7R x 7C)
3.  [Name](https://exceljet.net/glossary/named-range)
     K5 "start" and enter a date like "September 1, 2018"
4.  Formula in B4 =start
5.  [Format](https://exceljet.net/articles/custom-number-formats)
     B4 as "mmmm yyyy"
6.  Select B4:H4, set alignment to "Center across selection"
7.  In range B5:H5, enter day abbreviations (SMTWTFS)
8.  Formula in B6 =start-CHOOSE(WEEKDAY(start),0,1,2,3,4,5,6)
9.  Select B6:H11, apply [custom number format](https://exceljet.net/articles/custom-number-formats)
     "d"
10.  Formula in C6 =IF(B6<>"",B6,$H5)+1
11.  Copy the formula in C6 to the remaining cells in the calendar grid
12.  Add Prev/Next conditional formatting rule (see formula above)
13.  Add Current conditional formatting rule (see formula above)
14.  Change the date in K5 to another "first of month" date to test
15.  For perpetual calendar, formula in K5 =EOMONTH(TODAY(),-1)+1

Related formulas
----------------

[![Excel formula: Dynamic calendar formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula_0.png "Excel formula: Dynamic calendar formula")](https://exceljet.net/formulas/dynamic-calendar-formula)

### [Dynamic calendar formula](https://exceljet.net/formulas/dynamic-calendar-formula)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will automatically return the first day of the current month. In this example, the goal is to generate a dynamic calendar for any given month, based on a start date entered in cell J6...

[![Excel formula: Dynamic date list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20date%20list.png "Excel formula: Dynamic date list")](https://exceljet.net/formulas/dynamic-date-list)

### [Dynamic date list](https://exceljet.net/formulas/dynamic-date-list)

Dates in Excel are just serial numbers , formatted to display as dates. This means you can perform math operations on dates to calculate days in the future or past. In the example shown, the date in the named range "start" is provided by the TODAY function: =TODAY() //returns current date The...

[![Excel formula: Gantt chart](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20gantt%20chart.png "Excel formula: Gantt chart")](https://exceljet.net/formulas/gantt-chart)

### [Gantt chart](https://exceljet.net/formulas/gantt-chart)

The trick with this approach is the calendar header (row 4), which is just a series of valid dates, formatted with the custom number format "d". With a static date in D4, you can use =D4+1 to populate the calendar. This makes it easy to set up a conditional formatting rule that compares the date...

[![Excel formula: Get Monday of the week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20monday%20of%20the%20week.png "Excel formula: Get Monday of the week")](https://exceljet.net/formulas/get-monday-of-the-week)

### [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)

Imagine you have a random date and want to find the Monday of the week in which the date appears. You can see you will need to "roll back" a specific number of days, depending on what day of the week the given date is. If the date is a Wednesday, you need to roll back 2 days, if the date is a...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic calendar formula](https://exceljet.net/formulas/dynamic-calendar-formula)
    
*   [Dynamic date list](https://exceljet.net/formulas/dynamic-date-list)
    
*   [Gantt chart](https://exceljet.net/formulas/gantt-chart)
    
*   [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

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
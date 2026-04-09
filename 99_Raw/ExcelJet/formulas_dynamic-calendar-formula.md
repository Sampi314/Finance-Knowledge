# Dynamic calendar formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-calendar-formula

---

[Skip to main content](https://exceljet.net/formulas/dynamic-calendar-formula#main-content)

[](https://exceljet.net/formulas/dynamic-calendar-formula#)

*   [Previous](https://exceljet.net/formulas/due-date-by-category)
    
*   [Next](https://exceljet.net/formulas/dynamic-calendar-grid)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Dynamic calendar formula
========================

by Dave Bruns · Updated 15 May 2024

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

[TODAY](https://exceljet.net/functions/today-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[DATE](https://exceljet.net/functions/date-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7080/download?token=wg_e8RN0)
 (19 KB)

![Excel formula: Dynamic calendar formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Dynamic%20calendar%20formula_0.png "Excel formula: Dynamic calendar formula")

Summary
-------

To create a dynamic monthly calendar with a formula, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
, with help from the [CHOOSE](https://exceljet.net/functions/choose-function)
 and [WEEKDAY](https://exceljet.net/functions/weekday-function)
 functions. In the example shown, the formula in B6 is:

    =SEQUENCE(6,7,start-CHOOSE(WEEKDAY(start),0,1,2,3,4,5,6))
    

where **start** is the [named range](https://exceljet.net/glossary/named-range)
 J6. In the example shown, conditional formatting is used to highlight the current date and holidays, and lighten days in other months. See below for a full explanation.

_Note: dynamic array functions are only available in [Excel 365](https://exceljet.net/glossary/excel-365)
 and 2021. For a formula approach that works in older versions of Excel, [see this example](https://exceljet.net/formulas/dynamic-calendar-grid)
._

Explanation 
------------

_Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will automatically return the first day of the current month._

In this example, the goal is to generate a dynamic calendar for any given month, based on a start date entered in cell J6, which is [named](https://exceljet.net/glossary/named-range)
 "start" We assume that **start** is a valid first-of-month date like 1-Jan-2022, 1-Feb-2022, 1-Mar-2022, etc. The final calendar should place each day of the month in a grid with each week starting on Sunday, as seen in the example. The solution explained below is based on the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. SEQUENCE is one of the original [dynamic array functions in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, and a perfect fit for this problem.

### Background study

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
     \- overview
*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
     \- 3 min video
*   [WEEKDAY function](https://exceljet.net/functions/weekday-function)
     \- overview and examples
*   [Custom number formats in Excel](https://exceljet.net/articles/custom-number-formats)
     \- overview

### Short version

The explanation below is rather long. The short version is that the [SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
 outputs a 6 x 7 [array](https://exceljet.net/glossary/array)
 of 42 dates in a calendar grid, [formatted](https://exceljet.net/glossary/number-format)
 to display the day only. This works because [Excel dates are just serial numbers](https://exceljet.net/glossary/excel-date)
. The main challenge with this problem is figuring out what date to start with for a given month, which is always a Sunday. This is handled with the [CHOOSE](https://exceljet.net/functions/choose-function)
 and [WEEKDAY](https://exceljet.net/functions/weekday-function)
 functions. Conditional formatting is used to highlight the current date and holidays and to lighten days in other months. Read below for all the details.

### Basic SEQUENCE

The SEQUENCE function can be used to generate numeric sequences. For example, to generate the numbers 1 to 10 in ten rows, you can use SEQUENCE like this:

    =SEQUENCE(10) // returns {1;2;3;4;5;6;7;8;9;10}
    

The result is an [array](https://exceljet.net/glossary/array)
 that contains the numbers 1-10. The array [spills](https://exceljet.net/glossary/spill)
 into a vertical range of ten cells. SEQUENCE can generate arrays in rows and columns. For example, the following formula creates the numbers 1-10 in an array with 5 rows and 2 columns:

    =SEQUENCE(5,2)
    

Similarly, the formula below will fill a 7 x 6 grid of cells with the numbers 1-42:

    =SEQUENCE(6,7)
    

The screen below shows how these formulas behave on a worksheet:

![Basic SEQUENCE function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/basic%20SEQUENCE%20function%20examples.png?itok=cgdj-GrC "Basic SEQUENCE function examples")

These are just numbers, not dates, but you can see the core concept.

### SEQUENCE with dates

Because [Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
, the SEQUENCE function can easily be used to generate [arrays](https://exceljet.net/glossary/array)
 of dates. For example, the formula below will generate dates for the 31 days of January 2022:

    =SEQUENCE(7,1,DATE(2022,1,1))
    

_Note: the [DATE function](https://exceljet.net/functions/date-function)
 is a safer way to hard code dates into formulas since dates entered as text can be misinterpreted._

To translate: we are asking for 7 numbers, in a 7 x 1 array, starting with January 1, 2022. SEQUENCE automatically defaults to a step value of 1, so the result is a list of serial numbers starting with 44562. We don't want to display serial numbers in our calendar, we want to show days. To do that we can use the custom number format "d". That will cause Excel to display just the day numbers. The screen below shows before and after:

![SEQUENCE with dates and custom number formatting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/SEQUENCE%20with%20dates%20and%20custom%20number%20formatting.png?itok=3dRzS0nb "SEQUENCE with dates and custom number formatting")

Now let's see what happens if we ask for 6 x 7 grid, starting with January 1, 2022:

    =SEQUENCE(6,7,DATE(2022,1,1))
    

Once we format the output with the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "d", we see a total of 42 numbers, beginning with January 1. At the end of January, the month changes to February, and the day becomes 1 again:

![SEQUENCE dates formatted to show day only](https://exceljet.net/sites/default/files/images/formulas/inline/SEQUENCE%20dates%20formatted%20to%20show%20day%20only.png "SEQUENCE dates formatted to show day only")

We still don't have a usable calendar, but we're getting closer! 

To make a proper calendar, we need the first day in our grid to start on Sunday. If the first day of a month is not a Sunday, we need to start the grid on the last Sunday of the previous month. How can we calculate the last Sunday of the previous month? Before we get into specific functions, let's clarify the goal.

### First Sunday

If the first of a month happens to be a Sunday, we're done. There's no need to do anything. The first of the month _is_ our start date. However, if the first of the month is _not_ a Sunday, we need to "roll back" some number of days to the _prior_ Sunday. How many days do we need to roll back? This depends on what day of the week the first day of a month lands on. For example, if the first is a Tuesday, we need to roll back 2 days. If the first is a Friday, we need to roll back 5 days. And if the first is already a Sunday, we need to roll back 0 days.

Now we have a pretty good idea of what we need to do, we just need to implement that behavior in a formula. This is where the formula gets a bit tricky because we need to combine two functions, WEEKDAY and CHOOSE, in a way that most users won't recognize.

### The WEEKDAY function

To figure out the day of the week, we use the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. WEEKDAY returns a number for each day of the week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday. For example, WEEKDAY returns 7 for January 1, 2022, since the first is a Saturday:

    =WEEKDAY(DATE(2022,1,1)) // returns 7
    

For January 2, 2022, WEEKDAY returns 1, since the second is a Sunday:

    =WEEKDAY(DATE(2022,1,2)) // returns 1
    

To summarize, WEEKDAY will give us a number between 1-7 for each day of the week, and we can use that result to figure out how many days we need to roll back.

### The CHOOSE function

The [CHOOSE function](https://exceljet.net/functions/choose-function)
 is used to select arbitrary values by numeric position. For example, if we have the colors "red", "blue", and "green", we can use CHOOSE like this:

    =CHOOSE(1,"red", "blue", "green") // returns "red"
    =CHOOSE(2,"red", "blue", "green") // returns "blue"
    =CHOOSE(3,"red", "blue", "green") // returns "green"
    

CHOOSE is a flexible function and accepts a list of text values, numbers, and cell references, in any combination.

### CHOOSE + WEEKDAY

Next, we're going to combine CHOOSE and WEEKDAY to give us the correct "roll back" number like this:

    =CHOOSE(WEEKDAY(start),0,1,2,3,4,5,6)
    

The _index\_num_ argument is provided by the WEEKDAY function. The other individual values given to CHOOSE are the rollback numbers, one for each day of the week. WEEKDAY returns a number between 1-7, and the CHOOSE function uses the number from WEEKDAY to select a number from the list of numbers provided. For example, if WEEKDAY returns 3 (Tuesday), CHOOSE returns 2:

    CHOOSE(3,0,1,2,3,4,5,6) // returns 2
    

Now we are finally ready to use this rollback number to compute the first Sunday in the grid. Because dates are just numbers in Excel, the operation is simple – we just need to subtract the rollback number from the start date:

    start-CHOOSE(WEEKDAY(start),0,1,2,3,4,5,6) // first Sunday
    

The result is a valid date that represents the first Sunday in the calendar grid.

### Putting it all together

Now we need to combine the ideas explained above into a single formula based on the SEQUENCE function. We start off by asking for a 6 x 7 array of numbers like this:

    =SEQUENCE(6,7 // 6 rows, 7 columns
    

Then, for the _start_ [argument](https://exceljet.net/glossary/function-argument)
, we simply provide the code we worked out above:

    =SEQUENCE(6,7,start-CHOOSE(WEEKDAY(start),0,1,2,3,4,5,6))
    

The result is a full grid of 42 dates that can be displayed as a monthly calendar. If the start date in J6 is changed to another first-of-month date, the grid automatically updates.

### Conditional formatting rules

The conditional formatting rules to highlight the current date and holidays, and lighten days in other months are listed below:

![Conditional formatting rules](https://exceljet.net/sites/default/files/images/formulas/inline/Conditional%20formatting%20rules%20for%20dynamic%20calendar.png "Conditional formatting rules")

The formula for the current date is:

    =B6=TODAY()
    

The formula to highlight holidays is based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
:

    =COUNTIF(holidays,B6)
    

If the count is anything but zero, the date must be a holiday. Holidays must be a range that contains valid Excel dates that represent non-working days. In the example shown, **holidays** is the [named range](https://exceljet.net/glossary/dynamic-named-range)
 L6:L8. You can add more holidays to this list as you like but don't forget to update the named range. Alternatively, you can define holidays as an [Excel Table](https://exceljet.net/glossary/excel-table)
 so the range updates automatically.

The formula to lighten days in other months is based on the [MONTH function](https://exceljet.net/functions/month-function)
:

    =MONTH(B6)<>MONTH(start)
    

If the month of the current date is different from the month of the date in J6, trigger the rule.

Read more: [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
, [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)

### Calendar Title

The formula to output the calendar title in cell B4 is based on the [TEXT function](https://exceljet.net/functions/text-function)
:

    =TEXT(start,"mmmm yyyy")
    

The title is centered over the calendar grid with the Center Across Selection. Select B4:H4, and use [Control + 1 to open Format Cells](https://exceljet.net/shortcuts/format-almost-anything)
, then select "Center Across Selection" from the Horizontal text alignment dropdown. This is a better option than merging cells since it doesn't alter the grid structure in the worksheet.

### Perpetual calendar with current date

To create a perpetual calendar that updates automatically based on the current date, we need to update the formula to generate the first day of the current month on the fly. The first day of the current month can be calculated with the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 like this:

    =EOMONTH(TODAY(),-1)+1
    

You can use this formula directly in cell J6 and the calendar will always stay up to date. For an all-in-one formula, we can add the [LET function](https://exceljet.net/functions/let-function)
 like this:

    =LET(start,EOMONTH(TODAY(),-1)+1,SEQUENCE(6,7,start-CHOOSE(WEEKDAY(start),0,1,2,3,4,5,6)))
    

Here, we use the LET function to define "start" as the first day of the current month, then run the original formula unchanged. The local variable "start" overrides the named range **start** on the worksheet, which can be deleted if desired.

### Monday start

To generate a calendar that starts on Monday instead of Sunday, you can use the following code inside of SEQUENCE as the _start_ argument:

    =start-CHOOSE(WEEKDAY(start),6,0,1,2,3,4,5)
    

Using the same logic explained above, this code rolls back the start date as needed to begin the calendar on Monday. [This example](https://exceljet.net/formulas/get-previous-sunday)
 has more information on rolling back dates to previous days of the week.

Related formulas
----------------

[![Excel formula: Sequence of days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_days.png "Excel formula: Sequence of days")](https://exceljet.net/formulas/sequence-of-days)

### [Sequence of days](https://exceljet.net/formulas/sequence-of-days)

The goal is to generate a series of sequential dates with a formula. In the current version of Excel, the easiest method is to use the SEQUENCE function. SEQUENCE can return all dates at the same time into a range on the worksheet. In older versions of Excel without the SEQUENCE function, you can...

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Gantt chart](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20gantt%20chart.png "Excel formula: Gantt chart")](https://exceljet.net/formulas/gantt-chart)

### [Gantt chart](https://exceljet.net/formulas/gantt-chart)

The trick with this approach is the calendar header (row 4), which is just a series of valid dates, formatted with the custom number format "d". With a static date in D4, you can use =D4+1 to populate the calendar. This makes it easy to set up a conditional formatting rule that compares the date...

[![Excel formula: Get Monday of the week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20monday%20of%20the%20week.png "Excel formula: Get Monday of the week")](https://exceljet.net/formulas/get-monday-of-the-week)

### [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)

Imagine you have a random date and want to find the Monday of the week in which the date appears. You can see you will need to "roll back" a specific number of days, depending on what day of the week the given date is. If the date is a Wednesday, you need to roll back 2 days, if the date is a...

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

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

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/SEQUENCE%20of%20dates-Play.png)](https://exceljet.net/videos/sequence-of-dates)

### [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)

In this video, we'll look at how to generate a sequence of dates with the SEQUENCE function . The SEQUENCE function can be used to generate numeric sequences of all kinds. Since Excel dates are just numbers, SEQUENCE works well for generating dates. In this first worksheet, we have a couple cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sequence of days](https://exceljet.net/formulas/sequence-of-days)
    
*   [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
    
*   [Gantt chart](https://exceljet.net/formulas/gantt-chart)
    
*   [Get Monday of the week](https://exceljet.net/formulas/get-monday-of-the-week)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)
    

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
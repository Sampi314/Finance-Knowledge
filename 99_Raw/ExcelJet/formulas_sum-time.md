# Sum time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-time

---

[Skip to main content](https://exceljet.net/formulas/sum-time#main-content)

[](https://exceljet.net/formulas/sum-time#)

*   [Previous](https://exceljet.net/formulas/sum-race-time-splits)
    
*   [Next](https://exceljet.net/formulas/sum-time-by-week-and-project)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Sum time
========

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7213/download?token=ugUZqMCI)
 (14.98 KB)

![Excel formula: Sum time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20time%20with%20a%20formula.png "Excel formula: Sum time")

Summary
-------

To sum valid Excel times with a formula, you can use the [SUM function](https://exceljet.net/functions/sumif-function)
, or the [SUMIF function](https://exceljet.net/functions/sumif-function)
. In the example shown, the formula in H5 is:

    =SUM(data[Hours])
    

Where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:E16.

Generic formula
---------------

    =SUM(range)

Explanation 
------------

Dates and times are just numbers in Excel, so you can use them in any normal math operation. However, by default, Excel will only display hours and minutes up to 24 hours. This means you might seem to "lose time" if you are adding up time that is more than 1 day.

In this example, the goal is to sum total hours in cell H5 and calculate total hours per person in the range H8:H10. All data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range B5:E16. The table is used for convenience only, and is not required to solve the problem. The main challenge in this example is to correctly display time as a duration instead of time of day.

### How Excel handles times

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
 and [times are fractional parts of 1 day](https://exceljet.net/glossary/excel-time)
. This means the date and time values are just regular numbers and can be summed, added, and subtracted like other numbers. The screen below shows what the dates in column D and the times in column E look like with the General [number format](https://exceljet.net/glossary/number-format)
 applied:

![Dates and times with general number format applied](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/dates%20and%20times%20with%20general%20number%20format%20applied.png?itok=W0ejjgvF "Dates and times with general number format applied")

As you can see, dates are large serial numbers. The times in column E are just fractional values of one day, expressed as decimal values. This means you can use standard functions like SUM and SUMIF, etc. to sum time in various ways. But you have to be careful about how the result is displayed.

### Excel times over 24 hours

What causes a time to look like a time in Excel is a [number format](https://exceljet.net/glossary/number-format)
. A simple number format for time might look like this:

    h:mm // display time like 9:15
    

The main thing to understand is that a standard time format is meant to display time like a clock, which resets every 24 hours. This works fine when the goal is to display a time of day, or when total hours are less than 24. But in cases where time is meant to show a _duration_ (i.e. elapsed time), the problem is that Excel will not display more than 24 hours by default. For example, if total time is 23 hours, the time format above will display "23:00", but if total time is 31.5 hours, the time format above will display "7:30":

![Example of incorrect total hours](https://exceljet.net/sites/default/files/images/formulas/inline/example%20of%20incorrect%20total%20hours.png "Example of incorrect total hours")

The time format causes hours to reset at midnight, and the extra 7.5 hours roll over into the next day. The formula is actually working fine, but the display makes it seem like hours are being undercounted or "lost" in the calculation.

### Custom time format

To display 25 hours like "25:00", we need to use a [custom time format](https://exceljet.net/articles/custom-number-formats)
 like this:

    [h]:mm // display 25 hours as 25:00
    

The square brackets around the "h" tell Excel to display hours as a duration, not a time of day. You can see how this works in the screen below. Cell D3 uses the time format "h:mm" and cell D4 uses the time format "\[h\]:mm". Both cells contain the same formula:

    =SUM(B3:B6)
    

![Total hours with different time formats](https://exceljet.net/sites/default/files/images/formulas/inline/total%20hours%20with%20different%20time%20formats.png "Total hours with different time formats")

### Apply custom time format

To apply a custom time format, first select the cells you want to format and use [Control + 1](https://exceljet.net/shortcuts/format-almost-anything)
 to open the Format Cells window. Next, navigate to the Number tab, select Custom in the list to the left, and enter "\[h\]:mm" in the Type input area:

![Applying a custom time format to show time as a duration](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sum%20time%20custom%20number%20format.png?itok=sP3UQaFi "Applying a custom time format to show time as a duration")

You will see a sample of the result displayed in the "Sample" area above Type.

Video: [How to create a custom time format](https://exceljet.net/videos/how-to-create-a-custom-time-format)

### Total time

With the above in mind, the formula to calculate total time in cell H5 is:

    =SUM(data[Hours]) // sum all time
    

With the following custom time format above applied:

    [h]:mm
    

The number returned by the SUM function is 3.1875 (3.19 days), which displays as 76:30 with the above time format applied.

### Time per person

To calculate time logged per person, we use the [SUMIF function](https://exceljet.net/functions/sumif-function)
. The formula in cell H8, copied down, is:

    =SUMIF(data[Name],G8,data[Hours])
    

The range is the "Name" column of the table, the criteria is the value from G8 ("Jane"), and the sum\_range is the "Hours" column. As the formula is copied down, SUMIF returns total hours per person. The range H8:H10 has the custom time format "\[h\]:mm" applied.

For more information on number formats, see [Excel Custom Number formats.](https://exceljet.net/articles/custom-number-formats)

### Decimal time

Another solution for working with time values over 24 hours is to convert the time to a decimal number. For example, instead of using native time values like 4:30, 7:00, and 8:30, you convert these times to decimal hours like 4.5, 7.0, and 8.5. Once you have time in this format, you can calculate total time any way you like. [This formula example](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
 explains the details.

Related formulas
----------------

[![Excel formula: Sum time with SUMIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20with%20SUMIFS%20v2.png "Excel formula: Sum time with SUMIFS")](https://exceljet.net/formulas/sum-time-with-sumifs)

### [Sum time with SUMIFS](https://exceljet.net/formulas/sum-time-with-sumifs)

Excel times are numbers and can be summed like other numeric values. In this example, F4:G7 is a summary table, showing the total time logged in each of three states: Standby, Run, and Offline. These values are hardcoded in the range F5:F7. To sum time conditionally by each state, we are using the...

[![Excel formula: Sum time by week and project](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20by%20week%20and%20project.png "Excel formula: Sum time by week and project")](https://exceljet.net/formulas/sum-time-by-week-and-project)

### [Sum time by week and project](https://exceljet.net/formulas/sum-time-by-week-and-project)

In this example, the sum range is the named range "time", entered as an Excel time in hh:mm format. The first criteria inside SUMIFS includes dates that are greater than or equal to week date in column F: date,">="...

[![Excel formula: Sum time over 30 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20over%2030%20minutes.png "Excel formula: Sum time over 30 minutes")](https://exceljet.net/formulas/sum-time-over-30-minutes)

### [Sum time over 30 minutes](https://exceljet.net/formulas/sum-time-over-30-minutes)

This formula uses the SUMPRODUCT function to sum the result of two expressions that yield arrays. The goal is to sum only time greater than 30 minutes, the "surplus" or "extra" time. The first expression subtracts 30 minutes from every time in the named range "times": times-TIME(0,30,0) This...

[![Excel formula: Remove time from timestamp](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20time%20from%20timestamp.png "Excel formula: Remove time from timestamp")](https://exceljet.net/formulas/remove-time-from-timestamp)

### [Remove time from timestamp](https://exceljet.net/formulas/remove-time-from-timestamp)

In this example, the goal is to use a formula to remove the time value from a timestamp that includes both the date and time. To solve this problem, it's important to understand that Excel handles dates and time using a scheme in which dates are large serial numbers and times are fractional values...

[![Excel formula: Basic timesheet formula with breaks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20timesheet%20formula%20with%20breaks.png "Excel formula: Basic timesheet formula with breaks")](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)

### [Basic timesheet formula with breaks](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)

At the core, this formula subtracts start time from end time to get duration in hours. This is done to calculate both work time and break time. MOD(C6-B6,1) // get work time MOD(E6-D6,1) // get break time Next, break time is subtracted from work time to get "net" work hours. This formula uses the...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum time with SUMIFS](https://exceljet.net/formulas/sum-time-with-sumifs)
    
*   [Sum time by week and project](https://exceljet.net/formulas/sum-time-by-week-and-project)
    
*   [Sum time over 30 minutes](https://exceljet.net/formulas/sum-time-over-30-minutes)
    
*   [Remove time from timestamp](https://exceljet.net/formulas/remove-time-from-timestamp)
    
*   [Basic timesheet formula with breaks](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    

### Articles

*   [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
    
*   [Excel Tables](https://exceljet.net/articles/excel-tables)
    

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
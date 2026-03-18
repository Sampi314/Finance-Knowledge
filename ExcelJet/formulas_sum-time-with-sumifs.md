# Sum time with SUMIFS - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-time-with-sumifs

---

[Skip to main content](https://exceljet.net/formulas/sum-time-with-sumifs#main-content)

[](https://exceljet.net/formulas/sum-time-with-sumifs#)

*   [Previous](https://exceljet.net/formulas/sum-time-over-30-minutes)
    
*   [Next](https://exceljet.net/formulas/time-duration-with-days)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Sum time with SUMIFS
====================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5666/download?token=XV7kow-o)
 (9.68 KB)

![Excel formula: Sum time with SUMIFS](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20time%20with%20SUMIFS%20v2.png "Excel formula: Sum time with SUMIFS")

Summary
-------

To sum time conditionally, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in G5 is:

    =SUMIFS(times,states,F5)
    

where **times** (C5:C15), and **states** (D5:D15) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =SUMIFS(times,range,criteria)

Explanation 
------------

[Excel times are numbers](https://exceljet.net/glossary/excel-time)
 and can be summed like other numeric values. In this example, F4:G7 is a summary table, showing the total time logged in each of three states: Standby, Run, and Offline. These values are hardcoded in the range F5:F7.

To sum time conditionally by each state, we are using the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 in G5:

    =SUMIFS(times,states,F5)
    

1.  The sum\_range is the named range **times** (C5:C15), entered in hh:mm format
2.  Criteria\_range1 is the named range **states** (D5:D15)
3.  Criteria1 is entered as F5

The reference to F5 is [relative](https://exceljet.net/glossary/relative-reference)
. When the formula is copied down the column, F5 changes at each new row. The two named ranges, **times** and **states,** are fixed and do not change. In each row, SUMIFS correctly shows the total hours logged for a given state. Note when time exceeds 24 hours, you will need to use a custom time format as explained below.

### Duration over 24 hours

With normal time formats like hh:mm, hours will "reset" to zero every 24 hours. This makes sense when the intent is to display an actual time, but it can be confusing when the total time exceeds 1 day because hours appear to be lost.

To display time durations of more than 24 hours use a [custom number format](https://exceljet.net/articles/custom-number-formats)
 with hours in square brackets, as shown below:

    [h]:mm
    

For a more detailed explanation, see [Sum time in Excel](https://exceljet.net/formulas/sum-time)
.

### Without names ranges

The [named ranges](https://exceljet.net/glossary/named-range)
 in this formula are used for convenience only. Named ranges are automatically [absolute](https://exceljet.net/glossary/absolute-reference)
, so there is no need to lock references manually. However, the named ranges are entirely optional. Without named ranges, the equivalent formula is:

    =SUMIFS($D$5:$D$15,$C$5:$C$15,F5)
    

Related formulas
----------------

[![Excel formula: Sum time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20with%20a%20formula.png "Excel formula: Sum time")](https://exceljet.net/formulas/sum-time)

### [Sum time](https://exceljet.net/formulas/sum-time)

Dates and times are just numbers in Excel, so you can use them in any normal math operation. However, by default, Excel will only display hours and minutes up to 24 hours. This means you might seem to "lose time" if you are adding up time that is more than 1 day. In this example, the goal is to sum...

[![Excel formula: Sum time by week and project](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20by%20week%20and%20project.png "Excel formula: Sum time by week and project")](https://exceljet.net/formulas/sum-time-by-week-and-project)

### [Sum time by week and project](https://exceljet.net/formulas/sum-time-by-week-and-project)

In this example, the sum range is the named range "time", entered as an Excel time in hh:mm format. The first criteria inside SUMIFS includes dates that are greater than or equal to week date in column F: date,">="...

[![Excel formula: Sum race time splits](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20race%20time%20splits.png "Excel formula: Sum race time splits")](https://exceljet.net/formulas/sum-race-time-splits)

### [Sum race time splits](https://exceljet.net/formulas/sum-race-time-splits)

Excel times are fractional numbers . This means you can add times together with the SUM function to get total durations. However, you must take care to enter times with the right syntax and use a suitable time format to display results, as explained below. Enter times in the correct format You must...

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")](https://exceljet.net/formulas/get-work-hours-between-dates)

### [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per...

[![Excel formula: Group times into 3 hour buckets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group%20times%20into%203%20hour%20buckets.png "Excel formula: Group times into 3 hour buckets")](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

### [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

If you need to group times into buckets (i.e. group by 6 hours, group by 3 hours, etc.) you can do so with a rounding function called FLOOR. In the example shown, we have a number of transactions, each with a timestamp. Let's say you want to group these transactions into buckets of 3 hours like...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum time](https://exceljet.net/formulas/sum-time)
    
*   [Sum time by week and project](https://exceljet.net/formulas/sum-time-by-week-and-project)
    
*   [Sum race time splits](https://exceljet.net/formulas/sum-race-time-splits)
    
*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    
*   [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

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
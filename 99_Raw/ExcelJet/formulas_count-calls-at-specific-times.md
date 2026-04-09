# Count calls at specific times - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-calls-at-specific-times

---

[Skip to main content](https://exceljet.net/formulas/count-calls-at-specific-times#main-content)

[](https://exceljet.net/formulas/count-calls-at-specific-times#)

*   [Previous](https://exceljet.net/formulas/count-birthdays-by-month)
    
*   [Next](https://exceljet.net/formulas/count-dates-in-current-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Count calls at specific times
=============================

by Dave Bruns · Updated 29 Jul 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6194/download?token=Dkjv3xDw)
 (19.74 KB)

![Excel formula: Count calls at specific times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20calls%20at%20specific%20times.png "Excel formula: Count calls at specific times")

Summary
-------

To count calls at specific time intervals, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in H5 is:

    =COUNTIFS(table[Time],">="&F5,table[Time],"<"&G5)
    

where **table** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 holding call times as shown.

Generic formula
---------------

    =COUNTIFS(times,">="&start,times,"<"&end)

Explanation 
------------

_Note: this formula depends on values in the Time column (C), and values in the Start and End columns (F, G) being [valid Excel times](https://exceljet.net/glossary/excel-time)
._

The data is in an Excel table called **table**. By [creating a proper Excel table](https://exceljet.net/videos/how-to-create-an-excel-table)
, we make the formulas easier to read and write. In addition, any new data that is added to the table will be automatically picked up by the formulas in columns H and I.

The summary table on the right is constructed by entering Excel times in the Start and End columns. After you enter a couple times, you can use the [fill handle to enter the rest](https://exceljet.net/videos/how-to-enter-custom-patterns-with-the-fill-handle-in-excel)
. To count cells that occur in each interval as shown, the formula in H5 is:

    =COUNTIFS(table[Time],">="&F5,table[Time],"<"&G5)
    

The COUNTIFS function has been configured with two criteria and, like other [RACON functions](https://exceljet.net/articles/excels-racon-functions)
, COUNTIFS accepts criteria entered in range/criteria pairs like this:

    table[Time],">="&F5 // greater than or equal to F5
    table[Time],"<"&G5 // less than G5
    

Literal translation: _count values in the [Time column](https://exceljet.net/glossary/structured-reference)
 in **table** that are greater than or equal to the start time in F5 AND less than the end time in G5"_

As the formula is copied down the table, COUNTIFS returns the count of calls occurring between each start and end time.

### Total time

To calculate the total time of all calls at each interval you can use the SUMIFS function. The logical criteria is exactly the same, the only difference is the first argument, called _sum\_range_. This is the range that contains values to sum, which is the Duration column in the table shown. The formula in I5, copied down, is:

    =SUMIFS(table[Duration],table[Time],">="&F5,table[Time],"<"&G5)
    

The results returned by SUMIFS in column I are formatted as hours and minutes:

    h:mm // hours and minutes
    

If total call time might exceed 24 hours, use a [custom time format](https://exceljet.net/articles/custom-number-formats)
 like this:

    [h]:mm // for hours > 24
    

The square brackets stop Excel from resetting hours at 1 day (24 hours).

### With dynamic arrays

If you have [Excel 365](https://exceljet.net/glossary/excel-365)
, you can enter one formula each to count and sum times in all intervals at once:

    =COUNTIFS(table[Time],">="&F5:F11,table[Time],"<"&G5:G11)
    =SUMIFS(table[Duration],table[Time],">="&F5:F11,table[Time],"<"&G5:G11)
    

Both formulas will [spill](https://exceljet.net/glossary/spill)
 multiple results into a [dynamic array](https://exceljet.net/glossary/dynamic-array)
.

Related formulas
----------------

[![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

### [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value. You can also express 15 minutes in a formula with this...

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Group times into 3 hour buckets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group%20times%20into%203%20hour%20buckets.png "Excel formula: Group times into 3 hour buckets")](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

### [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

If you need to group times into buckets (i.e. group by 6 hours, group by 3 hours, etc.) you can do so with a rounding function called FLOOR. In the example shown, we have a number of transactions, each with a timestamp. Let's say you want to group these transactions into buckets of 3 hours like...

[![Excel formula: Count times in a specific range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20times%20in%20a%20specific%20range.png "Excel formula: Count times in a specific range")](https://exceljet.net/formulas/count-times-in-a-specific-range)

### [Count times in a specific range](https://exceljet.net/formulas/count-times-in-a-specific-range)

The COUNTIFS function takes one or more criteria, entered as range/criteria pairs. In this example, the first range/criteria pair is: B5:B11,">="&E5 Matching any time greater than or equal to the time E5 (5:00). The second range/criteria pair is: B5:B11,"<"&E6 Matching any time less...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    
*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    
*   [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)
    
*   [Count times in a specific range](https://exceljet.net/formulas/count-times-in-a-specific-range)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

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
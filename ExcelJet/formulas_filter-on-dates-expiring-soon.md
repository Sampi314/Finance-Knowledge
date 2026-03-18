# Filter on dates expiring soon - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-on-dates-expiring-soon

---

[Skip to main content](https://exceljet.net/formulas/filter-on-dates-expiring-soon#main-content)

[](https://exceljet.net/formulas/filter-on-dates-expiring-soon#)

*   [Previous](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    
*   [Next](https://exceljet.net/formulas/future-time-intervals)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Filter on dates expiring soon
=============================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SORT](https://exceljet.net/functions/sort-function)

[AND](https://exceljet.net/functions/and-function)

[TODAY](https://exceljet.net/functions/today-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7390/download?token=NNJun8L5)
 (16.02 KB)

![Excel formula: Filter on dates expiring soon](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20on%20dates%20expiring%20soon.png "Excel formula: Filter on dates expiring soon")

Summary
-------

To filter a set of data to show rows where dates are expiring soon (or have already expired) you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [SORT function](https://exceljet.net/functions/sort-function)
. In the example shown, the formula in G5 is:

    =SORT(FILTER(data,data[Expires]-date<=days),4)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:E16, and **date** (H2) and **days** (J2) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is the five rows in the table with an expiration date within the next 15 days:

Explanation 
------------

In this example, the goal is to filter data to show rows where dates have expired or will be expiring soon. In the table to the left, we have equipment that needs to be replaced every x months, where x appears in the "Months" column. The "Replaced" column shows the date equipment was replaced. The "Expires" column shows the date it will need to be replaced again.

All data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range B5:E16 and the dates to check are in the "Expires" column. In addition, the current date is in the [named range](https://exceljet.net/glossary/named-range)
 **date** (H2) and the number of days to use when deciding if a date is expiring soon is in the named range **days** (J2). Dates _already expired_ are highlighted in yellow with conditional formatting. The named ranges are for convenience only, to make the formula easier to read and write.

You can use this same approach to filter on any data that has an upcoming date. i.e. retirements, events, renewals, etc. 

_Note: In the example shown, the current date is 7-July-2022, provided by the TODAY function. As time goes by, the current date will move forward, and more dates will be expired or expiring soon. To see the worksheet in its original state, you can hardcode the date 7-July-2022 into cell H2._

### The core logic

In the example shown, the formula in G5 is:

    =SORT(FILTER(data,data[Expires]-date<=days),4)
    

Working from the inside out, the core logic in this formula first works out the difference between the value in **date** (H2) and all dates in column E:

    data[Expires]-date<=days)
    

Because [Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
, we simply subtract the value in **date** from each date in the Expires column. When the expiration date is in the past, the result is a _negative_ number. When the expiration date is in the future, the result date is a _positive_ number. In the example shown:

    data[Expires]-date
    

returns the following [array](https://exceljet.net/glossary/array)
:

    {-36;33;14;293;331;3;248;10;34;-3;17;35}
    

Each number represents the number of days until expiration. Again, negative numbers are dates _already expired_. When this array is compared to **days** (J2) which is 15:

    ={-36;33;14;293;331;3;248;10;34;-3;17;35}<=15
    

the result is an array of TRUE and FALSE values like this:

    {TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE}
    

Each TRUE value represents a date that has already expired or will expire in the next 15 days. We can use this same logic in the FILTER function to select dates expiring soon.

### FILTER function

The next step is to implement the logic above inside the [FILTER function](https://exceljet.net/functions/filter-function)
. To filter the dates to show those expiring within 15 days, we embed the expression explained above inside FILTER like this:

    FILTER(data,data[Expires]-date<=days)
    

The _array_ argument is the [Excel Table](https://exceljet.net/glossary/excel-table)
 **data**, and the _include_ argument is the logical expression explained above. In this configuration, FILTER returns the five rows from the table where the Expires date has already occurred or will occur in the next 15 days. Note that this result is based on the current date in cell H2, which is 7-July-2022.

### SORT function

The final step in the problem is to sort the data by expiration date, so that dates already expired are listed first, followed by dates expiring soon in the order they will expire. This can be done by [nesting](https://exceljet.net/glossary/nesting)
 the FILTER formula inside the [SORT function](https://exceljet.net/functions/sort-function)
 like this:

    =SORT(FILTER(data,data[Expires]-date<=days),4)
    

Here, the _array_ provided to SORT is the result returned by FILTER, and _sort\_index_ is given as 4, since the "Expires" date is in the fourth column of the table.

### Current date

In the worksheet shown, the current date is provided by the [TODAY function](https://exceljet.net/functions/today-function)
:

    =TODAY()
    

TODAY takes no arguments, and will return the current date on an ongoing basis. This is often what you want in real life, where the data being tracked is always changing. However, it can be confusing in the case of this example, because the worksheet in the future will not look the same as the worksheet looks today. To make the worksheet look like it did on July 7, 2022, just hardcode that date into cell H2.  

### Conditional formatting

In the example shown, [conditional formatting](https://exceljet.net/articles/conditional-formatting-with-formulas)
 is used to highlight dates that have _already_ expired. The formula used to apply the rule is based on the [AND function](https://exceljet.net/functions/and-function)
:

    =AND($J5<>"",$J5<=date)
    

In this formula, we check two conditions: (1) the date in J5 is not empty and (2) the date in J5 is less than or equal to (<=) **date** (H2), which holds the current date. This is an example of a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 – the column is locked in order to [highlight the entire row](https://exceljet.net/formulas/highlight-entire-rows)
.

### Expires date

The date in the "Expires" column is calculated with the [EDATE function](https://exceljet.net/functions/edate-function)
. The formula in E5 is:

    =EDATE(C5,D5)
    

Starting with the "Replaced" date, EDATE returns moves forward the number of months given in "Months" and returns the resulting date.

Related formulas
----------------

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Calculate time before expiration date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_time_before_expiration_date.png "Excel formula: Calculate time before expiration date")](https://exceljet.net/formulas/calculate-time-before-expiration-date)

### [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)

In this example, the goal is to calculate the time remaining before an expiration date. There are many ways to do something like this in Excel, and in this article, we'll look at three different approaches: Calculating the remaining time in days Calculating the remaining time in years, months, and...

[![Excel formula: Filter by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_by_date.png "Excel formula: Filter by date")](https://exceljet.net/formulas/filter-by-date)

### [Filter by date](https://exceljet.net/formulas/filter-by-date)

This example shows how to filter dates using Excel's FILTER function. Several common date-based filtering patterns are shown below, including filtering by month, filtering by a specific date, and filtering by month and year. Filter by month In the worksheet below, the goal is to filter the data to...

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

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

*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)
    
*   [Filter by date](https://exceljet.net/formulas/filter-by-date)
    
*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

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
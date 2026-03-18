# Average call time per month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-call-time-per-month

---

[Skip to main content](https://exceljet.net/formulas/average-call-time-per-month#main-content)

[](https://exceljet.net/formulas/average-call-time-per-month#)

*   [Previous](https://exceljet.net/formulas/average-by-month)
    
*   [Next](https://exceljet.net/formulas/average-hourly-pay-per-day)
    

[Average](https://exceljet.net/formulas#Average)

Average call time per month
===========================

by Dave Bruns · Updated 28 Apr 2025

Related functions 
------------------

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[EDATE](https://exceljet.net/functions/edate-function)

[FILTER](https://exceljet.net/functions/filter-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Average call time per month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_call_time_per_month.png "Excel formula: Average call time per month")

Summary
-------

To calculate average call time (duration) per month, you can use the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
, with the [EDATE function](https://exceljet.net/functions/edate-function)
. In the example shown, the formula in H5 is:

    =AVERAGEIFS(data[Duration],data[Date],">="&G5,data[Date],"<"&EDATE(G5,1))
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:E16, and the values in G5:G8 are valid [Excel dates](https://exceljet.net/glossary/excel-date)
. As the formula is copied down, the result is the average call duration for each month listed in column G.

Generic formula
---------------

    =AVERAGEIFS(durations,dates,">="&A1,dates,"<"&EDATE(A1,1))

Explanation 
------------

In this example, the goal is to calculate the average call time (duration in minutes) for each month listed in column G using the dates in column B and the durations in column E. The article below explains two approaches. The first formula is based on the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
, which is designed to calculate averages using multiple criteria. The second formula is based on the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [AVERAGE function](https://exceljet.net/functions/average-function)
. For convenience, all data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range B5:E16.

_Note: the values in G5:G8 are valid_ [_Excel dates_](https://exceljet.net/glossary/excel-date)
_. This makes it easier to use these values in the formula criteria. You can use a_ [_custom number format_](https://exceljet.net/articles/custom-number-formats)
 _to display these dates any way you like._

### AVERAGEIFS function

The AVERAGEIFS function calculates the average of cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. The generic syntax for AVERAGEIFS looks like this:

    =AVERAGEIFS(avg_range,range1,criteria1,range2,criteria2,...)

Notice each condition is entered as a separate \[_range_, _criteria_\] pair. In this problem, we need to configure AVERAGEIFS to average amounts by month using two criteria: (1) dates greater than or equal to the _first_ day of the month, (2) dates less than the first day of the _next month_. We start off with the _average range_, which is the call durations column in the table:

    =AVERAGEIFS(data[Duration],

Next, we need to enter the criteria needed to target the right dates for each month. To make this step easier, the values in G5:G8 are entered as "first of month" dates. For the start date, we use the **data\[Date\]** column for the _criteria range_ and the greater than or equal to operator (>=) [concatenated](https://exceljet.net/glossary/concatenation)
 to cell G5 for the _criteria:_

    =AVERAGEIFS(data[Duration],data[Date],">="&G5,

For the end date, we again use the **data\[Date\]** column for the _criteria range:_

    =AVERAGEIFS(data[Duration],data[Date],">="&G5,data[Date],

For _criteria_, we use the [EDATE function](https://exceljet.net/functions/edate-function)
 to return the _first day of the next month_:

    =EDATE(E5,1) // first of next month
    

The final formula in H5, copied down, is:

    =AVERAGEIFS(data[Duration],data[Date],">="&G5,data[Date],"<"&EDATE(G5,1))

Notice we need to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the dates to [logical operators](https://exceljet.net/glossary/logical-operators)
, as required by the AVERAGEIFS function. The [structured references](https://exceljet.net/glossary/structured-reference)
 behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
 and don't change, while the reference to G5 is [relative](https://exceljet.net/glossary/relative-reference)
 and changes at each new row. As the formula is copied down, it returns an average call duration for each month in column G.

### FILTER with AVERAGE

Another nice way to average by month is to use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [AVERAGE function](https://exceljet.net/functions/average-function)
 like this:

    =AVERAGE(FILTER(data[Duration],TEXT(data[Date],"mmyy")=TEXT(G5,"mmyy")))

Working from the inside out, the FILTER function extracts the durations for a given month and returns these amounts to the AVERAGE function, which calculates an average. The FILTER function is configured like this:

    FILTER(data[Duration],TEXT(data[Date],"mmyy")=TEXT(G5,"mmyy"))

The first argument, _array_, is set to **data\[Duration\]**. The second argument, _include_, is where most of the work gets done:

    TEXT(data[Date],"mmyy")=TEXT(G5,"mmyy")

Here, we use the [TEXT function](https://exceljet.net/functions/text-function)
 to convert the **dates** to [text strings](https://exceljet.net/glossary/text-value)
 in the format "mmyy". Because there are 12 dates in the list, all in 2023, the result is an [array](https://exceljet.net/glossary/array)
 with 12 values like this:

    {"0123";"0123";"0123";"0223";"0223";"0223";"0223";"0323";"0323";"0323";"0323";"0423"}
    

Next, the TEXT function is used in the same way to extract the month and year from the date in G5:

    TEXT(G5,"mmyy") // returns "0123"
    

The two results above are then compared to each other. The result is an array of 12 TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

In this array, a TRUE value indicates dates in B5:B16 that are in the same month and year as the date in G5, i.e. January dates. The FILTER function uses this array to retrieve only values in January. The result is delivered directly to the AVERAGE function like this:

    {0.0111111111111111;0.0118055555555556;0.0173611111111112}

Excel times are just [fractional parts of 1 day](https://exceljet.net/glossary/excel-time)
, so the decimal numbers represent time in a raw number format. AVERAGE then returns a result of approximately 0.01343, which, when formatted with the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mm:ss", displays as 19:20. As the formula is copied down, FILTER delivers durations for each month to the AVERAGE function, which returns a final result.

_Note: the overall structure of this formula is more compact and elegant, so you might wonder why we don't use the TEXT function in the same way with the AVERAGEIFS function? Unfortunately, this is not possible because AVERAGEIFS won't accept an array operation in a range argument. This is a limitation of the \*IFS functions in Excel, which you can_ [_read more about here_](https://exceljet.net/articles/excels-racon-functions)
_._

### Pivot Table solution

A pivot table is an excellent solution when you need to summarize or average data by year, month, quarter, and so on, because pivot tables provide controls for grouping dates automatically. For a side-by-side comparison of formulas vs. pivot tables, see this video: [Why pivot tables](https://exceljet.net/plc/why-pivot-tables)
.

Related formulas
----------------

[![Excel formula: Average by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_month.png "Excel formula: Average by month")](https://exceljet.net/formulas/average-by-month)

### [Average by month](https://exceljet.net/formulas/average-by-month)

In this example, the goal is to calculate a monthly average for the amounts shown in column C using the dates in column B. The article below explains two approaches. One approach is based on the AVERAGEIFS function , which is designed to calculate averages using multiple criteria. The second...

[![Excel formula: Average by group](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_group.png "Excel formula: Average by group")](https://exceljet.net/formulas/average-by-group)

### [Average by group](https://exceljet.net/formulas/average-by-group)

In this example, the goal is to create a formula that calculates an average by group, using the group names in column C. The solution shown requires three general steps: Create an Excel Table called data List unique groups with the UNIQUE function Calculate averages with the AVERAGEIFS function...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

Related functions
-----------------

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageifs-function)

### [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)

In this video we'll look at how to use the AVERAGEIFS function to calculate an average from numbers that meet multiple criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the criteria shown in column K. Note that this data already...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-create-an-excel-table)

### [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

In this video, we'll look at how to create an Excel table. Here we have some data that is a good candidate for a table. Each row represents an entry or record with information that belongs together. Each column has a unique name. The first step in creating a table is to remove any blank rows or...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_time_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)

### [How to use time formatting in Excel](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)

In this lesson we'll look at the Time format. Like the Date format, the Time format includes a number of built-in options for displaying time. Let's take a look. Here we have a set of times in column B of our table. Let's start off by copying these times to all columns, then adjust formats to match...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average by month](https://exceljet.net/formulas/average-by-month)
    
*   [Average by group](https://exceljet.net/formulas/average-by-group)
    
*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    

### Functions

*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Videos

*   [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)
    
*   [How to use time formatting in Excel](https://exceljet.net/videos/how-to-use-time-formatting-in-excel)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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
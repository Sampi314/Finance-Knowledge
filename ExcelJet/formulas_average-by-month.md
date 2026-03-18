# Average by month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-by-month

---

[Skip to main content](https://exceljet.net/formulas/average-by-month#main-content)

[](https://exceljet.net/formulas/average-by-month#)

*   [Previous](https://exceljet.net/formulas/average-by-group)
    
*   [Next](https://exceljet.net/formulas/average-call-time-per-month)
    

[Average](https://exceljet.net/formulas#Average)

Average by month
================

by Dave Bruns · Updated 10 Jan 2023

Related functions 
------------------

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[EDATE](https://exceljet.net/functions/edate-function)

[FILTER](https://exceljet.net/functions/filter-function)

[AVERAGE](https://exceljet.net/functions/average-function)

![Excel formula: Average by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_by_month.png "Excel formula: Average by month")

Summary
-------

To calculate an average by month, you can use the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
, with help from the [EDATE function](https://exceljet.net/functions/edate-function)
. In the example shown, the formula in F5 is:

    =AVERAGEIFS(amount,date,">="&E5,date,"<"&EDATE(E5,1))
    

where **amount** (C5:C16) and **date** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: The values in E5:E10 are valid [Excel dates](https://exceljet.net/glossary/excel-date)
 with the_ _[number format](https://exceljet.net/glossary/number-format)
 "mmm" applied._

Generic formula
---------------

    =AVERAGEIFS(values,dates,">="&A1,dates,"<"&EDATE(A1,1))

Explanation 
------------

In this example, the goal is to calculate a monthly average for the amounts shown in column C using the dates in column B. The article below explains two approaches. One approach is based on the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
, which is designed to calculate averages using multiple criteria. The second approach is based on the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [AVERAGE function](https://exceljet.net/functions/average-function)
. For convenience only, both solutions use the [named ranges](https://exceljet.net/glossary/named-range)
 **amount** (C5:C16) and **date** (B5:B16).

_Note: the values in E5:E10 are valid [Excel dates](https://exceljet.net/glossary/excel-date)
, formatted to display the month name only with the_ _[number format](https://exceljet.net/glossary/number-format)
 "mmm". See below for more information._

### AVERAGEIFS function

The AVERAGEIFS function calculates the average of cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. The generic syntax for AVERAGEIFS looks like this:

    =AVERAGEIFS(avg_range,range1,criteria1,range2,criteria2,...)

In this problem, we need to configure AVERAGEIFS to average amounts by month using two criteria: (1) dates greater than or equal to the _first_ day of the month, (2) dates less than the first day of the _next month_. We start off with the _average range_, which contains the values to average in **data** (C5:C16):

    =AVERAGEIFS(amount,

Next, we need to enter the criteria needed to target the appropriate dates for each month. To make this step easier, the values in E5:E10 are all first of month dates formatted to show an abbreviated month name. To enter a criteria for the start date, we use the named range **date** (B5:B16) followed by a greater than or equal to operator (>=)  [concatenated](https://exceljet.net/glossary/concatenation)
 to cell E5:

    =AVERAGEIFS(amount,date,">="&E5,

To enter criteria for the end date, we use the [EDATE function](https://exceljet.net/functions/edate-function)
 to advance one full month to the _first day of the next month_:

    =EDATE(E5,1) // first of next month
    

We can then use the less than operator (<) to select the correct dates. The final formula in F5, copied down, is:

    =AVERAGEIFS(amount,date,">="&E5,date,"<"&EDATE(E5,1))

Roughly translated, the meaning of this formula is "Average the amounts in B6:B16 when the date in C5:C16 is greater than or equal to the date in E5 and less than the first day of the _next_ month". Notice we need to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the dates to [logical operators](https://exceljet.net/glossary/logical-operators)
, as required by the AVERAGEIFS function. As the formula is copied down, it returns a total for each month in column E. The named ranges behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
 and don't change, while the reference to E5 is [relative](https://exceljet.net/glossary/relative-reference)
 and changes at each new row.

_Note: we could use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 to get the last day of the current month, then use "<=" as the second logical operator. However, because EOMONTH returns a date that is technically midnight, t__here is a danger of excluding [dates with times](https://exceljet.net/glossary/excel-datetime)
 that occur on the last of the month. Using EDATE is a simpler and more robust solution._

### FILTER with AVERAGE

Another nice way to average by month is to use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [AVERAGE function](https://exceljet.net/functions/average-function)
 like this:

    =AVERAGE(FILTER(amount,TEXT(date,"mmyy")=TEXT(E5,"mmyy")))

At a high level, the FILTER function extracts the amounts for a given month, and returns these amounts to the AVERAGE function, which calculates an average. The FILTER function is configured like this:

    FILTER(amount,TEXT(date,"mmyy")=TEXT(E5,"mmyy"))

The first argument, _array_, is set to **amount** (C5:C16). The second argument, include, is where most of the work gets done:

    TEXT(date,"mmyy")=TEXT(E5,"mmyy")

Here, we use the [TEXT function](https://exceljet.net/functions/text-function)
 to convert the **dates** to [text strings](https://exceljet.net/glossary/text-value)
 in the format "mmyy". Because there are 12 dates in the list, the result is an [array](https://exceljet.net/glossary/array)
 with 12 values like this:

    {"0122";"0222";"0222";"0322";"0322";"0322";"0422";"0422";"0422";"0522";"0522";"0522"}
    

Next, the TEXT function is used in the same way to extract the month and year from the date in E5:

    TEXT(E5,"mmyy") // returns "0122"
    

The two results above are then compared to each other. The result is an array of TRUE and FALSE values like this:

    {TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

In this array, a TRUE value indicates dates in B5:B16 that are in the same month and year as the date in E5. As you can see, only the first date occurs in January 2022. The FILTER function uses this array to select only values in **data** that meet criteria. The result is delivered directly to the AVERAGE function like this:

    =AVERAGE({100})

AVERAGE then returns a result of 100. As the formula is copied down, FILTER delivers amounts for each month to the AVERAGE function, which returns a final result.

One nice feature of this formula is that it automatically ignores time values that may be attached to dates, so there is no need to worry about excluding dates on the last day of the month that include time values, as with AVERAGEIFS above. This is because the logic created with the TEXT function only compares month and year values. It would be nice to use the TEXT function inside the AVERAGEIFS formula as well, but the AVERAGEIFS function [won't accept an array operation in a range argument](https://exceljet.net/articles/excels-racon-functions)
.

### Display dates as names

To display the dates in E5:E10 as names only, you can apply a [custom number format](https://exceljet.net/articles/custom-number-formats)
. Select the dates, then use Control + 1 to bring up the [Format Cells Dialog](https://exceljet.net/shortcuts/format-almost-anything)
 box and apply the "mmm" date format as shown below:

![Custom number format to display month only](https://exceljet.net/sites/default/files/images/formulas/inline/average_by_month_custom_number_format.png "Custom number format to display month only")

This allows you to use [valid Excel dates](https://exceljet.net/glossary/excel-date)
 in column E (required for the formula) but display them as month names only.

### Pivot Table solution

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 is another excellent solution when you need to summarize data by year, month, quarter, and so on, because it can do this kind of grouping for you without any formulas at all. For a side-by-side comparison of formulas vs. pivot tables, see this video: [Why pivot tables](https://exceljet.net/plc/why-pivot-tables)
.

Related formulas
----------------

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Average call time per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_call_time_per_month.png "Excel formula: Average call time per month")](https://exceljet.net/formulas/average-call-time-per-month)

### [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)

In this example, the goal is to calculate the average call time (duration in minutes) for each month listed in column G using the dates in column B and the durations in column E. The article below explains two approaches. The first formula is based on the AVERAGEIFS function , which is designed to...

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

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageifs-function)

### [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)

In this video we'll look at how to use the AVERAGEIFS function to calculate an average from numbers that meet multiple criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the criteria shown in column K. Note that this data already...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    
*   [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)
    

### Functions

*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    

### Videos

*   [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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
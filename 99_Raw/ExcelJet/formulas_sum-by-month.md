# Sum by month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-by-month

---

[Skip to main content](https://exceljet.net/formulas/sum-by-month#main-content)

[](https://exceljet.net/formulas/sum-by-month#)

*   [Previous](https://exceljet.net/formulas/sum-by-group)
    
*   [Next](https://exceljet.net/formulas/sum-by-month-ignore-year)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum by month
============

by Dave Bruns · Updated 11 Feb 2023

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[EDATE](https://exceljet.net/functions/edate-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[TEXT](https://exceljet.net/functions/text-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7460/download?token=oe9zwW6m)
 (14.68 KB)

![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")

Summary
-------

To sum a set of data by month, you can use a formula based on the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 and the [EDATE function](https://exceljet.net/functions/edate-function)
. In the example shown, the formula in F5 is:

    =SUMIFS(amount,date,">="&E5,date,"<"&EDATE(E5,1))
    

where **amount** (C5:C16) and **date** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: The values in E5:E10 are valid [Excel dates](https://exceljet.net/glossary/excel-date)
 with the_ _[number format](https://exceljet.net/glossary/number-format)
 "mmm" applied._

Generic formula
---------------

    =SUMIFS(values,dates,">="&A1,dates,"<"&EDATE(A1,1))

Explanation 
------------

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the [SUMIFS function](https://exceljet.net/functions/sumif-function)
, which can sum numeric values based on multiple criteria. The second approach is based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, which allows a more flexible solution. For convenience, both solutions use the [named ranges](https://exceljet.net/glossary/named-range)
 **amount** (C5:C16) and **date** (B5:B16).

_Note: the values in E5:E10 are valid [Excel dates](https://exceljet.net/glossary/excel-date)
, formatted to display the month name only with the_ _[number format](https://exceljet.net/glossary/number-format)
 "mmm". See below for more information._

### SUMIFS solution

The [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 can sum values in ranges based on multiple criteria. The syntax for SUMIFS looks like this:

    =SUMIFS(sum_range,range1,criteria1,range2,criteria2,...)
    

In this problem, we need to configure SUMIFS to sum values by month using two criteria: one for a start date, and one for an end date. We start off with the _sum\_range_, which contains the values to sum in **amount** (C5:C16):

    =SUMIFS(amount,

To enter a criteria for the start date, we use the named range **date** (B5:B16) followed by a greater than or equal to operator (>=)  [concatenated](https://exceljet.net/glossary/concatenation)
 to cell E5:

    =SUMIFS(amount,date,">="&E5,

This works because cell E5 already contains the first day of the month, formatted to display the month only. To enter criteria for the end date, we use the [EDATE function](https://exceljet.net/functions/edate-function)
 to advance one full month to the _first day of the next month_:

    =EDATE(E5,1) // first of next month
    

We can then use the less than operator (<) to select the correct dates. The final formula in F5, copied down, is:

    =SUMIFS(amount,date,">="&E5,date,"<"&EDATE(E5,1))
    

Roughly translated, the meaning of this formula is "Sum the amounts in C6:C16 when the date in B5:B16 is greater than or equal to the date in E5 and less than the first day of the _next_ month". Notice we need to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the dates to [logical operators](https://exceljet.net/glossary/logical-operators)
, as required by the SUMIFS function. As the formula is copied down, it returns a total for each month in column E. The named ranges behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
 and don't change, while the reference to E5 is [relative](https://exceljet.net/glossary/relative-reference)
 and changes at each new row.

_Note: we could use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 to get the last day of the current month, then use "<=" as the second logical operator. However, because EOMONTH returns a date that is technically midnight, t__here is a danger of excluding [dates with times](https://exceljet.net/glossary/excel-datetime)
 that occur on the last of the month. Using EDATE is a simpler and more robust solution._

### With hardcoded dates

To use the SUMIFS function with hardcoded dates, the best approach is to use the [DATE function](https://exceljet.net/functions/date-function)
 like this:

    =SUMIFS(amount,date,">="&DATE(2021,1,1),date,"<"&DATE(2021,2,1))
    

This formula uses the DATE function to create the first and last days of the month. This is a safer option than entering a date as text, because it guarantees that Excel will interpret the date correctly.

### SUMPRODUCT option

Another nice way to sum by month is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together like this:

    =SUMPRODUCT((TEXT(date,"mmyy")=TEXT(E5,"mmyy"))*amount)
    

In this version, we use the [TEXT function](https://exceljet.net/functions/text-function)
 to convert the **dates** to [text strings](https://exceljet.net/glossary/text-value)
 in the format "mmyy". Because there are 12 dates in the list, the result is an [array](https://exceljet.net/glossary/array)
 with 12 values like this:

    {"0122";"0222";"0222";"0322";"0322";"0322";"0422";"0422";"0422";"0522";"0522";"0522"}
    

Next, the TEXT function is used in the same way to extract the month and year from the date in E5:

    TEXT(E5,"mmyy") // returns "0122"
    

The two results above are then compared to each other. The result is an array of TRUE and FALSE values like this:

    {TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

This array indicates the dates in B5:B16 that are in the same month and year as the date in E5. The TRUE value in this array corresponds to the only date in January 2022. This array is then multiplied by the values in **amount**. The math operation automatically coerces the TRUE and FALSE values to 1s and 0s, so the final result inside SUMPRODUCT looks like this:

    =SUMPRODUCT({100;0;0;0;0;0;0;0;0;0;0;0}) // returns 100
    

With just one array to process, the SUMPRODUCT sums the array and returns 100 as the result in F5. As the formula is copied down, the [relative reference](https://exceljet.net/glossary/relative-reference)
 E5 changes at each new row, and SUMPRODUCT generates a new result. One nice feature of this formula is that it automatically ignores time values that may be attached to dates, so there is no need to worry about excluding [datetimes](https://exceljet.net/glossary/excel-datetime)
 that occur on the last day of the month, as with SUMIFS above.

_Notes: (1) In the current version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can substitute the SUM function for the SUMPRODUCT function. [This article](https://exceljet.net/articles/why-sumproduct)
 explains the details. (2) It would be nice to use the TEXT function inside the SUMIFS formula as well, but_ the _SUMIFS function [won't accept an array operation in a range argument](https://exceljet.net/articles/excels-racon-functions)
._

### Display dates as names

To display the dates in E5:E10 as names only, you can apply the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mmmm". Select the dates, then use Control + 1 to bring up the [Format Cells Dialog](https://exceljet.net/shortcuts/format-almost-anything)
 box and apply the date format as shown below:

![Custom number format to display month names](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/custom%20number%20format%20for%20month%20names.png?itok=p415XXvr "Custom number format to display month names")

This allows you to use [valid Excel dates](https://exceljet.net/glossary/excel-date)
 in column E (required for the formula) and display them as you like.

### Pivot Table solution

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 is another excellent solution when you need to summarize data by year, month, quarter, and so on, because it can do this kind of grouping for you without any formulas at all. For a side-by-side comparison of formulas vs. pivot tables, see this video: [Why pivot tables](https://exceljet.net/plc/why-pivot-tables)
.

Related formulas
----------------

[![Excel formula: Sum by month in columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month_in_columns.png "Excel formula: Sum by month in columns")](https://exceljet.net/formulas/sum-by-month-in-columns)

### [Sum by month in columns](https://exceljet.net/formulas/sum-by-month-in-columns)

In this example, the goal is to construct a formula that will subtotal the amounts in column D by client and month as seen in the range G5:I8. A big part of the problem is to set up the proper references so that the formula can be entered once, and copied throughout G5:I8. The solution explained...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")](https://exceljet.net/formulas/sum-by-week)

### [Sum by week](https://exceljet.net/formulas/sum-by-week)

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named data in the range B5:C16. This problem can be solved in a straightforward way with the SUMIFS function . In the current version of...

[![Excel formula: Sum by month ignore year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20month%20ignore%20year.png "Excel formula: Sum by month ignore year")](https://exceljet.net/formulas/sum-by-month-ignore-year)

### [Sum by month ignore year](https://exceljet.net/formulas/sum-by-month-ignore-year)

In this example, the goal is to sum numeric values by month while ignoring the year that contains the date. The solution below is based on the SUMPRODUCT function, the MONTH function, and Boolean algebra . For convenience, amount (C5:C16) and date (B5:B16) are named ranges . Basic concept The basic...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum by month in columns](https://exceljet.net/formulas/sum-by-month-in-columns)
    
*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Sum by week](https://exceljet.net/formulas/sum-by-week)
    
*   [Sum by month ignore year](https://exceljet.net/formulas/sum-by-month-ignore-year)
    
*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Videos

*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    

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
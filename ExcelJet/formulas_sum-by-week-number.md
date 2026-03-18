# Sum by week number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-by-week-number

---

[Skip to main content](https://exceljet.net/formulas/sum-by-week-number#main-content)

[](https://exceljet.net/formulas/sum-by-week-number#)

*   [Previous](https://exceljet.net/formulas/sum-by-week)
    
*   [Next](https://exceljet.net/formulas/sum-by-weekday)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum by week number
==================

by Dave Bruns · Updated 28 Mar 2025

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[WEEKNUM](https://exceljet.net/functions/weeknum-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[BYROW](https://exceljet.net/functions/byrow-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

![Excel formula: Sum by week number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20by%20week%20number.png "Excel formula: Sum by week number")

Summary
-------

To sum values by week number, you can use a formula based on the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 and the [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
. In the example shown, the formula in G5 is:

    =SUMIFS(data[Amount],data[Week],G5)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:E16, and the week numbers in column E are generated with the [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
.

Generic formula
---------------

    =SUMIFS(sum_range,week_range,week)

Explanation 
------------

In this example, the goal is to sum the amounts in column D by week number, using the dates in column C to determine the week number. The week numbers in column G are manually entered. The final results should appear in column H. All data is in an Excel Table named **data** in the range B5:E16. This problem can be solved with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 and the [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
 as explained below.

### WEEKNUM function

The first step in this problem is to generate a week number for each date in column B. In the table shown, column E is a [helper column](https://exceljet.net/glossary/helper-column)
 with week numbers generated with the [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
. The formula in E5, copied down, is:

    =WEEKNUM([@Date],2) // get week number
    

_Note: because we are using an_ [_Excel Table_](https://exceljet.net/articles/excel-tables)
 _to hold the data, we automatically get the_ [_structured reference_](https://exceljet.net/glossary/structured-reference)
 _seen above. The reference \[@Date\] means: current row in Date column. If you are new to structured references, see this short video:_ [_Introduction to structured references_](https://exceljet.net/videos/introduction-to-structured-references)
_._

The WEEKNUM function takes a valid [Excel date](https://exceljet.net/glossary/excel-date)
 as the first argument. The second argument is called _return\_type_ and indicates the day of the week that week numbers should begin. Setting _return\_type_ to 2 specifies that week numbers should begin on Mondays.

### SUMIFS solution

The next step in the problem is to add up the amounts in column D using the week numbers in column E. This can easily be done with the SUMIFS function. The [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 is designed to sum values in ranges _conditionally_ based on multiple criteria. The signature of the SUMIFS function looks like this:

    =SUMIFS(sum_range,range1,criteria1,range2,criteria2,...)
    

Notice the _sum\_range_ comes first, followed by _range/criteria_ pairs. Each range/criteria pair of arguments represents another condition.

In this case, we need to configure SUMIFS to sum values by week number using just one condition: we need to check the week number in column E for a match in the week number in column G. We start off with the _sum\_range_:

    =SUMIFS(data[Amount]
    

Next, we add criteria as a _range/criteria_ pair, where _criteria\_range1_ is the date column, and _criteria1_ is the week number in column G:

    =SUMIFS(data[Amount],data[Week],G5)
    

_Note: we don't use data\[Week\]=G5 because SUMIFS is in a_ [_group of eight functions_](https://exceljet.net/articles/excels-racon-functions)
 _that split formula criteria into two parts._

As the formula is copied down, we get a total for each week number in column G.

### Dynamic array solution

In the latest version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, it is possible to create a single all-in-one formula that builds the entire summary table, including headers, like this:

    =LET(
    weeks,WEEKNUM(+data[Date],2),
    amounts,data[Amount],
    uweeks,UNIQUE(weeks),
    totals, BYROW(uweeks, LAMBDA(r, SUM((weeks=r)*amounts))),
    VSTACK({"Week","Total"},HSTACK(uweeks, totals))
    )
    

The [LET function](https://exceljet.net/functions/let-function)
 is used to assign four intermediate variables: _weeks_, _uweeks,_ _totals_, and _totals_. The value for _weeks_ is created like this:

    WEEKNUM(+data[Date],2) // get all weeks
    

Here, the [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
 is used to fetch week numbers for all dates in **data\[Date\]**. Because the table contains 12 rows, the result is an [array](https://exceljet.net/glossary/array)
 with 12 week numbers like this:

    {1;1;2;2;3;3;4;5;5;6;6;6}
    

_Note: the + operator before data\[Date\] is a workaround for some Excel functions that don't_ [_spill_](https://exceljet.net/glossary/spill)
 _properly._

In the next line, we assign a value to _amounts_ like this:

    amounts,data[Amount]
    

_Note: Technically, we could just use the reference to data\[Amount\], but defining a variable here keeps all worksheet references at the top of the formula where they can be easily changed._

In our summary table, we want a list of unique week numbers, so we define _uweeks_ (unique weeks) with the [UNIQUE function](https://exceljet.net/functions/unique-function)
 like this:

    UNIQUE(weeks) // get unique week numbers
    

From the 12 week numbers seen above, the UNIQUE function returns just 6 _unique_ numbers:

    {1;2;3;4;5;6} // unique week numbers
    

_Note: You could run these week numbers through the_ [_SORT function_](https://exceljet.net/functions/sort-function)
 _to ensure that weeks are in the correct order, but a better approach would be to SORT the dates themselves before extracting the week numbers. This is because week numbers in Excel can vary in the early part of a year. For example, the first few days of a year could be in week number 53._

At this point, we are ready to sum amounts by week number. We do this with the [BYROW function,](https://exceljet.net/functions/byrow-function)
 which calculates the sums and assigns the result to the variable _totals_ for each week, like this:

    totals, BYROW(uweeks, LAMBDA(r, SUM((weeks=r)*amounts)))
    

BYROW runs through the _uweeks_ values row by row. At each row, it applies this calculation:

    LAMBDA(r, SUM((weeks=r)*amounts))
    

The value for r is the week number in the "current" row. Inside the SUM function, this value is compared to _weeks_. Since _weeks_ contains all 12 values, the result is an array with 12 TRUE and FALSE results. The TRUE and FALSE values are multiplied by _amounts_. The math operation automatically converts the TRUE and FALSE values to 1s and 0s, and the zeros effectively "cancel" the values in week numbers not equal to _r_. The [SUM function](https://exceljet.net/functions/sum-function)
 then sums the resulting array and returns the result. When BYROW is finished, we have an array with six sums like this:

    {204;202;230;165;280;450} // totals
    

This is the value assigned to _totals_.

Finally, the [HSTACK](https://exceljet.net/functions/hstack-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
 functions are used to assemble a complete table:

    VSTACK({"Week","Total"},HSTACK(uweeks, totals))
    

At the top of the table, the [array constant](https://exceljet.net/glossary/array-constant)
 {"Week","Total"} creates a header row. The HSTACK function combines _uweeks_ and _totals_ horizontally, and VSTACK combines the header row and the data to make the final table. The final result [spills](https://exceljet.net/glossary/spill)
 into multiple cells on the worksheet.

Related formulas
----------------

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")](https://exceljet.net/formulas/sum-by-week)

### [Sum by week](https://exceljet.net/formulas/sum-by-week)

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named data in the range B5:C16. This problem can be solved in a straightforward way with the SUMIFS function . In the current version of...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel WEEKNUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weeknum%20function.png "Excel WEEKNUM function")](https://exceljet.net/functions/weeknum-function)

### [WEEKNUM Function](https://exceljet.net/functions/weeknum-function)

The Excel WEEKNUM function takes a date and returns a week number (1-54) that corresponds to the week of year. The WEEKNUM function starts counting on the week that contains January 1. By default, weeks begin on Sunday, but this can be changed.

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

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
    
*   [Sum by week](https://exceljet.net/formulas/sum-by-week)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [WEEKNUM Function](https://exceljet.net/functions/weeknum-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    

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
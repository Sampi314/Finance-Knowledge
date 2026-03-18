# Sum by week - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-by-week

---

[Skip to main content](https://exceljet.net/formulas/sum-by-week#main-content)

[](https://exceljet.net/formulas/sum-by-week#)

*   [Previous](https://exceljet.net/formulas/sum-by-quarter)
    
*   [Next](https://exceljet.net/formulas/sum-by-week-number)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum by week
===========

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[LET](https://exceljet.net/functions/let-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[BYROW](https://exceljet.net/functions/byrow-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7473/download?token=xr6ly8cs)
 (15.75 KB)

![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")

Summary
-------

To sum values by week, you can use a formula based on the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in F5 is:

    =SUMIFS(data[Amount],data[Date],">="&E5,data[Date],"<"&E5+7)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C16, and the dates in E5:E10 are Mondays.

Generic formula
---------------

    =SUMIFS(values,date,">="&A1,date,"<"&A1+7)

Explanation 
------------

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named **data** in the range B5:C16. This problem can be solved in a straightforward way with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the current version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can also create an [all-in-one formula](https://exceljet.net/formulas/sum-by-week#dynamic_array)
 that builds the entire summary table in one step. Both approaches are explained in detail below.

### SUMIFS solution

The [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 can sum values in a range _conditionally_ based on multiple criteria. The pattern of the SUMIFS function looks like this:

    =SUMIFS(sum_range,range1,criteria1,range2,criteria2,...)
    

Notice the _sum\_range_ comes first, followed by _range/criteria_ pairs. Each _range/criteria_ pair of arguments represents another condition.

In this case, we need to configure SUMIFS to sum values by week using two criteria: one to match dates greater than or equal to the _first_ day of the week, one to match dates less than the first day of the _next_ week. We start off with the _sum\_range_ and the first condition:

    =SUMIFS(data[Amount],data[Date],">="&E5
    

_Note: because we are using an [Excel Table](https://exceljet.net/articles/excel-tables)
 to hold the data, we automatically get the [structured references](https://exceljet.net/glossary/structured-reference)
 seen above. If you are new to structured references, see this short video: [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
._

The _sum\_range_ is **data\[Amount\]**, _criteria\_range1_ is **data\[Date\]**, and _criteria1_ is ">="&E5. Notice we need to [concatenate](https://exceljet.net/glossary/concatenation)
 the greater than or equal to [operator](https://exceljet.net/glossary/logical-operators)
 (>=) to the reference E5. This is because SUMIFS is in a [group of eight functions](https://exceljet.net/articles/excels-racon-functions)
 that split formula criteria into two parts.

Next, we need to add a second _range/criteria_ pair of arguments to target dates through the last day of the week:

    =SUMIFS(data[Amount],data[Date],">="&E5,data[Date],"<"&E5+7)
    

Here, _criteria\_range2_ is again **data\[Date\]**, and _criteria2_ is "<"&E5+7. Basically, we add 7 days to the date in E5 and use the less than operator (<) to catch all days prior to the next week. Again, we need to use [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
 to join the operator to the cell reference. The reason we can add 7 days to E5 with simple addition is because [Excel Dates are just serial numbers](https://exceljet.net/glossary/excel-date)
.

The formula is now complete. As the formula is copied down column F, the SUMIFS formula will generate a sum for each week using the date in column F.

### Week of dates

The dates in column E are Mondays. The first date in E5 (3-Jan-22) is hard-coded, and the rest of the dates are calculated with a simple formula:

    =E5+7
    

At each new row, the formula returns the next Monday in the calendar.

### Dynamic array solution

In the current version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, it is possible to create a single all-in-one formula that builds out the entire summary table, including headers, in one step like this:

    =LET(
    dates,data[Date],
    amounts,data[Amount],
    weeks,dates-WEEKDAY(dates,3),
    uweeks,UNIQUE(weeks),
    totals,BYROW(uweeks,LAMBDA(r,SUM((weeks=r)*amounts))),
    VSTACK({"Week of","Total"},HSTACK(uweeks,totals)))
    

_Note: Currently, VSTACK and HSTACK are only available through the Beta channel of Office Insiders. The [Office Insiders program](https://insider.office.com/)
 is free to join in Excel 365._ 

The [LET function](https://exceljet.net/functions/let-function)
 is used to assign values to five variables: _dates_, _amounts, weeks, uweeks,_ and _totals_. First, we assign values to _dates_ and _amounts_ like this:

    =LET(
    dates,data[Date],
    amounts,data[Amount]
    

Technically, we could just use the references **data\[date\]** and **data\[Amount\]** throughout the formula, but defining these variables for these up front keeps all worksheet references at the top of the code where they can be easily changed. In other words, by editing just these two references, you can easily adapt the formula to work with a different data set.

Next, the value for _weeks_ is created like this:

    weeks,dates-WEEKDAY(dates,3)
    

Here the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
 is used to calculate a "Monday of the week" for each date in **data\[Date\]**. This formula is [explained in more detail here](https://exceljet.net/formulas/get-monday-of-the-week)
. Because the table contains 12 rows of data, the result is an [array](https://exceljet.net/glossary/array)
 with 12 dates like this:

    {44564;44564;44571;44578;44578;44578;44585;44592;44592;44592;44599;44599}
    

[Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
, so these are the raw numbers that correspond to the dates seen in E5:E10, which are all Mondays.

In the next line we define _uweeks_ (unique weeks) with the [UNIQUE function](https://exceljet.net/functions/unique-function)
 like this:

    uweeks,UNIQUE(weeks)
    

We do this because we only want one row per week in our final summary table. The UNIQUE function returns the 6 dates seen in E5:E10, which are all Mondays:

    {44564;44571;44578;44585;44592;44599}
    

_Note: you could sort the result from UNIQUE with the [SORT function](https://exceljet.net/functions/sort-function)
 to ensure that weeks are in the correct order if needed._

We are now ready to calculate the total amounts for each week. We do this with the [BYROW function](https://exceljet.net/functions/byrow-function)
 which generates the sums and assigns the result to the variable _totals_ like this:

    totals,BYROW(uweeks,LAMBDA(r,SUM((weeks=r)*amounts)))
    

BYROW runs through the _uweeks_ values row by row. At each row, it applies this calculation with the [LAMBDA function](https://exceljet.net/functions/lambda-function)
:

    LAMBDA(r,SUM((weeks=r)*amounts))
    

The value of _r_ is the date in the "current" row of _uweeks_. Inside the [SUM function](https://exceljet.net/functions/sum-function)
, the _r_ is compared to _weeks_. Since _weeks_ contains 12 dates for all 12 rows, the result is an array with 12 TRUE and FALSE results. The TRUE and FALSE values are multiplied by _amounts_. This math operation automatically converts the TRUE and FALSE values to 1s and 0s, and the zeros effectively "cancel out" the values in weeks not equal to _r_. The [SUM function](https://exceljet.net/functions/sum-function)
 then sums the resulting array. When BYROW is finished, we have an array with 6 weekly sums like this:

    {225;80;150;90;350;235} // totals
    

This is the value assigned to the variable _totals_.

Finally the [HSTACK](https://exceljet.net/functions/hstack-function)
 and [VSTACK](https://exceljet.net/functions/vstack-function)
 functions are used to assemble a complete table:

    VSTACK({"Week of","Total"},HSTACK(uweeks,totals))
    

At the top of the table, the [array constant](https://exceljet.net/glossary/array-constant)
 {"Week of","Total"} creates a header row. The [HSTACK function](https://exceljet.net/functions/hstack-function)
 combines _uweeks_ and _totals_ horizontally, and the [VSTACK function](https://exceljet.net/functions/vstack-function)
 combines the header row and result from HSTACK _vertically_ to make the final table. The final result [spills](https://exceljet.net/glossary/spill)
 into multiple cells on the worksheet.

### Pivot Table solution

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 is an excellent solution when you need to summarize data by year, month, quarter, and so on. For a side-by-side comparison of formulas vs. pivot tables, see this video: [Why pivot tables](https://exceljet.net/plc/why-pivot-tables)
.

Related formulas
----------------

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Sum by week number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week%20number.png "Excel formula: Sum by week number")](https://exceljet.net/formulas/sum-by-week-number)

### [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)

In this example, the goal is to sum the amounts in column D by week number, using the dates in column C to determine the week number. The week numbers in column G are manually entered. The final results should appear in column H. All data is in an Excel Table named data in the range B5:E16. This...

[![Excel formula: Sum by group](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20group.png "Excel formula: Sum by group")](https://exceljet.net/formulas/sum-by-group)

### [Sum by group](https://exceljet.net/formulas/sum-by-group)

In this example, the goal is to sum by group, where each group is represented by a different color: Blue, Red, Green, and Purple. The worksheet shown contains two different approaches. In the range F5:G8, we have created a summary table to summarize counts by color. In column D, we are using a...

[![Excel formula: Dynamic two-way sum](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20sum.png "Excel formula: Dynamic two-way sum")](https://exceljet.net/formulas/dynamic-two-way-sum)

### [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)

In this example, the goal is to create a formula that performs a dynamic two-way sum of all City and Size combinations in the range B5:D17 . The solution shown requires four basic steps: Create an Excel Table called data List unique cities with the UNIQUE function List unique sizes with the UNIQUE...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

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
    
*   [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)
    
*   [Sum by group](https://exceljet.net/formulas/sum-by-group)
    
*   [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    

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
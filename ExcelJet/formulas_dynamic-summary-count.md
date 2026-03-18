# Dynamic summary count - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-summary-count

---

[Skip to main content](https://exceljet.net/formulas/dynamic-summary-count#main-content)

[](https://exceljet.net/formulas/dynamic-summary-count#)

*   [Previous](https://exceljet.net/formulas/distinct-values)
    
*   [Next](https://exceljet.net/formulas/dynamic-two-way-average)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Dynamic summary count
=====================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[LET](https://exceljet.net/functions/let-function)

[SORT](https://exceljet.net/functions/sort-function)

[SCAN](https://exceljet.net/functions/scan-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7107/download?token=Qd_3tMMZ)
 (18.15 KB)

![Excel formula: Dynamic summary count](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20summary%20count.png "Excel formula: Dynamic summary count")

Summary
-------

To create a basic dynamic summary count with a formula, you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 to get unique values, and the [COUNTIF function](https://exceljet.net/functions/countif-function)
 to count those values in the data. In the example shown, the formula in F5 is:

    =COUNTIF(data,E5#)
    

Where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in B5:B16. With five values in E5:E9, COUNTIF returns the five counts to cell F5, and the results [spill](https://exceljet.net/glossary/spill)
 into the range F5:F9. See below for progressively more advanced options including all-in-one formulas.

Explanation 
------------

In this example, the goal is to build a simple summary count table with a formula. Once created, the summary table should automatically update to show new values and counts when data changes. The article below walks through several options, from simple to very advanced. The more advanced options show how to sort the table in descending order by count.

### Manual formula

Note that it is possible to build a summary table with formulas manually. The basic approach is to copy all values, use the Remove Duplicates command to get unique values, and then copy a COUNTIF formula into each cell that needs to show a count:

Video: [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

This works fine, but the summary table will not update automatically if new values are added or removed from the data. In other words, if a new color is added to the **data** table, it will not appear in the summary table.

### Pivot table

Another good approach is to use a [Pivot Table](https://exceljet.net/pivot-tables/pivot-table-basic-count)
. This is one of the easiest ways to create a summary count, and if you [use an Excel Table as the source data](https://exceljet.net/videos/why-you-should-use-a-table-for-your-pivot-table)
, the summary will stay in sync with the data. Also, the summary table can be easily sorted in a Pivot Table. However, a Pivot Table must be refreshed to see the latest data, and the solution is not a formula. Nevertheless, a pivot table is an excellent way to create a summary table.

Video: [How to quickly create a pivot table](https://exceljet.net/videos/how-to-quickly-create-a-pivot-table)

### Two formulas

In the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, a simple way to create a summary table is to use two formulas, one to collect unique values, and one to count the values. This is the solution shown in the worksheet at the top of the page. The formula in E5 is based on the UNIQUE function:

    =UNIQUE(data) // get unique values
    

The formula in F5 uses the COUNTIF function:

    =COUNTIF(data,E5#) // count unique values
    

Notice that inside COUNTIF, the table named **data** is provided as the _range_ argument, and the [spill reference](https://exceljet.net/glossary/spill-range)
 E5# is used for _criteria_. When source data changes, both formulas will stay in sync. In general this is a good, simple option. However, there are limitations. For example, because there are two separate formulas, we can't sort the results (in place) with the [SORT function](https://exceljet.net/functions/sort-function)
.

### All-in-one formula

A more advanced solution involves an all-in-one formula. One approach looks like this:

    =CHOOSE({1,2},UNIQUE(data),COUNTIF(data,UNIQUE(data)))
    

In this formula, we are using the [CHOOSE function](https://exceljet.net/functions/choose-function)
 to [combine two arrays](https://exceljet.net/formulas/combine-ranges-with-choose)
. The first array contains the unique values in the data:

    UNIQUE(data) // unique values
    

The second array is essentially the COUNTIF formula explained above, except the _criteria_ argument is created dynamically:

    COUNTIF(data,UNIQUE(data)) // counts
    

_Note: we are using CHOOSE function as a stand-in for the forthcoming [HSTACK function](https://exceljet.net/functions/hstack-function)
, which has just been released to the Beta Channel._

The CHOOSE function combines both arrays into a single array, which displays as a two-column table in the worksheet:

![All in one formula for a dynamic summary count table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/dynamic%20summary%20count%20all%20in%20one.png?itok=2Xnqj_0P "All in one formula for a dynamic summary count table")

### Sorting results

Now that we have a formula that returns the entire table, we can easily sort the table in descending order by count. To do this, we wrap the entire formula in the [SORT function](https://exceljet.net/functions/sort-function)
, and specify 2 for _sort\_index_ and -1 for _sort\_order_:

    =SORT(CHOOSE({1,2},UNIQUE(data),COUNTIF(data,UNIQUE(data))),2,-1)
    

Video: [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)

Now the table will update automatically if data changes, and the table will remain sorted by count, with highest counts at the top.

### With the LET function

We can use the [LET function](https://exceljet.net/functions/let-function)
 to streamline the formula a bit, by defining a variable, **u**, to hold the unique values:

    =LET(u,UNIQUE(data),SORT(CHOOSE({1,2},u,COUNTIF(data,u)),2,-1))
    

Notice this version of the formula calls the UNIQUE function once only, storing the result in **u**, which is used twice.

### Array option

As one of [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
, one limitation of COUNTIF is that it requires an actual [range](https://exceljet.net/glossary/range)
 for the _range_ argument. If you try to use the formula above on an in-memory [array](https://exceljet.net/glossary/array)
, you'll get an error. To workaround this limitation, we can use an even more advanced formula based on the [SCAN function](https://exceljet.net/functions/scan-function)
 together with the [LAMBDA function](https://exceljet.net/functions/lambda-function)
:

    =LET(u,UNIQUE(data),SORT(CHOOSE({1,2},u,SCAN(0,u,LAMBDA(a,v,SUM(--(v=data))))),2,-1))
    

_Note: The LAMBDA function lets you create custom functions in Excel. [More here](https://exceljet.net/functions/lambda-function)
._

At a high level, the mechanics of this formula are similar to the LET version above: UNIQUE gets unique values, CHOOSE combines two arrays, and SORT sorts the results. However, this formula uses a different method of counting, which is done here:

    SCAN(0,u,LAMBDA(a,v,SUM(--(v=data)))
    

Starting with an initial value of zero, SCAN loops through each value (**v**) in the unique array (u) and compares each value to data. The result is an array of TRUE and FALSE values which are coerced to 1s and 0s and summed with the SUM function here:

    SUM(--(v=data))
    

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

After looping through all values in **u**, SCAN returns an array that contains five counts. Next, CHOOSE joins the unique values (**u**) to the array result from SCAN, and the SORT function sorts the array returned by CHOOSE in descending order by count. Like the formula above, this formula will also update the table automatically, but it will also work with an array of data that is not in a range on the worksheet.

_Note: with slight changes, the [BYROW function](https://exceljet.net/functions/byrow-function)
 could be used instead of SCAN to produce the same result. Also note that CHOOSE is again standing in for [HSTACK](https://exceljet.net/functions/hstack-function)
 until HSTACK is available._

Related formulas
----------------

[![Excel formula: Dynamic two-way sum](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20sum.png "Excel formula: Dynamic two-way sum")](https://exceljet.net/formulas/dynamic-two-way-sum)

### [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)

In this example, the goal is to create a formula that performs a dynamic two-way sum of all City and Size combinations in the range B5:D17 . The solution shown requires four basic steps: Create an Excel Table called data List unique cities with the UNIQUE function List unique sizes with the UNIQUE...

[![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")](https://exceljet.net/formulas/dynamic-two-way-count)

### [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps: Create an Excel Table called data List unique colors with UNIQUE function List unique sizes with UNIQUE...

[![Excel formula: Combine ranges with CHOOSE](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join%20ranges%20with%20choose.png "Excel formula: Combine ranges with CHOOSE")](https://exceljet.net/formulas/combine-ranges-with-choose)

### [Combine ranges with CHOOSE](https://exceljet.net/formulas/combine-ranges-with-choose)

In this example, the goal is to join two one-dimensional ranges together horizontally. This can be done with the CHOOSE function and array constant . The CHOOSE function The CHOOSE function is used to select arbitrary values by numeric position. CHOOSE is a flexible function and accepts a list of...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)
    
*   [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)
    
*   [Combine ranges with CHOOSE](https://exceljet.net/formulas/combine-ranges-with-choose)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

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
# Excel GROUPBY function | Exceljet

**Source:** https://exceljet.net/functions/groupby-function

---

[Skip to main content](https://exceljet.net/functions/groupby-function#main-content)

[](https://exceljet.net/functions/groupby-function#)

*   [Previous](https://exceljet.net/functions/filter-function)
    
*   [Next](https://exceljet.net/functions/hstack-function)
    

Excel 365

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

GROUPBY Function
================

by Dave Bruns · Updated 27 Jun 2025

Related functions 
------------------

[PIVOTBY](https://exceljet.net/functions/pivotby-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

[PERCENTOF](https://exceljet.net/functions/percentof-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9035/download?token=tIQ2mAwY)
 (80.88 KB)

![Excel GROUPBY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_groupby_function.png "Excel GROUPBY function")

Summary
-------

The Excel GROUPBY function is designed to summarize data by grouping rows and aggregating values. The result is a summary table created with a single formula.

Purpose 
--------

Summarize data by grouping rows

Return value 
-------------

Data summary table

Syntax
------

    =GROUPBY(row_fields,values,function,[field_headers],[total_depth],[sort_order],[filter_array],[field_relationship])

*   _row\_fields_ - The values for grouping.
*   _values_ - The values to aggregate.
*   _function_ - The calculation to run when aggregating.
*   _field\_headers_ - \[optional\] 0 = No, 1 = Yes, don't show, 2 = No, generate, 3 = Yes, show.
*   _total\_depth_ - \[optional\] Totals and subtotals. 0 = No, 1 = Grand Totals, 2 = Both, -1 = Grand Totals at top, -2 = Both at top.
*   _sort\_order_ - \[optional\] Sort by index number. Negative numbers = descending order.
*   _filter\_array_ - \[optional\] Logic to exclude specific rows.
*   _field\_relationship_ - \[optional\] Field relationship when multiple columns are provided as row fields. 0 = Hierarchy (default), 1 = Table.

Using the GROUPBY function 
---------------------------

The GROUPBY function is designed to summarize data by grouping rows and aggregating values. The result is a dynamic summary table created with a single formula. The output from the GROUPBY function is similar to the output from a Pivot Table, but without formatting. The summary returned by the GROUPBY function is fully dynamic and will immediately recalculate when source data changes. Here is a brief list of GROUPBY features and limitations:

*   A simple and flexible way to make a summary table with a formula.
*   Can apply aggregation functions like SUM, AVERAGE, COUNT, COUNTA, etc.
*   Does not require a Pivot Table or helper columns.
*   Can group by more than one level (i.e., Region and Color, etc.).
*   Returns a dynamic array that automatically updates when data changes.
*   Able to exclude specific rows in the source data with logical expressions.
*   Does not apply formatting; you must apply formatting manually.
*   Only available in Excel 365.

> The GROUPBY function is similar to the [PIVOTBY function](https://exceljet.net/functions/pivotby-function)
> . The difference is that PIVOTBY can group by row and column, whereas GROUPBY can group by row only.

### Table of Contents

*   [GROUPBY basic example](https://exceljet.net/functions/groupby-function#basic-example)
    
*   [GROUPBY with field headers](https://exceljet.net/functions/groupby-function#groupby-field-headers)
    
*   [GROUPBY calculation options](https://exceljet.net/functions/groupby-function#calculation-options)
    
*   [GROUPBY with multiple calculations](https://exceljet.net/functions/groupby-function#multiple-calculations)
    
*   [GROUPBY with custom headers](https://exceljet.net/functions/groupby-function#custom-headers)
    
*   [GROUPBY with multiple columns](https://exceljet.net/functions/groupby-function#multiple-columns)
    
*   [GROUPBY total options](https://exceljet.net/functions/groupby-function#total-options)
    
*   [GROUPBY sort options](https://exceljet.net/functions/groupby-function#sort-options)
    
*   [GROUPBY with filter array](https://exceljet.net/functions/groupby-function#filter-array)
    
*   [GROUPBY with field relationships](https://exceljet.net/functions/groupby-function#field_relationships)
    
*   [GROUPBY with custom LAMBDA](https://exceljet.net/functions/groupby-function#custom-lambda)
    
*   [GROUPBY with a dynamic range](https://exceljet.net/functions/groupby-function#dynamic-range)
    

### GROUPBY basic example

The GROUPBY function takes _eight_ arguments, but only the first three are required. In the worksheet below, we use the GROUPBY function to summarize Sales by City. The formula in cell F5 is:

    =GROUPBY(B5:B16,D5:D16,SUM)

![GROUPBY function basic example - sum of sales by city](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_basic_example.png "GROUPBY function basic example - sum of sales by city")

For this example, GROUPBY is configured with three arguments as follows:

*   _row\_fields_ - provided as the range B5:B16, which contains city names.
*   _values_ - provided as the range D5:D16, which contains sales amounts.
*   _function_ - provided as SUM, the calculation to perform during aggregation.

With the inputs above, the GROUPBY function sums Sales by City and outputs the table in F4:G8 in one step. Notice that we _have not_ included the header row in _row\_fields_ or _values_, because we are not asking GROUPBY to generate a header automatically. Instead, we have manually entered a header row in F4:G4. Also note that GROUPBY includes a Total row by default. In the example below, we'll look at how to configure GROUPBY to output field headers in the source data.

### GROUPBY with field headers

The fourth argument in GROUPBY, _field\_headers_, controls how the header row is handled when it is part of the data provided to the GROUPBY function. There are five possible values for field\_headers:

| Value | Meaning |
| --- | --- |
| <none> | Automatic header detection (default). |
| 0   | Headers are not provided in the data. |
| 1   | Headers are included, but should not be displayed. |
| 2   | Headers are not included but should be generated. |
| 3   | Headers are included and should be displayed. |

The _field\_headers_ argument is optional. When _field\_headers_ is omitted, GROUPBY will automatically detect headers in the source data by testing values. If the first value is text and the second value is numeric, GROUPBY will assume the first row contains headers. You can see the automatic detection behavior in the example above, where the ranges used for _row\_fields_ and _values_ _do not_ include the header row. Because the first value is numeric (not text), GROUPBY assumes that headers are not part of the source data (which is correct). However, automatic detection only prevents the headers from being processed as values; it does not display headers. To display field headers in source data, you must specifically enable them by setting _field\_headers_ to 3. You can see how this works in the example below, where the ranges provided for _row\_fields_ and _values_ include a header row, and _field\_headers_ is provided as 3:

    =GROUPBY(B4:B16,D4:D16,SUM,3) // field headers enabled

![GROUPBY function with field headers enabled](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_field_headers_enabled.png "GROUPBY function with field headers enabled")

The inputs to GROUPBY are as follows:

*   _row\_fields_ - provided as the range B4:B16, which contains city names, plus the header row.
*   _values_ - provided as the range D4:D16, which contains sales amounts, plus the header row.
*   _function_ - provided as SUM, the calculation to perform during aggregation.
*   _field\_headers_ - provided as 3, since the data now includes a header row that should be displayed.

Note that the data in this example is the same as the previous example. However, the ranges used for row fields and values now include the headers in row 4. As a result, the formula is entered in cell F4 instead of F5 to keep the output table in the same location.

### GROUPBY calculation options

The third argument in GROUPBY is _function,_ which specifies the calculation to perform when values are grouped. Available calculations include Excel functions like SUM, COUNT, COUNTA, MAX, MIN, etc. The function is called with [eta lambda](https://exceljet.net/glossary/eta-lambda)
 syntax, which is just the function name, without parentheses and arguments. In the worksheet below, we have a list of meal preferences for 100 employees in different departments and the cost per meal. We can use the GROUPBY function to analyze this data in a variety of ways. In the first example below, we use GROUPBY to generate a count for each meal (Beef, Chicken, and Veggie). In this case, we want to count the meals, which are text values, so we provide COUNTA for _function_. The formula in G5 looks like this:

    =GROUPBY(D4:D104,D4:D104,COUNTA,1)

![GROUPBY function calculation count by meal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_calculation_count_by_meal.png "GROUPBY function calculation count by meal")

*   _row\_fields_ - D4:D104 (Meal), because we want to group by meal.
*   _values_ - D4:D104 (Meal) because we want to count meals.
*   _function_ - COUNTA, because we want to count text values.
*   _field\_headers_ - 1, because the data contains a header row we don't want to display.

_Note: Field headers are included in the source data ranges, but we don't want to display field headers because we want to use the word "Count" for the counted meals in cell H4. As a result, we provide 1 for field\_headers._

In the next example, we've changed the calculation to generate a total cost by meal, as seen below. The formula in G5 now looks like this:

    =GROUPBY(D4:D104,E4:E104,SUM,1)

![GROUPBY function calculation sum by meal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_calculation_sum_by_meal.png "GROUPBY function calculation sum by meal")

*   _row\_fields_ - D4:D104 (Meal), because we want to group by meal.
*   _values_ - E4:E104 (Cost) because we want to sum cost.
*   _function_ - SUM, because we want to provide a total.
*   _field\_headers_ - 1, because the data contains a header row we don't want to display.

_Note: Here again, we don't want to display field headers because we want to use the word "Total" in H4, so we provide 1 for field\_headers._

### GROUPBY with multiple calculations

It is possible to perform more than one calculation with GROUPBY, but it is not obvious how to do so, since the _function_ argument accepts just one value. The trick is to use the [HSTACK function](https://exceljet.net/functions/hstack-function)
 inside GROUPBY to call more than one function simultaneously. For example, in the worksheet below, we are using GROUPBY to count by meal and sum by meal at the same time. The formula in G4 looks like this:

    =GROUPBY(D4:D104,E4:E104,HSTACK(COUNT,SUM),1)

![GROUPBY function calculation count and sum by meal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_calculation_count_and_sum_by_meal.png "GROUPBY function calculation count and sum by meal")

*   _row\_fields_ - D4:D104 (Meal), because we want to group by meal.
*   _values_ - E4:E104 (Cost), because we want to sum the cost.
*   _function_ - HSTACK(COUNT,SUM), because we want to count and sum.
*   _field\_headers_ - 1, because the data contains a header row we don't want to display.

Notice that the formula is now entered in cell G4, even though we have set _field\_headers_ to 1 (do not display). This is because GROUPBY automatically adds column headers when you ask for multiple calculations. As a result, we have COUNT in H4 and SUM in I4. Cell G4 is blank because we have disabled field headers. To perform another calculation, just add the function name to the values inside HSTACK. In the example below, we have added the [PERCENTOF function](https://exceljet.net/functions/percentof-function)
 to HSTACK, and the formula in G4 is now:

    =GROUPBY(D4:D104,E4:E104,HSTACK(COUNT,SUM,PERCENTOF),1)

![GROUPBY function calculation count, sum, and percent by meal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_calculation_count_sum_and_percentof_by_meal.png "GROUPBY function calculation count, sum, and percent by meal")

Note that the formatting in the table seen above has been applied manually. Also, note that the structure of the table is not ideal. The first column lacks a header, and the function names used for calculations are a bit clunky. See below for a workaround.

> When adding the PERCENTOF function as a _function_ inside GROUPBY, you must take care that you are providing numeric _values_. If the values are text, PERCENTOF will return #DIV/0!. For a detailed explanation, see: [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)
> .

### GROUPBY with custom headers

When you add multiple calculations to the GROUPBY function, you automatically get headers on the calculated columns. Depending on your use case, you may want to override these headers and supply your own custom values. To do that, you can remove the headers with the [DROP function](https://exceljet.net/functions/drop-function)
 and add your own with the [VSTACK function](https://exceljet.net/functions/vstack-function)
. You can see an example of this in the example below, which performs three calculations: COUNT, SUM, PERCENTOF. The formula in cell G4 looks like this:

    =VSTACK(
    {"Meal","Count","Cost","%"},
    DROP(GROUPBY(D4:D104,E4:E104,HSTACK(COUNT,SUM,PERCENTOF),1),1)
    )

![GROUPBY function with custom headers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_custom_headers.png "GROUPBY function with custom headers")

*   Inside the DROP function, we have the original GROUPBY formula.
*   DROP removes the header row and passes the result into VSTACK.
*   VSTACK stacks the custom headers on top of the remaining table.

Note that the headers in G4:J4 come from custom values supplied as an [array constant](https://exceljet.net/glossary/array-constant)
 like `{"Meal","Count","Cost","%"}`. You are free to customize these values as you like.

> In this example, we did extra work in order to get an all-in-one formula that returned both headers and data at the same time. However, a hybrid approach would be to enter the header row manually and then use DROP + GROUPBY alone to return just the table data without headers.

### GROUPBY with multiple columns

The GROUPBY function can handle multiple columns for _row\_fields_ and _values_ arguments. When you include multiple columns, the output will have multiple row group levels. To illustrate how this works, consider the examples below. In the first example, we provide one column for _row\_fields_, and 1 column for values. The formula in G4 looks like this:

    =GROUPBY(C4:C226,E4:E226,SUM,3)

![GROUPBY function with single columns for row fields and values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_multiple_columns1.png "GROUPBY function with single columns for row fields and values")

The inputs to GROUPBY are as follows:

*   _row\_fields_ - Color (C4:C226), including the header row.
*   _values_ - Sales (E4:E226), including the header row.
*   _function_ - SUM to generate a total for each color.
*   _field\_headers_ - 3, since the source data includes a header row that should be displayed.

With this configuration, GROUPBY groups Sales by Color and generates a total for Red, Green, Blue, and Silver as shown above. In the example below, we've modified the formula to include Region and Color for _row\_fields_:

    =GROUPBY(B4:C226,E4:E226,SUM,3)

![GROUPBY function with two columns for row fields](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_multiple_columns2.png "GROUPBY function with two columns for row fields")

*   _row\_fields_ - Region and Color (B4:C226), including the header row.
*   _values_ - Sales (E4:E226), including the header row.
*   _function_ - SUM to generate a total for each region/color.
*   _field\_headers_ - 3, since the source data includes a header row that _should_ be displayed.

The result is that GROUPBY groups Sales by Region and Color, and returns total Sales for each combination. _Values_ can also be supplied as a range with more than one column. In the example below, row fields and values are provided as ranges that include two columns. The formula in G4 is:

    =GROUPBY(B4:C226,D4:E226,SUM,3)

![GROUPBY function with two columns for row fields and two columns for values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_multiple_columns3.png "GROUPBY function with two columns for row fields and two columns for values")

*   _row\_fields_ - Region and Color (B4:C226), including the header row.
*   _values_ - Units and Sales (D4:E226), including the header row.
*   _function_ - SUM to generate totals for each region/color.
*   _field\_headers_ - 3, since the source data includes a header row that should be displayed.

Here, we modified the Values range to include both Units and Sales. In this configuration, the GROUPBY function generates two totals for each Region/Color combination: a total for Units and a total for Sales. 

### GROUPBY total options

The fifth argument in GROUPBY, _total\_depth_, controls how the totals are displayed in the output. _Total\_depth_ is an optional argument. When not provided, GROUPBY will automatically display grand totals. The table below shows possible settings for _total\_depth:_

| Value | Meaning |
| --- | --- |
| <none> | Automatic grand totals (default). |
| 0   | Do not display totals. |
| 1   | Display Grand Totals. |
| 2   | Display Grand Totals and Subtotals. |
| \-1 | Display Grand Totals at top. |
| \-2 | Display Grand Totals and Subtotals at top. |

By default, GROUPBY will create and display grand totals when _total\_depth_ argument is not provided. You can see how this works below, where the formula in cell G4 looks like this:

    =GROUPBY(B4:C226,E4:E226,SUM,3) // total depth not provided

![GROUPBY function displays Grand Totals by default](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_total_depth_default.png "GROUPBY function displays Grand Totals by default")

*   _row\_fields_ - Region and Color (B4:C226), including the header row.
*   _values_ - Sales (E4:E226), including the header row.
*   _function_ - SUM to generate totals for Sales
*   _field\_headers_ - 3, since the source data includes a header row that should be displayed.
*   _total\_depth_ - not provided.

Note that the total in cell I13 is displayed by default. If we explicitly enable grand totals by setting _total\_depth_ to 1, we get the same result:

    =GROUPBY(B4:C226,E4:E226,SUM,3,1) // total depth = 1

![GROUPBY function with total depth set to 1](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_total_depth_set_to_1.png "GROUPBY function with total depth set to 1")

*   _row\_fields_ - Region and Color (B4:C226), including the header row.
*   _values_ - Sales (E4:E226), including the header row.
*   _function_ - SUM to generate totals for Sales
*   _field\_headers_ - 3, since the source data includes a header row that should be displayed.
*   _total\_depth_ - 1, to explicitly enable a grand total.

Setting _total\_depth_ to 2 enables both grand totals and subtotals, as shown in the example below:

    =GROUPBY(B4:C226,E4:E226,SUM,3,2) // total depth = 2

![GROUPBY function with total depth set to 2](https://exceljet.net/sites/default/files/images/functions/inline/groupby_function_with_total_depth_set_to_2.png "GROUPBY function with total depth set to 2")

*   _row\_fields_ - Region and Color (B4:C226), including the header row.
*   _values_ - Sales (E4:E226), including the header row.
*   _function_ - SUM to generate totals for Sales
*   _field\_headers_ - 3, since the source data includes a header row that should be displayed.
*   _total\_depth_ - 2, to enable subtotals and grand totals.

Now we have subtotals for Region in cells I9 and I14, and a grand total in cell I15.

> For subtotals to display, _row\_fields_ must have at least 2 columns. If you try to enable subtotals when _row\_fields_ contains just one column, GROUPBY will return a #VALUE! error. It is possible to provide numbers greater than 2 for _total\_depth_ as long as _row\_fields_ has enough columns to support the requested total depth.

The GROUPBY function also supports displaying grand totals and subtotals at the top of a group instead of at the bottom. The example below moves grand totals to the top by setting _total\_depth_ to -1:

    =GROUPBY(B4:C226,E4:E226,SUM,3,-1) // total depth = -1

![GROUPBY function with total depth set to -1](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_total_depth_set_to_-1.png "GROUPBY function with total depth set to -1")

Likewise, subtotals can also be displayed at the top of a group by setting _total\_depth_ to -2:

    =GROUPBY(B4:C226,E4:E226,SUM,3,-2) // total depth = -2

![GROUPBY function with total depth set to -2](https://exceljet.net/sites/default/files/images/functions/inline/groupby_function_with_total_depth_set_to_-2.png "GROUPBY function with total depth set to -2")

### GROUPBY Sort options

By default, the GROUPBY function will sort values in standard ascending (A-Z) order, beginning with the leftmost row field. You can see this behavior in the example below, where no sort order has been specified and the table returned by GROUPBY is sorted A-Z by city name. The formula in cell F4 looks like this:

    =GROUPBY(B4:B16,D4:D16,SUM,3) // no sort order specified

![GROUPBY function with no sort order provided sorts A-Z by default ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_sort_order_default.png "GROUPBY function with no sort order provided sorts A-Z by default ")

To override the default sort order, provide a value for the _sort\_order_ argument, which is given as an index number that can be positive (A-Z) or negative (Z-A). The number itself corresponds to the columns in the table, starting with 1 for the first column. For example, to sort the table by city name in descending (Z-A) order, use -1:

    =GROUPBY(B4:B16,D4:D16,SUM,3,,-1) // sort city names Z-A

![GROUPBY function with sort order set to -1 sorts city names Z-A](https://exceljet.net/sites/default/files/images/functions/inline/groupby_function_with_sort_order_set_to_-1.png "GROUPBY function with sort order set to -1 sorts city names Z-A")

To sort the table by Sales in ascending order, provide a 2 for _sort\_order_, where 2 means the second column:

    =GROUPBY(B4:B16,D4:D16,SUM,3,,2)

![GROUPBY function with sort order set to 2 sorts by Sales ascending](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_sort_order_set_to_2.png "GROUPBY function with sort order set to 2 sorts by Sales ascending")

To sort the table by Sales in descending order, provide a -2 for _sort\_order_, where the 2 means the second column and the negative sign (-) specifies a descending (Z-A) sort:

    =GROUPBY(B4:B16,D4:D16,SUM,3,,-2)

![GROUPBY function with sort order set to -2 sorts by Sales descending](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_sort_order_set_to_-2.png "GROUPBY function with sort order set to -2 sorts by Sales descending")

### GROUPBY with filter array

One of the interesting options available for the GROUPBY function is the ability to filter incoming data to include or exclude specific values. The optional _filter\_array_ argument controls this feature. When provided, _filter\_array_ is expected to be a single column of Booleans (i.e., TRUE and FALSE, or 1s and 0s) that indicate whether the corresponding row in the data should be included. These Booleans are typically generated with a logical expression. For example, in the workbook below, the data has been filtered to allow only rows corresponding to the West Region by providing the logical expression B4:B226="West" for _filter\_array_. The formula in G4 looks like this:

    =GROUPBY(B4:C226,D4:E226,SUM,3,,,B4:B226="West")

![GROUPBY function with filter array to include Region = West](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_filter_array_region_equals_west.png "GROUPBY function with filter array to include Region = West")

Note that _filter\_array_ should be the same length as the incoming data. In the example above, we match B4:B226 to the ranges used for row and value fields. The logic can be easily modified. To exclude all rows where the color is "Red", we can use a formula like this:

    =GROUPBY(B4:C226,D4:E226,SUM,3,,,C4:C226<>"Red")

![GROUPBY function with filter array to exclude Red color](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_filter_array_color_is_not_red.png "GROUPBY function with filter array to exclude Red color")

The logic for _filter\_array_ can be any expression that generates a correctly sized array of Booleans, and there are many ways to do this with Excel formulas and functions. We could, for example, use the REGEXTEST function to include rows where the color is "Red" or "Blue" in a formula like this:

    =GROUPBY(B4:C226,D4:E226,SUM,3,,,REGEXTEST(C4:C226,"Red|Blue"))

![GROUPBY function with filter array to include Red or Blue](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_with_filter_array_color_is_red_or_blue.png "GROUPBY function with filter array to include Red or Blue")

> Regex is a newer feature in Excel. For a general introduction, see [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
> .

### GROUPBY and field relationships

The _field\_relationship_ argument specifies the "relationship" between fields when multiple columns are provided as row fields. There are two possible values: 0 = Hierarchy and 1 = Table. The default value is 0 (Hierarchy). Field relationship affects the way sorting works, but only when _row\_fields_ includes _multiple_ columns. By default, GROUPBY uses a _hierarchical relationship_ between row fields, which means that row fields sort from left to right. In other words, the sorting of additional row fields is controlled by the hierarchy of previous columns. When _field\_relationship_ is set to 1, the sorting of each field column works independently. 

In the example below, we use the _field\_relationship_ argument (set to 1) to disable the hierarchy and allow the months to sort correctly using the month numbers created by the [MONTH function](https://exceljet.net/functions/month-function)
. The formula in G5 looks like this:

    =CHOOSECOLS(GROUPBY(HSTACK(TEXT(data[Date],"mmm"),MONTH(data[Date])),data[Total],SUM,,,2,,1),{1,3})

[![Field relationship set to 1 to allow months to sort by month number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_field_relationship_example.png "Field relationship set to 1 to allow months to sort by month number")](https://exceljet.net/formulas/groupby-with-monthly-totals)

For a full tear-down of this formula and a detailed explanation of why the field relationship setting is required, [see this page](https://exceljet.net/formulas/groupby-with-monthly-totals)
.

> Note that when the field relationship is set to Table, subtotals are not supported because they rely on a hierarchy to work correctly.

### GROUPBY with custom LAMBDA

The calculation performed by the GROUPBY function can be called in two different ways: (1) a short-form "[eta lambda syntax](https://exceljet.net/glossary/eta-lambda)
" or (2) a long-form syntax that uses a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
. For example, to group and sum values, the short-form syntax looks like this:

    =GROUPBY(row_fields,values,SUM)
    

The long-form custom syntax for the same calculation looks like this:

    =GROUPBY(row_fields,LAMBDA(x,SUM(x)))
    

Both formulas above will return the same result. Why two syntax options? The short form is for convenience. It is concise and easy to read. However, the behavior cannot be customized. The long-form syntax uses the LAMBDA function and can be customized as needed to apply a more advanced calculation. To illustrate this concept, suppose you want the round values that GROUPBY returns to the nearest 1000. We can use the [ROUND function](https://exceljet.net/functions/round-function)
 to round to the nearest 1000 like this:

    =ROUND(number,-3)

But how do we get this into the GROUPBY function, which needs to sum the values before rounding them? The trick is to switch to the long-form LAMBDA syntax and use a calculation like this:

     LAMBDA(x,ROUND(SUM(x),-3))

The core of this calculation is the long-form syntax `LAMBDA(x,SUM(x),` plus the ROUND function. The grouped values are passed into SUM, which returns the sum of a given group directly to ROUND, which rounds the number to the nearest 1000. The GROUPBY function then returns the rounded sum in the final output. You can see an example of this formula in action in the worksheet below, where the formula in cell F4 looks like this:

    =GROUPBY(B4:B16,D4:D16,LAMBDA(x,ROUND(SUM(x),-3)),3)

![GROUPBY function with custom lambda to round results to nearest 1000](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/groupby_function_custom_lambda_to_round_results.png "GROUPBY function with custom lambda to round results to nearest 1000")

> The ROUND example above is just for illustration. Because GROUPBY supports a custom LAMBDA function, you can perform any calculation that makes sense in the context of the GROUPBY function. See another example [here](https://exceljet.net/formulas/look-up-and-return-to-single-cell)
> .

### GROUPBY with a dynamic range

When you use the GROUPBY function with data that changes frequently, you will probably want to configure it to use a dynamic range. A dynamic range is a range that expands and contracts as rows are added or removed. You have two good options to make the range: converting the data to an [Excel Table](https://exceljet.net/articles/excel-tables)
, or using the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
 to create a dynamic named range. In both cases, you will then need to feed specific columns of the range into GROUPBY. With Excel Tables, this is easy, since you can refer to table columns by name. With a [named range](https://exceljet.net/glossary/named-range)
, you can use the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 to access specific columns and, if desired, you could give those columns names by wrapping the formula in the [LET function](https://exceljet.net/functions/let-function)
, then feeding the column names into GROUPBY. 

GROUPBY function examples
-------------------------

[![Excel formula: GROUPBY with survey results](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/groupby_with_survey_results.png "Excel formula: GROUPBY with survey results")](https://exceljet.net/formulas/groupby-with-survey-results)

### [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)

In May 2025, I ran a survey asking Exceljet newsletter subscribers what version of Excel they use most. This is an important question for Excel learning because the new dynamic array engine has completely changed how many formulas are written. These changes started rolling out after Excel 2019, so...

[![Excel formula: Sum if with multiple ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum_if_with_multiple_ranges.png "Excel formula: Sum if with multiple ranges")](https://exceljet.net/formulas/sum-if-with-multiple-ranges)

### [Sum if with multiple ranges](https://exceljet.net/formulas/sum-if-with-multiple-ranges)

In this example, the goal is to calculate a total quantity for each color across the two ranges shown in the worksheet. The two ranges are "non-contiguous", which means they are not connected or touching. Both ranges contain a list of colors in the first column and quantities in the second column...

[![Excel formula: Sum if multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_columns.png "Excel formula: Sum if multiple columns")](https://exceljet.net/formulas/sum-if-multiple-columns)

### [Sum if multiple columns](https://exceljet.net/formulas/sum-if-multiple-columns)

In this example, the goal is to calculate a sum for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. In other words, we want to perform a "sum if" with a data range that contains three columns. For convenience only, data (C5:E16) and group (B5:B16) are named...

[![Excel formula: Look up and return to single cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_and_return_to_single_cell.png "Excel formula: Look up and return to single cell")](https://exceljet.net/formulas/look-up-and-return-to-single-cell)

### [Look up and return to single cell](https://exceljet.net/formulas/look-up-and-return-to-single-cell)

In this example, the goal is to look up and retrieve all names for a given team and return them in a single cell as a comma‑separated list. At the core, this is a lookup problem, but the twist is that we want to return multiple matches for each team, not just one. That means traditional lookup...

[![Excel formula: GROUPBY with monthly totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/groupby_with_monthly_totals.png "Excel formula: GROUPBY with monthly totals")](https://exceljet.net/formulas/groupby-with-monthly-totals)

### [GROUPBY with monthly totals](https://exceljet.net/formulas/groupby-with-monthly-totals)

In this example, the goal is to generate monthly totals using the GROUPBY function. This is a tricky problem in Excel because typically, source data contains a regular date field and not a separate field with month names. In addition, the GROUPBY function will, by default, sort everything in...

Related functions
-----------------

[![Excel PIVOTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_pivotby_function.png "Excel PIVOTBY function")](https://exceljet.net/functions/pivotby-function)

### [PIVOTBY Function](https://exceljet.net/functions/pivotby-function)

The Excel PIVOTBY function is designed to summarize data by grouping rows and columns. The result is a dynamic summary table created with a single formula.

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

[![Excel PERCENTOF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_percentof_function.png "Excel PERCENTOF function")](https://exceljet.net/functions/percentof-function)

### [PERCENTOF Function](https://exceljet.net/functions/percentof-function)

The Excel PERCENTOF function is designed to calculate the percentage of a subset of data with respect to all data. The output from PERCENTOF is a decimal number that can be formatted with Excel's percentage number format....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if multiple columns](https://exceljet.net/formulas/sum-if-multiple-columns)
    
*   [Look up and return to single cell](https://exceljet.net/formulas/look-up-and-return-to-single-cell)
    
*   [GROUPBY with monthly totals](https://exceljet.net/formulas/groupby-with-monthly-totals)
    
*   [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)
    
*   [Sum if with multiple ranges](https://exceljet.net/formulas/sum-if-with-multiple-ranges)
    

### Functions

*   [PIVOTBY Function](https://exceljet.net/functions/pivotby-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [PERCENTOF Function](https://exceljet.net/functions/percentof-function)
    

### Links

*   [Microsoft GROUPBY function documentation](https://support.microsoft.com/en-us/office/groupby-function-5e08ae8c-6800-4b72-b623-c41773611505)
    

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
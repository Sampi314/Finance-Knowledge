# Excel SORT function | Exceljet

**Source:** https://exceljet.net/functions/sort-function

---

[Skip to main content](https://exceljet.net/functions/sort-function#main-content)

[](https://exceljet.net/functions/sort-function#)

*   [Previous](https://exceljet.net/functions/sequence-function)
    
*   [Next](https://exceljet.net/functions/sortby-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

SORT Function
=============

by Dave Bruns · Updated 12 Feb 2026

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9526/download?token=gJcjQGbt)
 (43.37 KB)

![Excel SORT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")

Summary
-------

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

Purpose 
--------

Sorts range or array

Return value 
-------------

Sorted array

Syntax
------

    =SORT(array,[sort_index],[sort_order],[by_col])

*   _array_ - Range or array to sort.
*   _sort\_index_ - \[optional\] Column index to use for sorting. Default is 1.
*   _sort\_order_ - \[optional\] 1 = Ascending, -1 = Descending. Default is ascending order.
*   _by\_col_ - \[optional\] TRUE = sort by column. FALSE = sort by row. Default is FALSE.

Using the SORT function 
------------------------

The SORT function sorts the contents of a [range](https://exceljet.net/glossary/range)
 or [array](https://exceljet.net/glossary/array)
 in ascending or descending order. The result is a dynamic array of values that will "[spill](https://exceljet.net/glossary/spill)
" onto the worksheet. If values in the source data change, the result from SORT updates automatically. Note that the SORT function cannot sort data _in place_ like Excel's Sort command on the Ribbon. SORT always outputs results to a new location.

By default, SORT sorts values in ascending order using the first column in _array_. Use _sort\_index_ to specify which column (or row) to sort by, and _sort\_order_ to control direction: 1 for ascending, -1 for descending. To sort horizontally by columns instead of rows, set _by\_col_ to TRUE.

SORT only accepts a single value for _sort\_index_, but you can sort by multiple columns at once using [array constants](https://exceljet.net/glossary/array-constant)
. For example, `{1,2}` sorts by column 1, then column 2. See the [multi-level sort example](https://exceljet.net/functions/sort-function#multi-level-sort)
 below. SORT can only sort alphabetically in A-Z or Z-A order. To sort in a custom order (e.g., "High, Medium, Low"), use the [SORTBY function](https://exceljet.net/functions/sortby-function)
 instead.

Note that SORT won't automatically adjust the source range if data is added or deleted. To configure SORT with a range that automatically adjusts to fit the data, use an [Excel Table](https://exceljet.net/articles/excel-tables)
 or a dynamic range created with [TRIMRANGE](https://exceljet.net/functions/trimrange-function)
 or the [dot operator](https://exceljet.net/glossary/dot-operator)
.

> Video: [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)

### Key features

*   Returns a dynamic array that spills automatically
*   Sorts rows (default) or columns (set _by\_col_ to TRUE)
*   Ascending order by default; use -1 for descending
*   Handles text, numbers, and dates
*   Supports multi-level sorting with array constants
*   Works with Excel Tables and structured references

### Table of contents

*   [Basic usage](https://exceljet.net/functions/sort-function#basic-usage)
    
*   [Simple A-Z sort](https://exceljet.net/functions/sort-function#simple-a-z-sort)
    
*   [Sort by specific column](https://exceljet.net/functions/sort-function#sort-by-specific-column)
    
*   [Sort data horizontally](https://exceljet.net/functions/sort-function#sort-data-horizontally)
    
*   [Filter on top n values](https://exceljet.net/functions/sort-function#filter-on-top-n-values)
    
*   [Unique rows](https://exceljet.net/functions/sort-function#unique-rows)
    
*   [Multi-level sort](https://exceljet.net/functions/sort-function#multi-level-sort)
    
*   [Reverse sort with checkbox](https://exceljet.net/functions/sort-function#reverse-sort-with-checkbox)
    
*   [Dates in chronological order](https://exceljet.net/functions/sort-function#dates-in-chronological-order)
    
*   [Notes](https://exceljet.net/functions/sort-function#notes)
    

### Basic usage

To sort in ascending or descending order:

    =SORT(A1:A10) // sort A-Z (ascending)
    =SORT(A1:A10,,-1) // Z-A (descending)
    

To sort by a specific column:

    =SORT(A1:B10) // sort by column 1, ascending
    =SORT(A1:B10,2) // sort by column 2, ascending
    =SORT(A1:B10,2,-1) // sort by column 2, descending
    

### Simple A-Z sort

In its simplest form, the SORT function sorts a single column of data in ascending order. In the worksheet below, the goal is to sort names in column B alphabetically. The formula in D5 is:

    =SORT(B5:B16)
    

![SORT function example - simple A-Z sort](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_simple_az.png "SORT function example - simple A-Z sort")

With no optional arguments, SORT returns all values in ascending (A-Z) order. The result spills into D5:D16.

### Sort by specific column

When data has multiple columns, use _sort\_index_ to specify which column to sort by. In the worksheet below, the goal is to sort names and scores by score in descending order (highest first). The formula in E5 is:

    =SORT(B5:C16,2,-1)
    

![SORT function example - sort by specific column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_by_specific_column.png "SORT function example - sort by specific column")

The _sort\_index_ of 2 tells SORT to use the second column (Score) for sorting. The _sort\_order_ of -1 sorts in descending order. The entire range is returned, sorted by score from highest to lowest. When _sort\_order_ is omitted, it defaults to 1 (ascending order).

For more details, see [Sort by one column](https://exceljet.net/formulas/sort-by-one-column)
.

### Sort data horizontally

The SORT function has the ability to sort data vertically (by row) or horizontally (by column). To sort data horizontally, set _by\_col_ to TRUE. In the worksheet below, names appear in row 4 and scores in row 5. The goal is to sort by score in descending order. The formula in B8 is:

    =SORT(B4:K5,2,-1,TRUE)
    

![SORT function example - sort data horizontally](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_horizontal.png "SORT function example - sort data horizontally")

With _by\_col_ set to TRUE, the _sort\_index_ of 2 refers to row 2 of the array (the scores in row 5). The result is returned horizontally, with names and scores rearranged from highest to lowest score.

For more details, see [Sort values by columns](https://exceljet.net/formulas/sort-values-by-columns)
.

### Filter on top n values

The SORT function pairs well with [FILTER](https://exceljet.net/functions/filter-function)
 to filter and sort data in one step. In the worksheet below, the goal is to extract the top n scores (where n is a variable in cell F2), sorted from highest to lowest. The formula in E5 is:

    =SORT(FILTER(B5:C16,C5:C16>=LARGE(C5:C16,F2)),2,-1)
    

![SORT function example - filter and sort top n values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_filter_top_n.png "SORT function example - filter and sort top n values")

The [LARGE function](https://exceljet.net/functions/large-function)
 returns the nth largest score (where n comes from F2). FILTER returns all rows where the score is greater than or equal to this value. SORT then sorts the results by column 2 (Score) in descending order. Changing the value in F2 instantly updates the results.

For more details, see [Filter on top n values](https://exceljet.net/formulas/filter-on-top-n-values)
.

### Unique rows

The SORT function works well with [UNIQUE](https://exceljet.net/functions/unique-function)
 to extract and sort unique rows. In the worksheet below, the goal is to extract unique Group/Color combinations, sorted by Group. The formula in E5 is:

    =SORT(UNIQUE(B5:C16))
    

![SORT function example - extract and sort unique rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_unique_rows.png "SORT function example - extract and sort unique rows")

The UNIQUE function extracts unique rows from B5:C16. SORT then sorts these rows by the first column (Group) in ascending order. The result spills into the output range automatically.

For more details, see [Unique rows](https://exceljet.net/formulas/unique-rows)
.

### Multi-level sort

The SORT function can sort by multiple columns using [array constants](https://exceljet.net/glossary/array-constant)
 for _sort\_index_ and _sort\_order_. In the worksheet below, the goal is to sort first by Group (ascending), then by Score (descending). The formula in F5 is:

    =SORT(B5:D16,{2,3},{1,-1})
    

![SORT function example - multi-level sort](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_multi_level.png "SORT function example - multi-level sort")

The array constant `{2,3}` tells SORT to sort first by column 2 (Group), then by column 3 (Score). The array constant `{1,-1}` specifies ascending order for Group and descending order for Score. Items in Group "A" appear first, sorted by Score from highest to lowest.

> For more flexible multi-level sorting, consider the [SORTBY function](https://exceljet.net/functions/sortby-function)
> , which lets you sort by columns that aren't part of the source data.

### Reverse sort with checkbox

You can use a [checkbox](https://exceljet.net/articles/native-checkboxes-in-excel)
 (or any TRUE/FALSE value) to toggle between ascending and descending sort order. In this example, movie titles are sorted from oldest to newest by default using the release year in the second column. Cell F2 contains a checkbox labeled "Reverse sort". The formula in E5 is:

    =SORT(B5:C16,2,1-2*F2)
    

![SORT function example - reverse sort with checkbox (unchecked)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_checkbox_unchecked.png "SORT function example - reverse sort with checkbox (unchecked)")

In Excel, a checkbox returns a TRUE/FALSE value. When the checkbox is _unchecked_, the value is FALSE. When the checkbox is _checked_, the value is TRUE. The expression `1-2*F2` is a simple trick to convert TRUE/FALSE to the sort order values SORT expects:

*   When F2 is FALSE (unchecked): `1-2*0 = 1` (ascending)
*   When F2 is TRUE (checked): `1-2*1 = -1` (descending)

Clicking the checkbox instantly reverses the sort order:

![SORT function example - reverse sort with checkbox (checked)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_checkbox_checked.png "SORT function example - reverse sort with checkbox (checked)")

### Dates in chronological order

The SORT function can be used to validate whether data is sorted correctly. For example, in the worksheet below, each row contains project milestone dates: Start, Ship, Install, Inspect, and Complete. The goal is to verify that all dates in a row are in the correct sequence. The formula in H5 is:

    =IF(SUM(--(B5:F5<>SORT(B5:F5,1,1,1)))=0,"✓","")
    

![SORT function example - verify that dates are in chronological order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sort_example_dates_chronological.png "SORT function example - verify that dates are in chronological order")

The formula compares each date in B5:F5 to the same dates after sorting horizontally with SORT (the final argument of 1 sets _by\_col_ to TRUE for horizontal sorting). The [double-negative](https://exceljet.net/glossary/double-unary)
 (--) converts the TRUE/FALSE values to 1/0, and the [SUM function](https://exceljet.net/functions/sum-function)
 counts how many dates are different after sorting. If the count is zero, all dates are listed chronologically and a check mark (✓) is returned.

For more details, see [All dates in chronological order](https://exceljet.net/formulas/all-dates-in-chronological-order)
.

### Notes

*   SORT returns a #VALUE! error if _sort\_index_ is out of range.
*   SORT returns a #SPILL! error if the spill range is not empty.
*   SORT returns a #REF! error when referencing a closed workbook (dynamic arrays require open workbooks).
*   SORT is a "stable sort"—items with the same sort value maintain their original relative order.
*   Do not include headers in the _array_ argument; SORT treats all rows as data.
*   SORT works with [Excel Tables](https://exceljet.net/articles/excel-tables)
     and structured references. Results update automatically when table data changes.
*   Use the [SORTBY](https://exceljet.net/functions/sortby-function)
     function to sort data by values that are not part of the data being sorted.

SORT function examples
----------------------

[![Excel formula: FILTER on top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values.png "Excel formula: FILTER on top n values")](https://exceljet.net/formulas/filter-on-top-n-values)

### [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE function. The LARGE function is a simple way to get the nth largest value in a range. Simply provide a range for the first argument ( array ), and a value for n as the second argument ( k ): =...

[![Excel formula: Dynamic summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20summary%20count.png "Excel formula: Dynamic summary count")](https://exceljet.net/formulas/dynamic-summary-count)

### [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)

In this example, the goal is to build a simple summary count table with a formula. Once created, the summary table should automatically update to show new values and counts when data changes. The article below walks through several options, from simple to very advanced. The more advanced options...

[![Excel formula: Filter on dates expiring soon](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20on%20dates%20expiring%20soon.png "Excel formula: Filter on dates expiring soon")](https://exceljet.net/formulas/filter-on-dates-expiring-soon)

### [Filter on dates expiring soon](https://exceljet.net/formulas/filter-on-dates-expiring-soon)

In this example, the goal is to filter data to show rows where dates have expired or will be expiring soon. In the table to the left, we have equipment that needs to be replaced every x months, where x appears in the "Months" column. The "Replaced" column shows the date equipment was replaced. The...

[![Excel formula: Filter and sort without errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_and_sort_without_errors.png "Excel formula: Filter and sort without errors")](https://exceljet.net/formulas/filter-and-sort-without-errors)

### [Filter and sort without errors](https://exceljet.net/formulas/filter-and-sort-without-errors)

A common situation in Excel is to use the SORT function to sort results returned by the FILTER function . However, a formula based on the FILTER and SORT may return an error when no data is returned. In this example, the goal is to create a formula based on FILTER and SORT that will not return an...

[![Excel formula: Filter and exclude columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter_and_exclude_columns.png "Excel formula: Filter and exclude columns")](https://exceljet.net/formulas/filter-and-exclude-columns)

### [Filter and exclude columns](https://exceljet.net/formulas/filter-and-exclude-columns)

In this example, the goal is to use a single formula to extract high-value projects and list them in a simple table. We also want to remove unnecessary columns to create a clean, uncluttered view. The solutions explained below are based on a combination of several functions in Excel, including...

[![Excel formula: Sort comma separated values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort_comma_separated_values.png "Excel formula: Sort comma separated values")](https://exceljet.net/formulas/sort-comma-separated-values)

### [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)

In this example the goal is to sort the comma separated values in column B in alphabetical order. In the latest version of Excel, you can solve this problem with a formula based on TEXTSPLIT, SORT, and TEXTJOIN. In earlier versions of Excel the problem is more complicated. See below for a couple of...

[![Excel formula: Sort values by columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20values%20by%20columns.png "Excel formula: Sort values by columns")](https://exceljet.net/formulas/sort-values-by-columns)

### [Sort values by columns](https://exceljet.net/formulas/sort-values-by-columns)

The SORT function sorts a range using a given index, called sort\_index . Normally, this index represents a column in the source data. However, the SORT function has an optional argument called " by\_col " which allows sorting values organized in columns. To sort by column, this argument must be set...

[![Excel formula: Sort by one column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20one%20column_0.png "Excel formula: Sort by one column")](https://exceljet.net/formulas/sort-by-one-column)

### [Sort by one column](https://exceljet.net/formulas/sort-by-one-column)

The SORT function requires very little configuration. In the example shown, we want to sort data in B5:D14 by the third column, Group. For array , we provide entire range, B5:D14. For sort\_index , we provide 3: =SORT(B5:D14,3) With this formula in F5, the SORT function outputs the sorted array in...

[![Excel formula: 10 most common text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/10%20most%20common%20text%20values.png "Excel formula: 10 most common text values")](https://exceljet.net/formulas/10-most-common-text-values)

### [10 most common text values](https://exceljet.net/formulas/10-most-common-text-values)

In this example, the goal is to list the 10 most frequently occurring text values in a range, in descending order by count, as seen in the range in E5:F14. This is an advanced formula that requires a number of nested functions. However, it is an excellent example of the power of dynamic array...

[![Excel formula: Multiple matches into separate columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_columns.png "Excel formula: Multiple matches into separate columns")](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

### [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

In this example, the goal is to get all names in a given group into the same row, in separate columns, as seen in the worksheet. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns using common values, which in this case are the group...

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: Biggest gainers and losers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/biggest%20gainers%20and%20losers.png "Excel formula: Biggest gainers and losers")](https://exceljet.net/formulas/biggest-gainers-and-losers)

### [Biggest gainers and losers](https://exceljet.net/formulas/biggest-gainers-and-losers)

In this example, the goal is to display the biggest 3 gainers and losers in a set of data where Start and End columns contain values at two points in time, and Change contains the percentage change in the values. The data in B5:E16 is defined as an Excel Table with the name data . Two formulas are...

[![Excel formula: UNIQUE with non-adjacent columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20with%20non-adjacent%20columns.png "Excel formula: UNIQUE with non-adjacent columns")](https://exceljet.net/formulas/unique-with-non-adjacent-columns)

### [UNIQUE with non-adjacent columns](https://exceljet.net/formulas/unique-with-non-adjacent-columns)

Although FILTER is commonly used to filter rows, you can also filter columns. The trick is to use an include argument that operates on columns instead of rows. In this example, we use a hard-coded array constant to filter out unwanted columns, but you can also use a logical expression that returns...

[![Excel formula: Multiple matches into separate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_rows.png "Excel formula: Multiple matches into separate rows")](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

### [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

In this example, the goal is to get all names in a given group into separate rows grouped by column, as seen in the worksheet above. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns where each column holds the names that belong to a...

[![Excel formula: Filter by column, sort by row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20by%20column%20sort%20by%20row.png "Excel formula: Filter by column, sort by row")](https://exceljet.net/formulas/filter-by-column-sort-by-row)

### [Filter by column, sort by row](https://exceljet.net/formulas/filter-by-column-sort-by-row)

Note: FILTER is a new dynamic array function in Excel 365 . In other versions of Excel, there are alternatives , but they are more complex. In this example, the goal is to filter the data shown in B5:G15 by year, then sort the results in descending order. In addition, the result should include the...

SORT function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Filter%20with%20dynamic%20dropdown%20list-Play.png)](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)

### [Filter with dynamic dropdown list](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)

In this video, we'll build a dropdown list using dynamic arrays to filter data. Here we have data in an Excel Table called "data". In cell J2, I'll set up a dropdown list we can use to filter data by color. First, I'll type "Red" in J2, so we have something to filter on. Next, I'll enter the FILTER...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/SORT%20and%20SORTBY%20with%20multiple%20columns-Play_0.png)](https://exceljet.net/videos/sort-and-sortby-with-multiple-columns)

### [SORT and SORTBY with multiple columns](https://exceljet.net/videos/sort-and-sortby-with-multiple-columns)

In this video, we’ll look at how to sort by multiple columns with the SORT and SORTBY functions. In this worksheet, we have a list of names, projects, values, and regions. This data is not sorted. Our goal is to sort the data first by region, then by name, and finally by value, with larger values...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/New%20dynamic%20array%20functions%20in%20Excel-Play.png)](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

### [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

In this video, we'll quickly review new Dynamic Array functions in Excel. With the introduction of dynamic array formulas, Excel includes 6 brand new functions that directly leverage dynamic array behavior. Each of these functions is covered in more detail later in the course, so this is just a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20SORT%20function%20example-Play.png)](https://exceljet.net/videos/basic-sort-function-example)

### [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)

In this video, we’ll look at a basic example of sorting with the SORT function . Sorting with formulas is one of those traditionally hard problems in Excel that new dynamic array formulas have made much easier. In this worksheet, we have a list of names, scores, and groups. Currently the data is...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Nesting%20dynamic%20array%20formulas-Play.png)](https://exceljet.net/videos/nesting-dynamic-array-formulas)

### [Nesting dynamic array formulas](https://exceljet.net/videos/nesting-dynamic-array-formulas)

In this video, we'll look at how to nest dynamic array formulas together. One of the most powerful ways to extend the functionality of dynamic array formulas is to nest one function inside another. To illustrate, let's look at an example based on the SORT and FILTER functions. Here we have data...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Two-way%20summary%20with%20dynamic%20arrays-PLAY.png)](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)

### [Two-way summary with dynamic arrays](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)

In this video, we'll look at how to create a two-way summary table with dynamic array formulas that works like a pivot table. This worksheet contains several hundred rows of sample order data in an Excel Table called "data". I'll first build a pivot table to summarize this data by Color and Region...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20perform%20a%20random%20sort-Play_0.png)](https://exceljet.net/videos/how-to-perform-a-random-sort)

### [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)

In this video, we’ll look at how to perform a random sort with the SORTBY function , with help from the RANDARRAY function . In this worksheet, we have the first 10 letters in the alphabet in the range B5:B14. How can we sort this data in random order? One way to do this is to add a helper column...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)
    
*   [Filter and exclude columns](https://exceljet.net/formulas/filter-and-exclude-columns)
    
*   [Biggest gainers and losers](https://exceljet.net/formulas/biggest-gainers-and-losers)
    
*   [FILTER on top n values with criteria](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria)
    
*   [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)
    
*   [Unique rows](https://exceljet.net/formulas/unique-rows)
    
*   [Filter and sort without errors](https://exceljet.net/formulas/filter-and-sort-without-errors)
    
*   [All dates in chronological order](https://exceljet.net/formulas/all-dates-in-chronological-order)
    
*   [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)
    
*   [Extract common values from text strings](https://exceljet.net/formulas/extract-common-values-from-text-strings)
    

### Videos

*   [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)
    
*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
    
*   [Nesting dynamic array formulas](https://exceljet.net/videos/nesting-dynamic-array-formulas)
    
*   [SORT and SORTBY with multiple columns](https://exceljet.net/videos/sort-and-sortby-with-multiple-columns)
    
*   [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)
    
*   [Two-way summary with dynamic arrays](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)
    
*   [Filter with dynamic dropdown list](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

### Links

*   [Microsoft SORT function documentation](https://support.office.com/en-us/article/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c)
    

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
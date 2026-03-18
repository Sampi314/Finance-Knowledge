# Excel UNIQUE function | Exceljet

**Source:** https://exceljet.net/functions/unique-function

---

[Skip to main content](https://exceljet.net/functions/unique-function#main-content)

[](https://exceljet.net/functions/unique-function#)

*   [Previous](https://exceljet.net/functions/trimrange-function)
    
*   [Next](https://exceljet.net/functions/valuetotext-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

UNIQUE Function
===============

by Dave Bruns · Updated 29 Jan 2026

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SORT](https://exceljet.net/functions/sort-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9515/download?token=VvnXh64A)
 (48.61 KB)

![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")

Summary
-------

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

Purpose 
--------

Extract unique values from range

Return value 
-------------

Array of unique values

Syntax
------

    =UNIQUE(array,[by_col],[exactly_once])

*   _array_ - Range or array from which to extract unique values.
*   _by\_col_ - \[optional\] How to compare and extract. FALSE = by row (default); TRUE = by column.
*   _exactly\_once_ - \[optional\] TRUE = values that occur once, FALSE= all unique values (default).

Using the UNIQUE function 
--------------------------

The UNIQUE function extracts a list of unique values from a range or [array](https://exceljet.net/glossary/array)
. The result is a [dynamic array](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 that [spills](https://exceljet.net/glossary/spill)
 onto the worksheet, automatically updating when source data changes.

UNIQUE is often combined with other dynamic array functions like [FILTER](https://exceljet.net/functions/filter-function)
 and [SORT](https://exceljet.net/functions/sort-function)
. For example, you can filter data before extracting unique values, or sort the results alphabetically. Use the [ROWS function](https://exceljet.net/functions/rows-function)
 or [COUNTA function](https://exceljet.net/functions/counta-function)
 to count the unique values returned by UNIQUE.

Note that UNIQUE won't automatically adjust the source range if data is added or deleted. To use UNIQUE with a range that automatically resizes to fit the data, use an [Excel Table](https://exceljet.net/articles/excel-tables)
 or a dynamic range created with [TRIMRANGE](https://exceljet.net/functions/trimrange-function)
 or the [dot operator](https://exceljet.net/glossary/dot-operator)
.

> Video: [The UNIQUE function](https://exceljet.net/videos/the-unique-function)

### Key features

*   Extracts unique values from a range or array automatically.
*   Returns a dynamic array that updates when source data changes.
*   Case-insensitive: "APPLE", "Apple", and "apple" are treated as the same value.
*   Set _exactly\_once_ to TRUE to return only values that appear once (distinct values).
*   Set _by\_col_ to TRUE to extract unique values from horizontal data.
*   Only works with adjacent columns; use CHOOSECOLS or FILTER for non-adjacent columns.

### Table of contents

*   [Basic usage](https://exceljet.net/functions/unique-function#basic-usage)
    
*   [Unique values](https://exceljet.net/functions/unique-function#unique-values)
    
*   [Unique values by column](https://exceljet.net/functions/unique-function#unique-values-by-column)
    
*   [Sort unique values](https://exceljet.net/functions/unique-function#sort-unique-values)
    
*   [Unique rows](https://exceljet.net/functions/unique-function#unique-rows)
    
*   [Distinct values](https://exceljet.net/functions/unique-function#distinct-values)
    
*   [Unique values ignore blanks](https://exceljet.net/functions/unique-function#unique-values-ignore-blanks)
    
*   [Unique values with criteria](https://exceljet.net/functions/unique-function#unique-values-with-criteria)
    
*   [Count unique values](https://exceljet.net/functions/unique-function#count-unique-values)
    
*   [Unique values by count](https://exceljet.net/functions/unique-function#unique-values-by-count)
    
*   [Unique with non-adjacent columns](https://exceljet.net/functions/unique-function#unique-with-non-adjacent-columns)
    
*   [Notes](https://exceljet.net/functions/unique-function#notes)
    

### Basic usage

Using the UNIQUE function is straightforward. Just provide a range or array:

    =UNIQUE(A1:A10) // unique values from A1:A10

Here are a few variations, which are explained in more detail below:

    =UNIQUE(A1:B10) // unique rows from two columns
    =UNIQUE(A1:E1,TRUE) // unique values from horizontal range
    =UNIQUE(A1:A10,,TRUE) // unique values that appear exactly once
    =SORT(UNIQUE(A1:A10)) // unique values, sorted
    

### Unique values

In the worksheet below, the goal is to extract a list of unique colors from the range B5:B16. The formula in D5 is:

    =UNIQUE(B5:B16)
    

![UNIQUE function example - unique values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_unique_values.png "UNIQUE function example - unique values")

The UNIQUE function evaluates the 12 values in B5:B16 and returns the 7 unique colors. The result spills into the range D5:D11 automatically. If any data in B5:B16 changes, the output from UNIQUE updates immediately.

For more details, see [Unique values](https://exceljet.net/formulas/unique-values)
.

### Unique values by column

By default, UNIQUE compares values by row. To extract unique values from horizontal data (arranged in columns), set _by\_col_ to TRUE. In the worksheet below, the goal is to extract unique colors from the range C4:I4. The formula in C6 is:

    =UNIQUE(C4:I4,TRUE)
    

![UNIQUE function example - unique values by column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_by_column.png "UNIQUE function example - unique values by column")

With _by\_col_ set to TRUE, UNIQUE compares values across columns instead of down rows. The result spills horizontally, returning the 5 unique colors: red, blue, green, purple, and gray. To convert the horizontal result to a vertical list, wrap the formula with [TRANSPOSE](https://exceljet.net/functions/transpose-function)
:

    =TRANSPOSE(UNIQUE(C4:I4,TRUE))

### Sort unique values

A common pattern is to combine UNIQUE with [SORT](https://exceljet.net/functions/sort-function)
 to return unique values in alphabetical or numerical order. In the worksheet below, the goal is to extract unique colors and sort them alphabetically. The formula in D5 is:

    =SORT(UNIQUE(B5:B16))
    

![UNIQUE function example - sort unique values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_sort_unique.png "UNIQUE function example - sort unique values")

Working from the inside out, UNIQUE extracts the 7 unique colors, then SORT arranges them in ascending order (A to Z). To sort in descending order (Z to A), add -1 as the third argument to SORT:

    =SORT(UNIQUE(B5:B16),,-1)
    

### Unique rows

UNIQUE can extract unique rows from multi-column data. In the worksheet below, the goal is to extract unique rows from the range B5:C15, which contains Group and Color columns. The formula in E5 is:

    =SORT(UNIQUE(B5:C15))
    

![UNIQUE function example - unique rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_unique_rows.png "UNIQUE function example - unique rows")

By default, UNIQUE compares values by row, so no special configuration is needed. The UNIQUE function evaluates all 11 rows and returns the 7 unique combinations of Group and Color. The [SORT function](https://exceljet.net/functions/sort-function)
 then sorts the result by the first column (Group). SORT is optional and can be removed if sorting isn't needed.

For more details, see [Unique rows](https://exceljet.net/formulas/unique-rows)
.

### Distinct values

The _exactly\_once_ argument controls how UNIQUE handles repeating values. By default, UNIQUE returns all unique values regardless of how many times they appear. Set _exactly\_once_ to TRUE to return only values that appear exactly once in the data. In the worksheet below, the goal is to extract colors that appear only once. The formula in D5 is:

    =UNIQUE(B5:B16,FALSE,TRUE)
    

![UNIQUE function example - distinct values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_distinct_values.png "UNIQUE function example - distinct values")

Because _exactly\_once_ is TRUE, UNIQUE returns only the 3 values that appear once: "purple", "pink", and "gray". Notice _by\_col_ is set to FALSE, which is the default. You can also omit _by\_col_ entirely:

    =UNIQUE(B5:B16,,TRUE)
    

For more details, see [Distinct values](https://exceljet.net/formulas/distinct-values)
.

### Unique values ignore blanks

By default, UNIQUE will include blank cells in the results, which will appear as a zero (0) in the output. To exclude blanks, use the [FILTER function](https://exceljet.net/functions/filter-function)
 to remove them first. In the worksheet below, the goal is to extract unique colors while ignoring blank cells. The formula in D5 is:

    =UNIQUE(FILTER(B5:B16,B5:B16<>""))
    

![UNIQUE function example - ignore blanks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_ignore_blanks.png "UNIQUE function example - ignore blanks")

Working from the inside out, FILTER removes blank cells using the criterion `<>""` (not equal to empty string). The filtered array is then passed to UNIQUE, which extracts the 5 unique colors.

For more details, see [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)
.

### Unique values with criteria

To extract unique values that meet specific criteria, combine UNIQUE with [FILTER](https://exceljet.net/functions/filter-function)
. In the worksheet below, the goal is to extract unique colors for each group (A and B). The formula in E5 is:

    =UNIQUE(FILTER(B5:B16,C5:C16=E4))
    

![UNIQUE function example - with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_with_criteria.png "UNIQUE function example - with criteria")

Working from the inside out, FILTER returns only colors where the corresponding group matches E4 ("A"). UNIQUE then extracts the unique colors from that filtered list. The formula in F5 works the same way, filtering for group "B" in F4.

For more details, see [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)
.

### Count unique values

To count unique values, wrap UNIQUE with [COUNTA](https://exceljet.net/functions/counta-function)
 or [ROWS](https://exceljet.net/functions/rows-function)
. In the worksheet below, the goal is to count the unique colors in B5:B16. The formula in F5 is:

    =COUNTA(UNIQUE(B5:B16))
    

![UNIQUE function example - count unique values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_count_unique.png "UNIQUE function example - count unique values")

UNIQUE returns an array of 7 unique colors, which COUNTA counts. You can also use `=ROWS(UNIQUE(B5:B16))` for the same result. If UNIQUE has already spilled results to the worksheet (as in D5), you can count them with a [spill range reference](https://exceljet.net/glossary/spill-range)
:

    =COUNTA(D5#)
    

The hash character (#) tells Excel to reference the entire spill range.

For more details, see [Count unique values](https://exceljet.net/formulas/count-unique-values)
.

> The GROUPBY function can also be used to count unique values. See [GroupBy function](https://exceljet.net/functions/groupby-function)
> .

### Unique values by count

To extract unique values that appear a certain number of times, combine UNIQUE with FILTER and [COUNTIF](https://exceljet.net/functions/countif-function)
. In the worksheet below, the goal is to extract colors that appear more than once (duplicates). The formula in D5 is:

    =UNIQUE(FILTER(B5:B16,COUNTIF(B5:B16,B5:B16)>1))
    

![UNIQUE function example - by count](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_by_count.png "UNIQUE function example - by count")

Working from the inside out, COUNTIF counts how many times each value appears in the data. The expression `COUNTIF(data,data)>1` returns TRUE for values that appear more than once. FILTER keeps only those values, and UNIQUE extracts the unique ones. The result shows the 4 colors that appear more than once: red, green, blue, and gray. In cell E5, the formula has been adjusted to extract unique values that appear more than twice:

    =UNIQUE(FILTER(B5:B16,COUNTIF(B5:B16,B5:B16)>2))

For more details, see [Unique values by count](https://exceljet.net/formulas/unique-values-by-count)
.

### Unique with non-adjacent columns

UNIQUE only works with adjacent columns. To extract unique values from non-adjacent columns, use [FILTER](https://exceljet.net/functions/filter-function)
 or [CHOOSECOLS](https://exceljet.net/functions/choosecols-function)
 to select the columns first. In the worksheet below, the goal is to extract unique combinations of Color (column B) and Region (column D), skipping Qty (column C). The formula in F5 is:

    =SORT(UNIQUE(FILTER(B5:D15,{1,0,1})))
    

![UNIQUE function example - non-adjacent columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/unique_example_non_adjacent.png "UNIQUE function example - non-adjacent columns")

The array constant `{1,0,1}` tells FILTER to include the first and third columns while excluding the middle column. UNIQUE then extracts unique rows from the two remaining columns, and SORT arranges the results alphabetically. As an alternative, you can use the CHOOSECOLS function instead of an array constant like this:

    =SORT(UNIQUE(CHOOSECOLS(B5:D15,1,3)))

For more details, see [UNIQUE with non-adjacent columns](https://exceljet.net/formulas/unique-with-non-adjacent-columns)
.

### Notes

*   UNIQUE is case-insensitive. "APPLE", "Apple", and "apple" are treated as identical.
*   UNIQUE treats text and numbers as different types. The text "10" and the number 10 are considered different values.
*   Empty cells appear as zeros (0) in results. Use FILTER to exclude blanks before UNIQUE runs.
*   The empty string "" and truly empty cells may be treated differently. Use `<>""` to filter both.
*   UNIQUE returns #SPILL! if the destination range isn't empty or doesn't have room for results.
*   Cross-workbook references require both workbooks to be open. Closed workbooks return #REF!.
*   UNIQUE won't automatically adjust the source range if data is added or deleted. Use an [Excel Table](https://exceljet.net/articles/excel-tables)
     or dynamic range if needed.

UNIQUE function examples
------------------------

[![Excel formula: Multiple matches into separate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_rows.png "Excel formula: Multiple matches into separate rows")](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

### [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

In this example, the goal is to get all names in a given group into separate rows grouped by column, as seen in the worksheet above. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns where each column holds the names that belong to a...

[![Excel formula: Unique values with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20with%20multiple%20criteria.png "Excel formula: Unique values with multiple criteria")](https://exceljet.net/formulas/unique-values-with-multiple-criteria)

### [Unique values with multiple criteria](https://exceljet.net/formulas/unique-values-with-multiple-criteria)

This example uses the UNIQUE function together with the FILTER function. The FILTER function removes data that does not meet required criteria, and the UNIQUE function further limits results to unique values only. Working from the inside out, the FILTER function is used to collect source data in...

[![Excel formula: Minimum value if unique](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum%20value%20if%20unique.png "Excel formula: Minimum value if unique")](https://exceljet.net/formulas/minimum-value-if-unique)

### [Minimum value if unique](https://exceljet.net/formulas/minimum-value-if-unique)

The goal in this example is to return the minimum value that is unique, i.e. the minimum value that occurs only once in the data. The UNIQUE function, new in Excel 365 , will return a unique list of values from a set of data. By default, this is a list of any value that occurs one or more times in...

[![Excel formula: 10 most common text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/10%20most%20common%20text%20values.png "Excel formula: 10 most common text values")](https://exceljet.net/formulas/10-most-common-text-values)

### [10 most common text values](https://exceljet.net/formulas/10-most-common-text-values)

In this example, the goal is to list the 10 most frequently occurring text values in a range, in descending order by count, as seen in the range in E5:F14. This is an advanced formula that requires a number of nested functions. However, it is an excellent example of the power of dynamic array...

[![Excel formula: UNIQUE with non-adjacent columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20with%20non-adjacent%20columns.png "Excel formula: UNIQUE with non-adjacent columns")](https://exceljet.net/formulas/unique-with-non-adjacent-columns)

### [UNIQUE with non-adjacent columns](https://exceljet.net/formulas/unique-with-non-adjacent-columns)

Although FILTER is commonly used to filter rows, you can also filter columns. The trick is to use an include argument that operates on columns instead of rows. In this example, we use a hard-coded array constant to filter out unwanted columns, but you can also use a logical expression that returns...

[![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")](https://exceljet.net/formulas/dynamic-two-way-count)

### [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps: Create an Excel Table called data List unique colors with UNIQUE function List unique sizes with UNIQUE...

[![Excel formula: Unique values ignore blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20ignore%20blanks.png "Excel formula: Unique values ignore blanks")](https://exceljet.net/formulas/unique-values-ignore-blanks)

### [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove any blank values from the data: FILTER(B5:B16,B5:B16<>"") The <> symbol is a logical operator that means "does not equal". For more examples...

[![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")](https://exceljet.net/formulas/sum-by-week)

### [Sum by week](https://exceljet.net/formulas/sum-by-week)

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named data in the range B5:C16. This problem can be solved in a straightforward way with the SUMIFS function . In the current version of...

[![Excel formula: Multiple matches into separate columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_columns.png "Excel formula: Multiple matches into separate columns")](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

### [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

In this example, the goal is to get all names in a given group into the same row, in separate columns, as seen in the worksheet. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns using common values, which in this case are the group...

[![Excel formula: Dynamic two-way average](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20average.png "Excel formula: Dynamic two-way average")](https://exceljet.net/formulas/dynamic-two-way-average)

### [Dynamic two-way average](https://exceljet.net/formulas/dynamic-two-way-average)

In this example, the goal is to create a formula that performs a dynamic two-way average of all age and gender combinations in the range B5:D16 . The solution shown requires four general steps: Create an Excel Table called data List unique age groups with UNIQUE function List unique genders with...

[![Excel formula: Count unique values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values%20with%20criteria.png "Excel formula: Count unique values with criteria")](https://exceljet.net/formulas/count-unique-values-with-criteria)

### [Count unique values with criteria](https://exceljet.net/formulas/count-unique-values-with-criteria)

In this example, the goal is to count unique values that meet one or more specific conditions. In the example shown, the formula used in cell H7 is: =SUM(--(LEN(UNIQUE(FILTER(B6:B15,C6:C15=H6,"")))>0)) At the core, this formula uses the FILTER function to apply criteria, and the UNIQUE function...

[![Excel formula: Dynamic summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20summary%20count.png "Excel formula: Dynamic summary count")](https://exceljet.net/formulas/dynamic-summary-count)

### [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)

In this example, the goal is to build a simple summary count table with a formula. Once created, the summary table should automatically update to show new values and counts when data changes. The article below walks through several options, from simple to very advanced. The more advanced options...

[![Excel formula: Sum numbers with text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20numbers%20with%20text.png "Excel formula: Sum numbers with text")](https://exceljet.net/formulas/sum-numbers-with-text)

### [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)

In this example, one goal is to sum the numbers that appear in the range B5:B16. A second more challenging goal is to create the table of results seen in E7:F12. For convenience, data is the named range B5:B16. Total sum To sum all the numbers that appear in B5:B16, ignoring text, the formula in E5...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Average salary by department](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_salary_by_department.png "Excel formula: Average salary by department")](https://exceljet.net/formulas/average-salary-by-department)

### [Average salary by department](https://exceljet.net/formulas/average-salary-by-department)

In this example, the goal is to create a formula that calculates an average salary by department, where data is an Excel Table in the range B5:D16. The solution shown requires three general steps: Create an Excel Table called data List unique departments with the UNIQUE function Calculate averages...

UNIQUE function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Filter%20with%20dynamic%20dropdown%20list-Play.png)](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)

### [Filter with dynamic dropdown list](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)

In this video, we'll build a dropdown list using dynamic arrays to filter data. Here we have data in an Excel Table called "data". In cell J2, I'll set up a dropdown list we can use to filter data by color. First, I'll type "Red" in J2, so we have something to filter on. Next, I'll enter the FILTER...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Two-way%20summary%20with%20dynamic%20arrays-PLAY.png)](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)

### [Two-way summary with dynamic arrays](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)

In this video, we'll look at how to create a two-way summary table with dynamic array formulas that works like a pivot table. This worksheet contains several hundred rows of sample order data in an Excel Table called "data". I'll first build a pivot table to summarize this data by Color and Region...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20count%20unique%20values-Play_0.png)](https://exceljet.net/videos/how-to-count-unique-values)

### [How to count unique values](https://exceljet.net/videos/how-to-count-unique-values)

In this video, we'll look at how to count the unique values returned by the UNIQUE function . Before dynamic array formulas, counting unique values in Excel involved complex array formulas, especially if you needed to count values based on one or more conditions. Now that dynamic array formulas,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Spilling%20and%20the%20spill%20range-Play.png)](https://exceljet.net/videos/spilling-and-the-spill-range)

### [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)

In this video, we’ll look at a core idea in dynamic array behavior, the spill range . When a dynamic array formula outputs multiple values, it is said to “spill” these values onto the worksheet. For example, if I use the UNIQUE function on this list of colors, UNIQUE spills 3 values - red, blue,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/New%20dynamic%20array%20functions%20in%20Excel-Play.png)](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

### [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

In this video, we'll quickly review new Dynamic Array functions in Excel. With the introduction of dynamic array formulas, Excel includes 6 brand new functions that directly leverage dynamic array behavior. Each of these functions is covered in more detail later in the course, so this is just a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20UNIQUE%20function-Play.png)](https://exceljet.net/videos/the-unique-function)

### [The UNIQUE function](https://exceljet.net/videos/the-unique-function)

In this video, we'll introduce the UNIQUE function . One of the new functions that comes with the dynamic array version of Excel is UNIQUE. The UNIQUE function lets you extract unique values in a variety of ways. The UNIQUE function takes three arguments. The first argument, array is the source...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/List%20duplicate%20values%20with%20FILTER-Play.png)](https://exceljet.net/videos/list-duplicate-values-with-filter)

### [List duplicate values with FILTER](https://exceljet.net/videos/list-duplicate-values-with-filter)

In this video, we'll look at how to list duplicate values. In other words, values that appear more than once in a set of data. In this worksheet, we have a list of the Wimbledon Men's Singles Champions since 1968, in a table called "data". How can we list names that appear more than once, along...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20see%20arrays%20in%20formulas-Play.png)](https://exceljet.net/videos/how-to-see-arrays-in-formulas)

### [How to see arrays in formulas](https://exceljet.net/videos/how-to-see-arrays-in-formulas)

In this video, we'll look at a few ways that you can see or visualize arrays in a formula. One of the best things about the new dynamic array formula engine in Excel is that it's much easier to see and visualize arrays. Let's take a look at a few examples. The first way to see arrays is to enter...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Unique%20values%20with%20criteria-Play.png)](https://exceljet.net/videos/unique-values-with-criteria)

### [Unique values with criteria](https://exceljet.net/videos/unique-values-with-criteria)

In this video, we'll look at how to use the FILTER function together with the UNIQUE function to limit results using logical criteria. There are many situations in which you may want to use logical criteria to filter or limit the values processed by the UNIQUE function. In this first worksheet, we...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

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

*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)
    
*   [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)
    
*   [Unique values by count](https://exceljet.net/formulas/unique-values-by-count)
    
*   [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)
    
*   [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)
    
*   [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)
    
*   [Unique values from multiple ranges](https://exceljet.net/formulas/unique-values-from-multiple-ranges)
    
*   [UNIQUE with non-adjacent columns](https://exceljet.net/formulas/unique-with-non-adjacent-columns)
    
*   [Unique values](https://exceljet.net/formulas/unique-values)
    

### Videos

*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
    
*   [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)
    
*   [The UNIQUE function](https://exceljet.net/videos/the-unique-function)
    
*   [How to count unique values](https://exceljet.net/videos/how-to-count-unique-values)
    
*   [Unique values with criteria](https://exceljet.net/videos/unique-values-with-criteria)
    
*   [How to see arrays in formulas](https://exceljet.net/videos/how-to-see-arrays-in-formulas)
    
*   [Two-way summary with dynamic arrays](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)
    
*   [Filter with dynamic dropdown list](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)
    
*   [List duplicate values with FILTER](https://exceljet.net/videos/list-duplicate-values-with-filter)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

### Links

*   [Microsoft UNIQUE function documentation](https://support.office.com/en-us/article/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e)
    

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
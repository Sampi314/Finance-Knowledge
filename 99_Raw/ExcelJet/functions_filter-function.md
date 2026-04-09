# Excel FILTER function | Exceljet

**Source:** https://exceljet.net/functions/filter-function

---

[Skip to main content](https://exceljet.net/functions/filter-function#main-content)

[](https://exceljet.net/functions/filter-function#)

*   [Previous](https://exceljet.net/functions/expand-function)
    
*   [Next](https://exceljet.net/functions/groupby-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

FILTER Function
===============

by Dave Bruns · Updated 4 Jun 2025

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SORT](https://exceljet.net/functions/sort-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel FILTER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")

Summary
-------

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without altering the original dataset. 

Purpose 
--------

Filter range with given criteria

Return value 
-------------

Array of filtered values

Syntax
------

    =FILTER(array,include,[if_empty])

*   _array_ - Range or array to filter.
*   _include_ - Boolean array, supplied as criteria.
*   _if\_empty_ - \[optional\] Value to return when no results are returned.

Using the FILTER function 
--------------------------

The FILTER function "filters" data based on one or more conditions, and extracts matching values. The conditions are provided as logical expressions that test the source data and return TRUE or FALSE. The result from FILTER is an [array](https://exceljet.net/glossary/array)
 of matching values from the original data. The results from FILTER are _dynamic_. If source data changes or if conditions are modified, FILTER will return new results. This makes FILTER a very good way to isolate and inspect specific data without altering the original dataset. Watch the video below to see a basic example of FILTER in action:

Video: [Basic FILTER function example](https://exceljet.net/videos/filter-function-basic-example)
 (3 minutes)

FILTER is a flexible function that can extract matching data based on a wide variety of conditions. If you can apply a test that returns TRUE or FALSE, you can use that test to extract data with FILTER. You can filter data that occurs in a certain year or month, data associated with a particular day of the week, data that contains specific text, data that meets a numeric threshold, and more.

### Basic example

The FILTER function takes two required arguments: _array_ and _include_. The _array_ is the source data to filter. The _include_ argument should consist of one or more [logical tests](https://exceljet.net/glossary/logical-test)
 that return TRUE or FALSE. For example, to extract _values_ in B5:B14 that are greater than 100, you can use the FILTER function like this:

![FILTER function basic example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/FILTER_function_basic_example.png "FILTER function basic example")

The formula in cell D5 looks like this:

    =FILTER(B5:B14,B5:B14>100)
    

Notice that the _include_ argument is a logical expression, B5:B14. Because there are 10 cells in the range, the expression returns an array that contains 10 results like this:

    =FILTER(B5:B14,{FALSE;TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE})

Each result in the array corresponds to a value in B5:B14. The FILTER function uses this array to "filter" the values in B5:B14. The values in B5:B14 that are associated with TRUE are returned, and the values associated with FALSE are discarded.

### Filter for Red group

![Filter on red group example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/FILTER%20on%20red%20group%20example.png?itok=2Db5lAoo "Filter on red group example")

In the example shown above, the formula in F5 is:

    =FILTER(B5:D14,D5:D14=H2,"No results")
    

Since the value in H2 is "Red", the FILTER function extracts data from the _array_ when the Group column equals "Red". All matching records are returned to the worksheet starting from cell F5, where the formula resides.

Values can be hardcoded as well. The formula below has the same result as above with "red" hardcoded into the criteria:

    =FILTER(B5:D14,D5:D14="Red","No results")
    

### No matching data

FILTER will return a #CALC! error if no matching data is found, but you can use the optional _is\_empty_ argument to return a different result. Often, _is\_empty_ is configured to provide a message to the user. For example, the formula below will return "No results" if the logic applied by the _include_ argument fails to match any values:

    =FILTER(array,include,"No results") // display message
    

To display nothing when no matching data is found, provide an [empty string](https://exceljet.net/glossary/empty-string)
 ("") for _if\_empty_:

    =FILTER(array,include,"") // display nothing
    

Note that the value for _is\_empty_ is only used when FILTER does not find matching results.

### Values that contain text

To extract data based on a logical test for values that contain specific text, you can use a formula like this:

    =FILTER(rng1,ISNUMBER(SEARCH("txt",rng2)))
    

In this formula, the [SEARCH function](https://exceljet.net/functions/search-function)
 is used to look for "txt" in **rng2**, which would typically be a column in **rng1**. The [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 is used to convert the result from SEARCH into TRUE or FALSE. [Read a full explanation here](https://exceljet.net/formulas/filter-text-contains)
.

### Filter by date

FILTER can be used with dates by constructing logical tests appropriate for [Excel dates](https://exceljet.net/glossary/excel-date)
. For example, to extract records from **rng1** where the date in **rng2** is in July you can use a generic formula like this:

    =FILTER(rng1,MONTH(rng2)=7,"No data")
    

This formula relies on the [MONTH function](https://exceljet.net/functions/month-function)
 to compare the month of dates in **rng2** to 7. [See full explanation here](https://exceljet.net/formulas/filter-by-date)
.

### Multiple criteria

At first glance, it's not obvious how to apply multiple criteria with the FILTER function. Unlike older functions like [COUNTIFS](https://exceljet.net/functions/countifs-function)
 and [SUMIFS](https://exceljet.net/functions/sumifs-function)
, which provide _multiple_ arguments for entering multiple conditions, the FILTER function only provides a single argument, _include_, to target data. The trick is to create logical expressions that use [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
 to target the data of interest and supply these expressions as the _include_ argument. For example, to extract data where one value is "A" and another value is greater than 80, you can use a formula like this:

    =FILTER(range,(range="A")*(range>80),"No data")
    

The math operation of multiplication (\*) joins the two conditions with AND logic: both conditions must be TRUE in order for FILTER to retrieve the data. [See a detailed explanation here](https://exceljet.net/formulas/filter-with-multiple-criteria)
.

### Complex criteria

To filter and extract data based on multiple complex criteria, you can use the FILTER function with a chain of expressions that use Boolean logic. For example, the generic formula below filters based on three separate conditions: account begins with "x" AND region is "east", and month is NOT April.

    =FILTER(data,(LEFT(account)="x")*(region="east")*NOT(MONTH(date)=4))
    

[See this page for a full explanation](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
. Building criteria with logical expressions is an elegant and flexible approach that can be extended to handle many complex scenarios. See below for more examples.

### Wildcards

The FILTER function _does not_ support [wildcards](https://exceljet.net/glossary/wildcard)
 (\*?~) like the XLOOKUP function. However, you can work around this limitation by combining the FILTER function with the SEARCH function like this:

    =FILTER(range,ISNUMBER(SEARCH("substring",range)))

The SEARCH function automatically performs a substring search and supports wildcards directly if you need more flexibility. See [FILTER text contains](https://exceljet.net/formulas/filter-text-contains)
 and [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
 for a more complete explanation.

### Notes

1.  FILTER can work with both vertical and [horizontal](https://exceljet.net/formulas/filter-horizontal-data)
     arrays.
2.  The _include_ argument must have dimensions compatible with the _array_ argument, or FILTER will return #VALUE!
3.  If the _include_ array includes any errors, FILTER will return an error.

FILTER function examples
------------------------

[![Excel formula: nth largest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value_with_criteria.png "Excel formula: nth largest value with criteria")](https://exceljet.net/formulas/nth-largest-value-with-criteria)

### [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)

In this example, the goal is to retrieve the top 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the LARGE function, which can be used to retrieve the "nth" largest...

[![Excel formula: FILTER last n valid entries](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20last%20n%20valid%20entries.png "Excel formula: FILTER last n valid entries")](https://exceljet.net/formulas/filter-last-n-valid-entries)

### [FILTER last n valid entries](https://exceljet.net/formulas/filter-last-n-valid-entries)

The goal in this example is to display the last 3 valid entries from the table shown, where "valid" is defined as a temperature of less than 75 in the "Temp" column. At a high level, the FILTER function is used to filter entries based on a logical test, and the INDEX function is used to extract the...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: FILTER with multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20multiple%20or%20criteria.png "Excel formula: FILTER with multiple OR criteria")](https://exceljet.net/formulas/filter-with-multiple-or-criteria)

### [FILTER with multiple OR criteria](https://exceljet.net/formulas/filter-with-multiple-or-criteria)

In this example, criteria are entered in the range F5:H6. The logic of the formula is: item is (tshirt OR hoodie) AND color is (red OR blue) AND city is (denver OR seattle) The filtering logic of this formula (the include argument) is applied with the ISNUMBER and MATCH functions, together with...

[![Excel formula: Large with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/large_with_criteria.png "Excel formula: Large with criteria")](https://exceljet.net/formulas/large-with-criteria)

### [Large with criteria](https://exceljet.net/formulas/large-with-criteria)

In this example, the goal is to display the top 3 values in C5:C16 that match a specific group, entered as a variable in cell F4. If the group is changed, the formulas should calculate new results. For convenience, group (B5:B16) and value (C5:C16) are named ranges . The core of the solution is the...

[![Excel formula: Multiple matches into separate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_rows.png "Excel formula: Multiple matches into separate rows")](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

### [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

In this example, the goal is to get all names in a given group into separate rows grouped by column, as seen in the worksheet above. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns where each column holds the names that belong to a...

[![Excel formula: FILTER to remove columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20to%20remove%20columns.png "Excel formula: FILTER to remove columns")](https://exceljet.net/formulas/filter-to-remove-columns)

### [FILTER to remove columns](https://exceljet.net/formulas/filter-to-remove-columns)

Although FILTER is more commonly used to filter rows, you can also filter columns, the trick is to supply an array with the same number of columns as the source data. In this example, we construct the array we need with boolean logic , also called Boolean algebra. In Boolean algebra, multiplication...

[![Excel formula: Sum matching columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20matching%20columns.png "Excel formula: Sum matching columns")](https://exceljet.net/formulas/sum-matching-columns)

### [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)

At the core, this formula relies on the SUMPRODUCT function to sum values in matching columns in the named range data C5:G14. If all data were provided to SUMPRODUCT in a single range, the result would be the sum of all values in the range: =SUMPRODUCT(data) // all data, returns 387 To apply a...

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

[![Excel formula: Sum bottom n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values%20with%20criteria.png "Excel formula: Sum bottom n values with criteria")](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

### [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

In this example, the goal is to sum the smallest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three smallest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Get last match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match.png "Excel formula: Get last match")](https://exceljet.net/formulas/get-last-match)

### [Get last match](https://exceljet.net/formulas/get-last-match)

In the example shown, we have a set of order data that includes Date, Product, Name, and Amount. The data is sorted by date in ascending order. The goal is to look up the latest order for a given person by Name. In other words, we want the last match by name. The challenge is that Excel lookup...

[![Excel formula: Extract common values from text strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_common_values_from_two_text_strings.png "Excel formula: Extract common values from text strings")](https://exceljet.net/formulas/extract-common-values-from-text-strings)

### [Extract common values from text strings](https://exceljet.net/formulas/extract-common-values-from-text-strings)

In this example, the goal is to extract common values from two text strings that contain comma-delimited values. In the worksheet shown the values for "List1" appear in column B and the values for "List2" appear in column C. The results in column D show the intersection of the two lists, that is,...

[![Excel formula: Lookup first negative value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20first%20negative%20value.png "Excel formula: Lookup first negative value")](https://exceljet.net/formulas/lookup-first-negative-value)

### [Lookup first negative value](https://exceljet.net/formulas/lookup-first-negative-value)

In this example, the goal is to lookup the first negative value in a set of data. In addition, we also want to get the corresponding date. All data is in an Excel Table called data, in the range B5:C16. This information represents the low temperature in Fahrenheit (F) for the dates as shown. There...

[![Excel formula: List nth weekdays of the month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_nth_weekdays_of_the_month.png "Excel formula: List nth weekdays of the month")](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

### [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

In this example, the goal is to generate a list of "nth weekdays of the month" with a formula. For example, the formula should be able to create a list of any of the following: 2nd Tuesdays of the month 1st Fridays of the month 3rd Mondays of the month This is a somewhat challenging problem in...

[![Excel formula: Sequence of leap years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_leap_years.png "Excel formula: Sequence of leap years")](https://exceljet.net/formulas/sequence-of-leap-years)

### [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)

In this example, the goal is to generate a list of leap years between a given start year and end year. The worksheet is set up so that the start year is an input in cell B5 and the end year is an input in cell B8. If either value changes, the formula should generate a new list of leap years. In the...

FILTER function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20with%20boolean%20logic-Play.png)](https://exceljet.net/videos/filter-with-boolean-logic)

### [FILTER with boolean logic](https://exceljet.net/videos/filter-with-boolean-logic)

In this video we'll look how to use the FILTER function with Boolean logic to apply multiple criteria. In this worksheet we have some sample order data in a table called "data". Let's use the FILTER function to find all "blue" orders in June. To visualize how this works I'm going to set up the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20data%20between%20two%20dates-Play.png)](https://exceljet.net/videos/filter-data-between-two-dates)

### [FILTER data between two dates](https://exceljet.net/videos/filter-data-between-two-dates)

In this video, we’ll look at a couple ways to use the FILTER function to extract data between dates. In this worksheet, we have sample order data that contains a date field. Let's set up the FILTER function to extract data between two dates. Before we begin, I want to remind you that Excel dates...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Nesting%20dynamic%20array%20formulas-Play.png)](https://exceljet.net/videos/nesting-dynamic-array-formulas)

### [Nesting dynamic array formulas](https://exceljet.net/videos/nesting-dynamic-array-formulas)

In this video, we'll look at how to nest dynamic array formulas together. One of the most powerful ways to extend the functionality of dynamic array formulas is to nest one function inside another. To illustrate, let's look at an example based on the SORT and FILTER functions. Here we have data...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20with%20two%20criteria-play.png)](https://exceljet.net/videos/filter-function-with-two-criteria)

### [FILTER function with two criteria](https://exceljet.net/videos/filter-function-with-two-criteria)

In this video, we’ll set up the FILTER function with two criteria. The FILTER function is designed to extract data from a list or table using supplied criteria. In this worksheet, we have data that contains an order number, amount, name, and state. Our goal is to use the FILTER function to extract...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/List%20duplicate%20values%20with%20FILTER-Play.png)](https://exceljet.net/videos/list-duplicate-values-with-filter)

### [List duplicate values with FILTER](https://exceljet.net/videos/list-duplicate-values-with-filter)

In this video, we'll look at how to list duplicate values. In other words, values that appear more than once in a set of data. In this worksheet, we have a list of the Wimbledon Men's Singles Champions since 1968, in a table called "data". How can we list names that appear more than once, along...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/New%20dynamic%20array%20functions%20in%20Excel-Play.png)](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

### [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

In this video, we'll quickly review new Dynamic Array functions in Excel. With the introduction of dynamic array formulas, Excel includes 6 brand new functions that directly leverage dynamic array behavior. Each of these functions is covered in more detail later in the course, so this is just a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20show%20top%20or%20bottom%20results-Play.png)](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)

### [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)

In this video, we'll use the FILTER function to show the top or bottom results in a set of data. Here we have some test scores for a group of students. In column F, I want to set up a formula to display the top students by score. Now, I'm going to use the FILTER function, but we'll need a way to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Filter%20with%20dynamic%20dropdown%20list-Play.png)](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)

### [Filter with dynamic dropdown list](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)

In this video, we'll build a dropdown list using dynamic arrays to filter data. Here we have data in an Excel Table called "data". In cell J2, I'll set up a dropdown list we can use to filter data by color. First, I'll type "Red" in J2, so we have something to filter on. Next, I'll enter the FILTER...

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

*   [FILTER last n valid entries](https://exceljet.net/formulas/filter-last-n-valid-entries)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [Max value with variable column](https://exceljet.net/formulas/max-value-with-variable-column)
    
*   [Filter and exclude columns](https://exceljet.net/formulas/filter-and-exclude-columns)
    
*   [XLOOKUP approximate match with multiple criteria](https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    
*   [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)
    
*   [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)
    
*   [FILTER with multiple OR criteria](https://exceljet.net/formulas/filter-with-multiple-or-criteria)
    
*   [Unique values with multiple criteria](https://exceljet.net/formulas/unique-values-with-multiple-criteria)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [FILTER function with two criteria](https://exceljet.net/videos/filter-function-with-two-criteria)
    
*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
    
*   [Nesting dynamic array formulas](https://exceljet.net/videos/nesting-dynamic-array-formulas)
    
*   [How to count unique values](https://exceljet.net/videos/how-to-count-unique-values)
    
*   [Unique values with criteria](https://exceljet.net/videos/unique-values-with-criteria)
    
*   [FILTER data between two dates](https://exceljet.net/videos/filter-data-between-two-dates)
    
*   [FILTER with boolean logic](https://exceljet.net/videos/filter-with-boolean-logic)
    
*   [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)
    
*   [Filter with dynamic dropdown list](https://exceljet.net/videos/filter-with-dynamic-dropdown-list)
    

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

*   [Microsoft FILTER function documentation](https://support.office.com/en-us/article/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759)
    

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
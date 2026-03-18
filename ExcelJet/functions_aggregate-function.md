# Excel AGGREGATE function | Exceljet

**Source:** https://exceljet.net/functions/aggregate-function

---

[Skip to main content](https://exceljet.net/functions/aggregate-function#main-content)

[](https://exceljet.net/functions/aggregate-function#)

*   [Previous](https://exceljet.net/functions/abs-function)
    
*   [Next](https://exceljet.net/functions/arabic-function)
    

Excel 2010

[Math](https://exceljet.net/functions#Math)

AGGREGATE Function
==================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[COUNT](https://exceljet.net/functions/count-function)

[SUBTOTAL](https://exceljet.net/functions/subtotal-function)

![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")

Summary
-------

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

Purpose 
--------

Return aggregate calculation

Return value 
-------------

Depends on function specified

Syntax
------

    =AGGREGATE(function_num,options,ref1,[ref2],...)

*   _function\_num_ - Operation to perform (1-19).
*   _options_ - Values to ignore (0-7).
*   _ref1_ - First argument.
*   _ref2_ - \[optional\] Second argument (k).

Using the AGGREGATE function 
-----------------------------

The AGGREGATE function returns the result of an aggregate calculation like AVERAGE, COUNT, MAX, MIN, etc. performed on one or more references. The AGGREGATE function is like an upgraded version of the older [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
, and provides more calculation options, and more control over ignoring specific things. There are two reasons that make the AGGREGATE function especially useful, compared to other functions which perform the same operations:

1.  AGGREGATE has a number of options for ignoring errors, hidden rows, and other functions that may appear in data.
2.  AGGREGATE can handle many [array operations](https://exceljet.net/glossary/array-operation)
     natively, without [Control + Shift + Enter](https://exceljet.net/glossary/cse)
    .

AGGREGATE can run a total of [19 functions](https://exceljet.net/functions/aggregate-function#function_numbers)
, and the function to perform is given as a number, which appears as the first argument in the function, _function\_num_. The second argument, _options_, controls how AGGREGATE handles errors and values in hidden rows. See the [table below](https://exceljet.net/functions/aggregate-function#options)
 for all available options.

The AGGREGATE function takes four [arguments](https://exceljet.net/glossary/function-argument)
: _function\_num_, _options_, _ref1_, and _ref2_. For the first 13 functions supported, only the first three arguments are required: _function\_num_ specifies the operation, _options_ controls various behaviors, and _ref1_ is the array of values to process.

The last 6 functions require all four arguments: _function\_num_ specifies the operation, _options_ controls [various behaviors](https://exceljet.net/functions/aggregate-function#options)
, _ref1_ is the array of values to process, and _ref2_ is the "second argument" for the function being called. For example, functions like [SMALL](https://exceljet.net/functions/small-function)
 and [LARGE](https://exceljet.net/functions/large-function)
 take a second argument, _k_, and _ref2_ represents that argument. The following six functions require the _ref2_ argument:

    LARGE(array,k)
    SMALL(array,k)
    PERCENTILE.INC(array,k)
    QUARTILE.INC(array,quart)
    PERCENTILE.EXC(array,k)
    QUARTILE.EXC(array,quart)
    

### Example #1 

To return the MAX value in the range A1:A10, ignoring both errors _and_ hidden rows, provide 4 for function number and 7 for _options_:

    =AGGREGATE(4,7,A1:A10) // max value
    

To return the MIN value with the same options, change the function number to 5:

    =AGGREGATE(5,7,A1:A10) // min value
    

### Example #2

In the example shown above, the formula in D5 is:

    =AGGREGATE(4,6,values)
    

where "values" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B14. The function number is 4, which specifies MAX. _Options_ is provided as 6, to ignore errors only.

### Example #3 - nth largest

The formulas in D8:D10 demonstrate how to return "nth largest" values:

    =AGGREGATE(14,6,values,1) // 1st largest
    =AGGREGATE(14,6,values,2) // 2nd largest
    =AGGREGATE(14,6,values,3) // 3rd largest
    

The function number here is 14, which runs the [LARGE function](https://exceljet.net/functions/large-function)
. Because the LARGE function requires a _k_ argument, it appears as the last argument in the three formulas above.

### Example #4 - array operation

What makes AGGREGATE especially useful for more complex formulas is that it can handle arrays natively when the function number is 14-19. For example, to find the MAX value on Mondays, with data that includes dates and values, you could use AGGREGATE like this:

    =AGGREGATE(14,6,values/(TEXT(dates,"ddd")="Mon"),1)
    

Here we specify 14 for function (LARGE) and 6 for option (ignore errors). Then we build a [logical expression](https://exceljet.net/glossary/logical-test)
 using the TEXT function to check all dates for Mondays. The result of this operation is an [array](https://exceljet.net/glossary/array)
 of TRUE/FALSE values, which become the denominator of the original values. FALSE evaluates as zero, and throws a #DIV/0! error. TRUE evaluates as 1 and returns the original value. The final array of values and errors acts like a filter. AGGREGATE ignores all errors and returns the largest (maximum) of the surviving values. [More complete example here](https://exceljet.net/formulas/max-value-on-given-weekday)
.

### Function numbers

The table below lists the function numbers available to the AGGREGATE function, along with the name of the associated function. The third column, _Ref2_, indicates the "second argument" expected by the last 6 functions.

| Function number | Function | Ref2 |
| --- | --- | --- |
| 1   | [AVERAGE](https://exceljet.net/functions/average-function) |     |
| 2   | [COUNT](https://exceljet.net/functions/count-function) |     |
| 3   | [COUNTA](https://exceljet.net/functions/counta-function) |     |
| 4   | [MAX](https://exceljet.net/functions/max-function) |     |
| 5   | [MIN](https://exceljet.net/functions/min-function) |     |
| 6   | [PRODUCT](https://exceljet.net/functions/product-function) |     |
| 7   | [STDEV.S](https://exceljet.net/functions/stdev.s-function) |     |
| 8   | [STDEV.P](https://exceljet.net/functions/stdev.p-function) |     |
| 9   | [SUM](https://exceljet.net/functions/sum-function) |     |
| 10  | [VAR.S](https://exceljet.net/functions/var.s-function) |     |
| 11  | [VAR.P](https://exceljet.net/functions/var.p-function) |     |
| 12  | [MEDIAN](https://exceljet.net/functions/median-function) |     |
| 13  | [MODE.SNGL](https://exceljet.net/functions/mode.sngl-function) |     |
| 14  | [LARGE](https://exceljet.net/functions/large-function) | k   |
| 15  | [SMALL](https://exceljet.net/functions/small-function) | k   |
| 16  | [PERCENTILE.INC](https://exceljet.net/functions/percentile.inc-function) | k   |
| 17  | [QUARTILE.INC](https://exceljet.net/functions/quartile.inc-function) | quart |
| 18  | [PERCENTILE.EXC](https://exceljet.net/functions/percentile.exc-function) | k   |
| 19  | [QUARTILE.EXC](https://exceljet.net/functions/quartile.exc-function) | quart |

### Behavior options

The AGGREGATE function has many options for ignoring errors, hidden rows, and other functions. Options are set with the _options_ argument. Possible values are 0-7, as shown in the table below.

| Option | Behavior |
| --- | --- |
| 0   | Ignore SUBTOTAL and AGGREGATE functions |
| 1   | Ignore hidden rows, SUBTOTAL and AGGREGATE functions |
| 2   | Ignore error values, SUBTOTAL and AGGREGATE functions |
| 3   | Ignore hidden rows, error values, SUBTOTAL and AGGREGATE functions |
| 4   | Ignore nothing |
| 5   | Ignore hidden rows |
| 6   | Ignore error values |
| 7   | Ignore hidden rows and error values |

_Note: The AGGREGATE function is like an upgraded version of the older [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
, and provides more calculation options, and more control over ignoring specific things. However, one subtle difference between AGGREGATE and SUBTOTAL is that the default behavior for hidden rows is reversed. While SUBTOTAL will always ignore values in rows hidden by a filter, and needs a different function number to ignore manually hidden rows, AGGREGATE will always ignore manually hidden rows and needs a specific option to ignore rows hidden by a filter. Even when the option argument is set to 4 (ignore nothing), AGGREGATE will ignore values in manually hidden rows._

### Notes

*   AGGREGATE returns a #VALUE! error if a second function argument is required, but not provided.
*   [3D references](https://exceljet.net/videos/how-to-create-3d-references)
     do not work with AGGREGATE.
*   The AGGREGATE function is designed for vertical ranges, not horizontal ranges.

AGGREGATE function examples
---------------------------

[![Excel formula: Max value on given weekday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_value_on_given_weekday.png "Excel formula: Max value on given weekday")](https://exceljet.net/formulas/max-value-on-given-weekday)

### [Max value on given weekday](https://exceljet.net/formulas/max-value-on-given-weekday)

In this example, the goal is to calculate the maximum value that occurs in a set of data on a given weekday (i.e. Monday, Tuesday, Wednesday, Thursday, Friday). In the current version of Excel, the simplest approach is to use the FILTER function. In older versions of Excel, you can use a...

[![Excel formula: INDEX and MATCH all partial matches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_all_partial_matches.png "Excel formula: INDEX and MATCH all partial matches")](https://exceljet.net/formulas/index-and-match-all-partial-matches)

### [INDEX and MATCH all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)

Note: in the current version of Excel, the FILTER function is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for legacy versions of Excel that do not provide the FILTER function. The core of this formula is the INDEX function, with AGGREGATE used to figure...

[![Excel formula: Get last match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match_cell_contains.png "Excel formula: Get last match cell contains")](https://exceljet.net/formulas/get-last-match-cell-contains)

### [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)

The goal is to search through a cell for one of several specified values and return the last match found when one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in column C...

[![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")](https://exceljet.net/formulas/get-first-match-cell-contains)

### [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in...

[![Excel formula: Sum visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_visible_rows_in_a_filtered_list.png "Excel formula: Sum visible rows in a filtered list")](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)

### [Sum visible rows in a filtered list](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)

In this example, the goal is to sum values in rows that are visible and ignore values in rows that are hidden. The range F7:F19 contains 13 values total, 4 of which are hidden by the filter applied to column C. This is a good job for the SUBTOTAL function , which can distinguish between visible and...

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Sum and ignore errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20and%20ignore%20errors.png "Excel formula: Sum and ignore errors")](https://exceljet.net/formulas/sum-and-ignore-errors)

### [Sum and ignore errors](https://exceljet.net/formulas/sum-and-ignore-errors)

In this example, the goal is to create a formula that will sum values in a range that may contain errors. A common problem in Excel is that errors in data show up in the results of other formulas. For example, in the worksheet shown, the SUM function is used to sum the named range data (D5:D15) ...

[![Excel formula: Max value ignore all errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_value_ignore_all_errors.png "Excel formula: Max value ignore all errors")](https://exceljet.net/formulas/max-value-ignore-all-errors)

### [Max value ignore all errors](https://exceljet.net/formulas/max-value-ignore-all-errors)

In this example, the goal is to return the maximum value in a set of data while ignoring any errors that might exist. This problem can be solved with the AGGREGATE function or with the MAXIFS function, as explained below. MAX with errors The standard way to retrieve the maximum value in a range of...

[![Excel formula: Average and ignore errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average%20and%20ignore%20errors2.png "Excel formula: Average and ignore errors")](https://exceljet.net/formulas/average-and-ignore-errors)

### [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)

In this example, the goal is to average a list of values that may contain errors. The values to average are in the named range data (B5:B15). Normally, you can use the AVERAGE function to calculate an average. However, if the data contains errors, AVERAGE will return an error. You can see this in...

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel SUBTOTAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20subtotal%20function.png "Excel SUBTOTAL function")](https://exceljet.net/functions/subtotal-function)

### [SUBTOTAL Function](https://exceljet.net/functions/subtotal-function)

The Excel SUBTOTAL function is designed to run a given calculation on a range of cells while ignoring cells that should not be included. SUBTOTAL can return a SUM, AVERAGE, COUNT, MAX, and others (see complete list below), and SUBTOTAL function can either include or exclude values in hidden...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum visible rows in a filtered list](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
    
*   [Sum and ignore errors](https://exceljet.net/formulas/sum-and-ignore-errors)
    
*   [Max value on given weekday](https://exceljet.net/formulas/max-value-on-given-weekday)
    
*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    
*   [INDEX and MATCH all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)
    
*   [Max value ignore all errors](https://exceljet.net/formulas/max-value-ignore-all-errors)
    
*   [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)
    
*   [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)
    
*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [SUBTOTAL Function](https://exceljet.net/functions/subtotal-function)
    

### Links

*   [Microsoft AGGREGATE function documentation](https://support.office.com/en-us/article/aggregate-function-43b9278e-6aa7-4f17-92b6-e19993fa26df)
    

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
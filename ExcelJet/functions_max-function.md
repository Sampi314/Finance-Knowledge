# Excel MAX function | Exceljet

**Source:** https://exceljet.net/functions/max-function

---

[Skip to main content](https://exceljet.net/functions/max-function#main-content)

[](https://exceljet.net/functions/max-function#)

*   [Previous](https://exceljet.net/functions/linest-function)
    
*   [Next](https://exceljet.net/functions/maxa-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

MAX Function
============

by Dave Bruns · Updated 4 Nov 2025

Related functions 
------------------

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[LARGE](https://exceljet.net/functions/large-function)

[MIN](https://exceljet.net/functions/min-function)

[RANK](https://exceljet.net/functions/rank-function)

[MAXA](https://exceljet.net/functions/maxa-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

![Excel MAX function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")

Summary
-------

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

Purpose 
--------

Get the largest value

Return value 
-------------

The largest value in supplied data

Syntax
------

    =MAX(number1,[number2],...)

*   _number1_ - Number, reference to numeric value, or range that contains numeric values.
*   _number2_ - \[optional\] Number, reference to numeric value, or range that contains numeric values.

Using the MAX function 
-----------------------

The MAX function returns the largest numeric value in the data provided. The MAX function can be used to return the largest value from any type of numeric data. For example, MAX can return the slowest time in a race, the latest date, the largest percentage, the highest temperature, or the top sales number. 

The MAX function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc., up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a range, in any combination. MAX ignores empty cells, text values, and the logical values TRUE and FALSE.

### Basic Example

The MAX function returns the largest numeric value in the supplied data:

    =MAX(12,17,25,11,23) // returns 25
    

When given a [range](https://exceljet.net/glossary/range)
, MAX returns the largest value in the range:

    =MAX(A1:A10) // maximum value in A1:A10

### Mixed arguments

The MAX function can accept a mix of arguments:

    =MAX(5,10)
    =MAX(A1,A2,A3)
    =MAX(A1:A10,100)
    =MAX(A1:A10,C1:C10)
    

### Logical values

The MAX function will _ignore_ logical values and numbers entered as text that appear on the worksheet. However, if such values are provided _directly as arguments_, MAX will use them:

    =MAX(-1,TRUE) // returns 1
    =MAX(-1,TRUE,"3") // returns 3
    

### Errors

When MAX encounters an error in a range, it will return an error. To calculate a maximum value while _ignoring errors_, you can use the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
, which can be configured to ignore errors. See a [detailed example here](https://exceljet.net/formulas/max-value-ignore-all-errors)
.

### Other functions

Excel provides other functions that deal with maximum values and rank:

*   To calculate the maximum value with criteria, use the [MAXIFS function](https://exceljet.net/functions/maxifs-function)
    .
*   To retrieve the nth largest value in a data set, use the [LARGE function](https://exceljet.net/functions/large-function)
    .
*   To determine the rank of a number in a set of data, use the [RANK function](https://exceljet.net/functions/rank-function)
    .

### Notes

*   Arguments can be provided as numbers, names, arrays, or references.
*   MAX accepts up to 255 arguments. If arguments contain no numbers, MAX returns 0.
*   MAX ignores empty cells, text values, and TRUE and FALSE in references.
*   MAX _will_ evaluate numbers as text and logical values supplied directly as arguments.
*   To include logical values in a reference, see the [MAXA function](https://exceljet.net/functions/maxa-function)
    .

MAX function examples
---------------------

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: nth largest without duplicates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_without_duplicates.png "Excel formula: nth largest without duplicates")](https://exceljet.net/formulas/nth-largest-without-duplicates)

### [nth largest without duplicates](https://exceljet.net/formulas/nth-largest-without-duplicates)

In this example, the goal is to retrieve the largest 3 (top 3) values in the named range data , which appears in the range B6:B16. The standard solution to get "nth largest values" is the LARGE function. However, one potential problem with LARGE is that it will return duplicate values if they are...

[![Excel formula: First in last out times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first_in_last_out_time.png "Excel formula: First in last out times")](https://exceljet.net/formulas/first-in-last-out-times)

### [First in last out times](https://exceljet.net/formulas/first-in-last-out-times)

In this problem, the goal is to find the first (earliest) time in and the last (latest) time out for a given name. This is essentially a lookup problem and the solution shown in the worksheet is an example of how you can sometimes use minimum and maximum functions to perform lookups. This works...

[![Excel formula: Get earliest and latest project dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20earliest%20and%20latest%20project%20dates.png "Excel formula: Get earliest and latest project dates")](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)

### [Get earliest and latest project dates](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)

The MINIFS function returns the smallest numeric value that meets supplied criteria, and the MAXIFS function returns the largest numeric value that meets supplied criteria. Like COUNTIFS and SUMIFS, these functions use range/criteria "pairs" to apply conditions. For both formulas, we need just one...

[![Excel formula: Find longest string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_longest_string.png "Excel formula: Find longest string")](https://exceljet.net/formulas/find-longest-string)

### [Find longest string](https://exceljet.net/formulas/find-longest-string)

The goal is to find the longest text string in the range B5:B16. At the core, this is a lookup problem that requires creating a value (the string length) that does not exist in the data as part of the formula. The easiest way to solve this problem is with the XLOOKUP function or the FILTER function...

[![Excel formula: Basic array formula example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20array%20formula%20example.png "Excel formula: Basic array formula example")](https://exceljet.net/formulas/basic-array-formula-example)

### [Basic array formula example](https://exceljet.net/formulas/basic-array-formula-example)

The example on this page shows a simple array formula. Working from the inside out, the expression: C5:C12-D5:D12 Results in an array containing seven values: {17;19;32;25;12;26;29;22} Each number in the array is the result of subtracting the "low" from the "high" in each of the seven rows of data...

[![Excel formula: Lookup last file revision](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20last%20file%20revision.png "Excel formula: Lookup last file revision")](https://exceljet.net/formulas/lookup-last-file-revision)

### [Lookup last file revision](https://exceljet.net/formulas/lookup-last-file-revision)

Context In this example, we have a number of file versions listed in a table with a date and user name. Note that file names are repeated, except for the code appended at the end to represent version ("CA", "CB", "CC", "CD", etc.). For a given file, we want to locate the position (row number) for...

[![Excel formula: Position of max value in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/position%20of%20max%20value%20in%20list.png "Excel formula: Position of max value in list")](https://exceljet.net/formulas/position-of-max-value-in-list)

### [Position of max value in list](https://exceljet.net/formulas/position-of-max-value-in-list)

In this formula, the goal is to return the numeric position of the most expensive property in the list. The formula in cell I5 is: =MATCH(MAX(C3:C11),C3:C11,0) The MAX function extracts the maximum value from the range C3:C11. In this case, that value is 849900. This number is then supplied to the...

[![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value.png "Excel formula: Maximum value")](https://exceljet.net/formulas/maximum-value)

### [Maximum value](https://exceljet.net/formulas/maximum-value)

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below. MAX function The MAX function accepts...

[![Excel formula: Odometer gas mileage log](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/odometer%20gas%20mileage%20log.png "Excel formula: Odometer gas mileage log")](https://exceljet.net/formulas/odometer-gas-mileage-log)

### [Odometer gas mileage log](https://exceljet.net/formulas/odometer-gas-mileage-log)

Note: this example assumes that fuel is added to capacity at each gas stop, in order to calculate miles per gallon (MPG) based on the miles driven and fuel used since the last stop. In addition, this example keeps all data in an Excel Table called "data" to illustrate how Tables can make some...

[![Excel formula: Larger of two values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/larger_of_two_values.png "Excel formula: Larger of two values")](https://exceljet.net/formulas/larger-of-two-values)

### [Larger of two values](https://exceljet.net/formulas/larger-of-two-values)

In this example, the goal is to return the greater of two values which appear in columns B and C. Although this problem could be solved with the IF function (see below), the simplest solution is to use the MAX function. MAX function The MAX function returns the largest numeric value in the data...

[![Excel formula: Max by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_by_month.png "Excel formula: Max by month")](https://exceljet.net/formulas/max-by-month)

### [Max by month](https://exceljet.net/formulas/max-by-month)

In this example, the goal is to get the maximum value in the data for each month listed in column E. The easiest way to do this is with the MAXIFS function, which is designed to return a maximum value based on one or more criteria. In older versions of Excel without the MAXIFS function, you can use...

[![Excel formula: Max value with variable column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max%20value%20with%20variable%20column.png "Excel formula: Max value with variable column")](https://exceljet.net/formulas/max-value-with-variable-column)

### [Max value with variable column](https://exceljet.net/formulas/max-value-with-variable-column)

Note: If you are new to INDEX and MATCH, see: How to use INDEX and MATCH In a standard configuration, the INDEX function retrieves a value at a given row and column. For example, to get the value at row 2 and column 3 in a given range: =INDEX(range,2,3) // get value at row 2, column 3 However,...

[![Excel formula: Max if criteria match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max%20if%20criteria%20match.png "Excel formula: Max if criteria match")](https://exceljet.net/formulas/max-if-criteria-match)

### [Max if criteria match](https://exceljet.net/formulas/max-if-criteria-match)

The example shown contains almost 10,000 rows of data. The data represents temperature readings taken every 2 minutes over a period of days. For any given date (provided in cell H7), we want to get the maximum temperature on that date. Inside the IF function , logical test is entered as B5:B9391=H7...

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

MAX function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Structured%20reference%20syntax%20examples-Thumb.png)](https://exceljet.net/videos/structured-reference-syntax-examples)

### [Structured reference syntax examples](https://exceljet.net/videos/structured-reference-syntax-examples)

In this video, we'll look at the syntax used in a variety of structured references. Structured references are used to refer to Excel tables in formulas. The syntax for structured references allows you to precisely target different parts of the table. Let's walk through some examples. All these...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20named%20range-thumb.png)](https://exceljet.net/videos/how-to-create-a-named-range)

### [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)

Named ranges are one of the most useful features in Excel. They make your formulas much easier to read and understand; they automatically give you absolute references , and they reduce errors. Let's take a look at a few ways to create named ranges. The simplest way to create a named range is to use...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20maximum%20and%20minimum%20values-thumb.png)](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

### [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

In this video we'll look at how to calculate minimum and maximum values in Excel. Let's take a look. Here we have a list of properties, that includes an address, a price, and a variety of other information. Let's calculate the maximum and minimum values in this list. First, I'm going to create a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20a%20dynamic%20named%20range-thumb.png)](https://exceljet.net/videos/what-is-a-dynamic-named-range)

### [What is a dynamic named range](https://exceljet.net/videos/what-is-a-dynamic-named-range)

In this video we'll introduce the idea of a dynamic range and show you why you might want to use one. Let's take a look. In this first worksheet, we have a list of ten properties set up in a normal way. If we check the formulas that summarize this data to the right, you can see that each formula...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20a%20named%20range%20to%20an%20existing%20formula-thumb.png)](https://exceljet.net/videos/how-to-apply-a-named-range-to-an-existing-formula)

### [How to apply a named range to an existing formula](https://exceljet.net/videos/how-to-apply-a-named-range-to-an-existing-formula)

Sometimes you might create named ranges after you've already built formulas. In that case, Excel will not automatically update the formulas to use the named ranges. However, there are a couple of ways you can apply named ranges to formulas that already exist. Let's take a look. Here we have a table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/3%20Basic%20Array%20Formulas-Play.png)](https://exceljet.net/videos/3-basic-array-formulas)

### [3 basic array formulas](https://exceljet.net/videos/3-basic-array-formulas)

In this video we'll look at three basic array formula examples. The latest version of Excel ships with new functions like UNIQUE , SORT, FILTER and so on that make certain array formulas easy. But you can still build traditional array formulas as well, and they can solve some tricky problems. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20dynamic%20chart_thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)

### [How to build a simple dynamic chart](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)

In this video, we'll look at how to build a simple dynamic chart in Excel. First, let's look at the problem we're trying to solve. Here we have monthly sales data. At the moment, we only have 5 months, but we'll be adding more data over time. Now, if I insert a column chart, everything works fine...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Create%20a%20dynamic%20reference%20to%20a%20worksheet-thumb.png)](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)

### [Create a dynamic reference to a worksheet](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)

In this video we'll look at how to create a dynamic reference to a worksheet in a formula. Sometimes you want to reference a worksheet dynamically in a formula, so it can be easily changed. In this workbook we have five weeks of test scores, each in the same format. Let's assume we want to build a...

Related functions
-----------------

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel MAXA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxa%20function.png "Excel MAXA function")](https://exceljet.net/functions/maxa-function)

### [MAXA Function](https://exceljet.net/functions/maxa-function)

The Excel MAXA function returns the largest numeric value in a range of values. The MAXA function ignores empty cells, but evaluates the logical values TRUE and FALSE as 1 and 0, and evaluates text as zero.

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    
*   [Basic array formula example](https://exceljet.net/formulas/basic-array-formula-example)
    
*   [XLOOKUP latest by date](https://exceljet.net/formulas/xlookup-latest-by-date)
    
*   [Count consecutive monthly orders](https://exceljet.net/formulas/count-consecutive-monthly-orders)
    
*   [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)
    
*   [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)
    
*   [Convert negative numbers to zero](https://exceljet.net/formulas/convert-negative-numbers-to-zero)
    
*   [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)
    
*   [Find longest string](https://exceljet.net/formulas/find-longest-string)
    
*   [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)
    

### Videos

*   [What is a dynamic named range](https://exceljet.net/videos/what-is-a-dynamic-named-range)
    
*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    
*   [How to apply a named range to an existing formula](https://exceljet.net/videos/how-to-apply-a-named-range-to-an-existing-formula)
    
*   [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)
    
*   [Create a dynamic reference to a worksheet](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)
    
*   [How to build a simple dynamic chart](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    
*   [Structured reference syntax examples](https://exceljet.net/videos/structured-reference-syntax-examples)
    
*   [3 basic array formulas](https://exceljet.net/videos/3-basic-array-formulas)
    

### Functions

*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [MAXA Function](https://exceljet.net/functions/maxa-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    

### Links

*   [Microsoft MAX function documentation](https://support.office.com/en-us/article/max-function-e0012414-9ac8-4b34-9a47-73e662c08098)
    

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
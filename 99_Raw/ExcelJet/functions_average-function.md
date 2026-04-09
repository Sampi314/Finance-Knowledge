# Excel AVERAGE function | Exceljet

**Source:** https://exceljet.net/functions/average-function

---

[Skip to main content](https://exceljet.net/functions/average-function#main-content)

[](https://exceljet.net/functions/average-function#)

*   [Previous](https://exceljet.net/functions/avedev-function)
    
*   [Next](https://exceljet.net/functions/averagea-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

AVERAGE Function
================

by Dave Bruns · Updated 6 Nov 2021

Related functions 
------------------

[MEDIAN](https://exceljet.net/functions/median-function)

[MODE](https://exceljet.net/functions/mode-function)

[AVERAGEA](https://exceljet.net/functions/averagea-function)

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")

Summary
-------

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

Purpose 
--------

Get the average of a group of numbers

Return value 
-------------

A number representing the average.

Syntax
------

    =AVERAGE(number1,[number2],...)

*   _number1_ - A number or cell reference that refers to numeric values.
*   _number2_ - \[optional\] A number or cell reference that refers to numeric values.

Using the AVERAGE function 
---------------------------

The AVERAGE function calculates the average of numbers provided as [arguments](https://exceljet.net/glossary/function-argument)
. To calculate the average, Excel sums all numeric values and divides by the count of numeric values.

AVERAGE takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can include numbers, cell references, ranges, arrays, and constants. Empty cells, and cells that contain text or logical values are ignored. However, zero (0) values are included. You can ignore zero (0) values with the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
, as explained below.

The AVERAGE function will ignore logical values and numbers entered as text. If you need to include these values in the average, see the [AVERAGEA function](https://exceljet.net/functions/averagea-function)
.

If the values given to AVERAGE contain errors, AVERAGE returns an error. You can use the [AGGREGATE function to ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)
.

### Basic usage

A typical way to use the AVERAGE function is to provide a [range](https://exceljet.net/glossary/range)
, as seen below. The formula in F3, copied down, is:

    =AVERAGE(C3:E3)
    

![AVERAGE function basic usage](https://exceljet.net/sites/default/files/images/functions/inline/average%20function%20basic%20usage.png "AVERAGE function basic usage")

At each new row, AVERAGE calculates an average of the quiz scores for each person.

### Blank cells

The AVERAGE function automatically ignores blank cells. In the screen below, notice cell C4 is empty, and AVERAGE simply ignores it and computes an average with B4 and D4 only:

![AVERAGE function with blank cells](https://exceljet.net/sites/default/files/images/functions/inline/average%20function%20blank%20cells.png "AVERAGE function with blank cells")

However, note the zero (0) value in C5 _is included_ in the average, since it is a valid numeric value. To exclude zero values, use [AVERAGEIF](https://exceljet.net/functions/averageif-function)
 or [AVERAGEIFS](https://exceljet.net/functions/averageifs-function)
 instead. In the example below,  AVERAGEIF is used to exclude zero values. Like the AVERAGE function, AVERAGEIF _automatically excludes_ empty cells.

    =AVERAGEIF(B3:D3,">0") // exclude zero
    

![AVERAGEIF function exclude zero](https://exceljet.net/sites/default/files/images/functions/inline/averageif%20function%20exclude%20zero.png "AVERAGEIF function exclude zero")

### Mixed arguments

The numbers provided to AVERAGE can be a mix of references and constants:

![AVERAGE function with mixed arguments](https://exceljet.net/sites/default/files/images/functions/inline/average%20function%20mixed%20arguments.png "AVERAGE function with mixed arguments")

    =AVERAGE(A1,A2,4) // returns 3
    

### Average with criteria

To calculate an average with criteria, use [AVERAGEIF](https://exceljet.net/functions/averageif-function)
 or [AVERAGEIFS](https://exceljet.net/functions/averageifs-function)
. In the example below, AVERAGEIFS is used to calculate the average score for Red and Blue groups:

![AVERAGEIFS function with criteria](https://exceljet.net/sites/default/files/images/functions/inline/averageifs%20function%20with%20criteria.png "AVERAGEIFS function with criteria")

    =AVERAGEIFS(C5:C14,D5:D14,"red") // red average
    =AVERAGEIFS(C5:C14,D5:D14,"blue") // blue average
    

The AVERAGEIFS function can also [apply multiple criteria](https://exceljet.net/formulas/average-with-multiple-criteria)
.

### Average top 3

By combining the AVERAGE function with the [LARGE function](https://exceljet.net/functions/large-function)
, you can calculate an average of top n values. In the example below, the formula in column I computes an average of the top 3 quiz scores in each row:

![AVERAGE function top 3](https://exceljet.net/sites/default/files/images/functions/inline/AVERAGE%20function%20top%203.png "AVERAGE function top 3")

[Detailed explanation here](https://exceljet.net/formulas/average-top-3-scores)
.

### Weighted average

To calculate a _weighted_ average, you'll want to use the SUMPRODUCT function, as shown below:

![Weighted average with SUMPRODUCT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/excel%20weighted%20average.png?itok=Xjs4yV-i "Weighted average with SUMPRODUCT")

[Read a complete explanation here](https://exceljet.net/formulas/weighted-average)
.

### Average without #DIV/0!

The average function automatically ignores empty cells in a set of data. However, if the range contains no numeric values, AVERAGE will return a #DIV/0! error. To avoid this problem, you can check the count of values with the [COUNT function](https://exceljet.net/functions/count-function)
 and the [IF function](https://exceljet.net/videos/the-if-function)
 like this:

    =IF(COUNT(range)>0,AVERAGE(range),"") // check count first
    

When the count of numeric values is zero, IF returns an empty string (""). When the count is greater than zero, AVERAGE returns the average. [This example](https://exceljet.net/formulas/only-calculate-if-not-blank)
 explains this idea in more detail.

### Manual average

To calculate the average, AVERAGE sums all numeric values and divides by the count of numeric values. This behavior can be replicated with the [SUM](https://exceljet.net/functions/sum-function)
 and [COUNT](https://exceljet.net/functions/count-function)
 functions manually like this:

    =SUM(range)/COUNT(range) // manual average calculation
    

### Notes

*   AVERAGE automatically ignores empty cells and cells with text values.
*   AVERAGE includes zero values. Use AVERAGEIF or AVERAGEIFS [to ignore zero values](https://exceljet.net/formulas/average-numbers-ignore-zero)
    .
*   Arguments can be supplied as constants, ranges, [named ranges](https://exceljet.net/glossary/named-range)
    , or cell references.
*   AVERAGE can handle up to 255 total arguments.
*   To see a quick average _without a formula_, you can [use the status bar](https://exceljet.net/videos/how-to-use-the-status-bar-for-quick-calculations)
    .

AVERAGE function examples
-------------------------

[![Excel formula: Average last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_5_columns.png "Excel formula: Average last n columns")](https://exceljet.net/formulas/average-last-n-columns)

### [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)

In this example, the goal is to average the last n columns in a set of data, where n is a variable entered in cell K5 that can be changed at any time. Since more data may be added, a key requirement is to average amounts by position. For convenience, the values to average are in the named range...

[![Excel formula: Average if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_if_not_blank.png "Excel formula: Average if not blank")](https://exceljet.net/formulas/average-if-not-blank)

### [Average if not blank](https://exceljet.net/formulas/average-if-not-blank)

In this example, the goal is to average the Prices in C5:C16 when the Group in D5:D16 is not blank (i.e. not empty). The traditional way to solve this problem is to use the AVERAGEIFS function . However, you can also use the FILTER function with the AVERAGE function , as explained below. Because...

[![Excel formula: Average call time per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_call_time_per_month.png "Excel formula: Average call time per month")](https://exceljet.net/formulas/average-call-time-per-month)

### [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)

In this example, the goal is to calculate the average call time (duration in minutes) for each month listed in column G using the dates in column B and the durations in column E. The article below explains two approaches. The first formula is based on the AVERAGEIFS function , which is designed to...

[![Excel formula: Weighted average](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/weighted_average.png "Excel formula: Weighted average")](https://exceljet.net/formulas/weighted-average)

### [Weighted average](https://exceljet.net/formulas/weighted-average)

In this example, the goal is to calculate a weighted average of scores for each name in the table using the weights that appear in the named range weights (I5:K5) and the scores in columns C through E. A weighted average (also called a weighted mean ) is an average where some values are more...

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: Average if with filter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Average_if_with_filter.png "Excel formula: Average if with filter")](https://exceljet.net/formulas/average-if-with-filter)

### [Average if with filter](https://exceljet.net/formulas/average-if-with-filter)

In this example, the goal is to calculate an average for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. For convenience only, data (C5:E16) and group (B5:B16) are named ranges . In the article below, we look at several approaches to this problem: Why the...

[![Excel formula: Average and ignore errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average%20and%20ignore%20errors2.png "Excel formula: Average and ignore errors")](https://exceljet.net/formulas/average-and-ignore-errors)

### [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)

In this example, the goal is to average a list of values that may contain errors. The values to average are in the named range data (B5:B15). Normally, you can use the AVERAGE function to calculate an average. However, if the data contains errors, AVERAGE will return an error. You can see this in...

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

[![Excel formula: Moving average formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/moving%20average%20formula.png "Excel formula: Moving average formula")](https://exceljet.net/formulas/moving-average-formula)

### [Moving average formula](https://exceljet.net/formulas/moving-average-formula)

The formulas shown in the example all use the AVERAGE function with a relative reference set up for each specific interval. The 3-day moving average in E7 is calculated by feeding AVERAGE a range that includes the current day and the two previous days like this: =AVERAGE(C5:C7) // 3-day average The...

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

[![Excel formula: Coefficient of variation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/coefficient%20of%20variation.png "Excel formula: Coefficient of variation")](https://exceljet.net/formulas/coefficient-of-variation)

### [Coefficient of variation](https://exceljet.net/formulas/coefficient-of-variation)

The coefficient of variation measures the relative variability of data with respect to the mean. It represents a ratio of the standard deviation to the mean and can be a useful way to compare data series when means are different. It is sometimes called relative standard deviation (RSD). In this...

[![Excel formula: Average last N values in a table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Average%20last%20N%20values%20in%20a%20table.png "Excel formula: Average last N values in a table")](https://exceljet.net/formulas/average-last-n-values-in-a-table)

### [Average last N values in a table](https://exceljet.net/formulas/average-last-n-values-in-a-table)

This formula is a good example of how structured references can make working with data in Excel much easier. At the core, this is what we're doing: =AVERAGE(first:last) where "first" is a reference to the first cell to include in the average and "last" is a reference to the last cell to include...

[![Excel formula: Average by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_month.png "Excel formula: Average by month")](https://exceljet.net/formulas/average-by-month)

### [Average by month](https://exceljet.net/formulas/average-by-month)

In this example, the goal is to calculate a monthly average for the amounts shown in column C using the dates in column B. The article below explains two approaches. One approach is based on the AVERAGEIFS function , which is designed to calculate averages using multiple criteria. The second...

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

AVERAGE function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Create%20a%20dynamic%20reference%20to%20a%20named%20range-thumb.png)](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)

### [Create a dynamic reference to a named range](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)

In this video we'll look at how to create a dynamic reference to a named range using the INDIRECT function . Let's take a look. Here we have a simple table that summarizes sales by salesperson over a four-month period. What we're going to do is use the INDIRECT function to make a dynamic reference...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20an%20average%20value-thumb.png)](https://exceljet.net/videos/how-to-calculate-an-average-value)

### [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)

In this video we'll look at how to calculate an average value. Let's take a look. In this worksheet we have a list of 16 properties, each with a price and other information. Let's calculate an average price. First, I'll create a named range for the prices. This makes the formulas easier to read and...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20a%20dynamic%20named%20range-thumb.png)](https://exceljet.net/videos/what-is-a-dynamic-named-range)

### [What is a dynamic named range](https://exceljet.net/videos/what-is-a-dynamic-named-range)

In this video we'll introduce the idea of a dynamic range and show you why you might want to use one. Let's take a look. In this first worksheet, we have a list of ten properties set up in a normal way. If we check the formulas that summarize this data to the right, you can see that each formula...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20rank%20values%20with%20the%20RANK%20function.png)](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)

### [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)

In this video we'll look at how to rank values in ascending or descending order using the RANK function . Here we have a table that contains five test scores for a group of students and an average score in Column I. How can we rank these students from highest to lowest scores? Well, one option is...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20a%20Table-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)

### [How to create a dynamic named range with a Table](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)

In this video we'll look at how to create a dynamic named range with a Table. This is the simplest way to create a dynamic named range in Excel. This table contains data for ten properties. I can easily create a named range for this data. For example, I can create a range called "data." Then, using...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Create%20a%20dynamic%20reference%20to%20a%20worksheet-thumb.png)](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)

### [Create a dynamic reference to a worksheet](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)

In this video we'll look at how to create a dynamic reference to a worksheet in a formula. Sometimes you want to reference a worksheet dynamically in a formula, so it can be easily changed. In this workbook we have five weeks of test scores, each in the same format. Let's assume we want to build a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%203d%20references-thumb.png)](https://exceljet.net/videos/how-to-create-3d-references)

### [How to create 3D references](https://exceljet.net/videos/how-to-create-3d-references)

Sometimes in Excel you may want to reference a large number of sheets that have the same structure. In this case, you can use a special trick called a "3D reference". Here are the test scores we looked at earlier. The Summary sheet is pulling in the results from Week1 through Week5. Suppose we want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageif-function)

### [How to use the AVERAGEIF function](https://exceljet.net/videos/how-to-use-the-averageif-function)

In this video, we'll look at how to use the AVERAGEIF function to calculate an average from numbers that meet a single criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the conditions listed in column K. The AVERAGEIF function...

Related functions
-----------------

[![Excel MEDIAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20median%20function.png "Excel MEDIAN function")](https://exceljet.net/functions/median-function)

### [MEDIAN Function](https://exceljet.net/functions/median-function)

The Excel MEDIAN function returns the median (middle number) in the supplied set of data. For example, =MEDIAN(1,2,3,4,5) returns 3.

[![Excel MODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")](https://exceljet.net/functions/mode-function)

### [MODE Function](https://exceljet.net/functions/mode-function)

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

[![Excel AVERAGEA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20averagea%20function.png "Excel AVERAGEA function")](https://exceljet.net/functions/averagea-function)

### [AVERAGEA Function](https://exceljet.net/functions/averagea-function)

The Excel AVERAGEA function returns the average of a set of supplied values. Unlike AVERAGE, AVERAGEA will also evaluate the logical values TRUE and FALSE, and numbers represented as text, whereas AVERAGE ignores these values during calculation

[![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")](https://exceljet.net/functions/averageif-function)

### [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [Average if with filter](https://exceljet.net/formulas/average-if-with-filter)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    
*   [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)
    
*   [Coefficient of variation](https://exceljet.net/formulas/coefficient-of-variation)
    
*   [Average last N values in a table](https://exceljet.net/formulas/average-last-n-values-in-a-table)
    
*   [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)
    
*   [Average call time per month](https://exceljet.net/formulas/average-call-time-per-month)
    
*   [Average by month](https://exceljet.net/formulas/average-by-month)
    
*   [Moving average formula](https://exceljet.net/formulas/moving-average-formula)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
*   [How to create a dynamic named range with a Table](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)
    
*   [What is a dynamic named range](https://exceljet.net/videos/what-is-a-dynamic-named-range)
    
*   [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)
    
*   [How to use the AVERAGEIF function](https://exceljet.net/videos/how-to-use-the-averageif-function)
    
*   [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)
    
*   [Create a dynamic reference to a named range](https://exceljet.net/videos/create-a-dynamic-reference-to-a-named-range)
    
*   [Create a dynamic reference to a worksheet](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)
    
*   [How to create 3D references](https://exceljet.net/videos/how-to-create-3d-references)
    

### Functions

*   [MEDIAN Function](https://exceljet.net/functions/median-function)
    
*   [MODE Function](https://exceljet.net/functions/mode-function)
    
*   [AVERAGEA Function](https://exceljet.net/functions/averagea-function)
    
*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    

### Links

*   [Microsoft AVERAGE function documentation](https://support.office.com/en-us/article/average-function-047bac88-d466-426c-a32b-8f33eb960cf6)
    

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
# Excel MIN function | Exceljet

**Source:** https://exceljet.net/functions/min-function

---

[Skip to main content](https://exceljet.net/functions/min-function#main-content)

[](https://exceljet.net/functions/min-function#)

*   [Previous](https://exceljet.net/functions/median-function)
    
*   [Next](https://exceljet.net/functions/mina-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

MIN Function
============

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[MINIFS](https://exceljet.net/functions/minifs-function)

[SMALL](https://exceljet.net/functions/small-function)

[RANK](https://exceljet.net/functions/rank-function)

[MINA](https://exceljet.net/functions/mina-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

![Excel MIN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")

Summary
-------

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Purpose 
--------

Get the smallest value.

Return value 
-------------

The smallest value in supplied data

Syntax
------

    =MIN(number1,[number2],...)

*   _number1_ - Number, reference to numeric value, or range that contains numeric values.
*   _number2_ - \[optional\] Number, reference to numeric value, or range that contains numeric values.

Using the MIN function 
-----------------------

The MIN function returns the smallest numeric value in the data provided. The MIN function can be used to return the smallest value from any type of numeric data. For example, MIN can return the fastest time in a race, the earliest date, the smallest percentage, the lowest temperature, or the bottom sales number. 

The MIN function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a [cell reference](https://exceljet.net/videos/what-is-a-cell-reference)
, or a [range](https://exceljet.net/glossary/range)
, in any combination. MIN ignores empty cells, [text values](https://exceljet.net/glossary/text-value)
, and the logical values TRUE and FALSE.

### Basic example

The MIN function returns the smallest numeric value in supplied data:

    =MIN(12,17,25,11,23) // returns 11
    

When given a [range](https://exceljet.net/glossary/range)
, MIN returns the smallest value in the range:

    =MIN(A1:A10) // minimum value in A1:A10

### Mixed arguments

The MIN function can accept a mix of arguments:

    =MIN(5,10)
    =MIN(A1,A2,A3)
    =MIN(A1:A10,1)
    =MIN(A1:A10,C1:C10)
    

### Logical values

The MIN function will _ignore_ logical values and numbers entered as text that appear on the worksheet. However, if such values are provided _directly as arguments_, MIN will use them:

    =MIN(5,TRUE) // returns 1
    =MIN(7,5,"3") // returns 3
    

### Errors

When MIN encounters an error in a range, it will return an error. To calculate a minimum value while ignoring errors, you can use the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
, which can be configured to ignore errors.

### Other functions

Excel provides other functions that deal with minimum values and rank:

*   To calculate the minimum value with criteria, use the [MINIFS function](https://exceljet.net/functions/minifs-function)
    .
*   To retrieve the nth smallest value in a data set, use the [SMALL function](https://exceljet.net/functions/small-function)
    .
*   To determine the rank of a number in a set of data, use the [RANK function](https://exceljet.net/functions/rank-function)
    .

### Notes

*   Arguments can be provided as numbers, names, arrays, or references.
*   MIN accepts up to 255 arguments. If arguments contain no numbers, MIN returns 0.
*   MIN ignores empty cells, text values, and TRUE and FALSE in references.
*   MIN _will_ evaluate numbers as text and logical values supplied directly as arguments.
*   To include logical values in a reference, see the [MINA function](https://exceljet.net/functions/mina-function)
    .

MIN function examples
---------------------

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Timesheet overtime calculation formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20overtime%20calculation.png "Excel formula: Timesheet overtime calculation formula")](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

### [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

Note: it's important to understand that Excel deals with time as fractions of a day . So, 12:00 PM is .5, 6:00 AM is .25, 6 PM is .75, and so on. This works fine for standard time and date calculations, but in many cases you'll want to convert times to decimal hours to make other calculations more...

[![Excel formula: Basic array formula example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20array%20formula%20example.png "Excel formula: Basic array formula example")](https://exceljet.net/formulas/basic-array-formula-example)

### [Basic array formula example](https://exceljet.net/formulas/basic-array-formula-example)

The example on this page shows a simple array formula. Working from the inside out, the expression: C5:C12-D5:D12 Results in an array containing seven values: {17;19;32;25;12;26;29;22} Each number in the array is the result of subtracting the "low" from the "high" in each of the seven rows of data...

[![Excel formula: Odometer gas mileage log](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/odometer%20gas%20mileage%20log.png "Excel formula: Odometer gas mileage log")](https://exceljet.net/formulas/odometer-gas-mileage-log)

### [Odometer gas mileage log](https://exceljet.net/formulas/odometer-gas-mileage-log)

Note: this example assumes that fuel is added to capacity at each gas stop, in order to calculate miles per gallon (MPG) based on the miles driven and fuel used since the last stop. In addition, this example keeps all data in an Excel Table called "data" to illustrate how Tables can make some...

[![Excel formula: Lookup lowest Monday tide](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20lowest%20monday%20tide.png "Excel formula: Lookup lowest Monday tide")](https://exceljet.net/formulas/lookup-lowest-monday-tide)

### [Lookup lowest Monday tide](https://exceljet.net/formulas/lookup-lowest-monday-tide)

At a high level, this example is about finding a minimum value based on multiple criteria. To do that, we are using the MIN function together with two nested IF functions : {=MIN(IF(day=I5,IF(tide="L",pred)))} working from the inside out, the first IF checks if the day is "Mon", based on the value...

[![Excel formula: Get nth match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match.png "Excel formula: Get nth match")](https://exceljet.net/formulas/get-nth-match)

### [Get nth match](https://exceljet.net/formulas/get-nth-match)

The goal is to retrieve the nth matching record in a set of data, after filtering on a specific product. In the worksheet shown, the product in H4 and the value for n in H5 are inputs that can be changed at any time. For instance, if the product in H4 is "A" and the value in H5 is 3, the formula...

[![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value.png "Excel formula: Minimum value")](https://exceljet.net/formulas/minimum-value)

### [Minimum value](https://exceljet.net/formulas/minimum-value)

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below. MIN function The MIN function...

[![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")](https://exceljet.net/formulas/last-row-number-in-range)

### [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range: {5;6;7;8;9;10} To get the first row number in a range, we use the MIN...

[![Excel formula: Get earliest and latest project dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20earliest%20and%20latest%20project%20dates.png "Excel formula: Get earliest and latest project dates")](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)

### [Get earliest and latest project dates](https://exceljet.net/formulas/get-earliest-and-latest-project-dates)

The MINIFS function returns the smallest numeric value that meets supplied criteria, and the MAXIFS function returns the largest numeric value that meets supplied criteria. Like COUNTIFS and SUMIFS, these functions use range/criteria "pairs" to apply conditions. For both formulas, we need just one...

[![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")](https://exceljet.net/formulas/find-closest-match)

### [Find closest match](https://exceljet.net/formulas/find-closest-match)

In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the XLOOKUP function . However in older versions of Excel without the XLOOKUP function...

[![Excel formula: Cap percentage between 0 and 100](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20between%200%20and%20100.png "Excel formula: Cap percentage between 0 and 100")](https://exceljet.net/formulas/cap-percentage-between-0-and-100)

### [Cap percentage between 0 and 100](https://exceljet.net/formulas/cap-percentage-between-0-and-100)

In order to understand this problem, make sure you understand how percentage number formatting works . In a nutshell, percentages are decimal values: 0.1 is 10%, 0.2 is 20%, and so on. The number 1, when formatted as a percentage, is 100%. More on number formats here . The goal of this example is...

[![Excel formula: First row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20row%20in%20range.png "Excel formula: First row number in range")](https://exceljet.net/formulas/first-row-number-in-range)

### [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range that contains multiple rows, the ROW function will return an array that contains all row numbers for the range. In the example shown the array looks like this: {5;6;7;8;9;10}...

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Smaller of two values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/smaller_of_two_values.png "Excel formula: Smaller of two values")](https://exceljet.net/formulas/smaller-of-two-values)

### [Smaller of two values](https://exceljet.net/formulas/smaller-of-two-values)

In this example, the goal is to return the smaller of two values which appear in columns B and C. Although this problem could be solved with the IF function (see below), the simplest solution is to use the MIN function. MIN function The MIN function returns the smallest numeric value in the data...

[![Excel formula: Cap percentage at specific amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20specific%20amount.png "Excel formula: Cap percentage at specific amount")](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

### [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

This formula uses the MIN function to make a decision that might otherwise be handled with the IF function . Although MIN is usually used to return the minimum value in a data set with many numbers, it also works fine for the "lesser of the two" situations. Inside MIN, the value in C6 is multiplied...

MIN function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20dynamic%20chart_thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)

### [How to build a simple dynamic chart](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)

In this video, we'll look at how to build a simple dynamic chart in Excel. First, let's look at the problem we're trying to solve. Here we have monthly sales data. At the moment, we only have 5 months, but we'll be adding more data over time. Now, if I insert a column chart, everything works fine...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Simplified%20formula%20example%20401k%20Match-thumb.png)](https://exceljet.net/videos/simplified-formula-example-401k-match)

### [Simplified formula example 401k Match](https://exceljet.net/videos/simplified-formula-example-401k-match)

In this video we'll look at how to simplify some formulas we created in a previous video by replacing IF statements with the MIN function and a bit of Boolean logic. Make sure you watch the first video if you haven't already. In the example we have formulas that calculate a company match for an...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Create%20a%20dynamic%20reference%20to%20a%20worksheet-thumb.png)](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)

### [Create a dynamic reference to a worksheet](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)

In this video we'll look at how to create a dynamic reference to a worksheet in a formula. Sometimes you want to reference a worksheet dynamically in a formula, so it can be easily changed. In this workbook we have five weeks of test scores, each in the same format. Let's assume we want to build a...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel MINA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mina%20function.png "Excel MINA function")](https://exceljet.net/functions/mina-function)

### [MINA Function](https://exceljet.net/functions/mina-function)

The Excel MINA function returns the smallest numeric value in a range of values. The MINA function ignores empty cells, but evaluates the logical values TRUE and FALSE as 1 and 0, and evaluates text as zero when these values appear in a [range](https://exceljet.net/glossary/range)
 or cell reference.

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

*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Lookup lowest Monday tide](https://exceljet.net/formulas/lookup-lowest-monday-tide)
    
*   [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)
    
*   [Smaller of two values](https://exceljet.net/formulas/smaller-of-two-values)
    
*   [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Lookup lowest value](https://exceljet.net/formulas/lookup-lowest-value)
    
*   [Odometer gas mileage log](https://exceljet.net/formulas/odometer-gas-mileage-log)
    
*   [Calculate date overlap in days](https://exceljet.net/formulas/calculate-date-overlap-in-days)
    
*   [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)
    

### Videos

*   [What is a dynamic named range](https://exceljet.net/videos/what-is-a-dynamic-named-range)
    
*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    
*   [How to apply a named range to an existing formula](https://exceljet.net/videos/how-to-apply-a-named-range-to-an-existing-formula)
    
*   [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)
    
*   [Create a dynamic reference to a worksheet](https://exceljet.net/videos/create-a-dynamic-reference-to-a-worksheet)
    
*   [Simplified formula example 401k Match](https://exceljet.net/videos/simplified-formula-example-401k-match)
    
*   [How to build a simple dynamic chart](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [MINA Function](https://exceljet.net/functions/mina-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    

### Links

*   [Microsoft MIN function documentation](https://support.office.com/en-us/article/min-function-61635d12-920f-4ce2-a70f-96f202dcc152)
    

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
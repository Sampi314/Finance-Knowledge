# Average and ignore errors - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-and-ignore-errors

---

[Skip to main content](https://exceljet.net/formulas/average-and-ignore-errors#main-content)

[](https://exceljet.net/formulas/average-and-ignore-errors#)

*   [Previous](https://exceljet.net/formulas/sumproduct-with-if)
    
*   [Next](https://exceljet.net/formulas/average-by-group)
    

[Average](https://exceljet.net/formulas#Average)

Average and ignore errors
=========================

by Dave Bruns · Updated 28 Jan 2023

Related functions 
------------------

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[FILTER](https://exceljet.net/functions/filter-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6883/download?token=mRAyJTHG)
 (14.51 KB)

![Excel formula: Average and ignore errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average%20and%20ignore%20errors2.png "Excel formula: Average and ignore errors")

Summary
-------

To average values in a range while ignoring any errors that may exist, you can use the [AVERAGEIF](https://exceljet.net/functions/averageif-function)
 or [AGGREGATE](https://exceljet.net/functions/aggregate-function)
 function, as described below. In the example shown, the formula in E6 is:

    =AGGREGATE(1,6,data)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

Generic formula
---------------

    =AGGREGATE(1,6,data)

Explanation 
------------

In this example, the goal is to average a list of values that may contain errors. The values to average are in the [named range](https://exceljet.net/glossary/named-range)
 **data** (B5:B15). Normally, you can use the [AVERAGE function](https://exceljet.net/functions/average-function)
 to calculate an average. However, if the data contains errors, AVERAGE will return an error. You can see this in cell E5, which contains the average function:

    =AVERAGE(data) // returns #N/A
    

This happens because B9 and B13 contain the #N/A errors, and this is a common problem in Excel: errors in the data tend to percolate up to summary calculations.

### AVERAGEIF

One way to work around this problem is to use the [AVERAGEIF function](https://exceljet.net/functions/averageif-function)
, which can apply a condition to filter values in a range before they are averaged. For example, to specifically ignore #N/A errors, you can configure AVERAGEIF like this:

    =AVERAGEIF(data,"<>#N/A") // ignore #N/A errors
    

In the worksheet shown, this is the formula in cell E8. This works fine as long as the data contains only #N/A errors, but it will fail if there are other errors in the data. Another option with AVERAGEIF is to select only numbers that are greater than or equal to zero:

    =AVERAGEIF(data,">=0") // zero or greater
    

This is the formula in E7. This simple formula works fine, as long as the numbers to average are not negative.

### AGGREGATE

The simplest and most robust way to ignore errors when calculating an average is to use the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
. In cell E6, AGGREGATE is configured to average and ignore errors by setting _function\_num_ to 1, and _options_ to 6:

    =AGGREGATE(1,6,data) // average and ignore errors
    

This formula in E6 will ignore all errors that might appear in data, not just the #N/A error, and it will work fine with negative values. The AGGREGATE function is a "Swiss Army knife" function that can run _other functions_ like SUM, COUNT, AVERAGE, MAX, etc. with special behaviors. For example, AGGREGATE can optionally ignore errors, hidden rows, and even other calculations. AGGREGATE can perform [19 different functions](https://exceljet.net/functions/aggregate-function)
.

### AVERAGE and IFERROR

It is possible to write an [array formula](https://exceljet.net/glossary/array-formula)
 that uses the [AVERAGE function](https://exceljet.net/functions/average-function)
 with the [IFERROR function](https://exceljet.net/functions/iferror-function)
 to filter out errors before averaging:

    =AVERAGE(IFERROR(data,""))
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
, where [arrays are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
._

IFERROR returns an alternative result when there is an error, and the original result when there is not. In this formula, the IFERROR function is used to catch errors in the data and convert them to empty strings (""). In the example shown, the named range **data** (B5:B15) contains eleven cells, which can be represented as an [array](https://exceljet.net/glossary/array)
 like this:

    {98;95;88;95;#N/A;75;90;100;#N/A;84;91} // 11 values in B5:B15
    

IFERROR converts the #N/A errors to [empty strings](https://exceljet.net/glossary/empty-string)
 ("") like this:

    =IFERROR(data,"")
    =IFERROR({98;95;88;95;#N/A;75;90;100;#N/A;84;91},"")
    {98;95;88;95;"";75;90;100;"";84;91}
    

The resulting array is returned directly to the [AVERAGE function](https://exceljet.net/functions/average-function)
:

    =AVERAGE({98;95;88;95;"";75;90;100;"";84;91}) // returns 90.67
    

AVERAGE automatically ignores text values and returns the same result as above: 90.67.

### AVERAGE and FILTER

Finally, in [Excel 365](https://exceljet.net/glossary/excel-365)
, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with the ISNUMBER function to filter out errors before they are averaged with a formula like this:

    =AVERAGE(FILTER(data,ISNUMBER(data)))
    

_Note: this is an array formula, but it only works in [Excel 365](https://exceljet.net/glossary/excel-365)
, where [arrays are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
._

Here, the [ISNUMBER function](https://exceljet.net/functions/filter-function)
 tests each value in **data** and returns an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE}
    

Because there are 11 values in **data**, ISNUMBER returns 11 TRUE / FALSE results. TRUE corresponds to numeric values, and FALSE corresponds to non-numeric values. This array is returned directly to the FILTER function as the _include_ argument:

    FILTER(data,{TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE})
    

FILTER then returns a "filtered array" that contains the 9 numeric values to AVERAGE:

    =AVERAGE({98;95;88;95;75;90;100;84;91}) // returns 90.67
    

and AVERAGE returns 90.67.

_Note: Be careful when ignoring errors. Suppressing errors can hide underlying problems._ 

Related formulas
----------------

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

[![Excel formula: Sum and ignore errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20and%20ignore%20errors.png "Excel formula: Sum and ignore errors")](https://exceljet.net/formulas/sum-and-ignore-errors)

### [Sum and ignore errors](https://exceljet.net/formulas/sum-and-ignore-errors)

In this example, the goal is to create a formula that will sum values in a range that may contain errors. A common problem in Excel is that errors in data show up in the results of other formulas. For example, in the worksheet shown, the SUM function is used to sum the named range data (D5:D15) ...

Related functions
-----------------

[![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")](https://exceljet.net/functions/averageif-function)

### [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    
*   [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)
    
*   [Sum and ignore errors](https://exceljet.net/formulas/sum-and-ignore-errors)
    

### Functions

*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

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
# Excel BYROW function | Exceljet

**Source:** https://exceljet.net/functions/byrow-function

---

[Skip to main content](https://exceljet.net/functions/byrow-function#main-content)

[](https://exceljet.net/functions/byrow-function#)

*   [Previous](https://exceljet.net/functions/bycol-function)
    
*   [Next](https://exceljet.net/functions/choosecols-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

BYROW Function
==============

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[MAP](https://exceljet.net/functions/map-function)

[SCAN](https://exceljet.net/functions/scan-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

[MAKEARRAY](https://exceljet.net/functions/makearray-function)

[BYCOL](https://exceljet.net/functions/bycol-function)

![Excel BYROW function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")

Summary
-------

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array.

Purpose 
--------

Apply function to row

Return value 
-------------

One result per row

Syntax
------

    =BYROW(array,function)

*   _array_ - The array or array to process.
*   _function_ - The function to apply to each row.

Using the BYROW function 
-------------------------

The Excel BYROW function applies a function to each row in _array_ and returns one result per row in a single [array](https://exceljet.net/glossary/array)
. The purpose of BYROW is to process data in an array or range in a "by row" fashion. For example, if BYROW is given an array with 10 rows, BYROW will return an array with 10 results. The calculation performed on each row can be a stock function like SUM, COUNT, etc., or a custom LAMBDA function designed to operate on row values. BYROW can accept an abbreviated "eta lamba" syntax for simple operations like SUM, as explained below.

### The concept and syntax

Essentially, BYROW allows you to loop over all rows in a range or array and perform a custom calculation on each row in a single formula. The second argument, _function,_ determines the calculation performed_:_

    =BYROW(array,function)
    

The _function_ can be provided in two ways: a short-form "eta lambda" syntax or a long-form custom LAMBDA syntax. For example, to sum each row in an array, the short-form syntax looks like this:

    =BYROW(array,SUM)
    

The long-form custom syntax looks like this:

    =BYROW(array,LAMBDA(row,SUM(row))
    

Why two syntax options? The short form is for convenience. It is concise and easy to read. However, the behavior cannot be customized. The long-form syntax uses the LAMBDA function and can be customized as desired. See below for an example of BYROW formulas that use both options.

_Note: in the examples above, we use the variable name "row" in the LAMBDA function for clarity. However, you are free to use whatever name you like._

### Example - sum all rows

In the worksheet below, the BYROW function is used to sum the values in each row of the range C5:H15. The formula in cell J5 looks like this:

    =BYROW(C5:H15,LAMBDA(row,SUM(row)))
    

![BYROW function example - sum rows with long-form syntax](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_byrow_function_long_form_example.png "BYROW function example - sum rows with long-form syntax")

The BYROW function returns all results at once in a single array. Because there are 11 rows in data, the result is an array that contains 11 sums like this:

    {432;440;403;455;479;433;426;463;407;431;519}
    

The values in this array spill into the range J5:J15. The formulas below are other examples of how BYROW can be used on the same data with formulas that follow the same pattern:

    =BYROW(data,LAMBDA(row,MAX(row))) // max
    =BYROW(data,LAMBDA(row,MIN(row))) // min
    =BYROW(data,LAMBDA(row,AVERAGE(row))) // average
    

### Example - Short form "eta lambda" syntax

While BYROW is designed to accept a function defined by LAMBDA, it will also accept a short-form "eta lambda" syntax for simple operations. Using the eta lambda syntax, you can pass a function by name only into BYROW like this:

    =BYROW(array,SUM)

This formula is equivalent to the long-form version:

    =BYROW(array,LAMBDA(x,SUM(x)))

For example, in the worksheet below, we have adapted the formula in J5 to use the short-form syntax. The formula now looks like this:

    =BYROW(C5:H15,SUM)

![BYROW function example - sum rows with short-form syntax](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_byrow_function_eta_short_form_example.png "BYROW function example - sum rows with short-form syntax")

The Excel formula engine knows how to pass each row into the SUM function, and the results are exactly the same as the long-form version. You can use the same syntax to call other functions like this:

    =BYROW(array,SUM) // sum each row
    =BYROW(array,MAX) // max of each row
    =BYROW(array,MIN) // min of each row
    =BYROW(array,COUNT) // count of each row

The short-form eta syntax works for functions that accept a single argument, such as SUM, AVERAGE, MIN, MAX, COUNT, COUNTA, etc. It will not work in all scenarios because the logic can't be modified. For example, the formula in the next section below can't use the eta lambda syntax.

### Example - Count cells over 90

In this example, the goal is to count the values in each row greater than 90. The formula is a bit more complex because we need more logic. This is a situation where we can't use the short-form syntax. The formula in cell K5 looks like this:

    =BYROW(C5:H15,LAMBDA(row,SUM(--(row>90))))
    

![BYROW function example - count values over 90](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/byrow_function_example_count_values_over_90.png "BYROW function example - count values over 90")

Working from the inside out, a custom lambda counts all values in a row greater than 90:

    LAMBDA(row,SUM(--(row>90))) // custom lambda
    

The logical expression row>90 returns an array of TRUE and FALSE values, and we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to coerce these values to 1s and 0s. The SUM function then sums the 1s and 0s, and the result is the count of values greater than 90:

    SUM(--(row>90))

The LAMBDA runs on each row in the data. Since there are 11 rows in the range B5:H15, BYROW returns 11 results that [spill](https://exceljet.net/glossary/spill)
 into the range K5:K15. See [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
 for more information about the logic inside of SUM. 

> You could use COUNTIFS instead of SUM to solve this problem. However, COUNTIFS [requires a range](https://exceljet.net/functions/countifs-function#array_problem)
> , which means you can't give BYROW an _array_ if you use COUNTIFS in the calculation. For this reason, I generally avoid the \*IFS functions when working with the new dynamic array functions where arrays are more common.

### Example - BYROW with multiple functions

It is also possible to configure BYROW to run more than one function at the same time, although it is not obvious how. The trick is to wrap the functions in the [HSTACK](https://exceljet.net/functions/hstack-function)
 or [VSTACK](https://exceljet.net/functions/vstack-function)
 functions (depending on the layout needed). For example, in the worksheet below, BYROW is configured to return the sum, the maximum value, and the minimum value for each row at the same time. The formula in J5, copied down, is:

    =BYROW(C5:H15,HSTACK(SUM,MAX,MIN))

![BYROW function example - multiple calculations at the same time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_byrow_function_example_multiple_calculations.png "BYROW function example - multiple calculations at the same time")

Although this formula uses the short-form syntax, you can take the same approach with custom LAMBDA calculations. 

> Because of the current [array of arrays](https://exceljet.net/glossary/array-of-arrays)
>  limitation in Excel, this formula will not spill down across all rows. It will initially only calculate results for the first row. You will then need to copy the formula manually to all rows in a second step.

BYROW function examples
-----------------------

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

[![Excel formula: Row is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/row_is_blank.png "Excel formula: Row is blank")](https://exceljet.net/formulas/row-is-blank)

### [Row is blank](https://exceljet.net/formulas/row-is-blank)

The goal is to use a formula to check if all cells in a row are blank or empty and return TRUE or FALSE. One way to solve this problem is with the SUMPRODUCT function, as seen in the worksheet above. Another approach is to use the newer BYROW function. Both methods are described below. SUMPRODUCT...

[![Excel formula: Sum by week number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week%20number.png "Excel formula: Sum by week number")](https://exceljet.net/formulas/sum-by-week-number)

### [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)

In this example, the goal is to sum the amounts in column D by week number, using the dates in column C to determine the week number. The week numbers in column G are manually entered. The final results should appear in column H. All data is in an Excel Table named data in the range B5:E16. This...

[![Excel formula: Sum if multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_columns.png "Excel formula: Sum if multiple columns")](https://exceljet.net/formulas/sum-if-multiple-columns)

### [Sum if multiple columns](https://exceljet.net/formulas/sum-if-multiple-columns)

In this example, the goal is to calculate a sum for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. In other words, we want to perform a "sum if" with a data range that contains three columns. For convenience only, data (C5:E16) and group (B5:B16) are named...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum by quarter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20quarter.png "Excel formula: Sum by quarter")](https://exceljet.net/formulas/sum-by-quarter)

### [Sum by quarter](https://exceljet.net/formulas/sum-by-quarter)

In this example, the goal is to sum the amounts in column C by quarter in column G. Column D is a helper column , and the formula to calculate quarters from the dates in column B is explained below. All data is in an Excel Table named data in the range B5:E16. This problem can be solved with the...

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Sequence of leap years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_leap_years.png "Excel formula: Sequence of leap years")](https://exceljet.net/formulas/sequence-of-leap-years)

### [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)

In this example, the goal is to generate a list of leap years between a given start year and end year. The worksheet is set up so that the start year is an input in cell B5 and the end year is an input in cell B8. If either value changes, the formula should generate a new list of leap years. In the...

[![Excel formula: Sum numbers with text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20numbers%20with%20text.png "Excel formula: Sum numbers with text")](https://exceljet.net/formulas/sum-numbers-with-text)

### [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)

In this example, one goal is to sum the numbers that appear in the range B5:B16. A second more challenging goal is to create the table of results seen in E7:F12. For convenience, data is the named range B5:B16. Total sum To sum all the numbers that appear in B5:B16, ignoring text, the formula in E5...

[![Excel formula: Remove blank rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_blank_rows.png "Excel formula: Remove blank rows")](https://exceljet.net/formulas/remove-blank-rows)

### [Remove blank rows](https://exceljet.net/formulas/remove-blank-rows)

In this example, the goal is to remove empty rows from a range with a formula. One approach is to use the BYROW function to identify all non-empty rows in the range and pass this result into the FILTER function as the include argument. This is the approach used in the worksheet shown, where the...

[![Excel formula: Count birthdays by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20birthdays%20by%20year_0.png "Excel formula: Count birthdays by year")](https://exceljet.net/formulas/count-birthdays-by-year)

### [Count birthdays by year](https://exceljet.net/formulas/count-birthdays-by-year)

In this example, the goal is to count birthdays by year. The source data is an Excel Table named data in the range C5:C16. The birthdays we want to count are in the Birthday column. In column E, the years of interest have been previously entered. The easiest way to solve this problem is with the...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

[![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")](https://exceljet.net/formulas/sum-by-week)

### [Sum by week](https://exceljet.net/formulas/sum-by-week)

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named data in the range B5:C16. This problem can be solved in a straightforward way with the SUMIFS function . In the current version of...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel MAKEARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20makearray%20function.png "Excel MAKEARRAY function")](https://exceljet.net/functions/makearray-function)

### [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)

The Excel MAKEARRAY function returns an array with specified rows and columns, based on a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. MAKEARRAY can be used to create arrays with variable dimensions based on a calculation....

[![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")](https://exceljet.net/functions/bycol-function)

### [BYCOL Function](https://exceljet.net/functions/bycol-function)

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

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
    
*   [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)
    
*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    
*   [Remove blank rows](https://exceljet.net/formulas/remove-blank-rows)
    
*   [Count birthdays by year](https://exceljet.net/formulas/count-birthdays-by-year)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)
    
*   [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    
*   [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)
    
*   [Row is blank](https://exceljet.net/formulas/row-is-blank)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)
    
*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    

### Links

*   [Microsoft BYROW function documentation](https://support.microsoft.com/en-us/office/byrow-function-2e04c677-78c8-4e6b-8c10-a4602f2602bb)
    

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
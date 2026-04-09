# Excel BYCOL function | Exceljet

**Source:** https://exceljet.net/functions/bycol-function

---

[Skip to main content](https://exceljet.net/functions/bycol-function#main-content)

[](https://exceljet.net/functions/bycol-function#)

*   [Previous](https://exceljet.net/functions/arraytotext-function)
    
*   [Next](https://exceljet.net/functions/byrow-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

BYCOL Function
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

[BYROW](https://exceljet.net/functions/byrow-function)

![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")

Summary
-------

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array.

Purpose 
--------

Apply function to column

Return value 
-------------

One result per column

Syntax
------

    =BYCOL(array,lambda)

*   _array_ - The array or array to process.
*   _lambda_ - The lambda function to apply to each column.

Using the BYCOL function 
-------------------------

The Excel BYCOL function applies a function to each column in _array_ and returns one result per column in a single [array](https://exceljet.net/glossary/array)
. The purpose of BYCOL is to process data in an array or range in a "by column" fashion. For example, if BYCOL is given an array with 10 columns, BYCOL will return an array with 10 results. The calculation performed on each column can be a stock function like SUM, COUNT, etc., or a custom LAMBDA function designed to operate on column values. BYCOL can accept an abbreviated "eta lamba" syntax for simple operations like SUM, as explained below.

### The concept and syntax

Essentially, BYCOL allows you to loop over all columns in a range or array and perform a custom calculation on each column in a single formula. The second argument, _function,_ determines the calculation performed_:_

    =BYCOL(array,function)
    

The _function_ can be provided in two ways: a short-form "eta lambda" syntax or a long-form custom LAMBDA syntax. For example, to sum each column in an array, the short-form syntax looks like this:

    =BYCOL(array,SUM)
    

The long-form custom syntax looks like this:

    =BYCOL(array,LAMBDA(column,SUM(column))
    

Why two syntax options? The short form is for convenience. It is concise and easy to read. However, the behavior cannot be customized. The long-form syntax uses the LAMBDA function and can be customized as desired. See below for an example of BYCOL formulas that use both options.

_Note: in the examples above, we use the variable name "column" in the LAMBDA function for clarity. However, you are free to use whatever name you like._

### Example - sum all columns

In the worksheet below, the BYCOL function is used to sum the values in each column of the range C5:H14. The formula in cell C16 looks like this:

    =BYCOL(C5:H14,LAMBDA(column,SUM(column)))
    

![BYCOL function example - sum all columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_bycol_function_-_sum_columns_example.png "BYCOL function example - sum all columns")

The BYCOL function returns all sums at once in a single array. Because there are 6 columns in the range, the result is an array that contains 6 sums like this:

    {8859,8690,9020,9112,8876,9153}
    

The values in this array spill into the range C16:H16. The formulas below are other examples of how BYCOL can be used on the same data with formulas that follow the same pattern:

    =BYCOL(C5:H14,LAMBDA(column,MAX(column))) // max
    =BYCOL(C5:H14,LAMBDA(column,MIN(column))) // min
    =BYCOL(C5:H14,LAMBDA(column,AVERAGE(column))) // average
    

### Example - Short form "eta lambda" syntax

While BYCOL is designed to accept a function defined by LAMBDA, it will also accept a short-form "eta lambda" syntax for simple operations. Using the eta lambda syntax, you can pass a function by name only into BYCOL like this:

    =BYCOL(array,SUM)

This formula is equivalent to the long-form version:

    =BYCOL(array,LAMBDA(x,SUM(x)))

For example, in the worksheet below, we have adapted the formula in J5 to use the short-form syntax. The formula now looks like this:

    =BYCOL(C5:H14,SUM)

![BYCOL function example - sum columns with short-form syntax](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_bycol_function_eta_short_form_example.png "BYCOL function example - sum columns with short-form syntax")

The Excel formula engine knows how to pass each column into the SUM function, and the results are exactly the same as the long-form version. You can use the same syntax to call other functions like this:

    =BYCOL(array,SUM) // sum each column
    =BYCOL(array,MAX) // max of each column
    =BYCOL(array,MIN) // min of each column
    =BYCOL(array,COUNT) // count of each column

The short-form eta syntax works for functions that accept a single argument, such as SUM, AVERAGE, MIN, MAX, COUNT, COUNTA, etc. It will not work in all scenarios because the logic can't be modified. For example, the formula in the next section below can't use the eta lambda syntax.

### Example - Count values over 900

In this example, the goal is to count the values in each column greater than 900. The formula is a bit more complex because we need more logic. This is a situation where we can't use the short-form syntax above. The formula in cell C16 looks like this:

    =BYCOL(C5:H14,LAMBDA(column,SUM(--(column>900))))
    

![BYCOL function example - count values over 900](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_byrow_function_example_count_values_over_900.png "BYCOL function example - count values over 900")

Working from the inside out, a custom lambda counts all values in a column greater than 900:

    LAMBDA(column,SUM(--(column>900))) // custom lambda
    

The logical expression column>900 returns an array of TRUE and FALSE values, and we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to coerce these values to 1s and 0s. The SUM function then sums the 1s and 0s, and the result is the count of values greater than 900:

    SUM(--(column>900))

The LAMBDA runs on each column in the data. Since there are 6 columns in the range C5:H14, BYCOL returns 6 results that [spill](https://exceljet.net/glossary/spill)
 into the range C16:H16. See [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
 for more information about the logic inside of SUM. 

> You could use COUNTIFS instead of SUM to solve this problem. However, COUNTIFS [requires a range](https://exceljet.net/functions/countifs-function#array_problem)
> , which means you can't give BYCOL an _array_ if you use COUNTIFS in the calculation. For this reason, I generally avoid the \*IFS functions when working with the new dynamic array functions where arrays are more common.

### Example - BYCOL with multiple functions

It is also possible to configure BYCOL to run more than one function at the same time, although it is not obvious how. The trick is to wrap the functions in the [HSTACK](https://exceljet.net/functions/hstack-function)
 or [VSTACK](https://exceljet.net/functions/vstack-function)
 functions (depending on the layout needed). For example, in the worksheet below, BYCOL is configured to return the sum, the maximum value,  the minimum value, and the average value for each column at the same time. The formula in C12, copied across, is:

    =BYCOL(C5:H10,VSTACK(SUM,MAX,MIN,AVERAGE))

![BYCOL function example - multiple calculations at the same time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_bycol_function_example_multiple_calculations.png "BYCOL function example - multiple calculations at the same time")

Although this formula uses the short-form syntax, you can take the same approach with custom LAMBDA calculations. 

> Because of the current [array of arrays](https://exceljet.net/glossary/array-of-arrays)
>  limitation in Excel, this formula will not spill down across all columns. It will initially only calculate results for the first column. You will then need to copy the formula manually to all columns in a second step.

BYCOL function examples
-----------------------

[![Excel formula: Count columns that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20columns%20that%20contain%20specific%20values.png "Excel formula: Count columns that contain specific values")](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

### [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

In this example, the goal is to count the number of columns in the data that contain 19 (the value in cell I4). The main challenge in this problem is that the value might appear in any row, and more than once in the same column. If we wanted to simply count the total number of times a value...

[![Excel formula: Get column totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20column%20totals.png "Excel formula: Get column totals")](https://exceljet.net/formulas/get-column-totals)

### [Get column totals](https://exceljet.net/formulas/get-column-totals)

In this example, the goal is to return an array with 7 subtotals, one for each day of the week, as seen in columns C:I. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We...

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

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get column totals](https://exceljet.net/formulas/get-column-totals)
    
*   [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Links

*   [Microsoft BYCOL function documentation](https://support.microsoft.com/en-us/office/bycol-function-58463999-7de5-49ce-8f38-b7f7a2192bfb)
    

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
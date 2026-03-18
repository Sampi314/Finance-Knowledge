# Excel MAP function | Exceljet

**Source:** https://exceljet.net/functions/map-function

---

[Skip to main content](https://exceljet.net/functions/map-function#main-content)

[](https://exceljet.net/functions/map-function#)

*   [Previous](https://exceljet.net/functions/makearray-function)
    
*   [Next](https://exceljet.net/functions/percentof-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

MAP Function
============

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

[BYROW](https://exceljet.net/functions/byrow-function)

![Excel MAP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")

Summary
-------

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

Purpose 
--------

Map array to custom function

Return value 
-------------

Array of results

Syntax
------

    =MAP(array1,[array2],...,lambda)

*   _array1_ - The array to be mapped.
*   _array2_ - \[optional\] Additional arrays required by the LAMBDA.
*   _lambda_ - The custom LAMBDA function to apply.

Using the MAP function 
-----------------------

The MAP function "maps" a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

The MAP function is useful when you want to process each item in an array individually but as an array operation that yields an array result. MAP is also useful when the formula logic is complex and would be best managed in a single location. Using a named LAMBDA function with MAP is possible to reuse the same code elsewhere.

The MAP function takes two required [arguments](https://exceljet.net/glossary/function-argument)
: _array1_ and _lambda_. _Array1_ is the array that should be mapped. _Lambda_ is the custom lambda function that should be run on each item in _array1_. Additional arguments can be added in the form of _array2_, _array3_, etc., before _lambda_, which must always be the last argument provided. When additional arrays are provided to MAP, the LAMBDA function must be configured to accept additional arguments. _Array1_ should be the first argument in the LAMBDA, _array2_ should be the second argument, etc. Note that the second argument must be an array if not a lambda. 

### Examples

The MAP function maps each value in an array to a custom LAMBDA function. For example, the formula below maps a LAMBDA function that simply adds 1 to each item in the supplied array:

    =MAP({1,2,3},LAMBDA(a,a+1)) // returns {2,3,4}
    

The variable _a_ passed into the LAMBDA function as the first argument is _array1_ in the MAP function.

### Remove non-numeric values

In the worksheet shown above, MAP is used to remove non-numeric values from the array provided (B5:D16). The formula in F5 is:

    =MAP(B5:D16,LAMBDA(a,IF(ISNUMBER(a),+a,"")))
    

Because _array1_ has 12 rows and 3 columns, the result from MAP is a 12 x 3 array that [spills](https://exceljet.net/glossary/spill)
 into the range F5:H16.

_Note: the +a notation is used to force Excel to coerce a from a range reference to an array of values. Without the +, MAP will return a #CALC! error. This step is sometimes necessary when working with array formulas that spill._

### Additional arrays

MAP can accept additional arrays that can be used by the LAMBDA during calculation. The formula below adds each item in _array1_ to the corresponding item in _array2_:

    =MAP({1,2,3},{1,2,3},LAMBDA(a,b,a+b)) // returns {2,4,6}
    

Here, the variable _a_ given to the LAMBDA function is _array1_ in  the MAP function_,_ and _b_ is _array2_.

### When to use MAP

The [dynamic array engine in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 can handle many array operations natively without a function like MAP. For example, the formulas below both return the same result:

    =array+1
    =MAP(array,LAMBDA(a,a+1))
    

As such, there is no particular reason to use MAP when a native array operation will achieve the same result. However, there are cases where MAP can be useful:

1.  To run logical tests with the [AND](https://exceljet.net/functions/and-function)
     and [OR](https://exceljet.net/functions/or-function)
     functions. These functions aggregate arrays to a single value, so normally they can be used in array operations that need to maintain multiple values.
2.  To perform certain aggregate operations on multiple arrays, i.e.
    
        =MAP(rng1,rng2,rng3,LAMBDA(a,b,c,MAX(a,b,c)))
        
    
3.  To make a function [spill](https://exceljet.net/glossary/spill)
     that otherwise won't.

Note: The MAP function returns an array of results. See the [REDUCE function](https://exceljet.net/functions/reduce-function)
 if you want to process each item in an array individually but you want a _single_ aggregated result.

MAP function examples
---------------------

[![Excel formula: Tiered discounts based on quantity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tiered_discounts_based_on_quantity.png "Excel formula: Tiered discounts based on quantity")](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)

### [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)

This example shows a workbook designed to apply discounts based on seven pricing tiers. The total quantity of items is entered as a variable in cell C4. The discount is applied via the unit costs in E7:E13, which decrease as the quantity increases. The first 200 items have an undiscounted price of...

[![Excel formula: Get location of value in 2D array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_location_of_value_in_2D_array.png "Excel formula: Get location of value in 2D array")](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

### [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

In this example, the goal is to return a list of the locations for a specific value in a 2D array of values (i.e., a table). The target value is entered in cell N5, and the table being tested is in the range C4:L16. The coordinates are supplied from row 4 and column B, as seen in the worksheet. In...

[![Excel formula: Hours that overlap specific time blocks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hours_that_overlap_specific_time_blocks.png "Excel formula: Hours that overlap specific time blocks")](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

### [Hours that overlap specific time blocks](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

In this example, the goal is to calculate exactly how much of a task, shift, or event falls inside one or more defined blocks of time. The formula accepts a start and end time for the overall task or shift, as well as a start and end time for the block of interest. In the worksheet shown, the Start...

[![Excel formula: MAP with AND and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20with%20and%20and%20or%20logic.png "Excel formula: MAP with AND and OR logic")](https://exceljet.net/formulas/map-with-and-and-or-logic)

### [MAP with AND and OR logic](https://exceljet.net/formulas/map-with-and-and-or-logic)

In this example, the goal is to apply AND and OR logic to an array using the AND function and the OR function . The challenge is that the AND function and the OR function both aggregate values to a single result. This means you can't use them in an array operation where the goal is to return more...

[![Excel formula: Number to words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/number_to_words.png "Excel formula: Number to words")](https://exceljet.net/formulas/number-to-words)

### [Number to words](https://exceljet.net/formulas/number-to-words)

In this example, the goal is to build a custom function that will convert a number like 123 into "One hundred twenty three" or "One hundred twenty three dollars" when currency is specified as USD. In addition, the formula should support multiple currencies and handle decimals. Traditionally, "...

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

*   [Hours that overlap specific time blocks](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)
    
*   [MAP with AND and OR logic](https://exceljet.net/formulas/map-with-and-and-or-logic)
    
*   [Number to words](https://exceljet.net/formulas/number-to-words)
    
*   [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)
    
*   [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)
    
*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Links

*   [Microsoft MAP function documentation](https://support.microsoft.com/en-us/office/map-function-48006093-f97c-47c1-bfcc-749263bb1f01)
    

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
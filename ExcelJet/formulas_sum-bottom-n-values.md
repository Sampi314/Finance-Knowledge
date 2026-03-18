# Sum bottom n values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-bottom-n-values

---

[Skip to main content](https://exceljet.net/formulas/sum-bottom-n-values#main-content)

[](https://exceljet.net/formulas/sum-bottom-n-values#)

*   [Previous](https://exceljet.net/formulas/sum-and-ignore-errors)
    
*   [Next](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum bottom n values
===================

by Dave Bruns · Updated 13 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SMALL](https://exceljet.net/functions/small-function)

[SUM](https://exceljet.net/functions/sum-function)

[ROW](https://exceljet.net/functions/row-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Sum bottom n values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20bottom%20n%20values.png "Excel formula: Sum bottom n values")

Summary
-------

To sum the lowest **n** values in a range, you can use a formula based on the [SMALL function](https://exceljet.net/functions/small-function)
 and the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the generic form of the formula above, **range** contains numeric values and **n** is the number of values to sum. In the example shown, the formula in cell E5 is:

    =SUMPRODUCT(SMALL(data,{1,2,3}))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. The result is the sum of the smallest 3 values (10, 15, 20) which is 45.

Generic formula
---------------

    =SUMPRODUCT(SMALL(range,{1,2,n}))

Explanation 
------------

In this example, the goal is to sum the smallest **n** values in a set of data, where **n** is a variable that can be easily changed. At a high level, the solution breaks down into two steps (1) extract the **n** smallest values from the data set and (2) sum the extracted values. This problem can be solved with the SMALL function together with the SUMPRODUCT function, as explained below. For convenience only, the range B5:B16 is [named](https://exceljet.net/glossary/named-range)
 "data".

### SMALL function

The [SMALL function](https://exceljet.net/functions/small-function)
 is designed to return the _nth_ smallest value in a range. For example:

    =SMALL(range,1) // 1st smallest
    =SMALL(range,2) // 2nd smallest
    =SMALL(range,3) // 3rd smallest
    

Normally, SMALL returns just one value. However, if you supply an [array constant](https://exceljet.net/glossary/array-constant)
 (e.g. a constant in the form {1,2,3}) to SMALL as the second argument, _k_ , SMALL will return an [array](https://exceljet.net/glossary/array)
 of results instead of a single result. For example:

    =SMALL(A1:A10,{1,2,3})
    

will return the 1st, 2nd, and 3rd smallest values in the range A1:A10.

### Example

In the example shown, the formula in E5 is:

    =SUMPRODUCT(SMALL(data,{1,2,3}))
    

Working from the inside out, the SMALL function is configured to return the 3 smallest values in the range B5:B16:

    =SMALL(data,{1,2,3}) // returns {10,15,20}
    

Because we provide three separate values for _k_, the result is an array that contains three results:

    {10,15,20}
    

This [array](https://exceljet.net/glossary/array)
 is returned directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    SUMPRODUCT({10,20,30}) // returns 45
    

With just a single array to process, SUMPRODUCT sums the values in the array and returns 45 as a final result.

### SUM alternative

It is common to use SUMPRODUCT in problems like this because [SUMPRODUCT can handle arrays natively](https://exceljet.net/articles/why-sumproduct)
 without any special handling in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. However, in a modern version of Excel, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead:

    =SUM(SMALL(data,{1,2,3})) // returns 45
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

### When n becomes large

As **n** becomes a larger number, it becomes tedious to enter longer [array constants](https://exceljet.net/glossary/array-constant)
 like {1,2,3,4,5,6,7,8,9,10}, etc. In this situation, you can use a shortcut to create an array that contains sequential numbers automatically based on the [ROW](https://exceljet.net/functions/row-function)
 and [INDIRECT](https://exceljet.net/functions/indirect-function)
 functions. For example, to sum the lowest 10 values in a range, you can use a formula like this:

    =SUMPRODUCT(SMALL(range,ROW(INDIRECT("1:10"))))
    

Here, the INDIRECT function converts the [text string](https://exceljet.net/glossary/text-value)
 "1:10" to the [_range_](https://exceljet.net/glossary/range)
 1:10, which is returned to the ROW function. The ROW function then returns the 10 row numbers that correspond to the range 1:10 in an array like this:

    {1;2;3;4;5;6;7;8;9;10}
    

Note this is actually a [vertical array](https://exceljet.net/glossary/array)
, as indicated by the semicolons (;) but the SMALL function will happily accept a vertical or horizontal array as the _k_ argument. Once INDIRECT and ROW have been evaluated, the formula is in the same form as before:

    =SUMPRODUCT(SMALL(range,{1;2;3;4;5;6;7;8;9;10}) // sum 10 smallest
    

SMALL will return the 10 lowest values, and SUMPRODUCT will return the sum of these values as a final result.

### Variable n

To set up a formula where **n** is a variable in another cell, you can [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 inside INDIRECT. For example, if A1 contains **n**, you can use:

    =SUMPRODUCT(SMALL(range,ROW(INDIRECT("1:"&A1))))
    

This allows a user to change the value of **n** directly on the worksheet and the formula will respond instantly.

### With the SEQUENCE function

New in [Excel 365](https://exceljet.net/glossary/excel-365)
, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 can generate numeric arrays directly in one step, which eliminates the need for the ROW + INDIRECT combination explained above. In fact, with SEQUENCE there is really no need to use array constant either. We can simplify the formula as follows:

    =SUM(SMALL(range,SEQUENCE(3)) // sum lowest 3 values
    =SUM(SMALL(range,SEQUENCE(9)) // sum lowest 9 values
    

_Note: Because SEQUENCE requires the new [dynamic array engine in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 (where array behavior is native), we have also replaced SUMPRODUCT with the SUM function. Read more about SUMPRODUCT and arrays [here](https://exceljet.net/articles/why-sumproduct)
._

Related formulas
----------------

[![Excel formula: Sum bottom n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values%20with%20criteria.png "Excel formula: Sum bottom n values with criteria")](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

### [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

In this example, the goal is to sum the smallest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three smallest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Sum top n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20top%20n%20values%20with%20criteria.png "Excel formula: Sum top n values with criteria")](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

### [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

In this example, the goal is to sum the largest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three largest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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
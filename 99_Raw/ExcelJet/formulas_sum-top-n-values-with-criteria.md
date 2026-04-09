# Sum top n values with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-top-n-values-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/sum-top-n-values-with-criteria#main-content)

[](https://exceljet.net/formulas/sum-top-n-values-with-criteria#)

*   [Previous](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Next](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum top n values with criteria
==============================

by Dave Bruns · Updated 6 Jun 2023

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

[LARGE](https://exceljet.net/functions/large-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Sum top n values with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20top%20n%20values%20with%20criteria.png "Excel formula: Sum top n values with criteria")

Summary
-------

To sum the largest **n** values in a range with criteria, you can use a formula based on [FILTER](https://exceljet.net/functions/filter-function)
, [LARGE](https://exceljet.net/functions/large-function)
, and [SUM](https://exceljet.net/functions/sum-function)
. In the example shown, the formula in cell F5 is:

    =SUM(LARGE(FILTER(data[Values],data[Group]="A"),{1,2,3}))
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C16. The result is the sum of the top 3 values in Group A (65,45,25) which is 135.

_Note: FILTER is a [newer function](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 not available in all versions of Excel. See below for an alternative formula that works in older versions._

Generic formula
---------------

    =SUM(LARGE(FILTER(values,criteria),{1,2,3,n}))

Explanation 
------------

In this example, the goal is to sum the largest **n** values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three largest values, so **n** is equal to 3. At a high level, this problem breaks down into three separate steps:

1.  Apply criteria to select specific values
2.  Extract the 3 largest values
3.  Sum the 3 extracted values

This problem can be solved with a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
, the [LARGE function](https://exceljet.net/functions/large-function)
, and the [SUM function](https://exceljet.net/functions/sum-function)
. For convenience, the range B5:C16 is an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data**. This allows the formula to use [structured references](https://exceljet.net/glossary/structured-reference)
.

_Note: FILTER is a newer function not available in "[Legacy Excel](https://exceljet.net/glossary/legacy-excel)
". See below for an alternative formula that works in older versions of Excel._

### Example formula

The final formula in cell F5 is:

    =SUM(LARGE(FILTER(data[Values],data[Group]="A"),{1,2,3}))
    

To explain how this formula works, we'll walk through the steps listed above. This means we will be working through the formula from the inside out. This is typical of Excel formulas where one function is [nested](https://exceljet.net/glossary/nesting)
 inside another.

### Apply criteria

The first step in the problem is to apply criteria to select values by group. This can be done with the [FILTER function](https://exceljet.net/functions/filter-function)
. To select values in group "A", we can use FILTER like this:

    FILTER(data[Values],data[Group]="A")
    

In this formula _array_ is provided as the **Values** column in the table, and the _include_ argument provides logic to select only values in group "A". The result is a subset of the values where the group is "A", which is returned in an [array](https://exceljet.net/glossary/array)
 like this:

    {10;65;25;45;20;15}
    

If you are new to the FILTER function, see this video: [Basic FILTER function example](https://exceljet.net/videos/filter-function-basic-example)

### Extract 3 largest values

The next step in the problem is to extract the three largest values from the array returned by FILTER. For this, we use the LARGE function. The [LARGE function](https://exceljet.net/functions/small-function)
 is designed to return the _nth_ largest value in a range. For example:

    =LARGE(range,1) // 1st largest
    =LARGE(range,2) // 2nd largest
    =LARGE(range,3) // 3rd largest
    

Normally, LARGE returns just one value. However, if you supply an [array constant](https://exceljet.net/glossary/array-constant)
 (e.g. a constant in the form {1,2,3}) to LARGE as the second argument, _k_, LARGE will return an [array](https://exceljet.net/glossary/array)
 of results instead of a single result. For example:

    =LARGE(range,{1,2,3}) // largest 3 values
    

Picking up where we left off, FILTER is used to extract values in group "A". The results returned by FILTER are returned directly to the LARGE function like this:

    LARGE({10;65;25;45;20;15},{1,2,3}) // returns {65,45,25}
    

The LARGE function then returns the 3 largest values in an array: 65, 45, 25.

### Sum largest values

The final step in the problem is to sum the values extracted by the LARGE function. This is done with the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM({65,45,25}) // returns 135
    

SUM returns 135 as a final result, which is the sum of the top 3 values in group A.

### Dynamic n

As **n** becomes larger, it becomes tedious to enter longer [array constants](https://exceljet.net/glossary/array-constant)
 like {1,2,3,4,5,6,7,8,9,10}, etc. To make **n** dynamic, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 to generate an array of sequential numbers automatically like this:

    =SUM(LARGE(FILTER(values,criteria),SEQUENCE(n))
    

Just replace **n** with the number of largest values you want to extract:

    =SUM(LARGE(FILTER(values,criteria),SEQUENCE(3)) // largest 3
    =SUM(LARGE(FILTER(values,criteria),SEQUENCE(5)) // largest 5
    

To make the value for n easier to change, enter n in a cell on the worksheet and replace the hardcoded number above with the cell reference:

    =SUM(LARGE(FILTER(values,criteria),SEQUENCE(A1)) // variable n
    

Video: The SEQUENCE function

### Legacy Excel

In older versions of Excel that don't provide the FILTER function, you can use the [IF function](https://exceljet.net/functions/if-function)
 to "filter" data like this:

    =SUM(LARGE(IF(data[Group]="A",data[Values]),{1,2,3}))
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

The behavior of this formula is similar to the original formula above. The main difference is that the IF function returns values from group A when the group="A", but it returns FALSE when the group is not "A". The LARGE function receives an array from IF that looks like this:

    {10;FALSE;65;FALSE;25;FALSE;45;FALSE;20;FALSE;15;FALSE}
    

Unlike the FILTER function, which returned just the six values associated with group A, IF returns an array that includes _twelve_ results, one for each value in the original data. However, because LARGE is programmed to _automatically_ ignore the logical values TRUE and FALSE, the result from LARGE, {65,45,25},  is the same as before and the final result is correct:

    =SUM({65,45,25}) // returns 135
    

Related formulas
----------------

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Sum bottom n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values.png "Excel formula: Sum bottom n values")](https://exceljet.net/formulas/sum-bottom-n-values)

### [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)

In this example, the goal is to sum the smallest n values in a set of data, where n is a variable that can be easily changed. At a high level, the solution breaks down into two steps (1) extract the n smallest values from the data set and (2) sum the extracted values. This problem can be solved...

[![Excel formula: Sum bottom n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values%20with%20criteria.png "Excel formula: Sum bottom n values with criteria")](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

### [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

In this example, the goal is to sum the smallest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three smallest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)
    
*   [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)
    
*   [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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
# Sum top n values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-top-n-values

---

[Skip to main content](https://exceljet.net/formulas/sum-top-n-values#main-content)

[](https://exceljet.net/formulas/sum-top-n-values#)

*   [Previous](https://exceljet.net/formulas/sum-numbers-in-single-cell)
    
*   [Next](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum top n values
================

by Dave Bruns · Updated 18 Jan 2023

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

[LARGE](https://exceljet.net/functions/large-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ROW](https://exceljet.net/functions/row-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")

Summary
-------

To sum the largest **n** values in a range, you can use a formula based on the [LARGE function](https://exceljet.net/functions/large-function)
. In the example shown, the formula in cell E5 is:

    =SUM(LARGE(data,SEQUENCE(D5)))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. The result 190, the sum of 70, 65, and 55.

Generic formula
---------------

    =SUM(LARGE(range,SEQUENCE(n)))

Explanation 
------------

In this example, the goal is to sum the largest **n** values in a set of data, where **n** is a variable that can be easily changed. For convenience, the range B5:B16 is [named](https://exceljet.net/glossary/named-range)
 **data**. At a high level, the solution breaks down into two steps: (1) extract the **n** largest values from the data set and (2) sum the extracted values. There are several ways to approach this problem depending on what version of Excel is available. Regardless of the approach, all solutions below depend on the LARGE function.

### LARGE function

The [LARGE function](https://exceljet.net/functions/large-function)
 is designed to return the _nth_ largest value in a range. For example:

    =LARGE(range,1) // 1st largest
    =LARGE(range,2) // 2nd largest
    =LARGE(range,3) // 3rd largest
    

Normally, LARGE returns just one value. However, if you supply an [array](https://exceljet.net/glossary/array)
 like {1,2,3} to LARGE as the second argument, _k_ , LARGE will return an array of results instead of a single result. For example, the formula below will return the 3 largest values in B5:B16:

    =LARGE(data,{1,2,3}) // returns {70;65;55}
    

Note that the result from LARGE is an [array](https://exceljet.net/glossary/array)
. By [nesting](https://exceljet.net/glossary/nesting)
 the LARGE function side the SUM function, we can get a sum of the 3 largest three values in **data**:

    =SUM(LARGE(data,{1,2,3})) // returns 190

The SUM function returns a result of 190, the sum of 70, 65, and 55. In older versions of Excel, you might have to use the SUMPRODUCT function instead of the SUM function, [for reasons described here](https://exceljet.net/articles/why-sumproduct)
.

Given the formula outlined above, the challenge becomes how best to create the array needed to extract the top **n** values from a set of data. This depends on what Excel version is available.

### Current Excel

The latest version of Excel supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 and provides a number of functions that make working with arrays easier. One of these functions is [SEQUENCE](https://exceljet.net/functions/sequence-function)
, which is designed to generate arrays on the fly. In the example shown, the formula in E5 uses SEQUENCE to create a numeric array based on the value for **n** in cell D5

    =SUM(LARGE(data,SEQUENCE(D5)))
    

Working from the inside out, the SEQUENCE function is configured with the _rows_ [argument](https://exceljet.net/glossary/function-argument)
 set to cell D5. With the number 3 in D5, sequence generates a sequential array like this:

    SEQUENCE(D5) // returns {1;2;3}

The numeric array is returned directly to the LARGE function for the _k_ argument:

    =SUM(LARGE(data,{1;2;3}))

And the solution proceeds as outlined above:

    =SUM(LARGE(data,{1;2;3}))
    =SUM({70;65;55})
    =190

The final result is 190, as shown in the worksheet above.

### Legacy Excel

In older versions of Excel that do not provide dynamic array support, or the SEQUENCE function, we need to take a different approach. One simple solution is to hardcode the numeric array given to LARGE as an [array constant](https://exceljet.net/glossary/array-constant)
 and switch to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT(LARGE(data,{1,2,3}))

This formula works fine in older versions of Excel, but because the array is hardcoded inside LARGE, it is not a dynamic solution that uses the value for **n** in cell D5. In addition, as **n** becomes larger, it gets tedious to enter longer array constants like {1,2,3,4,5,6,7,8,9}, etc. To workaround this problem, you can use the more advanced formula below.

### Dynamic n

The classic solution for creating a numeric array in older versions of Excel is to use the [ROW](https://exceljet.net/functions/row-function)
 and [INDIRECT](https://exceljet.net/functions/indirect-function)
 functions. For example, to generate a numeric array from 1 to 10, you can use a formula like this:

    =ROW(INDIRECT("1:10")) // returns {1;2;3;4;5;6;7;8;9;10}
    

The INDIRECT function converts the [text string](https://exceljet.net/glossary/text-value)
 "1:10" to the [_range_](https://exceljet.net/glossary/range)
 1:10, which is returned to the ROW function. The ROW function returns the 10 row numbers that correspond to 1:10 in an array like this:

    {1;2;3;4;5;6;7;8;9;10}
    

Note this is actually a [vertical array](https://exceljet.net/glossary/array)
, as indicated by the semicolons (;) but the LARGE function will happily accept a vertical or horizontal array for _k_. To adapt this approach in the worksheet as shown, we need to adjust the formula to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the value for **n** to the string "1:" inside of INDIRECT like this:

    =SUMPRODUCT(LARGE(data,ROW(INDIRECT("1:"&D5))))
    

This formula is now dynamic. When the value for **n** is changed, ROW and INDIRECT will spin up a new array that reflects the current value, and LARGE will extract the top **n** values as before, and SUMPRODUCT will return a sum.

Related formulas
----------------

[![Excel formula: Sum top n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20top%20n%20values%20with%20criteria.png "Excel formula: Sum top n values with criteria")](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

### [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

In this example, the goal is to sum the largest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three largest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Sum bottom n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values.png "Excel formula: Sum bottom n values")](https://exceljet.net/formulas/sum-bottom-n-values)

### [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)

In this example, the goal is to sum the smallest n values in a set of data, where n is a variable that can be easily changed. At a high level, the solution breaks down into two steps (1) extract the n smallest values from the data set and (2) sum the extracted values. This problem can be solved...

[![Excel formula: Sum bottom n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values%20with%20criteria.png "Excel formula: Sum bottom n values with criteria")](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

### [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

In this example, the goal is to sum the smallest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three smallest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20get%20nth%20values%20with%20SMALL%20and%20LARGE_thumb.png)](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

In this video we'll look at how to calculate the "nth" smallest or largest values in a range using the SMALL or LARGE function s. This would be, for example, the 1st, 2nd, and 3rd smallest or largest values. In this first sheet, we have a list of students with five test scores. I'll use the LARGE...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    
*   [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)
    
*   [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)
    
*   [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)
    

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
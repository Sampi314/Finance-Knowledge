# Average top 3 scores - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-top-3-scores

---

[Skip to main content](https://exceljet.net/formulas/average-top-3-scores#main-content)

[](https://exceljet.net/formulas/average-top-3-scores#)

*   [Previous](https://exceljet.net/formulas/average-salary-by-department)
    
*   [Next](https://exceljet.net/formulas/average-with-multiple-criteria)
    

[Average](https://exceljet.net/formulas#Average)

Average top 3 scores
====================

by Dave Bruns · Updated 2 Feb 2023

Related functions 
------------------

[LARGE](https://exceljet.net/functions/large-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7698/download?token=BVEmZxDh)
 (15.8 KB)

![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")

Summary
-------

To average the top 3 scores in a set of data, you can use the [AVERAGE function](https://exceljet.net/functions/average-function)
 with the [LARGE function](https://exceljet.net/functions/large-function)
. In the example shown, the formula in I5, copied down, is:

    =AVERAGE(LARGE(C5:F5,{1,2,3}))
    

The result in cell I5 is 10, the average of the top 3 scores for Hannah. The average in H5 is 9.5 and includes all 4 quiz scores.

Generic formula
---------------

    =AVERAGE(LARGE(range,{1,2,3}))

Explanation 
------------

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the average to only the top 3 scores. The classic solution is to use the AVERAGE function with the LARGE function as explained below.

### LARGE function

The [LARGE function](https://exceljet.net/functions/large-function)
 is designed to retrieve the "top nth value" from a set of numbers. For a given range, LARGE(range,1) will return the largest value, LARGE(range,2) will return the 2nd largest value, and so on, as seen below:

    LARGE(range,1) // 1st largest value
    LARGE(range,2) // 2nd largest value
    LARGE(range,3) // 2nd largest value
    

In this problem, we need to configure LARGE to retrieve the largest 3 values, and the easiest way to do that is to pass an [array constant](https://exceljet.net/glossary/array-constant)
  like {1,2,3} into LARGE as the second [argument](https://exceljet.net/glossary/function-argument)
, _k_. Because we are asking for the top 3 values, LARGE will return an [array](https://exceljet.net/glossary/array)
 that contains all 3 values:

    LARGE(range,{1,2,3}) // largest 3 values
    

Video: [How to use the LARGE and SMALL](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### LARGE with AVERAGE

In the example shown, the formula in cell I5 is:

    =AVERAGE(LARGE(C5:F5,{1,2,3}))

Working from the inside out, the LARGE function is configured to extract the top 3 scores from the range C5:F5 like this:

    LARGE(C5:F5,{1,2,3}) // returns {10,10,10}

Because we have provided the array constant {1,2,3} for the second argument, _k_, LARGE returns the top 3 scores in C5:F5 in an [array](https://exceljet.net/glossary/array)
 like this:

    {10,10,10}
    

This array is returned directly to the AVERAGE function:

    =AVERAGE({10,10,10}) // returns 10
    

The [AVERAGE function](https://exceljet.net/functions/average-function)
 then returns the average of these values as a final result. As the formula is copied down, it returns an average of the top 3 scores for each name in the list. Although this set of data contains only 4 scores, the formula will work correctly for any number of scores, as long as there are at least 3.

Video: [How to use the AVERAGE function](https://exceljet.net/videos/how-to-calculate-an-average-value)

### Variable n

To make this formula use a variable for **n**, where **n** represents the number of values to include in the average, you can add the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 like this:

    =AVERAGE(LARGE(C5:F5,SEQUENCE(n)))

To supply a value for **n**, you can use a cell reference like A1 or simply hardcode a number into the formula. The SEQUENCE function dynamically generates a numeric array which is then returned to LARGE as the second argument, and the formula works the same thereafter.

Video: [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

### Legacy Excel

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, the SEQUENCE function does not exist. The classic solution for creating a numeric array in older versions of Excel is to use the [ROW](https://exceljet.net/functions/row-function)
 and [INDIRECT](https://exceljet.net/functions/indirect-function)
 functions. For example, to generate a numeric array from 1 to 10, you can use a formula like this:

    =ROW(INDIRECT("1:10")) // returns {1;2;3;4;5;6;7;8;9;10}
    

The INDIRECT function converts the [text string](https://exceljet.net/glossary/text-value)
 "1:10" to the [_range_](https://exceljet.net/glossary/range)
 1:10, which is returned to the ROW function. ROW then returns an array of row numbers like {1;2;3;4;5;6;7;8;9;10}. To make **n** variable, you can concatenate the string "1:" to a cell reference that provides a value for **n**:

    =AVERAGE(LARGE(C5:F5,ROW(INDIRECT("1:"&n))))

Note that this formula is an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 and must be entered with control + shift + enter in older versions of Excel.

Related formulas
----------------

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

Related functions
-----------------

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

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
    
*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    
*   [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    

### Functions

*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

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
# Large with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/large-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/large-with-criteria#main-content)

[](https://exceljet.net/formulas/large-with-criteria#)

*   [Previous](https://exceljet.net/formulas/first-in-last-out-times)
    
*   [Next](https://exceljet.net/formulas/larger-of-two-values)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Large with criteria
===================

by Dave Bruns · Updated 8 Mar 2023

Related functions 
------------------

[LARGE](https://exceljet.net/functions/large-function)

[FILTER](https://exceljet.net/functions/filter-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Large with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/large_with_criteria.png "Excel formula: Large with criteria")

Summary
-------

To return the largest values in a set of data that meet specific criteria you can use a formula based on the [LARGE function](https://exceljet.net/functions/large-function)
 with the [FILTER function](https://exceljet.net/functions/filter-function)
. In the example shown, the formula in F7 is:

    =LARGE(FILTER(value,group=$F$4),E7)

where **group** (B5:B16) and **value** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. As the formula is copied down, it returns the top 3 values in group A, using the value in F4 ("A") for group and the value in column E to determine the "nth" largest value.

Generic formula
---------------

    =LARGE(FILTER(values,criteria),n)

Explanation 
------------

In this example, the goal is to display the top 3 values in C5:C16 that match a specific group, entered as a variable in cell F4. If the group is changed, the formulas should calculate new results. For convenience, **group** (B5:B16) and **value** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. The core of the solution is the LARGE function, which can be used to retrieve the "nth" largest value in a set of data. The challenge is that the LARGE function does not offer any direct way to apply criteria to the values being processed. This means we need to create our own logic to apply conditions in a separate step.

There are two basic ways to approach this problem. In the current version of Excel, you can use the FILTER function to apply conditions to data before it is delivered to LARGE. In older versions of Excel, you can use the IF function in an array formula. Both approaches are explained below.

### LARGE function

The [LARGE function](https://exceljet.net/functions/large-function)
 can be used to return the nth largest value in a set of data. The generic syntax for LARGE looks like this:

    =LARGE(range,n)
    

where **n** is a number like 1, 2, 3, etc. For example, you can retrieve the first, second, and third largest values like this:

    =LARGE(range,1) // first largest
    =LARGE(range,2) // second largest
    =LARGE(range,3) // third largest

The challenge in this problem is that LARGE has no built-in way to apply criteria. One way to apply criteria is with the FILTER function, as described in the next section below.

### LARGE with FILTER

In the current version of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
 can be used to apply criteria _inside_ of LARGE. This is the approach used in the worksheet shown, where the formula in F7 is:

    =LARGE(FILTER(value,group=$F$4),E7)

Working from the inside out, the FILTER function is configured to extract values for the group entered in F4 like this:

    =FILTER(value,group=$F$4)

Inside FILTER, _array_ is given as **value** (C5:C16), and the _include_ [argument](https://exceljet.net/glossary/function-argument)
 is provided as an expression that compares each value in **group** (B5:B16) to the value in F4 ("A"). Note that $F$4 is an [absolute reference](https://exceljet.net/glossary/absolute-reference)
, because we don't want this reference to change when the formula is copied down column F. Since there are 12 values in B5:B16, the expression returns an [array](https://exceljet.net/glossary/array)
 that contains 12 TRUE and FALSE values like this:

    {TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}

The TRUE values indicate rows where the group equals "A". This array is used by FILTER to extract matching values. The result from FILTER is an array that contains the 6 values in the data in group "A":

    {100;70;50;85;91;96}

These values are provided to the LARGE function as the _array_ argument. The second argument, _k_, comes from cell E7:

    =LARGE({100;70;50;85;91;96},E7)
    =LARGE({100;70;50;85;91;96},1)
    =100

As the formula is copied down, the value for _k_ changes and LARGE returns the 1st, 2nd, and 3rd largest numbers in group A.

### LARGE with IF

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, the FILTER function does not exist so we do not have a dedicated function to filter values by group. Instead, we can use a traditional [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 based on the [IF function](https://exceljet.net/functions/if-function)
 like this:

    {=LARGE(IF(group=$F$4,value),E7)}

_Note: this is an array formula and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

In this formula, the IF function provides the same purpose as the FILTER function above: it "filters" the values by group. Since we are running a logical test on a _range_ of cells (B5:B16), we get an _array_ of results. The array returned by IF looks like this:

    {100;FALSE;70;FALSE;50;FALSE;85;FALSE;91;FALSE;96;FALSE}

Note that only values in group A make it into the array. Group B values become FALSE since they fail the logical test. This array is returned directly to the LARGE function as the _array_ argument. The value for _k_ comes from cell E7:

    =LARGE({100;FALSE;70;FALSE;50;FALSE;85;FALSE;91;FALSE;96;FALSE},E7)
    =LARGE({100;FALSE;70;FALSE;50;FALSE;85;FALSE;91;FALSE;96;FALSE},1)
    =100

LARGE automatically ignores the FALSE values and returns the largest number in the remaining values, which is 100.

### Multiple criteria

To take into account multiple criteria, you can extend the formula with [boolean logic](https://exceljet.net/glossary/boolean-logic)
. With FILTER, the generic formula looks like this:

    =LARGE(FILTER(data,(criteria1)*(criteria2),n)
    

Where _criteria1_ and _criteria2_ represent expressions to test specific conditions. In older versions of Excel, you can use the same approach like this:

    =LARGE(IF((criteria1)*(criteria2),values),n)
    

For more information on using Boolean logic in array formulas, see the video below.

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

Related formulas
----------------

[![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")](https://exceljet.net/formulas/nth-largest-value)

### [nth largest value](https://exceljet.net/formulas/nth-largest-value)

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function. Note...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: nth smallest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value_with_criteria.png "Excel formula: nth smallest value with criteria")](https://exceljet.net/formulas/nth-smallest-value-with-criteria)

### [nth smallest value with criteria](https://exceljet.net/formulas/nth-smallest-value-with-criteria)

In this example, the goal is to retrieve the lowest 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the SMALL function, which can be used to retrieve the "nth"...

[![Excel formula: nth largest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value_with_criteria.png "Excel formula: nth largest value with criteria")](https://exceljet.net/formulas/nth-largest-value-with-criteria)

### [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)

In this example, the goal is to retrieve the top 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the LARGE function, which can be used to retrieve the "nth" largest...

Related functions
-----------------

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

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

*   [nth largest value](https://exceljet.net/formulas/nth-largest-value)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [nth smallest value with criteria](https://exceljet.net/formulas/nth-smallest-value-with-criteria)
    
*   [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    

### Functions

*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)
    

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
# nth smallest value with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nth-smallest-value-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/nth-smallest-value-with-criteria#main-content)

[](https://exceljet.net/formulas/nth-smallest-value-with-criteria#)

*   [Previous](https://exceljet.net/formulas/nth-smallest-value)
    
*   [Next](https://exceljet.net/formulas/smaller-of-two-values)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

nth smallest value with criteria
================================

by Dave Bruns · Updated 24 Feb 2023

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

![Excel formula: nth smallest value with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nth_smallest_value_with_criteria.png "Excel formula: nth smallest value with criteria")

Summary
-------

To return the nth smallest value that meet specific conditions you can use a formula based on the [SMALL function](https://exceljet.net/functions/small-function)
 with the [FILTER function](https://exceljet.net/functions/filter-function)
. In the example shown, the formula in G8 is:

    =SMALL(FILTER(data[Score],data[Group]=$F$5),F8)

where all data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
 called **data** in the range B5:D16. As the formula is copied down, it returns the lowest 3 scores in group A, using the value in F5 ("A") for group and the value in column F for _n_.

_Note: FILTER is a newer function in Excel. See below for a formula that will work in older versions._

Generic formula
---------------

    =SMALL(FILTER(data,criteria),n)

Explanation 
------------

In this example, the goal is to retrieve the lowest 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the SMALL function, which can be used to retrieve the "nth" smallest value in a set of data. The challenge is that the SMALL function does not offer any direct way to apply criteria before calculating a result, so we need to create our own logic to apply criteria.

There are two basic ways to approach this problem. In the [current version](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 of Excel, you can use the FILTER function to apply conditions to data before it is delivered to SMALL. In older versions of Excel, you can use the IF function in a traditional array formula. Both approaches are explained below.

### Excel Table

For convenience, all data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
 named **data** in the range B5:D16. Excel Tables are a convenient way to work with data in Excel because they (1) automatically expand to include new data and (2) offer [structured references](https://exceljet.net/videos/introduction-to-structured-references)
, which let you refer to data by name instead of by address. If you are new to Excel Tables, [this article provides an overview](https://exceljet.net/articles/excel-tables)
. Also see this short video:

Video: [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

### SMALL function

The [SMALL function](https://exceljet.net/functions/small-function)
 is used to return the nth smallest value in a set of data like this:

    =SMALL(range,n)
    

where **n** is a number like 1, 2, 3, etc. For example, you can retrieve the first, second, and third smallest values like this:

    =SMALL(range,1) // first smallest
    =SMALL(range,2) // second smallest
    =SMALL(range,3) // third smallest

The challenge in this problem is that SMALL has no built-in way to apply criteria. A good way to apply criteria is with the FILTER function, as described in the next section.

### SMALL with FILTER

In the current version of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
 can be used to apply criteria _inside_ of SMALL. This is the approach used in the worksheet shown, where the formula in G8 is:

    =SMALL(FILTER(data[Score],data[Group]=$F$5),F8)

Working from the inside out, the FILTER function is configured to extract scores for the group in F5 like this:

    FILTER(data[Score],data[Group]=$F$5)

Inside FILTER, _array_ is given as the Score column, and the _include_ [argument](https://exceljet.net/glossary/function-argument)
 is provided as an expression that compares each value in the Group column to the value in F5 ("A"). Note that $F$5 is an [absolute reference](https://exceljet.net/glossary/absolute-reference)
, because we don't want this reference to change when the formula is copied down column G. Since there are 12 values in C5:C16, the expression returns an [array](https://exceljet.net/glossary/array)
 with 12 TRUE and FALSE values like this:

    {TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}

The TRUE values indicate rows where the group equals "A". This array is used by FILTER to retrieve matching data. The result from FILTER is an array that contains the 6 values in group "A":

    {90;83;74;87;79;72}

These values are provided to the SMALL function as the _array_ argument. The second argument, _k_, comes from cell F8:

    =SMALL({90;83;74;87;79;72},F8)
    =SMALL({90;83;74;87;79;72},1)
    =72

In cell G8, the result is 72, the lowest score in group A. As the formula is copied down, the value for _k_ changes and SMALL returns the second and third lowest scores in group A.

### SMALL with IF

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, the FILTER function does not exist, so we need a different approach. The classic solution is to use a traditional [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 based on the [IF function](https://exceljet.net/functions/if-function)
:

    =SMALL(IF(data[Group]=$F$5,data[Score]),F8)

_Note: this is an array formula and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

In this formula, the IF function serves the same purpose as the FILTER function: it "filters" the values by group. Since we are running a logical test on 12 separate values in the Group column (C5:C16), we get an _array_ that contains 12 results like this:

    {90;FALSE;83;FALSE;74;FALSE;87;FALSE;79;FALSE;72;FALSE}

Notice that only values in group A make it into the array. The values in group B become FALSE when they fail the logical test. This array is returned directly to the SMALL function as the _array_ argument. The value for _k_ comes from cell F8:

    =SMALL({90;FALSE;83;FALSE;74;FALSE;87;FALSE;79;FALSE;72;FALSE},F8)
    =SMALL({90;FALSE;83;FALSE;74;FALSE;87;FALSE;79;FALSE;72;FALSE},1)
    =72

SMALL automatically ignores the FALSE values and returns the smallest number in the remaining values, which is 72. As the formula is copied down, the value for _k_ changes and SMALL returns the second and third smallest values in group A.

### Multiple criteria

To apply multiple criteria, you can extend the formula with [boolean logic](https://exceljet.net/glossary/boolean-logic)
. With FILTER, the generic formula looks like this:

    =SMALL(FILTER(data,(criteria1)*(criteria2),n)
    

Where _criteria1_ and _criteria2_ are logical expressions to test specific conditions.

Video: [FILTER function with two criteria](https://exceljet.net/videos/filter-function-with-two-criteria)

 In older versions of Excel, you can use the same idea with the IF function like this:

    =SMALL(IF((criteria1)*(criteria2),values),n)
    

For more information on using Boolean logic in array formulas, see the video below.

> Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

Related formulas
----------------

[![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")](https://exceljet.net/formulas/nth-largest-value)

### [nth largest value](https://exceljet.net/formulas/nth-largest-value)

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function. Note...

[![Excel formula: nth smallest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value.png "Excel formula: nth smallest value")](https://exceljet.net/formulas/nth-smallest-value)

### [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)

In this example, the goal is to extract the 3 best race times for each name from the 5 race times that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the fastest time, the 2nd fastest time, and the 3rd fastest time. This problem can be solved with the SMALL...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: nth largest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value_with_criteria.png "Excel formula: nth largest value with criteria")](https://exceljet.net/formulas/nth-largest-value-with-criteria)

### [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)

In this example, the goal is to retrieve the top 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the LARGE function, which can be used to retrieve the "nth" largest...

[![Excel formula:  Highlight 3 smallest values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%203%20smallest%20values%20with%20criteria_0.png "Excel formula:  Highlight 3 smallest values with criteria")](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)

### [Highlight 3 smallest values with criteria](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)

Inside the AND function there are two logical criteria. The first is straightforward, and ensures that only cells that match the color in E5 are highlighted: $B3=$E$5 The second test is more complex: $C3<=SMALL(IF(color=$E$5,amount),3) Here, we filter amounts to make sure that only values...

Related functions
-----------------

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20get%20nth%20values%20with%20SMALL%20and%20LARGE_thumb.png)](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

In this video we'll look at how to calculate the "nth" smallest or largest values in a range using the SMALL or LARGE function s. This would be, for example, the 1st, 2nd, and 3rd smallest or largest values. In this first sheet, we have a list of students with five test scores. I'll use the LARGE...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-create-an-excel-table)

### [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

In this video, we'll look at how to create an Excel table. Here we have some data that is a good candidate for a table. Each row represents an entry or record with information that belongs together. Each column has a unique name. The first step in creating a table is to remove any blank rows or...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

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
    
*   [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    
*   [Highlight 3 smallest values with criteria](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)
    

### Functions

*   [SMALL Function](https://exceljet.net/functions/small-function)
    

### Videos

*   [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)
    
*   [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

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
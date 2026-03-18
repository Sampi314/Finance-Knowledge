# Excel LARGE function | Exceljet

**Source:** https://exceljet.net/functions/large-function

---

[Skip to main content](https://exceljet.net/functions/large-function#main-content)

[](https://exceljet.net/functions/large-function#)

*   [Previous](https://exceljet.net/functions/intercept-function)
    
*   [Next](https://exceljet.net/functions/linest-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

LARGE Function
==============

by Dave Bruns · Updated 13 Oct 2021

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[SMALL](https://exceljet.net/functions/small-function)

[RANK](https://exceljet.net/functions/rank-function)

![Excel LARGE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")

Summary
-------

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

Purpose 
--------

Get nth largest value

Return value 
-------------

The nth largest value in an array.

Syntax
------

    =LARGE(array,k)

*   _array_ - An array or range of numeric values.
*   _k_ - Position as an integer, where 1 corresponds to the largest value.

Using the LARGE function 
-------------------------

The LARGE function returns a numeric value based on its position in a list when sorted by value. In other words, LARGE returns the "nth largest" value in the list where 1 corresponds to the largest value, 2 corresponds to the second largest value, etc. For example, the LARGE function is useful when you want to retrieve first, second, or third highest scores for a test. 

The LARGE function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _array_ and k. _Array_ is an [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
 of numeric values. The argument _k_ represents position or rank. For example, to return the largest value in _array_, provide 1 for _k_. To return the fifth largest value in _array_, provide 5 for _k_.

To get nth _smallest_ values, see the [](https://exceljet.net/functions/small-function)
[SMALL](https://exceljet.net/functions/small-function)
 [function](https://exceljet.net/functions/small-function)
.

### Examples

In the formula below, the LARGE function returns the third largest value in a list of five numbers provided in an [array constant](https://exceljet.net/glossary/array-constant)
:

    =LARGE({29,14,33,19,17},3) // returns 19
    

Note values do not need to be sorted. To retrieve the 1st, 2nd, and 3rd largest values in a range:

    =LARGE(range,1) // 1st largest value
    =LARGE(range,2) // 2nd largest value
    =LARGE(range,3) // 3rd largest value
    

In the example shown, the formulas in G5, G6, and G7 are, respectively:

    =LARGE(D5:D16,1) // returns 92
    =LARGE(D5:D16,2) // returns 89
    =LARGE(D5:D16,3) // returns 86
    

See below for more advanced formulas based on the LARGE function.

### Notes

*   LARGE ignores empty cells, text values, and TRUE and FALSE values.
*   If _array_ contains no numeric values, LARGE returns a #NUM! error.
*   To determine the rank of a number in a data set, use the [RANK function](https://exceljet.net/functions/rank-function)
    .

LARGE function examples
-----------------------

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

[![Excel formula: Name of nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value.png "Excel formula: Name of nth largest value")](https://exceljet.net/formulas/name-of-nth-largest-value)

### [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)

In a nutshell, this formula uses the LARGE function to find the nth largest value in a set of data. Once we have that value, we plug it into a standard INDEX and MATCH formula to retrieve the associated name. In other words, we use the nth largest value like a "key" to retrieve associated...

[![Excel formula: Large with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/large_with_criteria.png "Excel formula: Large with criteria")](https://exceljet.net/formulas/large-with-criteria)

### [Large with criteria](https://exceljet.net/formulas/large-with-criteria)

In this example, the goal is to display the top 3 values in C5:C16 that match a specific group, entered as a variable in cell F4. If the group is changed, the formulas should calculate new results. For convenience, group (B5:B16) and value (C5:C16) are named ranges . The core of the solution is the...

[![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")](https://exceljet.net/formulas/nth-largest-value)

### [nth largest value](https://exceljet.net/formulas/nth-largest-value)

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function. Note...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: FILTER on top n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values%20with%20criteria.png "Excel formula: FILTER on top n values with criteria")](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria)

### [FILTER on top n values with criteria](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE and IF functions. The result is the top 3 scores in group B. The FILTER function applies criteria with the include argument. In this example, criteria are constructed with boolean logic like...

[![Excel formula: Rank values by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/display%20ranked%20names%20by%20month.png "Excel formula: Rank values by month")](https://exceljet.net/formulas/rank-values-by-month)

### [Rank values by month](https://exceljet.net/formulas/rank-values-by-month)

This example is set up in two parts for clarity: (1) a formula to determine the top 3 amounts for each month and (2) a formula to retrieve the client name for each of the top 3 monthly amounts. Note there is no actual rank in the source data. Instead, we are using the LARGE function to work...

[![Excel formula: Maximum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value.png "Excel formula: Maximum value")](https://exceljet.net/formulas/maximum-value)

### [Maximum value](https://exceljet.net/formulas/maximum-value)

In this example, the goal is to get the maximum quiz score (i.e. the best quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MAX function or the LARGE function, as explained below. MAX function The MAX function accepts...

[![Excel formula: FILTER on top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values.png "Excel formula: FILTER on top n values")](https://exceljet.net/formulas/filter-on-top-n-values)

### [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE function. The LARGE function is a simple way to get the nth largest value in a range. Simply provide a range for the first argument ( array ), and a value for n as the second argument ( k ): =...

[![Excel formula: Sum top n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20top%20n%20values%20with%20criteria.png "Excel formula: Sum top n values with criteria")](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

### [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

In this example, the goal is to sum the largest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three largest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Name of nth largest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value%20with%20criteria.png "Excel formula: Name of nth largest value with criteria")](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)

### [Name of nth largest value with criteria](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)

The LARGE function is an easy way to get the nth largest value in a range: =LARGE(range,1) // 1st largest =LARGE(range,2) // 2nd largest =LARGE(range,3) // 3rd largest In this example, we can use the LARGE function to get a highest score, then use the score like a "key" to retrieve the associated...

[![Excel formula: Sort numbers ascending or descending](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20numbers%20ascending%20or%20descending.png "Excel formula: Sort numbers ascending or descending")](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

### [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

The SMALL function is meant to extract the "nth" smallest value from a set of data. The value for N is supplied as the second argument. To get the smallest value with SMALL, supply 1, to get the second smallest value, supply 2, and so on. =SMALL(data,1) // 1st smallest =SMALL(data,2) // 2nd...

[![Excel formula: Highlight top values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20top%20values.png "Excel formula: Highlight top values")](https://exceljet.net/formulas/highlight-top-values)

### [Highlight top values](https://exceljet.net/formulas/highlight-top-values)

This formula uses two named ranges: data (B4:G11) and input (F2). These are for readability and convenience only. If you don't want to use named ranges, make sure you use absolute references for both of these ranges in the formula. This formula is based on the LARGE function , which returns the nth...

[![Excel formula: nth largest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value_with_criteria.png "Excel formula: nth largest value with criteria")](https://exceljet.net/formulas/nth-largest-value-with-criteria)

### [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)

In this example, the goal is to retrieve the top 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the LARGE function, which can be used to retrieve the "nth" largest...

LARGE function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20get%20nth%20values%20with%20SMALL%20and%20LARGE_thumb.png)](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

In this video we'll look at how to calculate the "nth" smallest or largest values in a range using the SMALL or LARGE function s. This would be, for example, the 1st, 2nd, and 3rd smallest or largest values. In this first sheet, we have a list of students with five test scores. I'll use the LARGE...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20maximum%20and%20minimum%20values-thumb.png)](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

### [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

In this video we'll look at how to calculate minimum and maximum values in Excel. Let's take a look. Here we have a list of properties, that includes an address, a price, and a variety of other information. Let's calculate the maximum and minimum values in this list. First, I'm going to create a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20show%20top%20or%20bottom%20results-Play.png)](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)

### [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)

In this video, we'll use the FILTER function to show the top or bottom results in a set of data. Here we have some test scores for a group of students. In column F, I want to set up a formula to display the top students by score. Now, I'm going to use the FILTER function, but we'll need a way to...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

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
    
*   [FILTER on top n values with criteria](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria)
    
*   [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    
*   [Name of nth largest value with criteria](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)
    
*   [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    
*   [Maximum value](https://exceljet.net/formulas/maximum-value)
    
*   [Biggest gainers and losers](https://exceljet.net/formulas/biggest-gainers-and-losers)
    
*   [Large with criteria](https://exceljet.net/formulas/large-with-criteria)
    
*   [Highlight top values](https://exceljet.net/formulas/highlight-top-values)
    

### Videos

*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    
*   [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)
    
*   [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    

### Links

*   [Microsoft LARGE function documentation](https://support.office.com/en-us/article/large-function-3af0af19-1190-42bb-bb8b-01672ec00a64)
    

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
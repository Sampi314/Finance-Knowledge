# Excel SMALL function | Exceljet

**Source:** https://exceljet.net/functions/small-function

---

[Skip to main content](https://exceljet.net/functions/small-function#main-content)

[](https://exceljet.net/functions/small-function#)

*   [Previous](https://exceljet.net/functions/slope-function)
    
*   [Next](https://exceljet.net/functions/standardize-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

SMALL Function
==============

by Dave Bruns · Updated 1 Dec 2021

Related functions 
------------------

[LARGE](https://exceljet.net/functions/large-function)

[RANK](https://exceljet.net/functions/rank-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel SMALL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")

Summary
-------

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

Purpose 
--------

Get nth smallest value

Return value 
-------------

The nth smallest value in the array.

Syntax
------

    =SMALL(array,k)

*   _array_ - An array or range of numeric values.
*   _k_ - Position as an integer, where 1 corresponds to the smallest value.

Using the SMALL function 
-------------------------

The SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

The SMALL function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _array_ and _k_. _Array_ is an [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
 of numeric values. The argument _k_ represents position or rank. For example, to return the smallest value in _array_, provide 1 for _k_. To return the fifth smallest value in _array_, provide 5 for _k_.

To get nth _largest_ values, see the [LARGE function](https://exceljet.net/functions/large-function)
.

### Examples

In the formula below, the SMALL function returns the third smallest value in a list of five numbers provided in an [array constant](https://exceljet.net/glossary/array-constant)
:

    =SMALL({29,14,33,19,17},3) // returns 19
    

Note values do not need to be sorted. To retrieve the 1st, 2nd, and 3rd smallest values in a range:

    =SMALL(range,1) // 1st smallest value
    =SMALL(range,2) // 2nd smallest value
    =SMALL(range,3) // 3rd smallest value
    

In the example shown, the formulas in G5, G6, and G7 are, respectively:

    =SMALL(D5:D16,1) // returns 66
    =SMALL(D5:D16,2) // returns 69
    =SMALL(D5:D16,3) // returns 71
    

See below for more advanced formulas based on the SMALL function.

### Notes

*   SMALL ignores empty cells, text values, and TRUE and FALSE values.
*   If _array_ contains no numeric values, SMALL returns a #NUM! error.
*   To determine the rank of a number in a data set, use the [RANK function](https://exceljet.net/functions/rank-function)
    .

SMALL function examples
-----------------------

[![Excel formula: Get nth match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match.png "Excel formula: Get nth match")](https://exceljet.net/formulas/get-nth-match)

### [Get nth match](https://exceljet.net/formulas/get-nth-match)

The goal is to retrieve the nth matching record in a set of data, after filtering on a specific product. In the worksheet shown, the product in H4 and the value for n in H5 are inputs that can be changed at any time. For instance, if the product in H4 is "A" and the value in H5 is 3, the formula...

[![Excel formula: Sum bottom n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values%20with%20criteria.png "Excel formula: Sum bottom n values with criteria")](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

### [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)

In this example, the goal is to sum the smallest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three smallest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Highlight bottom values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20bottom%20values.png "Excel formula: Highlight bottom values")](https://exceljet.net/formulas/highlight-bottom-values)

### [Highlight bottom values](https://exceljet.net/formulas/highlight-bottom-values)

In this example, the goal is to highlight the 5 bottom values in B4:G11 where the number 5 is a variable set in cell F2. This formula uses two named ranges: data (B4:G11) and input (F2). These are for readability and convenience only. If you don't want to use named ranges, make sure you use...

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Minimum value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value.png "Excel formula: Minimum value")](https://exceljet.net/formulas/minimum-value)

### [Minimum value](https://exceljet.net/formulas/minimum-value)

In this example, the goal is to get the minimum quiz score (i.e. the lowest quiz score) for each person listed in column B from the five quiz scores that appear in columns C through G. This is a job for the MIN function or the SMALL function, as explained below. MIN function The MIN function...

[![Excel formula: Sum bottom n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values.png "Excel formula: Sum bottom n values")](https://exceljet.net/formulas/sum-bottom-n-values)

### [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)

In this example, the goal is to sum the smallest n values in a set of data, where n is a variable that can be easily changed. At a high level, the solution breaks down into two steps (1) extract the n smallest values from the data set and (2) sum the extracted values. This problem can be solved...

[![Excel formula: Biggest gainers and losers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/biggest%20gainers%20and%20losers.png "Excel formula: Biggest gainers and losers")](https://exceljet.net/formulas/biggest-gainers-and-losers)

### [Biggest gainers and losers](https://exceljet.net/formulas/biggest-gainers-and-losers)

In this example, the goal is to display the biggest 3 gainers and losers in a set of data where Start and End columns contain values at two points in time, and Change contains the percentage change in the values. The data in B5:E16 is defined as an Excel Table with the name data . Two formulas are...

[![Excel formula: Find lowest n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Find%20lowest%20n%20values.png "Excel formula: Find lowest n values")](https://exceljet.net/formulas/find-lowest-n-values)

### [Find lowest n values](https://exceljet.net/formulas/find-lowest-n-values)

The SMALL function retrieves the smallest values from data based on a given rank. For example: =SMALL(range,1) // smallest =SMALL(range,2) // 2nd smallest =SMALL(range,3) // 3rd smallest In the worksheet shown, the rank (which is provided to SMALL as the k argument) comes from numbers in column E...

[![Excel formula: nth smallest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value.png "Excel formula: nth smallest value")](https://exceljet.net/formulas/nth-smallest-value)

### [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)

In this example, the goal is to extract the 3 best race times for each name from the 5 race times that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the fastest time, the 2nd fastest time, and the 3rd fastest time. This problem can be solved with the SMALL...

[![Excel formula: Sort numbers ascending or descending](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20numbers%20ascending%20or%20descending.png "Excel formula: Sort numbers ascending or descending")](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

### [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

The SMALL function is meant to extract the "nth" smallest value from a set of data. The value for N is supplied as the second argument. To get the smallest value with SMALL, supply 1, to get the second smallest value, supply 2, and so on. =SMALL(data,1) // 1st smallest =SMALL(data,2) // 2nd...

[![Excel formula: Multiple matches into separate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_rows.png "Excel formula: Multiple matches into separate rows")](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

### [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

In this example, the goal is to get all names in a given group into separate rows grouped by column, as seen in the worksheet above. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns where each column holds the names that belong to a...

[![Excel formula: Break ties with helper column and COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/break%20ties%20with%20helper%20column%20and%20COUNTIF.png "Excel formula: Break ties with helper column and COUNTIF")](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)

### [Break ties with helper column and COUNTIF](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)

In this example, the goal is to retrieve information about the lowest three estimates in the data shown. The problem is that there are some duplicate values in the estimate column. This means we will have some trouble trying to display the names of the 2nd and 3rd lowest suppliers because the tie...

[![Excel formula:  Highlight 3 smallest values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%203%20smallest%20values%20with%20criteria_0.png "Excel formula:  Highlight 3 smallest values with criteria")](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)

### [Highlight 3 smallest values with criteria](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)

Inside the AND function there are two logical criteria. The first is straightforward, and ensures that only cells that match the color in E5 are highlighted: $B3=$E$5 The second test is more complex: $C3<=SMALL(IF(color=$E$5,amount),3) Here, we filter amounts to make sure that only values...

[![Excel formula: Multiple matches into separate columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_columns.png "Excel formula: Multiple matches into separate columns")](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

### [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

In this example, the goal is to get all names in a given group into the same row, in separate columns, as seen in the worksheet. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns using common values, which in this case are the group...

[![Excel formula: nth smallest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value_with_criteria.png "Excel formula: nth smallest value with criteria")](https://exceljet.net/formulas/nth-smallest-value-with-criteria)

### [nth smallest value with criteria](https://exceljet.net/formulas/nth-smallest-value-with-criteria)

In this example, the goal is to retrieve the lowest 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the SMALL function, which can be used to retrieve the "nth"...

SMALL function videos
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

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)
    
*   [Biggest gainers and losers](https://exceljet.net/formulas/biggest-gainers-and-losers)
    
*   [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)
    
*   [Get nth match](https://exceljet.net/formulas/get-nth-match)
    
*   [Break ties with helper column and COUNTIF](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)
    
*   [Highlight 3 smallest values with criteria](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)
    
*   [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)
    
*   [Highlight bottom values](https://exceljet.net/formulas/highlight-bottom-values)
    
*   [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)
    
*   [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    

### Videos

*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    
*   [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)
    
*   [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)
    

### Functions

*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

### Links

*   [Microsoft SMALL function documentation](https://support.office.com/en-us/article/small-function-17da8222-7c82-42b2-961b-14c45384df07)
    

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
# Name of nth largest value with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria#main-content)

[](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria#)

*   [Previous](https://exceljet.net/formulas/name-of-nth-largest-value)
    
*   [Next](https://exceljet.net/formulas/nth-largest-value)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Name of nth largest value with criteria
=======================================

by Dave Bruns · Updated 29 Mar 2023

Related functions 
------------------

[LARGE](https://exceljet.net/functions/large-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[IF](https://exceljet.net/functions/if-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

![Excel formula: Name of nth largest value with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/name%20of%20nth%20largest%20value%20with%20criteria.png "Excel formula: Name of nth largest value with criteria")

Summary
-------

To get the name of the nth largest value with criteria, you can use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, the [LARGE function](https://exceljet.net/functions/large-function)
, and a filter created with the [IF function](https://exceljet.net/videos/the-if-function)
. In the example shown, the formula in cell G5, copied down, is:

    =INDEX(name,MATCH(LARGE(IF(group="A",score),F5),IF(group="A",score),0))
    

where **name** (B5:B16), **group** (C5:C16), and **score** (D5:D16) are [named ranges](https://exceljet.net/glossary/named-range)
. The formula returns the name associated with the 1st, 2nd, and 3rd highest values in Group A.

_Note: This is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Generic formula
---------------

    =INDEX(range,MATCH(LARGE(filtered_range,F5),filtered_range,0))

Explanation 
------------

The LARGE function is an easy way to get the nth largest value in a range:

     =LARGE(range,1) // 1st largest
     =LARGE(range,2) // 2nd largest
     =LARGE(range,3) // 3rd largest
    

In this example, we can use the LARGE function to get a highest score, then use the score like a "key" to retrieve the associated name with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. Notice we are picking up the values for **n** from the range F5:F7, in order to get the 1st, 2nd, and 3rd highest scores.

The twist however in this case is that we need to distinguish between scores in group A and group B. In other words, we need to _apply criteria_. We do this with the IF function, which is used to "filter" values before they are evaluated with LARGE. As a generic example, to get the largest value (i.e. 1st value) in range2 where range 1 = "A", you can use a formula like this:

    LARGE(IF(range="A",range2),1)
    

_Note: using IF this way makes this an [array formula](https://exceljet.net/glossary/array-formula)
._

Working from the inside out, the first step is to get the "1st" largest value in the data associated with Group A with the LARGE function:

    LARGE(IF(group="A",score),F5)
    

In this case, the value in F5 is 1, so we are asking for the top score in Group A. When the IF function is evaluated, it tests each value in the named range **group**. The named range **score** is provided for _value\_if\_true_. This generates a new [array](https://exceljet.net/glossary/array)
, which is returned directly to the LARGE function:

    LARGE({79;FALSE;93;FALSE;83;FALSE;67;FALSE;85;FALSE;69;FALSE},1)
    

Notice the only scores that survive the filter are from Group A. LARGE then returns the highest remaining score, 93, directly to the MATCH function as a lookup value. We can now simplify the formula to:

    =INDEX(name,MATCH(93,IF(group="A",score),0))
    

Now we can see that the [MATCH function](https://exceljet.net/functions/match-function)
 is configured to use the same filtered array we saw above. The IF function again filters out unwanted values, and the MATCH portion of the formula resolves to:

    MATCH(93,{79;FALSE;93;FALSE;83;FALSE;67;FALSE;85;FALSE;69;FALSE},0)
    

Since 93 appears in the 3rd position, MATCH returns 3 directly to the [INDEX function](https://exceljet.net/functions/index-function)
:

    =INDEX(name,3) // Hannah
    

Finally, the INDEX function returns the name in the 3rd row, "Hannah".

### With XLOOKUP

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 can also be used to solve this problem, using the same approach explained above:

    =XLOOKUP(LARGE(IF(group="A",score),F5),IF(group="A",score),name)
    

As above, LARGE is configured to work with an array filtered by IF, and returns a result of 93 to XLOOKUP as the lookup value:

    =XLOOKUP(93,IF(group="A",score),name) // Hannah
    

The lookup array is also created by using IF as a filter on scores from Group A. With the return array provided as **name** (B5:B16). XLOOKUP returns "Hannah" as the final result.

### Notes

1.  To get the name of nth value _with criteria_, (i.e. limit results to group A or B) you will need to [extend the formula to use additional logic](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)
    .
2.  In [Excel 365](https://exceljet.net/glossary/excel-365)
    , the [FILTER function](https://exceljet.net/functions/filter-function)
     is a better way to [list top or bottom results dynamically](https://exceljet.net/formulas/filter-on-top-n-values)
    . This approach will automatically handle ties.

Related formulas
----------------

[![Excel formula: Name of nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value.png "Excel formula: Name of nth largest value")](https://exceljet.net/formulas/name-of-nth-largest-value)

### [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)

In a nutshell, this formula uses the LARGE function to find the nth largest value in a set of data. Once we have that value, we plug it into a standard INDEX and MATCH formula to retrieve the associated name. In other words, we use the nth largest value like a "key" to retrieve associated...

[![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")](https://exceljet.net/formulas/nth-largest-value)

### [nth largest value](https://exceljet.net/formulas/nth-largest-value)

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function. Note...

[![Excel formula: nth largest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value_with_criteria.png "Excel formula: nth largest value with criteria")](https://exceljet.net/formulas/nth-largest-value-with-criteria)

### [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)

In this example, the goal is to retrieve the top 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the LARGE function, which can be used to retrieve the "nth" largest...

[![Excel formula: nth smallest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value.png "Excel formula: nth smallest value")](https://exceljet.net/formulas/nth-smallest-value)

### [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)

In this example, the goal is to extract the 3 best race times for each name from the 5 race times that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the fastest time, the 2nd fastest time, and the 3rd fastest time. This problem can be solved with the SMALL...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: FILTER on top n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values%20with%20criteria.png "Excel formula: FILTER on top n values with criteria")](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria)

### [FILTER on top n values with criteria](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE and IF functions. The result is the top 3 scores in group B. The FILTER function applies criteria with the include argument. In this example, criteria are constructed with boolean logic like...

Related functions
-----------------

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

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

*   [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)
    
*   [nth largest value](https://exceljet.net/formulas/nth-largest-value)
    
*   [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    
*   [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [FILTER on top n values with criteria](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria)
    

### Functions

*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

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
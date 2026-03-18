# Name of nth largest value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/name-of-nth-largest-value

---

[Skip to main content](https://exceljet.net/formulas/name-of-nth-largest-value#main-content)

[](https://exceljet.net/formulas/name-of-nth-largest-value#)

*   [Previous](https://exceljet.net/formulas/minimum-value-if)
    
*   [Next](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Name of nth largest value
=========================

by Dave Bruns · Updated 30 Aug 2020

Related functions 
------------------

[LARGE](https://exceljet.net/functions/large-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6272/download?token=NS_zPX24)
 (16.33 KB)

![Excel formula: Name of nth largest value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/name%20of%20nth%20largest%20value.png "Excel formula: Name of nth largest value")

Summary
-------

To get the name of the nth largest value, you can use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 with the [LARGE function](https://exceljet.net/functions/large-function)
. In the example shown, the formula in cell H5 is:

    =INDEX(name,MATCH(LARGE(score,F5),score,0))
    

where **name** (B5:B16), and **score** (D5:D16) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =INDEX(names,MATCH(LARGE(values,F5),values,0))

Explanation 
------------

In a nutshell, this formula uses the LARGE function to find the nth largest value in a set of data. Once we have that value, we plug it into a standard [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula to retrieve the associated name. In other words, we use the nth largest value like a "key" to retrieve associated information.

The [LARGE function](https://exceljet.net/functions/large-function)
 is a straightforward way to get the nth largest value in a range. Simply provide a range for the first argument (_array_), and a value for n as the second argument (_k_):

     =LARGE(range,1) // 1st largest
     =LARGE(range,2) // 2nd largest
     =LARGE(range,3) // 3rd largest
    

Working from the inside out, the first step is to get the "1st" largest value in the data with the LARGE function:

    LARGE(score,F5) // returns 93
    

In this case, the value in F5 is 1, so we are asking for the 1st largest score (i.e. the top score), which is 93. We can now simplify the formula to:

    =INDEX(name,MATCH(93,score,0))
    

Inside the [INDEX function](https://exceljet.net/functions/index-function)
, the [MATCH function](https://exceljet.net/functions/match-function)
 is set up to locate the position of 93 in the [named range](https://exceljet.net/glossary/named-range)
 **score** (D5:D16):

    MATCH(93,score,0) // returns 3
    

Since 93 appears in the 3rd row, MATCH returns 3 directly to INDEX as the row number, with **name** as array:

    =INDEX(name,3) // Hannah
    

Finally, the INDEX function returns the name in the 3rd row, "Hannah".

Notice we are picking up the values for **n** from the range F5:F7, in order to get the 1st, 2nd, and 3rd highest scores as the formula is copied down.

### Retrieve group

The same basic formula will work to retrieve any associated information. To get the group for the largest values, you can simply change the array supplied to INDEX with the named range **group**:

    =INDEX(group,MATCH(LARGE(score,F5),score,0))
    

With the value 1 in F5, LARGE will get the highest score, and the formula will return "A".

_Note: with [Excel 365](https://exceljet.net/glossary/excel-365)
, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 to [list top or bottom results dynamically](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)
._

### With XLOOKUP

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 can also be used to return the name of the nth largest value like this:

    =XLOOKUP(LARGE(score,F5),score,name)
    

LARGE returns the largest value, 93, directly to XLOOKUP as the lookup value:

    =XLOOKUP(93,score,name) //  Hannah
    

With the named range **score** (D5:D16) as the _lookup array_, and **name** (B5:B16) as the _return array_, XLOOKUP returns "Hannah" as before.

### Handling ties

Duplicate values in the numeric data will create a "tie". If a tie occurs in the values being ranked, for example, if the first and second largest values are the same, LARGE will return the same value for each. When this value is passed into the MATCH function, MATCH will return the position of the _first_ match, so you will see the same (first) name returned.

If there is the possibility of ties, you may want to implement some kind of tie-breaking strategy. One approach is to create [a new helper column of values which have been adjusted to break ties](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)
. Then use the helper column values to rank and retrieve information. This makes the logic used to break ties clear and explicit.

Another approach is to break ties based on position only (i.e. the first tie "wins"). Here is a formula that takes that approach:

    INDEX(name,MATCH(1,(score=LARGE(score,F5))*(COUNTIF(H$4:H4,name)=0),0))
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Here, we use MATCH to find the number 1, and we construct a lookup array using [boolean logic](https://exceljet.net/glossary/boolean-logic)
 that (1) compares all scores to the value returned by LARGE:

    score=LARGE(score,F5)
    

and (2) uses an [expanding range](https://exceljet.net/glossary/expanding-reference)
 check if the name is _already_ in the ranked list:

    COUNTIF(H$4:H4,name)=0
    

When a name is already in the list, it is "cancelled" by the logic, and the next (duplicate) value is matched. Notice the expanding range starts on the _prior row_, in order to avoid a circular reference.

This approach works in this example because there are no duplicate names in the name column. However, if duplicate _names_ occur in ranked values, the approach needs to be adjusted. The easiest solution is to make sure that names are unique.

### Notes

1.  To get the name of nth value _with criteria_, (i.e. limit results to group A or B) you will need to [extend the formula to use additional logic](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)
    .
2.  In [Excel 365](https://exceljet.net/glossary/excel-365)
    , the [FILTER function](https://exceljet.net/functions/filter-function)
     is a better way to [list top or bottom results dynamically](https://exceljet.net/formulas/filter-on-top-n-values)
    . This approach will automatically handle ties.

Related formulas
----------------

[![Excel formula: Name of nth largest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value%20with%20criteria.png "Excel formula: Name of nth largest value with criteria")](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)

### [Name of nth largest value with criteria](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)

The LARGE function is an easy way to get the nth largest value in a range: =LARGE(range,1) // 1st largest =LARGE(range,2) // 2nd largest =LARGE(range,3) // 3rd largest In this example, we can use the LARGE function to get a highest score, then use the score like a "key" to retrieve the associated...

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

[![Excel formula: FILTER on top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values.png "Excel formula: FILTER on top n values")](https://exceljet.net/formulas/filter-on-top-n-values)

### [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE function. The LARGE function is a simple way to get the nth largest value in a range. Simply provide a range for the first argument ( array ), and a value for n as the second argument ( k ): =...

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

*   [Name of nth largest value with criteria](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)
    
*   [nth largest value](https://exceljet.net/formulas/nth-largest-value)
    
*   [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    
*   [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)
    

### Functions

*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
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
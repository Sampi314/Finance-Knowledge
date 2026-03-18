# nth largest without duplicates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nth-largest-without-duplicates

---

[Skip to main content](https://exceljet.net/formulas/nth-largest-without-duplicates#main-content)

[](https://exceljet.net/formulas/nth-largest-without-duplicates#)

*   [Previous](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    
*   [Next](https://exceljet.net/formulas/nth-smallest-value)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

nth largest without duplicates
==============================

by Dave Bruns · Updated 14 Apr 2023

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: nth largest without duplicates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nth_largest_without_duplicates.png "Excel formula: nth largest without duplicates")

Summary
-------

To get the nth largest value in a way that excludes duplicate values, you can use a formula based on the [LARGE function](https://exceljet.net/functions/large-function)
 and the [UNIQUE function](https://exceljet.net/functions/unique-function)
. In the worksheet shown, the formula in cell E5, copied down, is:

    =LARGE(UNIQUE(data),D5)

where **data** is the named range B5:B16. As the formula is copied down, it returns the top 3 values in the data, which are 100, 98, and 95.

_Note: UNIQUE is a newer function in Excel. See below for a formula that will work in older versions of Excel._

Generic formula
---------------

    =LARGE(UNIQUE(range),n)

Explanation 
------------

In this example, the goal is to retrieve the largest 3 (top 3) values in the named range **data**, which appears in the range B6:B16. The standard solution to get "nth largest values" is the LARGE function. However, one potential problem with LARGE is that it will return duplicate values if they are present in the source data.

### Named range

For convenience, all values are in the named range **data** (B6:B16). Using a named range is entirely optional, but it's a nice way to quickly try out a number of formulas without entering addresses and locking references.

Video: [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)

###  LARGE function

The [LARGE function](https://exceljet.net/functions/large-function)
 is used to return the nth largest value in a set of data like this:

    =LARGE(range,n)
    

where _n_ is a number like 1, 2, 3, etc. For example, you can retrieve the first, second, and third largest values like this:

    =LARGE(range,1) // first largest
    =LARGE(range,2) // second largest
    =LARGE(range,3) // third largest

The challenge in this problem is that LARGE will return duplicates. For example, because 100 is the top value in the data and occurs twice, LARGE will return 100 when _n_ = 1 and when _n_ = 2.

### LARGE with UNIQUE

One easy way to solve this problem is to use the UNIQUE function inside of LARGE. This is the approach seen in the worksheet shown, where the formula in cell E5 is:

    =LARGE(UNIQUE(data),D5)

The UNIQUE function simply returns UNIQUE values, so the formula is solved like this:

    =LARGE(UNIQUE(data),D5)
    =LARGE(UNIQUE({100;100;98;95;95;92;91;90;89;86;85;81}),D5)
    =LARGE({100;98;95;92;91;90;89;86;85;81},1)
    =100

In cell E6 when _n_ = 2, we get 98:

    =LARGE(UNIQUE(data),D5)
    =LARGE(UNIQUE({100;100;98;95;95;92;91;90;89;86;85;81}),D5)
    =LARGE({100;98;95;92;91;90;89;86;85;81},2)
    =98

Without the UNIQUE function, LARGE would return 100 when _n_ = 2.

### Legacy Excel

In [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not have the UNIQUE function, we need a different approach. One option is to use the [MAX function](https://exceljet.net/functions/max-function)
 with the [IF function](https://exceljet.net/functions/if-function)
. We start off with MAX alone in cell E5:

    =MAX(data) // returns 100

MAX returns 100, the largest value in data. Next in cell E6, we enter a different formula that uses the IF function to "filter" out previous values like this:

    =MAX(IF(data<E5,data))

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in Legacy Excel._

This formula evaluates like this:

    =MAX(IF(data<E5,data))
    =MAX({FALSE;FALSE;98;95;95;92;91;90;89;86;85;81})
    =98

Notice that the IF function converts the value of 100 (which occurs twice) to FALSE. In other words, values that have appeared previously are destroyed. The MAX function simply returns the maximum value in the remaining numbers. As the formula is copied down the column, the reference to E5 changes at each row and IF creates a new array that excludes the previous result, and MAX returns a new maximum value.

Related formulas
----------------

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

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

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
    
*   [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    
*   [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

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
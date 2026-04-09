# nth largest value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nth-largest-value

---

[Skip to main content](https://exceljet.net/formulas/nth-largest-value#main-content)

[](https://exceljet.net/formulas/nth-largest-value#)

*   [Previous](https://exceljet.net/formulas/name-of-nth-largest-value-with-criteria)
    
*   [Next](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

nth largest value
=================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[LARGE](https://exceljet.net/functions/large-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7706/download?token=w1Hv6pFu)
 (17.57 KB)

![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")

Summary
-------

To get the nth largest value (i.e. 1st largest, 2nd largest, 3rd largest, etc.) in a set of data, you can use the [LARGE function](https://exceljet.net/functions/large-function)
. In the example shown, the formula in I5 is:

    =LARGE($C5:$G5,I$4)
    

As the formula is copied across and down the table, it returns the top 3 scores for each student in the list. Note this formula makes use of [mixed references](https://exceljet.net/glossary/mixed-reference)
. See below for more information.

Generic formula
---------------

    =LARGE(range,n)

Explanation 
------------

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function.

_Note: I don't know why the second argument for LARGE is called "k" . In this article I pretty much ignore that fact and use "n" instead, since "nth" is easier to understand than "kth"._

### LARGE function

The [LARGE function](https://exceljet.net/functions/large-function)
 can be used to return the nth largest value in a set of data. The generic syntax for LARGE looks like this:

    =LARGE(range,n)
    

where _n_ is a number like 1, 2, 3, etc. For example, you can retrieve the first, second, and third largest values like this:

    =LARGE(range,1) // first largest
    =LARGE(range,2) // second largest
    =LARGE(range,3) // third largest

The LARGE function is fully automatic — you just need to supply a range and a number that indicates rank. The official names for these arguments are "_array_" and "_k_". To illustrate, below we use LARGE to get the top 3 scores in column C. The formula in F5, copied down, is:

    =LARGE(data,E5)

**Data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16, provided as the _array_ argument, and the value for _k_ (n) comes from column E. As the formula is copied down, it returns the top 3 scores:

![Nth largest value - basic example](https://exceljet.net/sites/default/files/images/formulas/inline/nth_largest_value_basic_example.png "Nth largest value - basic example")

Here, **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16, and the value for n comes from column E.

Video: [How to use the LARGE and SMALL to get nth values](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### Mixed references

In the worksheet shown at top, we can use LARGE to get the top 3 scores for Hannah like this:

     =LARGE(C5:G5,1) // best score
     =LARGE(C5:G5,2) // 2nd best score
     =LARGE(C5:G5,3) // 3rd best score
    

The main challenge in this example is to create the syntax needed to copy the formula across the range I5:K16. In the example shown, this is accomplished with the formula in cell I5:

    =LARGE($C5:$G5,I$4)
    

This is a clever use of [mixed references](https://exceljet.net/glossary/mixed-reference)
 that takes advantage of the fact that the numbers 1, 2, and 3 are _already_ in the range I5:K5, so that they can be plugged into the formula directly as n:

*   The value given for _array_ is the mixed reference $C5:$G5. Notice that the columns are locked, but rows are not. This allows the rows to update as the formula is copied _down_, but prevents columns from changing as the formula is copied _across_.
*   The value given for _k_ (n) is another mixed reference, I$4. Here, the _row_ is locked so that it will not change as the formula is copied _down_. However, the column is not locked, allowing it to change as the formula is copied _across_.

Video: [Example of how to create a mixed reference](https://exceljet.net/videos/how-to-use-absolute-references-example-2)

Related formulas
----------------

[![Excel formula: Name of nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value.png "Excel formula: Name of nth largest value")](https://exceljet.net/formulas/name-of-nth-largest-value)

### [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)

In a nutshell, this formula uses the LARGE function to find the nth largest value in a set of data. Once we have that value, we plug it into a standard INDEX and MATCH formula to retrieve the associated name. In other words, we use the nth largest value like a "key" to retrieve associated...

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

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20get%20nth%20values%20with%20SMALL%20and%20LARGE_thumb.png)](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

In this video we'll look at how to calculate the "nth" smallest or largest values in a range using the SMALL or LARGE function s. This would be, for example, the 1st, 2nd, and 3rd smallest or largest values. In this first sheet, we have a list of students with five test scores. I'll use the LARGE...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_absolute_references_-_example_2-thumb_0.png)](https://exceljet.net/videos/how-to-use-absolute-references-example-2)

### [How to use absolute references - example 2](https://exceljet.net/videos/how-to-use-absolute-references-example-2)

In simple cases, we either want our references to be absolute or relative, but there are times when we need both. Sometimes you want to copy a formula and have the column for the reference be fixed while the row changes, and vice versa. Excel has an easy way of handling this situation. Let's take a...

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
    
*   [nth largest value with criteria](https://exceljet.net/formulas/nth-largest-value-with-criteria)
    
*   [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    

### Functions

*   [LARGE Function](https://exceljet.net/functions/large-function)
    

### Videos

*   [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)
    
*   [How to use absolute references - example 2](https://exceljet.net/videos/how-to-use-absolute-references-example-2)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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
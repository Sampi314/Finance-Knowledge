# nth smallest value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nth-smallest-value

---

[Skip to main content](https://exceljet.net/formulas/nth-smallest-value#main-content)

[](https://exceljet.net/formulas/nth-smallest-value#)

*   [Previous](https://exceljet.net/formulas/nth-largest-without-duplicates)
    
*   [Next](https://exceljet.net/formulas/nth-smallest-value-with-criteria)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

nth smallest value
==================

by Dave Bruns · Updated 10 Feb 2023

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7709/download?token=HvuqexMA)
 (18.49 KB)

![Excel formula: nth smallest value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nth_smallest_value.png "Excel formula: nth smallest value")

Summary
-------

To get the nth smallest value (i.e. 1st smallest, 2nd smallest, 3rd smallest, etc.) in a set of data, you can use the [SMALL function](https://exceljet.net/functions/small-function)
. In the example shown, the formula in I5 is:

    =SMALL($C5:$G5,I$4)
    

As the formula is copied across and down the table, it returns the 3 fastest times for each name in the list. Note this formula makes used of [mixed references](https://exceljet.net/glossary/mixed-reference)
 to make the formula easy to copy. See below for details.

_Note: [Excel times are just numbers](https://exceljet.net/glossary/excel-time)
 underneath the formatting, so smaller numbers mean shorter times._

Generic formula
---------------

    =SMALL(range,n)

Explanation 
------------

In this example, the goal is to extract the 3 best race times for each name from the 5 race times that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the fastest time, the 2nd fastest time, and the 3rd fastest time. This problem can be solved with the SMALL function.

_Note: I don't know why the second argument for SMALL is called "k" . In this article, I use "n" instead, since "nth" is easier to understand than "kth"._

### SMALL function

The [SMALL function](https://exceljet.net/functions/small-function)
 can be used to return the nth smallest value in a set of data. The generic syntax for SMALL looks like this:

    =SMALL(range,n)
    

where **n** is a number like 1, 2, 3, etc. For example, you can retrieve the first, second, and third smallest values like this:

    =SMALL(range,1) // first smallest
    =SMALL(range,2) // second smallest
    =SMALL(range,3) // third smallest

The SMALL function is automatic. Simply supply a range and a number that indicates rank. The official names for these arguments are "array" and "k". To illustrate with a simple example, below we use the SMALL function to get the 3 best times in column C. The formula in F5, copied down, is:

    =SMALL(data,E5)

For _array_, we use the [name range](https://exceljet.net/glossary/named-range)
 **data** (C5:C16) and the value for _k_ (n) is pulled from column E. As the formula is copied down, it returns the 3 fastest times.

![nth smallest value - basic example](https://exceljet.net/sites/default/files/images/formulas/inline/nth_smallest_value_basic_example.png "nth smallest value - basic example")

_Note: [Excel times are just numbers](https://exceljet.net/glossary/excel-time)
 underneath the formatting, so smaller numbers mean shorter times. This is why we can use the SMALL function to get the "best" times._

Video: [How to use the LARGE and SMALL to get nth values](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### Mixed references

In the worksheet shown at top, we can use SMALL to get the 3 fastest times for Hannah like this:

     =SMALL(C5:G5,1) // 1st fastest time
     =SMALL(C5:G5,2) // 2nd fastest time
     =SMALL(C5:G5,3) // 3rd fastest time
    

The main challenge in the worksheet is to create the syntax needed to copy the formula across the range I5:K16. In the example shown, this is accomplished with the formula in cell I5:

    =SMALL($C5:$G5,I$4)
    

This is a clever use of [mixed references](https://exceljet.net/glossary/mixed-reference)
 that takes advantage of the fact that the numbers 1, 2, and 3 are _already_ in the range I5:K5, so that they can be plugged into the formula directly as n:

*   The value given for _array_ is the mixed reference $C5:$G5. Notice that the columns are locked, but rows are not. This allows the rows to update as the formula is copied _down_, but prevents columns from changing as the formula is copied _across_.
*   The value given for _k_ (n) is another mixed reference, I$4. Here, the _row_ is locked so that it will not change as the formula is copied _down_. However, the column is not locked, allowing it to change as the formula is copied _across_.

Video: [Example of how to create a mixed reference](https://exceljet.net/videos/how-to-use-absolute-references-example-2)

Related formulas
----------------

[![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")](https://exceljet.net/formulas/nth-largest-value)

### [nth largest value](https://exceljet.net/formulas/nth-largest-value)

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function. Note...

[![Excel formula: Find lowest n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Find%20lowest%20n%20values.png "Excel formula: Find lowest n values")](https://exceljet.net/formulas/find-lowest-n-values)

### [Find lowest n values](https://exceljet.net/formulas/find-lowest-n-values)

The SMALL function retrieves the smallest values from data based on a given rank. For example: =SMALL(range,1) // smallest =SMALL(range,2) // 2nd smallest =SMALL(range,3) // 3rd smallest In the worksheet shown, the rank (which is provided to SMALL as the k argument) comes from numbers in column E...

[![Excel formula: nth smallest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value_with_criteria.png "Excel formula: nth smallest value with criteria")](https://exceljet.net/formulas/nth-smallest-value-with-criteria)

### [nth smallest value with criteria](https://exceljet.net/formulas/nth-smallest-value-with-criteria)

In this example, the goal is to retrieve the lowest 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the SMALL function, which can be used to retrieve the "nth"...

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

*   [nth largest value](https://exceljet.net/formulas/nth-largest-value)
    
*   [Find lowest n values](https://exceljet.net/formulas/find-lowest-n-values)
    
*   [nth smallest value with criteria](https://exceljet.net/formulas/nth-smallest-value-with-criteria)
    

### Functions

*   [SMALL Function](https://exceljet.net/functions/small-function)
    

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
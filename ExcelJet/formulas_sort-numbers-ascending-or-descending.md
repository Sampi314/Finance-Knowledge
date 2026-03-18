# Sort numbers ascending or descending - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-numbers-ascending-or-descending

---

[Skip to main content](https://exceljet.net/formulas/sort-numbers-ascending-or-descending#main-content)

[](https://exceljet.net/formulas/sort-numbers-ascending-or-descending#)

*   [Previous](https://exceljet.net/formulas/sort-and-extract-unique-values)
    
*   [Next](https://exceljet.net/formulas/sort-text-and-numbers-with-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Sort numbers ascending or descending
====================================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

![Excel formula: Sort numbers ascending or descending](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort%20numbers%20ascending%20or%20descending.png "Excel formula: Sort numbers ascending or descending")

Summary
-------

To dynamically sort a list of numbers in ascending order, you can a simple formula based on the [SMALL function](https://exceljet.net/functions/small-function)
 with an [expanding range](https://exceljet.net/glossary/expanding-reference)
. In the example shown, the formula in cell C5 is:

    =SMALL(data,ROWS($B$5:B5))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B14

Generic formula
---------------

    =SMALL(data,ROWS(exp_rng))

Explanation 
------------

The SMALL function is meant to extract the "nth" smallest value from a set of data. The value for N is supplied as the second argument. To get the smallest value with SMALL, supply 1, to get the second smallest value, supply 2, and so on.

    =SMALL(data,1) // 1st smallest
    =SMALL(data,2) // 2nd smallest
    =SMALL(data,3) // 3rd smallest
    

In the example shown, "data" is the named range B5:B14. In this example, the main challenge is to increment a value for nth. This is done by using an [expanding range](https://exceljet.net/glossary/expanding-reference)
 inside the ROWS function:

    ROWS($B$5:B5)
    

As the formula is copied down the table, the range expands, and the number of rows increases, which creates an incrementing number.

### Sort numbers in descending order

To sort numbers in descending order, simply replace the SMALL function with the LARGE function:

    =LARGE(data,ROWS(exp_rng))
    

Like SMALL, the LARGE function extracts an "nth" value. However, rather than the "nth smallest" LARGE returns the "nth largest".

Related formulas
----------------

[![Excel formula: Basic numeric sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20with%20rank%20in%20helper%20column2.png "Excel formula: Basic numeric sort formula")](https://exceljet.net/formulas/basic-numeric-sort-formula)

### [Basic numeric sort formula](https://exceljet.net/formulas/basic-numeric-sort-formula)

Note: this formula is the set-up for a formula that can extract and display data using a predefined sort order in a helper column. One example here . The core of this formula is the RANK function, which is used to generate a rank of sales values, where the highest number is ranked #1: =RANK(C5,...

[![Excel formula: Basic text sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20text%20sort%20formula.png "Excel formula: Basic text sort formula")](https://exceljet.net/formulas/basic-text-sort-formula)

### [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)

This formula uses the "greater than or equal to" operator with text, something you might not have tried before. When Excel compares text, it decides which value is "greater" than another based on rules that follow the ASCII specification . Inside COUNTIF, the range argument is supplied as the named...

[![Excel formula: Display sorted values with helper column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/display%20sorted%20values%20with%20helper%20column.png "Excel formula: Display sorted values with helper column")](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

### [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

This formula relies on a helper column that already contains a sequential list of numbers to represent an established sort order. The numbers in the helper column are independent of the operation of this formula. As long as the sequence is continuous, it can represent an ascending or descending...

[![Excel formula: Random sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20sort%20formula.png "Excel formula: Random sort formula")](https://exceljet.net/formulas/random-sort-formula)

### [Random sort formula](https://exceljet.net/formulas/random-sort-formula)

This formula depends on two helper columns. The first helper column holds random values created with the RAND() function. The formula in C5, copied down is: =RAND() The RAND function generates a random value at each row. Note: RAND is a volatile function and will generate new values with each...

[![Excel formula: Sort and extract unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20and%20extract%20unique%20values.png "Excel formula: Sort and extract unique values")](https://exceljet.net/formulas/sort-and-extract-unique-values)

### [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)

Note: the core idea of this formula is adapted from an example in Mike Girvin's excellent book Control+Shift+Enter . The example shown uses several formulas, which are described below. At a high level, the MMULT function is used to compute a numeric rank in a helper column (column C), and this rank...

Related functions
-----------------

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

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

*   [Basic numeric sort formula](https://exceljet.net/formulas/basic-numeric-sort-formula)
    
*   [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)
    
*   [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
    
*   [Random sort formula](https://exceljet.net/formulas/random-sort-formula)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    

### Functions

*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    

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
# Basic numeric sort formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-numeric-sort-formula

---

[Skip to main content](https://exceljet.net/formulas/basic-numeric-sort-formula#main-content)

[](https://exceljet.net/formulas/basic-numeric-sort-formula#)

*   [Previous](https://exceljet.net/formulas/basic-in-cell-histogram)
    
*   [Next](https://exceljet.net/formulas/basic-outline-numbering)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Basic numeric sort formula
==========================

by Dave Bruns · Updated 25 Oct 2023

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Basic numeric sort formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Sort%20with%20rank%20in%20helper%20column2.png "Excel formula: Basic numeric sort formula")

Summary
-------

To dynamically sort data that contains only numeric values, you can use a [helper column](https://exceljet.net/glossary/helper-column)
 and a formula created with the RANK and COUNTIF functions. In the example shown, the formula in D5 is:

    =RANK(C5,sales)+COUNTIF($C$5:C5,C5)-1
    

where "sales" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C11.

> Note: in Excel 2021 and later, the [SORT Function](https://exceljet.net/functions/sort-function)
>  is a better approach.

Generic formula
---------------

    =RANK(A1,values)+COUNTIF(exp_rng,A1)-1

Explanation 
------------

_Note: this formula is the set-up for a formula that can extract and display data using a predefined sort order in a helper column. [One example here](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
._

The core of this formula is the RANK function, which is used to generate a rank of sales values, where the highest number is ranked #1:

    =RANK(C5,sales)
    

Here, RANK uses the [named range](https://exceljet.net/glossary/named-range)
 "sales" (C5:C11) for convenience. By default, RANK will assign 1 to the highest value, 2 to the second highest value, and so on. This works perfectly as long as numeric values are unique. However, to handle numeric values which contain duplicates, we need to use the COUNTIF function to break ties. This is done by adding the result of this snippet to the value returned by RANK:

    COUNTIF($C$5:C5,C5)-1
    

Notice the range is entered as a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 that will [expand](https://exceljet.net/glossary/expanding-reference)
 as the formula is copied down the table. As written, this reference will include the current row, so we subtract 1 to "zero out" the first occurrence. This means the expression will return zero for each numeric value until a duplicate is encountered. At the second instance, the expression will return 1, at the third instance, it will return 2, and so on. This effectively breaks ties, and allows the formula to generate a sequential list of numbers with no gaps.

Once the formula is in place, data can be sorted by the [helper column](https://exceljet.net/glossary/helper-column)
. It can also be retrieved with INDEX using the values in the helper column.

_Note: This formula is adapted from an example in the excellent book [Control + Shift + Enter](http://www.amazon.com/gp/product/1615470077/?tag=exceljet-20)
, by [Mike Girvin](https://www.youtube.com/user/excelisfun)
._

Related formulas
----------------

[![Excel formula: Basic text sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20text%20sort%20formula.png "Excel formula: Basic text sort formula")](https://exceljet.net/formulas/basic-text-sort-formula)

### [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)

This formula uses the "greater than or equal to" operator with text, something you might not have tried before. When Excel compares text, it decides which value is "greater" than another based on rules that follow the ASCII specification . Inside COUNTIF, the range argument is supplied as the named...

[![Excel formula: Sort numbers ascending or descending](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20numbers%20ascending%20or%20descending.png "Excel formula: Sort numbers ascending or descending")](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

### [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

The SMALL function is meant to extract the "nth" smallest value from a set of data. The value for N is supplied as the second argument. To get the smallest value with SMALL, supply 1, to get the second smallest value, supply 2, and so on. =SMALL(data,1) // 1st smallest =SMALL(data,2) // 2nd...

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

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20rank%20values%20with%20the%20RANK%20function.png)](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)

### [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)

In this video we'll look at how to rank values in ascending or descending order using the RANK function . Here we have a table that contains five test scores for a group of students and an average score in Column I. How can we rank these students from highest to lowest scores? Well, one option is...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)
    
*   [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    
*   [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
    
*   [Random sort formula](https://exceljet.net/formulas/random-sort-formula)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    

### Functions

*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)
    
*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    

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
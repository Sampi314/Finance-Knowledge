# Basic text sort formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-text-sort-formula

---

[Skip to main content](https://exceljet.net/formulas/basic-text-sort-formula#main-content)

[](https://exceljet.net/formulas/basic-text-sort-formula#)

*   [Previous](https://exceljet.net/formulas/basic-outline-numbering)
    
*   [Next](https://exceljet.net/formulas/bmi-calculation-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Basic text sort formula
=======================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Basic text sort formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20text%20sort%20formula.png "Excel formula: Basic text sort formula")

Summary
-------

To dynamically sort text values in alphabetical order, you can use a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in C5 is:

    =COUNTIF(countries,"<="&B5)
    

where "countries" is the [named range](https://exceljet.net/glossary/named-range)
 B4:B13

_Note: in Excel 2021 the [SORT](https://exceljet.net/functions/sort-function)
 and [SORTBY](https://exceljet.net/functions/sortby-function)
 functions make this approach unnecessary._

Generic formula
---------------

    =COUNTIF(range,"<="&A1)

Explanation 
------------

This formula uses the "greater than or equal to" operator with text, something you might not have tried before. When Excel compares text, it decides which value is "greater" than another based on rules that follow the [ASCII specification](https://exceljet.net/glossary/ascii)
.

Inside COUNTIF, the range argument is supplied as the [named range](https://exceljet.net/glossary/named-range)
 "countries" (B4:B13), and the criteria is supplied as "less than or equal to" the value in C5. In each row, COUNTIFS returns the number of values that are less than or equal to the current value, which creates a sequential list of numbers (i.e. a rank) in the [helper column](https://exceljet.net/glossary/named-range)
.

### Listing sorted values

The helper column can be used to retrieve sorted values by rank. In E5, the formula used to retrieve values is:

    =INDEX(countries,MATCH(ROWS($E$5:E5),helper,0))
    

This is an INDEX and MATCH formula that uses an [expanding reference](https://exceljet.net/glossary/expanding-reference)
 to generate sequential numbers, which are fed into MATCH as lookup values. MATCH figures out where each number exists in the data, and INDEX retrieves the value at that position. [See this page for a more detailed explanation](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
.

### Handling duplicates

If the data contains duplicate text values, the sequence of sort numbers will also contain duplicates, which will cause problems if you are trying to retrieve values with the INDEX function. To work around this problem, you can use a variation of the formula that increments duplicates with a second COUNTIF:

    =COUNTIF(countries,"<"&B5)+COUNTIF($B$5:B5,B5)
    

_Note the logical operator in the first COUNTIF function has been adjusted, and the range in the second COUNTIF function is an [expanding reference](https://exceljet.net/glossary/expanding-reference)
._

Related formulas
----------------

[![Excel formula: Sort numbers ascending or descending](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20numbers%20ascending%20or%20descending.png "Excel formula: Sort numbers ascending or descending")](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

### [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

The SMALL function is meant to extract the "nth" smallest value from a set of data. The value for N is supplied as the second argument. To get the smallest value with SMALL, supply 1, to get the second smallest value, supply 2, and so on. =SMALL(data,1) // 1st smallest =SMALL(data,2) // 2nd...

[![Excel formula: Display sorted values with helper column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/display%20sorted%20values%20with%20helper%20column.png "Excel formula: Display sorted values with helper column")](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

### [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

This formula relies on a helper column that already contains a sequential list of numbers to represent an established sort order. The numbers in the helper column are independent of the operation of this formula. As long as the sequence is continuous, it can represent an ascending or descending...

[![Excel formula: Random sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20sort%20formula.png "Excel formula: Random sort formula")](https://exceljet.net/formulas/random-sort-formula)

### [Random sort formula](https://exceljet.net/formulas/random-sort-formula)

This formula depends on two helper columns. The first helper column holds random values created with the RAND() function. The formula in C5, copied down is: =RAND() The RAND function generates a random value at each row. Note: RAND is a volatile function and will generate new values with each...

[![Excel formula: Basic numeric sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20with%20rank%20in%20helper%20column2.png "Excel formula: Basic numeric sort formula")](https://exceljet.net/formulas/basic-numeric-sort-formula)

### [Basic numeric sort formula](https://exceljet.net/formulas/basic-numeric-sort-formula)

Note: this formula is the set-up for a formula that can extract and display data using a predefined sort order in a helper column. One example here . The core of this formula is the RANK function, which is used to generate a rank of sales values, where the highest number is ranked #1: =RANK(C5,...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20CHAR%20and%20CODE%20functions-thumb.png)](https://exceljet.net/videos/how-to-use-char-and-code-functions)

### [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)

Each character you see displayed in Excel has a number. Excel has two functions that work with these numbers directly: CODE and CHAR (Character). Let's look first at the CODE function . The CODE function accepts one argument, which is the text for which you'd like a numeric code. If I use CODE with...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    
*   [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
    
*   [Random sort formula](https://exceljet.net/formulas/random-sort-formula)
    
*   [Basic numeric sort formula](https://exceljet.net/formulas/basic-numeric-sort-formula)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    

### Functions

*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)
    
*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    
*   [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)
    

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
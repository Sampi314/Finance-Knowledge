# Sort text and numbers with formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-text-and-numbers-with-formula

---

[Skip to main content](https://exceljet.net/formulas/sort-text-and-numbers-with-formula#main-content)

[](https://exceljet.net/formulas/sort-text-and-numbers-with-formula#)

*   [Previous](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    
*   [Next](https://exceljet.net/formulas/split-payment-across-months)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Sort text and numbers with formula
==================================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNT](https://exceljet.net/functions/count-function)

![Excel formula: Sort text and numbers with formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort%20mixed%20data%20with%20a%20formula.png "Excel formula: Sort text and numbers with formula")

Summary
-------

To dynamically sort data with both numbers and text in alphabetical order you can use a formula to generate a numeric rank in a helper column, then use INDEX and MATCH to display values based on rank. In the example shown the formula in C5 is :

    =COUNTIF(data,"<="&B5)+(COUNT(data)*ISTEXT(B5))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B13.

Generic formula
---------------

    =COUNTIF(data,"<="&A1)+(COUNT(data)*ISTEXT(A1))

Explanation 
------------

This formula first generates a rank value using an expression based on COUNTIF:

    =COUNTIF(data,"<="&B5)
    

which is [explained in more detail here](https://exceljet.net/formulas/basic-text-sort-formula)
. If the data contains all text values, or all numeric values, the rank will be correct. However, if the data includes both text and numbers, we need to "shift" the rank of all text values to account for the numeric values. This is done with the second part of the formula here:

    +(COUNT(data)*ISTEXT(B7))
    

Here, we use the COUNT function to get a count of numeric values in the data, then multiply the result by the logical result of ISTEXT, which tests if the value is text and returns either TRUE or FALSE. This effectively cancels out the COUNT result when we are working with a number in the current row.

### Handling duplicates

If data contains duplicates, the formula can be altered as shown below to assign a sequential rank to values that appear more than once:

    =COUNTIF(data,"<"&B5)+(COUNT(data)*ISTEXT(B5))+COUNTIF($B$5:B5,B5)
    

This version adjusts the logic of the initial COUNTIF function, and adds another COUNTIF with an expanding reference to increment duplicates.

### Display sorted values

To retrieve and display values sorted values in alphabetical order using the calculated rank value, E5 contains the following [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
:

    =INDEX(data,MATCH(ROWS($E$5:E5),rank,0))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B13, and "rank" is the named range C5:C13.

For more information about how this formula works, [see the example here](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
.

### Dealing with blanks

Empty cells will generate a rank of zero. Assuming you want to ignore empty cells, this works fine because the INDEX and MATCH formula above begins at 1. However, you will see #N/A errors at the end of sorted values, one for each empty cell. An easy way to handle this is to wrap the INDEX and MATCH formula in IFERROR like this:

    =IFERROR(INDEX(data,MATCH(ROWS($E$5:E5),rank,0)),"")
    

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

[![Excel formula: Basic text sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20text%20sort%20formula.png "Excel formula: Basic text sort formula")](https://exceljet.net/formulas/basic-text-sort-formula)

### [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)

This formula uses the "greater than or equal to" operator with text, something you might not have tried before. When Excel compares text, it decides which value is "greater" than another based on rules that follow the ASCII specification . Inside COUNTIF, the range argument is supplied as the named...

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

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

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
    
*   [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    

### Functions

*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    

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
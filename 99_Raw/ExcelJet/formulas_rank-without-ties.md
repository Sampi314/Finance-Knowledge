# Rank without ties - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/rank-without-ties

---

[Skip to main content](https://exceljet.net/formulas/rank-without-ties#main-content)

[](https://exceljet.net/formulas/rank-without-ties#)

*   [Previous](https://exceljet.net/formulas/rank-with-ordinal-suffix)
    
*   [Next](https://exceljet.net/formulas/get-decimal-part-of-a-number)
    

[Rank](https://exceljet.net/formulas#Rank)

Rank without ties
=================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Rank without ties](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/rank%20without%20ties.png "Excel formula: Rank without ties")

Summary
-------

To assign rank without ties, you can use a formula based on the [RANK](https://exceljet.net/functions/rank-function)
 and [COUNTIF](https://exceljet.net/functions/countif-function)
 functions. In the example shown, the formula in E5 is:

    =RANK(C5,points)+COUNTIF($C$5:C5,C5)-1
    

where "points" is a [named range](https://exceljet.net/glossary/dynamic-named-range)
.

Generic formula
---------------

    =RANK(A1,range)+COUNTIF(exp_range,A1)-1

Explanation 
------------

This formula breaks ties with a simple approach: this first tie in a list "wins" and is assigned the higher rank. The first part of the formula uses the RANK function normally:

    =RANK(C5,points)
    

Rank returns a computed rank, which will include ties when the values being ranked include duplicates. Note that the [RANK function](https://exceljet.net/functions/rank-function)
 by itself will assign the same rank to duplicate values, and skip the next rank value. You can see this in the Rank 1 column, rows 8 and 9 in the worksheet.

The second part of the formula breaks the tie with COUNTIF:

    COUNTIF($C$5:C5,C5)-1
    

Note the range we give COUNTIF is an [expanding reference](https://exceljet.net/glossary/expanding-reference)
: the first reference is absolute and the second is relative. As long as a value appears just once, this expression cancels itself out – COUNTIF returns 1, from which 1 is subtracted.

However, when a duplicate number is encountered, COUNTIF returns 2, the expression returns 1, and the rank value is increased by 1. Essentially, this "replaces" the rank value that was skipped originally.

The same process repeats as the formula is copied down the column. If another duplicate is encountered, the rank value is increased by 2, and so on.

Related formulas
----------------

[![Excel formula: Rank race results](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20race%20results2.png "Excel formula: Rank race results")](https://exceljet.net/formulas/rank-race-results)

### [Rank race results](https://exceljet.net/formulas/rank-race-results)

You can use the RANK function to rank numeric values. RANK has two modes of operation: ranking values so that the largest value is ranked #1 (order = 0), and ranking values so that the smallest value is #1 (order = 1). In this case, we are ranking race times. The lowest/fastest value should rank #1...

[![Excel formula: Rank if formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20with%20criteria.png "Excel formula: Rank if formula")](https://exceljet.net/formulas/rank-if-formula)

### [Rank if formula](https://exceljet.net/formulas/rank-if-formula)

Although Excel has a RANK function , there is no RANKIF function to perform a conditional rank. However, you can easily create a conditional RANK with the COUNTIFS function. The COUNTIFS function can perform a conditional count using two or more criteria. Criteria are entered in range/criteria...

[![Excel formula: Rank with ordinal suffix](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20with%20ordinal%20suffix.png "Excel formula: Rank with ordinal suffix")](https://exceljet.net/formulas/rank-with-ordinal-suffix)

### [Rank with ordinal suffix](https://exceljet.net/formulas/rank-with-ordinal-suffix)

Ordinal numbers represent position or rank in a sequential order. They are normally written using a number + letter suffix: 1st, 2nd, 3rd, etc. To get an ordinal suffix for a small set of numbers, you can use the CHOOSE function like this: =CHOOSE(B5,"st","nd","rd","th","th","th","th","th","th","th...

[![Excel formula: Break ties with helper column and COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/break%20ties%20with%20helper%20column%20and%20COUNTIF.png "Excel formula: Break ties with helper column and COUNTIF")](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)

### [Break ties with helper column and COUNTIF](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)

In this example, the goal is to retrieve information about the lowest three estimates in the data shown. The problem is that there are some duplicate values in the estimate column. This means we will have some trouble trying to display the names of the 2nd and 3rd lowest suppliers because the tie...

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Rank race results](https://exceljet.net/formulas/rank-race-results)
    
*   [Rank if formula](https://exceljet.net/formulas/rank-if-formula)
    
*   [Rank with ordinal suffix](https://exceljet.net/formulas/rank-with-ordinal-suffix)
    
*   [Break ties with helper column and COUNTIF](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)
    

### Functions

*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)
    

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
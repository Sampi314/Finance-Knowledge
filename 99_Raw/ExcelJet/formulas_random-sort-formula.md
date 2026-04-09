# Random sort formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-sort-formula

---

[Skip to main content](https://exceljet.net/formulas/random-sort-formula#main-content)

[](https://exceljet.net/formulas/random-sort-formula#)

*   [Previous](https://exceljet.net/formulas/parse-xml-with-formula)
    
*   [Next](https://exceljet.net/formulas/range-contains-duplicates)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Random sort formula
===================

by Dave Bruns · Updated 1 Nov 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Random sort formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random%20sort%20formula.png "Excel formula: Random sort formula")

Summary
-------

To randomly sort existing values with a formula, you can use an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 together with [helper columns](https://exceljet.net/glossary/helper-column)
 as shown in the screenshot. In the example shown, the formula in E5 is:

    =INDEX(names,MATCH(ROWS($D$5:$D5),sort,0))
    

where "names" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B11, "rand" is the named range C5:C11, and "sort" is the named range D5:D11.

_Note: If you are using a current version of Excel, [this formula based on SORTBY and RANDARRAY](https://exceljet.net/formulas/random-sort)
_ _is a better approach_

Generic formula
---------------

    =INDEX(data,MATCH(ROWS(exp_range),sort_values,0))

Explanation 
------------

This formula depends on two helper columns. The first [helper column](https://exceljet.net/glossary/helper-column)
 holds random values created with the RAND() function. The formula in C5, copied down is:

    =RAND()
    

The RAND function generates a random value at each row.

_Note: RAND is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and will generate new values with each worksheet change._

The second helper column holds the numbers used to sort data, generated with a formula. The formula in D5 is:

    =RANK(C5,rand)+COUNTIF($C$5:C5,C5)-1
    

See [this page](https://exceljet.net/formulas/basic-numeric-sort-formula)
 for an explanation of this formula.

The formula in E5 is:

    =INDEX(names,MATCH(ROWS($D$5:$D5),sort,0))
    

Here, the INDEX function is used to retrieve values in the named range "names", using the sort values in the named range "sort". The actual work of figuring out what value to retrieve is done my the MATCH function in this snippet:

    MATCH(ROWS($D$5:$D5),sort,0)
    

Inside MATCH, the ROWS function is given an [expanding range](https://exceljet.net/glossary/expanding-reference)
 as the lookup value, which begins as one cell, and expands as the formula is copied down the column. This increments the lookup value, starting at 1 and continuing to 7. MATCH then returns the position of the lookup value in the list.

The position is fed to INDEX as the row number, and INDEX retrieves the name at that position.

Related formulas
----------------

[![Excel formula: Basic numeric sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20with%20rank%20in%20helper%20column2.png "Excel formula: Basic numeric sort formula")](https://exceljet.net/formulas/basic-numeric-sort-formula)

### [Basic numeric sort formula](https://exceljet.net/formulas/basic-numeric-sort-formula)

Note: this formula is the set-up for a formula that can extract and display data using a predefined sort order in a helper column. One example here . The core of this formula is the RANK function, which is used to generate a rank of sales values, where the highest number is ranked #1: =RANK(C5,...

[![Excel formula: Display sorted values with helper column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/display%20sorted%20values%20with%20helper%20column.png "Excel formula: Display sorted values with helper column")](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

### [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

This formula relies on a helper column that already contains a sequential list of numbers to represent an established sort order. The numbers in the helper column are independent of the operation of this formula. As long as the sequence is continuous, it can represent an ascending or descending...

[![Excel formula: Basic text sort formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20text%20sort%20formula.png "Excel formula: Basic text sort formula")](https://exceljet.net/formulas/basic-text-sort-formula)

### [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)

This formula uses the "greater than or equal to" operator with text, something you might not have tried before. When Excel compares text, it decides which value is "greater" than another based on rules that follow the ASCII specification . Inside COUNTIF, the range argument is supplied as the named...

[![Excel formula: Sort numbers ascending or descending](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20numbers%20ascending%20or%20descending.png "Excel formula: Sort numbers ascending or descending")](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

### [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)

The SMALL function is meant to extract the "nth" smallest value from a set of data. The value for N is supplied as the second argument. To get the smallest value with SMALL, supply 1, to get the second smallest value, supply 2, and so on. =SMALL(data,1) // 1st smallest =SMALL(data,2) // 2nd...

[![Excel formula: Sort and extract unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20and%20extract%20unique%20values.png "Excel formula: Sort and extract unique values")](https://exceljet.net/formulas/sort-and-extract-unique-values)

### [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)

Note: the core idea of this formula is adapted from an example in Mike Girvin's excellent book Control+Shift+Enter . The example shown uses several formulas, which are described below. At a high level, the MMULT function is used to compute a numeric rank in a helper column (column C), and this rank...

[![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random_sort.png "Excel formula: Random sort")](https://exceljet.net/formulas/random-sort)

### [Random sort](https://exceljet.net/formulas/random-sort)

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the SORTBY function and the RANDARRAY function . SORTBY function The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

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
    
*   [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)
    
*   [Basic text sort formula](https://exceljet.net/formulas/basic-text-sort-formula)
    
*   [Sort numbers ascending or descending](https://exceljet.net/formulas/sort-numbers-ascending-or-descending)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    
*   [Random sort](https://exceljet.net/formulas/random-sort)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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
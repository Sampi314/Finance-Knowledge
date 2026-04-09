# Reverse VLOOKUP example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/reverse-vlookup-example

---

[Skip to main content](https://exceljet.net/formulas/reverse-vlookup-example#main-content)

[](https://exceljet.net/formulas/reverse-vlookup-example#)

*   [Previous](https://exceljet.net/formulas/rank-and-score-with-index-and-match)
    
*   [Next](https://exceljet.net/formulas/self-contained-vlookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Reverse VLOOKUP example
=======================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5731/download?token=T7OFDAmL)
 (10.77 KB)

![Excel formula: Reverse VLOOKUP example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/reverse%20VLOOKUP%20example.png "Excel formula: Reverse VLOOKUP example")

Summary
-------

To reverse a VLOOKUP – i.e. to find the original lookup value using a VLOOKUP formula result – you can use a tricky formula based on the [CHOOSE function](https://exceljet.net/functions/choose-function)
, or more straightforward formulas based on INDEX and MATCH or XLOOKUP as explained below. In the example shown, the formula in H10 is:

    =VLOOKUP(G10,CHOOSE({3,2,1},B5:B8,C5:C8,D5:D8),3,0)
    

With this setup, VLOOKUP finds the option associated with a cost of 3000, and returns "C".

_Note: this is a more advanced topic. If you are just getting started with VLOOKUP, [start here](https://exceljet.net/functions/vlookup-function)
._

Generic formula
---------------

    =VLOOKUP(A1,CHOOSE({3,2,1},col1,col2,col3),3,0)

Explanation 
------------

### Introduction

A key limitation of [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 is it can only look up values to the _right_. In other words, the column with lookup values must be to the left of the values you want to retrieve with VLOOKUP. As a result, with standard configuration, there is no way to use VLOOKUP to "look left" and reverse the original lookup. From the standpoint of VLOOKUP, we can visualize the problem like this:

![The table we have versus the table we need](https://exceljet.net/sites/default/files/images/formulas/inline/what%20we%20have%20vs%20what%20we%20need.png "The table we have versus the table we need")

The workaround explained below uses the CHOOSE function to rearrange the table inside VLOOKUP. Starting at the beginning, the formula in H5 is a normal VLOOKUP formula:

    =VLOOKUP(G5,B5:D8,3,0) // returns 3000
    

Using G5 as the _lookup value_ ("C"), and the data in B5:D8 as the _table array_, VLOOKUP performs a lookup on values in column B and returns the corresponding value from column 3 (column D), 3000. Notice zero (0) is provided as the last argument to force an exact match.

The formula in G10 simply pulls the result from H5:

    =H5 // 3000
    

To perform a reverse lookup, the formula in H10 is:

    =VLOOKUP(G10,CHOOSE({3,2,1},B5:B8,C5:C8,D5:D8),3,0)
    

The tricky bit is the CHOOSE function, which is used to rearrange the table array so that Cost is the first column, and Option is the last:

    CHOOSE({3,2,1},B5:B8,C5:C8,D5:D8) // reorder table 3, 2, 1
    

The CHOOSE function is designed to select a value based on a numeric index. In this case, we are supplying _three_ index values in an [array constant](https://exceljet.net/glossary/array-constant)
:

    {3,2,1} // array constant
    

In other words, we are asking for column 3, then column 2, then column 1. This is followed by the three ranges that represent each column of the table in the order they appear on the worksheet.

With this configuration, CHOOSE returns all three columns in a single 2D [array](https://exceljet.net/glossary/array)
 like this:

    {1000,"Silver","A";2000,"Gold","B";3000,"Platinum","C";5000,"Diamond","D"}
    

If we visualize this array as a table on the worksheet, we have:

![Table rearranged by CHOOSE function](https://exceljet.net/sites/default/files/images/formulas/inline/table%20rearranged%20by%20choose%20function.png "Table rearranged by CHOOSE function")

_Note: the headings are not part of the array and are shown here for clarity only._

Effectively, we have swapped columns 1 and 3. The reorganized table is returned directly to VLOOKUP, which matches 3000, and returns the corresponding value from column 3, "C".

### With INDEX and MATCH

The above solution works fine, but it is hard to recommend since most users will not understand how the formula works. A better solution is [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, using a formula like this:

    =INDEX(B5:B8,MATCH(G10,D5:D8,0)) 
    

Here, the MATCH function finds the value 3000 in D5:D8, and returns its position, 3:

    MATCH(G10,D5:D8,0) // returns 3
    

_Note: MATCH is configured for an exact match by setting the last argument to zero (0)._

MATCH returns a result directly to INDEX as the row number, so the formula becomes:

    =INDEX(B5:B8,3) // returns "C"
    

and INDEX returns the value from the third row of B5:B8, "C".

This formula shows how INDEX and MATCH can be more flexible than VLOOKUP.

### With XLOOKUP

XLOOKUP also provides a very good solution. The equivalent formula is:

    =XLOOKUP(G10,D5:D8,B5:B8) // returns "C"
    

With a _lookup\_value_ from G10 (3000), a l_ookup\_array_ of D5:D8 (costs), and a _results\_array_ of B5:B8 (options), XLOOKUP locates the 3000 in the lookup array and returns the corresponding item from the results array, "C". Because XLOOKUP performs an exact match by default, there is no need to set the match mode explicitly.

Related formulas
----------------

[![Excel formula: Left lookup with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Look%20left%20with%20VLOOKUP.png "Excel formula: Left lookup with VLOOKUP")](https://exceljet.net/formulas/left-lookup-with-vlookup)

### [Left lookup with VLOOKUP](https://exceljet.net/formulas/left-lookup-with-vlookup)

One of the VLOOKUP function's key limitations is that it can only look up values to the right. In other words, the column that contains lookup values must sit to the left of the values you want to retrieve with VLOOKUP. There is no way to override this behavior since it is hardwired into the...

[![Excel formula: VLOOKUP with variable table array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20variable%20table%20array.png "Excel formula: VLOOKUP with variable table array")](https://exceljet.net/formulas/vlookup-with-variable-table-array)

### [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)

In this example, the goal is to set up VLOOKUP to retrieve costs based on a variable vendor name. In other words, we want a formula that allows us to switch tables dynamically based on a user-supplied value. There are two cost tables in the worksheet, one for Vendor A and one for Vendor B. Both...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Left lookup with VLOOKUP](https://exceljet.net/formulas/left-lookup-with-vlookup)
    
*   [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

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
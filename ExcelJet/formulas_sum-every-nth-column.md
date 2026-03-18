# Sum every nth column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-every-nth-column

---

[Skip to main content](https://exceljet.net/formulas/sum-every-nth-column#main-content)

[](https://exceljet.net/formulas/sum-every-nth-column#)

*   [Previous](https://exceljet.net/formulas/sum-every-n-rows)
    
*   [Next](https://exceljet.net/formulas/sum-every-nth-row)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum every nth column
====================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[COLUMN](https://exceljet.net/functions/column-function)

[MOD](https://exceljet.net/functions/mod-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7497/download?token=kxND3WEI)
 (15.33 KB)

![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")

Summary
-------

To sum every nth column (i.e. every second column, every third column, etc.) you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
, the [MOD function](https://exceljet.net/functions/mod-function)
, and the [SUM function](https://exceljet.net/functions/sum-function)
. In the example shown, the formula in cell K5, copied down, is:

    =SUM(FILTER(B5:J5,MOD(SEQUENCE(1,COLUMNS(B5:J5)),$K$2)=0))
    

With the number 3 in cell K2 for **n**, the result is 17. As the formula is copied down, we get a new sum on each row. Each result is the sum of every third value from column B to column J.

_Note: With a small set of data, you can easily enter a formula manually to sum columns as you like. The point of this example is to show how to create a general solution that will scale up to a larger set of data, and allow the value for **n** to be easily changed._

Generic formula
---------------

    =SUM(FILTER(data,MOD(SEQUENCE(1,COLUMNS(data)),n)=0))

Explanation 
------------

In this example, the goal is to sum every nth value _by column_ in a range of data, as seen in the worksheet above. For example, if **n**\=2, we want to sum every second value by column, if **n**\=3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and **n** is entered into cell K2 as 3. The value for **n** can be changed at any time. There are two basic approaches to this problem in Excel:

1.  Extract nth column values & sum the result
2.  Zero-out non-nth values & sum the result

In the [current version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, a good way to solve the problem is with approach #1 and the FILTER function. In [Legacy Excel,](https://exceljet.net/glossary/legacy-excel)
 you can use approach #2 and a formula based on the SUMPRODUCT function. Both approaches are explained below.

_Note: The approaches below all depend on the [MOD function](https://exceljet.net/functions/mod-function)
 to work out which values to sum. The MOD function returns the remainder of two numbers after division, and you will often see it in formulas that deal with repeating values._

### Example formula

In the example shown, the formula in cell K5 is:

    =SUM(FILTER(B5:J5,MOD(SEQUENCE(1,COLUMNS(B5:J5)),$K$2)=0))
    

At a high level, this formula uses the [FILTER function](https://exceljet.net/functions/filter-function)
 to extract values associated with every nth column of the data, and the [SUM function](https://exceljet.net/functions/sum-function)
 to sum the values extracted.

### Extracting data

Working from the inside out, the first step in this problem is to collect the data that should be summed. This is done with the FILTER function like this:

    FILTER(B5:J5,include)
    

where _include_ represents the formula logic needed to target every nth value by column (every 3rd value in the example). To construct the logic we need, we use a combination of the [MOD function](https://exceljet.net/functions/mod-function)
, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
, and the [COLUMNS function](https://exceljet.net/functions/columns-function)
:

    MOD(SEQUENCE(1,COLUMNS(B5:J5)),$K$2)=0
    

The [COLUMNS function](https://exceljet.net/functions/columns-function)
 returns the count of columns in the range B5:J5, which is 9:

    MOD(SEQUENCE(1,9),$K$2)=0
    

With 1 as the _rows_ argument and 9 as the _columns_ argument, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 returns a numeric array of 9 numbers like this:

    {1,2,3,4,5,6,7,8,9}
    

Notice the commas in this array indicate that this is a [horizontal array](https://exceljet.net/glossary/array)
, 1 row x 9 columns. Substituting the array above and the value for **n** (3) into the formula we have:

    MOD({1,2,3,4,5,6,7,8,9},3)=0
    

The [MOD function](https://exceljet.net/functions/mod-function)
 returns the remainder of each number in the array divided by 3:

    {1,2,0,1,2,0,1,2,0}=0
    

The result from MOD is compared to zero, which creates an array of TRUE and FALSE values:

    {FALSE,FALSE,TRUE,FALSE,FALSE,TRUE,FALSE,FALSE,TRUE}
    

Note that every third value is TRUE. These are the values we want to sum.

The array above is returned to FILTER as the _include_ argument. FILTER uses this array to "filter" values in the range B5:J16 [_by column_](https://exceljet.net/formulas/filter-by-column-sort-by-row)
. Only values associated with TRUE make it through the filter operation. The result is an array that contains every 3rd value in the data. Since there are 9 values total, FILTER returns 3 values directly to the SUM function:

    =SUM({6,4,7}) // returns 17
    

The SUM function sums the array and returns 17 as a final result. This formula is dynamic. For example, if the value for **n** in cell K2 is changed to 2 (every 2nd value) the new result is 16.

### Legacy Excel formula

In [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not include the FILTER or SEQUENCE functions, you can use a different formula based on the SUMPRODUCT function:

    =SUMPRODUCT(--(MOD(COLUMN(B5:J5)-COLUMN(B5)+1,$K$2)=0),B5:J5)
    

The concept is similar to the formula explained above but the approach is different. Rather than extracting values of interest from the data, this formula "zeros out" values _not of interest_. First, the formula uses the COLUMN function to construct a [relative set of column numbers](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
:

    COLUMN(B5:J5)-COLUMN(B5)+1
    

The result is a numeric array like this:

    {1,2,3,4,5,6,7,8,9}
    

As above, is a [horizontal array](https://exceljet.net/glossary/array)
, 1 row x 9 columns. Inside the SUMPRODUCT function, we again use the MOD function to construct a filter:

    MOD(COLUMN(B5:J5)-COLUMN(B5)+1,$K$2)=0
    MOD({1,2,3,4,5,6,7,8,9},3)=0)
    

MOD returns an array of TRUE FALSE values like this:

    {FALSE,FALSE,TRUE,FALSE,FALSE,TRUE,FALSE,FALSE,TRUE}
    

Note that every 3rd value is TRUE. A [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to convert the TRUE and FALSE values to 1s and 0s. Back in the SUMPRODUCT, we now have:

    =SUMPRODUCT({0,0,1,0,0,1,0,0,1},B5:J5)
    

The SUMPRODUCT then multiplies the two arrays together and returns the sum of products. Only the values in B5:J5 that are associated with 1s survive this operation, the other values are "zeroed out":

    =SUMPRODUCT({0,0,6,0,0,4,0,0,7}) // returns 17
    

The final result is 17. This formula is also dynamic. If the value for **n** in cell K2 is changed to 2 (every 2nd value) the new result is 16.

### Hybrid approach

Yet another approach is to create a more modern version of the SUMPRODUCT formula above by replacing SUMPRODUCT with SUM, and the COLUMN construction with SEQUENCE:

    =SUM((MOD(SEQUENCE(1,COLUMNS(B5:J5)),$K$2)=0)*B5:J5)
    

This formula works the same way as the SUMPRODUCT formula above, but the SEQUENCE function is a simpler way to generate a relative set of column numbers. Notice that because we have replaced SUMPRODUCT with SUM, we need to move all logic into the first argument and do our own multiplication. This formula will only work in the current version of Excel.

Related formulas
----------------

[![Excel formula: Sum every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20row.png "Excel formula: Sum every nth row")](https://exceljet.net/formulas/sum-every-nth-row)

### [Sum every nth row](https://exceljet.net/formulas/sum-every-nth-row)

In this example, the goal is to sum every nth value in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value (every other value), if n =3, we want to sum every third value, and so on. All data is in the range B5:B16 and n is entered into cell F5 as...

[![Excel formula: Get relative column numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20column%20numbers%20in%20range.png "Excel formula: Get relative column numbers in range")](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

### [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

The first COLUMN function generates an array of 7 numbers like this: {2,3,4,5,6,7,8} The second COLUMN function generates an array with just one item like this: {2} which is then subtracted from the first array to yield: {0,1,2,3,4,5,6} Finally, 1 is added to get: {1,2,3,4,5,6,7} With a named range...

[![Excel formula: Sum columns based on adjacent criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20columns%20based%20on%20adjacent%20criteria.png "Excel formula: Sum columns based on adjacent criteria")](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)

### [Sum columns based on adjacent criteria](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)

In this example, the goal is to sum the values in columns C, E, G, and I conditionally using the text values in columns B, D, F, and H for criteria. This problem can be solved with the SUMPRODUCT function , which is designed to multiply ranges or arrays together and return the sum of products. The...

[![Excel formula: Copy value from every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20row_0.png "Excel formula: Copy value from every nth row")](https://exceljet.net/formulas/copy-value-from-every-nth-row)

### [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)

In this example, the goal is to copy every nth value from column B, where n is a variable that can be changed as needed. In Excel, it's difficult to create formulas that skip rows following a certain pattern, because the references in the formula will automatically change as the formula is copied...

[![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")](https://exceljet.net/formulas/copy-value-from-every-nth-column)

### [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum every nth row](https://exceljet.net/formulas/sum-every-nth-row)
    
*   [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
    
*   [Sum columns based on adjacent criteria](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)
    
*   [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    
*   [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    

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
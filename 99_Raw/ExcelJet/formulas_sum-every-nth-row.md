# Sum every nth row - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-every-nth-row

---

[Skip to main content](https://exceljet.net/formulas/sum-every-nth-row#main-content)

[](https://exceljet.net/formulas/sum-every-nth-row#)

*   [Previous](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Next](https://exceljet.net/formulas/sum-first-n-matching-values)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum every nth row
=================

by Dave Bruns · Updated 12 Sep 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[MOD](https://exceljet.net/functions/mod-function)

[SUM](https://exceljet.net/functions/sum-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Sum every nth row](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20every%20nth%20row.png "Excel formula: Sum every nth row")

Summary
-------

To sum every nth row (i.e. every second row, every third row, etc.) you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
, the [MOD function](https://exceljet.net/functions/mod-function)
, and the [SUM function](https://exceljet.net/functions/sum-function)
. In the example shown, the formula in cell F6 is:

    =SUM(FILTER(B5:B16,MOD(SEQUENCE(ROWS(B5:B16)),F5)=0))
    

With the number 3 in cell F5 for **n**, the result is 70.

Generic formula
---------------

    =SUM(FILTER(data,MOD(SEQUENCE(ROWS(data)),n)=0))

Explanation 
------------

In this example, the goal is to sum every nth value in a range of data, as seen in the worksheet above. For example, if **n**\=2, we want to sum every second value (every other value), if **n**\=3, we want to sum every third value, and so on. All data is in the range B5:B16 and **n** is entered into cell F5 as 3. This value can be changed at any time. In the [latest version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the easiest way to do this is to use the FILTER function. In [Legacy Excel,](https://exceljet.net/glossary/legacy-excel)
 you can use an alternative formula based on the SUMPRODUCT function as explained below.

### Example formula

In the example shown, the formula in cell F6 is:

    =SUM(FILTER(B5:B16,MOD(SEQUENCE(ROWS(B5:B16)),F5)=0))
    

At a high level, this formula uses the FILTER function to extract values associated with every nth row of the data, and the SUM function to sum the values extracted.

### Extracting data

Working from the inside out, the first step in this problem is to collect the data that should be summed. This is done with the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    FILTER(B5:B16,include)
    

where _include_ represents the formula logic needed to target every nth value (every 3rd value in the example). To construct the logic we need, we use a combination of the MOD function, the SEQUENCE function, and the ROWS function:

    MOD(SEQUENCE(ROWS(B5:B16)),F5)=0)
    

The [ROWS function](https://exceljet.net/functions/rows-function)
 returns the count of rows in the range B5:B16, which is 12:

    MOD(SEQUENCE(12),F5)=0)
    

With 12 as the _rows_ argument, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 returns a numeric [array](https://exceljet.net/glossary/array)
 of 12 numbers like this:

    {1;2;3;4;5;6;7;8;9;10;11;12}
    

Substituting the array above and the value for **n** (3) into the formula we have:

    MOD({1;2;3;4;5;6;7;8;9;10;11;12},3)=0)
    

The [MOD function](https://exceljet.net/functions/mod-function)
 returns the remainder of each number in the array divided by 3:

    {1;2;0;1;2;0;1;2;0;1;2;0}=0
    

The result from MOD is compared to zero, which creates an array of TRUE and FALSE values:

    {FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE}
    

Note that every third value is TRUE. This is the value returned to FILTER as the _include_ argument. FILTER uses this array to "filter" values in the range B5:B16. Only values associated with TRUE make it through the filter operation. The result is an array that contains every 3rd value in the data. Since there are 12 values total, FILTER returns 4 values:

    {20;15;10;25}
    

FILTER delivers this array of values directly to the SUM function, which returns the sum (70) as a final result:

    SUM ({20;15;10;25}) // returns 70
    

This formula is dynamic. For example, if the value for **n** in cell F5 is changed to 2 (every 2nd value) the new result is 120.

### Legacy Excel formula

In [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not include the FILTER or SEQUENCE functions, you can use a different formula based on the SUMPRODUCT function:

    =SUMPRODUCT(--(MOD(ROW(B5:B16)-ROW(B5)+1,F5)=0),B5:B16)
    

The concept is similar to the formula explained above but the approach is different. Rather than extract values of interest from the data, this formula "zeros out" the _other_ values not of interest. First, the formula uses the ROW function to construct a [relative set of row numbers](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
:

    ROW(B5:B16)-ROW(B5)+1
    

The result is a numeric array like this:

    {1;2;3;4;5;6;7;8;9;10;11;12}
    

Inside the SUMPRODUCT function, we again use the MOD function to construct a filter:

    =MOD(ROW(B5:B16)-ROW(B5)+1,F5)=0
    =MOD({1;2;3;4;5;6;7;8;9;10;11;12},F5)=0
    

MOD returns an array of TRUE FALSE values like this:

    {FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE}
    

Again, note that every 3rd value is TRUE. A [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to convert the TRUE and FALSE values to 1s and 0s. Back in the SUMPRODUCT, we now have:

    =SUMPRODUCT({0;1;0;1;0;1;0;1;0;1;0;1},B5:B16)
    

The SUMPRODUCT then multiplies the two arrays together and returns the sum of products. Only the values in B5:B6 that are associated with 1s survive this operation, the other values are "zeroed out":

    =SUMPRODUCT({0;0;20;0;0;15;0;0;10;0;0;25}) // returns 70
    

The final result is 70. This formula is also dynamic. If the value for **n** in cell F5 is changed to 2 (every 2nd value) the new result is 120.

Related formulas
----------------

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Filter every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20every%20nth%20row.png "Excel formula: Filter every nth row")](https://exceljet.net/formulas/filter-every-nth-row)

### [Filter every nth row](https://exceljet.net/formulas/filter-every-nth-row)

The FILTER function is designed to filter and extract information based on logical criteria. In this example, the goal is to extract every 3rd record from the data shown, but there is no row number information in the data. Working from the inside out, the first step is to generate a set of row...

[![Excel formula: Sum every n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20n%20rows.png "Excel formula: Sum every n rows")](https://exceljet.net/formulas/sum-every-n-rows)

### [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)

In this example, the goal is to calculate a weekly total using the data as shown. Notice each week corresponds to 5 rows of data (Monday-Friday) so we will need to sum values in every 5 rows. To build a range that corresponds to the correct 5 rows for each week, we use the OFFSET function. To sum...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Filter every nth row](https://exceljet.net/formulas/filter-every-nth-row)
    
*   [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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
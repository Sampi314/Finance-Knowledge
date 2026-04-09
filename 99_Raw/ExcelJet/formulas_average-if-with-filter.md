# Average if with filter - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-if-with-filter

---

[Skip to main content](https://exceljet.net/formulas/average-if-with-filter#main-content)

[](https://exceljet.net/formulas/average-if-with-filter#)

*   [Previous](https://exceljet.net/formulas/average-if-not-blank)
    
*   [Next](https://exceljet.net/formulas/average-last-3-numeric-values)
    

[Average](https://exceljet.net/formulas#Average)

Average if with filter
======================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[IF](https://exceljet.net/functions/if-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7600/download?token=Qhdbi7hY)
 (14.81 KB)

![Excel formula: Average if with filter](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Average_if_with_filter.png "Excel formula: Average if with filter")

Summary
-------

To calculate a _conditional average_ for multiple columns of data, you can use the [AVERAGE function](https://exceljet.net/functions/average-function)
 with the [FILTER function](https://exceljet.net/functions/filter-function)
. In the worksheet shown, the formula in cell H5 is:

    =AVERAGE(FILTER(data,group=G5))

where **data** (C5:E16) and **group** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is the average of values in group "A" for all three months of data. As the formula is copied down, it calculates an average for each group in column G. The FILTER function is a new function in Excel. See below for alternatives that will work in older versions of Excel.

_Note: I was inspired to create this example after watching a good [video by Excel expert Chandoo](https://www.youtube.com/watch?v=m4J9eRlMvFU)
._

Generic formula
---------------

    =AVERAGE(FILTER(data,group=A1))

Explanation 
------------

In this example, the goal is to calculate an average for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. For convenience only, **data** (C5:E16) and **group** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
. In the article below, we look at several approaches to this problem:

1.  Why the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
     won't work.
2.  A solution based on [AVERAGE](https://exceljet.net/functions/average-function)
     + [FILTER](https://exceljet.net/functions/filter-function)
    
3.  A solution based on [AVERAGE](https://exceljet.net/functions/average-function)
     + [IF function](https://exceljet.net/functions/if-function)
    
4.  A solution based on [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
     and [Boolean algebra](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

In the latest version of Excel, the FILTER option (#2) is easy and intuitive. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, you can use solution #3 or #4.

### AVERAGEIFS won't work

You might be tempted to solve this problem with the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
. After all, it seems to fit the bill. We simply need to calculate an average for a range of data based on one condition: we need to check if **group** (B5:B16) is equal to "A" or "B" or "C". In fact, we can easily use AVERAGEIFS to calculate an average for a given group on _one month_ of data. For example, to calculate an average for group "A" in January, we can use a formula like this:

    =AVERAGEIFS(C5:C16,group,"A") // returns 42

However, if we try to expand _average\_range_ to include all three columns in **data** (C5:E16), we'll get a #VALUE! error:

    =AVERAGEIFS(data,group,"A") // returns #VALUE!

Why? The reason is that [AVERAGEIFS](https://exceljet.net/functions/averageifs-function)
 expects _average\_range_ to be the same size as _criteria\_range_. When we try to use the 1-column range **group** (B5:B16) with the 3-column range **data** (C5:E16), AVERAGEIFS returns an error. Incidentally, if we give the older [AVERAGEIF function](https://exceljet.net/functions/averageif-function)
 the entire data range and the same criteria, we don't get an error, but we do get an _incorrect_ result:

    =AVERAGEIF(group,"A",data) // returns 42

This happens because AVERAGEIF makes certain assumptions about _average\_range_, essentially resizing it to match the _range_ argument, using the upper left cell in the range as an origin. It's worth noting that this kind of "silent failure" is dangerous, in that the result _seems reasonable_ but is in fact _incorrect_. You may not like formula errors, but at least they tell you something is wrong.

### AVERAGE with FILTER

In the latest version of Excel, a good solution in this case is to use the [AVERAGE function](https://exceljet.net/functions/average-function)
 with the [FILTER function](https://exceljet.net/functions/filter-function)
. This is the approach used in the worksheet shown, where the formula in cell H5, copied down, is:

    =AVERAGE(FILTER(data,group=G5))

And **data** (C5:E16) and **group** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
. Inside the AVERAGE function, the FILTER function is configured to filter the data in C5:E16 with a simple logical expression:

    FILTER(data,group=G5)

Because cell G5 contains "A", and **group** (B5:B16) contains 12 values, the expression returns an [array](https://exceljet.net/glossary/array)
 with 12 TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

Notice the first four values in the array are TRUE, which corresponds to the first 4 rows in the data, which are in group A. This array is returned to the FILTER function as the _include_ argument, and FILTER uses this array to select the first 4 rows of **data** (C5:E16).

Video: [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

The result from FILTER is delivered directly to the AVERAGE function as a single array:

    =AVERAGE({58,41,48;37,46,32;38,48,38;35,59,46})

AVERAGE returns a final result of 43.8, the average of the 12 numbers in the array returned by FILTER. As the formula is copied down, it calculates an average for each group, using the value in column G for group.

### AVERAGE with IF

The FILTER function is a newer function that does not exist in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. If you are using an older version of Excel, you can solve this problem with a simple [array formula](https://exceljet.net/articles/what-is-an-array-formula)
 like this:

    {=AVERAGE(IF(group=G5,data))}

In this formula, we use the [IF function](https://exceljet.net/functions/if-function)
 to filter values in each **group** instead of FILTER. When the value in **group** matches the value in G5 ("A"), IF returns the corresponding values in **data**. When a value doesn't match, IF returns FALSE for corresponding values in **data**. After IF is evaluated, the array of results returned to AVERAGE looks like this:

    =AVERAGE({58,41,48;37,46,32;38,48,38;35,59,46;FALSE,FALSE,FALSE;FALSE,FALSE,FALSE;FALSE,FALSE,FALSE;FALSE,FALSE,FALSE;FALSE,FALSE,FALSE;FALSE,FALSE,FALSE;FALSE,FALSE,FALSE;FALSE,FALSE,FALSE})

This works because the [AVERAGE function](https://exceljet.net/functions/average-function)
 will _automatically_ ignore the logical values TRUE and FALSE. This is an array formula and must be entered with control + shift + enter in older versions of Excel.

One thing to be aware of with this approach is that empty cells will be treated as zero, and become part of the calculated average. This happens because when the empty cells get passed through the IF function, they become zero (0). Although the AVERAGE function will ignore empty values, it will include zero (0) values in the calculated average. To avoid this problem, you can add a second IF function to test for empty values like this:

    {=AVERAGE(IF(group=G5,IF(data<>"",data)))}

In this formula, only values that are part of group "A" _and_ are not empty are passed into the AVERAGE function. All other values become FALSE and are ignored by the AVERAGE function.

_Both formulas above are [array formulas](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in older versions of Excel. In the current version of Excel, which supports [array formulas natively](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the formulas will "just work"._

### SUMPRODUCT function

As you might guess, you can also use the flexible [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to solve this problem in older versions of Excel. The formula looks like this:

    =SUMPRODUCT(--(group=G5)*data)/SUMPRODUCT(--(group=G5)*(data<>""))

In this formula, the first SUMPRODUCT calculates a _sum_ of all data in group "A" (from cell G5):

    =SUMPRODUCT(--(group=G5)*data) // sum (526)

The second SUMPRODUCT calculates a _count_ of all data in the same group:

    SUMPRODUCT(--(group=G5)*(data<>"")) // count (12)

After both SUMPRODUCT formulas are evaluated, the final step is to divide the sum by the count:

    =SUMPRODUCT(--(group=G5)*data)/SUMPRODUCT(--(group=G5)*(data<>""))
    =526/12
    =43.8

Although slightly more complicated, the SUMPRODUCT formula _does not_ need to be entered in a special way with control + shift + enter, since [SUMPRODUCT can handle array operations natively](https://exceljet.net/articles/why-sumproduct)
.

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

Related formulas
----------------

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Average with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_with_multiple_criteria.png "Excel formula: Average with multiple criteria")](https://exceljet.net/formulas/average-with-multiple-criteria)

### [Average with multiple criteria](https://exceljet.net/formulas/average-with-multiple-criteria)

In this example, the goal is to calculate an average for each group and region in the data as shown in the worksheet. For convenience, data is an Excel Table in the range B5:D16. This problem can be easily solved with the AVERAGEIFS function . Like the COUNTIFS function and SUMIFS function , the...

[![Excel formula: Sum if multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_columns.png "Excel formula: Sum if multiple columns")](https://exceljet.net/formulas/sum-if-multiple-columns)

### [Sum if multiple columns](https://exceljet.net/formulas/sum-if-multiple-columns)

In this example, the goal is to calculate a sum for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. In other words, we want to perform a "sum if" with a data range that contains three columns. For convenience only, data (C5:E16) and group (B5:B16) are named...

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    
*   [Average with multiple criteria](https://exceljet.net/formulas/average-with-multiple-criteria)
    
*   [Sum if multiple columns](https://exceljet.net/formulas/sum-if-multiple-columns)
    

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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
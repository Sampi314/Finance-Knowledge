# Sum if multiple columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-multiple-columns

---

[Skip to main content](https://exceljet.net/formulas/sum-if-multiple-columns#main-content)

[](https://exceljet.net/formulas/sum-if-multiple-columns#)

*   [Previous](https://exceljet.net/formulas/sum-if-less-than)
    
*   [Next](https://exceljet.net/formulas/sum-if-multiple-criteria)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if multiple columns
=======================

by Dave Bruns · Updated 16 Nov 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SUM](https://exceljet.net/functions/sum-function)

[GROUPBY](https://exceljet.net/functions/groupby-function)

[BYROW](https://exceljet.net/functions/byrow-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8807/download?token=QRVM7uZ_)
 (27.05 KB)

![Excel formula: Sum if multiple columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_multiple_columns.png "Excel formula: Sum if multiple columns")

Summary
-------

To calculate a _conditional sum_ for multiple columns of data, you can use a formula based on [SUM function](https://exceljet.net/functions/sum-function)
 and the [FILTER function](https://exceljet.net/functions/filter-function)
. In the example shown, the formula in H5, copied down, is:

    =SUM(FILTER(data,group=G5))

Here, **data** (C5:E16) and **group** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is the sum of values in group "A" for all three months of data. As the formula is copied down, it calculates a sum for each group in column G.

> The FILTER function is only available in Excel 2021 or later. See below for a formula based on SUMPRODUCT that will work in all versions of Excel.

Generic formula
---------------

    =SUM(FILTER(data,criteria))

Explanation 
------------

In this example, the goal is to calculate a sum for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. In other words, we want to perform a "sum if" with a data range that contains three columns. For convenience only, **data** (C5:E16) and **group** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
. The article below covers the following topics:

1.  [Why SUMIFS won't work](https://exceljet.net/formulas/sum-if-multiple-columns#why_sumifs_wont_work)
    
2.  [FILTER solution](https://exceljet.net/formulas/sum-if-multiple-columns#filter_solution)
    
3.  [SUMPRODUCT solution](https://exceljet.net/formulas/sum-if-multiple-columns#sumproduct_solution)
    
4.  [More advanced criteria](https://exceljet.net/formulas/sum-if-multiple-columns#more_advanced_criteria)
    
5.  [Clever all-in-one-formula](https://exceljet.net/formulas/sum-if-multiple-columns#all_in_one_formula)
    

In Excel 2021 or later, the FILTER solution is easy and intuitive. If you are using an older version of Excel, use the SUMPRODUCT option. The section on advanced criteria covers both options.

### Why SUMIFS won't work

You might be tempted to solve this problem with the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 or the [SUMIF function](https://exceljet.net/functions/sumif-function)
. After all, it seems simple enough - we need to check if **group** (B5:B16) is equal to "A" or "B" or "C", then sum the corresponding numbers in columns C, D, and E. In fact, we can easily use SUMIFS to calculate a sum for a given group on _one month_ of data. For example, to calculate a sum for group "A" in January, we can use a formula like this:

    =SUMIFS(C5:C16,group,"A") // returns 168

However, if you try to expand _sum\_range_ to include all three columns in **data** (C5:E16), you'll get a #VALUE! error:

    =SUMIFS(data,group,"A") // returns #VALUE!

Why? The reason is that SUMIFS expects _sum\_range_ to be the same size as _criteria\_range_. When we try to use the 1-column range **group** (B5:B16) with the 3-column range **data** (C5:E16), SUMIFS returns an error. What about the SUMIF function? If we give the older SUMIF function the entire data range and the same criteria, we don't get an error, but we do get an _incorrect_ result:

    =SUMIF(group,"A",data) // returns 168

This happens because SUMIF _assumes_ that the _sum\_range_ is the same size as the _range_. Basically, SUMIF resizes _sum\_range_ to match the _range_ argument. This kind of "silent failure" is dangerous because the result _seems reasonable_ but is, in fact, _incorrect_. You may not like formula errors, but at least they tell you something is wrong!

So, at this point, we could start chaining together multiple SUMIF or SUMIFS functions like this:

    =SUMIFS(C5:C16,group,"A")+SUMIFS(D5:D16,group,"A")+SUMIFS(E5:E16,group,"A")

But there must be a better way to do this in Excel, right? Yes!

### FILTER solution

In the current version of Excel, a nice solution is the [SUM function](https://exceljet.net/functions/sum-function)
 with the [FILTER function](https://exceljet.net/functions/filter-function)
. This is the approach used in the worksheet shown, where the formula in cell H5, copied down, is:

    =SUM(FILTER(data,group=G5))

Where **data** (C5:E16) and **group** (B5:B16) are [named ranges](https://exceljet.net/glossary/named-range)
. Inside the SUM function, the FILTER function is configured to filter the data in C5:E16 with a simple logical expression:

    FILTER(data,group=G5)

Because cell G5 contains "A", and **group** (B5:B16) contains 12 values, the expression returns an [array](https://exceljet.net/glossary/array)
 with 12 TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

Notice the first four values in the array are TRUE, which corresponds to the first 4 rows in the data, which are in group A. This array is returned to the FILTER function as the _include_ argument, and FILTER uses this array to select the first 4 rows of **data** (C5:E16).

The result from FILTER is delivered directly to the SUM function as a single array:

    =SUM({58,41,48;37,46,32;38,48,38;35,59,46})

SUM returns a final result of 526, the sum of the 12 numbers in the array returned by FILTER. As the formula is copied down, it calculates the correct sum for each group.

> This is a good example of how the FILTER function can change how you think about a problem in Excel. The trick is realizing that you can solve the problem in two simple steps: (1) filter the data, then (2) sum the data. If you are new to the FILTER function, see [this short video](https://exceljet.net/videos/filter-function-basic-example)
>  for a quick intro.

### SUMPRODUCT solution

You can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to solve this problem in older versions of Excel like this:

    =SUMPRODUCT(--(group=G5)*data)

Working from the inside out, the logical expression on the left tests for group A like this:

    --(group=G5) // test all group values

Since we are comparing one value in G5 to the 12 values in **group**, we get back 12 results:

    --{TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

Next, we use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert the TRUE and FALSE values to 1s and 0s. At this point, the result inside of SUMPRODUCT looks like this:

    =SUMPRODUCT({1;1;1;1;0;0;0;0;0;0;0;0}*data)

> _Notes: (1) technically, the double negative (--) is unnecessary in this formula because multiplying the TRUE and FALSE values by the numeric values in the data will automatically convert TRUE and FALSE values to 1s and 0s. However, the double negative does no harm, and I think it makes the formula easier to understand because it signals a [Boolean operation](https://exceljet.net/videos/boolean-operations-in-array-formulas)
> . (2) Like SUMIFS, SUMPRODUCT also requires that range/array arguments be the same size. We side-step this requirement above by multiplying the group \* data inside array1. The result is that SUMPRODUCT only gets a single array._

After multiplication, we have a single array in SUMPRODUCT like this:

    =SUMPRODUCT({58,41,48;37,46,32;38,48,38;35,59,46;0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;0,0,0})

Notice the Boolean array acts like a filter to "cancel out" values not associated with group "A". Only the 12 values in group A survive the operation, while the other 24 values are forced to zero. With just a single array to process, SUMPRODUCT sums the array and returns a final result: 526.

_Note: although this is an array formula, the SUMPRODUCT formula does not need to be entered in a special way with control + shift + enter, because [SUMPRODUCT can handle array operations natively](https://exceljet.net/articles/why-sumproduct)
._

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### More advanced criteria

Although the criteria needed for this example is simple (test for a specific group), you can adapt the criteria to handle more complex scenarios. For example, to perform a "contains" type search for a _substring_, you could use a FILTER formula like this:

    =SUM(FILTER(data,ISNUMBER(SEARCH(G5,group))))

Or a SUMPRODUCT formula like this:

    =SUMPRODUCT(--ISNUMBER(SEARCH(G5,group))*data)

These formulas will sum by group, treating the value in G5 as a substring. For more information about this particular logic, [see this example](https://exceljet.net/formulas/cell-contains-specific-text)
.

### Clever all-in-one formula

In the latest version of Excel 365, you can solve this problem with a clever all-in-one formula based on the [GROUPBY function](https://exceljet.net/functions/groupby-function)
 and the [BYROW function](https://exceljet.net/functions/byrow-function)
. In the workbook below, there is just one formula entered in cell G5:

![A clever all in one formula option](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sum_if_multiple_columns_clever_all_in_one_formula.png "A clever all in one formula option")

In this formula, the BROW function generates a sum for each row in "data", and the GROUPBY function groups these sums by the group values in column C automatically. Pretty cool!

Related formulas
----------------

[![Excel formula: Sum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_criteria.png "Excel formula: Sum if multiple criteria")](https://exceljet.net/formulas/sum-if-multiple-criteria)

### [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)

In this example, the goal is to sum the values in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". This is an example of a conditional sum with multiple criteria and the SUMIFS function is the easiest way to solve this problem. SUMIFS function The SUMIFS function sums cells...

[![Excel formula: Average if with filter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Average_if_with_filter.png "Excel formula: Average if with filter")](https://exceljet.net/formulas/average-if-with-filter)

### [Average if with filter](https://exceljet.net/formulas/average-if-with-filter)

In this example, the goal is to calculate an average for any given group ("A", "B", or "C") across all three months of data in the range C5:E16. For convenience only, data (C5:E16) and group (B5:B16) are named ranges . In the article below, we look at several approaches to this problem: Why the...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel GROUPBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_groupby_function.png "Excel GROUPBY function")](https://exceljet.net/functions/groupby-function)

### [GROUPBY Function](https://exceljet.net/functions/groupby-function)

The Excel GROUPBY function is designed to summarize data by grouping rows and aggregating values. The result is a summary table created with a single formula.

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

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

*   [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)
    
*   [Average if with filter](https://exceljet.net/formulas/average-if-with-filter)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [GROUPBY Function](https://exceljet.net/functions/groupby-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

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
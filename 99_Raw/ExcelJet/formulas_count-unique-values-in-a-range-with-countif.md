# Count unique values in a range with COUNTIF - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif

---

[Skip to main content](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif#main-content)

[](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif#)

*   [Previous](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Next](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)
    

[Count](https://exceljet.net/formulas#Count)

Count unique values in a range with COUNTIF
===========================================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count unique values in a range with COUNTIF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20unique%20values%20with%20COUNTIF.png "Excel formula: Count unique values in a range with COUNTIF")

Summary
-------

To count the number of unique values in a range of cells, you can use a formula based on the [COUNTIF](https://exceljet.net/functions/countif-function)
 and [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 functions. In the example shown, the formula in F6 is:

    =SUMPRODUCT(1/COUNTIF(B5:B14,B5:B14))
    

> In [Dynamic Excel](https://exceljet.net/glossary/dynamic-excel)
> , you can use a [simpler and faster formula](https://exceljet.net/formulas/count-unique-values)
>  based on [UNIQUE](https://exceljet.net/functions/unique-function)
> .

Generic formula
---------------

    =SUMPRODUCT(1/COUNTIF(data,data))

Explanation 
------------

Working from the inside out, COUNTIF is configured to values in the range B5:B14, using all of these _same_ values as criteria:

    COUNTIF(B5:B14,B5:B14)
    

Because we provide 10 values for criteria, we get back an [array](https://exceljet.net/glossary/array)
 with 10 results like this:

    {3;3;3;2;2;3;3;3;2;2}
    

Each number represents a count – "Jim" appears 3 times, "Sue" appears 2 times, and so on.

This array is configured as a divisor with 1 as the numerator. After division, we get another array:

    {0.333333333333333;0.333333333333333;0.333333333333333;0.5;0.5;0.333333333333333;0.333333333333333;0.333333333333333;0.5;0.5}
    

Any values that occur in just once in the range will appear as 1s, but values that occur multiple times will appear as fractional values that correspond to the multiple. (i.e. a value that appears 4 times in data will generate 4 values = 0.25).

Finally, the SUMPRODUCT function sums all values in the array and returns the result.

### Handling blank cells

One way to handle blank or empty cells is to adjust the formula as follows:

    =SUMPRODUCT(1/COUNTIF(data,data&""))
    

By [concatenating](https://exceljet.net/glossary/concatenation)
 an [empty string](https://exceljet.net/glossary/empty-string)
 ("") to the data, we prevent zeros from ending up in the array created by COUNTIF when there are blank cells in the data. This is important, because a zero in the divisor will cause the formula to throw a #DIV/0 error. It works because using an empty string ("") for criteria will count empty cells.

However, although this version of the formula won't throw a #DIV/0 error when with blank cells, it _will_ include blank cells in the count. If you want to exclude blank cells from the count, use:

    =SUMPRODUCT((data<>"")/COUNTIF(data,data&""))
    

This has the effect of canceling out the count of blank cells by making the numerator zero for associated counts.

### Slow Performance?

This is a cool and elegant formula, but it calculates much more slowly than formulas that use FREQUENCY to count unique values. For larger data sets, you may want to switch to a formula based on the FREQUENCY function. Here's a formula for [numeric values](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
, and one for [text values](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
.

### UNIQUE function in Excel 365

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 provides a better, more elegant way to [list unique values](https://exceljet.net/formulas/unique-values)
 and [count unique values](https://exceljet.net/formulas/count-unique-values)
. 

Related formulas
----------------

[![Excel formula: Count unique numeric values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values.png "Excel formula: Count unique numeric values in a range")](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

### [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

[![Excel formula: Count unique text values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20text%20values%20in%20a%20range.png "Excel formula: Count unique text values in a range")](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

### [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

This formula is more complicated than a similar formula that uses FREQUENCY to count unique numeric values because FREQUENCY doesn't normally work with non-numeric values. As a result, a large part of the formula simply transforms the non-numeric data into numeric data that FREQUENCY can handle...

[![Excel formula: Count unique text values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20text%20values%20with%20criteria.png "Excel formula: Count unique text values with criteria")](https://exceljet.net/formulas/count-unique-text-values-with-criteria)

### [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)

This is a complex formula that uses FREQUENCY to count numeric values that are derived with the MATCH function. Working from the inside out, the MATCH function is used to get the position of each value that appears in the data: MATCH(B5:B11,B5:B11,0) The result from MATCH is an array like this: {1;...

[![Excel formula: Count unique numeric values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values%20with%20criteria.png "Excel formula: Count unique numeric values with criteria")](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)

### [Count unique numeric values with criteria](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
    
*   [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    
*   [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Count unique numeric values with criteria](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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
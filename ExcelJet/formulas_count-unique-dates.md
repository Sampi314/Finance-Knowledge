# Count unique dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-dates

---

[Skip to main content](https://exceljet.net/formulas/count-unique-dates#main-content)

[](https://exceljet.net/formulas/count-unique-dates#)

*   [Previous](https://exceljet.net/formulas/count-total-matches-in-two-ranges)
    
*   [Next](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
    

[Count](https://exceljet.net/formulas#Count)

Count unique dates
==================

by Dave Bruns · Updated 11 Jul 2022

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[COUNT](https://exceljet.net/functions/count-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6336/download?token=0BVLxuQg)
 (14.29 KB)

![Excel formula: Count unique dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20unique%20dates2.png "Excel formula: Count unique dates")

Summary
-------

To count unique dates ("trading days" in the example) you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 with the [COUNT function](https://exceljet.net/functions/count-function)
, or a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in cell G8 is:

    =COUNT(UNIQUE(date))
    

where **date** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16.

Generic formula
---------------

    =COUNT(UNIQUE(date))

Explanation 
------------

Traditionally, counting unique items with an Excel formula has been a tricky problem, because there hasn't been a dedicated unique function. However, that changed when [dynamic arrays were added to Excel 365](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, along with several new functions, including UNIQUE.

_Note: In older versions of Excel, you can count unique items with the COUNTIF function, or the FREQUENCY function, as explained below._

In the example shown, each row in the table represents a stock trade. On some dates, more than one trade is performed. The goal is to count trading days – the number of unique dates on which some kind of trade occurred. The formula in cell G8 is:

    =COUNT(UNIQUE(date))
    

Working from the inside out, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 is used to extract a list of unique dates from the named range **date**:

    UNIQUE(date) // extract unique values
    

The result is an array with 5 numbers like this:

    {44105;44109;44111;44113;44116}
    

Each number represents an [Excel date](https://exceljet.net/glossary/excel-date)
, without [date formatting](https://exceljet.net/articles/custom-number-formats)
. The 5 dates are 1-Oct-20, 5-Oct-20, 7-Oct-20, 9-Oct-20, and 12-Oct-20.

This array is delivered directly to the [COUNT function](https://exceljet.net/functions/count-function)
:

    =COUNT({44105;44109;44111;44113;44116}) // returns 5
    

which returns a count of numeric values, 5, as the final result.

_Note: The COUNT function counts numeric values, while the [COUNTA function](https://exceljet.net/functions/counta-function)
 will count both numeric and text values. Depending on the situation, it may make sense to use one or the other. In this case, because dates are numeric, we use COUNT._

### With COUNTIF

In an older version of Excel, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 to count unique dates with a formula like this:

    =SUMPRODUCT(1/COUNTIF(date,date))
    

Working from the inside out, COUNTIF returns an array with a count for every date in the list:

    COUNTIF(date,date) // returns {2;2;3;3;3;2;2;2;2;3;3;3}
    

At this point, we have:

    =SUMPRODUCT(1/{2;2;3;3;3;2;2;2;2;3;3;3})
    

After 1 is divided by this array, we have an array of fractional values:

    {0.5;0.5;0.333333333333333;0.333333333333333;0.333333333333333;0.5;0.5;0.5;0.5;0.333333333333333;0.333333333333333;0.333333333333333}
    

This array is delivered directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. SUMPRODUCT then sums the items in the array and returns the total, 5.

### With FREQUENCY

If you are working with a large set of data, you might have performance problems with the COUNTIF formula above. In that case, you can switch to an [array formula](https://exceljet.net/glossary/array-formula)
 based on the [FREQUENCY function](https://exceljet.net/functions/frequency-function)
:

    {=SUM(--(FREQUENCY(date,date)>0))}
    

_Note: This is an array formula and must be entered with control + shift + enter, except in Excel 365._

This formula will calculate faster than the COUNTIF version above, but it will only work with numeric values.  For more details, [see this article](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
.

Related formulas
----------------

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

[![Excel formula: Count unique values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values%20with%20criteria.png "Excel formula: Count unique values with criteria")](https://exceljet.net/formulas/count-unique-values-with-criteria)

### [Count unique values with criteria](https://exceljet.net/formulas/count-unique-values-with-criteria)

In this example, the goal is to count unique values that meet one or more specific conditions. In the example shown, the formula used in cell H7 is: =SUM(--(LEN(UNIQUE(FILTER(B6:B15,C6:C15=H6,"")))>0)) At the core, this formula uses the FILTER function to apply criteria, and the UNIQUE function...

[![Excel formula: Count unique values in a range with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values%20with%20COUNTIF.png "Excel formula: Count unique values in a range with COUNTIF")](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)

### [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)

Working from the inside out, COUNTIF is configured to values in the range B5:B14, using all of these same values as criteria: COUNTIF(B5:B14,B5:B14) Because we provide 10 values for criteria, we get back an array with 10 results like this: {3;3;3;2;2;3;3;3;2;2} Each number represents a count – "Jim...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20UNIQUE%20function-Play.png)](https://exceljet.net/videos/the-unique-function)

### [The UNIQUE function](https://exceljet.net/videos/the-unique-function)

In this video, we'll introduce the UNIQUE function . One of the new functions that comes with the dynamic array version of Excel is UNIQUE. The UNIQUE function lets you extract unique values in a variety of ways. The UNIQUE function takes three arguments. The first argument, array is the source...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    
*   [Count unique values with criteria](https://exceljet.net/formulas/count-unique-values-with-criteria)
    
*   [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Videos

*   [The UNIQUE function](https://exceljet.net/videos/the-unique-function)
    

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
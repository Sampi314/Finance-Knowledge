# Count unique dates ignore time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-dates-ignore-time

---

[Skip to main content](https://exceljet.net/formulas/count-unique-dates-ignore-time#main-content)

[](https://exceljet.net/formulas/count-unique-dates-ignore-time#)

*   [Previous](https://exceljet.net/formulas/combine-ranges)
    
*   [Next](https://exceljet.net/formulas/count-unique-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Count unique dates ignore time
==============================

by Dave Bruns · Updated 1 Feb 2023

Related functions 
------------------

[INT](https://exceljet.net/functions/int-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[COUNT](https://exceljet.net/functions/count-function)

[LET](https://exceljet.net/functions/let-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[SCAN](https://exceljet.net/functions/scan-function)

![Excel formula: Count unique dates ignore time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20unique%20dates%20ignore%20time.png "Excel formula: Count unique dates ignore time")

Summary
-------

To count unique dates and ignore time values you can use a formula based on the [UNIQUE](https://exceljet.net/functions/unique-function)
, [INT](https://exceljet.net/functions/int-function)
, and [COUNT](https://exceljet.net/functions/count-function)
 functions. In the example shown, the formula in F4 is:

    =COUNT(UNIQUE(INT(data)))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16, and each timestamp includes both a date and time. See below for the formulas used to generate the summary table in E7:F9.

Generic formula
---------------

    =COUNT(UNIQUE(INT(data)))

Explanation 
------------

In this example, the goal is to count the unique dates in a range of timestamps (i.e. dates that contain dates and times). In addition, we also want to create the table of results seen in E7:F9. For convenience, **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16.

### Basic count

To get a count of individual dates that occur in B5:B16, ignoring time values, the formula in F4 is:

    =COUNT(UNIQUE(INT(data)))
    

Working from the inside out, the [INT function](https://exceljet.net/functions/int-function)
 is used to remove the time values from the timestamps like this:

    INT(data) // remove time
    

This works because [Excel dates are just serial numbers](https://exceljet.net/glossary/excel-date)
 and [Excel times are fractional dates](https://exceljet.net/glossary/excel-time)
 that appear as decimal values. The [INT function](https://exceljet.net/functions/int-function)
 simply removes the decimal portion of the date, leaving the serial number intact. Because we are giving the INT function 12 separate values, INT returns 12 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {44600;44600;44600;44600;44604;44604;44604;44635;44635;44635;44635;44635}
    

Each serial number in this array represents a date in **data**. Next, the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
 is used to remove duplicate dates. The two functions work together like this:

    UNIQUE(INT(data)) // returns {44600;44604;44635}
    

Because there are 3 unique dates, UNIQUE returns 3 serial numbers in an array like this:

    {44600;44604;44635}
    

This array is delivered directly to the COUNT function:

    =COUNT({44600;44604;44635}) // returns 3
    

and the [COUNT function](https://exceljet.net/functions/count-function)
 (which counts numbers only) returns 3 as a final result.

### Summary table in two parts

An easy way to create the summary table seen in the worksheet is to use two formulas. To list the 3 unique dates starting in cell D7, you can use:

    =UNIQUE(INT(data)) // unique dates
    

To count how many times each date occurs in the data, you can enter this formula in cell F7 and copy it down:

    =SUM(--(INT(data)=K7))
    

Note: we can't use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 in this case (which would be easier) because we don't have the dates without times in an actual [range](https://exceljet.net/glossary/range)
. Instead, the dates exist in an [array](https://exceljet.net/glossary/array)
 returned by the INT function. [COUNTIF requires a range](https://exceljet.net/articles/excels-racon-functions)
 for the _range_ argument.

### All-in-one summary table

To create an all-in-one summary table that lists the unique dates along with a count for each date, you can use an advanced formula like this:

    =LET(d,INT(data),u,UNIQUE(d),HSTACK(u,SCAN(0,u,LAMBDA(a,v,SUM(--(v=d))))))
    

![All-in-one summary table formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20unique%20dates%20ignore%20time%20summary%20table.png?itok=QZ6f6m2W "All-in-one summary table formula")

The [LET function](https://exceljet.net/functions/let-function)
 is used to assign intermediate results to named variables. First, we use INT to strip times from dates and assign the result to **d**. Then we feed **d** into UNIQUE (to get unique dates) and assign the result to **u.** Next, we use the [HSTACK function](https://exceljet.net/functions/hstack-function)
 to combine two arrays. _Array1_ is **u** (the unique dates), and _array2_ is generated with the [SCAN function](https://exceljet.net/functions/scan-function)
:

    SCAN(0,u,LAMBDA(a,v,SUM(--(v=d))))
    

With an initial value of zero, SCAN iterates through each date in **u** and runs a custom LAMBDA function to count how many times the date appears in **d**:

    LAMBDA(a,v,SUM(--(v=d))
    

The count is generated with [boolean logic](https://exceljet.net/glossary/boolean-logic)
 and the [SUM function](https://exceljet.net/functions/sum-function)
. The result from SCAN is an array with 3 counts:

    {4;3;5}
    

This array is returned to HSTACK as _array2_. HSTACK joins _array1_ and _array2_ together horizontally, and returns the 2-column array as a final result.

Related formulas
----------------

[![Excel formula: Count unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values.png "Excel formula: Count unique values")](https://exceljet.net/formulas/count-unique-values)

### [Count unique values](https://exceljet.net/formulas/count-unique-values)

This example uses the UNIQUE function to extract unique values. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. These are returned directly to the COUNTA function as an array like this: =COUNTA({"red";"amber";"green";"blue";"...

[![Excel formula: Sum numbers with text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20numbers%20with%20text.png "Excel formula: Sum numbers with text")](https://exceljet.net/formulas/sum-numbers-with-text)

### [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)

In this example, one goal is to sum the numbers that appear in the range B5:B16. A second more challenging goal is to create the table of results seen in E7:F12. For convenience, data is the named range B5:B16. Total sum To sum all the numbers that appear in B5:B16, ignoring text, the formula in E5...

Related functions
-----------------

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count unique values](https://exceljet.net/formulas/count-unique-values)
    
*   [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)
    

### Functions

*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    

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
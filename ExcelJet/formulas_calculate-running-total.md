# Calculate running total - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-running-total

---

[Skip to main content](https://exceljet.net/formulas/calculate-running-total#main-content)

[](https://exceljet.net/formulas/calculate-running-total#)

*   [Previous](https://exceljet.net/formulas/two-way-summary-count)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-formulas)
    

[Sum](https://exceljet.net/formulas#Sum)

Calculate running total
=======================

by Dave Bruns · Updated 9 Dec 2025

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

[SCAN](https://exceljet.net/functions/scan-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7448/download?token=0oakda3P)
 (17.89 KB)

![Excel formula: Calculate running total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Calculate%20running%20total.png "Excel formula: Calculate running total")

Summary
-------

To calculate a running total (sometimes called a "cumulative sum") you can use the [SUM function](https://exceljet.net/functions/sum-function)
 with an [expanding reference](https://exceljet.net/glossary/expanding-reference)
. In the example shown, the formula in cell D5 is:

    =SUM($C$5:C5)
    

As this formula is copied down the column, it calculates a running total on each row — a cumulative sum of all amounts up to that point.

Generic formula
---------------

    =SUM($A$1:A1)

Explanation 
------------

In this example, the goal is to calculate a running total in column D of the worksheet as shown. A running total, or cumulative sum, is a set of partial sums that changes as more data is collected. Each calculation represents the sum of values up to that point. In this example, each calculation takes into account another month of the year. There are several ways to approach this problem, as explained below.

_Note: if you want to create a running total in an_ [_Excel Table_](https://exceljet.net/glossary/excel-table)
_, you'll want to take a different approach from the formulas below. See_ [_this example_](https://exceljet.net/formulas/running-total-in-table)
_._

### SUM with expanding range

An easy way to create a running total in Excel is to use the [SUM function](https://exceljet.net/videos/how-to-use-the-sum-function)
 with what is called an "[expanding reference](https://exceljet.net/glossary/expanding-reference)
" — a special kind of reference that includes both absolute _and_ relative parts. In the example shown, the formula in D5 is:

    =SUM($C$5:C5)
    

Notice this range refers to one cell only (C5:C5). However, while the first reference to C5 on the left side of the colon (:) is an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 ($C$5), the second reference is a [relative reference](https://exceljet.net/glossary/relative-reference)
 (C5). As a result, when the formula is copied down the column, the left side of the range is "locked" and won't change, but the right side of the range is _relative_ and will change at each new row.  The result is that the range expands by one row each time it is copied down:

    =SUM($C$5:C5) // formula in D5
    =SUM($C$5:C6) // formula in D6
    =SUM($C$5:C7) // formula in D7
    =SUM($C$5:C8) // formula in D8
    

At each new row, the SUM function receives a larger range that includes the amount in the current row. The result is a cumulative sum of the values in column C up to that point.

_Note: formulas with expanding ranges can cause performance problems in large sets of data. The formula below is more efficient._

### SUM with two values

Another nice way to solve this problem is to use the SUM function to add the current amount to the _previous_ cumulative sum. In cell D5, you can write a formula like this:

    =SUM(C5,D4)
    

You can see this option in the screen below:

![Running total with SUM function and two values](https://exceljet.net/sites/default/files/images/formulas/inline/Calculate%20running%20total%20sum%20two%20values.png "Running total with SUM function and two values")

This may seem unusual, since D4 contains text, and not a number. However, the purpose of constructing the formula this way is to allow the _same formula_ to be copied down the column without changes. Using the same formula in a column is considered a best practice because it makes things more consistent and reduces the chance of errors when formulas are copied. The reason we use the [SUM function](https://exceljet.net/functions/sum-function)
 in this formula, instead of simple addition, is that SUM will _automatically_ ignore [text values](https://exceljet.net/glossary/text-value)
. If we try instead to write a formula like this:

    =C5+D4 // returns #VALUE!
    

The result is a #VALUE! error, because Excel's formula engine by default will not allow a number and text to be added together.

### SCAN function

This problem can also be solved with the [SCAN function](https://exceljet.net/functions/scan-function)
, a new function in Excel designed to work with [dynamic arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. SCAN can be used to generate running totals and other calculations that show intermediate or incremental results. The SCAN function uses the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to apply the logic needed. The LAMBDA is applied to each value, and the result from SCAN is an [array](https://exceljet.net/glossary/array)
 of results with the same dimensions as the original array. The structure of the LAMBDA used inside SCAN looks like this:

    LAMBDA(a,v,calculation)
    

The first argument, _a_, is the _accumulator_ used to create intermediate values. The accumulator begins as the _initial\_value_ provided to SCAN and changes as the SCAN function loops over the elements in _array_ and applies a calculation. The _v_ argument represents the _value_ of each element in _array_. _Calculation_ is the formula that creates the intermediate values that will appear in the final result. In this example, the basic SCAN formula to create a running total looks like this:

    =SCAN(0,C5:C16,LAMBDA(a,v,a+v))
    

Notice the initial value of the accumulator is zero. At each new row, we simply add the current value (v) to the accumulator (a). Because we give SCAN an array that contains 12 values, SCAN will return an array with 12 results like this:

    {1000;3500;5250;9750;15950;21450;25700;25700;25700;25700;25700;25700}
    

All twelve values will [spill](https://exceljet.net/glossary/spill)
 into the range D5:D16. To skip rows where the value in column C is not yet available, we can adapt the formula as follows:

    =SCAN(0,C5:C16,LAMBDA(a,v,IF(v<>"",a+v,"")))
    

In this version, we check to see if the current value (v) is _not empty_. If so, we return a+v. If v is empty, we return an [empty string](https://exceljet.net/glossary/empty-string)
 (""). The array returned by SCAN with the modified LAMBDA looks like this:

    {1000;3500;5250;9750;15950;21450;25700;"";"";"";"";""}
    

Here is the result on the worksheet:

![ Calculate running total with the SCAN function](https://exceljet.net/sites/default/files/images/formulas/inline/Calculate%20running%20total%20with%20SCAN.png " Calculate running total with the SCAN function")

Notice the last five values are empty strings, which will display as blank cells in Excel. The key advantage to use SCAN in a problem like this is that it returns all results at the same time in a [dynamic array](https://exceljet.net/glossary/dynamic-array)
. This makes it possible to use SCAN in more powerful [all-in-one formulas](https://exceljet.net/formulas/dynamic-summary-count)
.

### Pivot Table

A [Pivot Table](https://exceljet.net/glossary/pivot-table)
 is another good way to calculate running totals. See a [basic example here](https://exceljet.net/pivot-tables/pivot-table-running-total)
.

Related formulas
----------------

[![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

### [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the named range value . The core of the solution explained below is the COUNTIF function , with help from the IF function to suppress a count for...

[![Excel formula: Running total in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20total%20in%20table2.png "Excel formula: Running total in Table")](https://exceljet.net/formulas/running-total-in-table)

### [Running total in Table](https://exceljet.net/formulas/running-total-in-table)

At the core, this formula has a simple pattern like this: =SUM(first:current) Where "first" is the first cell in the Total column, and "current" is a reference to a cell in the current row of the Total column. To get the a reference to the first cell, we use INDEX like this: INDEX(\[Total\],1) Here,...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20a%20mixed%20reference%20to%20create%20a%20running%20total-thumb.png)](https://exceljet.net/videos/how-to-use-a-mixed-reference-to-create-a-running-total)

### [How to use a mixed reference to create a running total](https://exceljet.net/videos/how-to-use-a-mixed-reference-to-create-a-running-total)

Another example of a situation where you may need a mixed reference is a running total. Let's take a look. With normal totals, you can just sum a range and be done. The SUM function adds together all the values in the range and reports the result. But what if you want to create a running total?...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20set%20up%20a%20running%20total%20in%20a%20table-Thumb.png)](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)

### [How to set up a running total in a table](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)

In this video, we'll look at how to set up a running total in an Excel table. Setting up a running total in an Excel table is a little tricky because it's not obvious how to use structured references. This is because structured references provide a notation for current row, but not for first row in...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [Running total in Table](https://exceljet.net/formulas/running-total-in-table)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    

### Videos

*   [How to use a mixed reference to create a running total](https://exceljet.net/videos/how-to-use-a-mixed-reference-to-create-a-running-total)
    
*   [How to set up a running total in a table](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)
    

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
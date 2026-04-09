# Get column totals - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-column-totals

---

[Skip to main content](https://exceljet.net/formulas/get-column-totals#main-content)

[](https://exceljet.net/formulas/get-column-totals#)

*   [Previous](https://exceljet.net/formulas/generate-random-text-strings)
    
*   [Next](https://exceljet.net/formulas/get-row-totals)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Get column totals
=================

by Dave Bruns · Updated 27 Mar 2022

Related functions 
------------------

[BYCOL](https://exceljet.net/functions/bycol-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[MMULT](https://exceljet.net/functions/mmult-function)

[ROW](https://exceljet.net/functions/row-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel formula: Get column totals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20column%20totals.png "Excel formula: Get column totals")

Summary
-------

To get an array of column totals based from range of numeric values, you can use a formula based on the [BYCOL function](https://exceljet.net/functions/bycol-function)
 together with the [LAMBDA](https://exceljet.net/functions/lambda-function)
 and [SUM](https://exceljet.net/functions/sum-function)
 functions. In the example shown, the formula in C15 is:

    =BYCOL(data,LAMBDA(col,SUM(col)))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:I13. The result is an [array](https://exceljet.net/glossary/array)
 of with 7 sums, one for each column in the range, as seen in row 15.

_Note: in older versions of Excel you can use the [MMULT function](https://exceljet.net/functions/mmult-function)
, as explained below._

Generic formula
---------------

    =BYCOL(data,LAMBDA(col,SUM(col)))

Explanation 
------------

In this example, the goal is to return an array with 7 subtotals, one for each day of the week, as seen in columns C:I. The numbers to sum are contained in **data** which is the [named range](https://exceljet.net/glossary/named-range)
 C5:I13. This is an example of a problem where the goal is to create an [array](https://exceljet.net/glossary/array)
 of sums rather than a single sum. We can't use a function like [SUM](https://exceljet.net/functions/sum-function)
 by itself, because SUM will _aggregate_ results and return a single value. In the article below, we look at two approaches, one based on the [BYCOL function](https://exceljet.net/functions/bycol-function)
, and one based on the [MMULT function](https://exceljet.net/functions/mmult-function)
.

### With the BYCOL function

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the most straightforward way to generate subtotals for each column is with the [BYCOL function](https://exceljet.net/functions/bycol-function)
. The purpose of BYCOL is to process data in a "by column" fashion. For example, if BYCOL is given an array with 7 columns, BYCOL will return single [array](https://exceljet.net/glossary/array)
 with 7 results. In the example shown, the formula in C15 is:

    =BYCOL(data,LAMBDA(col,SUM(col)))
    

The calculation performed on each column is provided by a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
, which must return a single result for each column. In this example, the LAMBDA function used in BYCOL sums each row like this:

    LAMBDA(col,SUM(col)) // sum each column
    

The result is an array of sums, one per column, that [spill](https://exceljet.net/glossary/spill)
 into the range C15:I15. This result is fully dynamic. If data values change, or if the data range expands or contracts, the output from BYCOL will update as needed.

The result is an array of sums, one per row, that [spill](https://exceljet.net/glossary/spill)
 into the range K5:K13. This result is fully dynamic. If data values change, or if the data range expands or contracts, the output from BYROW will update as needed. Although this example deals with totals, the same pattern can be used to calculate other information about columns, including max, min, average, etc. like this:

    =BYCOL(data,LAMBDA(col,MAX(col))) // max
    =BYCOL(data,LAMBDA(col,MIN(row))) // min
    =BYCOL(data,LAMBDA(col,AVERAGE(col))) // average
    

### With the MMULT function

Another way to solve this problem is with the [MMULT function](https://exceljet.net/functions/mmult-function)
, which performs matrix multiplication. MMULT takes two arrays, _array1_ and _array2_, and requires that the number of _columns in array1_ be the same as the number of _rows in array2_. The resulting matrix will have same number of rows as the first matrix, and the same number of columns as the second matrix. The MMULT formula looks like this:

    =MMULT(TRANSPOSE(ROW(data)^0),--data)
    

In column-based operations with MMULT, the data appears as _array2_, which is simply all values in **data**, the [named range](https://exceljet.net/glossary/named-range)
 C5:I13:

    --data
    

To protect against blank cells, which will cause MMULT to throw #VALUE! error, we use a [double negative](https://exceljet.net/glossary/double-unary)
 (--) to force any empty cells to zero.

_Array1_ needs to be constructed with respect to _array2_. Because _array2_ contains 9 rows, we need _array1_ to contain 9 columns. We want just a single row of results, so the dimensions of _array1_ should be 1 row by 9 columns (1 x 9). Also, because we don't want to change any values, _array1_ should contain only the number 1 (i.e. multiplying by 1 does not change the original value). The code to create _array1_ uses the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 and the [ROW function](https://exceljet.net/functions/row-function)
 like this:

    TRANSPOSE(ROW(data)^0)
    

The [ROW function](https://exceljet.net/functions/row-function)
 returns a 1 x 7 array of row numbers:

    ROW(data) // returns {5;6;7;8;9;10;11;12;13}
    

Next, these numbers are raised to the power of zero with [exponent operator](https://exceljet.net/glossary/math-operators)
 (^), which creates a 1 x 7 array of 1s:

    ROW(data)^0) // returns {1;1;1;1;1;1;1;1;1}
    

And the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 flips the array from 9 x 1 to 1 x 9:

    TRANSPOSE({1,1,1,1,1,1,1}) // returns {1,1,1,1,1,1,1,1,1}
    

The result is handed off to the MMULT function as _array1_. The MMULT function then performs matrix multiplication with the two arrays, and returns a subtotal for each row:

    =MMULT({1,1,1,1,1,1,1,1,1},--data)
    

returns the array:

    {59,77,67,68,69,72,67}
    

These values are returned to cell C15, and [spill](https://exceljet.net/glossary/spill)
 into the range C15:I15.

### SEQUENCE alternative

Another way to construct _array1_ inside MMULT is with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 like this:

    =MMULT(SEQUENCE(1,ROWS(data),1,0),--data)
    

This formula works the same way, but _array1_ is created with the SEQUENCE function directly:

    SEQUENCE(1,ROWS(data),1,0)
    

Note we use the [ROWS function](https://exceljet.net/functions/rows-function)
 to tell SEQUENCE how many _columns_ to create (7).

Related formulas
----------------

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

Related functions
-----------------

[![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")](https://exceljet.net/functions/bycol-function)

### [BYCOL Function](https://exceljet.net/functions/bycol-function)

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    

### Functions

*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

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
# Get row totals - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-row-totals

---

[Skip to main content](https://exceljet.net/formulas/get-row-totals#main-content)

[](https://exceljet.net/formulas/get-row-totals#)

*   [Previous](https://exceljet.net/formulas/get-column-totals)
    
*   [Next](https://exceljet.net/formulas/groupby-with-monthly-totals)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Get row totals
==============

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[BYROW](https://exceljet.net/functions/byrow-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[MMULT](https://exceljet.net/functions/mmult-function)

[COLUMN](https://exceljet.net/functions/column-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")

Summary
-------

To get an array of row totals based from range of numeric values, you can use a formula based on the [BYROW function](https://exceljet.net/functions/byrow-function)
 together with the [LAMBDA](https://exceljet.net/functions/lambda-function)
 and [SUM](https://exceljet.net/functions/sum-function)
 functions. In the example shown, the formula in K5 is:

    =BYROW(data,LAMBDA(row,SUM(row)))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:I13. The result is an [array](https://exceljet.net/glossary/array)
 with nine sums, one for each row in the range, as seen in column K.

_Note: in older versions of Excel you can use the [MMULT function](https://exceljet.net/functions/mmult-function)
, as explained below._

Generic formula
---------------

    =BYROW(range,LAMBDA(row,SUM(row)))

Explanation 
------------

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in **data** which is the [named range](https://exceljet.net/glossary/named-range)
 C5:I13. This is an example of a problem where the goal is to create an [array](https://exceljet.net/glossary/array)
 of sums rather than a single sum. We can't use a function like [SUM](https://exceljet.net/functions/sum-function)
 by itself, because SUM will _aggregate_ results and return a single value. In the article below, we look at two approaches, one based on the [BYROW function](https://exceljet.net/functions/byrow-function)
, and one based on the [MMULT function](https://exceljet.net/functions/mmult-function)
.

### With the BYROW function

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the most straightforward way to generate subtotals for each row is with the [BYROW function](https://exceljet.net/functions/byrow-function)
. The purpose of BYROW is to process data in a "by row" fashion. For example, if BYROW is given an array with 10 rows, BYROW will return single [array](https://exceljet.net/glossary/array)
 with 10 results. In the example shown, the formula in K5 is:

    =BYROW(data,LAMBDA(row,SUM(row)))
    

The calculation performed on each row is provided by a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
, which must return a single result for each row. In this example, the LAMBDA function used in BYROW sums each row like this:

    LAMBDA(row,SUM(row)) // sum each row
    

The result is an array of sums, one per row, that [spill](https://exceljet.net/glossary/spill)
 into the range K5:K13. This result is fully dynamic. If data values change, or if the data range expands or contracts, the output from BYROW will update as needed. Although this example deals with totals, the same pattern can be used to calculate other information about rows, including max, min, average, etc. like this:

    =BYROW(data,LAMBDA(row,MAX(row))) // max
    =BYROW(data,LAMBDA(row,MIN(row))) // min
    =BYROW(data,LAMBDA(row,AVERAGE(row))) // average
    

### With the MMULT function

Another way to solve this problem is with the [MMULT function](https://exceljet.net/functions/mmult-function)
, which performs matrix multiplication. MMULT takes two arrays, _array1_ and _array2_, and requires that the number of _columns in array1_ be the same as the number of _rows in array2_. The resulting matrix will have same number of rows as the first matrix, and the same number of columns as the second matrix. The MMULT formula looks like this:

    =MMULT(--data,TRANSPOSE(COLUMN(data)^0))
    

The first array is simply all values in **data**, the [named range](https://exceljet.net/glossary/named-range)
 C5:I13:

    =MMULT(--data
    

To protect against blank cells, which will cause MMULT to throw #VALUE! error, we use a [double negative](https://exceljet.net/glossary/double-unary)
 (--) to force any empty cells to zero.

Next, we need to create _array2_. The first array contains 7 columns, so we need the second array to contain 7 rows. We want just a single column of results, so the second array should be 7 rows by 1 column (7 x 1). Also, because we don't want to change any values, the array should contain only the number 1 (i.e. multiplying by 1 does not change the original value). _Array2_ is generated with the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 and the [COLUMN function](https://exceljet.net/functions/column-function)
 like this:

    TRANSPOSE(COLUMN(data)^0)
    

While slightly cryptic, this syntax above is a clever way to accomplish the task. The [COLUMN function](https://exceljet.net/functions/column-function)
 returns a 1 x 7 array of column numbers:

    COLUMN(data) // returns {3,4,5,6,7,8,9}
    

Next, these numbers are raised to the power of zero with [exponent operator](https://exceljet.net/glossary/math-operators)
 (^), which creates a 1 x 7 array of 1s:

    COLUMN(data)^0) // returns {1,1,1,1,1,1,1}
    

And the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 flips the array from 1 x 7 to 7 x 1:

    TRANSPOSE({1,1,1,1,1,1,1}) // returns {1;1;1;1;1;1;1}
    

The result is handed off to the MMULT function as _array2_. The MMULT function then performs matrix multiplication with the two arrays, and returns a subtotal for each row:

    =MMULT(--data,{1;1;1;1;1;1;1})
    

returns the array:

    {51;59;67;56;51;49;52;42;52}
    

These values are returned to cell K5, and [spill](https://exceljet.net/glossary/spill)
 into the range K5:K13.

### SEQUENCE alternative

Another way to construct _array2_ inside MMULT is with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 like this:

    =MMULT(--data,SEQUENCE(COLUMNS(data),1,1,0))
    

This formula works the same way, but _array2_ is created with the SEQUENCE function directly:

    SEQUENCE(COLUMNS(data),1,1,0) // returns {1;1;1;1;1;1;1}
    

Note we use the [COLUMNS function](https://exceljet.net/functions/columns-function)
 to tell SEQUENCE how many rows to create (7).

Related formulas
----------------

[![Excel formula: Get column totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20column%20totals.png "Excel formula: Get column totals")](https://exceljet.net/formulas/get-column-totals)

### [Get column totals](https://exceljet.net/formulas/get-column-totals)

In this example, the goal is to return an array with 7 subtotals, one for each day of the week, as seen in columns C:I. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

Related functions
-----------------

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

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

*   [Get column totals](https://exceljet.net/formulas/get-column-totals)
    
*   [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    

### Functions

*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
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
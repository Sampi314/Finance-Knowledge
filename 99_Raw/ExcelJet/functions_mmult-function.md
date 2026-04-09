# Excel MMULT function | Exceljet

**Source:** https://exceljet.net/functions/mmult-function

---

[Skip to main content](https://exceljet.net/functions/mmult-function#main-content)

[](https://exceljet.net/functions/mmult-function#)

*   [Previous](https://exceljet.net/functions/minverse-function)
    
*   [Next](https://exceljet.net/functions/mod-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

MMULT Function
==============

by Dave Bruns · Updated 21 Aug 2021

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[MUNIT](https://exceljet.net/functions/munit-function)

[MINVERSE](https://exceljet.net/functions/minverse-function)

[MDETERM](https://exceljet.net/functions/mdeterm-function)

![Excel MMULT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")

Summary
-------

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

Purpose 
--------

Perform matrix multiplication

Return value 
-------------

The matrix product of two arrays

Syntax
------

    =MMULT(array1,array2)

*   _array1_ - The first array to multiply.
*   _array2_ - The second array to multiply.

Using the MMULT function 
-------------------------

The MMULT function returns the matrix product of two arrays, sometimes called the "dot product". The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. The MMULT function appears in certain more advanced formulas that need to process multiple rows or columns. For example, you can use MMULT with [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 to [match a value in any column](https://exceljet.net/formulas/xlookup-match-any-column)
.

The MMULT function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _array1_ and _array2_, both of which are required. The column count of _array1_ must equal the row count of _array2_. For example, you can multiply a 2 x 3 array by a 3 x 2 array to return a 2 x 2 array result. The MMULT function will return a #VALUE! error if _array1_ columns do not equal _array2_ rows.

_Note: In [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports [dynamic arrays](https://exceljet.net/glossary/dynamic-array)
, MMULT [spills](https://exceljet.net/glossary/spill)
 multiple values on the worksheet. In earlier versions, you will need to enter as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 with control + shift + enter._

### Example #1 - basic usage

In the example shown, the MMULT formula is evaluated like this:

    =MMULT(B6:D7,F6:G8)
    =MMULT({0,3,5;5,5,2},{3,4;3,-2;4,-2})
    ={29,-16;38,6}
    

### Example #2 - count rows with specific value

In this example, the goal is to count rows that contain the number 90. The challenge is that the value might appear in any of several columns, and might appear in more than one column of the same row. The MMULT function is used to condense results from multiple columns into a single 1-column array that can then be summed with the SUM function. The formula in G5 is:

    =SUM(--(MMULT(--(data=90),TRANSPOSE(COLUMN(data)))>0))
    

![MMULT example - count rows that contain specific value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/mmult%20example%20count%20rows%20with%20a%20value.png?itok=FsIa2OS4 "MMULT example - count rows that contain specific value")

Read a [detailed explanation here](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
. See below for more examples.

### Notes

*   Arrays must contain numbers only.
*   Columns in _array1_ must equal the rows in _array2_.
*   _Array1_ and _array2_ can be provided as cell ranges, array constants, or references.
*   MMULT returns #VALUE! if any cells in _array1_ and _array2_ are not numbers
*   MMULT returns #VALUE! if _array1_ columns do not equal _array2_ rows.

MMULT function examples
-----------------------

[![Excel formula: XLOOKUP match any column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20match%20any%20column.png "Excel formula: XLOOKUP match any column")](https://exceljet.net/formulas/xlookup-match-any-column)

### [XLOOKUP match any column](https://exceljet.net/formulas/xlookup-match-any-column)

In this example, we have a table that contains 6 columns of codes, and each row of codes belongs to a group in column B. The goal is to lookup any code in C5:H15, and return the name of the group the code belongs to. The challenge is that the code may be in any one of the six columns, and...

[![Excel formula: Get column totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20column%20totals.png "Excel formula: Get column totals")](https://exceljet.net/formulas/get-column-totals)

### [Get column totals](https://exceljet.net/formulas/get-column-totals)

In this example, the goal is to return an array with 7 subtotals, one for each day of the week, as seen in columns C:I. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We...

[![Excel formula: Sort and extract unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20and%20extract%20unique%20values.png "Excel formula: Sort and extract unique values")](https://exceljet.net/formulas/sort-and-extract-unique-values)

### [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)

Note: the core idea of this formula is adapted from an example in Mike Girvin's excellent book Control+Shift+Enter . The example shown uses several formulas, which are described below. At a high level, the MMULT function is used to compute a numeric rank in a helper column (column C), and this rank...

[![Excel formula: Count rows with at least n matching values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20at%20least%20n%20matching%20values3.png "Excel formula: Count rows with at least n matching values")](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)

### [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)

Working from the inside out, the logical criteria used in this formula is: (data)<70 where data is the named range C5:I14. This generates a TRUE / FALSE result for every value in data , and the double negative coerces the TRUE FALSE values to 1 and 0 to yield an array like this: {0,0,0,1,0,1,0;0...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

[![Excel formula: Index and match on multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/index%20and%20match%20on%20multiple%20columns.png "Excel formula: Index and match on multiple columns")](https://exceljet.net/formulas/index-and-match-on-multiple-columns)

### [Index and match on multiple columns](https://exceljet.net/formulas/index-and-match-on-multiple-columns)

Working from the inside out, the logical criteria used in this formula is this expression: --(names=G4) where names is the named range C4:E7. This generates a TRUE / FALSE result for every value in the data, and the double negative coerces the TRUE and FALSE values to 1 and 0 to yield an array like...

[![Excel formula: Count columns that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20columns%20that%20contain%20specific%20values.png "Excel formula: Count columns that contain specific values")](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

### [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

In this example, the goal is to count the number of columns in the data that contain 19 (the value in cell I4). The main challenge in this problem is that the value might appear in any row, and more than once in the same column. If we wanted to simply count the total number of times a value...

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

[![Excel formula: Count cells that do not contain many strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain%20many%20strings.png "Excel formula: Count cells that do not contain many strings")](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

### [Count cells that do not contain many strings](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

The goal in this example is to count cells in a range that do not contain a given number of strings. The cells to evaluate are in the named range data (B5:B14) and the strings to exclude are listed in the named range exclude (D5:D7). If your needs are simple, you can use the COUNTIFS function to...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel MUNIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20munit%20function.png "Excel MUNIT function")](https://exceljet.net/functions/munit-function)

### [MUNIT Function](https://exceljet.net/functions/munit-function)

The Excel MUNIT function returns a _unit matrix_ for a given dimension, **n**, with a size of **n** x **n**. This resulting matrix contains ones on the main diagonal and zeros in every other position.

[![Excel MINVERSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20minverse%20function.png "Excel MINVERSE function")](https://exceljet.net/functions/minverse-function)

### [MINVERSE Function](https://exceljet.net/functions/minverse-function)

The Excel MINVERSE function returns the inverse matrix of a given array. The input array must contain numbers only and be a square matrix, with equal rows and columns. The result is an inverse matrix with the same dimensions as the array provided.

[![Excel MDETERM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mdeterm%20function.png "Excel MDETERM function")](https://exceljet.net/functions/mdeterm-function)

### [MDETERM Function](https://exceljet.net/functions/mdeterm-function)

The Excel MDETERM function returns the matrix determinant of a given array. The input array must contain numbers only and be a square matrix, with equal rows and columns. The result is a number representing the matrix determinant.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)
    
*   [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)
    
*   [XLOOKUP match any column](https://exceljet.net/formulas/xlookup-match-any-column)
    
*   [Index and match on multiple columns](https://exceljet.net/formulas/index-and-match-on-multiple-columns)
    
*   [Get column totals](https://exceljet.net/formulas/get-column-totals)
    
*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    
*   [Count cells that do not contain many strings](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    
*   [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [MUNIT Function](https://exceljet.net/functions/munit-function)
    
*   [MINVERSE Function](https://exceljet.net/functions/minverse-function)
    
*   [MDETERM Function](https://exceljet.net/functions/mdeterm-function)
    

### Links

*   [Microsoft MMULT function documentation](https://support.office.com/en-us/article/mmult-function-40593ed7-a3cd-4b6b-b9a3-e4ad3c7245eb)
    

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
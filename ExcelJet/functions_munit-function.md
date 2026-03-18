# Excel MUNIT function | Exceljet

**Source:** https://exceljet.net/functions/munit-function

---

[Skip to main content](https://exceljet.net/functions/munit-function#main-content)

[](https://exceljet.net/functions/munit-function#)

*   [Previous](https://exceljet.net/functions/multinomial-function)
    
*   [Next](https://exceljet.net/functions/odd-function)
    

Excel 2013

[Math](https://exceljet.net/functions#Math)

MUNIT Function
==============

by Dave Bruns · Updated 15 Sep 2021

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[MINVERSE](https://exceljet.net/functions/minverse-function)

[MDETERM](https://exceljet.net/functions/mdeterm-function)

![Excel MUNIT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20munit%20function.png "Excel MUNIT function")

Summary
-------

The Excel MUNIT function returns a _unit matrix_ for a given dimension, **n**, with a size of **n** x **n**. This resulting matrix contains ones on the main diagonal and zeros in every other position.

Purpose 
--------

Return unit matrix for a given dimension

Return value 
-------------

Unix matrix of size n x n

Syntax
------

    =MUNIT(dimension)

*   _dimension_ - An integer for the size of the unit matrix.

Using the MUNIT function 
-------------------------

The MUNIT function returns a _unit matrix_ for a given dimension, **n**, with a size of **n** x **n**. The unit matrix is also called the identity matrix. The MUNIT function takes just one argument, _dimension_, which should be a positive integer. The resulting matrix contains ones on the main diagonal and zeros in every other position. 

### Examples

The formula in D5 returns a 3 x 3 unit matrix :

    =MUNIT(3) // 3 x 3
    

With 3 given for _dimension,_ the MUNIT function returns a 3 by 3 [array](https://exceljet.net/glossary/array)
 like this:

|     |     |     |
| --- | --- | --- |
| 1   | 0   | 0   |
| 0   | 1   | 0   |
| 0   | 0   | 1   |

The formula in J5 returns a 5 x 5 unit matrix. 

    =MUNIT(5) // 5 x 5
    

With 5 given for _dimension,_ the MUNIT function returns a 5 by 5 array like this:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| 1   | 0   | 0   | 0   | 0   |
| 0   | 1   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   | 0   |
| 0   | 0   | 0   | 1   | 0   |
| 0   | 0   | 0   | 0   | 1   |

### Array syntax

The MUNIT function returns an [array](https://exceljet.net/glossary/array)
 of values. In [Excel 365](https://exceljet.net/glossary/excel-365)
, where [dynamic arrays are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can use the MUNIT function without any special handling – MUNIT will return an array of values that [spill](https://exceljet.net/glossary/spill)
 directly into cells in the worksheet.

In versions of Excel _prior_ to Excel 365, you need to enter MUNIT enter as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 to display results directly on the worksheet. To do this, make a selection of the right size, and enter MUNIT with [control + shift + enter](https://exceljet.net/glossary/cse)
.

### Notes

*   _Dimension_ must be greater than zero.
*   If _dimension_ is zero or less than zero, MUNIT will return the #VALUE error.
*   A _unit matrix_ is also called an [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix)
    .

Related functions
-----------------

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

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

### Functions

*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [MINVERSE Function](https://exceljet.net/functions/minverse-function)
    
*   [MDETERM Function](https://exceljet.net/functions/mdeterm-function)
    

### Links

*   [Microsoft MUNIT function documentation](https://support.office.com/en-us/article/munit-function-c9fe916a-dc26-4105-997d-ba22799853a3)
    

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
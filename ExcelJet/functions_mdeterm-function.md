# Excel MDETERM function | Exceljet

**Source:** https://exceljet.net/functions/mdeterm-function

---

[Skip to main content](https://exceljet.net/functions/mdeterm-function#main-content)

[](https://exceljet.net/functions/mdeterm-function#)

*   [Previous](https://exceljet.net/functions/log10-function)
    
*   [Next](https://exceljet.net/functions/minverse-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

MDETERM Function
================

by Dave Bruns · Updated 21 Aug 2021

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[MUNIT](https://exceljet.net/functions/munit-function)

[MINVERSE](https://exceljet.net/functions/minverse-function)

![Excel MDETERM function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20mdeterm%20function.png "Excel MDETERM function")

Summary
-------

The Excel MDETERM function returns the matrix determinant of a given array. The input array must contain numbers only and be a square matrix, with equal rows and columns. The result is a number representing the matrix determinant.

Purpose 
--------

Get matrix determinant of given array

Return value 
-------------

A number representing the matrix determinant

Syntax
------

    =MDETERM(array)

*   _array_ - A square array of numbers only.

Using the MDETERM function 
---------------------------

The MDETERM function returns the matrix determinant of a given _array_, which must be a square matrix containing numbers only, and no empty values. In mathematics, the matrix determinant is a scalar value (single value) that is a function of the entries in a square matrix. The determinant is a special number that can help characterize some properties of the matrix. For example, if the determinant is zero, the matrix will not have an inverse.

The MDETERM function takes just one argument, _array_, which can be provided as a range or an [array constant](https://exceljet.net/glossary/array-constant)
. _Array_ must be a square matrix with the same numbers of rows and columns.

### Examples

To get the matrix determinant for the 2 x 2 array shown in B7:C8, the formula in E7 is:

    =MDETERM(B7:C8) // returns -1
    

The equivalent formula with an [array constant](https://exceljet.net/glossary/array-constant)
 is:

    =MDETERM({4,3;3,2}) // returns -1
    

To get the matrix determinant for the 3 x 3 array shown in I7:K9, the formula in M7 is:

    =MDETERM(I7:K9) // returns 1
    

The equivalent formula with an array constant is:

    =MDETERM({1,0,5;2,1,6;3,4,0}) // returns 1
    

### Notes

*   The _array_ argument must be a square matrix with an equal number of rows and columns
*   The _array_ argument can be provided as a [range](https://exceljet.net/glossary/range)
     or [array constant](https://exceljet.net/glossary/array-constant)
     like {4,3;3,2}
*   Empty cells or text in _array_ will cause MDETERM to return a #VALUE! error
*   MDETERM returns a #VALUE! if _array_ does not have an equal number of rows and columns

Related functions
-----------------

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

[![Excel MUNIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20munit%20function.png "Excel MUNIT function")](https://exceljet.net/functions/munit-function)

### [MUNIT Function](https://exceljet.net/functions/munit-function)

The Excel MUNIT function returns a _unit matrix_ for a given dimension, **n**, with a size of **n** x **n**. This resulting matrix contains ones on the main diagonal and zeros in every other position.

[![Excel MINVERSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20minverse%20function.png "Excel MINVERSE function")](https://exceljet.net/functions/minverse-function)

### [MINVERSE Function](https://exceljet.net/functions/minverse-function)

The Excel MINVERSE function returns the inverse matrix of a given array. The input array must contain numbers only and be a square matrix, with equal rows and columns. The result is an inverse matrix with the same dimensions as the array provided.

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
    
*   [MUNIT Function](https://exceljet.net/functions/munit-function)
    
*   [MINVERSE Function](https://exceljet.net/functions/minverse-function)
    

### Links

*   [Microsoft MDETERM function documentation](https://support.office.com/en-us/article/mdeterm-function-e7bfa857-3834-422b-b871-0ffd03717020)
    

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
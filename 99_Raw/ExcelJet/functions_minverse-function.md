# Excel MINVERSE function | Exceljet

**Source:** https://exceljet.net/functions/minverse-function

---

[Skip to main content](https://exceljet.net/functions/minverse-function#main-content)

[](https://exceljet.net/functions/minverse-function#)

*   [Previous](https://exceljet.net/functions/mdeterm-function)
    
*   [Next](https://exceljet.net/functions/mmult-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

MINVERSE Function
=================

by Dave Bruns · Updated 15 Sep 2021

Related functions 
------------------

[MMULT](https://exceljet.net/functions/mmult-function)

[MUNIT](https://exceljet.net/functions/munit-function)

[MDETERM](https://exceljet.net/functions/mdeterm-function)

![Excel MINVERSE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20minverse%20function.png "Excel MINVERSE function")

Summary
-------

The Excel MINVERSE function returns the inverse matrix of a given array. The input array must contain numbers only and be a square matrix, with equal rows and columns. The result is an inverse matrix with the same dimensions as the array provided.

Purpose 
--------

Get inverse matrix of array

Return value 
-------------

Inverse matrix of array with same dimensions

Syntax
------

    =MINVERSE(array)

*   _array_ - A square array of numbers only.

Using the MINVERSE function 
----------------------------

The MINVERSE function returns the _inverse matrix_ of a given array. The product of a matrix and its inverse is the _identity matrix_, a n × n square matrix with ones on the main diagonal and zeros in every other position. 

The MINVERSE function takes just one argument, _array_, which should be a square matrix, with an equal number of rows and columns. In order for MINVERSE to calculate an inverse matrix, _array_ must contain numbers only. When an inverse exists, MINVERSE returns an inverse matrix with the same dimensions as the _array_ provided.

If a matrix cannot be inverted, MINVERSE will return a #NUM! error. A matrix that can't be inverted has a [determinant](https://exceljet.net/functions/mdeterm-function)
 of zero (0).

### Examples

In the example shown the formula used in E7 to calculate the inverse matrix of the 2 x 2 matrix in the range B7:C8 is:

    =MINVERSE(B7:C8) // returns {-2,3;3,-4}
    

The result is the 2 x 2 matrix seen in E7:F8, which can also be expressed as the [array](https://exceljet.net/glossary/array)
 {-2,3;3,-4}.

The formula in M7 calculates the inverse matrix of the 3 x 3 matrix in B7:C8:

    =MINVERSE(I7:K9) // returns {-24,20,-5;18,-15,4;5,-4,1}
    

The result is the 3 x 3 matrix seen in M7:O9, which can be expressed as the [array](https://exceljet.net/glossary/array)
 {-24,20,-5;18,-15,4;5,-4,1}.

### Array syntax

The MINVERSE function returns an [array](https://exceljet.net/glossary/array)
 of values. In [Excel 365](https://exceljet.net/glossary/excel-365)
, where [dynamic arrays are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can use the MINVERSE function without any special handling – MINVERSE will return an array of values that [spill](https://exceljet.net/glossary/spill)
 directly into cells in the worksheet.

In versions of Excel _prior_ to Excel 365, you need to enter MINVERSE enter as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 to display results directly on the worksheet. To do this, make a selection of the right size, and enter MINVERSE with [control + shift + enter](https://exceljet.net/glossary/cse)
.

### Notes

*   The input array must be a square matrix with an equal number of rows and columns
*   The array argument can be provided as a range or [array constant](https://exceljet.net/glossary/array-constant)
     like {4,3;3,2}
*   Empty cells in the source array will cause MINVERSE to return the #VALUE! error
*   MINVERSE returns the #VALUE! error value if array does not have an equal number of rows and columns.
*   If a matrix cannot be inverted, MINVERSE will return a #NUM! error. 

Related functions
-----------------

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

[![Excel MUNIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20munit%20function.png "Excel MUNIT function")](https://exceljet.net/functions/munit-function)

### [MUNIT Function](https://exceljet.net/functions/munit-function)

The Excel MUNIT function returns a _unit matrix_ for a given dimension, **n**, with a size of **n** x **n**. This resulting matrix contains ones on the main diagonal and zeros in every other position.

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
    
*   [MUNIT Function](https://exceljet.net/functions/munit-function)
    
*   [MDETERM Function](https://exceljet.net/functions/mdeterm-function)
    

### Links

*   [Microsoft MINVERSE function documentation](https://support.office.com/en-us/article/minverse-function-11f55086-adde-4c9f-8eb9-59da2d72efc6)
    

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
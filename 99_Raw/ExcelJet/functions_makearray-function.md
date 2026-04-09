# Excel MAKEARRAY function | Exceljet

**Source:** https://exceljet.net/functions/makearray-function

---

[Skip to main content](https://exceljet.net/functions/makearray-function#main-content)

[](https://exceljet.net/functions/makearray-function#)

*   [Previous](https://exceljet.net/functions/let-function)
    
*   [Next](https://exceljet.net/functions/map-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

MAKEARRAY Function
==================

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[MAP](https://exceljet.net/functions/map-function)

[SCAN](https://exceljet.net/functions/scan-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

[MAKEARRAY](https://exceljet.net/functions/makearray-function)

[BYCOL](https://exceljet.net/functions/bycol-function)

[BYROW](https://exceljet.net/functions/byrow-function)

![Excel MAKEARRAY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20makearray%20function.png "Excel MAKEARRAY function")

Summary
-------

The Excel MAKEARRAY function returns an array with specified rows and columns, based on a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. MAKEARRAY can be used to create arrays with variable dimensions based on a calculation.

Purpose 
--------

Create array with calculated values

Return value 
-------------

An array of calculated values

Syntax
------

    =MAKEARRAY(rows,columns,function)

*   _rows_ - The number of rows to create.
*   _columns_ - The number of columns to create.
*   _function_ - The custom LAMBDA calculation to apply.

Using the MAKEARRAY function 
-----------------------------

The MAKEARRAY function returns an [array](https://exceljet.net/glossary/array)
 with specified rows and columns, based on a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. MAKEARRAY can be used to create arrays with variable dimensions that are calculated. The generic syntax for MAKEARRAY looks like this:

    =MAKEARRAY(rows,columns,function)

The MAKEARRAY function takes three arguments: _rows_, _columns_, and _function_. _Rows_ is the number of rows to create, and _columns_ is the number of columns to create. The _function_ is a custom LAMBDA (see below) to use when creating values in the array. The total number of values in the array returned by MAKEARRAY will equal rows \* columns. 

### LAMBDA structure

The MAKEARRAY uses the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to apply the function used to calculate array values. The structure of the LAMBDA used by MAKEARRAY is:

    LAMBDA(r,c,calculation)
    

where _r_ represents the row count, _c_ represents the column count originally passed into MAKEARRAY, and _calculation_ is the formula needed to create the values in the final array.

_Note: to generate an array with sequential values, see the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
._

### Examples

In the formula below, MAKEARRAY is used to create an array with 2 rows and 3 columns, populated with the result multiplying rows by columns:

    =MAKEARRAY(2,3,LAMBDA(r,c,r*c)) // returns {1,2,3;2,4,6}
    

The result is a 2 x 3 [array](https://exceljet.net/glossary/array)
 with six values {1,2,3;2,4,6}. The _calculation_ can be a hardcoded value as well. Below are examples of the same formula, with _calculation_ hardcoded as zero and "x", respectively:

    =MAKEARRAY(2,3,LAMBDA(r,c,0)) // returns {0,0,0;0,0,0}
    =MAKEARRAY(2,3,LAMBDA(r,c,"x")) // returns {"x","x","x";"x","x","x"}
    

### Random values

MAKEARRAY can be used to generate random values. In the formula below. The [CHAR function](https://exceljet.net/functions/char-function)
 is used with the [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
 to generate random uppercase letters A-Z: 

    =MAKEARRAY(2,3,LAMBDA(r,c,CHAR(RANDBETWEEN(65,90))))
    

The result is a 2 x 3 array like {"D","Q","F";"V","C","T"}.

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel MAKEARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20makearray%20function.png "Excel MAKEARRAY function")](https://exceljet.net/functions/makearray-function)

### [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)

The Excel MAKEARRAY function returns an array with specified rows and columns, based on a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. MAKEARRAY can be used to create arrays with variable dimensions based on a calculation....

[![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")](https://exceljet.net/functions/bycol-function)

### [BYCOL Function](https://exceljet.net/functions/bycol-function)

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)
    
*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Links

*   [Microsoft MAKEARRAY function documentation](https://support.microsoft.com/en-us/office/makearray-function-b80da5ad-b338-4149-a523-5b221da09097)
    

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
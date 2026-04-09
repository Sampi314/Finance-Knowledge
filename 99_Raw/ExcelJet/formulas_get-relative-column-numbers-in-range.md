# Get relative column numbers in range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-relative-column-numbers-in-range

---

[Skip to main content](https://exceljet.net/formulas/get-relative-column-numbers-in-range#main-content)

[](https://exceljet.net/formulas/get-relative-column-numbers-in-range#)

*   [Previous](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    
*   [Next](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    

[Range](https://exceljet.net/formulas#Range)

Get relative column numbers in range
====================================

by Dave Bruns · Updated 30 Jan 2021

Related functions 
------------------

[COLUMN](https://exceljet.net/functions/column-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

![Excel formula: Get relative column numbers in range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20relative%20column%20numbers%20in%20range.png "Excel formula: Get relative column numbers in range")

Summary
-------

To get a full set of relative column numbers in a range, you can use an array formula based on the COLUMN function.

In the example shown, the array formula in B4:H4 is:

    {=COLUMN(B4:H4)-COLUMN(B4)+1}
    

On the worksheet, this must be entered as multi-cell array formula using Control + Shift + Enter

This is a robust formula that will continue to generate relative numbers even when columns are inserted in front of the range.

Generic formula
---------------

    {=COLUMN(range)-COLUMN(range.firstcell)+1}

Explanation 
------------

The first COLUMN function generates an array of 7 numbers like this:

    {2,3,4,5,6,7,8}
    

The second COLUMN function generates an array with just one item like this:

    {2}
    

which is then subtracted from the first array to yield:

    {0,1,2,3,4,5,6}
    

Finally, 1 is added to get:

    {1,2,3,4,5,6,7}
    

### With a named range

You can adapt this formula to use with a named range. For example, in the above example, if you created a named range "data" for B4:H4, you can use this formula to generate column numbers:

    {=COLUMN(data)-COLUMN(INDEX(data,1,1))+1}
    

You'll encounter this formula in other array formulas that need to process data column-by-column.

### With SEQUENCE

With the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 the formula to return relative row columns for a range is simple:

    =SEQUENCE(COLUMNS(range))
    

The [COLUMNS function](https://exceljet.net/functions/columns-function)
 provides the count of columns, which is returned to the SEQUENCE function. SEQUENCE then builds an array of numbers, starting with the number 1.  So, following the original example above, the formula below returns the same result:

    =SEQUENCE(COLUMNS(B4:H4)) // returns {1;2;3;4;5;6;7}
    

_Note: the SEQUENCE formula is a new [dynamic array function](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 available only in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Related formulas
----------------

[![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")](https://exceljet.net/formulas/last-row-number-in-range)

### [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range: {5;6;7;8;9;10} To get the first row number in a range, we use the MIN...

[![Excel formula: First column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20column%20in%20range.png "Excel formula: First column number in range")](https://exceljet.net/formulas/first-column-number-in-range)

### [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. In the example shown the array looks like this...

[![Excel formula: Last column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20column%20in%20range.png "Excel formula: Last column number in range")](https://exceljet.net/formulas/last-column-number-in-range)

### [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. If you want only the first column number, you...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

Related functions
-----------------

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)
    
*   [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)
    
*   [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    

### Functions

*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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
# Last column number in range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-column-number-in-range

---

[Skip to main content](https://exceljet.net/formulas/last-column-number-in-range#main-content)

[](https://exceljet.net/formulas/last-column-number-in-range#)

*   [Previous](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [Next](https://exceljet.net/formulas/last-n-rows)
    

[Range](https://exceljet.net/formulas#Range)

Last column number in range
===========================

by Dave Bruns · Updated 15 Aug 2020

Related functions 
------------------

[COLUMN](https://exceljet.net/functions/column-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Last column number in range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/last%20column%20in%20range.png "Excel formula: Last column number in range")

Summary
-------

To get the last column in a range, you can use a formula based on the [COLUMN](https://exceljet.net/functions/column-function)
 and [COLUMNS](https://exceljet.net/functions/columns-function)
 functions. In the example shown, the formula in cell F5 is:

    =MIN(COLUMN(data))+COLUMNS(data)-1
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:D10.

Generic formula
---------------

    =MIN(COLUMN(rng))+COLUMNS(rng)-1

Explanation 
------------

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range.

If you want only the first column number, you can use the MIN function to extract just the first column number, which will be the lowest number in the array:

    =MIN(COLUMN(data)) // first column
    

Once we have the first column, we can add the total columns in the range and subtract 1 to get the last column number.

### Index version

Instead of MIN, you can also use INDEX to get the last row number:

    =COLUMN(INDEX(data,1,1))+COLUMNS(data)-1
    

This is possibly a bit faster for large ranges, since INDEX just supplies a single cell to COLUMN.

### Simple version

When a formula returns an array result, Excel will display the first item in the array if the formula is entered in a single cell. This means that in practice, you can sometimes use a simplified version of the formula:

    =COLUMN(data)+COLUMNS(data)-1
    

But be aware that this will return an [array](https://exceljet.net/glossary/array)
 for a multi-column range.

Inside formulas, it's sometimes necessary to make sure you are dealing with only one item, and not an array. In that case, you'll want to use the full version above.

Related formulas
----------------

[![Excel formula: First column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20column%20in%20range.png "Excel formula: First column number in range")](https://exceljet.net/formulas/first-column-number-in-range)

### [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. In the example shown the array looks like this...

[![Excel formula: Total columns in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20columns%20in%20range.png "Excel formula: Total columns in range")](https://exceljet.net/formulas/total-columns-in-range)

### [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)

The COLUMNS function is fully automatic. When you provide a range to COLUMNS, it will return a count of all columns in the range. In the example, the formula in F6 returns 2, because there are 2 columns in the range B5:C10: =COLUMNS(B5:C10) // count columns COLUMNS counts the number of columns in...

[![Excel formula: First row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20row%20in%20range.png "Excel formula: First row number in range")](https://exceljet.net/formulas/first-row-number-in-range)

### [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range that contains multiple rows, the ROW function will return an array that contains all row numbers for the range. In the example shown the array looks like this: {5;6;7;8;9;10}...

[![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")](https://exceljet.net/formulas/last-row-number-in-range)

### [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range: {5;6;7;8;9;10} To get the first row number in a range, we use the MIN...

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

Related functions
-----------------

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)
    
*   [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)
    
*   [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)
    
*   [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)
    
*   [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)
    

### Functions

*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

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
# Address of last cell in range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/address-of-last-cell-in-range

---

[Skip to main content](https://exceljet.net/formulas/address-of-last-cell-in-range#main-content)

[](https://exceljet.net/formulas/address-of-last-cell-in-range#)

*   [Previous](https://exceljet.net/formulas/address-of-first-cell-in-range)
    
*   [Next](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    

[Range](https://exceljet.net/formulas#Range)

Address of last cell in range
=============================

by Dave Bruns · Updated 22 Aug 2021

Related functions 
------------------

[ADDRESS](https://exceljet.net/functions/address-function)

[ROW](https://exceljet.net/functions/row-function)

[COLUMN](https://exceljet.net/functions/column-function)

[ROWS](https://exceljet.net/functions/rows-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")

Summary
-------

To get the address of the last cell in a range, you can use the ADDRESS function together with ROW, COLUMN, and MAX functions. In the example shown, the formula in F5 is:

    =ADDRESS(MAX(ROW(data)),MAX(COLUMN(data)))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:D14.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
, where [dynamic array formulas are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
._

Generic formula
---------------

    =ADDRESS(MAX(ROW(rng)),MAX(COLUMN(rng)))

Explanation 
------------

The [ADDRESS function](https://exceljet.net/functions/address-function)
 creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the [named range](https://exceljet.net/glossary/named-range)
 **data** (B5:D14).

To get the last row used, we use the [ROW function](https://exceljet.net/functions/row-function)
 together with the [MAX function](https://exceljet.net/functions/max-function)
 like this:

    MAX(ROW(data))
    

Because **data** contains more than one row, ROW returns an [array](https://exceljet.net/glossary/array)
 of row numbers:

    {5;6;7;8;9;10;11;12;13;14}
    

This array goes directly to the MAX function, which returns the largest number:

    MAX({5;6;7;8;9;10;11;12;13;14}) // returns 14
    

To get the last column, we use the [COLUMN function](https://exceljet.net/functions/column-function)
 in the same way:

    MAX(COLUMN(data))
    

Since **data** contains three rows, COLUMN returns an array with three column numbers:

    {2,3,4}
    

and the MAX function again returns the largest number:

    MAX({2,3,4}) // returns 4
    

Both results are returned directly to the ADDRESS function, which constructs a reference to the cell at row 14, column 4:

    =ADDRESS(14,4) // returns $D$14
    

If you want a [relative address](https://exceljet.net/glossary/relative-reference)
 instead of an [absolute reference](https://exceljet.net/glossary/absolute-reference)
, you can supply 4 for the third argument like this:

    =ADDRESS(MAX(ROW(data)),MAX(COLUMN(data)),4) // returns D14
    

### CELL function alternative

Although it's not obvious, the [INDEX function](https://exceljet.net/functions/index-function)
 returns a reference, so we can use the [CELL function](https://exceljet.net/functions/cell-function)
 with INDEX to get the address of the last cell in a range like this:

    =CELL("address",INDEX(data,ROWS(data),COLUMNS(data)))
    

In this case, we use the INDEX function to get a reference to the last cell in the range, which we determine by passing total rows and total columns for the range **data** into INDEX. We get total rows with the [ROWS function](https://exceljet.net/functions/rows-function)
, and total columns with the [COLUMNS function](https://exceljet.net/functions/columns-function)
:

    ROWS(data) // returns 10
    COLUMNS(data) // returns 3
    

With the array provided as data, INDEX then returns a reference to cell D14:

    INDEX(data,10,3) // returns reference to D14
    

We then use the CELL function with "address", to display the address.

_Note: The CELL function is a [volatile function](https://exceljet.net/glossary/volatile-function)
 which can cause performance problems in large or complex workbooks._

Related formulas
----------------

[![Excel formula: Address of first cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20first%20cell%20in%20range.png "Excel formula: Address of first cell in range")](https://exceljet.net/formulas/address-of-first-cell-in-range)

### [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)

The ADDRESS function creates a reference based on a given row and column number. In this case, we want to get the first row and the first column used by the named range data (B5:D14). To get the first row used, we use the ROW function together with the MIN function like this: MIN(ROW(data)) Because...

[![Excel formula: Total rows in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20rows%20in%20range.png "Excel formula: Total rows in range")](https://exceljet.net/formulas/total-rows-in-range)

### [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)

The ROWS function is fully automatic. When you provide a range to ROWS, it will return a count of all rows in the range. In the example, the formula in F5 returns 6, because there are 6 rows in the range B5:C10: =ROWS(B5:C10) // count rows ROWS counts the number of rows in any supplied range and...

[![Excel formula: Total columns in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20columns%20in%20range.png "Excel formula: Total columns in range")](https://exceljet.net/formulas/total-columns-in-range)

### [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)

The COLUMNS function is fully automatic. When you provide a range to COLUMNS, it will return a count of all columns in the range. In the example, the formula in F6 returns 2, because there are 2 columns in the range B5:C10: =COLUMNS(B5:C10) // count columns COLUMNS counts the number of columns in...

[![Excel formula: Count cells in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_cells_in_range.png "Excel formula: Count cells in range")](https://exceljet.net/formulas/count-cells-in-range)

### [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)

The goal is to count the number of cells in a given range, regardless of whether the cells are empty or not. Although Excel has several functions designed to count cells based on their contents, there is no built-in function for counting the total number of cells in a range. The classic solution is...

[![Excel formula: Get address of named range or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_named_range_or_table.png "Excel formula: Get address of named range or table")](https://exceljet.net/formulas/get-address-of-named-range-or-table)

### [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)

The goal is to return the full address of a range or named range as text. The purpose of this formula is informational, not functional. It provides a way to inspect the current range for a named range, an Excel Table, or even the result of a formula. The core of the solutions explained below is the...

Related functions
-----------------

[![Excel ADDRESS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20address%20function.png "Excel ADDRESS function")](https://exceljet.net/functions/address-function)

### [ADDRESS Function](https://exceljet.net/functions/address-function)

The Excel ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return an address in relative, mixed, or absolute format, and can be used to construct a cell reference inside a formula.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

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

*   [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)
    
*   [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)
    
*   [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)
    
*   [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)
    
*   [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    

### Functions

*   [ADDRESS Function](https://exceljet.net/functions/address-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    

### Articles

*   [Named Ranges in Excel](https://exceljet.net/articles/named-ranges)
    

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
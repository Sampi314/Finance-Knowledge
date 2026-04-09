# Excel ADDRESS function | Exceljet

**Source:** https://exceljet.net/functions/address-function

---

[Skip to main content](https://exceljet.net/functions/address-function#main-content)

[](https://exceljet.net/functions/address-function#)

*   [Previous](https://exceljet.net/functions/yearfrac-function)
    
*   [Next](https://exceljet.net/functions/areas-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

ADDRESS Function
================

by Dave Bruns · Updated 28 Feb 2023

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

[INFO](https://exceljet.net/functions/info-function)

![Excel ADDRESS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20address%20function.png "Excel ADDRESS function")

Summary
-------

The Excel ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return an address in relative, mixed, or absolute format, and can be used to construct a cell reference inside a formula.

Purpose 
--------

Create a cell address from a row and column number

Return value 
-------------

A cell address in the current or given worksheet.

Syntax
------

    =ADDRESS(row_num,col_num,[abs_num],[a1],[sheet])

*   _row\_num_ - The row number to use in the cell address.
*   _col\_num_ - The column number to use in the cell address.
*   _abs\_num_ - \[optional\] The address type (i.e. absolute, relative). Defaults to absolute.
*   _a1_ - \[optional\] The reference style, A1 vs R1C1. Defaults to A1 style.
*   _sheet_ - \[optional\] The name of the worksheet to use. Defaults to current sheet.

Using the ADDRESS function 
---------------------------

The ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return a relative, mixed, or absolute reference, and can be used to construct a cell reference inside a formula. Note that ADDRESS returns a reference as a [text value](https://exceljet.net/glossary/text-value)
. If you want to use this text inside a formula reference, you will need to coerce the text to a proper reference with the [INDIRECT function](https://exceljet.net/functions/indirect-function)
.

_Note: ADDRESS is a special purpose function and is not necessary in most formulas. For example, to retrieve a value at a specific row and column location, you can use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
_.

The ADDRESS function takes five arguments: _row_, _column_, _abs\_num_, _a1_, and _sheet\_text_. _Row_ and _column_ are required, other arguments are optional. The _abs\_num_ argument controls whether the address returned is [relative](https://exceljet.net/glossary/relative-reference)
, [mixed](https://exceljet.net/glossary/mixed-reference)
, or [absolute](https://exceljet.net/glossary/absolute-reference)
, with a default value of 1 for absolute. The _a1_ argument is a Boolean that toggles between A1 and R1C1 style references with a default value of TRUE for A1 style references. Finally, the _sheet\_text_ argument is meant to hold a sheet name that will be prepended to the address.

### ABS options

The table below shows the options available for the _abs\_num_ argument for returning a relative, mixed, or absolute address. 

| abs\_num | Result |
| --- | --- |
| 1 (or omitted) | Absolute ($A$1) |
| 2   | Absolute row, relative column (A$1) |
| 3   | Relative row, absolute column ($A1) |
| 4   | Relative (A1) |

### Examples

Use ADDRESS to create an address from a given row and column number. For example:

    =ADDRESS(1,1) // returns $A$1
    =ADDRESS(1,1,4) // returns A1
    =ADDRESS(100,26,4) // returns Z100
    =ADDRESS(1,1,1,FALSE) // R1C1
    =ADDRESS(1,1,4,TRUE,"Sheet1") // returns Sheet1!A1
    

ADDRESS function examples
-------------------------

[![Excel formula: COUNTIFS with variable range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/countifs%20with%20a%20variable%20range.png "Excel formula: COUNTIFS with variable range")](https://exceljet.net/formulas/countifs-with-variable-range)

### [COUNTIFS with variable range](https://exceljet.net/formulas/countifs-with-variable-range)

In the example shown, the formula in B11 is: =COUNTIFS(OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1),"<>") Working from the inside out, the work of setting up a variable range is done by the OFFSET function here: OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1) // variable range OFFSET has five arguments and is...

[![Excel formula: Get location of value in 2D array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_location_of_value_in_2D_array.png "Excel formula: Get location of value in 2D array")](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

### [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

In this example, the goal is to return a list of the locations for a specific value in a 2D array of values (i.e., a table). The target value is entered in cell N5, and the table being tested is in the range C4:L16. The coordinates are supplied from row 4 and column B, as seen in the worksheet. In...

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

[![Excel formula: Address of first cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20first%20cell%20in%20range.png "Excel formula: Address of first cell in range")](https://exceljet.net/formulas/address-of-first-cell-in-range)

### [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)

The ADDRESS function creates a reference based on a given row and column number. In this case, we want to get the first row and the first column used by the named range data (B5:D14). To get the first row used, we use the ROW function together with the MIN function like this: MIN(ROW(data)) Because...

[![Excel formula: Convert column number to letter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20column%20number%20to%20letter_0.png "Excel formula: Convert column number to letter")](https://exceljet.net/formulas/convert-column-number-to-letter)

### [Convert column number to letter](https://exceljet.net/formulas/convert-column-number-to-letter)

In this example, the goal is to convert an ordinary number into a column reference expressed in letters. For example, the number 1 should return "A", the number 2 should return "B", the number 26 should return "Z", etc. The challenge is that Excel can handle over 16,000 columns, so the number of...

[![Excel formula: Get cell content at given row and column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_cell_content_at_given_row_and_column.png "Excel formula: Get cell content at given row and column")](https://exceljet.net/formulas/get-cell-content-at-given-row-and-column)

### [Get cell content at given row and column](https://exceljet.net/formulas/get-cell-content-at-given-row-and-column)

The goal is to retrieve the value of a cell at a given row and column location, which are entered in cells G5 and G4, respectively. There are several ways to go about this, depending on your needs. See below for options. ADDRESS and INDIRECT In the example worksheet, the ADDRESS function is...

[![Excel formula: Get address of named range or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_named_range_or_table.png "Excel formula: Get address of named range or table")](https://exceljet.net/formulas/get-address-of-named-range-or-table)

### [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)

The goal is to return the full address of a range or named range as text. The purpose of this formula is informational, not functional. It provides a way to inspect the current range for a named range, an Excel Table, or even the result of a formula. The core of the solutions explained below is the...

Related functions
-----------------

[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)

### [CELL Function](https://exceljet.net/functions/cell-function)

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...

[![Excel INFO function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20info%20function.png "Excel INFO function")](https://exceljet.net/functions/info-function)

### [INFO Function](https://exceljet.net/functions/info-function)

The Excel INFO function returns information about the current environment, including platform, Excel version, number of worksheets in a workbook, and so on. To use the INFO function, supply the type of information you want as text. There are seven types of information available, summarized in...

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
    
*   [Convert column number to letter](https://exceljet.net/formulas/convert-column-number-to-letter)
    
*   [COUNTIFS with variable range](https://exceljet.net/formulas/countifs-with-variable-range)
    
*   [Get cell content at given row and column](https://exceljet.net/formulas/get-cell-content-at-given-row-and-column)
    
*   [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    
*   [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)
    
*   [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)
    

### Functions

*   [CELL Function](https://exceljet.net/functions/cell-function)
    
*   [INFO Function](https://exceljet.net/functions/info-function)
    

### Links

*   [Microsoft ADDRESS function documentation](https://support.office.com/en-us/article/address-function-d0c26c0d-3991-446b-8de4-ab46431d4f89)
    

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
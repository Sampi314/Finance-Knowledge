# Excel CELL function | Exceljet

**Source:** https://exceljet.net/functions/cell-function

---

[Skip to main content](https://exceljet.net/functions/cell-function#main-content)

[](https://exceljet.net/functions/cell-function#)

*   [Previous](https://exceljet.net/functions/yieldmat-function)
    
*   [Next](https://exceljet.net/functions/errortype-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

CELL Function
=============

by Dave Bruns · Updated 15 Feb 2023

Related functions 
------------------

[ADDRESS](https://exceljet.net/functions/address-function)

[INFO](https://exceljet.net/functions/info-function)

![Excel CELL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")

Summary
-------

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of information available.

Purpose 
--------

Get information about a cell

Return value 
-------------

A text value

Syntax
------

    =CELL(info_type,[reference])

*   _info\_type_ - The type of information to return about the reference.
*   _reference_ - \[optional\] The reference from which to extract information.

Using the CELL function 
------------------------

Use the CELL function to return a wide range of information about a _reference_. The type of information  returned is given as _info\_type_, which must be enclosed in double quotes (""). CELL can return a cell's address, the filename and path for a workbook, and information about the formatting used in the cell. See below for a full list of [info types](https://exceljet.net/functions/cell-function#info_types)
 and [format codes](https://exceljet.net/functions/cell-function#format_codes)
.

> CELL is a [volatile function](https://exceljet.net/glossary/volatile-function)
> , and can cause performance issues in large or complex worksheets.

The CELL function takes two arguments: _info\_type_ and _reference_. _Info\_type_ is a text string that indicates the type of information requested. See the table below for a full list of info types. _Reference_ is a cell reference. _Reference_ is typically a single cell. If _reference_ refers to more than one cell, CELL returns information about the _first_ cell in reference. For certain kinds of information (like filename) the cell address used for _reference_ is optional and can be omitted. However, if _reference_ is not supplied, CELL will return the name of the current "active sheet" which may or may not be the sheet where the formula exists, and might even be in a different workbook. To avoid confusion, use A1 for _reference._ 

_Note: the CELL function is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and may cause performance issues in large or complex worksheets._

### Examples

For example, to get the column number for C10:

    =CELL("col", C10) // returns 3
    

To get the address of A1 as text:

    =CELL("address",A1) // returns "$A$1"
    

To get the [full path and workbook name](https://exceljet.net/formulas/get-full-workbook-name-and-path)
 for the current worksheet:

    =CELL("filename",A1) // path + filename
    

CELL can also return format code information. For example, if A1 contains the number 100 with the currency number format applied, the CELL function will return "C2":

    =CELL("format",A1) // returns "C2"
    

When requesting the _info\_type_ "format" or "parentheses", a set of empty parentheses "()" is appended to the format returned if the number format uses parentheses for all values or for positive values. For example, if A1 uses the [custom number format](https://exceljet.net/articles/custom-number-formats)
 (0), then:

    =CELL("format",A1) // returns "F0()"
    

### Info types

The following _info\_types_ can be used with the CELL function:

| Info\_type | Description |
| --- | --- |
| address | returns the address of the first cell in _reference_ (as text). |
| col | returns the column number of the first cell in _reference_. |
| color | returns the value 1 if the first cell in _reference_ is formatted using color for negative values; or zero if not. |
| contents | returns the value of the upper-left cell in _reference_. Formulas are not returned. Instead, the result of the formula is returned. |
| filename | returns the file name and full path as text. If the worksheet that contains _reference_ has not yet been saved, an empty string is returned. |
| format | returns a code that corresponds to the number format of the cell. See below for a list of number format codes. If the first cell in _reference_ is formatted with color for values < 0, then "-" is appended to the code. If the cell is formatted with parentheses, returns "() - at the end of the code value. |
| parentheses | returns 1 if the first cell in _reference_ is formatted with parentheses and 0 if not. |
| prefix | returns a text value that corresponds to the _label prefix_ - of the cell:  a single quotation mark (') if the cell text is left-aligned, a double quotation mark (") if the cell text is right-aligned, a caret (^) if the cell text is centered text, a backslash () if the cell text is fill-aligned, and an empty string if the label prefix is anything else. |
| protect | returns 1 if the first cell in _reference_ is locked or 0 if not. |
| row | returns the row number of the first cell in _reference_. |
| type | returns a text value that corresponds to the type of data in the first cell in _reference_:  "b" for blank when the cell is empty, "l"  for label if the cell contains a text constant, and "v" for value if the cell contains anything else. |
| width | returns the column width of the cell, rounded to the nearest integer. A unit of column width is equal to the width of one character in the default font size. Note: this value comes back as an array with two values {width,default} where width is the column width and default is a boolean value that indicates if the width is the default column width. |

### Format codes

The table below shows the text codes returned by CELL when "format" is used for _info\_type_.

| Format code returned | Format code meaning |
| --- | --- |
| G   | General |
| F0  | 0   |
| ,0  | #,##0 |
| F2  | 0   |
| ,2  | #,##0.00 |
| C0  | $#,##0\_);($#,##0) |
| C0- | $#,##0\_);\[Red\]($#,##0) |
| C2  | $#,##0.00\_);($#,##0.00) |
| C2- | $#,##0.00\_);\[Red\]($#,##0.00) |
| P0  | 0%  |
| P2  | 0.00% |
| S2  | 0.00E+00 |
| G   | \# ?/? or # ??/?? |
| D1  | d-mmm-yy or dd-mmm-yy |
| D2  | d-mmm or dd-mmm |
| D3  | mmm-yy |
| D4  | m/d/yy or m/d/yy h:mm or mm/dd/yy |
| D5  | mm/dd |
| D6  | h:mm:ss AM/PM |
| D7  | h:mm AM/PM |
| D8  | h:mm:ss |

### Notes

*   The CELL function is a [volatile function](https://exceljet.net/glossary/volatile-function)
     and may cause performance issues in large or complex worksheets.
*   _Reference_ is optional for some info types, but use an address like A1 to avoid unexpected behavior.

CELL function examples
----------------------

[![Excel formula: Hyperlink to first match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hyperlink%20to%20first%20match.png "Excel formula: Hyperlink to first match")](https://exceljet.net/formulas/hyperlink-to-first-match)

### [Hyperlink to first match](https://exceljet.net/formulas/hyperlink-to-first-match)

Working from the inside out, we use a standard INDEX and MATCH function to locate the first match of lookup values in column B: INDEX(data,MATCH(B5,data,0)) The MATCH function gets the position of the value in B5 inside the named range data, which for the lookup value "blue" is 3. This result goes...

[![Excel formula: Count visible columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20visible%20columns.png "Excel formula: Count visible columns")](https://exceljet.net/formulas/count-visible-columns)

### [Count visible columns](https://exceljet.net/formulas/count-visible-columns)

There is no direct way to detect a hidden column with a formula in Excel. You might think of using the SUBTOTAL function , but SUBTOTAL only works with vertical ranges. As a result, the approach described in this example is a workaround based on a helper formula that must be entered in a range that...

[![Excel formula: Address of first cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20first%20cell%20in%20range.png "Excel formula: Address of first cell in range")](https://exceljet.net/formulas/address-of-first-cell-in-range)

### [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)

The ADDRESS function creates a reference based on a given row and column number. In this case, we want to get the first row and the first column used by the named range data (B5:D14). To get the first row used, we use the ROW function together with the MIN function like this: MIN(ROW(data)) Because...

[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)

### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...

[![Excel formula: Get workbook name and path without sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_name_and_path_without_sheet.png "Excel formula: Get workbook name and path without sheet")](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

### [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

In this example, the goal is to get a normal path to the current workbook, without a sheet name, and without the square brackets ("\[ \]") that normally enclose the workbook name. This is a pretty simple problem in the latest version of Excel, which provides the TEXTBEFORE function . In older...

[![Excel formula: Get full workbook name and path](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workbook%20name%20and%20path_0.png "Excel formula: Get full workbook name and path")](https://exceljet.net/formulas/get-full-workbook-name-and-path)

### [Get full workbook name and path](https://exceljet.net/formulas/get-full-workbook-name-and-path)

The CELL function can return various information about a worksheet. CELL can get things like address and filename, as well as information about the formatting used in the cell. The type of information to be returned is specified by the info\_type argument . In this example, we want the path, name,...

[![Excel formula: Increment cell reference with INDIRECT](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/increment%20cell%20reference%20with%20INDIRECT.png "Excel formula: Increment cell reference with INDIRECT")](https://exceljet.net/formulas/increment-cell-reference-with-indirect)

### [Increment cell reference with INDIRECT](https://exceljet.net/formulas/increment-cell-reference-with-indirect)

Consider a simple dynamic reference to Sheet2 using the INDIRECT in a formula like this: =INDIRECT($B$5&"!"&"A1") If we change the sheet name in B5 to another (valid) name, INDIRECT will return a reference to A1 in the new sheet. However, if we copy this formula down the column, the...

[![Excel formula: Get workbook name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_workbook_name_only.png "Excel formula: Get workbook name only")](https://exceljet.net/formulas/get-workbook-name-only)

### [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)

In this example, the goal is to return the name of the current workbook with a formula. This is a fairly simple problem in the latest version of Excel, which provides the TEXTAFTER function and the TEXTBEFORE function . In older versions of Excel, you can use a more complicated formula based on the...

[![Excel formula: Hyperlink to first blank cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Hyperlink%20to%20first%20blank%20cell.png "Excel formula: Hyperlink to first blank cell")](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)

### [Hyperlink to first blank cell](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)

Working from the inside out, we use MATCH to locate the relative position of the last entry in column C: MATCH(9.99E+307,C5:C100) Basically, we are giving MATCH a "big number" it will never find in approximate match mode. In this mode, MATCH will "step back" to the last numeric value. Note: this...

[![Excel formula: Link to multiple sheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/link%20to%20multiple%20sheets.png "Excel formula: Link to multiple sheets")](https://exceljet.net/formulas/link-to-multiple-sheets)

### [Link to multiple sheets](https://exceljet.net/formulas/link-to-multiple-sheets)

This formula relies on concatenation to assemble a valid location for the HYPERLINK function. In cell D5, the link location argument is created like this: "#"...

[![Excel formula: Highlight unprotected cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20unprotected%20cells.png "Excel formula: Highlight unprotected cells")](https://exceljet.net/formulas/highlight-unprotected-cells)

### [Highlight unprotected cells](https://exceljet.net/formulas/highlight-unprotected-cells)

The CELL function can provide a wide range of information about cell properties. One property is called "protect" and indicates whether a cell is unlocked or locked. All cells start out "locked" in a new Excel workbook, but this setting has no effect until a worksheet is protected. The CELL...

[![Excel formula: Get address of lookup result](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_lookup_result.png "Excel formula: Get address of lookup result")](https://exceljet.net/formulas/get-address-of-lookup-result)

### [Get address of lookup result](https://exceljet.net/formulas/get-address-of-lookup-result)

There are certain functions in Excel that return a cell reference as a result rather than a value. Two of these functions are XLOOKUP and INDEX . The presence of the cell reference in the result is not obvious, because Excel immediately resolves the reference to the value in that cell. You can...

[![Excel formula: Get workbook path only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_path_only.png "Excel formula: Get workbook path only")](https://exceljet.net/formulas/get-workbook-path-only)

### [Get workbook path only](https://exceljet.net/formulas/get-workbook-path-only)

In this example, the goal is to get the workbook path without the workbook name . For example, given a workbook called fruits.xlsx saved to: C:\\examples\\fruits.xlsx We want the path only like this: C:\\examples\\ TEXTBEFORE solution In a modern version of Excel (Excel 2021 or later) the simplest way...

Related functions
-----------------

[![Excel ADDRESS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20address%20function.png "Excel ADDRESS function")](https://exceljet.net/functions/address-function)

### [ADDRESS Function](https://exceljet.net/functions/address-function)

The Excel ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return an address in relative, mixed, or absolute format, and can be used to construct a cell reference inside a formula.

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

*   [Get full workbook name and path](https://exceljet.net/formulas/get-full-workbook-name-and-path)
    
*   [Hyperlink to first blank cell](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)
    
*   [Hyperlink to first match](https://exceljet.net/formulas/hyperlink-to-first-match)
    
*   [Link to multiple sheets](https://exceljet.net/formulas/link-to-multiple-sheets)
    
*   [Highlight unprotected cells](https://exceljet.net/formulas/highlight-unprotected-cells)
    
*   [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)
    
*   [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)
    
*   [Get address of lookup result](https://exceljet.net/formulas/get-address-of-lookup-result)
    
*   [Count visible columns](https://exceljet.net/formulas/count-visible-columns)
    
*   [Get workbook path only](https://exceljet.net/formulas/get-workbook-path-only)
    

### Functions

*   [ADDRESS Function](https://exceljet.net/functions/address-function)
    
*   [INFO Function](https://exceljet.net/functions/info-function)
    

### Links

*   [Microsoft CELL function documentation](https://support.office.com/en-us/article/cell-function-51bd39a5-f338-4dbe-a33f-955d67c2b2cf)
    

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
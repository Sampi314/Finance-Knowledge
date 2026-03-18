# Get full workbook name and path - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-full-workbook-name-and-path

---

[Skip to main content](https://exceljet.net/formulas/get-full-workbook-name-and-path#main-content)

[](https://exceljet.net/formulas/get-full-workbook-name-and-path#)

*   [Previous](https://exceljet.net/formulas/dynamic-worksheet-reference)
    
*   [Next](https://exceljet.net/formulas/get-sheet-name-only)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Get full workbook name and path
===============================

by Dave Bruns · Updated 1 Sep 2021

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

![Excel formula: Get full workbook name and path](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20workbook%20name%20and%20path_0.png "Excel formula: Get full workbook name and path")

Summary
-------

To get a full path and name for the current workbook, you can use the [CELL function](https://exceljet.net/functions/cell-function)
 and a reference to any cell in the workbook. In the example shown, the formula is:

    =CELL("filename",A1)
    

You must save the worksheet in order to get the a result.

_Note: the CELL function is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems in larger or more complicated worksheets._ 

Generic formula
---------------

    =CELL("filename",A1)

Explanation 
------------

The [CELL function](https://exceljet.net/functions/cell-function)
 can return various information about a worksheet. CELL can get things like address and filename, as well as information about the formatting used in the cell. The type of information to be returned is specified by the _info\_type_ argument_._ 

In this example, we want the path, name, and sheet for the current workbook. To get this information, the _info\_type_ argument is set to "reference" in a formula like this:

    =CELL("filename",A1)
    

With this configuration, CELL will return the name in this format:

    C:\examples\[workbook.xlsx]Sheet1
    

Note that you must save the worksheet in order to get the a result. 

The second argument, _reference_, is optional and can be any cell in the worksheet. If reference is not supplied, CELL will return the name of the current "active sheet" which may or may not be the sheet where the formula exists, and might even be in a different workbook. To avoid confusion, use A1 for _reference_.

Related formulas
----------------

[![Excel formula: Get workbook name and path without sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_name_and_path_without_sheet.png "Excel formula: Get workbook name and path without sheet")](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

### [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

In this example, the goal is to get a normal path to the current workbook, without a sheet name, and without the square brackets ("\[ \]") that normally enclose the workbook name. This is a pretty simple problem in the latest version of Excel, which provides the TEXTBEFORE function . In older...

[![Excel formula: Get workbook name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_workbook_name_only.png "Excel formula: Get workbook name only")](https://exceljet.net/formulas/get-workbook-name-only)

### [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)

In this example, the goal is to return the name of the current workbook with a formula. This is a fairly simple problem in the latest version of Excel, which provides the TEXTAFTER function and the TEXTBEFORE function . In older versions of Excel, you can use a more complicated formula based on the...

[![Excel formula: Get workbook path only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_path_only.png "Excel formula: Get workbook path only")](https://exceljet.net/formulas/get-workbook-path-only)

### [Get workbook path only](https://exceljet.net/formulas/get-workbook-path-only)

In this example, the goal is to get the workbook path without the workbook name . For example, given a workbook called fruits.xlsx saved to: C:\\examples\\fruits.xlsx We want the path only like this: C:\\examples\\ TEXTBEFORE solution In a modern version of Excel (Excel 2021 or later) the simplest way...

[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)

### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...

[![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")](https://exceljet.net/formulas/dynamic-worksheet-reference)

### [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)

The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using concatenation , and use the resulting text as a valid reference. In this example, we have Sheet names in column B, so we join the sheet name to the...

Related functions
-----------------

[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)

### [CELL Function](https://exceljet.net/functions/cell-function)

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)
    
*   [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)
    
*   [Get workbook path only](https://exceljet.net/formulas/get-workbook-path-only)
    
*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)
    
*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    

### Functions

*   [CELL Function](https://exceljet.net/functions/cell-function)
    

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
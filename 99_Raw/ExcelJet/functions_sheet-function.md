# Excel SHEET function | Exceljet

**Source:** https://exceljet.net/functions/sheet-function

---

[Skip to main content](https://exceljet.net/functions/sheet-function#main-content)

[](https://exceljet.net/functions/sheet-function#)

*   [Previous](https://exceljet.net/functions/na-function)
    
*   [Next](https://exceljet.net/functions/sheets-function)
    

Excel 2013

[Information](https://exceljet.net/functions#Information)

SHEET Function
==============

by Dave Bruns · Updated 8 Sep 2021

Related functions 
------------------

[SHEETS](https://exceljet.net/functions/sheets-function)

![Excel SHEET function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sheet%20function.png "Excel SHEET function")

Summary
-------

The Excel SHEET function returns the index number of a sheet in Excel. SHEET will report the sheet number for a cell reference, named range, or Excel Table.

Purpose 
--------

Get sheet index number

Return value 
-------------

The index number of a given sheet

Syntax
------

    =SHEET([value])

*   _value_ - \[optional\] The value to check.

Using the SHEET function 
-------------------------

The SHEET function returns the index number of a sheet in Excel. You can use the SHEET function to get a numeric index that represents the order of sheets in an Excel workbook, starting with 1 on the left and ending with N on the right, where N is the total number of sheets in the workbook. The SHEET function includes hidden sheets in the numbering sequence.

The SHEET function takes one argument, _value_, which should be a reference, a [named range](https://exceljet.net/glossary/named-range)
, or an [Excel Table](https://exceljet.net/glossary/excel-table)
. _Value_ is optional. When _value_ is omitted, SHEET will return a numeric index for the current sheet (i.e. the sheet the formula exists in).

### Examples

For example, in a workbook with Sheet1, Sheet2, and Sheet3 running left to right:

    =SHEET(Sheet1!A1) // returns 1
    =SHEET(Sheet2!A1) // returns 2
    =SHEET(Sheet3!A1) // returns 3
    

If Sheet2 is dragged all the way to the left, a reference to A1 on Sheet2 will return 1:

    =SHEET(Sheet2!A1) // returns 1
    

SHEET can report the sheet number for a cell reference, named range, or [Excel Table](https://exceljet.net/glossary/excel-table)
. For example, if a table called "Table1" exists on the _third_ sheet in a workbook the SHEET function will return 3:

    =SHEET(Table1) // returns 3
    

### Notes

*   If the _value_ argument is omitted, SHEET will return the index of the current sheet.
*   SHEET includes hidden sheets in the numbering sequence.
*   SHEET reports the _index_ of a sheet. The [SHEETS function](https://exceljet.net/functions/sheets-function)
     reports the _number of sheets_.

SHEET function examples
-----------------------

[![Excel formula: List sheet index numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/List%20sheet%20index%20numbers.png "Excel formula: List sheet index numbers")](https://exceljet.net/formulas/list-sheet-index-numbers)

### [List sheet index numbers](https://exceljet.net/formulas/list-sheet-index-numbers)

The INDIRECT function tries to evaluate text as a valid reference. In this case, the sheet name is pulled from column B and concatenated with an exclamation point and the text A1: =B5...

Related functions
-----------------

[![Excel SHEETS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sheets%20function.png "Excel SHEETS function")](https://exceljet.net/functions/sheets-function)

### [SHEETS Function](https://exceljet.net/functions/sheets-function)

The Excel SHEETS function returns the total number of sheets in a given reference. When no arguments are supplied SHEETS returns the total number of sheets in the workbook.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [List sheet index numbers](https://exceljet.net/formulas/list-sheet-index-numbers)
    

### Functions

*   [SHEETS Function](https://exceljet.net/functions/sheets-function)
    

### Links

*   [Microsoft SHEET function documentation](https://support.office.com/en-us/article/sheet-function-44718b6f-8b87-47a1-a9d6-b701c06cff24)
    

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
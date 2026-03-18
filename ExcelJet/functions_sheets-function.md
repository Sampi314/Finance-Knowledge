# Excel SHEETS function | Exceljet

**Source:** https://exceljet.net/functions/sheets-function

---

[Skip to main content](https://exceljet.net/functions/sheets-function#main-content)

[](https://exceljet.net/functions/sheets-function#)

*   [Previous](https://exceljet.net/functions/sheet-function)
    
*   [Next](https://exceljet.net/functions/t-function)
    

Excel 2013

[Information](https://exceljet.net/functions#Information)

SHEETS Function
===============

by Dave Bruns · Updated 9 Sep 2021

Related functions 
------------------

[SHEET](https://exceljet.net/functions/sheet-function)

![Excel SHEETS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sheets%20function.png "Excel SHEETS function")

Summary
-------

The Excel SHEETS function returns the total number of sheets in a given reference. When no arguments are supplied SHEETS returns the total number of sheets in the workbook.

Purpose 
--------

Get number of sheets in a reference

Return value 
-------------

Sheet count

Syntax
------

    =SHEETS([reference])

*   _reference_ - \[optional\] A valid Excel reference.

Using the SHEETS function 
--------------------------

The SHEETS function returns the total number of sheets in a given reference. SHEETS takes one argument, _reference_, which should be a cell reference, or a [3D reference](https://exceljet.net/videos/how-to-create-3d-references)
. When no references are supplied SHEETS returns the total number of sheets in the workbook. The SHEETS function includes hidden sheets.

### Examples

For example, in a workbook that contains 5 sheets, the following formula will return 5:

    =SHEETS()
    

SHEETS can be used to report the sheet count in 3D references as well. For example, in a workbook with three sheets (Sheet1 through Sheet3) in numeric order, the formulas below return results as shown:

    =SHEETS(Sheet1:Sheet1!A1) // returns 1
    =SHEETS(Sheet1:Sheet2!A1) // returns 2
    =SHEETS(Sheet1:Sheet3!A1) // returns 3
    

### Notes

*   If the _reference_ is omitted, SHEETS returns the total sheets in a workbook.
*   SHEETS includes hidden sheets in the count.
*   SHEETS will report sheet count in 3D references.
*   The [SHEET function](https://exceljet.net/functions/sheet-function)
     returns the _index_ of a sheet. SHEETS returns a count.

Related functions
-----------------

[![Excel SHEET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sheet%20function.png "Excel SHEET function")](https://exceljet.net/functions/sheet-function)

### [SHEET Function](https://exceljet.net/functions/sheet-function)

The Excel SHEET function returns the index number of a sheet in Excel. SHEET will report the sheet number for a cell reference, named range, or Excel Table.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SHEET Function](https://exceljet.net/functions/sheet-function)
    

### Links

*   [Microsoft SHEETS function documentation](https://support.office.com/en-us/article/sheets-function-770515eb-e1e8-45ce-8066-b557e5e4b80b)
    

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
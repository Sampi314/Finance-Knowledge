# List sheet index numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/list-sheet-index-numbers

---

[Skip to main content](https://exceljet.net/formulas/list-sheet-index-numbers#main-content)

[](https://exceljet.net/formulas/list-sheet-index-numbers#)

*   [Previous](https://exceljet.net/formulas/indirect-named-range-different-sheet)
    
*   [Next](https://exceljet.net/formulas/list-sheet-names-with-formula)
    

[Workbook](https://exceljet.net/formulas#Workbook)

List sheet index numbers
========================

by Dave Bruns · Updated 28 Nov 2017

Related functions 
------------------

[SHEET](https://exceljet.net/functions/sheet-function)

![Excel formula: List sheet index numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/List%20sheet%20index%20numbers.png "Excel formula: List sheet index numbers")

Summary
-------

To list the index numbers of sheets in an Excel workbook, you can enter the sheet names, then use a formula based on the SHEET and INDIRECT functions. In the example shown, the formula in C5 is:

    =SHEET(INDIRECT(B5&"!A1"))
    

Generic formula
---------------

    =SHEET(INDIRECT(name&"!A1"))

Explanation 
------------

The INDIRECT function tries to evaluate text as a valid reference. In this case, the sheet name is pulled from column B and concatenated with an exclamation point and the text A1:

    =B5&"!A1"
    ="Sheet1"&"!A1"
    ="Sheet1!A1"
    

The INDIRECT function then coerces the text "Sheet1!A1" into a valid reference, which is passed into the SHEET function.

The SHEET function then returns the current index for each sheet as listed.

Related formulas
----------------

[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)

### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...

[![Excel formula: Worksheet name exists](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/worksheet%20name%20exists.png "Excel formula: Worksheet name exists")](https://exceljet.net/formulas/worksheet-name-exists)

### [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)

The ISREF function returns TRUE for a valid worksheet reference and FALSE is not. In this case, we want to find out of a particular sheet exists in a workbook, so we construct a full reference by concatenating the sheet names in column B with an exclamation mark and "A1": B5...

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

### Formulas

*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)
    
*   [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)
    

### Functions

*   [SHEET Function](https://exceljet.net/functions/sheet-function)
    

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
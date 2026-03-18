# Increment cell reference with INDIRECT - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/increment-cell-reference-with-indirect

---

[Skip to main content](https://exceljet.net/formulas/increment-cell-reference-with-indirect#main-content)

[](https://exceljet.net/formulas/increment-cell-reference-with-indirect#)

*   [Previous](https://exceljet.net/formulas/increment-a-number-in-a-text-string)
    
*   [Next](https://exceljet.net/formulas/leave-a-comment-in-a-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Increment cell reference with INDIRECT
======================================

by Dave Bruns · Updated 1 Dec 2023

Related functions 
------------------

[INDIRECT](https://exceljet.net/functions/indirect-function)

[CELL](https://exceljet.net/functions/cell-function)

![Excel formula: Increment cell reference with INDIRECT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/increment%20cell%20reference%20with%20INDIRECT.png "Excel formula: Increment cell reference with INDIRECT")

Summary
-------

To increment a reference created as text inside the INDIRECT function, you can use the CELL function. In the example shown, the formula in D5 is:

    =INDIRECT($B$5&"!"&CELL("address",A1))
    

Which increments as the formula is copied down.

Generic formula
---------------

    =INDIRECT(sheet&"!"&CELL("address",A1))

Explanation 
------------

Consider a simple dynamic reference to Sheet2 using the INDIRECT in a formula like this:

    =INDIRECT($B$5&"!"&"A1")
    

If we change the sheet name in B5 to another (valid) name, INDIRECT will return a reference to A1 in the new sheet.

However, if we copy this formula down the column, the reference to A1 won't change, because "A1" is hardcoded as text.

To solve this problem, we use the CELL function to generate a text reference from a regular cell reference:

    CELL("address",A1)
    

With "address" as the first argument, and A1 as the second argument, the CELL function returns a string like "$A$1". Because A1 is a regular cell reference, it will increment normally as the formula is copied down the column. The result in D5:D9 is a series of formulas like this:

    =INDIRECT("Sheet2!$A$1")
    =INDIRECT("Sheet2!$A$2")
    =INDIRECT("Sheet2!$A$3")
    =INDIRECT("Sheet2!$A$4")
    =INDIRECT("Sheet2!$A$5")
    

In each case, INDIRECT resolves each text string to a reference and Excel returns the value at the given cell in Sheet2.

_Note: both INDIRECT and CELL are [volatile functions](https://exceljet.net/glossary/volatile-function)
 and recalculate with every worksheet change. This can cause performance problems in more complex worksheets._

Related formulas
----------------

[![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")](https://exceljet.net/formulas/dynamic-worksheet-reference)

### [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)

The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using concatenation , and use the resulting text as a valid reference. In this example, we have Sheet names in column B, so we join the sheet name to the...

Related functions
-----------------

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

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

*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    

### Functions

*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [CELL Function](https://exceljet.net/functions/cell-function)
    

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
# Dynamic worksheet reference - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-worksheet-reference

---

[Skip to main content](https://exceljet.net/formulas/dynamic-worksheet-reference#main-content)

[](https://exceljet.net/formulas/dynamic-worksheet-reference#)

*   [Previous](https://exceljet.net/formulas/dynamic-workbook-reference)
    
*   [Next](https://exceljet.net/formulas/get-full-workbook-name-and-path)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Dynamic worksheet reference
===========================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")

Summary
-------

To create a formula with a dynamic sheet name you can use the [INDIRECT function](https://exceljet.net/functions/indirect-function)
. In the example shown, the formula in C6 is:

    =INDIRECT(B6&"!A1")
    

_Note: The point of INDIRECT here is to build a formula where the sheet name is a dynamic variable. For example, you could change a sheet name (perhaps with a drop-down menu) and pull in information from different worksheet._

Generic formula
---------------

    =INDIRECT(sheet_name&"!A1")

Explanation 
------------

The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using [concatenation](https://exceljet.net/glossary/concatenation)
, and use the resulting text as a valid reference.

In this example, we have Sheet names in column B, so we join the sheet name to the cell reference A1 using concatenation:

    =INDIRECT(B6&"!A1")
    

After concatenation, we have:

    =INDIRECT("Sheet1!A1")
    

INDIRECT recognizes this as a valid reference to cell A1 in Sheet1, and returns the value in A1, 100. In cell C7, the formula evaluates like this:

    =INDIRECT(B7&"!A1")
    =INDIRECT("Sheet2!A1")
    =Sheet2!A1
    =200
    

And so on, for each formula in column C.

### Space and punctuation in sheet names

If sheet names contain spaces or punctuation characters, you'll need to adjust the formula to wrap the sheet name in single quotes (') like this:

    =INDIRECT("'"&sheet_name&"'!A1")
    

where **sheet\_name** is a reference that contains the sheet name. For the example on this page, the formula would be:

    =INDIRECT("'"&B6&"'!A1")
    

Note this requirement is not specific to the INDIRECT function. Any formula that refers to a sheet name with space or punctuation must enclose the sheet name in single quotes.

Related formulas
----------------

[![Excel formula: Lookup with variable sheet name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_with_variable_sheet_name.png "Excel formula: Lookup with variable sheet name")](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

### [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

In this example, the goal is to create a lookup formula with a variable sheet name. In other words, a formula that uses a sheet name typed into a cell to construct a reference to a range on that sheet. If the sheet name is changed, the reference should update automatically. The key to the solution...

[![Excel formula: Sum across multiple worksheets with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20across%20multiple%20worksheets%20with%20criteria.png "Excel formula: Sum across multiple worksheets with criteria")](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)

### [Sum across multiple worksheets with criteria](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)

In this example, the goal is to sum hours per project across three different worksheets: Sheet1, Sheet2, and Sheet3. The data on each of the three sheets has the same structure as Sheet1, as seen below: 3D reference won't work Before we look at a solution, let's look at something that doesn't work...

[![Excel formula: Dynamic workbook reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20workbook%20reference.png "Excel formula: Dynamic workbook reference")](https://exceljet.net/formulas/dynamic-workbook-reference)

### [Dynamic workbook reference](https://exceljet.net/formulas/dynamic-workbook-reference)

In this example, the goal is to create a reference to an external workbook with variable information. The easiest way to do this is to assemble the reference to a range or cell in another workbook as a text value , then use the INDIRECT function to convert the text to an actual reference. In Excel...

[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)

### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...

[![Excel formula: Indirect named range different sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Indirect%20named%20range%20different%20sheet.png "Excel formula: Indirect named range different sheet")](https://exceljet.net/formulas/indirect-named-range-different-sheet)

### [Indirect named range different sheet](https://exceljet.net/formulas/indirect-named-range-different-sheet)

The formula above evaluates something like this: =SUM(INDIRECT("'"...

[![Excel formula: Increment cell reference with INDIRECT](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/increment%20cell%20reference%20with%20INDIRECT.png "Excel formula: Increment cell reference with INDIRECT")](https://exceljet.net/formulas/increment-cell-reference-with-indirect)

### [Increment cell reference with INDIRECT](https://exceljet.net/formulas/increment-cell-reference-with-indirect)

Consider a simple dynamic reference to Sheet2 using the INDIRECT in a formula like this: =INDIRECT($B$5&"!"&"A1") If we change the sheet name in B5 to another (valid) name, INDIRECT will return a reference to A1 in the new sheet. However, if we copy this formula down the column, the...

Related functions
-----------------

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)
    
*   [Sum across multiple worksheets with criteria](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)
    
*   [Dynamic workbook reference](https://exceljet.net/formulas/dynamic-workbook-reference)
    
*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)
    
*   [Indirect named range different sheet](https://exceljet.net/formulas/indirect-named-range-different-sheet)
    
*   [Increment cell reference with INDIRECT](https://exceljet.net/formulas/increment-cell-reference-with-indirect)
    

### Functions

*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

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
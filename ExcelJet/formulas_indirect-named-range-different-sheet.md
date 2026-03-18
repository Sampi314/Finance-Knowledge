# Indirect named range different sheet - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/indirect-named-range-different-sheet

---

[Skip to main content](https://exceljet.net/formulas/indirect-named-range-different-sheet#main-content)

[](https://exceljet.net/formulas/indirect-named-range-different-sheet#)

*   [Previous](https://exceljet.net/formulas/get-workbook-path-only)
    
*   [Next](https://exceljet.net/formulas/list-sheet-index-numbers)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Indirect named range different sheet
====================================

by Dave Bruns · Updated 2 Sep 2017

Related functions 
------------------

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Indirect named range different sheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Indirect%20named%20range%20different%20sheet.png "Excel formula: Indirect named range different sheet")

Summary
-------

To reference a named range on another sheet, you can use the INDIRECT function with the required sheet syntax. In the example shown, the formula in D6 is:

    =SUM(INDIRECT("'"&B6&"'!"&C6))
    

Which returns the sum of the named range "data" on Sheet1.

Generic formula
---------------

    INDIRECT("'"&sheet&"'!"&name)

Explanation 
------------

The formula above evaluates something like this:

    =SUM(INDIRECT("'"&B6&"'!"&C6))
    =SUM(INDIRECT("'"&"Sheet1"&"'!"&"data"))
    =SUM('Sheet1'!data)
    

Once the string is assembled using values in B6 and C6, INDIRECT evaluates and transforms the string into a proper reference.

Note you can refer to a [named range](https://exceljet.net/glossary/named-range)
 in a formula without using INDIRECT. For example, the formula in D6 could be written:

    =SUM('Sheet1'!data)
    

However, if you want to assemble the reference as text, and have Excel treat the text as a reference, you need to use INDIRECT.

_Note: The single quotes are added in the formula above so that the formula will work when a sheet name contains spaces._

Related formulas
----------------

[![Excel formula: Worksheet name exists](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/worksheet%20name%20exists.png "Excel formula: Worksheet name exists")](https://exceljet.net/formulas/worksheet-name-exists)

### [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)

The ISREF function returns TRUE for a valid worksheet reference and FALSE is not. In this case, we want to find out of a particular sheet exists in a workbook, so we construct a full reference by concatenating the sheet names in column B with an exclamation mark and "A1": B5...

[![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")](https://exceljet.net/formulas/dynamic-worksheet-reference)

### [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)

The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using concatenation , and use the resulting text as a valid reference. In this example, we have Sheet names in column B, so we join the sheet name to the...

[![Excel formula: Sum across multiple worksheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20across%20multiple%20worksheets.png "Excel formula: Sum across multiple worksheets")](https://exceljet.net/formulas/sum-across-multiple-worksheets)

### [Sum across multiple worksheets](https://exceljet.net/formulas/sum-across-multiple-worksheets)

In this example, the goal is to sum total points for each student across five worksheets that all have the same structure. This can be accomplished with a 3D reference, as explained below. Standard reference Before we look at how 3D references work, let's look at the standard approach. To solve...

[![Excel formula: Sum across multiple worksheets with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20across%20multiple%20worksheets%20with%20criteria.png "Excel formula: Sum across multiple worksheets with criteria")](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)

### [Sum across multiple worksheets with criteria](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)

In this example, the goal is to sum hours per project across three different worksheets: Sheet1, Sheet2, and Sheet3. The data on each of the three sheets has the same structure as Sheet1, as seen below: 3D reference won't work Before we look at a solution, let's look at something that doesn't work...

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

*   [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)
    
*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    
*   [Sum across multiple worksheets](https://exceljet.net/formulas/sum-across-multiple-worksheets)
    
*   [Sum across multiple worksheets with criteria](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)
    

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
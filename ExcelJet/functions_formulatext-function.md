# Excel FORMULATEXT function | Exceljet

**Source:** https://exceljet.net/functions/formulatext-function

---

[Skip to main content](https://exceljet.net/functions/formulatext-function#main-content)

[](https://exceljet.net/functions/formulatext-function#)

*   [Previous](https://exceljet.net/functions/fieldvalue-function)
    
*   [Next](https://exceljet.net/functions/getpivotdata-function)
    

Excel 2013

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

FORMULATEXT Function
====================

by Dave Bruns · Updated 24 Jul 2021

Related functions 
------------------

[ISFORMULA](https://exceljet.net/functions/isformula-function)

![Excel FORMULATEXT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20formulatext%20function.png "Excel FORMULATEXT function")

Summary
-------

The Excel FORMULATEXT function returns a formula as a text string from a given reference. You can use FORMULATEXT to extract the formula as text from a cell. If you use FORMULATEXT on a cell that doesn't contain a formula, it returns #N/A.

Purpose 
--------

Get the formula in a cell

Return value 
-------------

The formula as text

Syntax
------

    =FORMULATEXT(reference)

*   _reference_ - Reference to cell or cell range.

Using the FORMULATEXT function 
-------------------------------

The FORMULATEXT function returns a formula as a [text string](https://exceljet.net/glossary/text-value)
 from a cell reference. The FORMULATEXT can be used to extract a formula as text from a cell reference. The text returned by FORMULATEXT is the same as displayed in the [formula bar](https://exceljet.net/glossary/formula-bar)
 when a cell with a formula is selected. Once text is extracted with FORMULA text, it can be handled as text in another formula.

FORMULATEXT takes just one argument, _reference_, which is normally a cell reference like A1. If you use FORMULATEXT on a cell that doesn't contain a formula, it returns #N/A. FORMULATEXT will handle formulas up to 8192 characters.

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the FORMULATEXT function will return more than one result when given a [range](https://exceljet.net/glossary/range)
 that contains formulas. These results will [spill](https://exceljet.net/glossary/spill)
 like other [dynamic array](https://exceljet.net/glossary/dynamic-array)
 formulas. In earlier versions of Excel, FORMULATEXT will return a single result from the upper left cell in the range.

To check if a cell contains a formula, use the [ISFORMULA function](https://exceljet.net/functions/isformula-function)
. To _temporarily_ display _all formula_ in a worksheet [with the keyboard shortcut Control + \`](https://exceljet.net/shortcuts/toggle-formulas-on-and-off)
.

### Examples

Assuming the formula =TODAY() in cell A1:

    =FORMULATEXT(A1) // returns "=TODAY()"
    

With the formula =C1+B1 in cell D1:

    =FORMULATEXT(D1) // returns "=C1+B1"
    

With the text "apple" in cell F1:

    =FORMULATEXT(F1) // returns #NA!
    

One quirk of FORMULATEXT is that it will not display a [circular reference error](https://exceljet.net/formulas/how-to-fix-a-circular-reference-error)
 if given a reference to the same cell it resides in. For example, if the formula below is entered in cell A1:

    =FORMULATEXT(A1) // returns =FORMULATEXT(A1)
    

The result is simply "=FORMULATEXT(A1)".

### Notes

*   To test if a cell contains a formula or not, use the [ISFORMULA](https://exceljet.net/functions/isformula-function)
     function.
*   FORMULATEXT will return #N/A if a cell does not contain a formula.
*   FORMULATEXT will return #N/A when referencing another workbook that is not open.
*   FORMULATEXT was introduced in Excel 2013.

FORMULATEXT function examples
-----------------------------

[![Excel formula: Show formula text with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/show%20formula%20text%20with%20formula.png "Excel formula: Show formula text with formula")](https://exceljet.net/formulas/show-formula-text-with-formula)

### [Show formula text with formula](https://exceljet.net/formulas/show-formula-text-with-formula)

The FORMULATEXT is fully automatic. When given the reference of a cell that contains a formula, it will return the entire formula as text. In the example as shown, the formula: =FORMULATEXT(C5) returns the text "=IF(B5>=70,"Pass","Fail")". Dealing with errors The FORMULATEXT function will return...

Related functions
-----------------

[![Excel ISFORMULA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isformula%20function.png "Excel ISFORMULA function")](https://exceljet.net/functions/isformula-function)

### [ISFORMULA Function](https://exceljet.net/functions/isformula-function)

The Excel ISFORMULA function returns TRUE if a cell contains a formula, and FALSE if not. When a cell contains a formula ISFORMULA will return TRUE regardless of the formula's output or error conditions.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Show formula text with formula](https://exceljet.net/formulas/show-formula-text-with-formula)
    

### Functions

*   [ISFORMULA Function](https://exceljet.net/functions/isformula-function)
    

### Links

*   [Microsoft FORMULATEXT function documentation](https://support.office.com/en-us/article/formulatext-function-0a786771-54fd-4ae2-96ee-09cda35439c8)
    

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
# Worksheet name exists - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/worksheet-name-exists

---

[Skip to main content](https://exceljet.net/formulas/worksheet-name-exists#main-content)

[](https://exceljet.net/formulas/worksheet-name-exists#)

*   [Previous](https://exceljet.net/formulas/list-sheet-names-with-formula)
    
*   [Next](https://exceljet.net/formulas/create-email-address-from-name)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Worksheet name exists
=====================

by Dave Bruns · Updated 28 Apr 2018

Related functions 
------------------

[ISREF](https://exceljet.net/functions/isref-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Worksheet name exists](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/worksheet%20name%20exists.png "Excel formula: Worksheet name exists")

Summary
-------

To test if a worksheet name exists in a workbook, you can use a formula based on the ISREF and INDIRECT functions. In the example shown, the formula in C5 is:

    =ISREF(INDIRECT(B5&"!A1"))
    

Generic formula
---------------

    =ISREF(INDIRECT("sheetname"&"!A1"))

Explanation 
------------

The ISREF function returns TRUE for a valid worksheet reference and FALSE is not.

In this case, we want to find out of a particular sheet exists in a workbook, so we construct a full reference by concatenating the sheet names in column B with an exclamation mark and "A1":

    B5&"!A1"
    

This returns the text:

    "Sheet1!A1"
    

which goes into the INDIRECT function. INDIRECT then tries to evaluate the text as a reference.

When INDIRECT succeeds, the reference is passed into ISREF which returns TRUE. When INDIRECT can't create a reference, it throws a #REF error, and ISREF returns FALSE.

### Dealing with spaces and punctuation in sheet names

If sheet names contain spaces, or punctuation characters, you'll need to adjust the formula to wrap the sheet name in single quotes like this:

    =ISREF(INDIRECT("'"&sheetname&"'!A1"))
    

Related formulas
----------------

[![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")](https://exceljet.net/formulas/dynamic-worksheet-reference)

### [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)

The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using concatenation , and use the resulting text as a valid reference. In this example, we have Sheet names in column B, so we join the sheet name to the...

[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)

### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...

Related functions
-----------------

[![Excel ISREF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")](https://exceljet.net/functions/isref-function)

### [ISREF Function](https://exceljet.net/functions/isref-function)

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

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

*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    
*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)
    

### Functions

*   [ISREF Function](https://exceljet.net/functions/isref-function)
    
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
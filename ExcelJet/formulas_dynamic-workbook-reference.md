# Dynamic workbook reference - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-workbook-reference

---

[Skip to main content](https://exceljet.net/formulas/dynamic-workbook-reference#main-content)

[](https://exceljet.net/formulas/dynamic-workbook-reference#)

*   [Previous](https://exceljet.net/formulas/count-errors-in-all-sheets)
    
*   [Next](https://exceljet.net/formulas/dynamic-worksheet-reference)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Dynamic workbook reference
==========================

by Dave Bruns · Updated 2 Dec 2021

Related functions 
------------------

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Dynamic workbook reference](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20workbook%20reference.png "Excel formula: Dynamic workbook reference")

Summary
-------

To build a dynamic worksheet reference – a reference to another workbook that is created with a formula based on information that may change – you can use a formula based on the [INDIRECT function](https://exceljet.net/functions/indirect-function)
. In the example shown, the formula in E6 is:

    =INDIRECT("'["&B6&"]"&C6&"'!"&D6)
    

_Note: the external workbook must be open for this reference to work._

Generic formula
---------------

    =INDIRECT("'["&workbook&"]"&sheet&"'!"&ref)

Explanation 
------------

In this example, the goal is to create a reference to an external workbook with variable information. The easiest way to do this is to assemble  the reference to a range or cell in another workbook as a [text value](https://exceljet.net/glossary/text-value)
, then use the INDIRECT function to convert the text to an actual reference. In Excel, a full reference to an external worksheet looks like this:

    '[sample data.xlsx]Sheet1'!A1
    

Note the square brackets (\[ \]) around workbook name, single quotes (' ') around the worksheet + sheet, and the exclamation mark (!) that follows.

To create a reference like this using text, we use [concatenation](https://exceljet.net/glossary/concatenation)
 to join values from columns B, C, and D with the required brackets, quotes, and exclamation mark:

    =INDIRECT("'["&B6&"]"&C6&"'!"&D6)
    

The result is fed into INDIRECT as _ref\_text_. Once the concatenation is performed, we have:

    =INDIRECT("'[sample data.xlsx]Sheet1'!A1")
    

The INDIRECT function then evaluates the text and converts it to a genuine reference, and Excel follows the reference and returns the value at the given reference.

_Note: if the reference is invalid, or if the workbook referenced is not open, INDIRECT will throw a #REF error. You can catch this error with the [IFERROR function](https://exceljet.net/functions/iferror-function)
 and display a custom result if you like._

Related formulas
----------------

[![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")](https://exceljet.net/formulas/dynamic-worksheet-reference)

### [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)

The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using concatenation , and use the resulting text as a valid reference. In this example, we have Sheet names in column B, so we join the sheet name to the...

[![Excel formula: VLOOKUP from another workbook](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/vlookup%20from%20another%20workbook.png "Excel formula: VLOOKUP from another workbook")](https://exceljet.net/formulas/vlookup-from-another-workbook)

### [VLOOKUP from another workbook](https://exceljet.net/formulas/vlookup-from-another-workbook)

In this example, the goal is to use VLOOKUP to find and retrieve price information for a given product stored in an external Excel workbook. The workbook exists in the same directory and the data in the file looks like this: Note the data itself is in the range B5:E13. VLOOKUP formula The formula...

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

*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    
*   [VLOOKUP from another workbook](https://exceljet.net/formulas/vlookup-from-another-workbook)
    

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
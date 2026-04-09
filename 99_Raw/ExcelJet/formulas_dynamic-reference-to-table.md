# Dynamic reference to table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-reference-to-table

---

[Skip to main content](https://exceljet.net/formulas/dynamic-reference-to-table#main-content)

[](https://exceljet.net/formulas/dynamic-reference-to-table#)

*   [Previous](https://exceljet.net/formulas/countifs-with-variable-table-column)
    
*   [Next](https://exceljet.net/formulas/get-column-index-in-excel-table)
    

[Tables](https://exceljet.net/formulas#Tables)

Dynamic reference to table
==========================

by Dave Bruns · Updated 5 Dec 2021

Related functions 
------------------

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Dynamic reference to table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic%20reference%20table%20name.png "Excel formula: Dynamic reference to table")

Summary
-------

To build a formula with a dynamic reference to an Excel Table name, you can use the [INDIRECT function](https://exceljet.net/functions/indirect-function)
 with [concatenation](https://exceljet.net/glossary/concatenation)
 as needed. In the example shown, the formula in L5 is:

    =SUM(INDIRECT(K5&"[Amount]"))
    

Which returns the sum of Amounts for three tables named "West", "Central", and "East".

Generic formula
---------------

    =SUM(INDIRECT(table&"[column]"))

Explanation 
------------

In this example, the goal is to create a dynamic reference to an [Excel Table](https://exceljet.net/glossary/excel-table)
 in a formula. In other words, create a formula that can refer to an Excel table by name as a variable. The easiest way to do this in Excel is to assemble the reference as a text value using [concatenation](https://exceljet.net/glossary/concatenation)
, then use the [INDIRECT function](https://exceljet.net/functions/indirect-function)
 to convert the text reference into a proper Excel reference.

In the example shown, the formulas in L5:L7 _behave_ like these simpler formulas:

    =SUM(West[Amount])
    =SUM(Central[Amount])
    =SUM(East[Amount])
    

However, instead of hardcoding the table into each SUM formula, the table names are listed in column K, and the formulas in column L use [concatenation](https://exceljet.net/glossary/concatenation)
 to assemble a reference to each table. This allows the same formula to be used in L5:L7.

The trick is the INDIRECT function to evaluate the reference. We start with:

    =SUM(INDIRECT(K5&"[Amount]"))
    

which becomes:

    =SUM(INDIRECT("West"&"[Amount]"))
    

and then:

    =SUM(INDIRECT("West[Amount]"))
    

The INDIRECT function then resolves the text string into a proper [structured reference](https://exceljet.net/glossary/structured-reference)
:

    =SUM(West[Amount])
    

And the SUM function returns the final result, 27,500 for the West region.

_Note: INDIRECT is a v[olatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance issues in larger, more complex workbooks._

Related formulas
----------------

[![Excel formula: VLOOKUP with variable table array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20variable%20table%20array.png "Excel formula: VLOOKUP with variable table array")](https://exceljet.net/formulas/vlookup-with-variable-table-array)

### [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)

In this example, the goal is to set up VLOOKUP to retrieve costs based on a variable vendor name. In other words, we want a formula that allows us to switch tables dynamically based on a user-supplied value. There are two cost tables in the worksheet, one for Vendor A and one for Vendor B. Both...

[![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")](https://exceljet.net/formulas/dynamic-worksheet-reference)

### [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)

The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using concatenation , and use the resulting text as a valid reference. In this example, we have Sheet names in column B, so we join the sheet name to the...

[![Excel formula: Dynamic workbook reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20workbook%20reference.png "Excel formula: Dynamic workbook reference")](https://exceljet.net/formulas/dynamic-workbook-reference)

### [Dynamic workbook reference](https://exceljet.net/formulas/dynamic-workbook-reference)

In this example, the goal is to create a reference to an external workbook with variable information. The easiest way to do this is to assemble the reference to a range or cell in another workbook as a text value , then use the INDIRECT function to convert the text to an actual reference. In Excel...

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

*   [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)
    
*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    
*   [Dynamic workbook reference](https://exceljet.net/formulas/dynamic-workbook-reference)
    

### Functions

*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

### Articles

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
    

### Training

*   [Excel Tables](https://exceljet.net/training/excel-tables)
    

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
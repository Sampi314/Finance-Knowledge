# Convert column letter to number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-column-letter-to-number

---

[Skip to main content](https://exceljet.net/formulas/convert-column-letter-to-number#main-content)

[](https://exceljet.net/formulas/convert-column-letter-to-number#)

*   [Previous](https://exceljet.net/formulas/conditional-mode-with-criteria)
    
*   [Next](https://exceljet.net/formulas/convert-column-number-to-letter)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Convert column letter to number
===============================

by Dave Bruns · Updated 23 Nov 2016

Related functions 
------------------

[COLUMN](https://exceljet.net/functions/column-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Convert column letter to number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20column%20letter%20to%20number.png "Excel formula: Convert column letter to number")

Summary
-------

To convert a column letter to an regular number (e.g. 1, 10, 26, etc.) you can use a formula based on the INDIRECT and COLUMN functions.

In the example shown, the formula in C5 is:

    =COLUMN(INDIRECT(B5&"1"))
    

Generic formula
---------------

    =COLUMN(INDIRECT(letter&"1"))

Explanation 
------------

The first step is to construct a standard "A1" style reference using the column letter, by adding a "1" with concatenation:

    B5&"1"
    

This results in a text string like "A1" which is passed into the INDIRECT function.

Next, the INDIRECT function transforms the text into a proper Excel reference and hands the result off to the COLUMN function.

Finally, the COLUMN function evaluates the reference and returns the column number for the reference.

Related formulas
----------------

[![Excel formula: Convert column number to letter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20column%20number%20to%20letter_0.png "Excel formula: Convert column number to letter")](https://exceljet.net/formulas/convert-column-number-to-letter)

### [Convert column number to letter](https://exceljet.net/formulas/convert-column-number-to-letter)

In this example, the goal is to convert an ordinary number into a column reference expressed in letters. For example, the number 1 should return "A", the number 2 should return "B", the number 26 should return "Z", etc. The challenge is that Excel can handle over 16,000 columns, so the number of...

Related functions
-----------------

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

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

*   [Convert column number to letter](https://exceljet.net/formulas/convert-column-number-to-letter)
    

### Functions

*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
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
# Increment a calculation with ROW or COLUMN - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/increment-a-calculation-with-row-or-column

---

[Skip to main content](https://exceljet.net/formulas/increment-a-calculation-with-row-or-column#main-content)

[](https://exceljet.net/formulas/increment-a-calculation-with-row-or-column#)

*   [Previous](https://exceljet.net/formulas/hyperlink-to-first-match)
    
*   [Next](https://exceljet.net/formulas/increment-a-number-in-a-text-string)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Increment a calculation with ROW or COLUMN
==========================================

by Dave Bruns · Updated 19 May 2024

Related functions 
------------------

[ROW](https://exceljet.net/functions/row-function)

[COLUMN](https://exceljet.net/functions/column-function)

![Excel formula: Increment a calculation with ROW or COLUMN](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/increment%20a%20calculation.png "Excel formula: Increment a calculation with ROW or COLUMN")

Summary
-------

To dynamically increment a calculation, so that a value automatically increments each time the formula is copied to a new row or column, you can use the [ROW](https://exceljet.net/functions/row-function)
 or [COLUMN](https://exceljet.net/functions/column-function)
 functions. In the example shown, the formula in cell D6 is:

    =$B$6*(ROW()-5)
    

When this formula is copied down column D, it multiplies the value in B6 by a number that starts with 1 and increments by one at each step.

Generic formula
---------------

    =calculation*ROW()

Explanation 
------------

The ROW function, when entered into a cell with no arguments returns the row number of that cell. In this case, the first instance of the formula is in cell D6 so, ROW() returns 6 inside the formula in D6.

We want to start with 1, however, so we need to subtract 5, which yields 1.

As the formula is copied down column D, ROW() keeps returning the current row number, and we keep subtracting 5 to "normalize" the result back to a 1-based scale:

    =$B$6*1 // D6
    =$B$6*2 // D7
    =$B$6*3 // D8
    etc
    

If you are copying a formula across columns, you can use the COLUMN function the same way.

Note that you are free to use the result of COLUMN or ROW any way you like in the formula. Both functions return a number, so you can apply them in a formula them just like you would use any number.

Related functions
-----------------

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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
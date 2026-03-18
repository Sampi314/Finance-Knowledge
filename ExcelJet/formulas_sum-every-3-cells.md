# Sum every 3 cells - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-every-3-cells

---

[Skip to main content](https://exceljet.net/formulas/sum-every-3-cells#main-content)

[](https://exceljet.net/formulas/sum-every-3-cells#)

*   [Previous](https://exceljet.net/formulas/student-class-enrollment-with-table)
    
*   [Next](https://exceljet.net/formulas/sum-roman-numbers)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Sum every 3 cells
=================

by Dave Bruns · Updated 24 Mar 2018

Related functions 
------------------

[OFFSET](https://exceljet.net/functions/offset-function)

[COLUMN](https://exceljet.net/functions/column-function)

![Excel formula: Sum every 3 cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20every%203%20cells.png "Excel formula: Sum every 3 cells")

Summary
-------

To write a formula that will sum "the next 3" cells each time it's copied, you can use the OFFSET function. In the example shown, the formula in O5 is:

    =SUM(OFFSET($B5,0,(COLUMN()-COLUMN($O$5))*3, 1,3))
    

_Note: the point of this formula is to eliminate the manual task of entering ranges manually with a single global formula, at the cost of a more complex formula._

Generic formula
---------------

    =SUM(OFFSET(first,0,(COLUMN()-COLUMN(current))*n, 1,n))

Explanation 
------------

At the core, the OFFSET function delivers a range of 3 cells to SUM, which returns a summed result.

The arguments for OFFSET are provided as follows:

For **reference** we use the first cell in the data range, B5, entered as a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 (column locked, row relative).

For **rows**, we use 0, since we don't need to change rows.

For **cols**, we use the expression:

    (COLUMN()-COLUMN($O$5))*3
    

This part of the formula figures out how many columns from the starting reference to offset. In O5, the offset is zero, in P5, the offset is 3, and so on.

Finally, **height** is input as 1 and **width** is input as 3, since in this case we always want a 1 x 3 range of cells.

_Note: change 3 to the multiplier you need, shown as "n" in the generic form of the formula above._

Related formulas
----------------

[![Excel formula: Copy value from every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20row_0.png "Excel formula: Copy value from every nth row")](https://exceljet.net/formulas/copy-value-from-every-nth-row)

### [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)

In this example, the goal is to copy every nth value from column B, where n is a variable that can be changed as needed. In Excel, it's difficult to create formulas that skip rows following a certain pattern, because the references in the formula will automatically change as the formula is copied...

[![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")](https://exceljet.net/formulas/copy-value-from-every-nth-column)

### [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct...

Related functions
-----------------

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

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

### Formulas

*   [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    
*   [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    

### Functions

*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    

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
# Flip table rows to columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/flip-table-rows-to-columns

---

[Skip to main content](https://exceljet.net/formulas/flip-table-rows-to-columns#main-content)

[](https://exceljet.net/formulas/flip-table-rows-to-columns#)

*   [Previous](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)
    
*   [Next](https://exceljet.net/formulas/forecast-vs-actual-variance)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Flip table rows to columns
==========================

by Dave Bruns · Updated 6 Apr 2016

Related functions 
------------------

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

![Excel formula: Flip table rows to columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/flip%20table%20rows%20to%20columns.png "Excel formula: Flip table rows to columns")

Summary
-------

To flip a table in Excel from rows to columns (i.e. to change orientation from vertical to horizontal) you can use the TRANSPOSE function.

In the example shown the formula in E5:K6 is:

    {=TRANSPOSE(B5:C11)}
    

Note: this is a multi-cell array formula and must be entered with Control + Shift + Enter.

Generic formula
---------------

    {=TRANSPOSE(range)}

Explanation 
------------

The TRANSPOSE function is fully automatic and can transpose cells vertical to horizontal, and vice versa. The only requirement is that there be a one to one relationship between source and target cells.

In the example shown, we are transposing a table that is 2 columns by 7 rows (14 cells), to a table that is 7 columns by 2 rows (14 cells).

Note that this function creates a dynamic link between the source and target. Any change in to data in the source table will be reflected in the target table.

### One-off conversion with Paste Special

If you simply need to do a one-time conversion, and don't need dynamic links, you can use Paste Special. Select the source data, copy, then use Paste Special > Transpose.

Related formulas
----------------

[![Excel formula: Transpose table without zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/transpose%20table%20without%20zeros.png "Excel formula: Transpose table without zeros")](https://exceljet.net/formulas/transpose-table-without-zeros)

### [Transpose table without zeros](https://exceljet.net/formulas/transpose-table-without-zeros)

The TRANSPOSE function automatically transposes values in a horizontal orientation to vertical orientation and vice versa. However, if a source cell is blank (empty) TRANSPOSE will output a zero. To fix that problem, this formula contains an IF function that checks first to see if a cell is blank...

Related functions
-----------------

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Transpose table without zeros](https://exceljet.net/formulas/transpose-table-without-zeros)
    

### Functions

*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    

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
# SUMIFS with horizontal range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sumifs-with-horizontal-range

---

[Skip to main content](https://exceljet.net/formulas/sumifs-with-horizontal-range#main-content)

[](https://exceljet.net/formulas/sumifs-with-horizontal-range#)

*   [Previous](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
    
*   [Next](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)
    

[Sum](https://exceljet.net/formulas#Sum)

SUMIFS with horizontal range
============================

by Dave Bruns · Updated 18 Jan 2023

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: SUMIFS with horizontal range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/SUMIFS%20with%20horizontal%20range.png "Excel formula: SUMIFS with horizontal range")

Summary
-------

To use SUMIFS with a horizontal range, be sure both the _sum\_range_ and criteria\_range are the same dimensions. In the example shown, the formula in cell I5 is:

    =SUMIFS(B5:G5,$B$4:$G$4,"red")
    

which returns the total of items in "Red" columns for each row.

Explanation 
------------

Normally, SUMIFS is used with data in a vertical arrangement, but it can also be used in cases where data is arranged horizontally. The trick is to make sure the _sum\_range_ and _criteria\_range_ are the same dimensions. In the example shown, the formula in cell I5, copied down the column is:

    =SUMIFS(B5:G5,$B$4:$G$4,"red")
    

Notice the _criteria\_range_, B4:G4 is locked as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to prevent changes as the formula is copied.

### Totals for each color

By carefully using a combination of absolute and [mixed references](https://exceljet.net/glossary/mixed-reference)
, you can calculate totals for each color in a summary table. Notice in the example below, we are now picking up the cell references, I4, J4, and K4 to use directly as criteria:

![SUMIFS horizontal range to subtotal rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/SUMIFS%20with%20horizontal%20range%20subtotals.png?itok=DjjrkSQB "SUMIFS horizontal range to subtotal rows")

The formula below in cell I5, copied down and across the table is:

    =SUMIFS($B5:$G5,$B$4:$G$4,I$4)
    

Notice references are set up carefully so that the formula can be copied across and down:

*   The _sum\_range_, $B5:$G5, is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
     with columns locked
*   The _criteria\_range_, B$4:$G$4 is [absolute](https://exceljet.net/glossary/absolute-reference)
     and fully locked as before
*   The criteria is a mixed reference, I$4, with the row locked

Related formulas
----------------

[![Excel formula: Sum entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20entire%20column.png "Excel formula: Sum entire column")](https://exceljet.net/formulas/sum-entire-column)

### [Sum entire column](https://exceljet.net/formulas/sum-entire-column)

In this example, the goal is to return the total for an entire column in an Excel worksheet. One way to do this is to use a full column reference. Full column references Excel supports " full column " like this: =SUM(A:A) // sum all of column A =SUM(C:C) // sum all of column C =SUM(A:C) // sum all...

[![Excel formula: Sum matching columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20matching%20columns.png "Excel formula: Sum matching columns")](https://exceljet.net/formulas/sum-matching-columns)

### [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)

At the core, this formula relies on the SUMPRODUCT function to sum values in matching columns in the named range data C5:G14. If all data were provided to SUMPRODUCT in a single range, the result would be the sum of all values in the range: =SUMPRODUCT(data) // all data, returns 387 To apply a...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum entire column](https://exceljet.net/formulas/sum-entire-column)
    
*   [Sum matching columns](https://exceljet.net/formulas/sum-matching-columns)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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
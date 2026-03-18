# Multiplication table formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/multiplication-table-formula

---

[Skip to main content](https://exceljet.net/formulas/multiplication-table-formula#main-content)

[](https://exceljet.net/formulas/multiplication-table-formula#)

*   [Previous](https://exceljet.net/formulas/most-frequently-occurring-number)
    
*   [Next](https://exceljet.net/formulas/new-customers-per-month)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Multiplication table formula
============================

by Dave Bruns · Updated 29 Apr 2023

![Excel formula: Multiplication table formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Mixed%20reference%20for%20multiplication%20table.png "Excel formula: Multiplication table formula")

Summary
-------

Building a multiplication table in Excel is a classic problem because it requires a "[mixed reference](https://exceljet.net/glossary/mixed-reference)
" – a reference that is partially absolute, partially relative. In the example shown, the formula in C5 is:

    =$B5*C$4
    

Note both cell references have absolute and relative elements, so they are referred to as "mixed references".

Generic formula
---------------

    =$A2*B$1

Explanation 
------------

This formula is designed to be copied throughout the interior of the multiplication table without change. In other words, when the formula is copied to other cells in the table, the references will automatically update as needed to calculate the product of the corresponding row and column.

In $B5, the column is "locked" so that it won't change, and in C$4, the row is locked.

As the formula is copied, this is what the references look like for the first 5 rows and columns:

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
|     | 1   | 2   | 3   | 4   | 5   |
| 1   | \=$B5\*C$4 | \=$B5\*D$4 | \=$B5\*E$4 | \=$B5\*F$4 | \=$B5\*G$4 |
| 2   | \=$B6\*C$4 | \=$B6\*D$4 | \=$B6\*E$4 | \=$B6\*F$4 | \=$B6\*G$4 |
| 3   | \=$B7\*C$4 | \=$B7\*D$4 | \=$B7\*E$4 | \=$B7\*F$4 | \=$B7\*G$4 |
| 4   | \=$B8\*C$4 | \=$B8\*D$4 | \=$B8\*E$4 | \=$B8\*F$4 | \=$B8\*G$4 |
| 5   | \=$B9\*C$4 | \=$B9\*D$4 | \=$B9\*E$4 | \=$B9\*F$4 | \=$B9\*G$4 |

  
[Mixed references](https://exceljet.net/glossary/mixed-reference)
 are a common feature in well-designed worksheets. They are harder to set up, but make formulas much easier to enter. In addition, they are a key strategy for preventing errors since they allow the same formula to be copied to many locations _without_ manual edits.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

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
# Total rows in range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/total-rows-in-range

---

[Skip to main content](https://exceljet.net/formulas/total-rows-in-range#main-content)

[](https://exceljet.net/formulas/total-rows-in-range#)

*   [Previous](https://exceljet.net/formulas/total-columns-in-range)
    
*   [Next](https://exceljet.net/formulas/automatic-row-numbers-in-table)
    

[Range](https://exceljet.net/formulas#Range)

Total rows in range
===================

by Dave Bruns · Updated 16 Sep 2020

Related functions 
------------------

[ROWS](https://exceljet.net/functions/rows-function)

![Excel formula: Total rows in range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/total%20rows%20in%20range.png "Excel formula: Total rows in range")

Summary
-------

To count the number of rows in a range, use the [ROWS function](https://exceljet.net/functions/rows-function)
. In the example shown, the formula in F5 is:

    =ROWS(B5:C10)
    

Generic formula
---------------

    =ROWS(rng)

Explanation 
------------

The ROWS function is fully automatic. When you provide a range to ROWS, it will return a count of all rows in the range. In the example, the formula in F5 returns 6, because there are 6 rows in the range B5:C10:

    =ROWS(B5:C10) // count rows
    

ROWS counts the number of rows in any supplied range and returns a number as a result. For example, if we provide all of column A in a range, Excel returns 1,048,576 the total number of rows in an Excel worksheet.

    =ROWS(A:A) // returns 1048576
    

To count columns in a range, see the [COLUMNS function](https://exceljet.net/functions/columns-function)
.

Related formulas
----------------

[![Excel formula: Total columns in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20columns%20in%20range.png "Excel formula: Total columns in range")](https://exceljet.net/formulas/total-columns-in-range)

### [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)

The COLUMNS function is fully automatic. When you provide a range to COLUMNS, it will return a count of all columns in the range. In the example, the formula in F6 returns 2, because there are 2 columns in the range B5:C10: =COLUMNS(B5:C10) // count columns COLUMNS counts the number of columns in...

[![Excel formula: Count cells in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_cells_in_range.png "Excel formula: Count cells in range")](https://exceljet.net/formulas/count-cells-in-range)

### [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)

The goal is to count the number of cells in a given range, regardless of whether the cells are empty or not. Although Excel has several functions designed to count cells based on their contents, there is no built-in function for counting the total number of cells in a range. The classic solution is...

Related functions
-----------------

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)
    
*   [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)
    

### Functions

*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

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
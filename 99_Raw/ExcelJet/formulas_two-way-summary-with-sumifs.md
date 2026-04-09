# Two-way summary with SUMIFS - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/two-way-summary-with-sumifs

---

[Skip to main content](https://exceljet.net/formulas/two-way-summary-with-sumifs#main-content)

[](https://exceljet.net/formulas/two-way-summary-with-sumifs#)

*   [Previous](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)
    
*   [Next](https://exceljet.net/formulas/how-to-fix-a-circular-reference-error)
    

[Tables](https://exceljet.net/formulas#Tables)

Two-way summary with SUMIFS
===========================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Two-way summary with SUMIFS](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/two-way%20summary%20with%20sumifs.png "Excel formula: Two-way summary with SUMIFS")

Summary
-------

To build a two-way summary table that sums numeric data with more than one condition, you can use the SUMIFS function. In the example shown, the formula in H5, copied across range H5:K7, is:

    =SUMIFS(value,name,$G5,stage,H$4)
    

where **value** (C5:C15), **name** (B5:B15), and **stage** (D5:D15) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is a table that shows summary totals for each name by stage.

Explanation 
------------

The [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 is designed to sum numeric values using multiple criteria. In the example shown, the data in the range B5:E15 shows a sales pipeline where each row is an opportunity owned by a salesperson, at a specific stage. The formula in H5 is:

    =SUMIFS(value,name,$G5,stage,H$4)
    

The first part of the formula sums opportunities by salesperson:

    =SUMIFS(value,name,$G5 // sum by name
    

*   Sum range is the named range **values**
*   Criteria range 1 is the named range **name**
*   Criteria 1 comes from cell G5

Notice $G5 is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
, with the column locked and the row relative. This allows the formula to change as needed when the formula is copied throughout the table.

The next range/criteria pair in SUMIFS, sums by stage:

    stage,H$4 // sum by stage
    

*   Criteria range 2 is the named range **stage**
*   Criteria 2 is H$4

Again, H$4 is a mixed reference, with the column relative and the row locked. This allows the criteria to pick up the stage values in row 4 as the formula is copied across and down the table.

With both criteria together, the SUMIFS function correctly sums the opportunities by name and by stage.

### Without names ranges

This example uses named ranges for convenience only. Without named ranges, the equivalent formula is:

    =SUMIFS($C$5:$C$15,$B$5:$B$15,$G5,$D$5:$D$15,H$4)
    

Notice references for name, value, and stage are now [absolute references](https://exceljet.net/glossary/absolute-reference)
 to prevent changes as the formula is copied across and down the table.

_Note: a [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 would also be an excellent way to solve this problem._

Related formulas
----------------

[![Excel formula: SUMIFS with Excel Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20with%20Excel%20Table.png "Excel formula: SUMIFS with Excel Table")](https://exceljet.net/formulas/sumifs-with-excel-table)

### [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)

This formula uses structured references to feed table ranges into the SUMIFS function. The sum range is provided as Table1\[Total\] , the criteria range is provided as Table1\[Item\] , and criteria comes from values in column I. The formula in I5 is: =SUMIFS(Table1\[Total\],Table1\[Item\],H5) which...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20SUMIFS%20with%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

### [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

In this video, we'll look at how to use the SUMIFS function with an Excel Table. On this worksheet, I have two identical sets of order data. I'm going to walk through the process of constructing a summary of sales by item for both sets of data. With the data on the left, I'll use standard formulas...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)
    

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
# Count table columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-table-columns

---

[Skip to main content](https://exceljet.net/formulas/count-table-columns#main-content)

[](https://exceljet.net/formulas/count-table-columns#)

*   [Previous](https://exceljet.net/formulas/basic-inventory-formula-example)
    
*   [Next](https://exceljet.net/formulas/count-table-rows)
    

[Tables](https://exceljet.net/formulas#Tables)

Count table columns
===================

by Dave Bruns · Updated 25 Oct 2023

Related functions 
------------------

[COLUMNS](https://exceljet.net/functions/columns-function)

![Excel formula: Count table columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20table%20columns.png "Excel formula: Count table columns")

Summary
-------

To count columns in an [Excel table,](https://exceljet.net/articles/excel-tables)
 you can use the COLUMNS function. In the example shown, the formula in I4 is:

    =COLUMNS(Table1)
    

The result is 5, the number of columns in Table1 as shown.

Generic formula
---------------

    COLUMNS(table)

Explanation 
------------

This formula uses [structured referencing](https://exceljet.net/glossary/structured-reference)
, a syntax that allows table parts to be referred to by name. When a table is referred to by the name only, Excel returns a reference to the data region of the table only. In this case, the entire table range is B4:F104 so Table1 returns the range B5:F105 to the COLUMNS function.

    =COLUMNS(Table1)
    =COLUMNS(B5:F105)
    

COLUMNS then returns a final result of 5, since there are 5 columns in the table.

Related formulas
----------------

[![Excel formula: Count table rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20table%20rows.png "Excel formula: Count table rows")](https://exceljet.net/formulas/count-table-rows)

### [Count table rows](https://exceljet.net/formulas/count-table-rows)

This formula uses structured referencing , a syntax that allows table parts to be called out by name. When a table is called with the name only, Excel returns a reference to the data region of the table only. In this case, the entire table range is B4:F104 so Table1 returns the range B5:F105 to the...

Related functions
-----------------

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count table rows](https://exceljet.net/formulas/count-table-rows)
    

### Functions

*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    

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
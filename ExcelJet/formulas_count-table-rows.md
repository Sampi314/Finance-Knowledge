# Count table rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-table-rows

---

[Skip to main content](https://exceljet.net/formulas/count-table-rows#main-content)

[](https://exceljet.net/formulas/count-table-rows#)

*   [Previous](https://exceljet.net/formulas/count-table-columns)
    
*   [Next](https://exceljet.net/formulas/countifs-with-variable-table-column)
    

[Tables](https://exceljet.net/formulas#Tables)

Count table rows
================

by Dave Bruns · Updated 25 Oct 2023

Related functions 
------------------

[ROWS](https://exceljet.net/functions/rows-function)

![Excel formula: Count table rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20table%20rows.png "Excel formula: Count table rows")

Summary
-------

To count rows in an [Excel table](https://exceljet.net/articles/excel-tables)
, you can use the ROWS function. In the example shown, the formula in I4 is:

    =ROWS(Table1)
    

The result is 100, since Table1 contains 100 rows of data.

Generic formula
---------------

    =ROWS(table)

Explanation 
------------

This formula uses [structured referencing](https://exceljet.net/glossary/structured-reference)
, a syntax that allows table parts to be called out by name. When a table is called with the name only, Excel returns a reference to the data region of the table only. In this case, the entire table range is B4:F104 so Table1 returns the range B5:F105 to the ROWS function.

    =ROWS(Table1)
    =ROWS(B5:F105)
    

ROWS then returns a final result of 100. Note that the header row is not included in this count.

Related formulas
----------------

[![Excel formula: Count table columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20table%20columns.png "Excel formula: Count table columns")](https://exceljet.net/formulas/count-table-columns)

### [Count table columns](https://exceljet.net/formulas/count-table-columns)

This formula uses structured referencing , a syntax that allows table parts to be referred to by name. When a table is referred to by the name only, Excel returns a reference to the data region of the table only. In this case, the entire table range is B4:F104 so Table1 returns the range B5:F105 to...

Related functions
-----------------

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Introduction%20to%20structured%20references_thumb.png)](https://exceljet.net/videos/introduction-to-structured-references)

### [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)

In this video, I'll give a brief introduction to structured references. A structured reference is a term for using a table name in a formula instead of a normal cell reference. Structured references are optional, and can be used with formulas both inside or outside an Excel table. Let's take a look...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count table columns](https://exceljet.net/formulas/count-table-columns)
    

### Functions

*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

### Videos

*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    

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
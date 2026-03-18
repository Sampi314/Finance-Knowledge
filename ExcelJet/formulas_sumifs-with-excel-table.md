# SUMIFS with Excel Table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sumifs-with-excel-table

---

[Skip to main content](https://exceljet.net/formulas/sumifs-with-excel-table#main-content)

[](https://exceljet.net/formulas/sumifs-with-excel-table#)

*   [Previous](https://exceljet.net/formulas/sumifs-vs-other-lookup-formulas)
    
*   [Next](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)
    

[Tables](https://exceljet.net/formulas#Tables)

SUMIFS with Excel Table
=======================

by Dave Bruns · Updated 17 Dec 2019

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: SUMIFS with Excel Table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/SUMIFS%20with%20Excel%20Table.png "Excel formula: SUMIFS with Excel Table")

Summary
-------

To conditionally sum numeric data in an Excel table, you can use SUMIFS with [structured references](https://exceljet.net/glossary/structured-reference)
 for both sum and criteria ranges. In the example shown, the formula in I5 is:

    =SUMIFS(Table1[Total],Table1[Item],H5)
    

Where Table1 is an [Excel Table](https://exceljet.net/glossary/excel-table)
 with the data range B105:F89.

Generic formula
---------------

    =SUMIFS(Table[sum_col],Table[crit_col],criteria)

Explanation 
------------

This formula uses [structured references](https://exceljet.net/glossary/structured-reference)
 to feed table ranges into the SUMIFS function.

The sum range is provided as **Table1\[Total\]**, the criteria range is provided as **Table1\[Item\]**, and criteria comes from values in column I.

The formula in I5 is:

    =SUMIFS(Table1[Total],Table1[Item],H5)
    

which resolves to:

    =SUMIFS(F5:F89,D5:D89,"Shorts")
    

The SUMIFS function returns 288, the sum values in the Total column where the value in the Item column is "Shorts".

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20SUMIFS%20with%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

### [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

In this video, we'll look at how to use the SUMIFS function with an Excel Table. On this worksheet, I have two identical sets of order data. I'm going to walk through the process of constructing a summary of sales by item for both sets of data. With the data on the left, I'll use standard formulas...

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

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Videos

*   [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)
    
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
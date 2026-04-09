# Get column name from index in table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-column-name-from-index-in-table

---

[Skip to main content](https://exceljet.net/formulas/get-column-name-from-index-in-table#main-content)

[](https://exceljet.net/formulas/get-column-name-from-index-in-table#)

*   [Previous](https://exceljet.net/formulas/get-column-index-in-excel-table)
    
*   [Next](https://exceljet.net/formulas/percentile-if-in-table)
    

[Tables](https://exceljet.net/formulas#Tables)

Get column name from index in table
===================================

by Dave Bruns · Updated 6 Aug 2020

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Get column name from index in table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20column%20name%20from%20index%20in%20table.png "Excel formula: Get column name from index in table")

Summary
-------

To get the name of a column in an Excel Table from its numeric index, you can use the INDEX function with a structured reference. In the example shown, the formula in I4 is:

    =INDEX(Table1[#Headers],H5)
    

When the formula is copied down, it returns an name for each column, based on index values in column H.

Generic formula
---------------

    =INDEX(Table[#Headers],index)

Explanation 
------------

This is a standard INDEX formula. The only trick to the formula is the use of a structured reference to return a range for the table headers:

    Table1[#Headers]
    

This range goes into INDEX for the array argument, with the index value supplied from column H:

    =INDEX(Table1[#Headers],H5)
    

The result is the name of the first item in the header, which is "ID".

Although the headers are in a horizontal array, with values in columns, INDEX will use the row number as a generic INDEX for one-dimensional arrays like this and correctly return the value at that position.

Related formulas
----------------

[![Excel formula: Get column index in Excel Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20column%20index%20in%20Excel%20Table.png "Excel formula: Get column index in Excel Table")](https://exceljet.net/formulas/get-column-index-in-excel-table)

### [Get column index in Excel Table](https://exceljet.net/formulas/get-column-index-in-excel-table)

This is a standard MATCH formula where the lookup values come from column H, the array is the headers in Table1, and match type is zero, to force an exact match. The only trick to the formula is the use of a structured reference to return a range for the table headers to the MATCH function: Table1...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20with%20a%20table-Thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-with-a-table)

### [How to use VLOOKUP with a table](https://exceljet.net/videos/how-to-use-vlookup-with-a-table)

In this video, we'll look at how to use VLOOKUP to lookup values in an Excel Table. On this worksheet, I have a table that contains employee data, named Table1. To illustrate how to work with VLOOKUP when the source data is in a table, I'll set up formulas to the right to extract data from the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get column index in Excel Table](https://exceljet.net/formulas/get-column-index-in-excel-table)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Videos

*   [How to use VLOOKUP with a table](https://exceljet.net/videos/how-to-use-vlookup-with-a-table)
    

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
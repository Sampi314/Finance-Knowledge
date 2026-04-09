# Get column index in Excel Table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-column-index-in-excel-table

---

[Skip to main content](https://exceljet.net/formulas/get-column-index-in-excel-table#main-content)

[](https://exceljet.net/formulas/get-column-index-in-excel-table#)

*   [Previous](https://exceljet.net/formulas/dynamic-reference-to-table)
    
*   [Next](https://exceljet.net/formulas/get-column-name-from-index-in-table)
    

[Tables](https://exceljet.net/formulas#Tables)

Get column index in Excel Table
===============================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Get column index in Excel Table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20column%20index%20in%20Excel%20Table.png "Excel formula: Get column index in Excel Table")

Summary
-------

To get the index of a column in an Excel Table, you can use the MATCH function. In the example shown, the formula in I4 is:

    =MATCH(H4,Table1[#Headers],0)
    

When the formula is copied down, it returns an index for each column listed in column H. Getting an index like this is useful when you want to refer to table columns by index in other formulas, like VLOOKUP, INDEX and MATCH, etc.

Generic formula
---------------

    =MATCH(name,Table[#Headers],0)

Explanation 
------------

This is a standard MATCH formula where the lookup values come from column H, the array is the headers in Table1, and match type is zero, to force an exact match.

The only trick to the formula is the use of a structured reference to return a range for the table headers to the MATCH function:

    Table1[#Headers]
    

The nice thing about this reference is that it will automatically adjust to any changes in the table. Even when columns are added or removed, the reference will continue to return the correct range.

Related formulas
----------------

[![Excel formula: Two-way lookup VLOOKUP in a Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20lookup%20VLOOKUP%20in%20a%20Table.png "Excel formula: Two-way lookup VLOOKUP in a Table")](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)

### [Two-way lookup VLOOKUP in a Table](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)

At a high level, we use VLOOKUP to extract employee information in 4 columns with ID as the lookup value: =VLOOKUP($I$4,Table1,MATCH(H5,Table1\[#Headers\],0),0) The ID value comes from cell I4, and is locked so that it won't change as the formula is copied down the column. The table array is Table1,...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

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

*   [Two-way lookup VLOOKUP in a Table](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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
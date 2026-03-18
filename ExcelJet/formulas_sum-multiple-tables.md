# Sum multiple tables - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-multiple-tables

---

[Skip to main content](https://exceljet.net/formulas/sum-multiple-tables#main-content)

[](https://exceljet.net/formulas/sum-multiple-tables#)

*   [Previous](https://exceljet.net/formulas/running-total-in-table)
    
*   [Next](https://exceljet.net/formulas/sumifs-vs-other-lookup-formulas)
    

[Tables](https://exceljet.net/formulas#Tables)

Sum multiple tables
===================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Sum multiple tables](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Sum%20multiple%20tables.png "Excel formula: Sum multiple tables")

Summary
-------

To sum a total in multiple tables, you can use the SUM function and [structured references](https://exceljet.net/glossary/structured-reference)
 to refer to the columns to sum. In the example shown, the formula in I6 is:

    =SUM(Table1[Amount],Table2[Amount])
    

Generic formula
---------------

    =SUM(Table1[column],Table2[column])

Explanation 
------------

This formula uses [structured references](https://exceljet.net/glossary/structured-reference)
 to refer to the "Amount" column in each table. The structured references in this formula resolve to normal references like this:

    =SUM(Table1[Amount],Table2[Amount])
    =SUM(C7:C11,F7:F13)
    =1495.5
    

When rows or columns are added or removed from either table, the formula will continue to return correct results. In addition, the formula will work even if the tables are located on different sheets in a workbook.

### Alternative syntax with Total row

It is also possible to reference the total row in a table directly, as long as tables have the Total Row enabled. The syntax looks like this:

    Table1[[#Totals],[Amount]]
    

_Translated: "The value for Amount in the Total row of Table1"._

Using this syntax, the original formula above could be re-written like this:

    =SUM(Table1[[#Totals],[Amount]],Table2[[#Totals],[Amount]])
    

As above, this formula will work even when the table is moved or resized.

_Note: the total row must be enabled. If you disable a total row, the formula will return the #REF error._

Related formulas
----------------

[![Excel formula: Two-way lookup VLOOKUP in a Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20lookup%20VLOOKUP%20in%20a%20Table.png "Excel formula: Two-way lookup VLOOKUP in a Table")](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)

### [Two-way lookup VLOOKUP in a Table](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)

At a high level, we use VLOOKUP to extract employee information in 4 columns with ID as the lookup value: =VLOOKUP($I$4,Table1,MATCH(H5,Table1\[#Headers\],0),0) The ID value comes from cell I4, and is locked so that it won't change as the formula is copied down the column. The table array is Table1,...

[![Excel formula: Running total in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20total%20in%20table2.png "Excel formula: Running total in Table")](https://exceljet.net/formulas/running-total-in-table)

### [Running total in Table](https://exceljet.net/formulas/running-total-in-table)

At the core, this formula has a simple pattern like this: =SUM(first:current) Where "first" is the first cell in the Total column, and "current" is a reference to a cell in the current row of the Total column. To get the a reference to the first cell, we use INDEX like this: INDEX(\[Total\],1) Here,...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

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

*   [Two-way lookup VLOOKUP in a Table](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)
    
*   [Running total in Table](https://exceljet.net/formulas/running-total-in-table)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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
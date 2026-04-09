# Automatic row numbers in Table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/automatic-row-numbers-in-table

---

[Skip to main content](https://exceljet.net/formulas/automatic-row-numbers-in-table#main-content)

[](https://exceljet.net/formulas/automatic-row-numbers-in-table#)

*   [Previous](https://exceljet.net/formulas/total-rows-in-range)
    
*   [Next](https://exceljet.net/formulas/average-last-n-values-in-a-table)
    

[Tables](https://exceljet.net/formulas#Tables)

Automatic row numbers in Table
==============================

by Dave Bruns · Updated 9 Mar 2023

Related functions 
------------------

[ROW](https://exceljet.net/functions/row-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Automatic row numbers in Table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/automatic%20row%20number%20in%20excel%20table.png "Excel formula: Automatic row numbers in Table")

Summary
-------

To add automatic row numbers to an Excel Table, you can use a formula based on the [ROW function](https://exceljet.net/functions/row-function)
. In the example shown, the formula in B5, copied down, is:

    =ROW()-ROW(Table1[#Headers])
    

_Note: The table name is not required. However, Excel will add the table name automatically if omitted._

Generic formula
---------------

    =ROW()-ROW([#Headers])

Explanation 
------------

When no argument is provided, the ROW function returns the "current row", that is, the row number of the cell that contains it. When a cell reference is provided, ROW returns the row number of the cell. When a range is provided, ROW returns the first row number in the range.

In the example shown, the formula in B5 is:

    =ROW()-ROW(Table1[#Headers])
    

The first ROW returns 5, since ROW is provided no argument, and resides in cell B5. The second ROW uses a structured reference:

    Table1[#Headers] // header row
    

The header row resolves to the range $B$4:$F$4, so ROW returns 4. For the first 3 rows of the table, we have:

    B5=5-4 // 1
    B6=6-4 // 2
    B7=7-4 // 3
    

### No header row

The formula above works great as long as a table has a header row, but it will fail if the header row is disabled. If you are working with a table without a header row, you can use this alternative:

    =ROW()-INDEX(ROW(Table1),1,1)+1
    

In this formula, the first ROW function returns the current row, as above. The [INDEX function](https://exceljet.net/functions/index-function)
 returns the first cell in the range Table1 (cell B5) to the second ROW function, which always returns 5. For the first 3 rows of the table, the formula works like this:

    B5=5-5+1 // 1
    B6=6-5+1 // 2
    B7=7-5+1 // 3
    

This formula will continue to work normally even when the header row is disabled.

Related formulas
----------------

[![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")](https://exceljet.net/formulas/automatic-row-numbers)

### [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a...

[![Excel formula: Running count in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20in%20excel%20table.png "Excel formula: Running count in Table")](https://exceljet.net/formulas/running-count-in-table)

### [Running count in Table](https://exceljet.net/formulas/running-count-in-table)

At the core, this formula uses INDEX to create an expanding reference like this: INDEX(\[Color\],1):\[@Color\] // expanding range On the left side of the colon (:), the INDEX function returns a reference to the first cell in the column. INDEX(\[Color\],1) // first cell in color This works because, the...

[![Excel formula: Running total in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20total%20in%20table2.png "Excel formula: Running total in Table")](https://exceljet.net/formulas/running-total-in-table)

### [Running total in Table](https://exceljet.net/formulas/running-total-in-table)

At the core, this formula has a simple pattern like this: =SUM(first:current) Where "first" is the first cell in the Total column, and "current" is a reference to a cell in the current row of the Total column. To get the a reference to the first cell, we use INDEX like this: INDEX(\[Total\],1) Here,...

[![Excel formula: Two-way lookup VLOOKUP in a Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20lookup%20VLOOKUP%20in%20a%20Table.png "Excel formula: Two-way lookup VLOOKUP in a Table")](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)

### [Two-way lookup VLOOKUP in a Table](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)

At a high level, we use VLOOKUP to extract employee information in 4 columns with ID as the lookup value: =VLOOKUP($I$4,Table1,MATCH(H5,Table1\[#Headers\],0),0) The ID value comes from cell I4, and is locked so that it won't change as the formula is copied down the column. The table array is Table1,...

Related functions
-----------------

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20set%20up%20a%20running%20total%20in%20a%20table-Thumb.png)](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)

### [How to set up a running total in a table](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)

In this video, we'll look at how to set up a running total in an Excel table. Setting up a running total in an Excel table is a little tricky because it's not obvious how to use structured references. This is because structured references provide a notation for current row, but not for first row in...

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

*   [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)
    
*   [Running count in Table](https://exceljet.net/formulas/running-count-in-table)
    
*   [Running total in Table](https://exceljet.net/formulas/running-total-in-table)
    
*   [Two-way lookup VLOOKUP in a Table](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)
    

### Functions

*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Videos

*   [How to set up a running total in a table](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)
    
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
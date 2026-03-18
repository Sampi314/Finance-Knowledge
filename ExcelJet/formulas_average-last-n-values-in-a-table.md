# Average last N values in a table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-last-n-values-in-a-table

---

[Skip to main content](https://exceljet.net/formulas/average-last-n-values-in-a-table#main-content)

[](https://exceljet.net/formulas/average-last-n-values-in-a-table#)

*   [Previous](https://exceljet.net/formulas/automatic-row-numbers-in-table)
    
*   [Next](https://exceljet.net/formulas/basic-inventory-formula-example)
    

[Tables](https://exceljet.net/formulas#Tables)

Average last N values in a table
================================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[ROWS](https://exceljet.net/functions/rows-function)

![Excel formula: Average last N values in a table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Average%20last%20N%20values%20in%20a%20table.png "Excel formula: Average last N values in a table")

Summary
-------

To calculate the average for the last N values n an Excel table (i.e. last 3 rows, last 5 rows, etc.) you can use the AVERAGE function together with the INDEX and ROWS functions. In the example shown, the formula in F5 is:

    =AVERAGE(INDEX(Table1[Sales],ROWS(Table1)-(F4-1)):INDEX(Table1[Sales],ROWS(Table1)))
    

Generic formula
---------------

    =AVERAGE(INDEX(table[column],ROWS(table)-(N-1)):INDEX(table[column],ROWS(table)))
    

Explanation 
------------

This formula is a good example of how [structured references](https://exceljet.net/glossary/structured-reference)
 can make working with data in Excel much easier. At the core, this is what we're doing:

    =AVERAGE(first:last)
    

where "first" is a reference to the first cell to include in the average and "last" is a reference to the last cell to include. The result is a range that includes the N cells to average.

To get the first cell in the range, we use INDEX like this:

    INDEX(Table1[Sales],ROWS(Table1)-(F4-1))
    

The array is the entire Sales column, and row number worked by subtracting (n-1) from total rows.

In the example, F4 contains 3, so the row number is 10-(3-1) = 8. With a row number of 8, INDEX returns C12.

To get the last cell we use INDEX again like this:

    INDEX(Table1[Sales],ROWS(Table1))
    

There are 10 rows in the table, so INDEX returns C14.

The AVERAGE function then returns the average of C12:C14, which is $78.33.

Related formulas
----------------

[![Excel formula: Count table rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20table%20rows.png "Excel formula: Count table rows")](https://exceljet.net/formulas/count-table-rows)

### [Count table rows](https://exceljet.net/formulas/count-table-rows)

This formula uses structured referencing , a syntax that allows table parts to be called out by name. When a table is called with the name only, Excel returns a reference to the data region of the table only. In this case, the entire table range is B4:F104 so Table1 returns the range B5:F105 to the...

[![Excel formula: SUMIFS with Excel Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20with%20Excel%20Table.png "Excel formula: SUMIFS with Excel Table")](https://exceljet.net/formulas/sumifs-with-excel-table)

### [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)

This formula uses structured references to feed table ranges into the SUMIFS function. The sum range is provided as Table1\[Total\] , the criteria range is provided as Table1\[Item\] , and criteria comes from values in column I. The formula in I5 is: =SUMIFS(Table1\[Total\],Table1\[Item\],H5) which...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

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

*   [Count table rows](https://exceljet.net/formulas/count-table-rows)
    
*   [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
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
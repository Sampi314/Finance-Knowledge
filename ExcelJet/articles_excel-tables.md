# Excel Tables | Exceljet

**Source:** https://exceljet.net/articles/excel-tables

---

[Skip to main content](https://exceljet.net/articles/excel-tables#main-content)

[](https://exceljet.net/articles/excel-tables#)

*   [Previous](https://exceljet.net/articles/excel-shows-formula-not-result)
    
*   [Next](https://exceljet.net/articles/how-to-ask-a-question-about-excel)
    

Excel Tables
============

by Dave Bruns · Updated 19 Oct 2023

![Excel Tables are packed with useful features](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/23%20things%20to%20know%20about%20Excel%20Tables.png "Excel Tables are packed with useful features")

Summary
-------

Excel Tables have a boring (and confusingly generic) name, but they are packed with useful features. This article is a summary of the things you should know about Excel Tables.

Excel Tables are one of the most interesting and useful features in Excel. If you need a range that expands to include new data, and if you want to refer to data by name instead of by address, Excel Tables are for you. This article provides an introduction and overview.

### 1\. Creating a table is fast

You can create an Excel Table in less than 10 seconds. First, remove blank rows and make sure all columns have a unique name, then put the cursor anywhere in the data and use the keyboard shortcut Control + T. When you click OK, Excel will create the table.

![After creating a new table with Control + T](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/create%20table%20with%20shortcut2.png?itok=jVFI1pQD "After creating a new table with Control + T")

### 2\. Navigate directly to tables

Like [named ranges](https://exceljet.net/glossary/named-range)
, tables will appear in the namebox dropdown menu. Just click the menu, and select the table. Excel will navigate to the table, even if it's on a different tab in a workbook.

![Navigate directly to a table with the namebox](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/navigate%20with%20namebox.png?itok=zxJ67xgA "Navigate directly to a table with the namebox")

### 3\. Tables provide special shortcuts

When you convert regular data to an Excel Table, almost every shortcut you know works better. For example, you can select rows with shift + space, and columns with control + space. These shortcuts make selections that run precisely to the edge of the table, even when you can't see the edge of the table. Watch the video below for a quick rundown.

Video: [Shortcuts for Excel tables](https://exceljet.net/videos/shortcuts-for-excel-tables)

### 4\. Painless drag and drop

Tables make it much easier to rearrange data with drag and drop. After you've selected a table row or column, simply drag to a new location. Excel will quietly insert the selection at the new location, without complaining about overwriting data.

![Step 1: make a selection](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/table%20drag%20and%20drop%201.png?itok=JwB19G3r "Step 1: make a selection")

![Step 2: drag to a new location](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/table%20drag%20and%20drop%202.png?itok=dNUyBjvv "Step 2: drag to a new location")

Note: you must [select the entire row or column](https://exceljet.net/videos/shortcuts-for-excel-tables)
. For columns, that includes the header.

### 5\. Table headers stay visible

One frustration when working with a large set of data is that table headers disappear as you scroll down the table. Tables solve this problem in a clever way. When column headers scroll off the top of the table, Excel silently replaces worksheet columns with table headers.

![Table headers replace columns in large data sets](https://exceljet.net/sites/default/files/images/articles/inline/table%20headers%20replace%20columns.png "Table headers replace columns in large data sets")

### 6\. Tables expand automatically

When new rows or columns are added to an Excel Table, the table expands to enclose them. In a similar way, a table automatically contracts when rows or columns are deleted. When combined with structured references (see below) this gives you a dynamic range to use with formulas.

![Tables expand and contract automatically](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/tables%20expand%20and%20contract.png?itok=ss0zwPjs "Tables expand and contract automatically")

### 7\. Totals without formulas

All tables can display an optional Total Row. The Total Row can be easily configured to perform operations like SUM and COUNT without entering a formula. When the table is filtered, these totals will automatically calculate on visible rows only. You can toggle the Total Row on and off with the shortcut control + shift + T.

![Total row can be turned on and off, and customized](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/table%20total%20row.png?itok=7rigYOsk "Total row can be turned on and off, and customized")

### 8\. Rename a table anytime

All tables are automatically assigned a generic name like Table1, Table2, etc. However, you can rename a table at any time. Select any cell in the table and enter a new name on the Table Tools menu.

![Rename a table anytime](https://exceljet.net/sites/default/files/images/articles/inline/rename%20a%20table%20any%20time.png "Rename a table anytime")

### 9\. Fill formulas automatically

Tables have a feature called calculated columns that makes entering and maintaining formulas easier and more accurate. When you enter a standard formula in a column, the formula is automatically copied throughout the column, with no need for copy and paste.

![Enter formula in table column normally](https://exceljet.net/sites/default/files/images/articles/inline/fill%20formulas%20in%20table%201.png "Enter formula in table column normally")

![Formula is filled down column automatically](https://exceljet.net/sites/default/files/images/articles/inline/fill%20formulas%20in%20table%202.png "Formula is filled down column automatically")

### 10\. Change formulas automatically

The same feature also handles formula changes. If you make a change to the formula anywhere in a calculated column, the formula is updated throughout the entire column. In the screen below, the tax rate has been changed to 7% in one step.

![Formula change in any row propagated to all rows](https://exceljet.net/sites/default/files/images/articles/inline/fill%20formulas%20in%20table%203.png "Formula change in any row propagated to all rows")

### 11\. Human-readable formulas

Tables use a special formula syntax to refer to parts of a table by name. This feature is called "[structured references](https://exceljet.net/glossary/structured-reference)
". For example, to SUM a column called "Amount" in a table called "Orders", you can use a formula like this:

    =SUM(Orders[Amount])
    

![Tables allow human-readable formulas](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/human%20readable%20formulas2.png?itok=Vby9Vee6 "Tables allow human-readable formulas")

### 12\. Easy dynamic ranges

The single biggest benefit of tables is that they automatically expand as new data is added, creating a [dynamic range](https://exceljet.net/glossary/dynamic-named-range)
. You can easily use this dynamic range in your formulas. For example, the table in the screen below is named "Properties". The following formulas will always return correct values, even as data is added to the table:

    =ROWS(Properties)
    =MAX(Properties[Price])
    =MIN(Properties[Price])
    

![Easy dynamic ranges with tables](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/easy%20dynamic%20ranges2.png?itok=ejx5wSxc "Easy dynamic ranges with tables")

### 13\. Enter structured references with the mouse

An easy way to enter structured references in formulas is to use the mouse to select part of the table. Excel will automatically enter the structured reference for you. In the screen below, the price column was selected after entering =MAX(

![Enter structured references by selecting](https://exceljet.net/sites/default/files/images/articles/inline/enter%20structured%20references%20by%20selecting.png "Enter structured references by selecting")

### 14\. Enter structured references by typing

Another way to enter structured references is by typing. When you type the first few letters of a table in a formula, Excel will list matching table names below.

![Enter structured references by typing](https://exceljet.net/sites/default/files/images/articles/inline/enter%20structured%20references%20by%20typing.png "Enter structured references by typing")

Use the arrow keys to select and the TAB key to confirm. To enter a column name, enter an opening square bracket (\[) after the table name follow the same process - type a few letters, select with arrow keys, and use TAB to confirm.\
\
![Enter column by typing square bracket](https://exceljet.net/sites/default/files/images/articles/inline/enter%20structured%20references%20by%20typing%202.png "Enter column by typing square bracket")\
\
Video: [Introduction to Structured References and Tables](https://exceljet.net/videos/introduction-to-structured-references)\
\
### 15\. Check structured references with a formula\
\
You can quickly check a structured reference with the formula bar. For example, the following formula will select data in the "Address" column in the "Properties" table shown above:\
\
    =Properties[Address]\
    \
\
And this formula will select the headers of the table:\
\
    =Properties[#Headers]\
    \
\
Video: [How to query a table with formulas](https://exceljet.net/videos/formulas-to-query-a-table)\
\
Video: [How to use SUMIFS with a table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)\
\
### 16\. Change table formatting with one click\
\
All Excel tables have a style applied by default, but you can change this at any time. Select any cell in the table and use the Table Styles menu on the Table Tools tab of the ribbon. With one click, the table will inherit the new style.\
\
![Change table formatting with table styles menu](https://exceljet.net/sites/default/files/images/articles/inline/table%20styles%20menu.png "Change table formatting with table styles menu")\
\
### 17\. Remove all formatting\
\
Table formatting is not a requirement of Excel tables. To use a table without formatting, select the first style in the styles menu, which is called "None".\
\
![The style called "None" will clear formatting](https://exceljet.net/sites/default/files/images/articles/inline/table%20styles%20menu%20none.png "The style called "None" will clear formatting")\
\
Tip: you can use this style to remove all table formatting before converting a table back to a normal range.\
\
### 18\. Override local formatting\
\
When you apply a table style, local formatting is _preserved by default_. However, you can optionally override local formatting if you want. Right-click any style and choose "Apply and Clear formatting":\
\
![Table formatting can preserve or clear local formatting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/table%20styles%20menu%20apply%20and%20clear.png?itok=4Ba_8Q0g "Table formatting can preserve or clear local formatting")\
\
### 19\. Set a default table style\
\
You can right-click any style and choose "Set as Default". New tables in the same workbook will now use the default you set.\
\
![Set a table style as default](https://exceljet.net/sites/default/files/images/articles/inline/table%20styles%20set%20as%20default.png "Set a table style as default")\
\
_Note: to set a default table style in new workbooks, create a custom start-up template [as described in this article](https://exceljet.net/articles/how-to-set-a-default-template-in-excel)\
. In the template file, set the default table style of your choice._\
\
### 20\. Use a Table with a pivot table\
\
When you use a table as the source for a pivot table, the pivot table will automatically stay up to date with changes in data. Watch the video below to see how this works.\
\
Video: [Use a table for your next pivot table](https://exceljet.net/videos/why-you-should-use-a-table-for-your-pivot-table)\
\
### 21\. Use a table to create a dynamic chart\
\
Tables are a great way to create dynamic charts. New data in the table will automatically appear in the chart, and charts will exclude filtered rows by default.\
\
Video: [How to build a simple dynamic chart](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)\
\
### 22\. Add a slicer to a table\
\
Although all tables get filter controls by default, you can also add a slicer to a table, to make it easy to filter data with large buttons. To add a slicer to a table,  click the Insert Slicer button on the Design tab of the Table Tools menu.\
\
![Insert slicer for an Excel Table](https://exceljet.net/sites/default/files/images/articles/inline/Insert%20slicer%20for%20an%20Excel%20Table.png "Insert slicer for an Excel Table")\
\
The table below has a slicer for Department:\
\
![Excel Table with slicer added](https://exceljet.net/sites/default/files/images/articles/inline/Table%20slicer%20example.png "Excel Table with slicer added")\
\
### 23\. Get rid of a table\
\
To get rid of a table, use the Convert to Range command on the Table Tools tab of the ribbon.\
\
![Convert a table back to a normal range](https://exceljet.net/sites/default/files/images/articles/inline/Table%20convert%20to%20range.png "Convert a table back to a normal range")\
\
You might be surprised to see that converting a table back to a normal range doesn't remove formatting. To remove table formatting, first apply the "None" table style, then use "Convert to Range".\
\
Was this page helpful? Yes No Report a problem\
\
Cancel Submit\
\
![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)\
\
Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)\
\
### Dave Bruns\
\
Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.\
\
Related Information\
-------------------\
\
### Training\
\
*   [Excel Tables](https://exceljet.net/training/excel-tables)\
    \
\
Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!\
\
Thierry\
\
[More Testimonials](https://exceljet.net/feedback)\
\
Get [Training](https://exceljet.net/training)\
\
----------------------------------------------\
\
### Quick, clean, and to the point training\
\
Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.\
\
[View Paid Training & Bundles](https://exceljet.net/training)\
\
[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)\
\
[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)\
\
[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)\
\
[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)\
\
[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)\
\
[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)
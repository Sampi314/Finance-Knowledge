# Basic inventory formula example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-inventory-formula-example

---

[Skip to main content](https://exceljet.net/formulas/basic-inventory-formula-example#main-content)

[](https://exceljet.net/formulas/basic-inventory-formula-example#)

*   [Previous](https://exceljet.net/formulas/average-last-n-values-in-a-table)
    
*   [Next](https://exceljet.net/formulas/count-table-columns)
    

[Tables](https://exceljet.net/formulas#Tables)

Basic inventory formula example
===============================

by Dave Bruns · Updated 10 Jul 2022

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Basic inventory formula example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20inventory%20formula%20example.png "Excel formula: Basic inventory formula example")

Summary
-------

To calculate current stock, or inventory, you can use Excel Tables with a formula based on the SUMIF function. In the example shown, the formula in K7 is:

    =SUMIFS(In[Qty],In[Color],J7)-SUMIFS(Out[Qty],Out[Color],J7)
    

Where "In" is the [Excel Table](https://exceljet.net/glossary/excel-table)
 on the left, "Out" is the table in the middle.

Generic formula
---------------

    =SUMIFS(In[Qty],In[Color],A1)-SUMIFS(Out[Qty],Out[Color],A1)

Explanation 
------------

This formula demonstrates a very simple inventory concept where current inventory is simply the result of all incoming stock minus all outgoing stock. In the example, colors are treated as unique item identifiers – imagine a product available in one size only in just three colors: red, blue, or green.

The key to this approach is to use [Excel Tables](https://exceljet.net/glossary/excel-table)
, because Table ranges automatically expand to handle changes in data. This means we can get a total of all incoming red items with:

    =SUMIFS(In[Qty],In[Color],J7)
    

And a total of all outgoing red items with:

    =SUMIFS(Out[Qty],Out[Color],J7)
    

In both cases, the SUMIFS function generates a total for all red items in each table.

Then, as long as both tables are up to date and complete, we can get the current inventory of red items with the following formula:

    =SUMIFS(In[Qty],In[Color],J7)-SUMIFS(Out[Qty],Out[Color],J7)
    

As the formula is copied down, we get current inventory for each color.

Related formulas
----------------

[![Excel formula: Subtotal by color](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/subtotal%20by%20color_0.png "Excel formula: Subtotal by color")](https://exceljet.net/formulas/subtotal-by-color)

### [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)

In this example, the goal is to subtotal (count and sum) values based on cell color. This is a tricky problem, because there is no Excel function that will let you count cells by color directly. There are several different approaches, as explained below. Standard formula logic If color is being...

[![Excel formula: SUMIFS with Excel Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20with%20Excel%20Table.png "Excel formula: SUMIFS with Excel Table")](https://exceljet.net/formulas/sumifs-with-excel-table)

### [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)

This formula uses structured references to feed table ranges into the SUMIFS function. The sum range is provided as Table1\[Total\] , the criteria range is provided as Table1\[Item\] , and criteria comes from values in column I. The formula in I5 is: =SUMIFS(Table1\[Total\],Table1\[Item\],H5) which...

[![Excel formula: Count sold and remaining](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20sold%20and%20remaining.png "Excel formula: Count sold and remaining")](https://exceljet.net/formulas/count-sold-and-remaining)

### [Count sold and remaining](https://exceljet.net/formulas/count-sold-and-remaining)

In this example, the goal is to count the number of items sold and remaining, based on the data visible in columns B and C. The ID column holds unique ids, and the Sold column is used to record a sale. An "x" in the Sold column indicates the item has been sold. As is typical in Excel, there are...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Introduction%20to%20structured%20references_thumb.png)](https://exceljet.net/videos/introduction-to-structured-references)

### [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)

In this video, I'll give a brief introduction to structured references. A structured reference is a term for using a table name in a formula instead of a normal cell reference. Structured references are optional, and can be used with formulas both inside or outside an Excel table. Let's take a look...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20SUMIFS%20with%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

### [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

In this video, we'll look at how to use the SUMIFS function with an Excel Table. On this worksheet, I have two identical sets of order data. I'm going to walk through the process of constructing a summary of sales by item for both sets of data. With the data on the left, I'll use standard formulas...

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

*   [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)
    
*   [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)
    
*   [Count sold and remaining](https://exceljet.net/formulas/count-sold-and-remaining)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Videos

*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
    
*   [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    

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
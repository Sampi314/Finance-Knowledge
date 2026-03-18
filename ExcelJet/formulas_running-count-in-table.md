# Running count in Table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/running-count-in-table

---

[Skip to main content](https://exceljet.net/formulas/running-count-in-table#main-content)

[](https://exceljet.net/formulas/running-count-in-table#)

*   [Previous](https://exceljet.net/formulas/percentile-if-in-table)
    
*   [Next](https://exceljet.net/formulas/running-total-in-table)
    

[Tables](https://exceljet.net/formulas#Tables)

Running count in Table
======================

by Dave Bruns · Updated 2 Aug 2022

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Running count in Table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/running%20count%20in%20excel%20table.png "Excel formula: Running count in Table")

Summary
-------

To create a running count in an [Excel Table](https://exceljet.net/glossary/excel-table)
, you can use the [INDEX function](https://exceljet.net/functions/index-function)
 with a [structured reference](https://exceljet.net/glossary/structured-reference)
 to create an expanding range. In the example shown, the formula in F5 is:

    =[@Color]&" - "&SUM(--(INDEX([Color],1):[@Color]=[@Color]))
    

When copied down the column, this formula will return a running count for each color in the Color column.

_In some versions of Excel, this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Explanation 
------------

At the core, this formula uses INDEX to create an expanding reference like this:

    INDEX([Color],1):[@Color] // expanding range
    

On the left side of the colon (:), the INDEX function returns a reference to the _first cell_ in the column.

    INDEX([Color],1) // first cell in color
    

This works because, the INDEX function returns a _reference_ to the first cell, not the actual value. On the _right_ side of the colon, we get a reference to the _current row_ of the color column like this:

    [@Color] // current row of Color
    

This is the standard structured reference syntax for "this row". Joined with the colon, these two references create a range that expands as the formula is copied down the table. So, we swap these references into the SUM function, we have:

    SUM(--(B5:B5=[@Color])) // first row
    SUM(--(B5:B11=[@Color])) // last row
    

Each of the expressions above generates an array of TRUE/FALSE values, and the double negative (--) is used to [convert these values to 1s and 0s](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
. So, in the last row, we end up with:

    SUM({0;0;0;1;0;0;0;0;1;0;1}) // returns 3
    

The rest of the formula simply [concatenates](https://exceljet.net/glossary/concatenation)
 the color from the current row to the count returned by SUM:

    =[@Color]&" - "&3
    ="Gold"&" - "&3
    ="Gold - 3"
    

### Simple expanding range?

Why not use a simple [expanding range](https://exceljet.net/glossary/expanding-reference)
 like this?

    SUM(--($B$5:B5=[@Color]))
    

For some reason, this kind of mixed reference becomes corrupted in an Excel Table as rows are added. Using INDEX with a structured reference solves the problem.

Related formulas
----------------

[![Excel formula: Running total in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20total%20in%20table2.png "Excel formula: Running total in Table")](https://exceljet.net/formulas/running-total-in-table)

### [Running total in Table](https://exceljet.net/formulas/running-total-in-table)

At the core, this formula has a simple pattern like this: =SUM(first:current) Where "first" is the first cell in the Total column, and "current" is a reference to a cell in the current row of the Total column. To get the a reference to the first cell, we use INDEX like this: INDEX(\[Total\],1) Here,...

[![Excel formula: Two-way lookup VLOOKUP in a Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20lookup%20VLOOKUP%20in%20a%20Table.png "Excel formula: Two-way lookup VLOOKUP in a Table")](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)

### [Two-way lookup VLOOKUP in a Table](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)

At a high level, we use VLOOKUP to extract employee information in 4 columns with ID as the lookup value: =VLOOKUP($I$4,Table1,MATCH(H5,Table1\[#Headers\],0),0) The ID value comes from cell I4, and is locked so that it won't change as the formula is copied down the column. The table array is Table1,...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

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

*   [Running total in Table](https://exceljet.net/formulas/running-total-in-table)
    
*   [Two-way lookup VLOOKUP in a Table](https://exceljet.net/formulas/two-way-lookup-vlookup-in-a-table)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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
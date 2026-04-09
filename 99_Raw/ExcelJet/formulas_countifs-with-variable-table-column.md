# COUNTIFS with variable table column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/countifs-with-variable-table-column

---

[Skip to main content](https://exceljet.net/formulas/countifs-with-variable-table-column#main-content)

[](https://exceljet.net/formulas/countifs-with-variable-table-column#)

*   [Previous](https://exceljet.net/formulas/count-table-rows)
    
*   [Next](https://exceljet.net/formulas/dynamic-reference-to-table)
    

[Tables](https://exceljet.net/formulas#Tables)

COUNTIFS with variable table column
===================================

by Dave Bruns · Updated 25 Jun 2018

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: COUNTIFS with variable table column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/COUNTIFS%20with%20variable%20table%20column.png "Excel formula: COUNTIFS with variable table column")

Summary
-------

To use COUNTIFS with a variable table column, you can use INDEX and MATCH to find and retrieve the column for COUNTIFS. In the example shown, the formula in H5 is:

    =COUNTIFS(INDEX(Table1,0,MATCH(G5,Table1[#Headers],0)),"x")
    

Generic formula
---------------

    =COUNTIFS(INDEX(Table,0,MATCH(name,Table[#Headers],0)),criteria))

Explanation 
------------

First, for context, it's important to note that you can use COUNTIFS with a regular structured reference like this:

    =COUNTIFS(Table1[Swim],"x")
    

This is a much simpler formula, but you can't copy it down column H, because the column reference won't change.

The example on this page therefore is meant to show one way to set up a formula that references a table with a variable column reference.

Working from the inside out, the MATCH function is used to find the position of the column name listed in column G:

    MATCH(G5,Table1[#Headers],0)
    

MATCH uses the value in G5 as lookup value, the headers in Table1 for array, and 0 for match type to force an exact match. The result for G5 is 2, which goes into INDEX as the column number:

    INDEX(Table1,0,2,0))
    

Notice row number has been set to zero, which causes INDEX to return the entire column, which is C5:C13 in this example.

This reference goes into COUNTIFS normally:

    =COUNTIFS(C5:C13,"x")
    

COUNTIFS counts cells that contain "x", and returns the result, 5 in this case.

When the formula is copied down column H, INDEX and MATCH return the correct column reference to COUNTIFS at each row.

### Alternative with INDIRECT

The INDIRECT function can also be used to set up a variable column reference like this:

    =COUNTIFS(INDIRECT("Table1["&G5&"]"),"x")
    

Here, the structured reference is assembled as text, and INDIRECT evaluates the text as a proper cell reference.

_Note: INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems in larger or more complicated workbooks._

Related formulas
----------------

[![Excel formula: SUMIFS with Excel Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20with%20Excel%20Table.png "Excel formula: SUMIFS with Excel Table")](https://exceljet.net/formulas/sumifs-with-excel-table)

### [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)

This formula uses structured references to feed table ranges into the SUMIFS function. The sum range is provided as Table1\[Total\] , the criteria range is provided as Table1\[Item\] , and criteria comes from values in column I. The formula in I5 is: =SUMIFS(Table1\[Total\],Table1\[Item\],H5) which...

[![Excel formula: Look up entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20column.png "Excel formula: Look up entire column")](https://exceljet.net/formulas/look-up-entire-column)

### [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)

In this example, the goal is to look up and retrieve an entire column of values in a set of data. For example, when a value like "Q3" is entered into cell H4, all values in the range E5:E16 should be returned. For convenience and readability, quarter (C4:F4) and data (C5:F16) are named ranges ...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)
    
*   [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

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
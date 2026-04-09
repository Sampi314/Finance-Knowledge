# Search multiple worksheets for value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/search-multiple-worksheets-for-value

---

[Skip to main content](https://exceljet.net/formulas/search-multiple-worksheets-for-value#main-content)

[](https://exceljet.net/formulas/search-multiple-worksheets-for-value#)

*   [Previous](https://exceljet.net/formulas/search-entire-worksheet-for-value)
    
*   [Next](https://exceljet.net/formulas/send-email-with-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Search multiple worksheets for value
====================================

by Dave Bruns · Updated 19 Dec 2019

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Search multiple worksheets for value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/search%20multiple%20worksheets%20for%20value.png "Excel formula: Search multiple worksheets for value")

Summary
-------

To search multiple worksheets in a workbook for a value and return a count, you can use a formula based on the [COUNTIF](https://exceljet.net/functions/countif-function)
 and [INDIRECT](https://exceljet.net/functions/indirect-function)
 functions. With some preliminary setup, you can use this approach to search an entire workbook for a specific value. In the example shown, the formula in C5 is:

    =COUNTIF(INDIRECT("'"&B7&"'!"&"1:1048576"),$C$4)
    

### Context - sample data

The workbook contains 4 worksheets total. **Sheet1**, **Sheet2**, and **Sheet3** each contain 1000 random first names that look like this:

![Sample data  - search entire workbook or multiple sheets](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/search%20multiple%20worksheets%20sample%20data.png?itok=Z89QZCK_ "Sample data - search entire workbook or multiple sheets")

Generic formula
---------------

    =COUNTIF(INDIRECT("'"&sheetname&"'!"&"range"),criteria)

Explanation 
------------

The range B7:B9 contains the sheet names we want to include in the search. These are just text strings, and we need to do some work to get them to be recognized as valid sheet references.

Working from the inside out, this expression is used to build a full sheet reference:

    "'"&B7&"'!"&"1:1048576"
    

The single quotes are added to allow sheet names with spaces, and the exclamation mark is a standard syntax for ranges that include a sheet name. The text "1:1048576" is a range that includes every row in the worksheet.

After B7 is evaluated, and values are concatenated, the expression above returns:

    "'Sheet1'!1:1048576"
    

which goes into the [INDIRECT function](https://exceljet.net/functions/indirect-function)
 as the 'ref\_text' argument. INDIRECT evaluates this text and returns a standard reference to every cell in **Sheet1**. This goes into the COUNTIF function as the range. The criteria is provided as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to C4 (locked so the formula can be copied down column C).

COUNTIF then returns a count of all cells with a value equal to "mary", 25 in this case.

_Note: COUNTIF is not case-sensitive._

### Contains vs. Equals

If you want to count all cells that _contain_ the value in C4, instead of all cells _equal_ to C4, you can add [wildcards](https://exceljet.net/glossary/wildcard)
 to the criteria like this:

    =COUNTIF(INDIRECT("'"&B7&"'!"&"1:1048576"),"*"&C4&"*")
    

Now COUNTIF will count cells with the substring "John" anywhere in the cell.

### Performance

In general, it's not a good practice to specify a range that includes all worksheet cells. Doing so can cause performance problems, since the range includes millions and millions of cells. In this example, the problem is compounded, since the formula uses the INDIRECT function, which is a [volatile function](https://exceljet.net/glossary/volatile-function)
. Volatile functions recalculate on every worksheet change, so the impact on performance can be huge.

When possible, restrict ranges to a sensible size. For example, if you know data won't appear past row 1000, you can search just the first 1000 rows like this:

    =COUNTIF(INDIRECT("'"&B7&"'!"&"1:1000"),$C$4)
    

Related formulas
----------------

[![Excel formula: Search entire worksheet for value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Search%20entire%20worksheet%20for%20value.png "Excel formula: Search entire worksheet for value")](https://exceljet.net/formulas/search-entire-worksheet-for-value)

### [Search entire worksheet for value](https://exceljet.net/formulas/search-entire-worksheet-for-value)

The second sheet in the workbook, Sheet2, contains 1000 first names in the range B4:F203. The COUNTIF function takes a range and a criteria. In this case, we give COUNTIF a range equal to all rows in Sheet2. Sheet2!1:1048576 Note: an easy way to enter this range is to use the Select All button ...

[![Excel formula: Count occurrences in entire workbook](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20occurrences%20in%20entire%20workbook.png "Excel formula: Count occurrences in entire workbook")](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)

### [Count occurrences in entire workbook](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)

In this example, the goal is to count the value in cell B5 ("Steven") in the sheets listed in B11:B13. The workbook shown in the example has four worksheets in total. The first sheet is named "Master" and contains the search string, the range, and the sheets to include in the count, as seen in the...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

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

*   [Search entire worksheet for value](https://exceljet.net/formulas/search-entire-worksheet-for-value)
    
*   [Count occurrences in entire workbook](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

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
# Search entire worksheet for value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/search-entire-worksheet-for-value

---

[Skip to main content](https://exceljet.net/formulas/search-entire-worksheet-for-value#main-content)

[](https://exceljet.net/formulas/search-entire-worksheet-for-value#)

*   [Previous](https://exceljet.net/formulas/score-quiz-answers-with-key)
    
*   [Next](https://exceljet.net/formulas/search-multiple-worksheets-for-value)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Search entire worksheet for value
=================================

by Dave Bruns · Updated 23 Nov 2016

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Search entire worksheet for value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Search%20entire%20worksheet%20for%20value.png "Excel formula: Search entire worksheet for value")

Summary
-------

To search an entire worksheet for a value and return a count, you can use a formula based on the COUNTIF function.

In the example shown, the formula in C5 is:

    =COUNTIF(Sheet2!1:1048576,C4)
    

Generic formula
---------------

    =COUNTIF(Sheet2!1:1048576,"apple")

Explanation 
------------

The second sheet in the workbook, Sheet2, contains 1000 first names in the range B4:F203.

![1000 first names on Sheet2](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/Search%20entire%20worksheet%20for%20value%201000%20first%20names.png?itok=B4keGDEm "1000 first names on Sheet2")

The COUNTIF function takes a range and a criteria. In this case, we give COUNTIF a range equal to all rows in Sheet2.

    Sheet2!1:1048576
    

_Note: an easy way to enter this range is to use the [Select All button](https://exceljet.net/glossary/select-all-button)
._

For criteria, we use a reference to C4, which contains "John". COUNTIF then returns 15, since there are 15 cells in Sheet2 equal to "John".

### Contains vs. Equals

If you want to count all cells that contain the value in C4, instead of all cells equal to C4, add the wildcards to the criteria like this:

    =COUNTIF(Sheet2!1:1048576,"*"&C4&"*")
    

Now COUNTIF will count cells with the substring "John" anywhere in the cell.

### Performance

In general, it's not a good practice to specify a range that includes all worksheet cells. Doing so can cause major performance problems, since the range includes millions and millions of cells. When possible, restrict the range to a sensible area.

Related formulas
----------------

[![Excel formula: Search multiple worksheets for value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/search%20multiple%20worksheets%20for%20value.png "Excel formula: Search multiple worksheets for value")](https://exceljet.net/formulas/search-multiple-worksheets-for-value)

### [Search multiple worksheets for value](https://exceljet.net/formulas/search-multiple-worksheets-for-value)

The range B7:B9 contains the sheet names we want to include in the search. These are just text strings, and we need to do some work to get them to be recognized as valid sheet references. Working from the inside out, this expression is used to build a full sheet reference: "'"...

[![Excel formula: Count occurrences in entire workbook](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20occurrences%20in%20entire%20workbook.png "Excel formula: Count occurrences in entire workbook")](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)

### [Count occurrences in entire workbook](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)

In this example, the goal is to count the value in cell B5 ("Steven") in the sheets listed in B11:B13. The workbook shown in the example has four worksheets in total. The first sheet is named "Master" and contains the search string, the range, and the sheets to include in the count, as seen in the...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Search multiple worksheets for value](https://exceljet.net/formulas/search-multiple-worksheets-for-value)
    
*   [Count occurrences in entire workbook](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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
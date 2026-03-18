# XLOOKUP binary search - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-binary-search

---

[Skip to main content](https://exceljet.net/formulas/xlookup-binary-search#main-content)

[](https://exceljet.net/formulas/xlookup-binary-search#)

*   [Previous](https://exceljet.net/formulas/xlookup-basic-exact-match)
    
*   [Next](https://exceljet.net/formulas/xlookup-case-sensitive)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP binary search
=====================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7816/download?token=pW_pagfD)
 (14.18 MB)

![Excel formula: XLOOKUP binary search](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP_binary_search.png "Excel formula: XLOOKUP binary search")

Summary
-------

With large sets of data, [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 can take a long time to calculate. If the source data is sorted by lookup value, one way to speed up calculation time considerably is to enable XLOOKUP's binary search feature. In the example shown, the formula in F5 is:

    =XLOOKUP(E5,data[Invoice],data[Amount],"",0,2)

where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 that contains 1 million invoice numbers and amounts. Because the data is sorted by invoice number, XLOOKUP will calculate results very quickly.

_Note: the attached worksheet is large (about 14 MB) because it contains 1 million rows of data._

Generic formula
---------------

    =XLOOKUP(A1,range1,range2,,0,2)

Explanation 
------------

In this example, the goal is to look up amounts for 1000 invoice numbers in a table that contains 1 million invoices. The catch is that not all of the 1000 invoice numbers exist in the source data. In fact, _most of the invoice numbers do not appear in column B_. This means we need to take care to configure XLOOKUP to use an _exact match_, and exact match lookups on large data sets can be painfully slow. However, because the data is sorted by invoice number, we can enable XLOOKUP's binary search mode, which is optimized for speed. The result is a much faster formula.

### XLOOKUP exact match mode

When you use XLOOKUP in "exact match mode" on a large set of data, it can slow down the calculation time in a worksheet. The general form for an exact match lookup with XLOOKUP looks like this:

    =XLOOKUP(A1,lookup_array,return_array,,0) // exact match
    

The 0 for _match\_mode_ specifies an exact match. The reason XLOOKUP is slow in this mode is that there is _no requirement_ that the lookup values be sorted. As a result, XLOOKUP must check every record in the data set until a match is found, or not. This is sometimes referred to as a _linear search_.

### XLOOKUP binary search mode

To enable binary search mode with XLOOKUP, data must be sorted in ascending or descending order. If values are sorted in _ascending order_, use the value 2 to enable binary search. If values are sorted in _descending order_, use the value -2:

    =XLOOKUP(A1,lookup_array,return_array,,0,2) // exact match binary A-Z
    =XLOOKUP(A1,lookup_array,return_array,,0,-2) // exact match binary Z-A
    

Note in the formulas above, we are not providing a value for the _if\_not\_found_ argument. This means XLOOKUP will simply return a #N/A error if a value is not found, like other lookup formulas. With binary search enabled, XLOOKUP will run very fast.

_For a complete XLOOKUP overview with many examples, see [How to use XLOOKUP](https://exceljet.net/functions/xlookup-function)
._

### The solution

In the worksheet shown, the goal is to look up each of the 1000 invoice numbers that appear in column E. If we find the invoice number in the Excel Table named **data**, we want to return the amount. If we don't find the invoice number, we don't want to show anything. To solve this problem, we use a formula like this in cell D5:

    =XLOOKUP(E5,data[Invoice],data[Amount],"",0,2)

For the _if\_not\_found_ argument, we provide an [empty string](https://exceljet.net/glossary/empty-string)
 (""). To require an exact match, we use 0 for _match\_mode_. To enable XLOOKUP'S binary search mode, we use 2 for _search\_mode_. As the formula is copied down column E, it returns the amount for invoice numbers that exist, and an [empty string](https://exceljet.net/glossary/empty-string)
 ("") if the invoice number is not found. XLOOKUP returns results very quickly because binary search mode is enabled and data is sorted by invoice number in ascending order.

### INDEX and XMATCH option

Because the [XMATCH function](https://exceljet.net/functions/xmatch-function)
 has a binary search option, it is possible to write an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula that also calculates very quickly. Like XLOOKUP, the _search\_mode_ argument must be 2:

    =INDEX(data[Amount],XMATCH(E5,data[Invoice],0,2))

Unlike XLOOKUP, there is no built-in option to handle errors, so you would need to wrap the formula above in [IFERROR](https://exceljet.net/functions/iferror-function)
 or [IFNA](https://exceljet.net/functions/ifna-function)
 to trap #N/A errors and return an empty string.

### Notes

1.  _This approach is overkill unless lookup_ _performance is an issue._
2.  _VLOOKUP does not have a binary search mode, [but there is a workaround](https://exceljet.net/formulas/vlookup-faster-vlookup)
    ._
3.  _See [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
     for a detailed comparison._

Related formulas
----------------

[![Excel formula: VLOOKUP faster VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_faster_VLOOKUP.png "Excel formula: VLOOKUP faster VLOOKUP")](https://exceljet.net/formulas/vlookup-faster-vlookup)

### [VLOOKUP faster VLOOKUP](https://exceljet.net/formulas/vlookup-faster-vlookup)

In this example, VLOOKUP is configured to look up 1000 invoice numbers in a table that contains 1 million invoices. The catch is that not all of the 1000 invoice numbers exist in the source data. In fact, most of the invoice numbers do not appear in column B . This means we need to configure...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP faster VLOOKUP](https://exceljet.net/formulas/vlookup-faster-vlookup)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    

### Articles

*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
    
*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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
# Flag first duplicate in a list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/flag-first-duplicate-in-a-list

---

[Skip to main content](https://exceljet.net/formulas/flag-first-duplicate-in-a-list#main-content)

[](https://exceljet.net/formulas/flag-first-duplicate-in-a-list#)

*   [Previous](https://exceljet.net/formulas/fixed-value-every-n-columns)
    
*   [Next](https://exceljet.net/formulas/flip-table-rows-to-columns)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Flag first duplicate in a list
==============================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Flag first duplicate in a list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/flag%20first%20duplicate%20in%20a%20list.png "Excel formula: Flag first duplicate in a list")

Summary
-------

To mark the first duplicate in a list, you can use a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
. Optionally, you can flag subsequent duplicates with a different marker. In the example shown the formula in cell C4 is:

    =IF(COUNTIF($B$4:$B$11,B4)>1,IF(COUNTIF($B$4:B4,B4)=1,"x","xx"),"")
    

This formula has been copied down the column, from C4 to C11.

Generic formula
---------------

    =IF(COUNTIF(A:A,A1)>1,IF(COUNTIF(A$1:A1,A1)=1,"x","xx"),"")

Explanation 
------------

At the core, this formula is composed of two sets of the [COUNTIF function](https://exceljet.net/functions/countif-function)
 wrapped in the [IF function](https://exceljet.net/functions/if-function)
. The outer IF + COUNTIF first checks to see if the value in question (B4) appears more than once in the list:

    =IF(COUNTIF($B$4:$B$11,B4)>1
    

If not, the outer IF function returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("") as a final result. If the value does appear more than once, we run another IF + COUNTIF combo. This one does the work of flagging duplicates:

    IF(COUNTIF($B$4:B4,B4)=1,"x","xx")
    

This part of the formula uses an [expanding reference](https://exceljet.net/glossary/expanding-reference)
 ($B$4:B4) that expands as the formula is copied down the column. The first B4 in the range is [absolute](https://exceljet.net/glossary/absolute-reference)
 (locked), and the second is relative, so it changes as the formula is copied down the list.

Remember that this part of the formula is only executed if the first COUNTIF returns a number greater than 1. So, at each row, the formula checks the count inside the range up to the current row. If the count is 1, we mark the duplicate with "x", since it's the first one we've seen. If it's not 1, we know it must be a subsequent duplicate, and we mark it with "xx"

### Basic formula

To flag the first duplicate in a list only with a 0 or 1, you can use this stripped-down formula, which uses an expanding range and the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
.

    =(COUNTIFS($B$5:B5,B5)=2)+0
    

This formula will return 1 only when a value has been encountered twice – the first occurrence will return zero:

![Flag duplicates simple formula](https://exceljet.net/sites/default/files/images/formulas/inline/flag%20duplicate%20simple.png "Flag duplicates simple formula")

To flag the second and all subsequent occurrences, the formula in F5 above is:

    =(COUNTIFS($E$5:E5,E5)>=2)+0
    

_Note: In both examples, adding zero is just a simple way to coerce TRUE and FALSE values to 1 and 0._

Also, using COUNTIFS instead of COUNTIF makes it possible to evaluate values in other columns as part of the test for duplicates. Each additional column also needs to be entered as an expanding range.

Related formulas
----------------

[![Excel formula: Highlight duplicate values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20duplicate%20values.png "Excel formula: Highlight duplicate values")](https://exceljet.net/formulas/highlight-duplicate-values)

### [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)

COUNTIF simply counts the number of times each value appears in the range. When the count is more than 1, the formula returns TRUE and triggers the rule. When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the...

[![Excel formula: Range contains duplicates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/range%20contains%20duplicates.png "Excel formula: Range contains duplicates")](https://exceljet.net/formulas/range-contains-duplicates)

### [Range contains duplicates](https://exceljet.net/formulas/range-contains-duplicates)

In this example, the goal is to test if a given range contains duplicate values and return TRUE if duplicates exist and FALSE if not. This is essentially a counting problem and the solution is based on the COUNTIF function , which counts values in a range that meet supplied criteria. The formula...

[![Excel formula: Customer is new](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/customer%20is%20new..png "Excel formula: Customer is new")](https://exceljet.net/formulas/customer-is-new)

### [Customer is new](https://exceljet.net/formulas/customer-is-new)

This formula uses an expanding range for the criteria range inside COUNTIFS: COUNTIFS($B$5:B5,B5) Because the first reference is absolute and the second reference is relative, the range expands as the formula is copied down the column. The criteria is simply the value in the current row of column B...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Compare%20two%20lists%20and%20highlight%20differences-Thumb.png)](https://exceljet.net/videos/how-to-compare-two-lists-and-highlight-differences)

### [How to compare two lists and highlight differences](https://exceljet.net/videos/how-to-compare-two-lists-and-highlight-differences)

In this video, we'll look at how to compare two lists using conditional formatting. This is a great way to visually highlight missing items in a list. Here we have two lists. Both lists contain the same number of items, but each list is slightly different. We can use conditional formatting with a...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)
    
*   [Range contains duplicates](https://exceljet.net/formulas/range-contains-duplicates)
    
*   [Customer is new](https://exceljet.net/formulas/customer-is-new)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Videos

*   [How to compare two lists and highlight differences](https://exceljet.net/videos/how-to-compare-two-lists-and-highlight-differences)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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
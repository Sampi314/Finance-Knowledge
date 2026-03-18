# Count cells that end with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-end-with

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-end-with#main-content)

[](https://exceljet.net/formulas/count-cells-that-end-with#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)
    
*   [Next](https://exceljet.net/formulas/count-columns-that-contain-specific-values)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that end with
=========================

by Dave Bruns · Updated 26 May 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count cells that end with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20end%20with.png "Excel formula: Count cells that end with")

Summary
-------

To count the number of cells that end with specific text, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with a wildcard. In the example shown, the formula in cell E5 is:

    =COUNTIF(data,D5)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. COUNTIF returns 3, since there are three cells that end with "R". Note that COUNTIF is _not_ case-sensitive. 

Generic formula
---------------

    =COUNTIF(range,"*text")

Explanation 
------------

In this example, the goal is to count cells in the range B5:B16 that end with specific text, which is provided in column D. For convenience, the range B5:B16 is named **data**. 

### COUNTIF function

The simplest way to solve this problem is with the COUNTIF function and a wildcard. [COUNTIF supports three wildcards](https://exceljet.net/functions/countifs-function)
 that can be used in the _criteria_ [argument](https://exceljet.net/glossary/function-argument)
: question mark (?), asterisk(\*), or tilde (~). A question mark (?) matches any one character and an asterisk (\*) matches zero or more characters of any kind. The tilde (~) is an escape character to match _literal_ wildcards that may appear in data. In this example, we mainly use an asterisk (\*). To count cells in a range that _end with_ "apple" you can use a formula like this:

    =COUNTIF(range,"*apple) // end with "apple"
    

In the worksheet shown, we use the criteria in column D directly like this:

    =COUNTIF(data,D5)
    

As the formula is copied down, COUNTIF returns the count of cells in **data** (B5:B16) that end with the text seen in D5:D8, which already includes the [wildcard](https://exceljet.net/glossary/wildcard)
(s) needed. Notice that COUNTIF is _not_ case-sensitive. Cell D6 contains a lowercase "y", yet COUNTIFS happily matches the uppercase "Y"s in B5:B16.

Below are the formulas in the worksheet, altered to include the criteria from column D directly:

    =COUNTIF(data,"*R") // returns 3
    =COUNTIF(data,"*y") // returns 2
    =COUNTIF(data,"*002??-?") // returns 5
    =COUNTIF(data,"*-?") // returns 12
    

Notice the last two formulas use both question mark (?) and asterisk (\*) wildcards. The ? wildcard matches any one character, so you can use it to create criteria that is more specific than with just the \* wildcard. Notice the hyphen (-) is hardcoded to make the pattern even more specific.

Related formulas
----------------

[![Excel formula: Count cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20begin%20with.png "Excel formula: Count cells that begin with")](https://exceljet.net/formulas/count-cells-that-begin-with)

### [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)

In this example, the goal is to count cells in the range B5:B16 that begin with specific text, which is provided in column D. For convenience, the range B5:B16 is named data . COUNTIF function The simplest way to solve this problem is with the COUNTIF function and a wildcard. COUNTIF supports three...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

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

*   [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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
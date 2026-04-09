# Count cells less than - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-less-than

---

[Skip to main content](https://exceljet.net/formulas/count-cells-less-than#main-content)

[](https://exceljet.net/formulas/count-cells-less-than#)

*   [Previous](https://exceljet.net/formulas/count-cells-greater-than)
    
*   [Next](https://exceljet.net/formulas/count-cells-not-between-two-numbers)
    

[Count](https://exceljet.net/formulas#Count)

Count cells less than
=====================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Count cells less than](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20less%20than.png "Excel formula: Count cells less than")

Summary
-------

To count cells that contain values less than a given number, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the generic form of the formula, **range** is the range of cells to count, and **x** is the number below which you want to count. In the example shown, cell F5 contains this formula:

    =COUNTIF(C5:C16,"<75")
    

COUNTIF returns 1, since there is one cell in C5:C16 with a value less than 75.

Generic formula
---------------

    =COUNTIF(rng,"<x")

Explanation 
------------

In this example, the goal is to count test scores in column C that are less than 75. The simplest way to do this is with the [COUNTIF function](https://exceljet.net/functions/countif-function)
, which takes two [arguments](https://exceljet.net/glossary/function-argument)
, _range_ and _criteria_:

    =COUNTIF(range,criteria)
    

The test scores in the [range](https://exceljet.net/glossary/range)
 C5:C16 and we want to count scores _less than 75_, so we configure COUNTIF like this:

    =COUNTIF(C5:C16,"<75") // returns 1
    

Since there is only one score in C5:C16 that is less than 75, COUNTIF returns 1 as a result. Notice that _criteria_ is given as a text value in double quotes (""). This is a requirement of the COUNTIF function which is in a [group of eight functions](https://exceljet.net/articles/excels-racon-functions)
 that use a special syntax for _criteria_. In this syntax, [logical operators](https://exceljet.net/glossary/logical-operators)
 are joined with numeric values and provided as text.

### Less than or equal to

To count cells that are _less than or equal to_, adjust the formula to use "<=" instead of "<". In the example shown, the formula in F6 is:

    =COUNTIF(C5:C16,"<=75") // returns 2
    

Here, COUNTIF returns 2 since there are two scores in C5:C16 less than or equal to 75.

### Value in another cell

To adjust the formula to use a value in another cell as part of the criteria, you can [concatenate](https://exceljet.net/glossary/concatenation)
 the logical operator to the cell reference with the ampersand (&) [operator](https://exceljet.net/glossary/math-operators)
 like this:

    =COUNTIF(range,"<"&A1)
    

For example, with 75 in cell A1, the criteria will be "<=75" after concatenation:

    =COUNTIF(range,"<="&A1)
    =COUNTIF(range,"<=75")
    =2
    

The result will again be 2. If the value in A1 is changed to a different number, COUNTIF will return a new result.

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 is designed to [handle multiple criteria](https://exceljet.net/formulas/count-cells-between-two-numbers)
, but can be used just like the COUNTIF function in this example:

    =COUNTIFS(C5:C16,"<75") // returns 1
    =COUNTIFS(C5:C16,"<=75") // returns 2
    

Video: [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

Related formulas
----------------

[![Excel formula: Count cells greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20greater%20than.png "Excel formula: Count cells greater than")](https://exceljet.net/formulas/count-cells-greater-than)

### [Count cells greater than](https://exceljet.net/formulas/count-cells-greater-than)

In this example, the goal is to count test scores in column C that are greater than 90. The simplest way to do this is with the COUNTIF function , which takes two arguments , range and criteria : =COUNTIF(range,criteria) All test scores are in the range C5:C16 and we want to count scores greater...

[![Excel formula: Count cells equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to.png "Excel formula: Count cells equal to")](https://exceljet.net/formulas/count-cells-equal-to)

### [Count cells equal to](https://exceljet.net/formulas/count-cells-equal-to)

In this example, the goal is to count cells equal to a specific value. In this case, we want to count cells that contain "red" in the range D5:D16. This problem can be solved with the COUNTIF function and the SUMPRODUCT function, as explained below. COUNTIF function One way to solve this problem is...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells greater than](https://exceljet.net/formulas/count-cells-greater-than)
    
*   [Count cells equal to](https://exceljet.net/formulas/count-cells-equal-to)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    
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
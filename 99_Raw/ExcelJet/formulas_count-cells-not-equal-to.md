# Count cells not equal to - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-not-equal-to

---

[Skip to main content](https://exceljet.net/formulas/count-cells-not-equal-to#main-content)

[](https://exceljet.net/formulas/count-cells-not-equal-to#)

*   [Previous](https://exceljet.net/formulas/count-cells-not-between-two-numbers)
    
*   [Next](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    

[Count](https://exceljet.net/formulas#Count)

Count cells not equal to
========================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Count cells not equal to](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20not%20equal%20to.png "Excel formula: Count cells not equal to")

Summary
-------

To count the number of cells that are _not equal_ to a given value, you can use the [COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
. In the generic form of the formula, **range** represents a range of cells, and **x** represents the value you _don't want to count_. All other values will be counted. In the example shown, G5 contains this formula:

    =COUNTIF(D5:D16,"<>red")
    

COUNTIF returns 9, since nine cells in D5:D16 are not equal to "red".

Generic formula
---------------

    =COUNTIF(range,"<>x")

Explanation 
------------

In this example, the goal is to count the number of cells in column D that are _not equal_ to a given color. The simplest way to do this is with the [COUNTIF function](https://exceljet.net/functions/countif-function)
, as explained below.

### Not equal to

In Excel, the [operator](https://exceljet.net/glossary/logical-operators)
 for not equal to is "<>". For example:

    =A1<>10 // A1 is not equal to 10
    =A1<>"apple" // A1 is not equal to "apple"
    

### COUNTIF function

The COUNTIF function counts the number of cells in a range that meet the supplied criteria:

    =COUNTIF(range,criteria)
    

To use the not equal to operator (<>) in COUNTIF, it must be enclosed in double quotes like this:

    =COUNTIF(range,"<>10") // not equal to 10
    =COUNTIF(range,"<>apple") // not equal to "apple"
    

This is a requirement of COUNTIF, which is in a [group of eight functions](https://exceljet.net/articles/excels-racon-functions)
 that share this syntax. In the example shown, we want to count cells not equal to "red" in D5:D16, so we use "<>red" for criteria. The formula in G5 is:

    =COUNTIF(D5:D16,"<>red") // returns 9
    

In cell G6, we count all cells not equal to blue with a similar formula:

    =COUNTIF(D5:D16,"<>blue") // returns 7
    

_Note: COUNTIF is not case-sensitive. The word "red" can appear in any combination of uppercase or lowercase letters._

### Not equal to another cell

To use a value in another cell as part of the criteria, use the ampersand (&) [operator](https://exceljet.net/glossary/math-operators)
 to [concatenate](https://exceljet.net/glossary/concatenation)
 like this:

    =COUNTIF(range,"<>"&A1)
    

For example, if A1 contains 100 the criteria will be "<>100" after concatenation, and COUNTIF will count cells not equal to 100:

    =COUNTIF(range,"<>100")
    

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 is designed to [handle multiple criteria](https://exceljet.net/formulas/count-cells-between-two-numbers)
, but can be used just like the COUNTIF function in this example:

    =COUNTIFS(D5:D16,"<>red") // returns 9
    =COUNTIFS(D5:D16,"<>blue") // returns 7
    

Video: [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

Related formulas
----------------

[![Excel formula: Count cells not equal to x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20x%20or%20y_1.png "Excel formula: Count cells not equal to x or y")](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

### [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

In this example, the goal is to count the number of cells in data (B5:B15) that are not equal to "red" or "blue". This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. Not equal to The not equal to operator in Excel is <>. For example, with the...

[![Excel formula: Count cells not equal to many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20many.png "Excel formula: Count cells not equal to many things")](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

### [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

First, a little context. Normally, if you have just a couple things you don't want to count, you can use COUNTIFS like this: =COUNTIFS(range,"<>apple",range,"<>orange") But this doesn't scale very well if you have a list of many things, because you'll have to add an additional range/...

[![Excel formula: Count cells equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to.png "Excel formula: Count cells equal to")](https://exceljet.net/formulas/count-cells-equal-to)

### [Count cells equal to](https://exceljet.net/formulas/count-cells-equal-to)

In this example, the goal is to count cells equal to a specific value. In this case, we want to count cells that contain "red" in the range D5:D16. This problem can be solved with the COUNTIF function and the SUMPRODUCT function, as explained below. COUNTIF function One way to solve this problem is...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

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

*   [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
    
*   [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    
*   [Count cells equal to](https://exceljet.net/formulas/count-cells-equal-to)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

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
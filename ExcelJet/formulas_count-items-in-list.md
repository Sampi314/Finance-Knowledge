# Count items in list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-items-in-list

---

[Skip to main content](https://exceljet.net/formulas/count-items-in-list#main-content)

[](https://exceljet.net/formulas/count-items-in-list#)

*   [Previous](https://exceljet.net/formulas/count-if-two-criteria-match)
    
*   [Next](https://exceljet.net/formulas/count-long-numbers)
    

[Count](https://exceljet.net/formulas#Count)

Count items in list
===================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Count items in list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20items%20in%20list.png "Excel formula: Count items in list")

Summary
-------

To create a count of the values that appear in a list or table, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in C5 is:

    =COUNTIFS(B:B,B5)
    

As the formula is copied down, it returns a count of each color in column B. This formula uses the [full column reference](https://exceljet.net/glossary/full-column-reference)
 B:B for convenience. You can also use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 like $B$5:$B$16. An [Excel Table](https://exceljet.net/articles/excel-tables)
 would also be a good option.

See also: [Running count of occurrence in list,](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
 and [Summary count with COUNTIFS](https://exceljet.net/formulas/summary-count-with-countif)

Generic formula
---------------

    =COUNTIFS(A:A,A1)

Explanation 
------------

In this example, the goal is to create a count of each color in column B. The simplest way to solve this problem is with the COUNTIFS function.

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 returns the count of cells that meet one or more criteria. COUNTIFS can be used with criteria based on dates, numbers, text, and other conditions. COUNTIFS supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. To configure COUNTIFS, conditions are supplied in _range/criteria_ pairs — each pair contains one range and the associated criteria for that range:

    =COUNTIFS(range1,criteria1,range2,criteria2,etc.)
    

In this example, we want to count each value in column B, starting with cell B5. To do this, we can use a formula like this in cell C5:

    =COUNTIFS(B:B,B5) // returns 4
    

The result in cell C5 is 4, since "Red" appears 4 times in column B. As the formula is copied down, it returns a count for each value in B5:B16. Note this formula uses the [full column reference](https://exceljet.net/glossary/full-column-reference)
 B:B for convenience. You can also use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 like this:

    =COUNTIFS($B$5:$B$16,B5) 
    

As an alternative, you could use an [Excel Table](https://exceljet.net/articles/excel-tables)
 to hold the data, and then use a [structured reference](https://exceljet.net/glossary/structured-reference)
.

### With two criteria

In the workbook below, we have Color and Price. By adding a second _range/criteria_ pair to COUNTIFS, we can count the _combination_ of Color and Price like this:

    =COUNTIFS(B:B,B5,C:C,C5)
    

 ![Count items in list with two criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20items%20in%20list%20with%20two%20criteria.png?itok=fM5SD3L- "Count items in list with two criteria")

Because both _range/criteria_ pairs appear in the same COUNTIFS function, they link the values in column B with those in column C, and COUNTIFS generates a count of each Color and Price combination that appears in the table. Notice these counts differ from the original example above because some of the same colors have different prices.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

### [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the named range value . The core of the solution explained below is the COUNTIF function , with help from the IF function to suppress a count for...

[![Excel formula: Calculate running total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20running%20total.png "Excel formula: Calculate running total")](https://exceljet.net/formulas/calculate-running-total)

### [Calculate running total](https://exceljet.net/formulas/calculate-running-total)

In this example, the goal is to calculate a running total in column D of the worksheet as shown. A running total, or cumulative sum, is a set of partial sums that changes as more data is collected. Each calculation represents the sum of values up to that point. In this example, each calculation...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Count occurrences in entire workbook](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20occurrences%20in%20entire%20workbook.png "Excel formula: Count occurrences in entire workbook")](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)

### [Count occurrences in entire workbook](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)

In this example, the goal is to count the value in cell B5 ("Steven") in the sheets listed in B11:B13. The workbook shown in the example has four worksheets in total. The first sheet is named "Master" and contains the search string, the range, and the sheets to include in the count, as seen in the...

Related functions
-----------------

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

*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [Calculate running total](https://exceljet.net/formulas/calculate-running-total)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Count occurrences in entire workbook](https://exceljet.net/formulas/count-occurrences-in-entire-workbook)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

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
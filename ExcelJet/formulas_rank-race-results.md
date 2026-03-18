# Rank race results - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/rank-race-results

---

[Skip to main content](https://exceljet.net/formulas/rank-race-results#main-content)

[](https://exceljet.net/formulas/rank-race-results#)

*   [Previous](https://exceljet.net/formulas/rank-if-formula)
    
*   [Next](https://exceljet.net/formulas/rank-values-by-month)
    

[Rank](https://exceljet.net/formulas#Rank)

Rank race results
=================

by Dave Bruns · Updated 10 Nov 2017

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

![Excel formula: Rank race results](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/rank%20race%20results2.png "Excel formula: Rank race results")

Summary
-------

To rank a set of race times, where the lowest (fastest) time is ranked #1, you can use the RANK function. In the example shown, the formula in D6 is:

    =RANK(C6,times,1)
    

Where times is the [named range](https://exceljet.net/glossary/named-range)
 C6:C13.

Generic formula
---------------

    =RANK(time,times,1)

Explanation 
------------

You can use the RANK function to rank numeric values. RANK has two modes of operation: ranking values so that the largest value is ranked #1 (order = 0), and ranking values so that the smallest value is #1 (order = 1).

In this case, we are ranking race times. The lowest/fastest value should rank #1, so we set the order argument to 1:

    =RANK(C6,times,1)
    

Related formulas
----------------

[![Excel formula: Rank function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/rank%20function%20example1.png "Excel formula: Rank function example")](https://exceljet.net/formulas/rank-function-example)

### [Rank function example](https://exceljet.net/formulas/rank-function-example)

You can use the RANK function to rank numeric values. RANK has two modes of operation: ranking values where the largest value is #1 (order = 0), and ranking values where the lowest value is #1 (order = 1). In this case, we are ranking test scores, so the highest value should rank #1, so we omit the...

Related functions
-----------------

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Rank function example](https://exceljet.net/formulas/rank-function-example)
    

### Functions

*   [RANK Function](https://exceljet.net/functions/rank-function)
    

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
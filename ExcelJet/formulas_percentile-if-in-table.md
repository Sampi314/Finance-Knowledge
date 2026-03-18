# Percentile IF in table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/percentile-if-in-table

---

[Skip to main content](https://exceljet.net/formulas/percentile-if-in-table#main-content)

[](https://exceljet.net/formulas/percentile-if-in-table#)

*   [Previous](https://exceljet.net/formulas/get-column-name-from-index-in-table)
    
*   [Next](https://exceljet.net/formulas/running-count-in-table)
    

[Tables](https://exceljet.net/formulas#Tables)

Percentile IF in table
======================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[PERCENTILE](https://exceljet.net/functions/percentile-function)

![Excel formula: Percentile IF in table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/percentile%20IF%20in%20table.png "Excel formula: Percentile IF in table")

Summary
-------

To calculate a conditional percentile, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 using the IF function inside the PERCENTILE function. In the example shown, the formula in G5 is:

    =PERCENTILE(IF(Table[Gender]=G$4,Table[Score]),$F5)
    

Where "Table" is an [Excel Table](https://exceljet.net/glossary/excel-table)
 with data in B5:D14.

_Note: This is an array formula and must be entered with control + shift + enter in Excel 2019 and earlier._

Generic formula
---------------

    =PERCENTILE(IF(criteria,values),k)

Explanation 
------------

This formula sits inside a small summary table with percentile values in column F and gender values in G4 and H4. Working from the inside out, the IF function is set up like this:

    IF(Table[Gender]=G$4,Table[Score])
    

Here, each value in the gender column is tested against the value in G4, "Male".

The result is an array of boolean values like this:

    {88;85;77;FALSE;FALSE;FALSE;83;FALSE;FALSE;79}
    

Only scores associated with males make it into the array, female scores are translated to FALSE. This array goes into the PERCENTILE function with the k value from F5, 90%.

PERCENTILE automatically ignores FALSE values and returns a result of 86.8.

The reference to Gender in G$4 is locked to prevent the row from changing. The reference to k values, $F5 is locked to prevent the column from changing. As a result, the formula can be copied across the range G5:H7.

Related formulas
----------------

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

Related functions
-----------------

[![Excel PERCENTILE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_percentile.png "Excel PERCENTILE function")](https://exceljet.net/functions/percentile-function)

### [PERCENTILE Function](https://exceljet.net/functions/percentile-function)

The Excel PERCENTILE function calculates the "kth percentile" for a set of data. A percentile is a value below which a given percentage of values in a data set fall. You can use PERCENTILE to determine the 90th percentile, the 80th percentile, etc.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    

### Functions

*   [PERCENTILE Function](https://exceljet.net/functions/percentile-function)
    

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
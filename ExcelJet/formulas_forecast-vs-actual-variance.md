# Forecast vs actual variance - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/forecast-vs-actual-variance

---

[Skip to main content](https://exceljet.net/formulas/forecast-vs-actual-variance#main-content)

[](https://exceljet.net/formulas/forecast-vs-actual-variance#)

*   [Previous](https://exceljet.net/formulas/flip-table-rows-to-columns)
    
*   [Next](https://exceljet.net/formulas/formula-with-locked-absolute-reference)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Forecast vs actual variance
===========================

by Dave Bruns · Updated 25 Oct 2023

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Forecast vs actual variance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/forecast%20vs%20actual%20variance.png "Excel formula: Forecast vs actual variance")

Summary
-------

To calculate forecast versus actual variance based on a set of data, you can use can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 to gather up totals, and basic other formulas to calculate variance and variance percentage. In the example shown, the formula in G5 is:

    =SUMIFS(amount,type,G$4,group,$F5)
    

where **amount** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C14, and **type** is the named range D5:D14, and **group** is the named range B5:B14.

Explanation 
------------

This is a pretty standard use of the SUMIFS function. In this case, we need to sum amounts based on two criteria: type (forecast or actual) and group. To sum by type, the range/criteria pair is:

    type,G$4
    

where type is the named range D5:D14, and G4 is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 with the row locked in order to match the column header in row 4 when the formula is copied down.

To sum by group, the range/criteria pair is:

    group,$F5
    

where **group** is the named range B5:B14, and F5 is a mixed reference with the column locked in order to match group names in column F when the formula is copied across.

### Variance formulas

To calculate a variance amount in column I, the formula simply subtracts the forecast from the actual:

    =G5-H5
    

The variance percentage formula in column J is:

    =(G5-H5)/H5
    

with [percentage number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Notes

1.  The data shown here would work well in an [Excel Table](https://exceljet.net/articles/excel-tables)
    , which would automatically expand to include new data. We are using named ranges here to keep the formulas as simple as possible.
2.  [Pivot tables](https://exceljet.net/articles/excel-pivot-tables)
     can also be used to calculate variance. Formulas provide more flexibility and control at the cost of more complexity.

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

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
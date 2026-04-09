# Get pivot table grand total - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-pivot-table-grand-total

---

[Skip to main content](https://exceljet.net/formulas/get-pivot-table-grand-total#main-content)

[](https://exceljet.net/formulas/get-pivot-table-grand-total#)

*   [Previous](https://exceljet.net/formulas/get-last-entry-by-month-and-year)
    
*   [Next](https://exceljet.net/formulas/get-pivot-table-subtotal)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Get pivot table grand total
===========================

by Dave Bruns · Updated 21 Dec 2016

Related functions 
------------------

[GETPIVOTDATA](https://exceljet.net/functions/getpivotdata-function)

![Excel formula: Get pivot table grand total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20pivot%20table%20grand%20total.png "Excel formula: Get pivot table grand total")

Summary
-------

To get the grand total for a value field in a pivot table, you can use the GETPIVOTDATA function. In the example shown, the formula in I6 is:

    =GETPIVOTDATA("Sales",$B$4)
    

Although you can reference any cell in a pivot table with a normal reference (i.e. F11) the GETPIVOTDATA will continue to return correct values even when the pivot table changes.

Generic formula
---------------

    =GETPIVOTDATA("field name",pivot_ref)

Explanation 
------------

To use the GETPIVOTDATA function, the field you want to query must be a value field in the pivot table, subtotaled at the right level.

In this case, we want the grand total of the "sales" field, so we simply provide the name the field in the first argument, and supply a reference to the pivot table in the second:

    =GETPIVOTDATA("Sales",$B$4)
    

The pivot\_table reference can be any cell in the pivot table, but by convention we use the upper left cell.

_Note: GETPIVOTDATA will return the value field based on current "summarize by" settings (sum, count, average, etc.)._

Related formulas
----------------

[![Excel formula: Get pivot table subtotal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20pivot%20table%20subtotal.png "Excel formula: Get pivot table subtotal")](https://exceljet.net/formulas/get-pivot-table-subtotal)

### [Get pivot table subtotal](https://exceljet.net/formulas/get-pivot-table-subtotal)

To use the GETPIVOTDATA function, the field you want to query must be a value field in the pivot table, subtotaled at the right level. In this case, we want a subtotal of the "sales" field, so we provide the name the field in the first argument, and supply a reference to the pivot table in the...

[![Excel formula: Get pivot table subtotal grouped date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20pivot%20table%20subtotal%20grouped%20date.png "Excel formula: Get pivot table subtotal grouped date")](https://exceljet.net/formulas/get-pivot-table-subtotal-grouped-date)

### [Get pivot table subtotal grouped date](https://exceljet.net/formulas/get-pivot-table-subtotal-grouped-date)

To use the GETPIVOTDATA function, the field you want to query must be a value field in the pivot table, subtotaled at the right level. When dates are grouped, they can be queried based on the numeric equivalent: Grouped by month - use numbers 1-12 Grouped by quarter - use numbers 1-4 Grouped by...

Related functions
-----------------

[![Excel GETPIVOTDATA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20getpivotdata%20function.png "Excel GETPIVOTDATA function")](https://exceljet.net/functions/getpivotdata-function)

### [GETPIVOTDATA Function](https://exceljet.net/functions/getpivotdata-function)

The Excel GETPIVOTDATA function can retrieve specific data from a pivot table by name based on the structure, instead of cell references.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get pivot table subtotal](https://exceljet.net/formulas/get-pivot-table-subtotal)
    
*   [Get pivot table subtotal grouped date](https://exceljet.net/formulas/get-pivot-table-subtotal-grouped-date)
    

### Functions

*   [GETPIVOTDATA Function](https://exceljet.net/functions/getpivotdata-function)
    

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
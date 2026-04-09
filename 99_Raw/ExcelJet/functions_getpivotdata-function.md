# Excel GETPIVOTDATA function | Exceljet

**Source:** https://exceljet.net/functions/getpivotdata-function

---

[Skip to main content](https://exceljet.net/functions/getpivotdata-function#main-content)

[](https://exceljet.net/functions/getpivotdata-function#)

*   [Previous](https://exceljet.net/functions/formulatext-function)
    
*   [Next](https://exceljet.net/functions/hlookup-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

GETPIVOTDATA Function
=====================

by Dave Bruns · Updated 7 Jun 2021

![Excel GETPIVOTDATA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20getpivotdata%20function.png "Excel GETPIVOTDATA function")

Summary
-------

The Excel GETPIVOTDATA function can retrieve specific data from a pivot table by name based on the structure, instead of cell references.

Purpose 
--------

Retrieve data from a pivot table in a formula

Return value 
-------------

The data requested

Syntax
------

    =GETPIVOTDATA(data_field,pivot_table,[field1, item1],...)

*   _data\_field_ - The name of the value field to query.
*   _pivot\_table_ - A reference to any cell in the pivot table to query.
*   _field1, item1_ - \[optional\] A field/item pair.

Using the GETPIVOTDATA function 
--------------------------------

Use the GETPIVOTDATA function to query an existing [Pivot Table](https://exceljet.net/articles/excel-pivot-tables)
 and retrieve specific data based on the pivot table structure. The advantage of GETPIVOTDATA over a simple cell reference is that it collects data based on _structure_, not cell location. GETPIVOTDATA will continue to work correctly even when a pivot table changes, as long as the field(s) being referenced is still present. 

The first argument, _data\_field_, names a value field to query. The second argument, pivot\_t_a_ble, is a reference to any cell in an existing pivot table. Additional arguments are supplied in field/item pairs that act like filters to limit the data retrieved based on the structure of the pivot table. For example, you might supply the field "Region" with the item "East" to limit sales data to Sales in the East Region.

The GETPIVOTDATA function is generated automatically when you reference a value cell in a pivot table by pointing and clicking. To avoid this, you can simply type the address of the cell you want (instead of clicking). If you want to disable this feature entirely, disable "Generate GETPIVOTDATA" in the menu at Pivot TableTools > Options > Options (far left, below the pivot table name).

### Examples

The examples below are based on the following pivot table:

![Example of GETPIVOTDATA function with a pivot table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/excel%20getpivotdata%20example.png?itok=b6dXcdmo "Example of GETPIVOTDATA function with a pivot table")

The first argument in the GETPIVOTDATA function names the field from which to retrieve data. The second argument is a reference to a cell that is part of the pivot table. To get total Sales from the pivot table shown:

    =GETPIVOTDATA("Sales",$B$4) // returns 138602
    

Fields and item pairs are supplied in pairs entered as [text values](https://exceljet.net/glossary/text-value)
. To get total sales for the Product Hazelnut:

    =GETPIVOTDATA("Sales",$B$4,"Product","Hazelnut") // returns 62456
    

To get total Sales for the West region:

    =GETPIVOTDATA("Sales",$B$4,"Region","West") // returns 41518
    

To get total sales for Almond in the East region, you can use either of the formulas below:

    =GETPIVOTDATA("Sales",$B$4,"Region","East","Product","Almond")
    =GETPIVOTDATA("Sales",$B$4,"Product","Almond","Region","East")
    

You can also use cell references to provide field and item names. In the example shown above, the formula in I8 is:

    =GETPIVOTDATA("Sales",$B$4,"Region",I6,"Product",I7)
    

The values for Region and Product come from cells I5 and I6. The data is collected based on the region "Midwest" in cell I6 for the product "Hazelnut" in cell I7.

### Dates and times

When using GETPIVOTDATA to fetch information from a pivot table based on a date or time date or time, use Excel's [native format](https://exceljet.net/glossary/excel-date)
, or a function like the [DATE function](https://exceljet.net/functions/date-function)
. For example, to get total Sales on April 1, 2021 when individual dates are displayed:

    =GETPIVOTDATA("Sales",A1,"Date",DATE(2021,4,1))
    

When [dates are grouped](https://exceljet.net/videos/how-to-group-a-pivot-table-by-date)
, refer to the group names as text. For example, if the Date field is grouped by year:

    =GETPIVOTDATA("Sales",A1,"Year","2021")
    

### Notes

*   The name of the data\_field, and field/item values must be enclosed in double quotes (")
*   GETPIVOTDATA will return a #REF error if any fields are spelled incorrectly.
*   GETPIVOTDATA will return a #REF error if the reference to _pivot\_table_ is not valid.

GETPIVOTDATA function examples
------------------------------

[![Excel formula: Get pivot table subtotal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20pivot%20table%20subtotal.png "Excel formula: Get pivot table subtotal")](https://exceljet.net/formulas/get-pivot-table-subtotal)

### [Get pivot table subtotal](https://exceljet.net/formulas/get-pivot-table-subtotal)

To use the GETPIVOTDATA function, the field you want to query must be a value field in the pivot table, subtotaled at the right level. In this case, we want a subtotal of the "sales" field, so we provide the name the field in the first argument, and supply a reference to the pivot table in the...

[![Excel formula: Get pivot table grand total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20pivot%20table%20grand%20total.png "Excel formula: Get pivot table grand total")](https://exceljet.net/formulas/get-pivot-table-grand-total)

### [Get pivot table grand total](https://exceljet.net/formulas/get-pivot-table-grand-total)

To use the GETPIVOTDATA function, the field you want to query must be a value field in the pivot table, subtotaled at the right level. In this case, we want the grand total of the "sales" field, so we simply provide the name the field in the first argument, and supply a reference to the pivot table...

[![Excel formula: Get pivot table subtotal grouped date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20pivot%20table%20subtotal%20grouped%20date.png "Excel formula: Get pivot table subtotal grouped date")](https://exceljet.net/formulas/get-pivot-table-subtotal-grouped-date)

### [Get pivot table subtotal grouped date](https://exceljet.net/formulas/get-pivot-table-subtotal-grouped-date)

To use the GETPIVOTDATA function, the field you want to query must be a value field in the pivot table, subtotaled at the right level. When dates are grouped, they can be queried based on the numeric equivalent: Grouped by month - use numbers 1-12 Grouped by quarter - use numbers 1-4 Grouped by...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get pivot table grand total](https://exceljet.net/formulas/get-pivot-table-grand-total)
    
*   [Get pivot table subtotal grouped date](https://exceljet.net/formulas/get-pivot-table-subtotal-grouped-date)
    
*   [Get pivot table subtotal](https://exceljet.net/formulas/get-pivot-table-subtotal)
    

### Articles

*   [Excel Pivot Tables](https://exceljet.net/articles/excel-pivot-tables)
    

### Links

*   [Microsoft GETPIVOTDATA function documentation](https://support.office.com/en-us/article/getpivotdata-function-8c083b99-a922-4ca0-af5e-3af55960761f)
    

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
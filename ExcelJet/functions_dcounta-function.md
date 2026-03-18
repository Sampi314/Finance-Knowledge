# Excel DCOUNTA function | Exceljet

**Source:** https://exceljet.net/functions/dcounta-function

---

[Skip to main content](https://exceljet.net/functions/dcounta-function#main-content)

[](https://exceljet.net/functions/dcounta-function#)

*   [Previous](https://exceljet.net/functions/dcount-function)
    
*   [Next](https://exceljet.net/functions/dget-function)
    

Excel 2003

[Database](https://exceljet.net/functions#Database)

DCOUNTA Function
================

by Dave Bruns · Updated 13 Dec 2021

Related functions 
------------------

[DCOUNT](https://exceljet.net/functions/dcount-function)

[DMAX](https://exceljet.net/functions/dmax-function)

[DMIN](https://exceljet.net/functions/dmin-function)

[DSUM](https://exceljet.net/functions/dsum-function)

[DPRODUCT](https://exceljet.net/functions/dproduct-function)

![Excel DCOUNTA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_dcounta.png "Excel DCOUNTA function")

Summary
-------

The Excel DCOUNTA function counts matching records in a database using criteria and an optional field. When a field is provided, DCOUNTA counts both numeric and text values when the field value is not empty. Use [DCOUNT](https://exceljet.net/functions/dcount-function)
 to count only numeric values in a given field.

Purpose 
--------

Count matching records in a database

Return value 
-------------

Numeric count of matching records

Syntax
------

    =DCOUNTA(database,[field],criteria)

*   _database_ - Database range including headers.
*   _field_ - \[optional\] Field name or index to count.
*   _criteria_ - Criteria range including headers.

Using the DCOUNTA function 
---------------------------

The Excel DCOUNTA function counts matching records in a database using a specified field and criteria. Unlike DCOUNT, which counts only numeric values, DCOUNTA counts _both_ numeric and text values. Empty cells are ignored. Use [DCOUNT](https://exceljet.net/functions/dcount-function)
 to count only numeric values.

The _database_ argument is a range of cells that includes field headers, _field_ is the name or index of the field to count, and _criteria_ is a range of cells with headers matching those in _database._ 

Using the example above, you can count records where the color is "red" and price is > 10 with these formulas:

    =DCOUNTA(B7:E14,"Color",B4:E5) // field by name
    =DCOUNTA(B7:E14,1,B4:E5) // field by index
    =DCOUNTA(B7:E14,,B4:E5) // field omitted
    

_Caution: If the value in a field is empty it will not be counted, even when criteria match._

_Note: The DCOUNTA function will count numbers or text in a given field, whereas [DCOUNT](https://exceljet.net/functions/dcount-function)
 only counts numeric values._

### Criteria options

The criteria can include a variety of expressions. The table below shows some examples:

| Criteria | Behavior |
| --- | --- |
| Red | Match "red" or "RED" |
| Re\* | Begins with "re" |
| 10  | Equal to 10 |
| \>10 | Greater than 10 |
| <>  | Not blank |
| <>100 | Not 100 |
| \>12/19/2017 | Greater than Dec 19, 2017 |

The _criteria_ range for DCOUNT can include more than one row below the headers. When _criteria_ includes more than one row, each row is joined with OR logic, and the expressions in a given _criteria_ row are joined with AND logic.

### Notes

*   DCOUNTA counts numbers and text in a given field when criteria match.
*   DCOUNTA supports [wildcards](https://exceljet.net/glossary/wildcard)
     in criteria, the support is not as good as in more modern functions like [COUNTIFS](https://exceljet.net/functions/countifs-function)
    .
*   _Criteria_ can include more than one row (as explained above),
*   The _field_ argument can be supplied as a name in double quotes ("") or as a number representing field index.
*   The _database_ and _criteria_ ranges must include matching headers.

Related functions
-----------------

[![Excel DCOUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dcount.png "Excel DCOUNT function")](https://exceljet.net/functions/dcount-function)

### [DCOUNT Function](https://exceljet.net/functions/dcount-function)

The Excel DCOUNT function counts matching records in a database using criteria and an optional field. When a field is provided DCOUNT will only count numeric values in the field. Use [DCOUNTA](https://exceljet.net/functions/dcounta-function)
 to count numbers or text values in a given field.

[![Excel DMAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dmax.png "Excel DMAX function")](https://exceljet.net/functions/dmax-function)

### [DMAX Function](https://exceljet.net/functions/dmax-function)

The Excel DMAX function returns the maximum value in a field, from a set of records that match criteria. Use the DMIN function to get the minimum value.

[![Excel DMIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dmin.png "Excel DMIN function")](https://exceljet.net/functions/dmin-function)

### [DMIN Function](https://exceljet.net/functions/dmin-function)

The Excel DMIN function returns the minimum value in a field, from a set of records that match criteria. Use the MAX function to get the maximum value.

[![Excel DSUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dsum_function.png "Excel DSUM function")](https://exceljet.net/functions/dsum-function)

### [DSUM Function](https://exceljet.net/functions/dsum-function)

The Excel DSUM function returns the sum of values from a set of records that match criteria. The values to sum are extracted from a given field in the database....

[![Excel DPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dproduct.png "Excel DPRODUCT function")](https://exceljet.net/functions/dproduct-function)

### [DPRODUCT Function](https://exceljet.net/functions/dproduct-function)

The Excel DPRODUCT function returns the product of values from a set of records that match criteria. The values to multiply are extracted from a given field in the database, specified as an argument.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [DCOUNT Function](https://exceljet.net/functions/dcount-function)
    
*   [DMAX Function](https://exceljet.net/functions/dmax-function)
    
*   [DMIN Function](https://exceljet.net/functions/dmin-function)
    
*   [DSUM Function](https://exceljet.net/functions/dsum-function)
    
*   [DPRODUCT Function](https://exceljet.net/functions/dproduct-function)
    

### Links

*   [Microsoft DCOUNTA function documentation](https://support.office.com/en-us/article/dcounta-function-00232a6d-5a66-4a01-a25b-c1653fda1244)
    

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
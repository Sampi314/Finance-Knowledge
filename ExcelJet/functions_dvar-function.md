# Excel DVAR function | Exceljet

**Source:** https://exceljet.net/functions/dvar-function

---

[Skip to main content](https://exceljet.net/functions/dvar-function#main-content)

[](https://exceljet.net/functions/dvar-function#)

*   [Previous](https://exceljet.net/functions/dsum-function)
    
*   [Next](https://exceljet.net/functions/dvarp-function)
    

Excel 2003

[Database](https://exceljet.net/functions#Database)

DVAR Function
=============

by Dave Bruns · Updated 13 Dec 2021

Related functions 
------------------

[DCOUNT](https://exceljet.net/functions/dcount-function)

[DCOUNTA](https://exceljet.net/functions/dcounta-function)

[DMAX](https://exceljet.net/functions/dmax-function)

[DVARP](https://exceljet.net/functions/dvarp-function)

![Excel DVAR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_dvar.png "Excel DVAR function")

Summary
-------

The Excel DVAR function returns the variance of a sample extracted from records that match the given criteria. If data represents the entire population, use the DVARP function.

Purpose 
--------

Get sample variance for matching records

Return value 
-------------

The calculated variance

Syntax
------

    =DVAR(database,field,criteria)

*   _database_ - Database range including headers.
*   _field_ - Field name or index to count.
*   _criteria_ - Criteria range including headers.

Using the DVAR function 
------------------------

The Excel DVAR function gets the variance of a sample extracted from records matching criteria, using values in a given field.

The _database_ argument is a range of cells that includes field headers, _field_ is the name or index of the field to get a max value from, and _criteria_ is a range of cells with headers that match those in _database._ 

Using the example above, you can get the variance of heights for the group "Fox" with either of these formulas:

    =DVAR(B7:C13,"Height",B4:C5) // field by name
    =DVAR(B7:C13,2,B4:C5) // field by index
    

### Criteria options

The criteria can include a variety of expressions, including some [wildcards](https://exceljet.net/glossary/wildcard)
. The table below shows some examples:

| Criteria | Behavior |
| --- | --- |
| Red | Match "red" or "RED" |
| Re\* | Begins with "re" |
| 10  | Equal to 10 |
| \>10 | Greater than 10 |
| <>  | Not blank |
| <>100 | Not 100 |
| \>12/19/2017 | Greater than Dec 19, 2017 |

Note: Support for [wildcards](https://exceljet.net/glossary/wildcard)
 is not quite the same as with other functions like COUNTIFS, SUMIFS, MATCH, etc. For example, the pattern ??? will match strings with 3 exactly characters in more modern functions, but not in the database functions. If you are using wildcards, test carefully.

### Multi-row criteria

The criteria range for DVAR can include more than one row below the headers. When criteria includes more than one row, each row is joined with OR logic, and the expressions in a given criteria row are joined with AND logic.

Notes:

*   DVAR is the mean to calculate variance for a sample. If data represents the entire population, use the DVARP function.
*   DVAR supports some [wildcards](https://exceljet.net/glossary/wildcard)
     in criteria
*   Criteria can include more than one row (as explained above)
*   The _field_ argument can be supplied as a name in double quotes ("") or as a number representing field index.
*   The _database_ and _criteria_ ranges must include matching headers.

Related functions
-----------------

[![Excel DCOUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dcount.png "Excel DCOUNT function")](https://exceljet.net/functions/dcount-function)

### [DCOUNT Function](https://exceljet.net/functions/dcount-function)

The Excel DCOUNT function counts matching records in a database using criteria and an optional field. When a field is provided DCOUNT will only count numeric values in the field. Use [DCOUNTA](https://exceljet.net/functions/dcounta-function)
 to count numbers or text values in a given field.

[![Excel DCOUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dcounta.png "Excel DCOUNTA function")](https://exceljet.net/functions/dcounta-function)

### [DCOUNTA Function](https://exceljet.net/functions/dcounta-function)

The Excel DCOUNTA function counts matching records in a database using criteria and an optional field. When a field is provided, DCOUNTA counts both numeric and text values when the field value is not empty. Use [DCOUNT](https://exceljet.net/functions/dcount-function)
 to count only numeric values in a ...

[![Excel DMAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dmax.png "Excel DMAX function")](https://exceljet.net/functions/dmax-function)

### [DMAX Function](https://exceljet.net/functions/dmax-function)

The Excel DMAX function returns the maximum value in a field, from a set of records that match criteria. Use the DMIN function to get the minimum value.

[![Excel DVARP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dvarp.png "Excel DVARP function")](https://exceljet.net/functions/dvarp-function)

### [DVARP Function](https://exceljet.net/functions/dvarp-function)

The Excel DVARP function returns the variance of an entire population extracted from records that match the given criteria. If data represents a sample only, use the DVAR function....

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
    
*   [DCOUNTA Function](https://exceljet.net/functions/dcounta-function)
    
*   [DMAX Function](https://exceljet.net/functions/dmax-function)
    
*   [DVARP Function](https://exceljet.net/functions/dvarp-function)
    

### Links

*   [Microsoft DVAR function documentation](https://support.office.com/en-us/article/dvar-function-d6747ca9-99c7-48bb-996e-9d7af00f3ed1)
    

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
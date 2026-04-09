# Excel DGET function | Exceljet

**Source:** https://exceljet.net/functions/dget-function

---

[Skip to main content](https://exceljet.net/functions/dget-function#main-content)

[](https://exceljet.net/functions/dget-function#)

*   [Previous](https://exceljet.net/functions/dcounta-function)
    
*   [Next](https://exceljet.net/functions/dmax-function)
    

Excel 2003

[Database](https://exceljet.net/functions#Database)

DGET Function
=============

by Dave Bruns · Updated 13 Dec 2021

Related functions 
------------------

[DCOUNT](https://exceljet.net/functions/dcount-function)

[DCOUNTA](https://exceljet.net/functions/dcounta-function)

[DMAX](https://exceljet.net/functions/dmax-function)

[DMIN](https://exceljet.net/functions/dmin-function)

[DAVERAGE](https://exceljet.net/functions/daverage-function)

![Excel DGET function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_dget.png "Excel DGET function")

Summary
-------

The Excel DGET function gets a single value in a given field from a record that matches criteria. DGET will throw the #NUM error if more than one record matches criteria.

Purpose 
--------

Get value from matching record

Return value 
-------------

The value in a given field

Syntax
------

    =DGET(database,field,criteria)

*   _database_ - Database range including headers.
*   _field_ - Field name or index to count.
*   _criteria_ - Criteria range including headers.

Using the DGET function 
------------------------

The Excel DGET function gets a single value from a given field in a record that matches criteria. The _database_ argument is a range of cells that includes field headers, _field_ is the name or index of the field to get a max value from, and _criteria_ is a range of cells with headers that match those in _database._ 

Using the example above, you can get the value from the field "Total" in a record where color is "Red" and "Day" is Tue with either of the two formulas below:

    =DGET(B7:E14,"Total",B4:E5) // field by name
    =DGET(B7:E14,4,B4:E5) // field by index
    

The DGET function is designed to extract a single value based on matching criteria. When more than one record matches criteria, DGET will throw the #NUM error.

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

Note: it appears support for [wildcards](https://exceljet.net/glossary/wildcard)
 is not as extensive as with other functions like COUNTIFS, SUMIFS, MATCH etc. For example, the pattern ??? will match strings with 3 exactly characters in more modern functions, but not in the database functions. If you are using wildcards, test carefully.

### Multi-row criteria

The criteria range for DGET can include more than one row below the headers. When criteria includes more than one row, each row is joined with OR logic, and the expressions in a given criteria row are joined with AND logic.

Notes:

*   DGET will throw the #NUM error if more than one record matches criteria.
*   DGET supports [wildcards](https://exceljet.net/glossary/wildcard)
     in criteria
*   Criteria can include more than one row
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

[![Excel DMIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_dmin.png "Excel DMIN function")](https://exceljet.net/functions/dmin-function)

### [DMIN Function](https://exceljet.net/functions/dmin-function)

The Excel DMIN function returns the minimum value in a field, from a set of records that match criteria. Use the MAX function to get the maximum value.

[![Excel DAVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_daverage.png "Excel DAVERAGE function")](https://exceljet.net/functions/daverage-function)

### [DAVERAGE Function](https://exceljet.net/functions/daverage-function)

The Excel DAVERAGE function returns the average in a given field for records that match criteria.

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
    
*   [DMIN Function](https://exceljet.net/functions/dmin-function)
    
*   [DAVERAGE Function](https://exceljet.net/functions/daverage-function)
    

### Links

*   [Microsoft DGET function documentation](https://support.office.com/en-us/article/dget-function-455568bf-4eef-45f7-90f0-ec250d00892e)
    

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
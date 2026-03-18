# Excel FIELDVALUE function | Exceljet

**Source:** https://exceljet.net/functions/fieldvalue-function

---

[Skip to main content](https://exceljet.net/functions/fieldvalue-function#main-content)

[](https://exceljet.net/functions/fieldvalue-function#)

*   [Previous](https://exceljet.net/functions/columns-function)
    
*   [Next](https://exceljet.net/functions/formulatext-function)
    

Excel 365

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

FIELDVALUE Function
===================

by Dave Bruns · Updated 25 Jan 2022

![Excel FIELDVALUE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20fieldvalue%20function.png "Excel FIELDVALUE function")

Summary
-------

The Excel FIELDVALUE function extracts a given field value from a data type. The field is specified by name and provided as a text value.

Purpose 
--------

Extract field value from a data type

Return value 
-------------

Field value for given data type

Syntax
------

    =FIELDVALUE(value,field_name)

*   _value_ - The data type with field values.
*   _field\_name_ - The field name provided as a text value.

Using the FIELDVALUE function 
------------------------------

The Excel FIELDVALUE function extracts a given field value from a [Data Type](https://exceljet.net/glossary/data-type)
. The field is specified by name and provided as a text value. Use the FIELDVALUE function to retrieve a field value by name from linked data types like Stocks, Geography, Food, Currency, and more.

### Examples

To retrieve a field value from a linked data type, provide the field name as text in double quotes (""). For example, with a city in cell A1, linked to a Geography data type, you can request population data like this:

    =FIELDVALUE(A1,"city population")
    

In the example shown, the formula in cell C5, copied down, is:

    =FIELDVALUE(B5,"city population")
    

The result is population data for the 12 cities listed in B5 to B16.

### Alternative syntax

The FIELDVALUE function is an alternative the "dot" syntax for retrieving a field value from a data type. The two formulas below return the same result:

    =FIELDVALUE(B5,"area")
    =B5.area
    

Note square brackets (\[\]) are required for field names that contain spaces:

    =FIELDVALUE(B5,"city population")
    =B5.[city population]
    

When the field name is a single word, the brackets are not required

### Trapping errors

In column D of the example, FIELDVALUE is used to extract "Area" like this:

    FIELDVALUE(B5,"area")
    

This returns a #FIELD! error for cities where area is not available. To trap this error and return an empty string ("") where there are errors, the [IFERROR function](https://exceljet.net/functions/iferror-function)
 is used in cell D5 like this:

    =IFERROR(FIELDVALUE(B5,"area"),"")
    

As a result, the cells for Cairo, Beijing, Istanbul, and Mexico City display nothing instead of a #FIELD! error.

FIELDVALUE function examples
----------------------------

[![Excel formula: Get current stock price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20current%20price.png "Excel formula: Get current stock price")](https://exceljet.net/formulas/get-current-stock-price)

### [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)

In this example, the goal is to retrieve the current stock price for the companies listed in Column B. Note these cells in the range B5:B16 have already been converted to the "Stocks" Data Type . Once the Stocks Data Type is available on the worksheet, you can retrieve various information using the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

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
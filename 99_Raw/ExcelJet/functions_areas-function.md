# Excel AREAS function | Exceljet

**Source:** https://exceljet.net/functions/areas-function

---

[Skip to main content](https://exceljet.net/functions/areas-function#main-content)

[](https://exceljet.net/functions/areas-function#)

*   [Previous](https://exceljet.net/functions/address-function)
    
*   [Next](https://exceljet.net/functions/choose-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

AREAS Function
==============

by Dave Bruns · Updated 23 Jul 2021

![Excel AREAS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20areas%20function.png "Excel AREAS function")

Summary
-------

The Excel AREAS function returns the number of areas in a given reference. For example, =AREAS((A1:C1,A2:C2)) returns 2. Multiple references must be enclosed in an extra set of parentheses.

Purpose 
--------

Get the number of areas in a reference.

Return value 
-------------

A number representing number of areas.

Syntax
------

    =AREAS(reference)

*   _reference_ - Reference(s) to a cell or range of cells.

Using the AREAS function 
-------------------------

The AREAS function returns the number of areas in a given reference as a number. In this context, areas mean separate contiguous ranges. AREAS takes just one [argument](https://exceljet.net/glossary/function-argument)
, called _reference_. _Reference_ can include more than one reference, but you must separate multiple references with a comma and wrap them in an extra set of parentheses. Otherwise, Excel will think the commas indicate multiple arguments and generate an error about entering too many arguments.

### Examples

The formulas below show how the AREAS function can be configured. Notice the first example does not need an extra set of parentheses, since there is just one reference). However, the examples following do need the extra set of parentheses.

    =AREAS(A1:C1) // returns 1
    =AREAS((A1:C1,A2:C2)) // returns 2
    =AREAS((F17:F19,J16:J18,I8)) // returns 3
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Links

*   [Microsoft AREAS function documentation](https://support.office.com/en-us/article/areas-function-8392ba32-7a41-43b3-96b0-3695d2ec6152)
    

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
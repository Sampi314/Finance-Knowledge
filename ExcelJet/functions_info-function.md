# Excel INFO function | Exceljet

**Source:** https://exceljet.net/functions/info-function

---

[Skip to main content](https://exceljet.net/functions/info-function#main-content)

[](https://exceljet.net/functions/info-function#)

*   [Previous](https://exceljet.net/functions/errortype-function)
    
*   [Next](https://exceljet.net/functions/isblank-function)
    

Excel 2003

[Information](https://exceljet.net/functions#Information)

INFO Function
=============

by Dave Bruns · Updated 7 Sep 2021

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

![Excel INFO function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20info%20function.png "Excel INFO function")

Summary
-------

The Excel INFO function returns information about the current environment, including platform, Excel version, number of worksheets in a workbook, and so on. To use the INFO function, supply the type of information you want as text. There are seven types of information available, summarized in the table below.

Purpose 
--------

Get information about current environment

Return value 
-------------

The information requested

Syntax
------

    =INFO(type_text)

*   _type\_text_ - The information type to return as text.

Using the INFO function 
------------------------

The INFO function can retrieve information about the current environment, including the operating system, the operating system version, Excel version, and so on. INFO takes one argument, _type\_text_, which is a [text value](https://exceljet.net/glossary/text-value)
 indicating the type of information to be returned.

### Examples

To use the INFO function, supply the type of information you want as text. For example, to retrieve the operating system, use "system":

    =INFO("system") // returns "pcdos" or "mac"
    

To request Excel release information, use "release":

    =INFO("release") // returns string like "16.0"
    

There are seven types of information you can request, summarized in the table below:

|     |     |
| --- | --- |
| **Type** | **Information** |
| directory | Path of the current directory or folder |
| numfile | Number of active worksheets in open workbooks |
| origin | First visible cell at upper left |
| osversion | Operating system version |
| recalc | Recalculation mode |
| release | Excel version |
| system | Operating system name |

_Note: INFO is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and will update each time a change is made to the worksheet. This can cause performance problems in larger or more complicated workbooks._

INFO function examples
----------------------

[![Excel formula: Add line break based on OS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20line%20break%20based%20on%20OS.png "Excel formula: Add line break based on OS")](https://exceljet.net/formulas/add-line-break-based-on-os)

### [Add line break based on OS](https://exceljet.net/formulas/add-line-break-based-on-os)

In older versions of Excel (before Excel 2016?), the character used for line breaks is different depending on whether Excel is running on a Mac or Windows computer: On Windows Excel, the line break character is ASCII 10. In older versions of Excel on a Mac, the line break character is ASCII 13...

Related functions
-----------------

[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)

### [CELL Function](https://exceljet.net/functions/cell-function)

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add line break based on OS](https://exceljet.net/formulas/add-line-break-based-on-os)
    

### Functions

*   [CELL Function](https://exceljet.net/functions/cell-function)
    

### Links

*   [Microsoft INFO function documentation](https://support.office.com/en-us/article/info-function-725f259a-0e4b-49b3-8b52-58815c69acae)
    

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
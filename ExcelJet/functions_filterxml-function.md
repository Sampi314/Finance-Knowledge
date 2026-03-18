# Excel FILTERXML function | Exceljet

**Source:** https://exceljet.net/functions/filterxml-function

---

[Skip to main content](https://exceljet.net/functions/filterxml-function#main-content)

[](https://exceljet.net/functions/filterxml-function#)

*   [Previous](https://exceljet.net/functions/encodeurl-function)
    
*   [Next](https://exceljet.net/functions/webservice-function)
    

Excel 2013

[Web](https://exceljet.net/functions#Web)

FILTERXML Function
==================

by Dave Bruns · Updated 25 Jan 2023

Related functions 
------------------

[WEBSERVICE](https://exceljet.net/functions/webservice-function)

[ENCODEURL](https://exceljet.net/functions/encodeurl-function)

![Excel FILTERXML function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20filterxml.png "Excel FILTERXML function")

Summary
-------

The Excel FILTERXML function returns specific data from XML text using the specified XPath expression.

Purpose 
--------

Get data from XML with Xpath

Return value 
-------------

Matching data as text

Syntax
------

    =FILTERXML(xml,xpath)

*   _xml_ - Valid XML as a text string.
*   _xpath_ - A valid Xpath expression as a text string.

Using the FILTERXML function 
-----------------------------

The Excel FILTERXML function returns specific data from XML text using a specified XPath expression. 

XML is a text format for storing and transporting data. It is not dependent on any particular hardware or software. XML is extensible and is designed to transport data, as opposed to displaying data in a particular way. XML has strict syntax rules which allows software to traverse the structure of an XML document and perform various operations.

XPath is a special query language for selecting the elements and attributes in an XML document. The FILTERXML function uses XPath to match and extract data from text in XML format.

> FILTERXML is only available in Excel for Windows, _not_ Excel for Mac, or Excel Online.

### Example

In the example shown, the cell contains XML that carries information about albums published as CDs. Each CD contains the title of the album, the name of the artist, and the year the album was released. The formula in cell D5 uses FILTERXML to extract all titles:

    =FILTERXML(B5,"//cd/title")
    

The _xml_ argument is the XML in cell B5, and the _xpath_ argument is the expression "//cd/title", which matches all title elements with the parent . In [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports [dynamic arrays](https://exceljet.net/glossary/dynamic-array)
, the results [spill](https://exceljet.net/glossary/spill)
 into the range D5:D14 automatically.

FILTERXML function examples
---------------------------

[![Excel formula: Sort comma separated values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort_comma_separated_values.png "Excel formula: Sort comma separated values")](https://exceljet.net/formulas/sort-comma-separated-values)

### [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)

In this example the goal is to sort the comma separated values in column B in alphabetical order. In the latest version of Excel, you can solve this problem with a formula based on TEXTSPLIT, SORT, and TEXTJOIN. In earlier versions of Excel the problem is more complicated. See below for a couple of...

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

[![Excel formula: Parse XML with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/parse%20xml%20with%20formula.png "Excel formula: Parse XML with formula")](https://exceljet.net/formulas/parse-xml-with-formula)

### [Parse XML with formula](https://exceljet.net/formulas/parse-xml-with-formula)

The FILTERXML function can parse XML using XPath expressions. XML is a special text format designed to transport data, with features that allow it to be easily parsed and verified by software. XPath is a query language for selecting the elements and attributes in an XML document. The FILTERXML...

[![Excel formula: LAMBDA split text to array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20split%20text%20to%20array.png "Excel formula: LAMBDA split text to array")](https://exceljet.net/formulas/lambda-split-text-to-array)

### [LAMBDA split text to array](https://exceljet.net/formulas/lambda-split-text-to-array)

Excel did not originally offer the TEXTSPLIT function. This article describes how to use the LAMBDA function to create a custom function that splits text as a workaround. It's a good example of how the LAMBDA function can be used to bridge a gap, but the workaround is no longer necessary. I leave...

[![Excel formula: Sum numbers in single cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_numbers_in_cell.png "Excel formula: Sum numbers in single cell")](https://exceljet.net/formulas/sum-numbers-in-single-cell)

### [Sum numbers in single cell](https://exceljet.net/formulas/sum-numbers-in-single-cell)

The goal is to sum numbers that appear inside a single cell as seen in column B. Technically, the numbers in each cell are a single text string, and the numbers are separated by commas, which is referred to as a "delimiter". In the current version of Excel, the easiest way to solve this problem is...

Related functions
-----------------

[![Excel WEBSERVICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20webservice.png "Excel WEBSERVICE function")](https://exceljet.net/functions/webservice-function)

### [WEBSERVICE Function](https://exceljet.net/functions/webservice-function)

The Excel WEBSERVICE function returns data from a web service. The WEBSERVICE function is only available in Excel 2013 and later for Windows.

[![Excel ENCODEURL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20encodeurl.png "Excel ENCODEURL function")](https://exceljet.net/functions/encodeurl-function)

### [ENCODEURL Function](https://exceljet.net/functions/encodeurl-function)

The Excel ENCODEURL function returns a URL-encoded string composed of US-ASCII characters. ENCODEURL is only available in Excel 2013 and later on Windows.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Parse XML with formula](https://exceljet.net/formulas/parse-xml-with-formula)
    
*   [LAMBDA split text to array](https://exceljet.net/formulas/lambda-split-text-to-array)
    
*   [Sum numbers in single cell](https://exceljet.net/formulas/sum-numbers-in-single-cell)
    
*   [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    

### Functions

*   [WEBSERVICE Function](https://exceljet.net/functions/webservice-function)
    
*   [ENCODEURL Function](https://exceljet.net/functions/encodeurl-function)
    

### Links

*   [Microsoft FILTERXML function documentation](https://support.office.com/en-us/article/filterxml-function-4df72efc-11ec-4951-86f5-c1374812f5b7)
    

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
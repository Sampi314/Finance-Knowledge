# Parse XML with formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/parse-xml-with-formula

---

[Skip to main content](https://exceljet.net/formulas/parse-xml-with-formula#main-content)

[](https://exceljet.net/formulas/parse-xml-with-formula#)

*   [Previous](https://exceljet.net/formulas/pad-a-number-with-zeros)
    
*   [Next](https://exceljet.net/formulas/random-sort-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Parse XML with formula
======================

by Dave Bruns · Updated 11 Jul 2022

Related functions 
------------------

[FILTERXML](https://exceljet.net/functions/filterxml-function)

![Excel formula: Parse XML with formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/parse%20xml%20with%20formula.png "Excel formula: Parse XML with formula")

Summary
-------

To parse XML with a formula, you can use the [FILTERXML function](https://exceljet.net/functions/filterxml-function)
. In the example shown, the formula in D5 is:

    =FILTERXML(B5,"//album/title")
    

which returns the ten album titles in the XML.

_Note: FILTERXML is not available in Excel on the Mac, or in Excel Online._

Generic formula
---------------

    =FILTERXML(A1,"xpath")

Explanation 
------------

The [FILTERXML function](https://exceljet.net/functions/filterxml-function)
 can parse XML using XPath expressions. [XML](https://developer.mozilla.org/en-US/docs/Web/XML/XML_introduction)
 is a special text format designed to transport data, with features that allow it to be easily parsed and verified by software. [XPath](https://www.w3schools.com/xml/xpath_syntax.asp)
 is a query language for selecting the elements and attributes in an XML document. The FILTERXML function uses XPath to match and extract data from text in XML format.

In the example shown cell B5 contains XML data that describes 10 music albums. For each album, there is information about the title, the artist, and the year. To parse this XML, the FILTERXML function is used 3 times in cells D5, E5, and F5 are as follows:

    =FILTERXML(B5,"//album/title") // get title
    =FILTERXML(B5,"//album/artist") // get artist
    =FILTERXML(B5,"//album/year") // get year
    

In each case, the XPath expression targets a specific element in the XML. For example, in cell D5, the XPath targets the title element with this string:

    "//album/title"
    

With this XPath expression, FILTERXML returns all 10 album titles. Because this example has been created in [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports [dynamic arrays](https://exceljet.net/glossary/dynamic-array)
, the results [spill](https://exceljet.net/glossary/spill)
 into the range D5:D14 automatically.

Related functions
-----------------

[![Excel FILTERXML function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20filterxml.png "Excel FILTERXML function")](https://exceljet.net/functions/filterxml-function)

### [FILTERXML Function](https://exceljet.net/functions/filterxml-function)

The Excel FILTERXML function returns specific data from XML text using the specified XPath expression.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FILTERXML Function](https://exceljet.net/functions/filterxml-function)
    

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
# Excel ENCODEURL function | Exceljet

**Source:** https://exceljet.net/functions/encodeurl-function

---

[Skip to main content](https://exceljet.net/functions/encodeurl-function#main-content)

[](https://exceljet.net/functions/encodeurl-function#)

*   [Previous](https://exceljet.net/functions/weibull.dist-function)
    
*   [Next](https://exceljet.net/functions/filterxml-function)
    

Excel 2013

[Web](https://exceljet.net/functions#Web)

ENCODEURL Function
==================

by Dave Bruns · Updated 27 Dec 2020

Related functions 
------------------

[WEBSERVICE](https://exceljet.net/functions/webservice-function)

[FILTERXML](https://exceljet.net/functions/filterxml-function)

![Excel ENCODEURL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20encodeurl.png "Excel ENCODEURL function")

Summary
-------

The Excel ENCODEURL function returns a URL-encoded string composed of US-ASCII characters. ENCODEURL is only available in Excel 2013 and later on Windows.

Purpose 
--------

Get URL-encoded string

Return value 
-------------

Encoded text

Syntax
------

    =ENCODEURL(text)

*   _text_ - The text to be encoded.

Using the ENCODEURL function 
-----------------------------

The ENCODEURL function returns a URL-encoded string composed of US-ASCII characters. URL encoding, sometimes called "percent encoding" is a method of encoding characters in a URL using only legal US-ASCII characters. Some characters cannot be part of a URL and are "reserved". Only characters that are  reserved are encoded by ENCODEURL; other characters are left untouched. Common reserved characters include the space character (" "), the forward slash "/", the hash character (#) and others as shown in the example above.

### Example

To use ENCODEURL, supply text or a cell reference that contains text. In the example below, ENCODEURL is used to encode the text "Hello World!"

    =ENCODEURL("Hello World!") // returns "Hello%20World%21"
    

In the example at the top of the page, the formula in cell C5, copied down is:

    =ENCODEURL(B5)
    

At each new row, ENCODEURL returns the encoded text from column B. 

### Reserved characters

The table below shows a list of reserved characters and their url-encoded equivalent.

| Character | Encoding |
| --- | --- |
| !   | %21 |
| #   | %23 |
| $   | %24 |
| %   | %25 |
| &   | %26 |
| '   | %27 |
| (   | %28 |
| )   | %29 |
| \*  | %2A |
| +   | %2B |
| ,   | %2C |
| /   | %2F |
| :   | %3A |
| ;   | %3B |
| \=  | %3D |
| ?   | %3F |
| @   | %40 |
| \[  | %5B |\
| \]  | %5D |
|     | %20 |

Related functions
-----------------

[![Excel WEBSERVICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20webservice.png "Excel WEBSERVICE function")](https://exceljet.net/functions/webservice-function)

### [WEBSERVICE Function](https://exceljet.net/functions/webservice-function)

The Excel WEBSERVICE function returns data from a web service. The WEBSERVICE function is only available in Excel 2013 and later for Windows.

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

*   [WEBSERVICE Function](https://exceljet.net/functions/webservice-function)
    
*   [FILTERXML Function](https://exceljet.net/functions/filterxml-function)
    

### Links

*   [Microsoft ENCODEURL function documentation](https://support.office.com/en-us/article/encodeurl-function-07c7fb90-7c60-4bff-8687-fac50fe33d0e)
    

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
# Excel WEBSERVICE function | Exceljet

**Source:** https://exceljet.net/functions/webservice-function

---

[Skip to main content](https://exceljet.net/functions/webservice-function#main-content)

[](https://exceljet.net/functions/webservice-function#)

*   [Previous](https://exceljet.net/functions/filterxml-function)
    
*   [Next](https://exceljet.net/functions/daverage-function)
    

Excel 2013

[Web](https://exceljet.net/functions#Web)

WEBSERVICE Function
===================

by Dave Bruns · Updated 25 Aug 2021

Related functions 
------------------

[FILTERXML](https://exceljet.net/functions/filterxml-function)

[ENCODEURL](https://exceljet.net/functions/encodeurl-function)

![Excel WEBSERVICE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20webservice.png "Excel WEBSERVICE function")

Summary
-------

The Excel WEBSERVICE function returns data from a web service. The WEBSERVICE function is only available in Excel 2013 and later for Windows.

Purpose 
--------

Get data from a web service

Return value 
-------------

Resulting data

Syntax
------

    =WEBSERVICE(url)

*   _url_ - The url of the web service to call.

Using the WEBSERVICE function 
------------------------------

The WEBSERVICE function returns data from a web service hosted on the internet. The WEBSERVICE function is only available in Excel 2013 and later for Windows.

A web service uses a protocol like HTTP to retrieve data in a machine-readable format like XML or JSON. For example, a formula that uses WEBSERVICE to call a fictitious web service hosted at somewebservice.com might look something like this:

    =WEBSERVICE(“http://somewebservice.com/endpoint?query=xxxx”) 
    

The result from the WEBSERVICE function is returned directly to the worksheet. In cases where the result from a webservice is in XML format, you can use the [FILTERXML function](https://exceljet.net/functions/filterxml-function)
 to parse the XML. 

### Example

A simple example of a web service is RSS, which is used to syndicate content in XML format. RSS is widely available and does not require authentication, so it is an easy way to test the WEBSERVICE function. In the example above, WEBSERVICE is used to fetch breaking news from NASA. The formula in B4 is:

    =WEBSERVICE("https://www.nasa.gov/rss/dyn/breaking_news.rss")
    

RSS uses XML, so the result is a long string of XML that contains the titles of the last 10 news articles published by NASA, along with meta information like description, date, url, and so on. The screen below shows this data in a text editor:

![Sample rss in xml format](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sample%20rss.png?itok=r5ngWqOr "Sample rss in xml format")

### Parsing the result

When the result from WEBSERVICE is XML, you can use the [FILTERXML function](https://exceljet.net/functions/filterxml-function)
 to parse the data. In the example shown, this is how the data and title of each article is extracted. The formula in B7 extracts the date, and trims extra characters with the [MID function](https://exceljet.net/functions/mid-function)
 to create an Excel-friendly date:

    =MID(FILTERXML(B4,"//item/pubDate"),6,11)
    

The formula in C7 extracts the title:

    =FILTERXML(B4,"//item/title")
    

### Notes

*   When WEBSERVICE can't retrieve data, it returns a #VALUE! error.
*   If the result from WEBSERVICE is more than 32767 characters, it returns a #VALUE! error.

Related functions
-----------------

[![Excel FILTERXML function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20filterxml.png "Excel FILTERXML function")](https://exceljet.net/functions/filterxml-function)

### [FILTERXML Function](https://exceljet.net/functions/filterxml-function)

The Excel FILTERXML function returns specific data from XML text using the specified XPath expression.

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

### Functions

*   [FILTERXML Function](https://exceljet.net/functions/filterxml-function)
    
*   [ENCODEURL Function](https://exceljet.net/functions/encodeurl-function)
    

### Links

*   [Microsoft WEBSERVICE function documentation](https://support.office.com/en-us/article/webservice-function-0546a35a-ecc6-4739-aed7-c0b7ce1562c4)
    

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
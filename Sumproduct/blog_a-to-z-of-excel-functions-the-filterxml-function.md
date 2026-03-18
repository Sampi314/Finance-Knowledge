# A to Z of Excel Functions: The FILTERXML Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filterxml-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The FILTERXML Function

*   May 26, 2019

A to Z of Excel Functions: The FILTERXML Function
=================================================

A to Z of Excel Functions: The FILTERXML Function
=================================================

27 May 2019

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **FILTERXML** function._

**The FILTERXML function**

Until Excel 2013, Excel was mostly an offline application, although you could use VBA, Power Query / Get & Transform or Power Pivot in Excel to gain access to internet and online datasets. However, Excel 2013 changed all that and introduced two new functions to the world:

1.  **WEBSERVICE**, which provides immediate and easy access to any REST WebAPI assuming you have an internet connection by downloading the HTTP response of the provided URL; _and  
    _
2.  **FILTERXML**, which parses an XML string (_i.e._ a text string that contains an XML document) and returns a single element (known as a node or attribute) provided by an XPath. In case you are wondering, XPath is a query language for selecting XML elements such as nodes and attributes and works with both XML and HTML.

Therefore, **FILTERXML** tends to work in tandem with **WEBSERVICE** insofar that it makes sense of the long text string delivered by the former function and finds what you are looking for in that text string.

The **FILTERXML** function employs the following syntax to operate:

**FILTERXML(xml, xpath)**

The **FILTERXML** function has the following arguments:

*   **xml:** this is required and represents a string in a valid XML format
*   **xpath:** this is also required. This represents a string in a standard XPath format.

It should be noted that:

*   if **xml** is not valid, **FILTERXML** returns the _#VALUE!_ error value
*   if **xml** contains a namespace with a prefix that is not valid, **FILTERXML** returns the _#VALUE!_ error
*   the **FILTERXML** function is not available in Excel Online
*   the **FILTERXML** function is not available in Excel (2016) for Mac
*   Further, this function may appear in the function gallery in Excel for Mac, but it relies on features of the Windows operating system, so it will not return results on a Mac.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filterxml-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filterxml-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filterxml-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filterxml-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filterxml-function/#0 "close")

top
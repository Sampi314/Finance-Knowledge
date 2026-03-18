# Excel for Mac: Functions Unavailable on Mac

**Source:** https://sumproduct.com/blog/excel-for-mac-functions-unavailable-on-mac/

---

[Home](https://sumproduct.com/)

\> Excel for Mac: Functions Unavailable on Mac

*   February 29, 2024

Excel for Mac: Functions Unavailable on Mac
===========================================

Excel for Mac: Functions Unavailable on Mac
===========================================

1 March 2024

_This week in our series about Microsoft Excel for Mac, we summarise a few worksheet functions that either aren’t supported on Mac or work slightly differently than their counterparts on a PC._

**_Functions to be aware of_**

Through the years, a few functions have been created for Excel on Windows that make use of special features of the Windows operating system. These, of course, don’t work when those special features aren’t available, as when running on macOS.

These are the functions:

**ENCODEURL**

This function is used to replace certain non-alphanumeric characters in a string of text with the percentage symbol (**%**) and a hexadecimal number. The example below shows how this works for the string [https://www.sumproduct.com/](https://www.sumproduct.com/)
, which gets converted to “https%3A%2F%2Fwww.sumproduct.com%2F”:

![](https://sumproduct.com/wp-content/uploads/2025/05/0bc6f7fab1e6ee39a72218206c8c4092.jpg)

The screen shot below shows that the formula **\=ENCODEURL(A2)** returns an _#NAME?_ error, indicating that the function is not supported on Mac

![](https://sumproduct.com/wp-content/uploads/2025/05/d94ab38ecb617ab21dbcf0c404799ffe.jpg)

**FILTERXML**

This returns specific data from XML content by using the specified xpath. This function relies on XML processing capability of the Windows OS, so it will also return the error _#NAME?_ error on Mac

**WEBSERVICE**

This returns data from a web service on the Internet or Intranet. It’s also not supported on Mac and will result with another _#NAME?_ error. The data returned would typically be further processed using the **FILTERXML** function, which as above, is not supported on Mac.

Check back for more details about Excel for Mac and how it’s different to Excel for Windows.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/excel-for-mac-functions-unavailable-on-mac/#0)
    
*   [Register](https://sumproduct.com/blog/excel-for-mac-functions-unavailable-on-mac/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/excel-for-mac-functions-unavailable-on-mac/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/excel-for-mac-functions-unavailable-on-mac/#0)

[](https://sumproduct.com/blog/excel-for-mac-functions-unavailable-on-mac/#0 "close")

top
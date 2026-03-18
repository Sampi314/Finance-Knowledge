# A to Z of Excel Functions: The IMPORTCSV Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-importcsv-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The IMPORTCSV Function

*   February 2, 2026

A to Z of Excel Functions: The IMPORTCSV Function
=================================================

_Welcome back to our regular A to Z of Excel Functions blog.  Today we look at the **IMPORTCSV** function._

**The IMPORTCSV function**

![](<Base64-Image-Removed>)

One of the new Import Functions, **IMPORTCSV** represents a more intuitive way for you to import data from a CSV file.  It provides a simpler way to bring in comma-delimited data as a dynamic array, with options to skip or take rows and apply locale settings for regional formatting.

Note: Bringing the data in using a dynamic array highlights this function will not work in all versions of Excel (for now, at least).  Presently, this feature is currently Generally Available to Microsoft 365 subscribers enrolled in the Insiders Beta channel, running Version 2502 (Build 18604.20002) or later in Excel for Windows.

Its syntax is as follows:

> **IMPORTCSV(path, \[skip\_rows\], \[take\_rows\], \[locale\])**

where:

*   **path** is required and represents the local file path or URL of the CSV file that you wish to import
*   **skip\_rows** is optional and is the number that specifies how many rows to skip.  A negative value skips rows from the end of the array instead
*   **take\_rows** is another optional argument.  It is the number that specifies how many rows to return.  A negative value takes rows from the end of the array
*   **locale** is the final optional argument.  This determines regional formatting (_e.g_. date, number formats).  By default, the operating system (OS) locale is used.

It should be noted that:

*   **IMPORTCSV** is an Import Function.  Import Functions do not automatically refresh.  To update imported data, use the ‘Refresh All’ button on the Data tab of the Ribbon  
      
    
*   the **IMPORTCSV** function is a simplified version of **IMPORTTEXT** that expects comma delimiters and **UTF-8** encoding.  For more flexibility, including support for multiple delimiters, encoding and fixed-width columns, you should use the **IMPORTTEXT** function.

When importing a file from the web, you may need to provide credentials or sign in to access the source file.  In such cases, you will be prompted to select the authentication method to use for the provided URL through an authentication dialog, _viz._

![](<Base64-Image-Removed>)

The available authentication methods are:

*   **Anonymous:** select this authentication method when the content is publicly accessible and does not require sign-in
*   **Windows:** select this authentication method when accessing a resource that requires your Windows credentials
*   **Basic:** select this authentication method when the resource requires a username and password
*   **Web API:** select this method if the web resource that you’re connecting to uses an API Key for authentication purposes
*   **Organizational account:** select this authentication method if the resource requires organisational account credentials.

To clear permissions given during the authentication process, click on **Data -> Get Data -> ‘Data Source Settings…’**.  Then, under the ‘Global Permissions’ tab, select the relevant URL path and click on ‘Clear Permissions’:

![](<Base64-Image-Removed>)

As an example, imagine you have the following file in my local file directory (how did you get it in there?).  The location is:

> **E:\\Main\\Admin\\Liam Bastick\\New Functions**

Imagine there is January 2026 data here called Jan 2026.csv.  Note no quotation marks should be used:

> **\=IMPORTCSV(“E:\\Main\\Admin\\Liam Bastick\\New Functions\\Jan 2026.csv”)**

![](<Base64-Image-Removed>)

Skipping the first row removes the headers:

> **\=IMPORTCSV(“E:\\Main\\Admin\\Liam Bastick\\New Functions\\Jan 2026.csv”, 1)**

![](<Base64-Image-Removed>)

If we only want to show the first 10 rows, we can use the fourth argument to **take** rows:

> **\=IMPORTCSV(“E:\\Main\\Admin\\Liam Bastick\\New Functions\\Jan 2026.csv”, 1, 10)**

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://sumproduct.com/thought/a-to-z-of-excel-functions)
._

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-importcsv-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-importcsv-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-importcsv-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-importcsv-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-importcsv-function/#0 "close")

top
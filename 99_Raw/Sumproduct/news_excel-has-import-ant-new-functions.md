# Excel Has Import-ant New Functions

**Source:** https://sumproduct.com/news/excel-has-import-ant-new-functions/

---

[Home](https://sumproduct.com/)

\> Excel Has Import-ant New Functions

*   January 16, 2026

Excel Has Import-ant New Functions
==================================

![](https://sumproduct.com/wp-content/uploads/2026/01/Image1-1-1024x576.png)

So Power Query, Copilot and Agent Mode were not enough!  Bringing data into Excel is an important aspect of so many spreadsheets, yet it can be fraught with unnecessary peril.  Get & Transform, The Artist Formerly Known as Power Query, is readily used to load data, but sometimes it does seem, well, a little too much like using a thermonuclear warhead to crack a nut. 

Many of us work with text (.txt) and CSV files regularly, and Microsoft has acknowledged this with the advent of two new functions into the fold – namely **IMPORTCSV** and **IMPORTTEXT** – very **IMPORT**ant functions indeed!

**_IMPORTCSV_**

The first of two new import functions (maybe more to come?), **IMPORTCSV** represents a more intuitive way for you to import data from a CSV file.  It provides a simpler way to bring in comma-delimited data as a dynamic array, with options to skip or take rows and apply locale settings for regional formatting.

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
*   the **IMPORTCSV** function is a simplified version of **IMPORTTEXT** _(see below)_ that expects comma delimiters and **UTF-8** encoding.  For more flexibility, including support for multiple delimiters, encoding and fixed-width columns, you should use the **IMPORTTEXT** function.

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

As an example, imagine you have a file in my local file directory (how did you get it in there?).  The location is:

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

**_IMPORTTEXT_**

A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here.  A bit of repetition here…

The second of these two new import functions, **IMPORTTEXT** represents a more intuitive way for you to import data from a text (.txt) file.  It may also be used for CSV and TSV files as well.  It provides a simpler way to bring in text-based data as a dynamic array, with options to skip or take rows and apply locale settings for regional formatting.

Note: Again, bringing the data in using a dynamic array highlights this function will not work in all versions of Excel (for now, at least).  Presently, this feature is currently Generally Available to Microsoft 365 subscribers enrolled in the Insiders Beta channel, running Version 2502 (Build 18604.20002) or later in Excel for Windows.

Its syntax is as follows:

> **IMPORTTEXT(path, \[delimiter\], \[skip\_rows\], \[take\_rows\], \[encoding\], \[locale\])**

where:

*   **path** is required and represents the local file path or URL of the text-based file that you wish to import
*   **delimiter** is an optional argument that is a character or string that specifies how columns are separated in the file.  If omitted, the function uses **TAB** as the delimiter
*   **skip\_rows** is also optional and is the number that specifies how many rows to skip.  A negative value skips rows from the end of the array instead
*   **take\_rows** is another optional argument.  It is the number that specifies how many rows to return.  A negative value takes rows from the end of the array
*   **encoding** is also not required but denotes the file encoding.  By default, **UTF-8** is used
*   **locale** is the final optional argument.  This determines regional formatting (_e.g_. date, number formats).  By default, the operating system (OS) locale is used.

It should be noted that:

*   **IMPORTTEXT** is an Import Function.  Import Functions do not automatically refresh.  To update imported data, use the ‘Refresh All’ button on the Data tab of the Ribbon
*   You may specify fixed-width columns by passing a comma-separated array of ascending integers in the delimiter argument, _e.g._  
    **\=IMPORTTEXT(“C:\\Data\\fixedwidth.txt”, {1,3})**
*   you may use the **CHAR** function to specify special characters for the delimiter argument

*   you can use the **IMPORTCSV** function as an easier alternative for importing **CSV** files.

Just in case you skipped the first function’s notes, let me reiterate.  When importing a file from the web, you may need to provide credentials or sign in to access the source file.  In such cases, you will be prompted to select the authentication method to use for the provided URL through an authentication dialog, _viz._

![](<Base64-Image-Removed>)

The available authentication methods are:

*   **Anonymous:** select this authentication method when the content is publicly accessible and does not require sign-in
*   **Windows:** select this authentication method when accessing a resource that requires your Windows credentials
*   **Basic:** select this authentication method when the resource requires a username and password
*   **Web API:** select this method if the web resource that you’re connecting to uses an API Key for authentication purposes
*   **Organizational account:** select this authentication method if the resource requires organisational account credentials.

To clear permissions given during the authentication process, click on **Data -> Get Data -> ‘Data Source Settings…’**.  Then, under the ‘Global Permissions’ tab, select the relevant URL path and click on ‘Clear Permissions’:

![](<Base64-Image-Removed>)

As an example, imagine you have a file in my local file directory.  The location remains:

> **E:\\Main\\Admin\\Liam Bastick\\New Functions**

Once more, there is January 2026 data here called Jan 2026.csv.  Note no single quotation marks should be used for file names with spaces, such as **Jan 2026**:

> **\=IMPORTTEXT(“E:\\Main\\Admin\\Liam Bastick\\New Functions\\Jan 2026.csv”)**

![](<Base64-Image-Removed>)

This looks much better if we cite the comma as the delimiter:

> **\=IMPORTTEXT(“E:\\Main\\Admin\\Liam Bastick\\New Functions\\Jan 2026.csv”, “,”)**

![](<Base64-Image-Removed>)

The effects of using **locale** may be difficult show when we have used 1 January (!), but you probably get the idea.  More striking, skipping the first row removes the headers:

> **\=IMPORTTEXT(“E:\\Main\\Admin\\Liam Bastick\\New Functions\\Jan 2026.csv”, “,”, 1)**

If we only want to show the first 10 rows, we can use the fourth argument to **take** rows:

> **\=IMPORTTEXT(“E:\\Main\\Admin\\Liam Bastick\\New Functions\\Jan 2026.csv”, “,”, 1, 10)**

![](<Base64-Image-Removed>)

Who needs Power Query?  But yes, you do need the Beta Channel and dynamic arrays! 😊

*   [Log in](https://sumproduct.com/news/excel-has-import-ant-new-functions/#0)
    
*   [Register](https://sumproduct.com/news/excel-has-import-ant-new-functions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/excel-has-import-ant-new-functions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/excel-has-import-ant-new-functions/#0)

[](https://sumproduct.com/news/excel-has-import-ant-new-functions/#0 "close")

top
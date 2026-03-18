# A to Z of Excel Functions: The RTD Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rtd-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The RTD Function

*   March 10, 2025

A to Z of Excel Functions: The RTD Function
===========================================

A to Z of Excel Functions: The RTD Function
===========================================

10 March 2025

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **RTD** function._

**The RTD Function**

![](<Base64-Image-Removed>)

The **RTD** function will retrieve real time data from a program that supports COM automation. This can be useful, as it assists in refreshing values from real-time data servers in Excel spreadsheets. You may use cell values as formula arguments and build powerful refreshable data sheets and models in a few minutes.

Microsoft Office Excel provides a worksheet function, **RTD**. This function enables you to call a Component Object Model (COM) Automation server to retrieve data in real time. When you have to create a workbook that includes data that is updated in real time, for example, financial data or scientific data, you can now use the RTD worksheet function.

In earlier versions of Excel, Dynamic Data Exchange (DDE) is used for that purpose. The **RTD** function is based on COM technology and provides advantages in robustness, reliability and convenience. **RTD** depends on the availability of an RTD server to make the real-time data available to Excel.

The **RTD** function retrieves data from an RTD server for use in the workbook. The function result is updated whenever new data becomes available from the server and the workbook can accept it. The server waits until Excel is idle before updating. This relieves the developer of having to determine whether Excel is available to accept updates. The **RTD** function differs from other functions in this regard because other functions are updated only when the worksheet is recalculated.

Although the RTD function provides a link to data on a server, it is not the same type of link as references to cells in other worksheets or workbooks. For example, if you use the **RTD** function in a workbook, you do not receive the Links startup message when you open the workbook, nor can you manage the status of an **RTD** function through the ‘Edit Links’ dialog box.

The function Real Time Data, **RTD**, has the following syntax:

**RTD(ProgID,  
server, topic1, \[topic2\], …)**

The **RTD** function syntax has the following arguments:

*   **ProgID:** this is required and represents the name of the **ProgID** of a registered COM automation add-in that has been installed on the local computer. You should enclose the name in quotation marks (**“**Name**”**)

*   **server:** this is also required. This is the name of the server where the add-in should be run. If there is no server, and the program is run locally, leave the argument blank. Otherwise, enter quotation marks (**“”**) around the server name. When using **RTD** within Visual Basic for Applications (VBA), double quotation marks or the **VBA NullString** property are required for the server, even if the server is running locally

*   **topic1, topic2, …:** whilst **topic1** is required, subsequent topics are optional. There can be one \[1\] to 253 parameters that together represent a unique piece of real-time data.

It should be noted that:

*   the **RTD** COM automation add-in must be created and registered on a local computer. If you haven’t installed a real-time data server, you will get an error message in a cell when you try to use the **RTD** function
*   when the server has been programmed to continually update results, unlike other functions, **RTD** formulae will change when Microsoft Excel is in automatic calculation mode.

Consider the following example:

![](<Base64-Image-Removed>)

Rather than use **[STOCKHISTORY](https://www.sumproduct.com/news/article/brand-new-excel-function-stockhistory)
** or some other approach, you could use Yahoo! Finance with the **RTD** function, _viz._

**\=RTD(“progid”,,“YahooFinanceWatchList”,“BHP”,“Open”)**

the RTD COM automation add-in must be installed and registered on the computer. If you haven’t installed a real-time data server, the **RTD** function returns the _#NAME?_ error

*   no RTD servers are shipped with Microsoft Office, so you must manually install a real-time data server if you wish to use the function
*   the “progID” must be enclosed in quotation marks
*   the “server” must be enclosed in quotation marks
*   if the real-time data server is being run locally, leave the “server” argument blank
*   the function will only continuously update when the calculation mode is set to automatic
*   when using RTD within Visual Basic for Applications (VBA), double quotation marks or the VBA **NullString** property is required for the server, even if the server is running locally
*   **N/A error:** RTD servers should be digitally signed. If an RTD server is not digitally signed, the server may not load, and an _#N/A_ error will be displayed in the cell(s) referencing the RTD server.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rtd-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rtd-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rtd-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rtd-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rtd-function/#0 "close")

top
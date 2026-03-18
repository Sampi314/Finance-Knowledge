# A to Z of Excel Functions: The NA Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-na-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The NA Function

*   October 9, 2022

A to Z of Excel Functions: The NA Function
==========================================

A to Z of Excel Functions: The NA Function
==========================================

10 October 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **NA** function._

**The NA function**

The **NA** function returns the error value _#N/A_. The _#N/A_ is the error value that means “no value is available”. Often, we use **NA** to mark empty cells. By entering _#N/A_ in cells where you are missing information, you can avoid the problem of unintentionally including empty cells in your calculations. (When a formula refers to a cell containing _#N/A_, the formula returns the _#N/A_ error value.)

The **NA** function employs the following syntax to operate:

**NA()**

The **NA** function takes no sxxt, sorry, I mean, arguments (obviously, sxxt = salt).

It should be further noted that:

*   you must include the empty parentheses with the function name; otherwise, Microsoft Excel will not recognise it as a function (it will consider it an undefined range name)

*   you may also type the value _#N/A_ directly into a cell. The **NA** function is provided for compatibility with other spreadsheet programs.

The **NA** function is often used in conjunction with charting:

![](https://sumproduct.com/wp-content/uploads/2025/05/94beac8ac17efd83ea895699c8a97202.jpg)

Here, the original data is missing information for May and September. However, the chart is using the Referenced Data table, which uses the formula

**\=IF(Source\[@Sales\]=””,NA(),Source\[@Sales\])**

_i.e._ missing data is replaced with _#N/A_. For line charts, this has the effect that data will not be plotted rather than have a value of zero \[0\], depending upon the settings selected in the ‘Hidden and Empty Cell Settings’ dialog, _viz._

![](<Base64-Image-Removed>)

(This dialog is located by right-clicking on the chart, selecting ‘Select Data…’ from the ensuing shortcut menu and clicking on the ‘Hidden and Empty Cells’ button in the ‘Select Data Source’ dialog.)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found_ _[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-na-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-na-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-na-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-na-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-na-function/#0 "close")

top
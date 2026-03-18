# Excel Office 365 Performance Improvements

**Source:** https://sumproduct.com/news/excel-office-365-performance-improvements/

---

[Home](https://sumproduct.com/)

\> Excel Office 365 Performance Improvements

*   October 15, 2017

Excel Office 365 Performance Improvements
=========================================

Excel Office 365 Performance Improvements
=========================================

15 October 2017

You remember when you installed Office and the installation process asked you whether you wanted to submit telemetry back to Redmond? Well, some of you said “yes” and as a consequence, Microsoft has been identifying some specific examples of slow, high CPU or out of memory performance issues. These have included:

*   Slow copying and pasting of one column, in a sheet comprising of lots of rows of data with many filtered
*   Slow copying and pasting of many cells on a sheet with lots conditional formatting rules
*   Slow performance or hanging when selecting cells after filtering or sorting rows from amongst lots of rows of data in a sheet
*   High CPU opening a workbook with one or more sheets with lots of rows filtered, containing merged cells and / or grouping
*   Slow when creating, deleting and / or editing sheet names in a workbook with lots of worksheets
*   High CPU and / or out of memory errors opening a workbook with lots of formulae (with full column references (_e.g._**VLOOKUP** over **A:A**) and / or multiple sheets
*   Slow with deleting rows in a workbook with lots of formulae with full column references (_e.g._**A:A**).

So, if you thought it was just you – it isn’t. Microsoft has been busy fixing these issues They have addressed each example above in the following ways:

*   While copying and pasting, Excel is now more intelligent in detecting the need to trigger time-consuming object searches before initiating them
*   While copying and pasting with conditional formatting (this is never a good thing!), the algorithm in Excel has now been “optimised” to consume time, proportional to the number of conditionally formatted cells involved
*   While selecting cells in the visible sheet, after an operation, Excel re-renders (or at least evaluates) all rows top to bottom (including filtered rows) in the visible sheet. This may be expensive from a resource perspective, depending upon the number of rows and Excel’s ability to calculate for animation related rendering (do consider turning this option off). This new optimisation caches prior rendered calculations for animation support and reduces time during each such calculation
*   While opening a workbook and rendering lots of rows with merged cells, Excel is now more intelligent in detecting the need to perform time-consuming merged cell rendering calculations before actually calculating
*   During sheet operations, the new fix ensures expensive sheet tab dimension calculations are performed optimally. Time savings here augment VBA to perform bulk sheet operations faster too
*   While deleting rows that contain formulae with full column references, _e.g._**A:A**, Excel optimises in bulk for all rows. This saves memory for such formulae and in turn reduces overhead for subsequent delete, edit and / or update operations involving them. However, we still strongly suggest never to have formulae reference an entire row or column.

These updates / optimisations / fixes apply to Excel O365 Version **16.0.8431.2058** or later updates, presently available to Office Insiders. Microsoft invites feedback – good or bad – on these modifications at for a such as [www.excel.uservoice.com](http://www.excel.uservoice.com/)
.

![](<Base64-Image-Removed>)

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/excel-office-365-performance-improvements/#0)
    
*   [Register](https://sumproduct.com/news/excel-office-365-performance-improvements/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/excel-office-365-performance-improvements/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/excel-office-365-performance-improvements/#0)

[](https://sumproduct.com/news/excel-office-365-performance-improvements/#0 "close")

top
# Hyperlinking Chart Sheets

**Source:** https://sumproduct.com/thought/hyperlinking-chart-sheets/

---

[Home](https://sumproduct.com/)

\> Hyperlinking Chart Sheets

*   May 14, 2025

Hyperlinking Chart Sheets
=========================

You can't hyperlink to and from chart sheets in Excel. Or can you.?.

Charting Hyperlinks
===================

You can’t hyperlink to and from chart sheets in Excel. Or can you..?. By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

I have started to use hyperlinks in my spreadsheets as a way of navigating around the workbook. However, I cannot create hyperlinks either to or from chart sheets. Any ideas?

Advice
------

Regular readers of these articles will have noted that I commonly use hyperlinks in my Excel files as they are a great way to move around a file. Once you know how to construct them, they take seconds to insert.

The ‘Insert Hyperlink’ dialog box is fairly straightforward to use and readily accessed via one of two keyboard shortcuts, either ALT + I + I or CTRL + K. Alternatively:

### Excel 2003 and earlier

*   From Insert drop down menu, select Hyperlink

![](https://sumproduct.com/wp-content/uploads/2025/05/image-01-insert-hyperlink-2003.gif)

### Excel 2007

*   From the Ribbon, select the Insert tab and click on the Links group

![](https://sumproduct.com/wp-content/uploads/2025/05/image-02-insert-hyperlink-2007.gif)

To create a hyperlink, first select the cell or range of cells that you wish to act as the hyperlink (i.e. clicking on any of these cells will activate the hyperlink). Then, open the Insert Hyperlink dialog box (above) and select ‘Place in This Document’ as the ‘Link to:’, which will change the appearance of the rest of the dialog box.

Insert the text for the hyperlink in the ‘Text to display:’ input box (clicking on the ‘ScreenTip…’ macro button will allow you to create an informative message in a message box when you hover over the hyperlink).

The next two input boxes, ‘Type the cell reference:’ and ‘Or select a place in this document:’, work in tandem – sort of:

*   If you type a cell reference in the first input box without making a selection in the second input box, the hyperlink will link to the cell reference on the current (active) worksheet;
*   If you type a cell reference in the first input box and select a worksheet reference in the second box, the hyperlink will link to the specified cell in the given worksheet. In my example above, this hyperlink will jump to Sheet1 cell A1; or
*   If you select a ‘Defined Name’ (i.e. a pre-defined range name) in the second input box, this will link to the cell(s) specified. This is the recommended option, where available, if you wish to link to cell(s) on another worksheet within the same workbook. This is because if the destination worksheet’s sheet name were to be changed, the link would still work.

So what is the problem in the case of our query? Simple: Excel will not let you link to chart sheets and range names cannot be attached to chart sheets – hence, seemingly no way to link to the worksheet. Most model developers will circumvent this issue by embedding their charts in Excel spreadsheets and then it’s easy. But what if you don’t want to do this for some reason (e.g. some Management Information Systems require charts to be on their own worksheets)?

There is an Excel function, **HYPERLINK(link\_location,\[friendly\_name\])**, but this does not help us either as there is no cell on a chart sheet to link to. There is a neat workaround, however…

### Linking to a Chart Sheet

Add a new worksheet in the workbook, and then create a new hyperlink as follows:

*   Select the cell (not cells) in the worksheet where you want the chart hyperlink to appear. This cannot be on the worksheet just added for reasons that will become apparent below;
*   Next, create a hyperlink that links to the worksheet just added (it doesn’t matter which cell you choose);
*   The text to display selection is **critical**. I will call it **Critical Text 01**, for this example’s sake, but please call it whatever you wish;
*   Hide the new worksheet just added. This will make our hyperlink ‘dead”, i.e. when you click on it, nothing will happen (hyperlinks cannot jump to hidden worksheets);
*   The chart sheet name is also critical. I will call this **Critical Text 02** for identification purposes;
*   Right click on the worksheet name in the tab for the chart sheet you wish to link from and choose ‘View Code’ from the shortcut menu.

This final step activates Excel’s Visual Basic Editor. The following code should be copied into the Module area of the screen (the large white area usually located on the right hand side):

**Private Sub** Worksheet\_FollowHyperlink(ByVal Target As Hyperlink)

**If** Target.TextToDisplay = “Critical Text 01” **Then** Sheets(“Critical Text 02”).Select

**End Sub**

\[**Critical Text 01** and **Critical Text 02** should be replaced with the relevant text.\]

With the hyperlink dead, clicking on a cell containing a hyperlink will merely test for the required text; if found, it will jump to the chart sheet as requested.

### Linking from a Chart Sheet

The problem with chart sheets is that there is no cell to attach a hyperlink to, so we need to get more inventive:

*   Insert a text box on your chart (in Excel 2003 and earlier, text boxes can be located on the Drawing toolbar, whereas in Excel 2007 it can be inserted from the ‘Insert’ tab of the Ribbon, in the ‘Text’ group, ALT + N + X);
*   Type in the text you want and make it appear to look like a hyperlink by formatting the text (e.g. colour blue and underline);
*   Right hand click on the text box and choose ‘Assign Macro…’ from the shortcut menu \[N.B. Excel 2007 users: ensure ‘Developer’ tab is available and visible before proceeding, see below\];
*   Type a name for the macro and then press the ‘Record’ button;
*   Select the worksheet and cell you want your “pseudo-hyperlink” to jump to;
*   Stop the macro using the ‘Stop’ button (Excel 2003 and earlier) / ‘Stop Recording’ button (on the ‘Developer’ tab in the ‘Code’ group). \[N.B. If the ‘Developer’ tab is not visible, use ALT + T + O to go to the ‘Popular’ Excel Options and check the third check box, ‘Show Developer tab in the Ribbon’.\]

The [attached Excel file](https://sumproduct.com/assets/user-upload/sp-hyperlinking-to-chart-sheets-example.xls)
 should make things clearer.

If you have a query for this section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the website [www.sumproduct.com](https://www.sumproduct.com/)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/hyperlinking-chart-sheets/#0)
    
*   [Register](https://sumproduct.com/thought/hyperlinking-chart-sheets/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/hyperlinking-chart-sheets/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/hyperlinking-chart-sheets/#0)

[](https://sumproduct.com/thought/hyperlinking-chart-sheets/#0 "close")

top
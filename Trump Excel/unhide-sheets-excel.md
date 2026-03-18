# How to Unhide Sheets in Excel (All In One Go)

**Source:** https://trumpexcel.com/unhide-sheets-excel

---

[Skip to content](https://trumpexcel.com/unhide-sheets-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/unhide-sheets-excel/#below-title)

**Watch Video – How to Unhide All Sheets In Excel**

In case you prefer reading a tutorial over watching a video, below is a detailed written tutorial on unhiding sheets in Excel.

When you work with data that is spread across multiple worksheets in Excel, you may want to hide a few worksheets. This could be to avoid the clutter or to not show some data to your client/manager by hiding some worksheets and only keeping the useful ones visible.

And in some cases, you may have a workbook that has some hidden sheets and you want to unhide some or all of these worksheets.

In this tutorial, I will show you some methods to unhide worksheets in Excel (manually as well as automatically using VBA). I will also show you how to selectively unhide worksheets based on the name or a condition.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/unhide-sheets-excel/#)

Unhiding Sheets Manually
------------------------

If you only have a few worksheets that are hidden, you can manually unhide some or all of these worksheets.

Suppose you have an Excel workbook that has 10 worksheets that are hidden.

Below are the steps to manually unhide worksheets (one at a time):

1.  Right-click on any of the existing worksheet tab![Right-Click on any visible sheet name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20230%20327'%3E%3C/svg%3E)
2.  Click on the Unhide option. This will open the Unhide dialog box that lists all the hidden worksheets![Click the Unhide Sheets option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20230%20327'%3E%3C/svg%3E)
3.  In the Unhide dialog box, click on the worksheet that you to unhide (you can only select one at a time).![Select the sheet you want to unhide](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%20263'%3E%3C/svg%3E)
4.  Click OK.![Click OK to unhide the selected sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%20263'%3E%3C/svg%3E)

The above steps would unhide the select worksheet.

**Note**: Unfortunately, there is no in-built functionality in Excel to quickly unhide all the hidden worksheets (or a way to select more than one worksheet and unhide it). As of now, you need to use the unhide dialog box where you can only select one worksheet to unhide.

**You can hide worksheets in bulk, but not unhide in bulk**

If you want to hide worksheets, you can select multiple worksheets at once (hold the control key and click on the worksheet tab name), right-click and click on the Hide option.

Unfortunately, there is no in-built functionality in Excel to quickly unhide all the hidden worksheets (or a way to select more than one worksheet and unhide it). As of now, you need to use the unhide dialog box where you can only select one worksheet to unhide.

While there is no-inbuilt functionality to unhide in bulk, you can easily do this with a simple VBA macro code.

Unhide All Sheets At One Go
---------------------------

With VBA, you can easily unhide worksheets in bulk.

For example, if you have 10 hidden worksheets, you can create a simple VBA code to unhide all the worksheets or you can unhide based on a condition (such as unhide only those where there is a specific prefix or year in the name).

Note: The methods covered in this tutorial doesn’t require you to save an Excel workbook in a macro-enabled format (.XLSM) to use the VBA code.

### Using Immediate Window

[VB Editor in Excel](https://trumpexcel.com/visual-basic-editor/)
 has an immediate window where you can type a line of code and instantly execute it right away.

Below are the steps to use this above line of code to unhide sheets through immediate window:

1.  Right-click on any of the visible sheets in the workbook
2.  Click on View code. This will open the VB Editor.![Click the View code option to open the VB Editor in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20241%20331'%3E%3C/svg%3E)
3.  Click the View option in the menu and then click on the Immediate window. This will make the Immediate window appear in the VB Editor (if not there already).![Click on View and the click on the Immediate Window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20334'%3E%3C/svg%3E)
4.  In the Immediate window, copy and paste the following line of code: _For each Sheet in Thisworkbook.Sheets: Sheet.Visible=True: Next Sheet![Enter the code to unhide sheets in immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20386'%3E%3C/svg%3E)_
5.  Place the cursor at the end of the line![Place the cursor at the end of the line of code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20386'%3E%3C/svg%3E)
6.  Hit the Enter key

That’s it!

The above steps would instantly unhide all the sheets in the workbook.

Once done, you can close the VB Editor.

The best part about this is that you can do this on any workbook. You don’t need to worry about saving the workbook in a macro-enabled format. Just execute a line of code and instantly unhide all the sheets in the workbook.

Let me also quickly explain the below VBA code that we have used in the immediate window to unhide sheets:

For each Sheet in Thisworkbook.Sheets: Sheet.Visible=True: Next Sheet

The above code uses a [For Next VBA loop](https://trumpexcel.com/vba-loops/)
 to go through all the sheets in the workbook and set the visible property to TRUE. Once the visible property of all the sheets is changed, the code will end.

The colon (:) used in the code above is equivalent to a line break. While it looks like a single line of code, it has three parts to it which are separated by two colons.

If you’re interested in learning more about the immediate window and some awesome things you can do with it, [here is a detailed tutorial about it](https://trumpexcel.com/vba-immediate-window/)
.

### By Adding Macro to QAT (with One Click)

In case you have to unhide worksheets quite often, another good way could be to have the macro code to unhide sheets in the [Personal macro workbook](https://trumpexcel.com/personal-macro-workbook/)
 and save the icon in the Quick Access Toolbar.

This is just a one time process and once you have it done, you can then unhide sheets in any workbook by simply clicking on a button in the QAT.

This is by far the most efficient way to unhide sheets in Excel (most useful when you get a lot of workbooks with hidden sheets and you have to unhide these).

The trick here is to save the code to unhide sheets in the Personal Macro Workbook.

A Personal Macro Workbook is something that is always open when you open any Excel file (you can’t see it though). When you save a macro code to the Personal Macro workbook, this code is now always available to you. And when you add this to the QAT and you run the macro code with a single click.

Below is the code that you need to add to the Personal Macro Workbook:

Sub UnhideAllSheets()
For Each Sheet In Sheets
    Sheet.Visible = True
Next Sheet
End Sub

Below are the steps to add this code to the Personal Macro Workbook:

1.  Click on the record macro button (it’s at the bottom left of the Excel workbook application)![Click on record macro icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20286%20170'%3E%3C/svg%3E)
2.  In the Record Macro dialog box, change the Store macro in setting to – Personal Macro Workbook.![Make sure Personal Macro Workbook is the place where macro is stored](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20372'%3E%3C/svg%3E)
3.  Click OK. This will start recording the macro![Click on OK](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20372'%3E%3C/svg%3E)
4.  Click on the Stop macro recording icon (at the bottom left of the workbook). This will stop the macro recording![Click on Stop Macro Recording Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20351%20187'%3E%3C/svg%3E)
5.   Right-click on any sheet tab and then click on ‘View Code’![Click the View code option to open the VB Editor in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20241%20331'%3E%3C/svg%3E)
6.  In the VB Editor, double-click on the Module object in the Personal.XLSB workbook![Double click on the Personal Macro Workbook Module option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20502%20399'%3E%3C/svg%3E)
7.  Remove any existing code and copy and paste the above code.![Copy and Paste the code in the module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20757%20391'%3E%3C/svg%3E)
8.  Click the Save icon in the toolbar![Save the macro in the Personal Macro Workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20757%20391'%3E%3C/svg%3E)
9.  Close the Vb Editor

The above steps allow you to make the Personal Macro Workbook visible in the VB Editor and place the code to unhide sheets in it.

Now all you need to do is add this code to the Quick Access Toolbar so that you can use it anytime from any workbook.

Below are the steps to add this code to the Quick Access Toolbar:

1.  Click on the Customize Quick Access Toolbar icon.![Click on the Customize Quick Access Toolbar icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20115'%3E%3C/svg%3E)
2.  Click on More Commands.![Click on More Commands](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20531'%3E%3C/svg%3E)
3.  In the Excel Options dialog box, click on the ‘Choose Commands from’ drop-down![Click on Choose Commands Drop Down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20338'%3E%3C/svg%3E)
4.  Click on Macros. This will show you a list of all the macros in the workbook (including the ones in PERSONAL.XLSB)![Click on Macros](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20337'%3E%3C/svg%3E)
5.  Select the macro code to unhide sheets![Click on the macro that you want to add to the QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20368'%3E%3C/svg%3E)
6.  Click on the Add button![Click on the Add Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20431'%3E%3C/svg%3E)
7.  Click OK.

The above steps would add this macro code to unhide sheets in the [Quick Access Toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
.

![Macro is added to the QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20349%20115'%3E%3C/svg%3E)

Now, whenever you get a workbook that has some sheets hidden, you just need to click on the code icon in the QAT and it will instantly unhide all sheets in one go.

Unhide Sheets With Specific Text in the Name
--------------------------------------------

With VBA, you can also unhide sheets based on the name.

For example, suppose you have a workbook that contains sheets with years in the name and you want to unhide all the ones where the year is 2020.

You can use the below code to unhide all the sheets with the text 2020 in it:

Sub UnhideSheetsWithSpecificText()
For Each ws In ThisWorkbook.Worksheets
    If InStr(ws.Name, "2020") > 0 Then
        ws.Visible = xlSheetVisible
    End If
Next ws
End Sub

The above uses the For Next loop to go through each worksheet in the workbook. The [IF Then](https://trumpexcel.com/if-then-else-vba/)
 condition then checks the name of the worksheet and if it contains the specified text (which is 2020 in this code), it will change the visible property to make it visible.

And if the name doesn’t contain the specified text, it will leave it as is.

You can also modify this code to hide sheets based on the text in the name.

For example, if you want to quickly hide all the worksheets where the name contains the text ‘2020’ in it, you can use the below code:

Sub HideSheetsWithSpecificText()
For Each ws In ThisWorkbook.Worksheets
    If InStr(ws.Name, "2020") > 0 Then
        ws.Visible = xlHidden
    End If
Next ws
End Sub

**Note**: You can save this code in a regular module inside VB Editor or you can save this in the Personal Macro Workbook. In case you save it in a regular module and need to use it again later, you need to save the workbook as a macro-enabled workbook (.XLSM format).

Unhide Selected Sheets (Based on User Selection)
------------------------------------------------

You can also use VBA to give the user the flexibility to choose whether to unhide a sheet or not.

This can be done by showing a message box that asks the user to select whether to unhide a sheet or not. If selected, it unhides that sheet, else it moves to the next one.

Below is the code that will do this:

Sub UnhideSheetsUserSelection()
For Each sh In ThisWorkbook.Sheets
    If sh.Visible <> True Then
        Result = MsgBox("Do You Want to Unhide " & sh.Name, vbYesNo)
        If Result = vbYes Then sh.Visible = True
    End If
Next sh
End Sub

The above code goes through each sheet in the workbook and checks whether it’s already visible or not. If it’s hidden, then it shows the [message box](https://trumpexcel.com/vba-msgbox/)
 with the name of the worksheet.

As a user, you can now decide whether you want to keep this sheet hidden or unhide it.

This can work well if you have some worksheets that are hidden and you want to take a call for every sheet individually.

**Note**: You can save this code in a regular module inside VB Editor or you can save this in the Personal Macro Workbook. In case you save it in a regular module and need to use it again later, you need to save the workbook as a macro-enabled workbook (.XLSM format).

_[Here is a tutorial](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
 where I show how to save the code in the regular module in Excel (search for the ‘Where to put this code’ section in this article)_

Unhide All or Selected Sheets Using Custom View
-----------------------------------------------

This is a less known method in case you want to quickly unhide all the worksheets (or some selected worksheets).

‘Custom View’ is functionality in Excel that allows you to create and save views that you can quickly resort to with a click of a button.

For example, suppose you have an Excel workbook with 10 worksheets. You can create a view where all these 10 sheets are visible. In the future, if you have some sheets hidden and you want o go back to the view where all the sheets were visible, you can do that by selecting the already saved custom view.

Don’t worry, you don’t lose any changes you made after creating the custom view. All custom view does is takes you back to the Excel view when you created it. So if some worksheets were visible when you created the view and are now hidden, selecting that custom view would unhide these sheets.

The intended use of Custom View is to allow users to create different views. For example, if you’re an analyst, you can create different views for different departments in your organization. So you can have a specific set of worksheets (or cells/rows/columns) visible for one department and another set for another department. Once you have these views, instead of changing this manually, you simply activate the view for a department and it will show you worksheets (or rows/columns) relevant for them only.

Below are the steps to create a custom view in Excel:

1.  Unhide all the worksheets to begin with
2.  Click the View tab
3.  Click on Custom Views![Click on Custom Views option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20202'%3E%3C/svg%3E)
4.  In the Custom Views dialog box, click on Add. This will open the Add view dialog box![Click on Add button in Custom views](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20235'%3E%3C/svg%3E)
5.  Enter any name for this view where all the sheets (or selected sheets) are visible![Enter the Custom view name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20221'%3E%3C/svg%3E)
6.  Click OK.![Click OK to create the custom view](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20221'%3E%3C/svg%3E)

Once the view is created, you can anytime ask Excel to activate this view (which would make all those sheets visible that were visible when you created the view).

Below are the steps to show/activate a custom view:

1.   Click the View tab
2.  Click on Custom Views![Click on Custom Views option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20202'%3E%3C/svg%3E)
3.  In the Custom Views dialog box, select the view that you want to show![Select the custom view](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20235'%3E%3C/svg%3E)
4.  Click on Show button![Click on Show to activate that custom view](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20235'%3E%3C/svg%3E)

This would instantly unhide sheets and show those that were visible when you created that custom view.

Unhiding Sheets that are ‘Very Hidden’
--------------------------------------

Sometimes, despite having some hidden sheets in your workbook, you would not be able to unhide it manually.

This could be because these sheets are not just hidden – these are ‘very hidden’.

When you have hidden sheets in a workbook and you right-click on any tab name, you would see the option to ‘Unhide’ sheets. But if you have sheets are ‘very hidden’ or if there are no hidden sheets, then you would not be able to use this option (it will be greyed out).

You can still unhide these ‘very hidden’ sheets by using the VBA code that we have covered above.

Just copy-paste the below code in the immediate window and hit enter and it would instantly unhide all the sheets (hidden as well as very hidden).

For each Sheet in Thisworkbook.Sheets: Sheet.Visible=True: Next Sheet

I also have a full tutorial on how to [hide sheets and make these very hidden](https://trumpexcel.com/hide-worksheet/)
 (in case you’re interested in learning)

**You may also like the following Excel tutorials:**

*   [How to Quickly Unhide COLUMNS in Excel](https://trumpexcel.com/unhide-columns/)
    
*   [How to Rename a Sheet in Excel](https://trumpexcel.com/rename-sheet-in-excel/)
    
*   [Delete Rows Based on a Cell Value (or Condition) in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)
    
*   [Hide Zero Values in Excel](https://trumpexcel.com/hide-zero-values-excel/)
    
*   [Working with Worksheets using Excel VBA](https://trumpexcel.com/vba-worksheets/)
    
*   [How to Group Worksheets in Excel](https://trumpexcel.com/group-worksheets-in-excel/)
    
*   [How to Delete All Hidden Rows and Columns in Excel](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/)
    
*   [Excel Tabs/Sheets Not Showing – How to Fix?](https://trumpexcel.com/excel-tabs-sheets-not-showing/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/unhide-sheets-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK
# How to Hide a Worksheet in Excel (that can not be unhidden)

**Source:** https://trumpexcel.com/hide-worksheet

---

[Skip to content](https://trumpexcel.com/hide-worksheet/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/hide-worksheet/#below-title)

Hiding and Unhiding worksheets in Excel is a straightforward task.

You can hide a worksheet and the user would not see it when he/she opens the workbook. However, they can easily unhide the worksheet if they want (as we will see later in this tutorial).

But what if you don’t want them to be able to unhide the worksheet(s).

To do that, you need to take a couple of additional steps to make sure the worksheets are ‘very hidden’ (also covered later in this tutorial).

Let’s see how to hide a worksheet in Excel so that it can easily be unhidden, or can not be unhidden.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/hide-worksheet/#)

Regular Way of Hiding a Worksheet in Excel
------------------------------------------

You can use the below steps to hide a worksheet in Excel:

*   Right-click on the sheet tab that you want to hide.
*   Click on Hide.![Hide a worksheet in Excel - right click and select Hide](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20202%20268'%3E%3C/svg%3E)

This would instantly hide the worksheet, and you will not see it in the workbook. This setting remains intact when you save the workbook and reopen it again, or send it to some else.

**PRO TIP:** To [hide multiple sheets at one go](https://trumpexcel.com/hide-worksheet/_wp_link_placeholder)
, hold the Control key and then select the sheet tabs (that you want to hide) one by one. Once selected, right-click on any one of the selected tabs and click on ‘Hide”. This will hide all the worksheets at one go.

While this method hides the worksheet, it’s extremely easy to unhide these worksheets as well.

Here are the steps to unhide a worksheet in Excel:

*   Right-click on any of the existing tabs.
*   Click on Unhide.![Right click and select Unhide option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20196%20263'%3E%3C/svg%3E)
*   In the Unhide dialog box, select the sheet you want to unhide.![Select the sheet you want to unhide in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20316%20204'%3E%3C/svg%3E)
*   Click OK.

This will instantly make the sheet visible in the workbook.

Note that you can only unhide one sheet at a time. To unhide multiple sheets, you need to repeat the above steps to unhide each worksheet. Alternately, you can use a macro code to [unhide all the worksheets at one go](https://trumpexcel.com/hide-worksheet/#HideUnhide_Worksheets_Using_VBA)
.

While this method works in most cases, it doesn’t really help if you want to hide the worksheets so that your client or colleague (or anyone with whom you share the workbook) can’t unhide and view these.

All they need to do is right-click on any of the tabs and they will see what all worksheets are hidden (and unhide these easily).

So let’s see how you can really hide a worksheet so that it can not be unhidden (at least not so easily).

Hide a Worksheet So That It Can Not be Unhidden
-----------------------------------------------

Here are the steps to hide a worksheet so that it can not be unhidden:

*   Right-click on any of the worksheet tabs.
*   Click on View Code.![hide worksheet in Excel - right click and view code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20186%20260'%3E%3C/svg%3E)
*   In the VB Editor, in the project explorer in VB Editor, select the worksheet you want to hide.![To hide a worksheet - select Sheet2 in the Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20220'%3E%3C/svg%3E)
*   With the sheet selected, click on the Properties icon in the toolbar (or use the keyboard shortcut F4).![Properties Icon in the Vb Editor Toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20439%20236'%3E%3C/svg%3E)
*   In the Properties pane that opens, select the drop-down in front of the option “Visible”.![Visible Property of the worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20292%20336'%3E%3C/svg%3E)
*   Select ‘2 – xlSheetVeryHidden’.![xlSheetVeryHidden selected to hide the worksheet in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20287%20331'%3E%3C/svg%3E)
*   Close the VB Editor.

Now you will notice that the sheet is hidden.

When you right-click on any of the tabs, you will not see it in the list of hidden sheets that you can unhide.

**Is this method foolproof? –** _NO!_

This method works as a user can not see the hidden sheet in the list of sheets that he/she can unhide.

But this doesn’t mean that the sheet can’t be unhidden.

Unhide a Sheet that has been ‘Very Hidden’
------------------------------------------

Here are the steps to unhide a sheet that has been ‘Very Hidden’:

*   Right-click on any of the existing tabs.
*   Click on View Code.![hide worksheet in Excel - right click and view code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20186%20260'%3E%3C/svg%3E)
*   In the VB Editor, click on the sheet name you want to unhide (it will be available in the project explorer as a part of the Workbook objects).![To hide a worksheet - select Sheet2 in the Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20220'%3E%3C/svg%3E)
*   If the properties pane is not visible, click on the Properties icon in the toolbar (or use the keyboard shortcut F4).![Properties Icon in the Vb Editor Toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20439%20236'%3E%3C/svg%3E)
*   In the Properties pane, change the Visible property from ‘2 – xlSheetVeryHidden’ to ‘-1 – xlSheetVisible’.![make sheet visible to unhide it in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20291%20298'%3E%3C/svg%3E)
*   Close the VB Editor.

This will unhide the worksheet and it will be visible in the workbook.

Hide/Unhide Worksheets Using VBA
--------------------------------

If you have a lot of worksheets that you need to hide/unhide, it can take up a lot of your time.

Using a simple VBA code can automate this task for you.

**Hide All Worksheets Using VBA**

Below is the VBA code that will hide all the worksheets except the current/active worksheet:

'This macro will hide all the worksheet except the active sheet
Sub HideAllExceptActiveSheet()
Dim ws As Worksheet
For Each ws In ThisWorkbook.Worksheets
If ws.Name <> ActiveSheet.Name Then ws.Visible = xlSheetHidden
Next ws
End Sub

The above code would hide all the worksheet except the except the active sheet. However, it will hide it so that these can be unhidden easily (note that ws.Visible property is set to xlSheetHidden).

If you want to hide the sheets so that these can not be unhidden, use the below code:

'This macro will hide all the worksheet except the active sheet
Sub HideAllExcetActiveSheet()
Dim ws As Worksheet
For Each ws In ThisWorkbook.Worksheets
If ws.Name <> ActiveSheet.Name Then ws.Visible = xlSheetVeryHidden
Next ws
End Sub

The only change we have done here is making the ws_.Visible_ property _xlSheetVeryHidden_.

**Unhide All Worksheets Using VBA**

Below is the code that will unhide all the hidden worksheets in the workbook.

'This code will unhide all sheets in the workbook
Sub UnhideAllWoksheets()
Dim ws As Worksheet
For Each ws In ThisWorkbook.Worksheets
ws.Visible = xlSheetVisible
Next ws
End Sub

Using this code, we simply go through each worksheet one by one and make the ws_.Visible_ property equal to _xlSheetVisible_.

**Where to put the code?**

Below are the steps to place the code in the VB Editor:

*   Click on the Developer tab.![Developer tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20132'%3E%3C/svg%3E)
*   Click on the Visual Basic icon (or use the keyboard shortcut – ALT + F11).![Visual Basic icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20132'%3E%3C/svg%3E)
*   In the VB Editor, right-click on any of the objects of the workbook.
*   Go to Insert and select Module. This will insert a new module in the workbook.![Insert module to copy code to hide and unhide sheet in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20340'%3E%3C/svg%3E)
*   Double click on the Module icon and copy and paste the code in the module code window.![Paste the code to hide unhide worksheet in the module window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20728%20254'%3E%3C/svg%3E)

Now you can assign the macro to a shape or run it from the Developer tab. You can read more about different ways to [run a macro in Excel here](https://trumpexcel.com/run-a-macro-excel/)
.

Note that you don’t need to insert a new module for each code. You can have one single module and have multiple VBA macro codes in it.

**You May Also Like the Following Excel Tutorials:**

*   [Unhide Columns in Excel](https://trumpexcel.com/unhide-columns/)
     (A Simple Step-by-step Guide)
*   [How to Unhide Sheets in Excel (All In One Go)](https://trumpexcel.com/unhide-sheets-excel/)
    
*   [How to Create and Use an Excel Add-in](https://trumpexcel.com/excel-add-in/)
    .
*   [Useful Excel Macros for Beginners](https://trumpexcel.com/excel-macro-examples/)
    .
*   [How to Lock Cells in Excel.](https://trumpexcel.com/lock-cells-in-excel/)
    
*   [How to Lock Formulas in Excel.](https://trumpexcel.com/lock-formulas-excel/)
    
*   [Hide Zero Values in Excel](https://trumpexcel.com/hide-zero-values-excel/)
    
*   [How to Delete All Hidden Rows and Columns in Excel](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/)
    
*   [How to Hide or Show Formula Bar in Excel?](https://trumpexcel.com/show-hide-formula-bar-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Hide a Worksheet in Excel (that can not be unhidden)”
---------------------------------------------------------------------------

1.  thank you so much sir, ‘superb trick’
    
    [Reply](https://trumpexcel.com/hide-worksheet/#comment-13291)
    
2.  THANKS THANKS THANKS 3x
    
    [Reply](https://trumpexcel.com/hide-worksheet/#comment-10303)
    
3.  Very nice. THANKS.
    
    [Reply](https://trumpexcel.com/hide-worksheet/#comment-9730)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/hide-worksheet/#respond)

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
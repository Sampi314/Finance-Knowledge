# How to Delete Named Range in Excel? 2 Easy Ways!

**Source:** https://trumpexcel.com/delete-named-range-excel

---

[Skip to content](https://trumpexcel.com/delete-named-range-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/delete-named-range-excel/#below-title)

[Named Ranges](https://trumpexcel.com/named-ranges-in-excel/)
 can be extremely useful when you’re working with a lot of data and formulas.

Named ranges allow you to quickly name a cell or a range of cells so that instead of using the reference, you can use those names in the formulas.

And when you get hooked to using named ranged, there is a possibility that you may end up creating a lot of named ranges and may want to delete some or all of them.

In this short tutorial, I will show you two simple ways to **delete named ranges in Excel**. You can choose to delete all the named ranges in one go, or you can choose manually or filter these and then delete them.

I will also show you how to delete named cells and range using VBA.

So let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/delete-named-range-excel/#)

Delete Named Ranges Using Name Manager
--------------------------------------

Excel has **Name Manager** – which is a place where you can manage all the named ranges (create, edit or delete).

So, if you want to delete some or all of the named ranges from your workbook, you can do that using the Name Manager.

Below are the steps to delete named ranges using the Name Manager:

1.  Click the Formula tab in the ribbon

![Click the Formula tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20222'%3E%3C/svg%3E)

2.  In the Defined Names group, click on Name Manager. This will open the Name Manager dialog box that lists all the named ranges in the workbook

![Click on Name Manager icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20622%20222'%3E%3C/svg%3E)

3.  Select the one that you want to delete
4.  Click the Delete button

![Click the Delete button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20469'%3E%3C/svg%3E)

The above steps would delete the selected Named Range from the workbook.

In case you want to delete multiple named ranges at one go, you can do that by selecting the ones you want to delete and then clicking the Delete button.

To select multiple Named Ranges, hold the Control key and then select the Named Ranges one by one. In case you want to select a block of Named Ranges in one go, select the first one, hold the SHIFT key, and then select the last one. This will select all the Named Ranges in between and you can delete all of these in one go.

### Filtering Named Ranges

As you become more proficient with Excel and start using Named Ranges regularly, there is a possibility that you will have a lot of named cells and ranges in a workbook.

While the Name Manager does make it easy to handle these named ranges, it could still become quite cumbersome when you have a lot of these.

Name Manager allows you to quickly filter Named Ranges based on the following criteria:

*   Names scoped to the worksheet
*   Names scoped to the workbook
*   Names with errors
*   Named without errors
*   Defined Names
*   Table Names

You can use these filters from the Name Manager itself (using the [Filter option](https://trumpexcel.com/excel-data-filter/)
 at the top-right of the Name Manager dialog box)

![Filter Named Ranges options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20469'%3E%3C/svg%3E)

Delete Named Ranges using VBA
-----------------------------

While using the Name Manager is an efficient way to delete named ranges, if you need to do this quite often, you can use a simple VBA code to delete all the named ranges or named ranges that contain a specific text string.

Below is the VBA code that will delete all the Named Ranges from the entire workbook.

'Code by Sumit Bansal from https://trumpexcel.com
Sub DeleteNames()
Dim RName As Name
For Each RName In Application.ActiveWorkbook.Names
RName.Delete
Next
End Sub

The above code uses the [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through all the Named Ranges one by one and delete them. After running this VBA code, your workbook will not have any Named Ranges in it.

You can also tweak this code a little to delete only those Named Ranges that contain a specific word.

For example, let’s say I want to only delete those Names where it contains the word ‘sales’ (anywhere in the name).

You can do this by using the below VBA code:

'Code by Sumit Bansal from https://trumpexcel.com
Sub DeleteNames()
Dim RName As Name
For Each RName In Application.ActiveWorkbook.Names
If InStr(1, RName.Name, "sales", vbTextCompare) > 0 Then RName.Delete
Next
End Sub

The above code again [loops through each name](https://trumpexcel.com/vba-loops/)
 in the Workbook and then checks whether the name contains the word sales or not.

This is done using the [VBA INSTR function](https://trumpexcel.com/excel-vba-instr/)
 along with an [IF Then condition](https://trumpexcel.com/if-then-else-vba/)
. Only those names where it contains the word ‘sales’ would be deleted and all the rest would be ignored.

Now, the big question – how do you use this code?

Below are the steps to use this code in your Excel file:

1.  Click the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then click on Visual Basic (or use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     ALT + F11). This will open the Visual Basic Editor

![Click on Visual Basic in the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20184'%3E%3C/svg%3E)

2.  Click the Insert option in the menu and the click on Module. This will insert a new module for the current workbook

![Insert a new module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20356'%3E%3C/svg%3E)

3.  Copy and paste the above VBA code in the module code window
4.  To execute the macro code, click on the Run icon in the toolbar (or place the cursor anywhere in the code and use the keyboard shortcut F5)

![Run the Macro by clicking the green run button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20207'%3E%3C/svg%3E)

The above steps would run the VBA code and delete the named ranges from your workbook.

Note that the change made to the VBA code is not reversible. So as a good practice, make sure you create a backup copy of your workbook before running the VBA code.

So these are two ways (manual and VBA) you can use to **delete named ranges in Excel**.

While the Name Manager allows you to go through all the named ranges and in the workbook and then you can choose and delete some (or all), if you want to delete all named ranges in one go, you can use the VBA method.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [Useful Excel Macro Code Examples](https://trumpexcel.com/excel-macro-examples/)
    
*   [Creating a Drop Down List in Excel](https://trumpexcel.com/excel-drop-down-list/)
    
*   [How to Reference Another Sheet or Workbook in Excel](https://trumpexcel.com/reference-another-sheet-or-workbook-in-excel/)
    
*   [How to Rename a Sheet in Excel (4 Easy Ways + Shortcut)](https://trumpexcel.com/rename-sheet-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/delete-named-range-excel/#respond)

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
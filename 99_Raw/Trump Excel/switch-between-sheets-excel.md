# How to Switch Between Sheets in Excel? (7 Better Ways)

**Source:** https://trumpexcel.com/switch-between-sheets-excel

---

[Skip to content](https://trumpexcel.com/switch-between-sheets-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/switch-between-sheets-excel/#below-title)

Working with a large Excel workbook that has multiple sheets could be challenging. Even advanced Excel users feel overwhelmed when trying to switch between multiple worksheets in the same workbook.

Imagine working on an Excel workbook with 15 worksheets, and having to constantly switch between worksheets #3 and #12.

There are multiple ways to switch between worksheets in Excel, and in this tutorial, I’m going to show you some really cool and advanced tricks that will help **switch between tabs** a little easier and faster.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/switch-between-sheets-excel/#)

Keyboard Shortcut to Switch Between Sheets (Page UP/DOWN)
---------------------------------------------------------

If you need to move between sheets in the same workbook that are not far apart (i.e., there are not many worksheets in between the two sheets in which you want to switch), then you can use the below [keyboard shortcuts](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
.

**Keyboard Shortcut to Move to Sheets to the Right:**

**Control + PageDown**

**Keyboard Shortcut to Move to Sheets to the Left:**

**Control + Up**

To use this shortcut, you need to keep the Control key pressed and then use the PageUp or PageDown key.

If you are using a Mac, you can use the Command key instead of the Control key.

If you want to move to the next sheet on the right/left, hit the PageDown/PageUp key only once. If you keep it pressed, it will move through multiple sheets till you keep the key pressed (or till it reaches the last/first worksheet).

This method is best suited when you only have a few sheets. In case you have a lot of sheets (10 or more), even this method could feel a bit overwhelming. You can make it easier by moving the sheets (between which you want to switch) next to each other (but that may not always be possible)

Move from One Sheet to Another Using Watch Window
-------------------------------------------------

This method is probably the **best way to switch between multiple sheets in Excel**.

[Watch Window](https://trumpexcel.com/watch-window-excel/)
 is a less known feature in Excel that allows you to keep a track of values in specific cells in the workbook.

Although its primary purpose is not to help us move between sheets in the workbook, it’s a pretty good solution for this use case.

Suppose you have a workbook and you want to switch between Sheet1 and Sheet5.

Below are the steps to make this possible using the Watch Window:

1.  Select cell A1 in Sheet1 (one of the sheets between which you want to move back and forth)
2.  Click the Formulas tab in the ribbon

![Click the Formulas tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20591%20220'%3E%3C/svg%3E)

3.  Click on the Watch Window option (it’s in the Formula Auditing group)

![Click on the watch window icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20514%20220'%3E%3C/svg%3E)

4.  In the Watch Window dialog box, click on Add Watch

![Click on the add watch button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20234'%3E%3C/svg%3E)

5.  Make sure the right cell is selected in the Sheet. You can change the cell reference if you want

![Check the cell reference in the Add Watch dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20138'%3E%3C/svg%3E)

6.  Click on Add. This will add the watch instance to the Watch Window

![Add the first cell to watch](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20138'%3E%3C/svg%3E)

7.  Click on Add Watch button again

![Click on add watch option again](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20234'%3E%3C/svg%3E)

8.  In the Add Watch window, navigate to the next sheet to which you want to switch and select any cell there
9.  Click on Add. This will add a second watch instance to the Watch Window

![Add the cell in the second sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20138'%3E%3C/svg%3E)

Once done, you will have two instances in the Watch Window, and when you double-click on any of the instances, you will instantly be taken to that cell.

![Both sheet cells have been added to the watch window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20234'%3E%3C/svg%3E)

And since these two cells are in different sheets, it means that whenever you double click on the other instance, it will jump to that cell in the different worksheet.

There are quite a few merits to this method for switching between sheets:

*   You can create as many instances you want and a simple double click will take you there
*   If you close the workbook and open it later, the Watch Window will still be configured and you can continue to use it
*   Watch Window will remain active and will be placed above the worksheet so it’s always visible. So you can reduce its size and place it anywhere in the worksheet and always have access to it. You can also drag it and place it below the ribbon (where it gets docked and is always available), or slide it to the right and dock it as a pane.

![Watch Window Docked below the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20433'%3E%3C/svg%3E)

Watch Window is docked below the ribbon so it’s always visible

Go To Any Sheet with Activate Sheet Option
------------------------------------------

There is an ‘Activate’ Sheet option in Excel that shows all the sheets in the workbook as a list, and you can easily select and jump to that sheet.

So if you need to switch back and forth between two or more sheets, you can easily do that.

But where is this Activate Sheet option?

For that, you need to know a little trick.

1.  Go to the gray area to the left of the first sheet tab in your workbook

![Gray area between the two icons](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20193'%3E%3C/svg%3E)

2.  Place the cursor in between the two gray arrow icons

![Place the cursor in between the two icons](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20578%20156'%3E%3C/svg%3E)

3.  Click the right mouse key (or trackpad) – Note it’s the right key, not the left key. This will open the ‘Activate’ dialog box that has all the sheet names

![Activate Sheet dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20467'%3E%3C/svg%3E)

4.  Double click on the Sheet where you want to go

You can repeat the same process if you want to go to any other sheet. So if you want to switch between two or more sheets, you can do that using the Activate Sheet option.

_Note that when you click on any sheet, it will take you to the cell in that sheet that was last activated when you were in that sheet._

Switch Between Sheets Using the Name Box
----------------------------------------

The [Name Box in Excel](https://trumpexcel.com/name-box-excel/)
 allows you to quickly jump to any Named Range in the workbook.

We can use this to our advantage by [creating named ranges](https://trumpexcel.com/named-ranges-in-excel/)
 that refer to a cell or a range of cells in the sheets between which we need to switch.

Let me explain how it works.

Suppose I want to switch between Sheet1 and Sheet3.

First, I would create two named ranges that would refer to a cell in Sheet1 and Sheet3.

Below are the steps to do this:

1.  Select cell A1 in Sheet1
2.  Enter Sheet1A1 in the Name Box (you can use any name you want, but it should not have a space character in the name)

![Create named range for sheet1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20321'%3E%3C/svg%3E)

3.  Go to Sheet3 and select cell A1
4.  Enter Sheet3A1 in the Name Box

![Create named range for sheet3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20357%20387'%3E%3C/svg%3E)

The above steps would create two named ranges in the workbook. Sheet1A1 would refer to cell A1 in Sheet1 and Sheet3A1 would refer to cell A1 in Sheet3.

Now, to switch between these two sheets, click on the drop-down icon in the Name Box. You will see all the named ranges names show up in the drop-down.

![Named ranges appear in the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20313'%3E%3C/svg%3E)

So if you’re in Sheet3 and want to switch to Sheet1, select Sheet3A1 from the options in the drop-down.

While I have only shown you how to do this for two sheets, you can do this for as many sheets as you want.

Also, I have shown you how to switch and go to cell A1, but you can jump to any cell or range of cells using this method. Just select that cells or range of cells to which you want to jump to, and then create a named range for it.

**Pro Tip**: Keep the names of the Named Ranges simple and descriptive. Also, you can not have a space character in the name

Switch Between Sheets Using the Go To Dialog Box
------------------------------------------------

Another fast way to quickly move to a specific sheet and specific cell or range of cells is by using the Go-To dialog box.

In the Go-To dialog box, you can manually enter the sheet name and the [cell address](https://trumpexcel.com/return-cell-address-instead-of-value-excel/)
, and it will instantly take you there.

Suppose you have a workbook and you want to go to cell D20 in Sheet3.

Below are the steps to do this using the Go-To Special dialog box:

1.  Use the keyboard shortcut F5 to open the Go-To Special dialog box (you can also get this by going to Home –> Editing –> Find & Select –> Go-To)

![Click on Go To option in ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20456'%3E%3C/svg%3E)

2.  In the Reference field, enter Sheet3!D20

![Enter the cell reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20348'%3E%3C/svg%3E)

3.  Hit Enter (or click on the OK button)

The above steps would instantly take you to cell D20 in Sheet 3.

So if you want to switch between sheets and you don’t mind typing the name of the Sheet followed by the [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 in the Go-To special dialog box, this could one way to switch between two or more sheets.

Go-To Special dialog box has a temporary memory, so if you use it to go to a specific cell, you will see that option the next time you open the Go-To dialog box. So if you see the reference of the cell where you want to jump to, you can simply double-click on it instead of typing it.

Jump from One Sheet to Another Using Hyperlinks
-----------------------------------------------

Adding hyperlinks is another good way to allow a user to jump from one sheet to another with a click of a button.

You can have a hyperlink in a cell or add it to a shape or image. When added, as soon as the user clicks on the hyperlink, they will instantly be taken to the linked cell or range.

And if this cell or range is in another sheet, clicking on the hyperlink would also activate the sheet for which the hyperlink is added.

Let me explain using an example,

Suppose I have an Excel workbook where I want to add a hyperlink in cell A1 so that when the hyperlink is clicked, it will take me to cell A1 in Sheet2.

Below are the steps to do this:

1.  Activate Sheet1
2.  Right-click on cell A1 (the cell where I want to create the hyperlink)
3.  Click on ‘Links’. This will open the ‘Insert Hyperlink’ dialog box

![Click on the Link option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20567'%3E%3C/svg%3E)

4.  In the ‘Link to:’ options on the left, click on ‘Place in This Document’ option

![Click on place in this document](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20622%20423'%3E%3C/svg%3E)

5.  In the sheet names that show up, select Sheet2 (or whatever sheet to which you want to jump to)

![Select the Sheet2 option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20678%20423'%3E%3C/svg%3E)

6.  Enter the text you want to show in cell A1 in the ‘Text to Display’ field. In this example, I will add the text “Go to Sheet2”

![Enter the text to show in the cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20585%20396'%3E%3C/svg%3E)

7.  In the ‘Type the cell reference’ field, enter A1 (this is the cell in Sheet2 where the hyperlink would take us)

![Enter the cell reference A1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20390'%3E%3C/svg%3E)

8.  Click OK

The above steps would insert the specified text in the selected cell, and then create a hyperlink, which when clicked, would take us to cell A1 in Sheet2

**Pro Tip**: To open the insert hyperlink dialog box, select the cell (or the range of cells) and then use the keyboard shortcut Control + K (or Command + K if you’re using Mac)

Note that you can also use the same steps shown above to create a hyperlink to a shape in the workbook. Once done, when you click on that shape, it would take you to the specified location (which could be in the same sheet or any other worksheet)

Easy VBA Macro to Switch Between Sheets/Tabs
--------------------------------------------

And the final method that I want to cover is by using VBA macro code.

You can create a macro and put an icon in the Quick Access Toolbar so that whenever you click on that icon, it would switch the sheets.

Below is the macro code that will switch between Sheet1 and Sheet3 whenever it is run.

'This macro code has been developed by Sumit Bansal of https://trumpexcel.com
Sub SwitchSheets()
If ActiveSheet.Name = "Sheet1" Then
Sheets("Sheet3").Activate
Else
Sheets("Sheet1").Activate
End If
End Sub

The above code checks the active sheet name, and if the active sheet is Sheet1, it will activate Sheet3, and if the active sheet is Sheet3, it will activate Sheet1.

You can add this code in a module in the VB Editor, and then add it to the [Quick Access Toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
. This way, it will act as a toggle icon that will switch between sheets with a click.

In this code, I have used the names Sheet1 and Sheet3. You can change these with the sheet names in your workbook.

So these are some of the methods that you can use to quickly switch between worksheets in Excel. Instead of manually trying to switch between sheets (which can be time-consuming and error-prone), you can use one or more of these workarounds.

As I already mentioned, using the watch window method to switch between sheets is probably the best and most efficient way to do it.

**Other articles you may also like:**

*   [How to Rename a Sheet in Excel](https://trumpexcel.com/rename-sheet-in-excel/)
    
*   [Count Sheets in Excel (using VBA)](https://trumpexcel.com/count-sheets-excel/)
    
*   [How to Get the Sheet Name in Excel?](https://trumpexcel.com/get-sheet-name-excel/)
    
*   [How to Insert New Worksheet In Excel](https://trumpexcel.com/insert-new-worksheet-excel/)
    
*   [How to Delete Sheets in Excel (Shortcuts + VBA)](https://trumpexcel.com/delete-sheets-excel/)
    
*   [How to Group Worksheets in Excel](https://trumpexcel.com/group-worksheets-in-excel/)
    
*   [7 Easy Ways to Select Multiple Cells in Excel](https://trumpexcel.com/select-multiple-cells-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/switch-between-sheets-excel/#respond)

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
# How to Insert New Worksheet in Excel (Easy Shortcuts)

**Source:** https://trumpexcel.com/insert-new-worksheet-excel

---

[Skip to content](https://trumpexcel.com/insert-new-worksheet-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/insert-new-worksheet-excel/#below-title)

Working with MS Excel means working in the worksheets in Excel.

A worksheet is an area that has all the cells where you can store data, enter formulas, insert charts and [create reports and dashboards](https://trumpexcel.com/creating-excel-dashboard/)
.

When you [open a new Excel workbook file](https://trumpexcel.com/automatically-open-excel-file-startup/)
, by default there is only one worksheet. Earlier versions of Excel (2013 or 2016 used to have 3 worksheets by default)

There are some simple shortcuts and techniques that you can use to quickly **insert new worksheets in the same workbook in Excel**.

In this tutorial, I will show you a couple of methods that you can use to insert a new worksheet in the same workbook (one at a time).

I will also show you a method to quickly insert worksheets in bulk, in case you want to add 5, 10, or 20 worksheets in one go (using a simple VBA code).

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/insert-new-worksheet-excel/#)

Keyboard Shortcut to Insert a New Worksheet
-------------------------------------------

If you are a fan of [keyboard shortcuts](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
, this is probably the fastest way to insert a new worksheet in an already open workbook in excel.

Below is the keyboard shortcut to insert a new worksheet

SHIFT + F11

For this shortcut, hold the SHIFT key and then press the F11 key.

Another keyboard shortcut that does the same job is **ALT + SHIFT + F1** (hold the ALT and the SHIFT keys and press the F1 key)

Personally, I find using the keyboard shortcut to be the best way to insert a new worksheet in Excel. Even if I have to insert multiple worksheets (say 3 or 5 or 10), I can still do that very quickly

Insert New Sheet Using the Plus Icon
------------------------------------

If you’re not a big fan of keyboard shortcuts and prefer using the mouse instead, this method is for you.

At the bottom of your [worksheet (in the area that has all the sheet names)](https://trumpexcel.com/get-sheet-name-excel/)
, you will see the plus icon.

![Click the Plus icon to add a new sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20363%20192'%3E%3C/svg%3E)

Clicking on this plus icon will immediately insert a new worksheet.

Insert New Sheet Using the Insert Dialog Box
--------------------------------------------

Another way to insert a new sheet in Excel is by using the Insert dialog box.

Below are the steps to do this:

1.  Right-click on any of the sheets
2.  Click the Insert option

![Right click and then click on Insert Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20397'%3E%3C/svg%3E)

3.  In the Insert dialog box, make sure Worksheet is already selected (which is also the default option).

![Make Sure Worksheet is Selected in the Insert dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20368'%3E%3C/svg%3E)

4.  Click on Ok

While this is not the fastest way to add a new sheet in an Excel workbook, it’s good to know as it gives you access to some other things as well.

Apart from inserting a regular worksheet, you can also use this to insert a ‘Chart Sheet’ or a ‘Macro Sheet’ using the insert dialog box.

If you’re wondering, a Chart Sheet is just like a worksheet but is meant only to hold a chart. A macro sheet is something that was used earlier before the VBA days and is no longer used.

In most cases, you won’t be needing these, but it’s good to know.

There is also the Spreadsheet Solutions tab that holds some of the [templates](https://trumpexcel.com/free-excel-templates/)
. You can also create and get your own templates here. So the next time you need to quickly insert a template, you can do it from here.

Adding New Worksheets Using the Insert Tab in the Ribbon
--------------------------------------------------------

And finally, you also have an option in the Excel ribbon to add a new worksheet.

To do this:

1.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20423%20227'%3E%3C/svg%3E)

2.  In the Cells group, click on the Insert option

![Click on Insert](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20225'%3E%3C/svg%3E)

3.  Click on the Insert Sheet option.

![Click on Insert Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%20261'%3E%3C/svg%3E)

This will insert one new worksheet in the open workbook

How to Insert Multiple Worksheets in One Go (One Line VBA Code)
---------------------------------------------------------------

So far, the methods that I have shown you insert one new worksheet at a time.

In case you want to insert multiple worksheets, you would have to use these methods again and again (i.e., use the keyboard shortcuts multiple times or use the plus icon multiple times).

While this works fine in most cases, if you have to insert worksheets in bulk, saying so 10 or 20 or 30 worksheets in one go, then this could be time-consuming and error-prone.

So let me show you a better way to insert multiple new worksheets in one go.

This can be done easily using a simple one-line VBA code:

Sheets.Add Count:=10

The above code would instantly add 10 new sheets in the workbook in which it’s run (if you want any other number of sheets to be added, just change the value in the code)

Below are the steps to [run this macro code](https://trumpexcel.com/run-a-macro-excel/)
:

1.  Click the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     (or use the keyboard shortcut ALT + F11) and then click on Visual Basic

![Click the Visual Basic icon in the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20201'%3E%3C/svg%3E)

2.  If you don’t see the immediate window in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
    , click on the View option and then click on [Immediate window](https://trumpexcel.com/vba-immediate-window/)
    

![Click the View tab and then click on Immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20481'%3E%3C/svg%3E)

3.  Copy and paste the above code in the immediate window

![Copy the line of code in the Immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20185'%3E%3C/svg%3E)

4.  Place the cursor at the end of the VBA code line and hit Enter

As soon as you hit Enter, it would instantly insert 10 new sheets in the workbook. In case you want to insert more (say 20 or 30), just change the number in the code

The good thing about using this code is that you can be sure that it would insert the right number of sheets (no chance of human error if the code is executed without any errors).

In case you need to do this quite often, you can use the below code and paste it into our [Personal Macro workbook](https://trumpexcel.com/personal-macro-workbook/)
.

Sub AddSheets()  
Sheets.Add Count:=10  
End Sub

Once in Personal Macro Workbook, you can add it to the [Quick Access Toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
 so you always have access to it in the workbook.

This way, you can easily add 10 or 20 sheets with just a single click.

Changing the Default Number of Sheets with New Excel Workbooks
--------------------------------------------------------------

If you always have a need for more worksheets in the workbook, you can change the default number of sheets you get when you open a new Excel file.

For example, you can change the setting so that you always get 5 or 10 sheets by default with every newly opened workbook.

Below are the steps to change this default setting:

1.  Open any Excel workbook
2.  Click the File tab

![Click the File tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20222'%3E%3C/svg%3E)

3.  Click on Options. This will open the [Excel Options](https://trumpexcel.com/excel-options-hacks/)
     dialog box
4.  In the Excel Options dialog box, make sure the General option is selected in the left-pane

![Click on General](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20711%20375'%3E%3C/svg%3E)

5.  In the ‘When creating new workooks’ section, enter the number of sheets you want (in the Include this many sheets value).

![Include this many sheets option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20717%20623'%3E%3C/svg%3E)

6.  Click OK

Now when you open a new Excel workbook, it will have the specified number of worksheets.

Note that an Excel file can have a maximum of 255 sheets.

These are all the ways you can use to insert a new sheet in Excel. In most cases, you only need to add one or a couple of new sheets, so you can use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 or the plus icon in the worksheet.

And in case you have a need to insert many new sheets in bulk, you can use the VBA code. Alternatively, you can also change the default number of sheets in any new Excel workbook.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [How to Delete Sheets in Excel (Shortcuts + VBA)](https://trumpexcel.com/delete-sheets-excel/)
    
*   [How to Rename a Sheet in Excel (4 Easy Ways + Shortcut)](https://trumpexcel.com/rename-sheet-in-excel/)
    
*   [How to Print Excel Sheet on One Page (Fit to One Page)](https://trumpexcel.com/print-excel-sheet-one-page/)
    
*   [How to Group Worksheets in Excel (Step-by-Step)](https://trumpexcel.com/group-worksheets-in-excel/)
    
*   [How to Compare Two Excel Sheets (for differences)](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [How to Move Chart to New Sheet in Excel?](https://trumpexcel.com/move-chart-to-new-sheet-excel/)
    
*   [Count Sheets in Excel (using VBA)](https://trumpexcel.com/count-sheets-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/insert-new-worksheet-excel/#respond)

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
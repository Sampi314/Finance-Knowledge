# How to Quickly Unhide Columns in Excel

**Source:** https://trumpexcel.com/unhide-columns

---

[Skip to content](https://trumpexcel.com/unhide-columns/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/unhide-columns/#below-title)

**Watch Video – How to Unhide Columns in Excel**

If you prefer written instruction instead, below is the tutorial.

Hidden rows and columns can be quite irritating at times.

Especially if someone else has hidden these and you forget to unhide it (or even worse, you don’t know how to unhide these).

While I can’t do anything about the first issue, I can show you how to unhide columns in Excel (the same techniques can also be used to unhide rows).

It may happen that one of the methods of unhiding columns/rows may not work for you. In that case, it is good to know the alternatives that can work.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/unhide-columns/#)

How to Unhide Columns in Excel
------------------------------

There are many different situations where you may need to unhide the columns:

1.  Multiple columns are hidden and you want to unhide all columns at once
2.  You want to unhide a specific column (in between two columns)
3.  You want to unhide the first column

Let’s go through each for these scenarios and see how to unhide the columns.

### Unhide All Columns At One Go

If you have a worksheet that has multiple hidden columns, you don’t need to go hunt each one and bring it to light.

You can do that all in one go.

And there are multiple ways to do this.

#### Using the Format Option

Here are the steps to unhide all columns at one go:

1.  Click on the small triangle at the top left of the worksheet area. This will select all the cells in the worksheet.
2.  Right-click anywhere in the worksheet area.
3.  Click on Unhide.

No matter where that pesky column is hidden, this will unhide it.

Note: You can also use the keyboard shortcut Control A A (hold the control key and hit the A key twice) to select all the cells in the worksheet.

#### Using VBA

If you need to do this often, you can also use VBA to get this done.

The below code will unhide column in the worksheet.

Sub UnhideColumns ()
Cells.EntireColumn.Hidden = False
EndSub

You need to place this code in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
 (in a module).

If you want to learn how to do this with VBA, read a detailed guide on how to [run a macro](https://trumpexcel.com/run-a-macro-excel/)
 in Excel.

Note: To save time, you can save this macro in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
 and add it to the quick access toolbar. This will allow you to unhide all columns with a single click.

#### Using a Keyboard Shortcut

If you’re more comfortable using keyboard shortcuts, there is a way to unhide all columns with a few keystrokes.

Here are the steps:

1.  Select any cell in the worksheet.
2.  Press **Control-A-A** (hold the control key and press A twice). This will select all the cells in the worksheet
3.  Use the following shortcut – **ALT H O U L** (one key at a time)

If you can get hang of this keyboard shortcut, it could be a lot faster to unhide columns.

Note: The reason you need to press A twice when holding the control key is that sometimes when you press Control A, it only selects the used range in Excel (or the area that has the data) and you need to press the A again to select the entire worksheet.

Another keyword shortcut that works for some and not for others is **Control 0** (from a numeric keypad) or **Control Shift 0** from a non-numeric keypad. It used to work for me earlier but doesn’t work anymore. [Here](https://superuser.com/questions/183197/whats-the-keyboard-shortcut-to-unhide-a-column-in-excel-2010)
 is some discussion on why it may happen. I suggest you use the longer (ALT HOUL) shortcut that works every time.

### Unhide Columns in Between Selected Columns

There are multiple ways you can quickly unhide columns in between selected columns. The methods shown here are useful when you want to unhide a specific column(s).

Let’s go through these one-by-one (and you can choose to use that you find the best).

#### Using a Keyboard Shortcut

Below are the steps:

1.  Select the columns that contain the hidden columns in between. For example, if you are trying to unhide column C, then select column B and D.![How to Unhide Columns in Excel - Select Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20280%20408'%3E%3C/svg%3E)
2.  Use the following shortcut – **ALT H O U L** (one key at a time)

This will instantly unhide the columns.![How to Unhide Columns in Excel - Shortcuts Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20408'%3E%3C/svg%3E)

#### Using the Mouse

One quick and easy way to unhide a column is to use the mouse.

Below are the steps:

*   Hover your mouse in between the columns alphabets that have the hidden column(s). For example, if Column C is hidden, then hover the mouse between Column B and D (at the top of the worksheet). You will see a double line icon with arrows pointing on left and right.![How to Unhide Columns in Excel - Double Arrow Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20180'%3E%3C/svg%3E)
*   Hold the left key of the mouse and drag it to the right. It will make the hidden column appear.![How to Unhide Columns in Excel - drag using mouse](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20180'%3E%3C/svg%3E)

#### Using the Format Option in the Ribbon

Under the home tab in the ribbon, there are options to hide and unhide columns in Excel.

Here is how to use it:

*   Select the columns between which there are hidden columns.
*   Click the Home tab.
*   In the Cells group, click on Format.![Click on Formart Option in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20399%20192'%3E%3C/svg%3E)
*   Hover the cursor on Hide & Unhide option.
*   Click on ‘Unhide Columns’![Unhide Columns option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20397%20571'%3E%3C/svg%3E)

Another way of accessing this option is by selecting the columns and right clicking using the mouse. In the menu that appears, select the unhide option.

![How to Unhide Columns in Excel - left Click Menu](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20360'%3E%3C/svg%3E)

#### Using VBA

Below is the code that you can use to unhide columns in between the selected columns.

Sub UnhideAllColumns()  
Selection.EntireColumn.Hidden = False  
End Sub

You need to place this code in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
 (in a module).

If you want to learn how to do this with VBA, read a detailed guide on how to [run a macro](https://trumpexcel.com/run-a-macro-excel/)
 in Excel.

Note: To save time, you can save this macro in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
 and add it to the quick access toolbar. This will allow you to unhide all columns with a single click.

#### By Changing the Column Width

There is a possibility that none of these methods work when you try to unhide column in Excel. It happens when you change the Column Width to 0. In that case, even if you unhide the column, it’s width still remains 0, and hence you can’t see it or select it.

Below are the steps to change the column width:

*   In the name box, type any [cell address](https://trumpexcel.com/return-cell-address-instead-of-value-excel/)
     in that column. For example, if it is column C, type C1.
*   Although the column is not visible, the cursor would go in between B1 and D1 (indicating that C1 has been selected).![How to Unhide Columns in Excel - Name Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20444%20196'%3E%3C/svg%3E)
*   Click the Home tab.
*   In the Cells group, click the Format option.
*   Click on the ‘Column Width option. It will open the Column Width dialogue box.![How to Unhide Columns in Excel - Column Width](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20234%20403'%3E%3C/svg%3E)
*   Enter a column width value to make the column visible. ![How to Unhide Columns in Excel - Column Width value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20196%20109'%3E%3C/svg%3E)

This is by far the most reliable way to unhide columns in Excel. If everything fails, just change the column width.

### Unhide the First Column

Unhiding the first column can be a little bit tricky.

You can use many of the methods covered above, with a little bit of extra work.

Let me show you a few ways.

### Use the Mouse to Drag the First Column

Even when the first column is hidden, Excel allows you to select it and drag it to make it visible.

To do this, hover the cursor on the left edge of column B (or whatever is the leftmost visible column).

The cursor would change into a double arrow pointer as shown below.

![hover the cursor on hidden column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20253%20158'%3E%3C/svg%3E)

Hold the left mouse button and drag the cursor to the right. You will see that it unhides the hidden column.

![Unhide Column by dragging the mouse cursor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20260'%3E%3C/svg%3E)

### Go to a Cell in the First Column and Unhide it

But how do you go to any cell in the column that’s hidden?

Good question!

You use the Name Box (it’s left to the [formula bar)](https://trumpexcel.com/show-hide-formula-bar-excel/)
.

![Name Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20398%20266'%3E%3C/svg%3E)

Enter A1 in the Name Box. It will instantly take you to the A1 cell. Since the first column is hidden, you won’t be able to see it, but be assured that it’s selected (you’ll still see a thin line just left of B1).

Once the hidden column cell is selected, follow the below steps:

*   Click the Home tab.
*   In the Cells group, click on Format.
*   Hover the cursor on the ‘Hide & Unhide’ option.
*   Click on ‘Unhide Columns’

### Select the First Column and Unhide it

Again! How do you select it when it’s hidden?

Well, there are many different ways to skin the cat.

And this is just another method in my kitty (this is the last cat sounding reference I promise).

When you select the leftmost visible cell and drag the cursor to the left (where there are row numbers), you end up selecting all the hidden columns (even when you don’t see it).

![Unhide columns by selecting using mouse drag](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20260'%3E%3C/svg%3E)

Once you have select all the hidden columns, follow the below steps:

*   Click the Home tab.
*   In the Cells group, click on Format.
*   Hover the cursor on the ‘Hide & Unhide’ option.
*   Click on ‘Unhide Columns’

Check The Number of Hidden Columns
----------------------------------

Excel has an ‘Inspect Document’ feature that is meant to quickly scan the workbook and give you some details about it.

And one of the things that you can do that ‘Inspect Document’ is to quickly check how many hidden columns or hidden rows are there in the workbook.

This might be useful when you get the workbook from someone and want to quickly inspect it.

Below are the steps on how to check the total number of hidden columns or hidden rows:

1.  Open the workbook
2.  Click on the File tab
3.  In the Info options, click on the ‘Check for Issues’ button (it’s next to the Inspect Workbook text).![Click on the Check for issues button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20567%20505'%3E%3C/svg%3E)
4.  Click on Inspect Document.![Click on Inspect Document option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20350'%3E%3C/svg%3E)
5.  In the Document Inspector, make sure Hidden Rows and Columns option is checked.![Make Sure Hidden rows and columns is checked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20459'%3E%3C/svg%3E)
6.  Click the Inspect button.![Click on Inspect Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20459'%3E%3C/svg%3E)

This will show you the total number of hidden rows and columns.

![Number of Hidden columns found reported](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20672%20243'%3E%3C/svg%3E)

It also gives you the option to [delete all these hidden rows/columns](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/)
. This can be the case if there is extra data that has been hidden and is not needed. Instead of finding hidden rows and columns, you can quickly delete these from this option.

**You May Also Like the following Excel Tips/Tutorials:**

*   [How to Insert Multiple Rows in Excel – 4 Methods](https://trumpexcel.com/how-to-insert-multiple-rows-in-excel/)
    .
*   [How to Quickly Insert New Cells in Excel](https://trumpexcel.com/how-to-quickly-insert-new-cells-in-excel/)
    .
*   [Keyboard & Mouse Tricks that will Reinvent the Way You Excel](https://trumpexcel.com/keyboard-mouse-tricks/)
    .
*   [How to Hide a Worksheet in Excel.](https://trumpexcel.com/hide-worksheet/)
    
*   [How to Unhide Sheets in Excel (All In One Go)](https://trumpexcel.com/unhide-sheets-excel/)
    
*   [Excel Text to Columns](https://trumpexcel.com/excel-text-to-columns-examples/)
     (7 Amazing things you can do with it)
*   [How to Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
    
*   [How to Lock Formulas in Excel](https://trumpexcel.com/lock-formulas-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Quickly Unhide COLUMNS in Excel (A Simple Guide)”
-----------------------------------------------------------------------

1.  Thanks, Very easy to understand video. well done!
    
    [Reply](https://trumpexcel.com/unhide-columns/#comment-12557)
    
2.  Thank you! I’ve now got my column A back again, haha.
    
    [Reply](https://trumpexcel.com/unhide-columns/#comment-12243)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/unhide-columns/#respond)

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
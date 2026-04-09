# How to Rename a Sheet in Excel (4 Easy Ways + Shortcut)

**Source:** https://trumpexcel.com/rename-sheet-in-excel

---

[Skip to content](https://trumpexcel.com/rename-sheet-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/rename-sheet-in-excel/#below-title)

Using multiple worksheets in an Excel workbook is an easy way to keep your data organized. For example, you can have different sheets for different regions, or for different months/year, or different projects, etc.

And when working with multiple sheets, you may sometimes need to change their names.

In this Excel tutorial, I will show you some simple ways to **rename a sheet in Excel** (including a keyboard shortcut).

And in case you want to rename all the sheets as one go (such as adding a prefix or suffix to all the sheets), check out the section on using VBA to do this (it’s not complicated).

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/rename-sheet-in-excel/#)

Rename Sheets with a Simple Double Click
----------------------------------------

Using a mouse is the easiest way to change the name of a sheet in Excel.

Below are the steps to rename a sheet using the mouse double-click:

1.  Place your cursor over the sheet tab that you want to rename
2.  Double-click on it. This will put the sheet name in the edit mode
3.  Enter the name of the sheet that you want
4.  Hit the Enter key (or click anywhere in the worksheet)

![Double click on the tab to rename the sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20304%20160'%3E%3C/svg%3E)

If you want to rename multiple sheets, you need to do these above steps for all the sheets.

Also, if you want to add a prefix/suffix to the sheet name, you the arrow keys to move the cursor when you’re in the edit mode in the tab. Once you have the cursor where you want to add the text, enter in manually.

Related: [Increase Excel Tab Numbering as You Create a Copy](https://trumpexcel.com/excel-tab-numbering/)

Rename Sheets with a Keyboard Shortcut
--------------------------------------

If you prefer using the keyboard and don’t want to switch to a mouse just to rename a sheet, you can also use the following keyboard shortcut (for Windows).

ALT + O + H + R

You need to press these keys one after the other in a succession.

While this is not one of the easy keyboard shortcuts, once you get used to it, you may find it a better way to rename sheets in Excel.

**Pro Tip**: In case you want to move to the next sheet, you can use the keyboard shortcut Control + PageUp/PageDown (hold the Control key and then press the PageUP key to move to the next sheet or PageDown key to move to the previous sheet.

Rename Sheets Using the Format Option in the Ribbon
---------------------------------------------------

You can also access the option to rename sheets through the Excel ribbon:

1.  Click the Home tab
2.  In the Cell group, click on the ‘Format’ option
3.  Click on the Rename Sheet option. This will get the sheet name into edit mode![Rename sheet option in the ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20345%20567'%3E%3C/svg%3E)
4.  Enter the name that you want for the sheet

This method would only allow you to change the name of the current sheet. To change the name of some other sheet, you first need to activate it and then use the above steps.

While this method exists, I always prefer using the mouse double-click technique to change the name of the sheet.

Rename Sheets Using VBA – Add Prefix/Suffix to All Sheet Names in One Go
------------------------------------------------------------------------

Sometimes, you may have a need to add a prefix or a suffix to all the sheets in your workbook.

While you can do this manually (using the methods shown above) if you only have a few worksheets. But in case you have a lot many, this could be tedious and error-prone.

In such a case, you can use a simple VBA code in the immediate window to get this done in a snap.

Below is the VBA code that will add the prefix “**2020 –** ‘ in front of all the sheet names:

For Each sh In Worksheets: sh.Name = "2020 - " & sh.Name: Next sh

The above code uses a [VBA loop](https://trumpexcel.com/vba-loops/)
 (the [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
) to go through each sheet in the workbook and change the name by adding the specified prefix.

Below are the steps to use this VBA macro code in Excel:

1.  Right-click on any of the sheet tabs
2.  Click on View Code. This will open the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
     backend![Click on View code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20307%20395'%3E%3C/svg%3E)
3.  In the VB Editor window, click on the ‘View’ option in the menu and then click on [Immediate Window](https://trumpexcel.com/vba-immediate-window/)
    . This will make the immediate window show up. You don’t need to do this in case the immediate window is already visible. ![Get the immediate window visible](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20484'%3E%3C/svg%3E)
4.  Copy and paste the above line of code in the immediate window![Copy and paste the VBA code in the immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20425'%3E%3C/svg%3E)
5.  Place the cursor at the end of the line![Place the cursor at the end of the code in the immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20427'%3E%3C/svg%3E)
6.  Hit the Enter key

As soon as you hit the Enter key, the code is executed and it adds the specified prefix in all the sheet names.

Note that this will rename all the sheets – visible as well as [hidden](https://trumpexcel.com/hide-worksheet/)
.

Similarly, if you want to add a suffix to all the sheet names, you can use the below code:

For Each sh In Worksheets: sh.Name = sh.Name & " - 2020": Next sh

You can even go a step further and also change the name of some specific sheets (let’s say only the ones where the text 2020 appears). This can easily be done by editing the code.

Sheet Naming Rules in Excel
---------------------------

When renaming a sheet in Excel, there are some naming rules you need to follow:

1.  A sheet name can be a maximum of 31 characters in length.
2.  You can not leave a sheet name blank.
3.  You can not have two sheets of the same name.
4.  You can not begin or end the sheet name with an apostrophe (‘). However, you can use it in the middle somewhere in the sheet name
5.  You can not use the following characters while renaming the sheet in Excel: **\[ \] \\ / ? : \*** 
    *   This means that you can’t have a sheet name with a date that uses a forward slash. For example, 01/01/2020 isn’t a valid sheet name but 01-01-2020 is valid.
6.  You can not name the sheet **History** (as it’s used internally by Excel)

I hope you found this Excel tutorial useful.

**You may also like the following Excel tips and tutorials:**

*   [How to Unhide Sheets in Excel (All In One Go)](https://trumpexcel.com/unhide-sheets-excel/)
    
*   [How to Get the Sheet Name in Excel?](https://trumpexcel.com/get-sheet-name-excel/)
    
*   [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [Combine Data From Multiple Worksheets into a Single Worksheet in Excel](https://trumpexcel.com/combine-multiple-worksheets/)
    
*   [How to Compare Two Excel Sheets](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [Count Sheets in Excel (using VBA)](https://trumpexcel.com/count-sheets-excel/)
    
*   [How to Change the Color of the Sheet Tab in Excel](https://trumpexcel.com/change-color-of-sheet-tab-excel/)
     

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Rename a Sheet in Excel (4 Easy Ways + Shortcut)”
----------------------------------------------------------------------

1.  the Keyboard Shortcut should be Alt + H + O + R..
    
    [Reply](https://trumpexcel.com/rename-sheet-in-excel/#comment-14008)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/rename-sheet-in-excel/#respond)

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
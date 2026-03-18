# How to Remove Conditional Formatting in Excel (Shortcut + VBA)

**Source:** https://trumpexcel.com/remove-conditional-formatting-excel

---

[Skip to content](https://trumpexcel.com/remove-conditional-formatting-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-conditional-formatting-excel/#below-title)

I love using Conditional Formatting in Excel. It allows me to quickly highlight and format cells based on specified conditions.

While Conditional Formatting is great, it’s also [volatile](https://trumpexcel.com/excel-volatile-formulas/)
 – which means that if you have a lot of conditional formatting rules applied to large data sets, it can [slow down your Excel file](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
.

So, I also have to make sure that I remove conditional formatting from datasets where I don’t need it anymore.

In this short tutorial, I will show you a couple of easy ways you can use to **remove conditional formatting from a selected range of cells, the entire worksheet, or the workbook**.

I will also show you how you can remove specific conditional formatting rules while keeping the rest.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-conditional-formatting-excel/#)

Keyboard Shortcut to Remove Conditional Formatting
--------------------------------------------------

Below is the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 to remove Conditional formatting rules from the selected range of cells:

ALT + H + L + C + S

To use the above keyboard shortcut, you first need to select the cells from which you want to remove that Conditional formatting and then press these keys in succession (one after the other)

And below is the keyboard shortcut to clear conditional formatting rules from the entire worksheet

ALT + H + L + C + E

To use the above keyboard shortcut, first activate the sheet from which you want to remove the conditional formatting rules, and then use it.

Also read: [Remove Formulas (but Keep Data) in Excel](https://trumpexcel.com/remove-formulas-keep-data-excel/)

Clear Conditional Formatting Using the Quick Analysis Tool option
-----------------------------------------------------------------

Another quick way to quickly clear conditional formatting from the selected cells is by using the [Quick Analysis tool](https://trumpexcel.com/excel-quick-analysis-tool/)
 option.

When you select a range of cells, it would show you the quick analysis tool icon at the bottom right of this election, where you would have one-click access to the clear formatting option.

Below I have a data set where I have conditional formatting applied to the scores of students.

![Dataset with conditional formatting applied to it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20382'%3E%3C/svg%3E)

And here are the steps to quickly remove conditional formatting from these cells that contain the scores:

1.  Select the cells from which you want to remove the formatting
2.  Click on the Quick Analysis tool icon that appears at the bottom right of the selection

![Click on the Quick Analysis Tool icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20443'%3E%3C/svg%3E)

3.  Click on the ‘Clear Format’ option

![Click on the Clear Format option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20612'%3E%3C/svg%3E)

Note that this is only going to remove the conditional formatting from the cells, it is not going to remove any other formatting such as fill color or borders or [font style](https://trumpexcel.com/best-excel-fonts/)
, etc.

Also read: [Conditional Formatting Not Working in Excel](https://trumpexcel.com/conditional-formatting-not-working/)

Remove Conditional Formatting Using the ‘Clear Rules’ Option
------------------------------------------------------------

If you think that the keyboard shortcut is long and quite hard to remember (which I agree it is), you can also use the inbuilt ‘Clear Rules’ option in the ribbon to clear conditional formatting rules from a selected range of cells or from the entire worksheet.

Below are the steps for removing conditional formatting from a selected range of cells:

1.  Select the range of cells from which you want to remove the formatting
2.  Click the ‘Home’ tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20223'%3E%3C/svg%3E)

3.  Click on the Conditional Formatting option

![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20223'%3E%3C/svg%3E)

4.  In the options that show up, click on the ‘Clear Rules’ option
5.  Click on the ‘Clear Rules from Selected Cells’ option

![Click on Clear Rules from selected cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20619'%3E%3C/svg%3E)

The above steps would remove conditional formatting from the selected range of cells only, and if you have applied it anywhere else in the worksheet, it would remain unaffected.

In case you want to get rid of all the conditional formatting in the worksheet, you can choose the “Clear Rules from Entire Sheet” option.

In the clear rules option, you would also see two additional options – “Clear Rules from This Table” and “Clear Rules from This Pivot Table”. Unless you’re working with a Pivot table or an Excel Table, these would be grayed out, and would only become available when you select a cell inside an Excel Table or [Pivot Table](https://trumpexcel.com/pivot-table/)
.

Remove Conditional Formatting Using ‘Paste Format Only’ Hack
------------------------------------------------------------

When you copy and paste a cell over another cell, it would not only copy and paste the value of the cell, but also the formatting.

Excel also allows you to only copy and paste the formatting from the copied cell, which is something we can use to remove conditional formatting from any cell or range of cells.

Below I have a data set where I have conditional formatting applied to the scores of students.

![Dataset with conditional formatting applied to it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20382'%3E%3C/svg%3E)

Here are the steps to remove the conditional formatting from these cells using the [Paste Special](https://trumpexcel.com/excel-paste-special-shortcuts/)
 technique:

1.  Select any cell that does not have conditional formatting applied to it (this is the cell whose formatting would be copied). In this example, I have selected cell F2

![Select a cell to copy](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20620%20391'%3E%3C/svg%3E)

2.  Copy this cell (you can use the keyboard shortcut Control + C or right-click and then click on Copy)
3.  Select the cells from which you want to remove the conditional formatting

![Select the cells from which you want to remove conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20613%20390'%3E%3C/svg%3E)

4.  Right-click on the selection
5.  Click on the Paste Special option. this will open the Paste Special dialog box

![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20490%20395'%3E%3C/svg%3E)

6.  In the dialog box, select the ‘Formats’ option

![Select Formats in the Paste Special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20413'%3E%3C/svg%3E)

7.  Click Ok

The above steps would override the formatting of the selected cells and copy the formatting from the cell we selected in Step 1.

![Final result when conditional formatting is removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20395'%3E%3C/svg%3E)

One drawback of this method is that it would remove all the formatting from the selected cells (not just the conditional formatting).

So if you copy formatting from a cell that has no formatting applied to it and paste the formatting on the selected range of cells, along with the conditional formatting, you would also lose any other formatting such as fill color, border, font style, etc.

Clear All Formatting (Including Conditional Formatting)
-------------------------------------------------------

Another way you can remove conditional formatting from a selected range of cells is by clearing all the formats.

Doing this would remove all the formatting such as cell color, bold/italics, borders, font size, etc. (as well as conditional formatting).

Below are the steps to clear all the formatting from the selected range of cells in Excel:

1.  Select the cells from which you want to remove the conditional formatting
2.  Click the ‘Home’ tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20223'%3E%3C/svg%3E)

3.  In the Editing group, click on the ‘Clear’ option
4.  In the options that show up in the drop-down, click on ‘Clear Formats’

![Click on Clear Formats](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20431'%3E%3C/svg%3E)

The above steps would leave the content of the cell as is, but remove all the formatting from it.

You can also use the below keyboard shortcut to clear all the formatting:

ALT + H + E + F

Remove Conditional Formatting from All Worksheets in One Go (using VBA)
-----------------------------------------------------------------------

If you have a lot of worksheets in the workbook and you want to remove Conditional formatting rules from all these worksheets, doing it one worksheet at a time would be time-consuming.

A quick way to clear conditional formatting rules from all the worksheets in a workbook is by using a simple VBA macro code.

Below are the steps to use a simple one-line VBA macro code to quickly cycle through all the worksheets in your workbook and remove conditional formatting from each sheet:

1.  Click the Developer tab in the ribbon (if you don’t see the developer tab, [here is a detailed guide on how to get it](https://trumpexcel.com/excel-developer-tab/)
    )
2.  Click on the Visual Basic icon

![Click on Visual Basic icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20189'%3E%3C/svg%3E)

3.  In the [VB editor](https://trumpexcel.com/visual-basic-editor/)
     that opens up, click the ‘View’ tab and then click on ‘Immediate Window’. This will make the Immediate window box appear in the VB editor. _You don’t need to do this step if you already see the Immediate Window in the VB editor_

![Click on Immediate Window view option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20504'%3E%3C/svg%3E)

4.  Copy and paste the below line of code in the immediate window

For Each ws In Worksheets: ws.Cells.FormatConditions.Delete: Next ws

![Copy paste the one line vba code in the immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20444'%3E%3C/svg%3E)

5.  Place the cursor at the end of the code line

![Place the cursor at the end of the code line](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20216'%3E%3C/svg%3E)

5.  Hit the Enter key
6.  Close the VB editor

When you place the cursor at the end of the code line and hit the enter key, that line of code is executed.

The above code uses a simple [For Each Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
, where it loops through each worksheet in the workbook and uses _Cells.FormatConditions.Delete_ method to delete conditional formatting from each sheet.

Note that this would only remove conditional formatting and all the other formatting such as [cell color](https://trumpexcel.com/shortcuts-fill-color-excel/)
, font color/size, borders, etc would not be impacted.

One big benefit of using the [Immediate window](https://trumpexcel.com/vba-immediate-window/)
 to run simple codes like these is that you don’t have to worry about anything else (such as saving the file as a macro-enabled workbook). You can run the code using the steps shown above and close the VB editor.

**Pro Tip:** Remember that the changes made using a VBA code are irreversible, so always make a backup copy before running the VBA code

In case you’re looking for the whole code that you can use in the module in the VB Editor, you can use the code below:

'Code developed by Sumit Bansal from https://trumpexcel.com
Sub RemoveConditionalFomatting\_AllSheets()
Dim ws As Worksheet
For Each ws In Worksheets
    ws.Cells.FormatConditions.Delete
Next ws
End Sub

If you use the above code (by copy-pasting it in a module in your workbook), make sure to save your workbook as a macro-enabled file (or else the code would be last the next time you open the file)

Remove Specific Conditional Formatting Rules
--------------------------------------------

So far, I have shown you how to remove all the conditional formatting rules from the selected cells or the entire worksheet.

But in some cases, you may not want to get rid of conditional formatting completely. Rather, you may want to edit or delete a few conditions formatting rules while keeping the others.

Below I have a data set where I have student names in column A and their scores in columns B, C, and  D.

![Dataset with conditional formatting applied to it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20382'%3E%3C/svg%3E)

In the cells that contain their score, I have two conditional formatting rules

*   Highlighting cells where the score is less than 30 in red font in red fill color and
*   Highlighting cells where the score is more than 80 in green color

Now let me show you how to only clear one of the conditional formatting rules while keeping the other rule in place:

1.  Select the cells that have the conditional formatting rules that you want to edit
2.  Click the Home tab
3.  Click on the ‘Conditional Formatting’ icon

![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20223'%3E%3C/svg%3E)

4.  Click on the ‘Manage Rules’ option. This will open the ‘Conditional Formatting Rules Manager’ dialog box

![Click on Manage Rules](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20361%20565'%3E%3C/svg%3E)

5.  In the dialog box, you would see all the conditional formatting rules that are applied to the selected cells. Select the one that you want to delete
6.  Click the ‘Delete Rule’ button

![Click the Delete Rule button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20248'%3E%3C/svg%3E)

The above steps would delete the selected rule only.

If you want to delete multiple conditional formatting rules, you can repeat the process by selecting the rule that you want to delete and then clicking the Delete Rule button.

Note that it does not allow you to select multiple rules, so you would have to do it one by one only.

In the dialog box, you also get options that allow you to edit any existing rule, duplicate a rule, or add a new rule from scratch.

In this tutorial, I showed you how to remove conditional formatting rules using keyboard shortcuts or using the inbuilt ‘Clear Rules’ option in the ribbon.

I also covered how to remove conditional formatting rules from all the worksheets in a workbook in one go using the group worksheets method or using a simple one-line VBA code.

And finally, I covered how to remove some of the conditional formatting rules while keeping the rest.

I hope this tutorial was easy to follow and would be helpful in your [day-to-day work](https://trumpexcel.com/24-excel-tricks/)
.

**Other Excel tutorials you may also like:**

*   [How to Remove Table Formatting in Excel (Easy Guide)](https://trumpexcel.com/remove-table-formatting-excel/)
    
*   [Apply Conditional Formatting Based on Another Column in Excel](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/)
    
*   [How to Copy Conditional Formatting to Another Cell in Excel](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/)
    
*   [How to Remove Cell Formatting in Excel (from All, Blank, Specific Cells)](https://trumpexcel.com/remove-cell-formatting-in-excel/)
    
*   [Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [How to Apply Conditional Formatting in a Pivot Table in Excel](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    
*   [Excel Conditional Formatting Based on Another Cell](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-conditional-formatting-excel/#respond)

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
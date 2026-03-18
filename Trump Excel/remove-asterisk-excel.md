# Remove Asterisk (*) in Excel - 3 Easy Ways!

**Source:** https://trumpexcel.com/remove-asterisk-excel

---

[Skip to content](https://trumpexcel.com/remove-asterisk-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-asterisk-excel/#below-title)

Remove asterisk (\*) symbol In Excel is a little tricky as it’s a [wildcard character](https://trumpexcel.com/excel-wildcard-characters/)
 and you cannot just use fine and replace to remove an ace risk symbol.

But nothing to worry about – I’ll tell you a simple methods to quickly remove all the asterisk symbols from your data set using the Find and Replace method and a simple formula.

So let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-asterisk-excel/#)

Remove Asterisk Using Find and Replace
--------------------------------------

Let’s start with the [Find and Replace method](https://trumpexcel.com/find-and-replace-in-excel/)
.

Below I have a data set of names where some of the names have an asterisk (\*) symbol at the end, and I want to remove these asterisk symbols.

![Dataset to remove asterisk symbol](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20247%20405'%3E%3C/svg%3E)

Here are the steps to do this using Find and Replace:

1.  Select all the cells from which you want to remove the asterisk symbol
2.  Click the Home tab.

![Click the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20223'%3E%3C/svg%3E)

3.  In the editing group click on the Find and Select icon
4.  In the drop-down menu that shows up, click on the Replace option. This will open the find and replace dialog box with the Replace tab activated

![Click on the replace option in the drop down menu](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20403'%3E%3C/svg%3E)

_Note: You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 **Control + H** to open the find and replace dialog box_

5.  In the _Find what_ field, enter ~\* (~ followed by these \* symbol)

![Enter tilde followed by asterisk symbol in find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

5.  Leave the _Replace with_ field empty
6.  Click on Replace All.

![Click on the replace all button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

That’s it!

Excel would remove all the asterisk characters and show you a dialog box telling you how many replacements have been made.

When we add the ~ key before the \* symbol, it tells Excel to treat the asterisk symbol just like any other character (and not a wild card character)

Also read: [Remove Dashes/Hyphens in Excel](https://trumpexcel.com/remove-dashes-excel/)

Remove Asterisk Using SUBSTITUTE Formula
----------------------------------------

You can also use the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
 to quickly remove all the asterisk symbols in a cell in Excel.

Below I have the same data set where I have names in column A and I want to remove the asterisk signs from all of these cells.

You can do this by using the below formula:

\=SUBSTITUTE(A2,"\*","")

Enter this formula in cell B two and then copy it for all the other cells in the column.

![Substitute function to remove asterisk symbol](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20413'%3E%3C/svg%3E)

And if you have dynamic arrays in your [Excel version](https://trumpexcel.com/excel-version/)
 you can also use the below formula (where you do not need to copy it for the other cells as it will spill the results and fill the column automatically).

\=SUBSTITUTE(A2:A12,"\*","")

![Substitute function to remove asterisk symbol dynamic array](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20412'%3E%3C/svg%3E)

The above formulas would remove all the asterisk symbols in the cells.

If you want to remove specific instances of the asterisk symbols, you can use the third argument of the SUBSTITUTE function. For example the below formula would only remove the first instance of the \* symbol in the cell:

\=SUBSTITUTE(A2,"\*","",1)

Also read: [Remove Parentheses in Excel](https://trumpexcel.com/remove-parentheses-excel/)

VBA to Remove Asterisk Symbols from a Range of Selected Cells
-------------------------------------------------------------

And finally if you also use a VBA macro code to remove the asterisk symbol from a range of selected cells or even the entire worksheet.

    Sub RemoveAsterisks()
        Dim cell As Range
        For Each cell In Selection
            cell.Value = Replace(cell.Value, "*", "")
        Next cell
    End Sub

To use this above VBA code:

1.  Select all the cells from which you want to remove the \* symbol
2.  Hold the ALT key and press the F11 key to open the [VBA editor in Excel](https://trumpexcel.com/visual-basic-editor/)
    .
3.  Go to Insert option in the menu and click on Module. This will insert a new module for the workbook.
4.  Copy and paste the above code into the module.
5.  Place the cursor anywhere in the macro code and press the F5 key to run the macro.

As soon as you run the macro code, it would go through each cell in the selection and remove any ace risk symbol it finds.

Remember that the changes done by VBA macro codes are irreversible, so it’s always a good idea to create a backup copy of your data set before running the macro

In this article, I showed you three different methods you can use to remove asterisk symbols from cells in Excel.

I hope you found this article helpful. If you have any questions or suggestions for me, please let me know in the comments section below.

**Other Excel articles you may also like:**

*   [Remove Last Character in Excel](https://trumpexcel.com/remove-last-character/)
    
*   [Remove Characters From Left in Excel](https://trumpexcel.com/remove-characters-from-left-excel/)
    
*   [How to Remove Comma in Excel (from Text and Numbers)](https://trumpexcel.com/remove-comma-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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
# Select Till End of Data in a Column in Excel (Shortcuts)

**Source:** https://trumpexcel.com/select-end-of-data-in-column-excel

---

[Skip to content](https://trumpexcel.com/select-end-of-data-in-column-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/select-end-of-data-in-column-excel/#below-title)

Most of us work with tabular data in Excel where the data is arranged in columns.

And one of the common tasks most Excel users have to do is to go to the end of the data in the column (i.e., the last filled cell).

While you can quickly go to the end of the column to the last filled cell, or [select the entire column](https://trumpexcel.com/select-entire-column-excel/)
 till the last filled cell with an easy keyboard shortcut, things can get a bit complicated if you have blank cells in the column.

In this tutorial, I will show you a couple of simple methods (including keyboard shortcuts) that you can use to quickly select the end of the column in Excel.

The method you choose would depend on how your data is structured, and I’ll make sure to mention the pros and cons of each method that I covered in this tutorial.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/select-end-of-data-in-column-excel/#)

Keyboard Shortcut to Select the End of the Column (CONTROL + SHIFT + Arrow Key)
-------------------------------------------------------------------------------

Below, I have a data set where I have the items in column A and I have the expenses made every day in column B, and I want to select all the expense values in column B.

![Expense Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20308%20385'%3E%3C/svg%3E)

If your data set has no [blank cells](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
 in any of the cells in the column, you can easily select till the end of the column by using the below keyboard shortcut:

**Control + Shift + Down Arrow Key**

To use the above keyboard shortcut:

1.  Select the first cell that you want to be a part of the selection (cell B2 in this example)

![Select the first cell that you want in the selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20307%20385'%3E%3C/svg%3E)

2.  Hold the Control key and the Shift key (together)
3.  With the Control and  Shift key pressed, press the down arrow key once

With the above keyboard shortcut, Excel would magically start the selection from the first selected cell and extend it till the last filled cell in the column.

![Entire column selected till the end of data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20388'%3E%3C/svg%3E)

But life ain’t perfect, and the same can be said for your data in Excel.

Often, data in columns have [blank cells](https://trumpexcel.com/highlight-blank-cells-in-excel/)
 that can complicate selecting the entire column till the last filled cell.

### When there are Blank Cells in the Column

Below I have the same data set but there are some blank cells in column B, and I want to start with cell B2 and select till the end of the data in the column.

![Dataset with blank cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20387'%3E%3C/svg%3E)

With this data set, if you try and use the above keyboard shortcut, you would notice that the selection is made only till the cell before the first empty cell.

![Selection only till filled cell before blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20312%20387'%3E%3C/svg%3E)

So we need to use the same keyboard shortcut a little differently.

Below are the steps to select till the end of the data in a column when you have blank cells in the column:

1.  Select the first cell from which you want the selection to begin (cell B2 in our example)
2.  Hold the Control and the Shift key
3.  Press the down arrow key, and **keep it pressed**
4.  Once you have reached the end of the column in the worksheet, press the up arrow key (while still holding the Control and the Shift key)

While this is not the most elegant solution, it gets the work done, and if you do not have a lot of blank cells in your column, it could be quite fast.

One scenario where this may not be the best method to use is when you have a lot of blank cells (say a blank cell in every other row or after every two or three rows). While the method would still work in such a scenario, it could take a few more seconds (which in my experience is not something most Excel users are willing to give).

Also read: [Select Every Other Row in Excel](https://trumpexcel.com/select-every-other-row-excel/)

Keyboard Shortcut to Select the End of the Column (CONTROL + SHIFT + End)
-------------------------------------------------------------------------

Below, I have a data set where I want to select all the expense values in column B.

![Expense Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20308%20385'%3E%3C/svg%3E)

Here is another keyboard shortcut that you can use to select the end of the data in a column:

Control + Shift + End

Below are the steps to use this keyboard shortcut:

1.  Select the first cell from which you want the selection to begin (cell B2 in our example)
2.  Hold the Control and the Shift key
3.  Press the End key

The above steps would start the selection from cell B2, and select all the cells till the last used cell.

In most cases, the last cell in your column would also be the last used cell, so this keyboard shortcut should work perfectly in selecting the end of the data in the column.

And the great thing about this method is that you do not need to worry about blank cells, as it selects all the cells between the first selected cell and the last used cell.

### When You Have More Data On the Right

When you use Control + Shift + End, it starts the selection from the cell that you selected (B2 in our example), and extends the selection till the last cell in the used range.

So if you have more data on the right of the column, using the above keyboard shortcut would not only select the existing column but also any data that Is to the right,

And sometimes, the used range would remain in the memory of Excel even if you have deleted that data. For example, if I enter some value in the cell E20 and then delete it, the used range in excel would be A1:E20 (as E20 is the last used cell in the memory of Excel).

So there is a possibility that when you use the above keyboard shortcut, it selects more cells on the right and below the column that we intend to select.

In such a scenario, you can use the same keyboard shortcuts with a minor twist:

1.  Select the first cell from which you want the selection to begin (cell B2 in our example)
2.  Hold the Control and the Shift key
3.  Press the End key
4.  If additional [blank rows](https://trumpexcel.com/delete-blank-rows-excel/)
     and columns have been selected, keep the Control and Shift keys pressed, press the Left key once, and then press the Up arrow key once
5.  Hold the Shift key and keep pressing the left arrow key till only the column that you need is selected.

While this is not the most elegant solution, when you get used to it, you will find it faster than manually selecting a column till the end of the data.

Using the Name Box
------------------

[Name Box](https://trumpexcel.com/name-box-excel/)
 allows you to quickly select a range of cells by entering the reference in the name box.

You will find the name box on the left of the [formula bar](https://trumpexcel.com/show-hide-formula-bar-excel/)
, just below the formula bar.

![Name Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20306'%3E%3C/svg%3E)

Let’s say that I want to select column A (starting from cell A2) till the last filled cell, where I have blank cells in the column (which will make using the keyboard shortcut Control + Shift + Down arrow key challenging).

Below are the steps to use the name box to select the entire column A till the end of the data (i.e., till the last filled cell):

1.  Place the cursor in the Name Box
2.  Enter the below cell reference in the Name Box – A2:A1048576

![Enter A2 A1048576 in Namebox](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20320%20296'%3E%3C/svg%3E)

3.  Hit the Enter key. This will select all the cells in the specified range
4.  Hold the Control and the Shift key and then press the Up-arrow key.

The above steps would select all the cells in column A till the last filled cell.

**Note**: This method works in Google Sheets as well (you can use the exact same steps)

Using Go To Dialog Box
----------------------

Just like the Name Box, you can also use the Go To dialog box to quickly select a range of cells by specifying the reference of that range

Let’s say I want to select the range B2:B100.

Below are the steps to do this using the Go To dialog box

1.  Go to the worksheet where you want to select this range
2.  Press the F5 key on your keyboard. This will open the Go-To dialog box

![Go to Dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20348'%3E%3C/svg%3E)

3.  Enter the below [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
     in the Reference field

B2:B100

![Enter reference you want to select in Go To dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20348'%3E%3C/svg%3E)

4.  Click OK

There were steps that would instantly select the range that you specified in the Go-To dialog box.

So these are some of the shortcut ways you can use to quickly select data in a column till the end of the data.

While the methods I’ve covered here have been shown using data in a column, you can use the same methods to select data till the end of the rows as well

While you always have the option to do this manually using the mouse, if you need to do this quite often, knowing these shortcuts will significantly improve your efficiency.

**Other Excel articles you may also like:**

*   [7 Easy Ways to Select Multiple Cells in Excel](https://trumpexcel.com/select-multiple-cells-excel/)
    
*   [How to Select Non-adjacent cells in Excel? (4 Easy Ways)](https://trumpexcel.com/select-non-adjacent-cells-in-excel/)
    
*   [How to Deselect Cells in Excel (An Easy Way)](https://trumpexcel.com/deselect-cells-in-excel/)
    
*   [\[Quick Tip\] How to Select 500 cells/rows in Excel (with a single click)](https://trumpexcel.com/select-500-cells-rows/)
    
*   [3 Quick Ways to Select Visible Cells in Excel](https://trumpexcel.com/select-visible-cells/)
    
*   [How to Select Every Third Row in Excel (or select every Nth Row)](https://trumpexcel.com/select-every-third-row/)
    
*   [How to Quickly Select a Far-off Excel Cell or Range](https://trumpexcel.com/quickly-select-excel-cell-or-range/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/select-end-of-data-in-column-excel/#respond)

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
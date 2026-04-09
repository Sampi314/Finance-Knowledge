# Name Box in Excel - What is It and How to Best Use it?

**Source:** https://trumpexcel.com/name-box-excel

---

[Skip to content](https://trumpexcel.com/name-box-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/name-box-excel/#below-title)

Among the many awesome features in Excel, Name Box doesn’t get talked about enough.

While it looks like a simple name box (just like its name says), there are some cool things you can do with it.

In this article, I will cover everything you need to know about Name Box in Excel and some amazing things you can do with it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/name-box-excel/#)

What is Name Box in Excel?
--------------------------

Let’s start with the very basics – **What is a Name Box**?

Name Box is a simple text box that is located at the left part of the formula bar.

![Name Box in Excel Location](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20397%20296'%3E%3C/svg%3E)

It’s a bar below the ribbon containing only the Name Box and the Formula Bar.

You can also resize the Name Box by placing the cursor on the three dots between the Name Box and Formula Bar, clicking the left mouse key, and then dragging the cursor left or right.

![Resizing name box in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20426%20355'%3E%3C/svg%3E)

With a Name Box, you can do some useful things, such as:

*   Create a Named Range
*   Select any range of cells, rows, or columns in the same worksheet or any worksheet in the workbook.
*   Go to any macro subroutine by typing its name in the Name Box.
*   Assign Names of Charts or Shapes

I will cover how each of these (and some more) work in detail later in this article.

Note: If you want the cursor to go to the Name Box, you can use **ALT + F3** (hold the ALT key and press the F3 key), This will put your cursor in the name box

Where is the Name Box? Name Box Not Showing!
--------------------------------------------

If, for some reason, you can see the Name box, the most common reason would be that the entire Formula Bar grid is hidden.

Here are the steps to make the Name Box reappear in your Excel:

1.  Click the View Tab in the Ribbon
2.  Within the Show group, check the Formula Bar option.

![Hide or Show the Name Box in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20222'%3E%3C/svg%3E)

If the Formula Bar option is already checked and you still do not see the Name Box, try to uncheck it and then check it again.

If even this doesn’t work, try closing the Excel application and open it again.

Also read: [How to Hide or Show Formula Bar in Excel?](https://trumpexcel.com/show-hide-formula-bar-excel/)

Things You Can Do Using Name Box in Excel
-----------------------------------------

Now, let me show you some amazing time-saving things you can achieve by using the Name Box in Excel.

### Create Named Ranges

The most useful thing you can do using Name Box is [create a named range](https://trumpexcel.com/named-ranges-in-excel/)
.

A named range allows you to refer to a cell or range of cells with a name instead of the cell reference.

For example, instead of using A2:A20, you can give it a name, say _SalesData_, and then use the name SalesData instead of the range in formulas.

Let me show you how to create a named range using Name Box.

1.  Select the cell or range of cells for which you want to create a named range.
2.  Click on the Name Box to bring the cursor there. You can also use ALT + F3 to bring the cursor focus on the Name Box.
3.  Enter the name that you want to assign to the selected cell or range of cells.

![Creating a named range using name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20490%20600'%3E%3C/svg%3E)

4.  Press the Enter key.

The above steps would create a named range that would refer to the cells you selected in step 1. Now, instead of using the cell reference to the selected range of cells, you can use the name.

For example, if I selected B2:B10 as the range and used the name _SalesData_ to create the named range, I can use the below formula to get the SUM of this data:

\=SUM(SalesData)

![Formula using the named range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20663'%3E%3C/svg%3E)

When you click on the Name Box arrow, it will show you the list of all the Named Ranges you have created with it.

Also read: [How to Delete Named Range in Excel?](https://trumpexcel.com/delete-named-range-excel/)

### Go To a Specific Cell Quickly

If you want to go to any cell quickly, you can do so by entering that cell’s reference in the name box and hitting the Enter key.

For example, if I want to go to cell K10, I can manually enter K10 in the Name Box and then hit Enter. This would instantly take me to that cell.

![Enter the cell reference in the name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20356%20296'%3E%3C/svg%3E)

This would be useful if you need to often go to some specific cells that are far off in the worksheet.

Also read: [Select a Far-off Excel Cell or Range](https://trumpexcel.com/quickly-select-excel-cell-or-range/)

### Select a Range of Cells (or Select Rows/Columns)

You can also use the Name Box to select a range of cells anywhere in the worksheet.

For example, if I want to select the range A1:D20, I can do this by entering this cell reference in the name box and hitting the enter key.

![Enter the Range reference in the name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20401%20321'%3E%3C/svg%3E)

When I enter two cell references with a colon in between, the Name Box considers that to be the entire range that needs to be selected.

If you want to select an entire row (say the first row), enter 1:1 in the Name Box and press Enter.

To select multiple rows, you can enter the starting row number and the ending row number with a colon between them. For example, to select rows 2, 3, and 4, you need to enter 2:4 in the Name box and hit the Enter key.

Similarly, to select one column (say column A), enter A:A in the Name Box and press Enter.

And to select multiple columns, enter the starting column number and the ending column number with a colon between. So, to select columns B, C, and D, enter B:D in the Name Box and press enter.

| To Select | Example |
| --- | --- |
| Entire Row | 1:1 |
| Entire Column | A:A |
| Multiple Contiguous Rows | 1:4 |
| Multiple Contiguous Columns | A:D |

Also read: [Shortcut to Select Entire Column (or Row) in Excel](https://trumpexcel.com/select-entire-column-excel/)

### Select Multiple Range of Cells (Non Contiguous)

You can also use the Name Box to select cells or ranges that are not continuous. To do this, you need to enter all the different cells or ranges with commas in between in the name box.

To select two non-adjacent cells (say A1 and D4), you need to enter A1,D4 in the Name Box and then press enter. This will select both the cells at the same time.

![Selecting multiple non adjacent cells with name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20350%20295'%3E%3C/svg%3E)

Similarly, you can also do this with ranges. For example, if I want to select A1:B20 and H5:K10, I can enter _A1:B20,H5:K10_ in the Name Box and press enter.

If you have created name ranges, instead of using the cell references, you can also use the names of those named ranges.

Also read: [Select Every Other Row in Excel](https://trumpexcel.com/select-every-other-row-excel/)

### Navigate to Another Sheet

If you are working with many worksheets in your workbook, you can also use Name Box to quickly navigate to another sheet.

To do this, you need to enter the name of the sheet in the name box along with a cell reference in that sheet.

For example, if I want to go to Sheet2, then I can enter _Sheet2!A1_ in the Name Box, and it will take me to cell A1 in Sheet2.

![Selecting another sheet using name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20313'%3E%3C/svg%3E)

Note that you always need to have an exclamation mark after the sheet name and before the cell reference in that sheet.

In case there are spaces in the name in your worksheet, you need to put the worksheet name within single quotes followed by the exclamation mark and the cell reference of that sheet to which you want to go.

For example, if my sheet name is _Sales Data_, then I will have to enter _‘Sales Data’!A1_ in the name box.

Also read: [How to Switch Between Sheets in Excel?](https://trumpexcel.com/switch-between-sheets-excel/)

### Get the Number of Rows and Columns in the Selected Range

Name box also shows you the total number of rows and columns in a selected range while you are selecting it.

When you hold the left mouse key and select a range manually in a worksheet, you will notice that the row number and column number are shown in the name box in the following format – 10R x 2C.

![Name Box showing the rows and columns in selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20375%20614'%3E%3C/svg%3E)

This tells me that there are ten rows and two columns in the selected range.

### Assign Names to Chart Objects or Shape Objects

Whenever you insert a chart object or any shape object in a worksheet in Excel, it gets a default name, which would be something like _Rectangle: Rounded Corners 1_

You can select any shape or chart in your worksheet and then change its name by typing it manually in the Name Box.

![Naming a chart using name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20343'%3E%3C/svg%3E)

This could be useful when you’re working with multiple charts or shapes and you want to quickly select one specific chart/shape.

So if I have named all my charts, I want to go to any specific chart, no matter where I am in my workbook, I can just enter the name of that chart in the name box and hit the enter key, and that chart would get selected.

### Go to the VBA Macro Code By Typing the Name in the Name Box

If you work with a lot of macros and subroutines, here is a neat trick for you.

Enter the name of any subroutine in the name box, and as soon as you press the enter key, it will automatically open the VB editor and place your cursor in that subroutine.

I’ve recently learned this Name Box trick, and I think I’ll be using it a lot now.

Also read: [Useful Excel Macro Examples for VBA Beginners](https://trumpexcel.com/excel-macro-examples/)

### Select Current Row or Column

Here’s another one that I don’t think many people know about.

If you enter the letter R in the name box and hit the enter key, it will automatically select the current row in the worksheet.

![Enter r to select entire row in name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20295'%3E%3C/svg%3E)

And, if you enter the alphabet C in the name box and hit the Enter key, it will automatically select the current column in the worksheet.

![Enter c to select entire row in name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20325%20293'%3E%3C/svg%3E)

And this is not case-sensitive, so you can enter R or r and C or c.

FAQs about Name Box in Excel
----------------------------

Below are some commonly asked questions people have about the Name Box.

### What is the Difference Between Name Box and Formula Bar?

While both Formula Bar and Name Box are part of the same bar in the Excel interface, they have different purposes.

The Formula bar is where you can write your formula and also edit the content of the cell.

Name Box is where you can name a cell or a range of cells to create name ranges and also quickly navigate to cells or ranges in the same worksheet or other worksheets.

### Can I place the Name Box above the ribbon?

As far as I know, there is no way for you to place the name box bar above the ribbon. The only flexibility you get with the name box is to either hide it or resize it.

### Is there a shortcut to hide and show the Name Box in Excel?

To hide a Name Box, you will have to hide the entire formula bar. This can be done using the shortcut **ALT + W + V + F** (press these keys one after the other in succession). This works as a toggle, so if you use the keyboard shortcut once and the Formula Bar and Name Box are hidden, it will get visible, and if it is visible, it will get hidden.

In this article, I covered everything you need to know about the Name Box in Excel, as well as some useful tricks you can use in your day-to-day work.

I hope you found this article helpful. If there are any other name box tricks that you use and that I have not covered in this article already, let me know in the comments section.

**Other Excel articles you may also like:**

*   [Using Find and Replace in Excel](https://trumpexcel.com/find-and-replace-in-excel/)
    
*   [How to Select Non-adjacent Cells in Excel?](https://trumpexcel.com/select-non-adjacent-cells-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/name-box-excel/#respond)

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
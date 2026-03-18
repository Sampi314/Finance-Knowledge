# How to Remove Line Breaks in Excel (3 Easy Ways)

**Source:** https://trumpexcel.com/remove-line-break-excel

---

[Skip to content](https://trumpexcel.com/remove-line-break-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-line-break-excel/#below-title)

If you work with data that is imported from databases or salesforce, you’ve probably already dealt with line breaks.

A line break is something that allows you to have multiple lines in the same cell in Excel.

Below is an example of a name and address dataset wherein a single line, name and different parts of the address are separated by a line break.

While it looks great in the above example, sometimes, you may not want these line breaks and have a need to remove these line breaks from the dataset.

In this tutorial, I will show you three simple ways to **remove line breaks in Excel** (also called in-cell **carriage return** in Excel).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-line-break-excel/#)

Remove Line Breaks Using Find and Replace
-----------------------------------------

The easiest way to remove line breaks manually is by using Find and Replace.

You can easily apply this to a large dataset and Find and Replace will do all the heavy lifting by finding all the line breaks and removing them from the cells.

Suppose you have a dataset of addresses as shown below from which you want to remove the line breaks.

![Address dataset from which line breaks need to be removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20302%20470'%3E%3C/svg%3E)

Below are the steps to remove line breaks using Find and Replace and replace it with a comma:

1.  Select the dataset from which you want to remove the line breaks
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20200'%3E%3C/svg%3E)
3.  In the Editing group, click on ‘Find & Select’![Click on Find and Select](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20276%20137'%3E%3C/svg%3E)
4.  In the options that show up, click on ‘Replace’![Click on Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20281%20436'%3E%3C/svg%3E)
5.  Place the cursor in the ‘Find what’ field and use the keyboard shortcut – Control + J (hold the Control key and press the J key). You may not see anything, but this puts the line break character in the ‘Find what’ field![Use Control J in Find and Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20250'%3E%3C/svg%3E)
6.  In the replace field, enter a comma followed by a space character (, )![Enter comma followed by space character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20250'%3E%3C/svg%3E)
7.  Click on Replace All

The above steps would remove all the line breaks and replace these with a comma. This will give you the result in a single line in a cell in Excel.

![Result after line breaks have been removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20407'%3E%3C/svg%3E)

In case you want to remove the line break and want to replace it with something else instead of the comma, then you need to specify that in Step 6 (in the ‘Replace with’ field)

Note: It’s recommended to create a backup copy of the file that has the data so that you don’t lose it in case you need it in the future.

Remove Line Breaks Using Formula
--------------------------------

Another way to get rid of line breaks in Excel is by using a formula. While the Find & Replace method gives you static results, the formula will give you results that will automatically update in case you make any changes in the original dataset.

Suppose you have the dataset as shown below and you want to remove the line breaks from all the cells.

![Address dataset from which line breaks need to be removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20302%20470'%3E%3C/svg%3E)

Below is the formula that will do this:

\=SUBSTITUTE(A2,CHAR(10),"")

The SUBSTITUTE function finds and replaces the CHAR(10) character – which represents the line feed character. So, the above formula finds all the line breaks and replace these with blank – which essentially means that these line breaks have been removed.

In case you want the result to be separated a comma (or any other character), you can use the below formula:

\=SUBSTITUTE(A2,CHAR(10),", ")

![formula to remove line breaks with comma and space in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20694%20525'%3E%3C/svg%3E)

Note: In case you’ve got the [Wrap-text](https://trumpexcel.com/wrap-text/)
 enabled in a cell where you get the result of the formula, you may still see some text moving to the next line in the same cell. This is not because of line breaks. If you adjust the column

Remove Line Breaks Using VBA
----------------------------

If you’re comfortable using VBA, this could be the fastest way to get rid off the line breaks in Excel.

But you got to do some work before making it a one-click operation.

Below is the VBA code that will go through each cell in the

Sub RemoveLineBreaks()
For Each Cell In Selection
Cell.Value = Replace(Cell.Value, Chr(10), ", ")
Next
End Sub

The above code uses the REPLACE function in VBA to replace all the line break characters in a cell with a comma followed by the space character.

The result of this VBA code is static and you can not undo this. So, if you’re planning to use it, I highly recommend you create a copy of the original dataset before using the code.

You can put this code in a regular module in Excel, and in case you have to use it often and need it available in all your Excel workbooks, you can save this code either in the Personal Macro Workbook, or you can add it as an Excel Add-in.

If you want to use it with a single click, you can add this macro code to the Quick Access Toolbar. This way, all you need to do is make the selection and click on the macro button in the QAT to [run the code](https://trumpexcel.com/run-a-macro-excel/)
.

Line Break Vs. Carriage Return
------------------------------

There is a minor difference between a line break in Excel and in a carriage return.

A carriage return’s function is to take the cursor at the beginning of the sentence. It was made use in the early versions of typewriters and later in computers. A carriage return by itself would not lead to a line break in Excel. When combined with Line Feed, it results in a line break.

In most cases, when you see a line break in Excel, there is carriage return in it.

Also, when you use ALT Enter to [insert a line break in Excel](https://trumpexcel.com/insert-line-break-in-excel/)
, it only inserts a line feed and not carriage return.

Then why should we worry about carriage return? Because you may get it in your data in case it has been downloaded from a database that uses carriage return.

The ASCII code of a carriage return is 13 (CR, ASCII code 13) and you can find and replace it using formulas.

You can read more about the difference between a line feed and carriage return [here](https://stackoverflow.com/questions/12747722/what-is-the-difference-between-a-line-feed-and-a-carriage-return)
.

I hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [How to Split Multiple Lines in a Cell into a Separate Cells / Columns](https://trumpexcel.com/split-multiple-lines/)
    
*   [How to Start a New Line in Excel Cell (Keyboard Shortcut + Formula)](https://trumpexcel.com/start-a-new-line-in-excel-cell/)
    
*   [How to Combine Cells in Excel](https://trumpexcel.com/combine-cells-in-excel/)
    
*   [How to Remove Dashes (-) in Excel?](https://trumpexcel.com/remove-dashes-excel/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [How to Remove Comma in Excel (from Text and Numbers)](https://trumpexcel.com/remove-comma-excel/)
    
*   [How to Insert/Draw a Line in Excel (Straight Line, Arrows, Connectors)](https://trumpexcel.com/draw-line-excel/)
    
*   [How to Edit Cells in Excel? (Shortcuts)](https://trumpexcel.com/edit-cells-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Remove Line Breaks in Excel (3 Easy Ways)”
----------------------------------------------------------------

1.  Step-1 doesn’t work in excel 2013 version
    
    [Reply](https://trumpexcel.com/remove-line-break-excel/#comment-44043)
    
2.  Doesn’t work on the Mac… 🙁
    
    [Reply](https://trumpexcel.com/remove-line-break-excel/#comment-33572)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-line-break-excel/#respond)

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
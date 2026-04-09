# How to Get the Sheet Name in Excel? Easy Formula

**Source:** https://trumpexcel.com/get-sheet-name-excel

---

[Skip to content](https://trumpexcel.com/get-sheet-name-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/get-sheet-name-excel/#below-title)

When working with Excel spreadsheets, sometimes you may have a need to get the name of the worksheet.

While you can always manually enter the sheet name, it won’t update in case the sheet name is changed.

So if you want to get the sheet name, so that it automatically updates when the name is changed, you can use a simple formula in Excel.

In this tutorial, I will show you how to get the sheet name in Excel using a simple formula.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/get-sheet-name-excel/#)

Get Sheet Name Using the CELL Function
--------------------------------------

CELL function in Excel allows you to quickly get information about the cell in which the function is used.

This function also allows us to get the entire [file name](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
 as a result of the formula.

Suppose I have an Excel workbook with the sheet name ‘Sales Data’

Below is the formula that I have used in any cells in the ‘Sales Data’ worksheet:

\=CELL("filename"))

![CELL formula to get workbook name and address](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20672%20253'%3E%3C/svg%3E)

As you can see, it gave me the whole address of the file in which I am using this formula.

But I needed only the sheet name, not the whole file address,

Well, to get the sheet name only, we will have to use this formula along with some other text formulas, so that it can extract only the sheet name.

Below is the formula that will give you only the sheet name when you use it in any cell in that sheet:

\=RIGHT(CELL("filename"),LEN(CELL("filename"))-FIND("\]",CELL("filename")))

![formula to get the sheet name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20750%20247'%3E%3C/svg%3E)

The above formula will give us the sheet name in all scenarios. And the best part is that it would automatically update in case you change the sheet name or the file name.

Note that the CELL formula only works if you have saved the workbook. If you haven’t, then it would return a blank (as it has no idea what the workbook path is)

**Wondering how this formula works? Let me explain!**

The CELL formula gives us the whole workbook address along with the sheet name at the end.

One rule it would always follow is to have the sheet name after the square bracket (\]).

Knowing this, we can find out the position of the square bracket, and then extract everything after it (which would be the sheet name)

And that’s exactly what this formula does.

The [FIND](https://trumpexcel.com/excel-find-function/)
 part of the formula looks for ‘\]’ and return it’s position (which is a number that denotes the number of characters after which the square bracket is found)

We use this position of the square bracket within the [RIGHT formula](https://trumpexcel.com/excel-right-function/)
 to extract everything after that square bracket

One major issue with the CELL formula is that it’s dynamic. So if you use it in Sheet1 and then go to Sheet2, the formula in Sheet1 would update and show you the name as Sheet2 (despite the formula being on Sheet1). This happens as the CELL formula considers the cell in the active sheet and gives the name for that sheet, no matter where it is in the workbook. A workaround would be to hit the F9 key when you want to update the CELL formula in the active sheet. This will force a recalculation.

### Alternative Formula to Get Sheet Name (MID formula)

There are many different ways to do the same thing in Excel. And in this case, there is another formula that works just as well.

Instead of the RIGHT function, it uses the [MID function](https://trumpexcel.com/excel-mid-function/)
.

Below is the formula:

\=MID(CELL("filename"),FIND("\]",CELL("filename"))+1,255)

This formula works similarly to the RIGHT formula, where it first finds the position of the square bracket (using the FIND function).

It then uses the MID function to extract everything after the square bracket.

Fetching Sheet Name and Adding Text to it
-----------------------------------------

If you’re building a dashboard, you may want to not just get the name of the worksheet, but also append a text before or after it.

For example, if you have a sheet name 2021, you may want to get the result as ‘Summary of 2021’ (and not just the sheet name).

This can easily be done by combining the formula we saw above with the text we want before it using the ampersand operator.

Below is the formula that will add the text ‘Summary of ‘ before the sheet name:

\="Summary of "&RIGHT(CELL("filename"),LEN(CELL("filename"))-FIND("\]",CELL("filename")))

![Formula to append text before the sheet name in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20775%20304'%3E%3C/svg%3E)

The ampersand operator (&) simply combines the text before the formula with the result of the formula. You can also use the CONCAT or [CONCATENATE function](https://trumpexcel.com/excel-concatenate-function/)
 instead of an ampersand.

Similarly, if you want to add any text after the formula, you can use the same ampersand logic (i.e., have the ampersand after the formula followed by the text that you want to append).

So these are two simple formulas that you can use to get the sheet name in Excel.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Rename a Sheet in Excel (4 Easy Ways + Shortcut)](https://trumpexcel.com/rename-sheet-in-excel/)
    
*   [How to Insert New Worksheet in Excel (Easy Shortcuts)](https://trumpexcel.com/insert-new-worksheet-excel/)
    
*   [How to Unhide Sheets in Excel (All In One Go)](https://trumpexcel.com/unhide-sheets-excel/)
    
*   [How to Sort Worksheets in Excel using VBA (alphabetically)](https://trumpexcel.com/sort-worksheets/)
    
*   [Combine Data From Multiple Worksheets into a Single Worksheet in Excel](https://trumpexcel.com/combine-multiple-worksheets/)
    
*   [How to Compare Two Excel Sheets](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [How to Group Worksheets in Excel](https://trumpexcel.com/group-worksheets-in-excel/)
    
*   [Add Sheet Name to Header or Footer in Excel](https://trumpexcel.com/add-sheet-name-to-header-footer-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Get the Sheet Name in Excel? Easy Formula”
---------------------------------------------------------------

1.  This formula makes all cells with that formula, across all sheets the same value.
    
    [Reply](https://trumpexcel.com/get-sheet-name-excel/#comment-35703)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/get-sheet-name-excel/#respond)

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
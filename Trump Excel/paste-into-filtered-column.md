# Paste into Filtered Column (Skipping Hidden Cells) in Excel

**Source:** https://trumpexcel.com/paste-into-filtered-column

---

[Skip to content](https://trumpexcel.com/paste-into-filtered-column/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/paste-into-filtered-column/#below-title)

Excel is an amazing spreadsheet tool, but there are some things that drive me crazy.

One such thing is when you need to copy and paste data into a column with filtered rows.

Excel would paste this data into the visible cells as well as the hidden cells that have been filtered out. In most cases, this is not what you want. In most cases, you want to paste your data only in the visible cells and not the hidden ones.

So how do we do this then?

In this article, I will show you a couple of workarounds for pasting into filtered columns in Excel while skipping the hidden cells.

Since there is no one solution that fits all, I will show you different scenarios and the most appropriate solution for each scenario (including a simple VBA code that works great).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/paste-into-filtered-column/#)

Copy Paste One Single Cell Value in a Filtered Column
-----------------------------------------------------

Let’s start with the most straightforward example.

Below, I have a dataset that I am going to use.

![Full dataset to paste into filtered cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20475%20552'%3E%3C/svg%3E)

Now, I have filtered this data to only show the records for the Marketing department.

![Filtered Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20281'%3E%3C/svg%3E)

Now, I want to copy the value in cell G1 and paste the same in all the visible cells in column D (i.e., only the cells that are visible and not the ones that are hidden after filtering).

![Copy one cell in filtered dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20215'%3E%3C/svg%3E)

This is very easy, as you can simply copy the value in cell G1, then select all the cells in column D and paste it.

Here are the steps to do this:

1.  Copy cell G1.
2.  Select all the cells in column D in which you want to paste the value in G1.

![Select filtered cells in which you want to paste](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20702%20215'%3E%3C/svg%3E)

3.  Use Control + V to paste the value. You can also right-click on any of the visible cells and then click on Paste Values.

![Copied cell pasted into the filtered cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20282'%3E%3C/svg%3E)

When I copied cell G1 and then selected cells in a column that has a filter applied to it, and then pasted the cell, it was only pasted in the cells that were visible.

You can confirm this by removing the filter, and you will notice that the value in cell G1 has only been pasted in the cells that were visible when the filter was applied.

Also read: [Copy Visible Cells Only in Excel](https://trumpexcel.com/copy-visible-cells/)

Copy Paste Cells from the Same Row in a Filtered Column
-------------------------------------------------------

Let’s look at another situation (which is not as straightforward).

Below, I have a filtered data set, and I have some values in column G that I want to copy and paste into the visible cells in column D.

![Dataset with data to copy in the same row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20737%20253'%3E%3C/svg%3E)

Now, you cannot do a simple copy and paste in this situation, as it won’t work.

If I copy the cells in column G, it is only going to copy the cells that are visible, but if I then paste it in the cells in column D, it is going to paste it in the visible cells as well as the ones that are not visible.

So if you try it, you may end up getting a result as shown below.

![Issue with regular copy paste](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20737%20256'%3E%3C/svg%3E)

Also, if you think you can try [selecting only the visible cells](https://trumpexcel.com/select-visible-cells/)
 in column D (which you can do by using the shortcut ALT + semicolon) and then paste the values copied from column G, Excel will give you the following error.

![Error when trying to paste in visible cells only](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20732%20500'%3E%3C/svg%3E)

Thankfully, when you have the values that you want to copy in the same row as your filter data set, you can use a very simple formula.

Here are the steps to do this:

1.  Select cell D6 (which is the first cell in our filtered data set in column D)
2.  Enter an equal to sign
3.  Select cell F6. This will make the reference in cell D6 as =F6.

![Enter the reference to cell in the first cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20733%20253'%3E%3C/svg%3E)

4.  Press the Enter key
5.  Copy the formula in all the cells in the column. You can do a simple copy-paste or drag the fill handle down to apply the formula to the entire column.

![Copy the formula for all the cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20735%20253'%3E%3C/svg%3E)

5.  Once you have the values in column D, you can select all the cells again and then convert the formula into values. To do this, select the cells, then use Control + C to copy them, and then use Control + Shift + V to paste the formula as values.

The good thing here is that when you copy and paste a formula in all the cells in a filtered dataset, it is only copied to the visible cells.

While this method works great, it’s likely that you may not get the data you want to copy and paste into the filtered rows in the same rows.

What if the data you want to copy and paste into the filtered rows is in a different location in the same worksheet or in a completely different worksheet or workbook?

The next two methods would tackle that.

Also read: [How to Copy and Paste Column in Excel?](https://trumpexcel.com/copy-paste-column-excel/)

Copy Paste Cells From Another Range Sheet or Workbook into a Filtered Column
----------------------------------------------------------------------------

Below, I have a filtered data set.

![Filtered Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20281'%3E%3C/svg%3E)

I also have some values on a different sheet that I want to copy and paste into column D in our filter dataset above.

![Data set in a different sheet that I need to copy paste into the filtered column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20376%20282'%3E%3C/svg%3E)

No copy-paste trick would work in this situation, so I have to get a bit creative.

Now, there could be two situations.

1.  There is a common column in both datasets that I can use to fetch the value from the table in the worksheet to get the result in the filtered dataset. For example, in our case, I can use the Names column in both datasets to look up the value in the worksheet and fetch it in the filter data set.
2.  There is no common column, and I cannot use any lookup formulas

Let’s see what to do in both of these situations.

### Using VLOOKUP (if there is a lookup Value)

Let’s first take an example where I have the names column in both datasets, and I can use a lookup function ([VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
 or [XLOOKUP](https://trumpexcel.com/xlookup-function/)
) to fetch the value for each name in the filtered dataset.

Below is the VLOOKUP formula that would work:

\=VLOOKUP(A6,'Copy From'!$A$2:$B$8,2,0)

Enter this formula in cell D6 (or whatever is the first cell in the filtered column) and then copy it for all the other cells.

![VLOOKUP to get values in filtered column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20716%20324'%3E%3C/svg%3E)

In case you prefer using XLOOKUP, you can use the below formula

\=XLOOKUP(A6,'Copy From'!$A$2:$A$8,'Copy From'!$B$2:$B$8,"",0)

Once you have the formula results, you can convert these formulas into static values, and you’re done.

Also read: [Copy and Paste Multiple Cells in Excel (Adjacent & Non-Adjacent)](https://trumpexcel.com/copy-paste-multiple-cells-excel/)

### Using VBA (works in all scenarios)

Now, let’s talk about the most complicated situation (which is also perhaps the most common one).

I have the filtered data set below.

![Filtered Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20281'%3E%3C/svg%3E)

I have these values in a different worksheet or workbook, and I want to copy and paste them into column D in the filtered column.

![Data to copy into the filtered column skipping visible cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20160%20291'%3E%3C/svg%3E)

There is no common column, so I cannot use any lookup formulas.

In such a case, I will have to rely on the big guns – a VBA macro code.

Below is the VBA macro code that would do this for me:

    Sub PasteintoFilteredColumn()
    
        Dim visibleSourceCells As Range
        Dim destinationCells As Range
        Dim initialDestinationLastRow As Long
        Dim sourceCell As Range
        Dim destCell As Range
    
        Set visibleSourceCells = Application.Selection.SpecialCells(xlCellTypeVisible)
    
        
        Set destinationCells = Application.InputBox("Please select the destination cells:", Type:=8)
        
        Application.ScreenUpdating = False
        
        
        initialDestinationLastRow = destinationCells.Rows(destinationCells.Rows.Count).Row
    
        
        For Each sourceCell In visibleSourceCells.Cells
            
            For Each destCell In destinationCells.Cells
                If destCell.EntireRow.Hidden = False Then
                   
                    sourceCell.Copy
                    destCell.PasteSpecial Paste:=xlPasteValues
                    
                    If destCell.Row < initialDestinationLastRow Then
                        Set destinationCells = destCell.Offset(1, 0).Resize(initialDestinationLastRow - destCell.Row)
                    End If
                    
                    Exit For
                End If
    
            Next destCell
        Next sourceCell
    
        Application.CutCopyMode = False
        Application.ScreenUpdating = True
        
    End Sub
    

Here are the steps to put the VBA code in the backend in Excel:

1.  Hold the ALT key and then press the F11 key. This will [open the Visual Basic editor](https://trumpexcel.com/visual-basic-editor/)
     in the workbook. You can also do the same thing by clicking on the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then clicking on the Visual Basic icon.
2.  In the VB Editor, click on the _Insert_ option in the menu and then click on _Module_. This will insert a new module where we will copy and paste the above VBA macro code.

![Insert a new module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20236%20233'%3E%3C/svg%3E)

3.  Copy and paste the above VBA code into the Module code window.

![Copy paste the code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20417'%3E%3C/svg%3E)

4.  Click on the Save icon and close the VB editor.

![Save the VBA code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20270%20124'%3E%3C/svg%3E)

Now that we have the VBA code in place, below are other steps to use it to copy data into the filtered data set while skipping the hidden cells:

1.  Select the cells that you want to copy and paste.

![Select the cells you want to copy](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20168%20292'%3E%3C/svg%3E)

2.  Click the Developer tab and then click on the Macros icon. This will open the Macros dialog box.

![Click on the Macros icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20168'%3E%3C/svg%3E)

3.  Select the _PasteintoFilteredColumn_ macro and then click on Run.

![Select and run the macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20470'%3E%3C/svg%3E)

4.  It will show you an input message box asking you to select the destination cells where you want to paste these selected data.

![Input box to select the cells to copy in filtered cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20398%20149'%3E%3C/svg%3E)

5.  Navigate to the filtered data and select the cells where you want to paste the previously selected data.

![Select the cells to paste in filtered columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20483%20221'%3E%3C/svg%3E)

6.  Click OK

As soon as you click OK, the magic behind the screen begins, and VBA pastes the data only into the visible filtered cells.

![VBA copies cells into the filtered cells skipping hidden cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20483%20220'%3E%3C/svg%3E)

CAVEAT: Remember that the changes done by a VBA code cannot be undone, so it’s always a good idea to keep a backup copy of your data set

Also read: [How to Select Entire Column (or Row) in Excel – Shortcut](https://trumpexcel.com/select-entire-column-excel/)

Use Google Sheets to Paste into Filtered Column
-----------------------------------------------

And finally, if you’re ok with putting your data in Google Sheets, then you don’t need any special tricks or formulas or VBA code.

Regular copy-paste is going to work in Google Sheets.

Let me show you how it works.

Below, I have the same filtered data set in Google Sheets.

![Data in Google Sheets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20265'%3E%3C/svg%3E)

In another sheet, I have these values in a column that I want to copy and paste into column D in my filter data set.

Here is how it works in Google Sheets:

1.  Copy the data that you want to paste (you can use Control + C).
2.  Select the filtered column range in which you want to paste this data
3.  Paste the Data (use Control + V)

![Copied to cells in filtered dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20265'%3E%3C/svg%3E)

And that’s it – it’s that simple.

When it comes to pasting data in filtered rows, Excel and Google Sheets work differently. While Excel always pastes the data in all the cells, whether visible or not, Google Sheets only pastes the data in the visible cells.

So, if it is possible for you to convert your Excel file into a Google Sheets or copy-paste data into a Google Sheets, then get the copy-paste done, and then bring the data back into Excel, you can also use this method.

Note: Remember that by default, there are only 1000 rows in Google Sheets. So if your data set is bigger than that, you need to increase the number of rows in Google Sheets first.

So these are some of the methods you can use to paste data into filtered column while skipping the hidden cells.

While I wish this were the default behavior in Excel, I hope the methods covered in this article help you get this done easily.

I hope you found this article helpful. In case you have any questions or you know of a method that can be used that I should have covered, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [Highlight Active Row and Column in Excel (VBA)](https://trumpexcel.com/highlight-active-row-column-excel/)
    
*   [How to Count Filtered Rows in Excel?](https://trumpexcel.com/count-filtered-rows-excel/)
    
*   [Dynamic Excel Filter Search Box – Extract Data as you Type](https://trumpexcel.com/dynamic-excel-filter/)
    
*   [Delete Rows Based on a Cell Value (or Condition) in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Paste into Filtered Column (Skipping Hidden Cells) in Excel”
--------------------------------------------------------------------------

1.  Hi! I’m Dusan  
    Thanks for posting the article “Paste in filtered column (skip hidden cells) in Excel”. The analysis of the macro code in VBA Excel helped me the most, because I deal with programs in VBA Excel.  
    Sincerely, Dušan!
    
    [Reply](https://trumpexcel.com/paste-into-filtered-column/#comment-32432)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/paste-into-filtered-column/#respond)

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
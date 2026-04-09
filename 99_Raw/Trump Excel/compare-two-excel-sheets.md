# How to Compare Two Excel Sheets (for differences)

**Source:** https://trumpexcel.com/compare-two-excel-sheets

---

[Skip to content](https://trumpexcel.com/compare-two-excel-sheets/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/compare-two-excel-sheets/#below-title)

**Watch Video – How to Compare Two Excel Sheets for Differences**

Comparing two Excel files (or comparing two sheets in the same file) can be tricky as an Excel workbook only shows one sheet at a time.

This becomes more difficult and error-prone when you have a lot of data that needs to be compared.

Thankfully, there are some cool features in Excel that allow you to open and easily compare two Excel files.

In this Excel tutorial, I will show you multiple ways to **compare two different Excel files (or sheets)** and check for differences. The method you choose will depend on how your data is structured and what kind of comparison you’re looking for.

Let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/compare-two-excel-sheets/#)

Compare Two Excel Sheets in Separate Excel Files (Side-by-Side)
---------------------------------------------------------------

If you want to compare two separate Excel files side by side (or two sheets in the same workbook), there is an in-built feature in Excel to do this.

It’s the _**View Side by Side**_ option.

This is recommended only when you have a small dataset and manually comparing these files is likely to be less time-consuming and error-prone. If you have a large dataset, I recommend using the conditional method or the formula method covered later in this tutorial.

Let’s see how to use this when you have to compare two separate files or two sheets in the same file.

Suppose you have two files for two different months and you want to check what values are different in these two files.

![Two files that need to be compared](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20782%20577'%3E%3C/svg%3E)

By default, when you open a file, it’s likely to take up your entire screen. Even if you reduce the size, you always see one Excel file at the top.

With the view side-by-side option, you can open two files and then arrange these horizontally or vertically. This allows you to easily compare the values without switching back and forth.

Below are the steps to align two files side by side and compare them:

1.  Open the files that you want to compare.
2.  In each file, select the sheet that you want to compare.
3.  Click the View tab![Click the view tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20685%20199'%3E%3C/svg%3E)
4.  In the Windows group, click on the ‘View Side by Side’ option. This becomes available only when you have two or more Excel files open.![Click on View Side by Side option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20585%20156'%3E%3C/svg%3E)

As soon as you click on the View side by side option, Excel will arrange the workbook horizontally. Both of the files will be visible, and you’re free to edit/compare these files while they are arranged side by side.

![Files get arranges side by side to be compared](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20419'%3E%3C/svg%3E)

In case you want to arrange the files vertically, click on the Arrange All option (in the View tab).

![Click on Arrange all to decide how to align these workbooks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20155'%3E%3C/svg%3E)

This will open the ‘Arrange Windows’ dialog box where you can select ‘Vertical’.

![Click on Vertical and then click on Ok](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20255'%3E%3C/svg%3E)

At this point, if you scroll down in one of the worksheets, the other one would remain as is. You can change this so that when you scroll in one sheet, the other also scrolls at the same time. This makes it easier to do a line by line comparison and spot any differences.

But to do this, you need to enable **Synchronous Scrolling.**

To enable Synchronous Scrolling, click on the View tab (in any of the workbooks) and then click on the Synchronous Scrolling option. This is a toggle button (so if you want to turn it off, simply click on it again).

![Click on Synchronous scrolling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20576%20157'%3E%3C/svg%3E)

### Comparing Multiple Sheets in Separate Excel Files (Side-by-Side)

With the ‘View Side by Side’ option, you can only compare two Excel file at one go.

In case you have multiple Excel files open, when you click on the View Side by Side option, it will show you a ‘Compare Side by Side’ dialog box, where you can choose which file you want to compare with the active workbook.

In case you want to compare more than two files at one go, open all these files and then click on the Arrange All option (it’s in the View tab).

![Click on Arrange all to decide how to align these workbooks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20155'%3E%3C/svg%3E)

In the Arrange Windows dialog box, select Vertical/Horizontal and then click OK.

This will arrange all the open Excel files in the selected order (vertical or horizontal).

Compare Two Sheets (Side-by-Side) in the Same Excel Workbook
------------------------------------------------------------

In case you want to compare two separate sheets in the same workbook, you can’t use the View side by side feature (as it works for separate Excel files only).

But you can still do the same side-by-side comparison.

This is made possible by the ‘**New Windows’ feature** in Excel, that allows you to open two instances on the same workbook. Once you have two instances open, you can arrange these side by side and then compare these.

Suppose you have an Excel workbook that has two sheets for two different months (Jan and Feb) and you want to compare these side by side to see how the sales per store have changed:

![Two Sheets that have data that needs to compared side by side](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20672'%3E%3C/svg%3E)

Below are the steps to compare two sheets in Excel:

1.  Open the workbook that has the sheets that you want to compare.
2.  Click the View tab![Click the view tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20685%20199'%3E%3C/svg%3E)
3.  In the Window group, click on the ‘New Window’ option. This opens the second instance of the same workbook.
4.  In the ‘View’ tab, click on ‘Arrange All’. This will open the Arrange Windows dialog box![Click on Arrange all to decide how to align these workbooks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20155'%3E%3C/svg%3E)
5.  Select ‘Vertical’ to compare data in columns (or select Horizontal if you want to compare data in rows).![Click on Vertical and then click on Ok](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20255'%3E%3C/svg%3E)
6.  Click OK.

The above steps would arrange both the instances of the workbook vertically.

At this point in time, both the workbooks would have the same worksheet selected. In one of the workbooks, select the other sheet that you want to compare with the active sheet.

**How does this work?**

When you click on New Window, it opens the same workbook again with a slightly different name. For example, if your workbook name is ‘Test’ and you click on New Window, it will name the already open workbook ‘Test – 1’ and the second instance as ‘Test – 2’.

Note that these are still the same workbook. If you make any changes in any of these workbooks, it would be reflected in both.

And when you close any one instance of the open file, the name would revert back to the original.

You can also enable synchronous scrolling if you want (by clicking on the ‘Synchronous Scrolling’ option in the ‘View’ tab)

Compare Two Sheets and Highlight Differences (Using Conditional Formatting)
---------------------------------------------------------------------------

While you can use the above method to align the workbooks together and manually go through the data line by line, it’s not a good way in case you have a lot of data.

Also, doing this level of comparison manually can lead to a lot of errors.

So instead of doing this manually, you can use the power of Conditional Formatting to quickly highlight any differences in the two Excel sheets.

This method is really useful if you have two versions in two different sheets and you want to quickly check what has changed.

Note that you **CAN NOT** compare two sheets in different workbooks.

Since Conditional Formatting can not refer to an external Excel file, the sheets you need to compare needs to be in the same Excel workbook. In case these aren’t, you can copy a sheet from the other file to the active workbook and then make this comparison.

For this example, suppose you have a dataset as shown below for two months (Jan and Feb) in two different sheets and you want to quickly compare the data in these two sheets and check if the prices of these items have changed or not.

![Price data for items to be compared over month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20350'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the data in the sheet where you want to highlight the changes. Since I want to check how prices have changed from Jan to Feb, I have selected the data in the Feb sheet.
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20200'%3E%3C/svg%3E)
3.  In the Styles group, click on ‘Conditional Formatting’![Click on Conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20352%20159'%3E%3C/svg%3E)
4.  In the options that show up, click on ‘New Rule’![Click on new rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20302%20465'%3E%3C/svg%3E)
5.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’![Click on Use a formula to determine which cells to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)
6.  In the formula field, enter the following formula: **\=B2<>Jan!B2![Formula to compare data in two sheets in conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)**
7.  Click the Format button![Click on the Format button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)
8.  In the Format Cells dialog box that shows up, click on the ‘Fill tab’ and select the color in which you want to highlight the mismatched data.![Specify the format in which you want to get the differences in data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20548'%3E%3C/svg%3E)
9.  Click OK
10.  Click OK

The above steps would instantly highlight any changes in the dataset in both the sheets.

![Data where differences have been highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20348'%3E%3C/svg%3E)

**How does this work?**

[Conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 highlights a cell when the given formula for that cell returns a TRUE. In this example, we are comparing each cell in one sheet with the corresponding cell in the other sheet (done using the not equal to operator <> in the formula).

When conditional formatting finds any difference in the data, it highlights that in the Jan sheet (the one in which we have applied the conditional formatting.

Note that I have used [relative reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 in this example (A1 and not $A$1 or $A1 or A$1).

When using this method to compare two sheets in Excel, remember the following;

*   This method is good to quickly identify differences, but you can’t use it on an on-going basis. For example, if I enter a new row in any of the datasets (or [delete a row), it would give me incorrect results](https://trumpexcel.com/delete-rows/)
    . As soon as I insert/delete the row, all subsequent rows are considered as different and highlighted accordingly.
*   You can only compare two sheets in the same Excel file
*   You can only compare the value (not the difference in formula or formatting).

Compare Two Excel Files/Sheets And Get The Differences Using Formula
--------------------------------------------------------------------

If you’re only interested in quickly comparing and identifying the differences between two sheets, you can use a formula to fetch only those values that are different.

For this method, you will need to have a separate worksheet where you can fetch the differences.

This method would work if want to compare two separate Excel workbook or worksheets in the same workbook.

Let me show you an example where I am comparing two datasets in two sheets (in the same workbook).

Suppose you have the dataset as shown below in a sheet called Jan (and similar data in a sheet called Feb), and you want to know what values are different.

![Price data for items to be compared over month](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20350'%3E%3C/svg%3E)

To compare the two sheets, first, insert a new worksheet (let’s call this sheet ‘Difference’).

In cell A1, enter the following formula:

\=IF(Jan!A1<>Feb!A1,"Jan Value:"&Jan!A1&CHAR(10)&"Feb Value:"&Feb!A1,"")

![Difference Report to highight difference betwen sheets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20357%20311'%3E%3C/svg%3E)

Copy and paste this formula for a range so that it covers the entire dataset in both the sheets. Since I have a small dataset, I will only copy and paste this formula in A1:B10 range.

The above formula uses an [IF condition](https://trumpexcel.com/excel-if-function/)
 to check for differences. In case there is no difference in the values, it will return blank, and in case there is a difference, it will return the values from both the sheets in [separate lines in the same cell](https://trumpexcel.com/insert-line-break-in-excel/)
.

The good thing with this method is that it only gives you the differences and show you exactly what the difference is. In this example, I can easily see that the price in cell B4 and B8 are different (as well as the exact values in these cells).

Compare Two Excel Files/Sheets And Get The Differences Using VBA
----------------------------------------------------------------

If you need to compare Excel files or sheets quite often, it’s a good idea to have a ready Excel macro VBA code and use it whenever you need to make the comparison.

You can also add the macro to the Quick Access Toolbar so that you can access with a single button and instantly know what cells are different in different files/sheets.

Suppose you have two sheets Jan and Feb and you want to compare and highlight differences in the Jan sheet, you can use the below VBA code:

Sub CompareSheets()
Dim rngCell As Range
 
For Each rngCell In Worksheets("Jan").UsedRange

    If Not rngCell = Worksheets("Feb").Cells(rngCell.Row, rngCell.Column) Then
        rngCell.Interior.Color = vbYellow
    End If

Next rngCell

End Sub

The above code uses the [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through each cell in the Jan sheet (the entire used range) and compares it with the corresponding cell in the Feb sheet. In case it finds a difference (which is checked using the [If-Then statement](https://trumpexcel.com/if-then-else-vba/)
), it highlights those cells in yellow.

You can use this code in a regular module in the VB Editor.

And if you need to do this often, it’s better to save this code in the Personal Macro workbook and then add it to the Quick Access toolbar. In those ways, you will be able to do this comparison with a click of a button.

Here are the steps to [get the Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/#Where-Can-I-Find-the-Personal-Macro-Workbook)
 in Excel (it’s not available by default so you need to enable it).

Here are the steps to [save this code in the Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/#How-to-Copy-Macros-in-the-Personal-Macro-Workbook)
.

And [here you will find the steps](https://trumpexcel.com/change-negative-to-positive-in-excel/#Convert-Negative-Numbers-to-Postive-with-a-Single-Click-VBA)
 to add this macro code to the QAT.

Using a Third-Party Tool – XL Comparator
----------------------------------------

Another quick way to compare two Excel files and check for matches and differences is by using a free third-party tool such as XL Comparator.

This is a web-based tool where you can upload two Excel files and it will create a comparison file that will have the data that is common (or different data based on what option you selected.

Suppose you have two files that have customer datasets (such as name and email address), and you want to quickly check what customers are there is file 1 and not in file 2.

Below is how you compare two Excel files and create a comparison report:

1.  Open [https://www.xlcomparator.net/](https://www.xlcomparator.net/)
    
2.  Use the Choose file option to upload two files (maximum size of each file can be 5MB)
3.  Click on the Next button.
4.  Select the common column in both these files. The tool will use this common column to look for matches and differences
5.  Select one of the four options, whether you want to get matching data or different data (based on File 1 or File 2)
6.  Click on Next
7.  Download the comparison file which will have the data (based on what option you selected in step 5)

Below is a video that shows how XL Comparator tool works.

One concern you may have when using a third-party tool to compare Excel files is about privacy.

If you have confidential data and privacy is really important for it, it’s better to use other methods shown above.

Note that the XL Comparator website mentions that they delete all the files after 1 hour of doing the comparison.

These are some of the methods you can use to compare two different Excel files (or worksheets in the same Excel file). Hope you found this Excel tutorial useful.

**You may also like the following Excel tutorials:**

*   [How to Compare Two Columns in Excel (for matches & differences)](https://trumpexcel.com/compare-two-columns/)
    
*   [How to  Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
    
*   [How to Compare Text in Excel (Easy Formulas)](https://trumpexcel.com/compare-text-excel/)
    
*   [Split Each Excel Sheet Into Separate Files (Step-by-Step)](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/)
    
*   [Combine Data from Multiple Workbooks in Excel](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    
*   [Combine Data From Multiple Worksheets into a Single Worksheet in Excel](https://trumpexcel.com/combine-multiple-worksheets/)
    
*   [How to Compare Dates in Excel (Greater/Less Than, Mismatches)](https://trumpexcel.com/compare-dates-in-excel/)
    
*   [Compare Two Lists (Free Online Tool)](https://trumpexcel.com/tools/compare-two-lists/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Compare Two Excel Sheets (for differences)”
-----------------------------------------------------------------

1.  Thanks for this, very helpful. However, with 50 rows and 20 columns to compare, the e.g.JanValue20:FebValue16 is fine other than I then have to go back manually to the Feb sheet to see which product was in cell R45 that has changed values.
    
    [Reply](https://trumpexcel.com/compare-two-excel-sheets/#comment-14929)
    
2.  This macro is just what i have been looking for, thank you.  
    one thing though, if i would want to color whole rows instead of only cells.  
    is there a way to do that?
    
    Sub CompareSheets()  
    Dim rngCell As Range
    
    For Each rngCell In Worksheets(“Jan”).UsedRange
    
    If Not rngCell = Worksheets(“Feb”).Cells(rngCell.Row, rngCell.Column) Then  
    rngCell.Interior.Color = vbYellow  
    End If
    
    Next rngCell
    
    End Sub
    
    [Reply](https://trumpexcel.com/compare-two-excel-sheets/#comment-14696)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/compare-two-excel-sheets/#respond)

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
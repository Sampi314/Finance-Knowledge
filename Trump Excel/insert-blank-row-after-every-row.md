# Insert a Blank Row after Every Row in Excel (or Every Nth Row)

**Source:** https://trumpexcel.com/insert-blank-row-after-every-row

---

[Skip to content](https://trumpexcel.com/insert-blank-row-after-every-row/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/insert-blank-row-after-every-row/#below-title)

**Watch Video – Insert Blank Row After Every Row in Excel**

People who work with large data sets often need simple things such as inserting/deleting rows or columns.

While there are already many different (and simple) ways to add rows in Excel, when it comes to inserting a blank row after every other row (or every third or fourth row), things get a bit complicated.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/insert-blank-row-after-every-row/#)

Insert a Blank Row After Every Other Row
----------------------------------------

In this tutorial, I will show you some really simple ways to insert a blank row after every row in the existing dataset (or every nth row).

Since there is no direct way to add rows in between rows, the method covered in this article are workarounds to make this happen, And if you’re comfortable with VBA, then you can do this with a single click.

### Using Helper Column and the Sort Feature

Suppose you have a dataset as shown below and you want to insert a blank between the existing rows.

![Dataset where alternate blank rows need to be inserted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20612%20421'%3E%3C/svg%3E)

Below are the steps to insert blank rows between existing rows:

1.  Insert a blank column to the left of the dataset. To do this, right-click on the column header of the left-most column and click on Insert.![Insert a column to the left of the dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20612%20420'%3E%3C/svg%3E)
2.  Enter the text ‘HelperColumn’ in A1 (you can use any text you want)![Name the column HelperColumn](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20366'%3E%3C/svg%3E)
3.  Enter 1 in cell A2 and 2 in cell A3.![Enter 1 and 2 in first two cells of the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20717%20371'%3E%3C/svg%3E)
4.  Select both the cells and place the cursor at the bottom-right of the selection. When the cursor changes to a plus icon, double click on it. This will fill the entire column with [incrementing numbers![Autofill the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20380'%3E%3C/svg%3E)](https://trumpexcel.com/number-rows-in-excel/)
    
5.  Go to the last filled cell in the helper column and then select the cell below it.
6.  Enter 1 in this cell and 2 in the cell below it![Enter 1 and 2 in first cells below the dataset records](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20717%20455'%3E%3C/svg%3E)
7.  Select both the cells and place the cursor at the bottom-right of the selection.
8.  When the cursor changes to a plus icon, click and drag it down. This will fill a series of numbers (just as we got in step 3). Make sure you get more numbers than what you have in the dataset. For example, if there are 10 records in the dataset, make sure to get at least 10 cells filled in this step. Once, done, your dataset would look as shown below.![Helper column with serial numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20471%20440'%3E%3C/svg%3E)
9.  Select the entire dataset (including all the cells in the helper column).
10.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20197'%3E%3C/svg%3E)
11.  Click on the Sort option![Click the Sort icon in the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20201'%3E%3C/svg%3E)
12.  In the Sort dialog box, use the following settings:
    *   Sort by: Helper
    *   Sort on: Cell Value
    *   Order: Smallest to Largest![Sort Dialog Box settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
13.  Click OK. This will give you the dataset as shown below.![Final Dataset where blank rows have been inserted after each row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20555%20527'%3E%3C/svg%3E)
14.  Delete the helper column.

You would notice that as soon as you click OK in the Sort dialog box, it instantly rearranges the rows and now you have a blank row after every row of your dataset.

In reality, this is not really inserting a blank row. This sorting method is simply rearranging the data by placing blank rows from below the dataset in between the rows in the dataset.

You can also extend the same logic to **insert a blank row after every two rows or every three rows**.

Suppose you have the dataset as shown below and you want to get a blank row after every two rows.

Below are the steps to do this:

1.  Insert a blank column to the left of the dataset. To do this, right-click on the column header of the left-most column and click on Insert.
2.  Enter the text ‘HelperColumn’ in A1 (you can use any text you want)![Name the column HelperColumn](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20366'%3E%3C/svg%3E)
3.  Enter 1 in cell A2 and 2 in cell A3.
4.  Select both the cells and place the cursor at the bottom-right of the selection. When the cursor changes to a plus icon, double click on it. This will fill the entire column with incrementing numbers![Autofill the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20380'%3E%3C/svg%3E)
5.  Go to the last filled cell in the helper column and then select the cell below it.
6.  Enter 2 in this cell and 4 in the cell below it. We are using numbers in multiples of 2 as we want one blank row after every two rows.![Enter 2 and 4 in the cells below the data set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20397'%3E%3C/svg%3E)
7.  Select both the cells and place the cursor at the bottom-right of the selection.
8.  When the cursor changes to a plus icon, click and drag it down. This will fill a series of numbers (just as we got in step 3). Make sure you get a number bigger than what you have in the dataset. For example, if there are 10 records in the dataset, make sure you get at least till the number 10.![Enter a series of numbers in the helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20477'%3E%3C/svg%3E)
9.  Select the entire dataset (including all the cells in the helper column).
10.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20197'%3E%3C/svg%3E)
11.  Click on the Sort option![Click the Sort icon in the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20201'%3E%3C/svg%3E)
12.  In the Sort dialog box, use the following settings:
    *   Sort by: Helper
    *   Sort on: Cell Value
    *   Order: Smallest to Largest![Sort Dialog Box settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20336'%3E%3C/svg%3E)
13.  Click OK. This will give you the final data set as shown below (with a blank row after every second row of the dataset)
14.  Delete the helper column.

Similarly, in case you want to insert a blank row after every third row, use the number 3, 6, 9, and so on in Step 5.

### Using a Simple VBA Code

While you need a lot of workarounds to insert alternate blank rows in Excel, with VBA it’s all a piece of cake.

With a simple VBA code, all you need to do is select the dataset in which you want to insert a blank row after every row, and simply run the code (takes a single click).

Below is the VBA code that will insert a blank row after every row in the dataset:

Sub InsertAlternateRows()
'This code will insert a row after every row in the selection
'This code has been created by Sumit Bansal from trumpexcel.com
Dim rng As Range
Dim CountRow As Integer
Dim i As Integer
Set rng = Selection
CountRow = rng.EntireRow.Count

For i = 1 To CountRow
    ActiveCell.Offset(1, 0).EntireRow.Insert
    ActiveCell.Offset(2, 0).Select
Next i

End Sub

The above code counts the total number of rows in the selection and uses a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to cycle through each row and insert a blank row after each existing row in the dataset.

Here are the steps to place this VBA code in the [VB Editor in Excel](https://trumpexcel.com/visual-basic-editor/)
:

1.  Copy the above code
2.  Go to the Developer tab and click on the Visual Basic option. This will open the VB Editor. You can also use the keyboard shortcut **ALT + F11**
3.  In the VB Editor, right-click on any object in the Project Explorer
4.  Hover the cursor over the Insert option and then click on Module. This will insert a new module![Insert a module in the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20466'%3E%3C/svg%3E)
5.  In the Module code window, paste the above code.![Copy paste code in the Module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20428'%3E%3C/svg%3E)

Once you have the code in the VB Editor, you can now use this code to insert blank rows after every other row in the dataset.

Here are the steps to use the code to insert blank rows after every row:

1.  Select the entire dataset (except the header row)
2.  Click the Developer tab (in case you don’t have the Developer tab, [click here to learn how to get it](https://trumpexcel.com/excel-developer-tab/)
    )![Click the developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20761%20200'%3E%3C/svg%3E)
3.  Click on the ‘Macros’ option![Click on Visual Basic icon in the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20761%20200'%3E%3C/svg%3E)
4.  In the Macro dialog box, select the macro – ‘InsertAlternateRows’
5.  Click on Run![Run thhe Macro using the Macro dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20470'%3E%3C/svg%3E)

That’s it!

The above steps would instantly insert alternating blank rows in the dataset.

There are many different ways to run a macro in Excel. For example, if you have to do this quite often, you can add this macro to the Quick Access Toolbar so that you can run it with a single click.

You can read more about [different ways to run macros here](https://trumpexcel.com/run-a-macro-excel/)
.

In case you want to insert a blank row after every second row, you can use the below code:

Sub InsertBlankRowAfterEvery2ndRow()
'This code will insert a row after every second row in the selection
'This code has been created by Sumit Bansal from trumpexcel.com
Dim rng As Range
Dim CountRow As Integer
Dim i As Integer
Set rng = Selection
CountRow = rng.EntireRow.Count

For i = 1 To CountRow / 2
    ActiveCell.Offset(2, 0).EntireRow.Insert
    ActiveCell.Offset(3, 0).Select
Next i

End Sub

Hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [How to Delete Every Other Row in Excel (or Every Nth Row)](https://trumpexcel.com/delete-every-other-row-excel/)
    
*   [Highlight EVERY Other ROW in Excel (using Conditional Formatting)](https://trumpexcel.com/highlight-every-other-row-excel/)
    
*   [How to Select Every Third Row in Excel (or select every Nth Row)](https://trumpexcel.com/select-every-third-row/)
    
*   [Delete Blank Rows in Excel (with and without VBA)](https://trumpexcel.com/delete-blank-rows-excel/)
    
*   [How to Quickly Select Blank Cells in Excel](https://trumpexcel.com/select-blank-cells-in-excel/)
    
*   [Hide Zero Values in Excel | Make Cells Blank If the Value is 0](https://trumpexcel.com/hide-zero-values-excel/)
    
*   [Insert New Columns in Excel](https://trumpexcel.com/insert-columns-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Insert a Blank Row after Every Row in Excel (or Every Nth Row)”
------------------------------------------------------------------------------

1.  Crazy super helpful!!! Thank you so much!
    
    [Reply](https://trumpexcel.com/insert-blank-row-after-every-row/#comment-14498)
    
2.  This is super helpful, thank you so much 🙂
    
    There is a very minor error in one of the screenshots.  
    “3. Click on the ‘Macros’ option” instruction, whereas “Visual Basic” is highlighted.
    
    Not a problem at all , but in case you wanted to fix it . Thanks again!
    
    [Reply](https://trumpexcel.com/insert-blank-row-after-every-row/#comment-14321)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/insert-blank-row-after-every-row/#respond)

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
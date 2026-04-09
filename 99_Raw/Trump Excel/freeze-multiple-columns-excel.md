# How to Freeze Multiple Columns in Excel? 4 Easy Ways!

**Source:** https://trumpexcel.com/freeze-multiple-columns-excel

---

[Skip to content](https://trumpexcel.com/freeze-multiple-columns-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/freeze-multiple-columns-excel/#below-title)

As you scroll horizontally across a worksheet with many columns, the columns at the beginning of the worksheet scroll out of view.

Usually, the first column (or the first few columns) has the headers for each row.

And when you scroll to the right of your worksheet, it would be helpful if the headers in the column were visible.

When they are visible all the time, you do not have to keep scrolling back to see what the values further across the worksheet mean. This saves effort and time.

This is where the ability to freeze columns comes in handy. This tutorial shows you four methods of **how to freeze multiple columns in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/freeze-multiple-columns-excel/#)

Method #1: Freeze Multiple Columns Using the Freeze Panes Option
----------------------------------------------------------------

The following example dataset extends to column V and is not fully viewable on a single screen.

![dataset in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201277%20335'%3E%3C/svg%3E)

If we scroll to the right towards the last column of the dataset, the columns at the beginning of the worksheet move out of view.  

We want to change Excel’s default behavior such that as we scroll the worksheet to the right, the columns A, B, and C remain visible.

Below are the steps to freeze multiple columns using the Freeze Pane option in the ribbon:

1.  Select column D, which is immediately on the right of columns A, B, and C.

![Select column D](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201280%20354'%3E%3C/svg%3E)

2.  Click the **View** tab, in the **Window** group, open the **Freeze Panes** option and click **Freeze Panes**.  

![Click on the Freeze Panes option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20565%20207'%3E%3C/svg%3E)

3.  Click anywhere in the worksheet to deselect column D.

Notice the grey vertical line running down the worksheet on the right border of column D. This indicates that all the columns on the left of the line are frozen. 

![gray line appears after the frozen columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201280%20412'%3E%3C/svg%3E)

You can now scroll the worksheet to the furthest extent to the right, and columns A, B, and C will remain visible.

![scrolling to far off columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20919%20357'%3E%3C/svg%3E)

In the above screenshot, you can see that I have scrolled to the right, and I have columns T, U, and V visible, while columns A, B, and C have been frozen and remain visible all the time.

### Unfreeze the Columns

In case you want to unfreeze the columns, open the **View** tab, open the **Freeze Panes** options in the **Window** group, and click **Unfreeze Panes**.

![Click on Unfreeze columns option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20567%20207'%3E%3C/svg%3E)

Method #2: Keyboard Shortcut to Freeze Multiple Columns
-------------------------------------------------------

Below is the keyboard shortcut to freeze multiple columns in Excel:

**ALT + W + F + F**

Below I have a large dataset that is not viewable on a single screen, and I will have to scroll to the right if I want to view data in far-off columns.

![large data set in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201277%20335'%3E%3C/svg%3E)

And as soon as I scroll to the right, the columns at the beginning of the worksheet are out of my view.  

Here are the steps to use the keyboard shortcut to freeze the first three columns:

1.  Select any cell in column D.
2.  Press and release the following keyboard keys one after the other: **Alt + W + F + F**.

The first three columns are frozen.

![first three columns are frozen](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201280%20358'%3E%3C/svg%3E)

**Note:** To unfreeze the columns, use the same shortcut **Alt + W + F + F** again. It will unfreeze any row or columns that have been freezed

Method #3: Freeze Multiple Columns Using VBA
--------------------------------------------

We can use Excel VBA to freeze multiple columns in Excel

Below is a dataset where I want to freeze the first three columns

![large data set in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201277%20335'%3E%3C/svg%3E)

Here is the VBA code to freeze the first three columns

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub FreezeFirstThreeColumns()
        Columns("D:D").Select
        ActiveWindow.FreezePanes = True
    End Sub

Below are the steps to use the above VBA code in your workbook:

1.  Click the tab of the worksheet containing the dataset to activate the worksheet.
2.  Open the **Developer** tab and click the **Visual Basic** button in the **Code** group.

![click on visual basic icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20125'%3E%3C/svg%3E)

3.  In the **Visual Basic Editor,** open the **Insert** menu and choose the **Module** item.

![Click on Insert Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20289%20169'%3E%3C/svg%3E)

4.  Copy the above VBA code and paste it in the Macro code window
5.  Save the sub-procedure and save the workbook as a **Macro-Enabled Workbook**.
6.  Place the cursor anywhere in the procedure and press **F5** to run the code. 
7.  Click the **View Microsoft Excel** button on the toolbar to switch to the active worksheet.

![Click the View Microsoft Excel button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20233%20132'%3E%3C/svg%3E)

Notice that column D is selected. Click anywhere in the worksheet to deselect the column. The first three columns of the worksheet are frozen.

![first three columns are frozen](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201280%20358'%3E%3C/svg%3E)

In the above code, I wanted to freeze the first three columns, so I used _Columns(“D:D”).Select_ in my code. In case you want to freeze the first two columns, you can use _Columns(“C:C”).Select_

You can also modify the above code to freeze one to multiple rows as well (or both rows and columns)

In case you want to freeze multiple columns in all the worksheets in your workbook, you can use the below code:

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub FreezeColumnsinAllSheets()
    For Each ws In Worksheets
        ws.Activate
        Columns("D:D").Select
        ActiveWindow.FreezePanes = True
    Next ws
    End Sub

**Note**: VBA method to freeze rows or columns in Excel is suitable only when you have to do this quite often. For example, if you want to freeze columns in multiple worksheets for all the worksheets in your workbook, then the VBA method would be helpful. But if you want to do this in one or two worksheets only, then you are better off using the keyboard shortcut or the Freeze Panes options in the ribbon.

Method #4: Keep Multiple Columns Visible Using the Split Option
---------------------------------------------------------------

Let me show you an innovative way to lock the rows or columns in their place while you can scroll and look at data that’s far off in your worksheet.

Excel’s **Split** option allows us to divide the window into different panes that scroll separately.

We can then scroll the worksheet in the second pane, and the columns we want to remain visible will remain visible in the first pane. 

Below is a dataset that extends till column V, and I want to have the first three columns always visible on the screen when I scroll to the right. 

![Dataset in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201277%20335'%3E%3C/svg%3E)

In this case, we can split the Excel screen into two panes, where the first pane has the columns I want to freeze in its place, while the second pane can be used to scroll the data

Below are the steps to do this:

1.  Select column D.

![select column D](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201280%20354'%3E%3C/svg%3E)

2.  Click the **View** tab and click the **Split** command in the Window group. The Split button becomes dark grey indicating that it is active. 

![Click on the Split icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20597%20124'%3E%3C/svg%3E)

3.  Click anywhere in the worksheet to deselect column D.

Notice the grey split line between the two panes:

![grey split line between panes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201280%20411'%3E%3C/svg%3E)

The worksheet has been split into two panes after column C, and each pane has its own scroll area.

![scroll bars in each pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201078%20398'%3E%3C/svg%3E)

You can scroll the worksheet in the second pane to the last column of the dataset, as columns A, B, and C remains visible in the first pane.

![far off columns become visible](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20797%20339'%3E%3C/svg%3E)

### To remove the split

If you want to remove the split, click on the Split button to deactivate it.

The split line is removed from the worksheet, and the two panes collapse into one. The Split button becomes transparent, indicating that it is inactive. 

In this tutorial, we have learned how to freeze columns to keep them visible while we scroll to another area of the worksheet.

This way, we do not have to keep scrolling back to the row headers to see what a value means.  This saves a lot of time and effort. 

This tutorial has shown four techniques for freezing multiple columns in Excel. The techniques involve using the Freeze Panes command, the Split command, the keyboard shortcut, and Excel VBA. 

**Other Excel articles you may also like:**

*   [Excel Freeze Panes: Use it to Lock Row/Column Headers](https://trumpexcel.com/excel-freeze-panes/)
    
*   [How to Zoom-in and Zoom-Out in Excel (Shortcuts)](https://trumpexcel.com/zoom-in-zoom-out-excel-shortcuts/)
    
*   [How to Lock Row Height & Column Width in Excel](https://trumpexcel.com/lock-row-height-column-width-excel/)
    
*   [Excel AUTOFIT: Make Rows/Columns Fit the Text Automatically](https://trumpexcel.com/autofit-excel/)
    
*   [5 Ways to Insert New Columns in Excel (including Shortcut & VBA)](https://trumpexcel.com/insert-columns-in-excel/)
    
*   [How to Group Columns in Excel?](https://trumpexcel.com/group-columns-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/freeze-multiple-columns-excel/#respond)

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
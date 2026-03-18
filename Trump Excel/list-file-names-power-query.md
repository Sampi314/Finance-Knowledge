# Get a List of File Names from Folders & Sub-folders (using Power Query)

**Source:** https://trumpexcel.com/list-file-names-power-query

---

[Skip to content](https://trumpexcel.com/list-file-names-power-query/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/list-file-names-power-query/#below-title)

**Watch Video – Get a List of File Names from Folders & Sub-folders**

Some time ago I wrote an Excel Tutorial about [getting a list of file names from a folder](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
 in Excel.

In that tutorial, I showed various ways to get the list of file names from a folder (using the FILE function and VBA).

However, the limitation of that method is that it can only get the file names from a folder, and not from the sub-folders within the main folder.

But you can do this using [Power Query](https://trumpexcel.com/power-query-course/)
 (‘Get & Transform’ if you’re using Excel 2016 or later versions).

Where to find Power Query
-------------------------

If you’re using Excel 2016, you don’t need to do anything extra. You will find all the [Power Query options](https://trumpexcel.com/power-query/)
 in the **Get & Transform** category in the Data tab.

![Power query - Get & Transform in Excel in Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20130'%3E%3C/svg%3E)

Note that Power Query and Get & Transform refer to the same thing.

For Excel 2010/2013, you need to install the Power Query add-in to use it (steps described below).

1.  [Click here to download the Power Query add-in](https://www.microsoft.com/en-in/download/details.aspx?id=39379)
    . Make sure you are downloading 32-bit if your Excel is 32-bit and 64 bit if your Excel is 64 bit.
2.  Install the Power Query add-in.
3.  Open Excel. If you see a Power Query tab, skip the remaining steps. If not, move to the next step.
4.  Go to File and click on Options.
5.  In the ‘Excel Options’ dialog box, click on Add-in in the left pane.
6.  From the Manage drop-down, select COM Add-ins, and click on Go.
7.  In the list of available add-ins, select Power Query and click OK.
8.  Close the Excel Application and restart Excel.

The above steps would install and activate the Power Query for your Excel.

Get a List of File Names from Folders & Sub-folders
---------------------------------------------------

Since I am using Excel 2016, all the snapshots and written steps are for Excel 2016. You can use the same for Excel 2010 and 2013 as well.

Now let’s see how to get a list of all the files names from a folder and sub-folders within it.

Here are the steps to get a list of all the file names from a folder:

1.  Go to the Data tab.![Get File names from folder - data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20418%20134'%3E%3C/svg%3E)
2.  In the Get & Transform group, click on New Query.![Get File names from folder - new query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20418%20134'%3E%3C/svg%3E)
3.  Hover the cursor on the ‘From File’ option and click on ‘From Folder’.![Get File names from folder - from folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20393%20482'%3E%3C/svg%3E)
4.  In the Folder dialog box, enter the folder path, or use the browse button to locate it.![Folder location in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20215'%3E%3C/svg%3E)
5.  Click OK.
6.  In the dialog box that opens, you’ll see the names of all the files along with other metadata.![Get File names from folder - data in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20875%20695'%3E%3C/svg%3E)
7.  Click on the Load button.![Get File names from folder - data in Power Query load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20875%20695'%3E%3C/svg%3E)

The above steps would load all the data about the files in your Excel worksheet.

![Get a list of File names from folder - file name in column A](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20146'%3E%3C/svg%3E)

Once you have the data in Excel, you can edit it if needed.

With the data that I have in Excel, I can do the following:

*   Filter the file0 names based on extension (file type) –  it’s in column B.
*   Filter the file names based on the folder name – it’s in column F.

Editing the Columns Data in Power Query
---------------------------------------

Before loading your data into Excel, you can also edit the data in Power Query.

For example, you can delete some columns or get some more metadata for each file.

Here are the steps to get additional metadata columns in Power Query editor:

1.  Go to the Data tab.
2.  In the Get & Transform group, click on New Query.
3.  Hover the cursor on the ‘From File’ option and click on ‘From Folder’.![Get File names from folder - from folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20393%20482'%3E%3C/svg%3E)
4.  In the Folder dialog box, enter the folder path, or use the browse button to locate it.![Folder location in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20215'%3E%3C/svg%3E)
5.  Click OK.
6.  In the dialog box that opens, click on ‘Edit’.![Load data in Get & Transform - Power Query Edit Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20875%20695'%3E%3C/svg%3E)
7.  In the Power Query editor, click on the expand icon in the ‘Attributes’ column. It will show you a list of the additional columns you can get for the files (such as file size or read-only or hidden). Select the columns that you want to have in the data (and uncheck the rest).![Power query - Get & Transform click on attribute](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20384'%3E%3C/svg%3E)
8.  Click OK.
9.  Click on ‘Load’.

This will load the data in the Excel with the selected additional columns.

You can also delete columns if you don’t need it. To do this, in the Power Query editor, select the column you want to delete, right-click, and click on Remove.

![Remove column in Power Query Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20583%20347'%3E%3C/svg%3E)

**You May Also Like the Following Excel Tutorials:**

*   [Get a List of All the Comments in a Worksheet in Excel](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/)
    .
*   [How to Combine Multiple Excel Files into One Excel Workbook](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
    .
*   [How to Combine Data from Multiple Workbooks into One Excel Table (using Power Query)](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    .
*   [Combine Data From Multiple Worksheets into a Single Worksheet in Excel.](https://trumpexcel.com/combine-multiple-worksheets/)
    
*   [Merge Tables in Excel Using Power Query.](https://trumpexcel.com/merge-tables/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

11 thoughts on “Get a List of File Names from Folders & Sub-folders (using Power Query)”
----------------------------------------------------------------------------------------

1.  It’s possible to get the file’s name from the subfolders using FSO as well, you just need to know how to implement inheritance
    
    Elton Senne
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-14387)
    
2.  Amazing, saved a lot of a time. Thanks for sharing the info.
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-12219)
    
3.  if I have files in folder and subfolder more the 100,000 file how it will work
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-11753)
    
4.  THANK YOU SIR, YOU DID GREAT JOB THANKS A LOT
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-11632)
    
5.  Great tutorial. If I have other metadata like “tags”, “author” on files, how can show add those columns?
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-11384)
    
6.  Really useful, thank you
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-10629)
    
7.  Really it is a good site for excel learning .
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-10097)
    
8.  Thank you Sumit. Very good tip using Power Query.
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-9990)
    
9.  Can we get power query in excel 2007?
    
    [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-9983)
    
    *   Unfortunately, Power Query is not available for Excel 2007
        
        [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-9984)
        
        *   Thanks.
            
            [Reply](https://trumpexcel.com/list-file-names-power-query/#comment-9986)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/list-file-names-power-query/#respond)

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
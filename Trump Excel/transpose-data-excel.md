# How to Transpose Data in Excel (Step-by-Step Guide)

**Source:** https://trumpexcel.com/transpose-data-excel

---

[Skip to content](https://trumpexcel.com/transpose-data-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/transpose-data-excel/#below-title)

**Watch Video – How to Transpose Data in Excel**

If you have a dataset and you want to transpose it in Excel (which means converting rows into columns and [columns into rows](https://trumpexcel.com/convert-columns-to-rows-excel/)
), doing it manually is a complete NO!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/transpose-data-excel/#)

Transpose Data using Paste Special
----------------------------------

[Paste Special](https://trumpexcel.com/excel-paste-special-shortcuts/)
 can do a lot of amazing things, and one such thing is to transpose data in Excel.

Suppose you have a dataset as shown below:

![Transpose Data in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20408%20153'%3E%3C/svg%3E)

This data has the regions in a column and quarters in a row.

Now for some reason, if you need to transpose this data, here is how you can do this using paste special:

*   Select the data set (in this case A1:E5).
*   Copy the dataset (Control + C) or right-click and select copy.![Transpose Data in Excel - Copy](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20197'%3E%3C/svg%3E)
*   Now you can paste the transposed data in a new location. In this example, I want to copy in G1:K5, so right-click on cell G1 and select paste special.![Transpose Data in Excel - Paste Special G1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20211'%3E%3C/svg%3E)
*   In the paste special dialogue box, check the transpose option in the bottom right.![Check the Transpose option in Paste Special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20338'%3E%3C/svg%3E)
*   Click OK.

This would instantly copy and paste the data but in such a way that it has been transposed. Below is a demo showing the entire process.

The steps shown above copies the value, the formula (if any), as well as the format. If you only want to copy the value, select ‘value’ in the paste special dialog box.

Note that the copied data is static, and if you make any changes in the original data set, those changes would not be reflected in the transposed data.

If you want these transposed cells to be linked to the original cells, you can combine the power of [Find & Replace](https://trumpexcel.com/find-and-replace-in-excel/)
 with Paste Special.

Also read: How [to Move Columns in Excel](https://trumpexcel.com/move-rows-columns/)

Transpose Data using Paste Special and Find & Replace
-----------------------------------------------------

Using Paste Special alone gives you static data. This means that if your original data changes and you want the transposed data to be updated as well, then you need to use Paste Special again to transpose it.

Here is a cool trick you can use to transpose the data and still have it linked with the original cells.

Suppose you have a dataset as shown below:

![Transpose Data in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20408%20153'%3E%3C/svg%3E)

Here are the steps to transpose the data but keep the links intact:

*   Select the data set (A1:E5).
*   Copy it (Control + C, or right-click and select copy).![Transpose Data in Excel - copy data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20628%20188'%3E%3C/svg%3E)
*   Now you can paste the transposed data in a new location. In this example, I want to copy in G1:K5, so right-click on cell G1 and select paste special.![Transpose Data in Excel - Paste Special G1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20211'%3E%3C/svg%3E)
*   In the Paste Special dialog box, click on the Paste Link button. This will give you the same data set, but here the cells are linked to the original data set (for example G1 is linked to A1, and G2 is linked to A2, and so on).![Transpose Data in Excel - paste link](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20339'%3E%3C/svg%3E)
*   With this new copied data selected, Press Control + H (or go to Home –> Editing –> Find & Select –> Replace). This will open the Find & Replace dialog box.![Transpose Data in Excel - Find & Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20206%20198'%3E%3C/svg%3E)
*   In the Find & Replace dialog box, use the following:
    *   In Find what: =
    *   In Replace with: !@# (note that I am using !@# as it’s a unique combination of characters that is unlikely to be a part of your data. You can use any such unique set of characters).![Transpose Data in Excel - replace dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20200'%3E%3C/svg%3E)
*   Click on Replace All. This will replace the equal to from the formula and you will have !@# followed by the cell reference in each cell.![Transpose Data in Excel - replaced data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20374%20161'%3E%3C/svg%3E)
*   Right-click and copy the data set (or use Control + C).![Transpose Data in Excel - copy replaced data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20186'%3E%3C/svg%3E)
*   Select a new location, right-click and select paste special. In this example, I am pasting it in cell G7. You can paste it anywhere you want.![Transpose Data in Excel - paste special replaced data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20276'%3E%3C/svg%3E)
*   In the Paste Special dialog box, select Transpose and click OK.![Transpose Data in Excel - transpose replaced data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20337'%3E%3C/svg%3E)
*   Copy paste this newly created transposed data to the one from which it is created.![Transpose Data in Excel - copying transposed data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20418%20288'%3E%3C/svg%3E)
*   Now open the Find and Replace dialog box again and replace !@# with =.![Transpose Data in Excel - find replace again](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20201'%3E%3C/svg%3E)

This will give you a linked data that has been transposed. If you make any changes in the original data set, the transposed data would automatically update.

![Transpose Data in Excel - Linked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20732%20136'%3E%3C/svg%3E)

Note: Since our original data has A1 as empty, you would need to manually delete the 0 in G1. The 0 appears when we paste links, as a link to an empty cell would still return a 0. Also, you’d need to format the new dataset (you can simply copy paste the format only from the original dataset).

Also read: [Combine Two Cells in Excel](https://trumpexcel.com/combine-cells-in-excel/)

Transpose Data using Excel TRANSPOSE Function
---------------------------------------------

Excel TRANSPOSE function – as the name suggests – can be used to transpose data in Excel.

Suppose you have a dataset as shown below:

![Transpose Data in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20408%20153'%3E%3C/svg%3E)

Here are the steps to transpose it:

*   Select the cells where you want to transpose the dataset. Note that you need to select the exact number of cells as the original data. So for example, if you have 2 rows and 3 columns, you need to select 3 rows and 2 columns of cells where you want the transposed data. In this case, since there are 5 rows and 5 columns, you need to select 5 rows and 5 columns.![Transpose Data in Excel - select cells transpose function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20857%20148'%3E%3C/svg%3E)
*   Enter =TRANSPOSE(A1:E5) in the active cell (which should be the top left cell of the selection and press Control Shift Enter.

This would transpose the dataset.

![Transpose Data in Excel - transpose function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20803%20181'%3E%3C/svg%3E)

Here are a few things you need to know about the TRANSPOSE function:

*   It is an array function, so you need to use Control-Shift-Enter and not just Enter.
*   You can not delete a part of the result. You need to delete the entire array of values that the TRANSPOSE function returns.
*   Transpose function only copies the values, not the formatting.

Also read: [Transpose Multiple Rows into One Column](https://trumpexcel.com/transpose-multiple-rows-into-one-column/)

Transpose Data Using Power Query
--------------------------------

Power Query is a powerful tool that enables you to quickly transpose data in Excel.

Power Query is a part of [Excel 2016](https://support.office.com/en-us/article/Get-Transform-in-Excel-2016-881c63c6-37c5-4ca2-b616-59e18d75b4de?ui=en-US&rs=en-US&ad=US)
 (Get & Transform in the Data tab) but if you’re using [Excel 2013 or 2010](https://support.office.com/en-us/article/Introduction-to-Microsoft-Power-Query-for-Excel-6e92e2f4-2079-4e1f-bad5-89f6269cd605?ui=en-US&rs=en-US&ad=US&fromAR=1)
, then you need to install it as an add-in.

Suppose you have the data set as shown below:

![Transpose Data in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20408%20153'%3E%3C/svg%3E)

Here are the steps to transpose this data using Power Query:

### In Excel 2016

*   Select the data and go to Data –> Get & Transform –> From Table.![Transpose Data in Excel - from table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20126'%3E%3C/svg%3E)
*   In the Create Table dialogue box, make sure the range is correct and click OK. This will open the Query Editor dialog box.![Transpose Data in Excel - power query ok](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20236%20156'%3E%3C/svg%3E)
*   In the Query editor dialog box, select the ‘Transform’ tab.![Transpose Data in Excel - transform](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20301%20183'%3E%3C/svg%3E)
*   In the Transform tab, go to Table –> Use First Row as Headers –> Use Headers as First Row. This ensures that the first row (that contains headers: Q1, Q2, Q3, and Q4) are also treated as data and transposed.![Transpose Data in Excel - power query header1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20273'%3E%3C/svg%3E)
*   Click on Transpose. This would instantly transpose the data.![Transpose Data in Excel - power query transpose](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20295'%3E%3C/svg%3E)
*   Click on Use First Row as Headers. This would now make the first row of the transposed data as headers.![Click on Use First Row as Headers Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20295'%3E%3C/svg%3E)
*   Go to File –> Close and Load. This will close the Power Editor window and create a new sheet that contains the transposed data.![Click in close and load in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20634%20348'%3E%3C/svg%3E)

Note that since the top left cell of our data set was empty, it gets a generic name Column1 (as shown below). You can delete this cell from the transposed data.

![Power query result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20450'%3E%3C/svg%3E)

### In Excel 2013/2010

In Excel 2013/10, you need to install Power Query as an add-in.

[Click here](https://www.microsoft.com/en-in/download/details.aspx?id=39379)
 to download the plugin and get installation instructions.

Once you have installed Power Query, go to Power Query –> Excel Data –> From Table.

![Get Data from Table using Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20122'%3E%3C/svg%3E)

This will open the create table dialog box. Now follow the same steps as shown for Excel 2016.

**You May Also Like the Following Excel Tutorials:**

*   [Multiply in Excel using Paste Special](https://trumpexcel.com/multiply-in-excel-using-paste-special/)
    .
*   [CONCATENATE Excel Range (with and without separator).](https://trumpexcel.com/concatenate-excel-ranges/)
    
*   [Clean Data in Excel Spreadsheets.](https://trumpexcel.com/clean-data-in-excel/)
    
*   [Compare Columns in Excel](https://trumpexcel.com/compare-two-columns/)
    
*   [Excel Text to Columns](https://trumpexcel.com/excel-text-to-columns-examples/)
    
*   [Excel TRIM Function](https://trumpexcel.com/excel-trim-function/)
    
*   [Merge Tables in Excel](https://trumpexcel.com/merge-tables/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Transpose Data in Excel”
----------------------------------------------

1.  Sumit, Your technical knowledge and clear, logical thinking alone are impressive. But then you inject a dose of lateral thinking – as with the method to transpose links in this article – and that is really inspiring. Thank you.
    
    [Reply](https://trumpexcel.com/transpose-data-excel/#comment-3578)
    
2.  Thanks for the PowerQuery method Sumit. PowerQuery is the big thing these days! My traditional method has been the Transpose array.  
    Cheers,  
    Kevin
    
    [Reply](https://trumpexcel.com/transpose-data-excel/#comment-3490)
    
    *   Thanks for commenting Kevin.. Power Query is super and I am trying my hands on it
        
        [Reply](https://trumpexcel.com/transpose-data-excel/#comment-3493)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/transpose-data-excel/#respond)

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
# How to Print the Top Row on Every Page in Excel (Repeat Row/Column Headers)

**Source:** https://trumpexcel.com/print-top-row-on-every-page-excel

---

[Skip to content](https://trumpexcel.com/print-top-row-on-every-page-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/print-top-row-on-every-page-excel/#below-title)

When you work with data in Excel, there is a handy feature that allows you to [freeze the top row and header columns](https://trumpexcel.com/excel-freeze-panes/)
 (or even lock multiple top rows or left columns).

So when you scroll down, the headers are always visible.

But that’s not the case when you print your reports.

By default, a printed report would only have the header row at the top of the first printed page, and then rest all the other pages won’t have it.

This can make going through the reports a nightmare. Imagine being on the third page and not knowing what a data point represents (and the back and forth to check the headers can be maddening).

The solution – have the headers repeat on every printed page of the report.

In this tutorial, I will show you **how to print the top row on every page in Excel**. You can also configure it so that multiple top rows or left columns repeat on every page.

Let’s see how to do this!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/print-top-row-on-every-page-excel/#)

How to Print the Top Row on Every Page in Excel
-----------------------------------------------

Suppose you have a dataset as shown below.

![Dataset to print and have top row repeat](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20773'%3E%3C/svg%3E)

If you print this data, it would take up multiple pages, but the heading will only appear on the first page.

Below are the steps to make sure that the header row repeats on every page that is printed:

1.  Click the ‘Page Layout’ tab![Click the page layout tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20557%20191'%3E%3C/svg%3E)
2.  In the ‘Page Setup’ group, click on the dialog box launcher (the small tilted arrow as shown below)![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20207'%3E%3C/svg%3E)
3.  In the ‘Page Setup’ dialog box, click on the ‘Sheet’ tab![Click on the Sheet tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20522'%3E%3C/svg%3E)
4.  Click on the field next to the ‘Rows to repeat at top’ option![Click on the rows to repeat at the top field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20705%20613'%3E%3C/svg%3E)
5.  Select the top row (you will notice that $1:$1 is automatically inserted in the “Rows to repeat at the top” field.![Row reference get entered in the field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20705%20613'%3E%3C/svg%3E)
6.  Click OK.

Now, when you print this data, you will notice that the top row header repeats on every page that is printed.

You can check this by Clicking on the ‘File’ tab and then clicking on the ‘Print’ option. This will open the Print Preview pane.

![Click on Print option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20547'%3E%3C/svg%3E)

Click on the arrow icons at the bottom of the Print preview pane, and you should see the headers repeat on each of the pages.

![Click to change page number in print preview](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20418'%3E%3C/svg%3E)

Just like we have configured the settings to print the top row on every page, you can also set it to print multiple header rows on every page.

To do this, in Step 5 of the above steps, instead of selecting the top row, select multiple top rows that you want to repeat on every printed page.

Note that you need to select contiguous rows (i.e., you can set row number 1, 2, and 3 to be printed on every page, but you cannot set row number 1 and 3 to be repeated on every printed page)

You can also set the left-most column (or multiple left-most columns) to repeat on every page when printed. The process is exactly the same, where, in Step 5, instead of choosing the row, you can select the column that you want to repeat.

And of course, you can also set the top row and the top column to repeat on every printed page.

Also read: [Freeze Columns In Excel](https://trumpexcel.com/freeze-multiple-columns-excel/)

Print the Rows on Every Page Using the NameBox Trick
----------------------------------------------------

Now, let me also share an amazing [Excel trick](https://trumpexcel.com/24-excel-tricks/)
 that not many people know about.

The benefit of using the above method (where we use the Page Setup dialog box) is that it gives you a lot more options when you’re printing your reports.

But if all you want to do is make sure that the top through or the leftmost column repeats on every printed page, this NameBox trick is a lot faster.

Suppose you have a dataset as shown below.

![Dataset to print and have top row repeat](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20773'%3E%3C/svg%3E)

Below are the steps to make sure the headers in printed on every page

1.  Select the header row![Select the header row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20463'%3E%3C/svg%3E)
2.  Click on the ‘NameBox’ field![Click on the Namebox](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20350'%3E%3C/svg%3E)
3.  Manually enter the text **Print\_Titles![Enter Print_Titles in the name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20663%20362'%3E%3C/svg%3E)**
4.  Hit the enter key

That’s it! Now when you print the dataset, the first row would repeat on every page.

In case you want to repeat multiple header rows or columns, select those first and then name these as **Print\_Titles**

**Why this Works?**

When you use the Page Setup dialog box to set the rows and columns that should be repeated, Excel automatically creates a [Named Range](https://trumpexcel.com/named-ranges-in-excel/)
 with the name Print\_Titles.

So, instead of going the Page Setup dialog box route, if you create the same Named Range yourself, that would work too.

Also read: [Add Sheet Name to Header](https://trumpexcel.com/add-sheet-name-to-header-footer-excel/)

How to Repeat Header Rows on Every Page Except the Last Few Pages?
------------------------------------------------------------------

Unfortunately, there is no way in-built way to make sure that the headers print on every page except the last page (or the last few pages).

One workaround could be to have the pages, where you do not want the headers to repeat, so be in a separate worksheet.

But this may not be ideal for everyone.

Below is the [VBA macro code](https://trumpexcel.com/excel-macro-examples/)
 that will do this.

Sub RepeatHeadersPrintExceptLastPage()

Dim TotalPages As Long

TotalPages = Application.ExecuteExcel4Macro("GET.DOCUMENT(50)")

With ActiveSheet.PageSetup
.PrintTitleRows = "$1:$1"

ActiveSheet.PrintOut From:=1, To:=TotalPages - 1
.PrintTitleRows = ""

ActiveSheet.PrintOut From:=TotalPages, To:=TotalPages

End With
End Sub

The above code uses _Application.ExecuteExcel4Macro(“GET.DOCUMENT(50)”)_ to get the total number of pages in the dataset that will be printed.

It then prints all the pages (except the last one), and during this time, the PrintTitleRows is set to $1:$1. So the first row will be printed as a header on all pages except the last one.

Then the last page is printed where the PrintTitleRows property is set to null, so no header rows are printed on the last page.

This is a clumsy workaround, but if all you want to do is print all the data in the worksheet so that the header repeats on every page except the last page, this would work.

You might have to modify the code a little bit in case you want more headers to repeat or also want the column headers to be printed on each page.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [How to Print Excel Sheet on One Page (Fit to One Page)](https://trumpexcel.com/print-excel-sheet-one-page/)
    
*   [How to Print Multiple Sheets (or All Sheets) in Excel in One Go](https://trumpexcel.com/print-multiple-sheets-excel/)
    
*   [How to Print Comments in Excel (Step-by-Step Guide)](https://trumpexcel.com/print-comments-excel/)
    
*   [How to Set the Print Area in Excel Worksheets](https://trumpexcel.com/how-to-set-the-print-area-in-excel/)
    
*   [How to Change Page Orientation in Excel?](https://trumpexcel.com/change-page-orientation-excel/)
    
*   [Repeat Rows N Times in Excel](https://trumpexcel.com/repeat-rows-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/print-top-row-on-every-page-excel/#respond)

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
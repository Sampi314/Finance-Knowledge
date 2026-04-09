# How to Print Multiple Sheets (or All Sheets) in Excel in One Go

**Source:** https://trumpexcel.com/print-multiple-sheets-excel

---

[Skip to content](https://trumpexcel.com/print-multiple-sheets-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/print-multiple-sheets-excel/#below-title)

Excel gives you a lot of options when you’re trying to print your work. You can choose to print the entire worksheet, a specific area in the worksheet, print multiple sheets, or all sheets at one go.

In this tutorial, I will show you how you can **print multiple sheets in Excel** at one go. These could be some selected sheets or all the sheets in the workbook.

And in case you want to print a specific area in multiple/all sheets, you can do that too with a little bit of VBA magic.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/print-multiple-sheets-excel/#)

Print All Sheets at One Go
--------------------------

Excel has an inbuilt feature that allows you to specify to print all the sheets at one go.

Below are the steps to print all the sheets in the workbook:

1.  Click the File tab![Click File tab in Excel ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20200'%3E%3C/svg%3E)
2.  Click on the Print option![Click the Print Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20356%20531'%3E%3C/svg%3E)
3.  In the Print page, click on the Print setting drop-down![Click on print settings option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20559'%3E%3C/svg%3E)
4.  Click on Print Entire Workbook![Click on Print entire workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20711'%3E%3C/svg%3E)
5.  Click on Print![Click on Print](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20397'%3E%3C/svg%3E)

The above steps would print all the sheets in the workbook. In case you have a [print area set](https://trumpexcel.com/how-to-set-the-print-area-in-excel/)
 in some of the sheets, then only that print area will be printed.

You can also see what will be printed in the Print preview on the right. You can also change page numbers and see what will be printed on each page.

Easy enough!

Now, what if you only want to print only some specific sheets and not the entire workbook.

Read on!

Print Multiple Sheets (Selected Ones) at One Go
-----------------------------------------------

This is again quite easy to achieve.

All you need to do is selected those specific sheets that you want to print and then print it!

Below are the steps to print some specific sheets in a workbook in Excel:

1.  Select all the sheets that you want to print. To do this, hold the Control key and select sheets one by one. In this example, I am selecting Sheet 1, 4 and 5![Select the sheets that you want to print](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20107'%3E%3C/svg%3E)
2.  Click the File tab
3.  Click on the Print option
4.  In the Print page, click on the Print setting drop-down
5.  Click on Print Active Sheets (in most cases, it’s already the default option, but in case it isn’t you can choose that from the drop-down)![Click on Print Active Sheets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20708'%3E%3C/svg%3E)
6.  Click on Print

When you select multiple sheets, these all act as active sheets while printing.

You can also see what will be printed in the Print preview on the right. You can also change page numbers and see what will be printed on each page.

Also read: [Add Sheet Name to Header or Footer in Excel](https://trumpexcel.com/add-sheet-name-to-header-footer-excel/)

Print Multiple Sheets With a Specific Print Area
------------------------------------------------

This one is a little more complex than the previous two.

Suppose you have a workbook with multiple sheets, and you want to print a specific area from each sheet.

Maybe there is summary data in each sheet and you only want to print this data and not the entire worksheet.

This can be done by setting a print area in all the sheets and then printing these (as shown in the above two methods).

Now when it comes to setting the print area:

*   You need to do it manually for each sheet (especially if the print area is different for each sheet)
*   Or you can use a simple VBA code to set the same print area in all the sheets at one go.

Once you have set the print area, you can then use any of the above methods to print the sheets.

So let me quickly show you how to set the Print area manually and using VBA.

### Setting the Print Area manually

Below are the steps to do this:

1.  Select the cells that you want to be covered in the print area
2.  Click the ‘Page Layout’ tab![Click on the Page Layout tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20193'%3E%3C/svg%3E)
3.  In the Page Setup group, click on ‘Print Area’![Click on Print Area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20623%20193'%3E%3C/svg%3E)
4.  Click on ‘Set Print Area’![Click on Set Print area option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20257'%3E%3C/svg%3E)

That’s it!

This would set the print area to the selected cells and when you print this sheet, only the print area will be printed.

You need to do this manually for each sheet. So if you want to print specific areas in Sheet1, Sheet4, and Sheet5, you will have to do it for each sheet separately.

### Setting the Print Area using VBA

In case you have a lot of worksheets, setting the print area manually can be time-consuming.

In that case, you can also use [VBA](https://trumpexcel.com/excel-vba/)
 to quickly set the print area in one sheet, and then run the code to replicate it to all the other sheets.

Note: This method works well when you have the same range of cells that you want to use while setting the Print Area.

Below is the VBA macro code that will do this:

Sub SetPrintAreas1()
    Dim PrntArea As String
    Dim ws As Worksheet
    PrntArea = ActiveSheet.PageSetup.PrintArea
    For Each ws In Worksheets
        ws.PageSetup.PrintArea = PrntArea
    Next
    Set wks = Nothing
End Sub

The above code uses the print area from the active sheets, goes to all the sheets in the workbook and **sets the same print area** in each of these sheets.

It uses a loop to go through each worksheet and then set the same area in each worksheet as the print area. In case you want this to be different for each sheet, I believe doing it manually would be faster.

Once you have this set, you can now print all the sheets (or some selected sheets), and only the print area will be printed.

You can put this VBA macro code in a regular module and [run it from there](https://trumpexcel.com/run-a-macro-excel/)
.

So these are some scenarios where you can print multiple sheets in Excel in one go.

Hope you found this tutorial useful!

**You may also like the following Excel tutorials:**

*   [How to Print Comments in Excel](https://trumpexcel.com/print-comments-excel/)
    
*   [How to Print Excel Sheet on One Page](https://trumpexcel.com/print-excel-sheet-one-page/)
    
*   [How to Insert Page Numbers in Excel Worksheets](https://trumpexcel.com/how-to-insert-page-numbers-in-excel/)
    
*   [How to Compare Two Excel Sheets (for differences)](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [How to Unhide Sheets in Excel (All In One Go)](https://trumpexcel.com/unhide-sheets-excel/)
    
*   [How to Print the Top Row on Every Page in Excel](https://trumpexcel.com/print-top-row-on-every-page-excel/)
    
*   [How to Change Page Orientation in Excel?](https://trumpexcel.com/change-page-orientation-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Print Multiple Sheets (or All Sheets) in Excel in One Go”
------------------------------------------------------------------------------

1.  I’m sure it is because I’m new to VBA, but I’ll ask a stupid question. Don’t you have to designate a range of cells to set a print area in each worksheet? If that’s what you are trying to accomplish.
    
    [Reply](https://trumpexcel.com/print-multiple-sheets-excel/#comment-14297)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/print-multiple-sheets-excel/#respond)

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
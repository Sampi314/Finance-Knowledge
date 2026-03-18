# How to Set the Print Area in Excel Worksheets

**Source:** https://trumpexcel.com/how-to-set-the-print-area-in-excel

---

[Skip to content](https://trumpexcel.com/how-to-set-the-print-area-in-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/how-to-set-the-print-area-in-excel/#below-title)

 **Watch Video – How to Set the Print Area in Excel**

If you need to print your work in Excel, this tip would save you some papers. Using this, you can set the print area in Excel worksheets, so that only that part of the worksheet is printed.

This technique could be useful if you want to print only a part of a report or there is a section of the report that you need to print often.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/how-to-set-the-print-area-in-excel/#)

Print Area in Excel Worksheets
------------------------------

A print area is a range of cells (contiguous or non-contiguous) that you designate to print whenever you print that worksheet. For example, instead of printing the entire worksheet, if I only want to print the first 10 rows, I can set the first 10 rows as the print area.

In this tutorial, you’ll learn:

*   How to Set the Print Area in Excel Worksheets.
*   How to Modify the Print Area in Excel.
*   How to Clear the Print Area in Excel.

### How to Set the Print Area in Excel Worksheets

Here are the steps to set the print area in Excel:

*   Select the range of cells that you want to set as the print area in that Excel worksheet.
*   Go to Page Layout –> Page Setup –> Print Area –> Set Print Area.
    *   This would set the selected cells as the print area. It also creates a [named range](https://trumpexcel.com/named-ranges-in-excel/)
         for the selected area (the name Print\_Area would be visible in the Name Box).![Set the Print Area in Excel Worksheets - Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20258%20161'%3E%3C/svg%3E)

Now when you print this worksheet, only the set print area would be printed.

Here are some important things to know when you set the print area in Excel worksheets.

*   There can be multiple print areas in a worksheet, however, these are printed separately. To selected multiple areas, hold the Control Key and make the selection using the mouse.
*   A print area specified using the above steps is specific to that worksheet only. Hence, you can set different print areas in different worksheets.
*   When you save the workbook, Excel saves the print area as well. The next time you open the workbook, the print area would still be there.
*   When you set a print area in different worksheets, a named range Print\_Area is created for each worksheet.

### How to Modify the Print Area in Excel

If you want to add cells to the existing print area:

*   Select the cells that you want to add.
*   Go to Page Layout –> Page Setup –> Print Area –> Add Print Area.
    *   Note that the option to Add Print Area would be visible only when you have an existing print area in the Excel worksheet.![Set the Print Area in Excel Worksheets - Add](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20182'%3E%3C/svg%3E)

This would modify the print area and include the new cells.

Here are a few things you need to know while modifying print area in Excel:

*   If the new print area is not adjacent to the existing print area, Excel would create a new print area and print it separately in a different page. However, if it is adjacent to the existing print area, it would be merged and printed in the same sheet.
*   When you add additional cells to the print area, the named range Print\_Area changes. You can directly edit the named range to modify the print area.

###  How to Clear the Print Area in Excel

Here are the steps to clear the print area:

*   Click anywhere in the worksheet from which you want to clear the print areas.
*   Go to Page Layout –> Page Setup –> Print Area –> Clear Print Area.![Set the Print Area in Excel Worksheets - Clear](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20248%20180'%3E%3C/svg%3E)

This will clear all the print areas (in case you have set more than one range of cells).

In case, you only want to remove some cells and not clear the entire print area, edit the name range from the name manager.

**You May Also Like the Following Excel Tutorials:**

*   [How to Insert Page Numbers in Excel Worksheets](https://trumpexcel.com/how-to-insert-page-numbers-in-excel/)
    .
*   [How to Print Excel Sheet on One Page](https://trumpexcel.com/print-excel-sheet-one-page/)
    
*   [How to Print Comments in Excel](https://trumpexcel.com/print-comments-excel/)
    .
*   [How to Print Multiple Sheets (or All Sheets) in Excel in One Go](https://trumpexcel.com/print-multiple-sheets-excel/)
    
*   [How to Print the Top Row on Every Page in Excel](https://trumpexcel.com/print-top-row-on-every-page-excel/)
    
*   [Add Sheet Name to Header in Excel](https://trumpexcel.com/add-sheet-name-to-header-footer-excel/)
    
*   [How to Insert Page Breaks in Excel (& Remove, Delete Page Breaks)](https://trumpexcel.com/insert-page-breaks-excel/)
    
*   [How to Show Ruler in Excel?](https://trumpexcel.com/ruler-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Set the Print Area in Excel Worksheets”
-------------------------------------------------------------

1.  What’s about selecting print area if you are on iPad?
    
    [Reply](https://trumpexcel.com/how-to-set-the-print-area-in-excel/#comment-12148)
    
2.  Hello Sumit,
    
    Thanks for the great videos. I have been watching your videos for a while and I really learned a lot from your tutorials.
    
    I have been a Linux user since 2007 and even before switching to Linux, I had been using LibreOffice (OpenOffice previously). In Libre, we can set a different page style for each sheet in a workbook. I mean we can set different margins and page layouts independently for each sheet. Can we do this in Excel ?
    
    Secondly, I was working with a price list in an xlsx file at work. And I was trying to publish the entire workbook into PDF. While trying to set the print area, although I choose width of the page should be as wide as the active columns in the sheet, when I look at the Print Preview, still it was scaling and shrinking to the left of the page. In other words, although I choose that page width should be from column A to M, let’s say, it sets the print are accordingly, however, it scales down the page instead of spreading to the width of the page. Interestingly, it worked for some sheets but not for some although all page details were the same. Finally, I opened the file in Libreoffice and chose fit the sheet into several pages, 5 or 6 let’s say, and it automatically fixed the problem.
    
    So, what should I have done with Excel to fix the problem ?
    
    Thanks for your help in advance.
    
    [Reply](https://trumpexcel.com/how-to-set-the-print-area-in-excel/#comment-7154)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/how-to-set-the-print-area-in-excel/#respond)

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
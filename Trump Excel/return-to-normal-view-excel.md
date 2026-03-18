# Return to Normal View in Excel (3 Easy Ways)

**Source:** https://trumpexcel.com/return-to-normal-view-excel

---

[Skip to content](https://trumpexcel.com/return-to-normal-view-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/return-to-normal-view-excel/#below-title)

Excel has three types of worksheet views:

*   Normal View
*   Page Break Preview, and
*   Page Layout View

In most cases, you will be working with the Normal view.

If for some reason, your worksheet looks weird, it’s possible that the view setting is changed and you need to return to the Normal view.

In this article, I will show you three simple ways to return to Normal view in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/return-to-normal-view-excel/#)

Method 1 – Using the View Tab in the Ribbon
-------------------------------------------

Below are the steps to return to Normal view in Excel using the option in the ribbon:

1.  Click the _View_ tab in the ribbon.

![Click on the view tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20222'%3E%3C/svg%3E)

2.  In the _Workbook Views_ group, click on the _Normal_ view icon.

![Click on the normal view icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20535%20222'%3E%3C/svg%3E)

That’s it! This would change the worksheet view to Normal.

_When you change the view settings of any of the worksheets, it is only applied to that worksheet. It’s not applied to any of the other worksheets. If you want to apply it to all the sheets, you need to do it one by one, or use the VBA code I cover later in this article._

Method 2 – Using a Keyboard Shortcut
------------------------------------

If this is something you need to do often, here is a simple keyboard shortcut to apply the Normal view to the worksheet.

ALT + W + L 

To use the above shortcut, press and release the Alt key, then press the W  
key and then the L key.

Method 3 – Using Icons in the Status Bar
----------------------------------------

Another easy way to return the worksheet to the Normal view is to click on the Normal view icon in the status bar.

In the [status bar](https://trumpexcel.com/status-bar-excel/)
, you will see the three worksheet view icons next to the zoom slider.

![Three page layout icons in the status bar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%2085'%3E%3C/svg%3E)

You can click on any of the icons to apply that view settings. So if you want to return to the Normal view, click on the _Normal_ icon (as shown below).

![Click on normal view icon in the status bar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%2079'%3E%3C/svg%3E)

When you return to the normal view, you will see a dotted line in the worksheet. This is a page-break line that indicates where a page will break when printed (i.e., part on the other side of the line will be printed in a different page). If you want to [remove this dotted line](https://trumpexcel.com/remove-dotted-lines-excel/#Removing-the-Page-Break-Dotted-Lines)
, close and reopen the file again.

Method 4 – VBA to Return All Sheets to Normal View
--------------------------------------------------

As I mentioned, when you change the view setting of a worksheet, it’s only applied to that specific worksheet.

If you want to apply the Normal view setting to all the worksheets in your file, you can use the below VBA code.

    Sub ReturnNormalView()
        Dim ws As Worksheet
        
        For Each ws In ThisWorkbook.Worksheets
            ws.Activate
            ActiveWindow.View = xlNormalView
        Next ws
        
        'Return to first worksheet
        ThisWorkbook.Worksheets(1).Activate
    End Sub

The above VBA code loops through each worksheet in the current workbook and changes the view to normal.

Normal View vs Page Layout View vs Page Break Preview
-----------------------------------------------------

In case you’re curious about the difference between the three workbook view settings in Excel, below is a table that explains it.

| Feature | Normal View | Page Layout View | Page Break Preview |
| --- | --- | --- | --- |
| Purpose | Day-to-day data entry and formula work | See how sheets will look when printed | Adjust page breaks and [print areas](https://trumpexcel.com/how-to-set-the-print-area-in-excel/) |
| Shows Margins | No  | Yes | No  |
| Shows Headers/Footers | No  | Yes | No  |
| Shows Page Breaks | Dotted lines | Solid lines | Blue dashed lines |
| [Shows Rulers](https://trumpexcel.com/ruler-excel/) | No  | Yes | No  |
| Grid Lines | Visible | Optional | Visible |
| Best Used For | [Data entry](https://trumpexcel.com/excel-data-entry-tips/)<br>, formula creation, general editing, charts, [pivot table](https://trumpexcel.com/creating-excel-pivot-table/) | Final formatting, adding headers/footer, adjusting margins, preparing for printing | Managing print areas, adjusting page breaks |

In this article, I showed you how to return to the Normal view in Excel using four different methods.

I hope you found this article helpful.

**Other Excel articles you may also like:**

*   [How to Insert Page Breaks in Excel (& Remove, Delete Page Breaks)](https://trumpexcel.com/insert-page-breaks-excel/)
    
*   [How to Print Excel Sheet on One Page (Fit to One Page)](https://trumpexcel.com/print-excel-sheet-one-page/)
    
*   [How to Make Cells Bigger in Excel?](https://trumpexcel.com/make-cells-bigger-excel/)
    
*   [Enable Dark Mode in Microsoft Excel](https://trumpexcel.com/dark-mode-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/return-to-normal-view-excel/#respond)

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
# Printing multiple pages with different layouts using Excel

**Source:** https://chandoo.org/wp/hui%e2%80%99s-excel-report-printer

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Hui’s Excel Report Printer
==========================

*   Last updated on September 14, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Over a decade ago I was working on a very large and complex budget model, come to think of it I still am?

It involved 4 linked Excel workbooks, about 30 worksheets, all different, and multiple views of each worksheet.

There were regular Worksheets and Chart Sheets interspersed throughout.

Some of the Ranges had Outlined/Grouped Totals that were indented on some reports, but not on others depending on whom the various reports were going to.

It was a great budget model until you had to print a copy of it.

And of course the different levels of Managers all want different reports etc, etc.

The Solution
------------

To solve this I developed a simple VBA routine which has evolved over the years to what is presented here.

[![](https://chandoo.org/wp/wp-content/uploads/2011/09/MainPrintScreen.png "MainPrintScreen")](https://chandoo.org/wp/wp-content/uploads/2011/09/MainPrintScreen.png)

The basic idea is to add a Printing Control sheet to your workbook.

This sheet has a list of print views, not Excel views, of various pages within the current workbook.

Each page can be setup as you wish and allows for a number of common parameters for each printed page.

Pages can be listed, multiple times if required, with different ranges or outlining selected each time

The Code handles Worksheets and Chartsheets, Normal and Named Ranges, Page Orientation, Page Size, Page Grouping and Headers/Footers.

As a user you setup the sheets as a list in the order you want them, with appropriate parameters.

The code then:

*   Loops through the list,
*   Obtain the parameters,
*   Sets up the print page and
*   Prints it.

You just need to sit back and wait for the printer to jam.

**HOW DO I USE IT**
-------------------

Download the sample file here [Excel 97-03](https://chandoo.org/wp/wp-content/uploads/2011/09/Print-Areas.xls "Print Areas 97/03")
, [Excel 2007/10](https://chandoo.org/wp/wp-content/uploads/2011/09/Print-Areas.xlsm "Print Areas 07/10")

You can use the sample file as is, for demo purposes or read on later where I describe how to use this in your workbooks.

Open the workbook and Goto the “Print\_Control” worksheet.

[![](https://chandoo.org/wp/wp-content/uploads/2011/09/MainPrintScreen.png "MainPrintScreen")](https://chandoo.org/wp/wp-content/uploads/2011/09/MainPrintScreen.png)

Browse through the various Headings in Row 4 and field values below them.

Note that some of the Row 4 cells have comments in which explain what options are available.

Each field is described below:

### **No.**

The Row No. in the list of page layouts available.

This has no use except when someone says the 5th page should be…

### **Description/Header**

A text field that is used as a Reminder of the layout of the Page Setup also serves as a Centred Header.

### **Status**

Print = **On**

Don’t Print = **Off**

The code only prints the pages marked as On.

### **Sheet**

The name of the Worksheet or Chartsheet you want to print

### **Area**

The Range on the Sheet that you want printed

Ignored for Chartsheets.

### **Land/Port**

Specify if the page should be printed Landscape or Portrait

Ignored for Chartsheets.

Chartsheets are printed in Landscape.

### **Pages Wide**

How many pages wide should the Range be printed on

This is fixed at 1 for Chartsheets.

### **Pages Tall**

How many pages tall should the Range be printed out on

This is fixed at 1 for Chartsheets.

### **Copies**

How Many Copies do you want of that individual page.

### **Rows & Columns**

If outline/grouping is used specify what level of Indentation should be used for the Rows and Columns.

0 – Leave as is

1 – Indent 1 level

8  – Indent 8 levels

The maximum indentation is 8

Ignored for Chartsheets.

### **Footer (Left)**

A description field printed as lower left footer.

### **No. of Copies**

This specifies the Number of Copies of the Whole Report you want

**Print All “On” Areas  
**
---------------------------

The **Print All “On” Areas** Button executes the code and prints out a number of copies of the report as specified in the various page setups.

[![](https://chandoo.org/wp/wp-content/uploads/2011/09/PrintOnArea.png "PrintOnArea")](https://chandoo.org/wp/wp-content/uploads/2011/09/PrintOnArea.png)

The printing is done on the default printer on your PC,

**Important: Ensure that the printer you want to use for the job is set as the default before you start Excel.**

[![](https://chandoo.org/wp/wp-content/uploads/2011/09/Default-Printer.png "Default Printer")](https://chandoo.org/wp/wp-content/uploads/2011/09/Default-Printer.png)

You can print to a PDF file by specifying your Adobe or other PDF Printer as the Default Printer.

I’m sorry, This doesn’t fix the printing multiple pages to multiple files when printing to PDF issue.

**Warning !** I maybe old school but I still recommend saving before printing !

**HELP**
--------

There is limited help built into the system, That’s what this Post is doing.

Some of the field headings have comments which show what values are acceptable in those fields.

[![](https://chandoo.org/wp/wp-content/uploads/2011/09/PrintHelp.png "PrintHelp")](https://chandoo.org/wp/wp-content/uploads/2011/09/PrintHelp.png)

**HOW DO I ADD THIS TO MY WORKBOOK ?  
**
-----------------------------------------

To add this to your workbook, copy the **Print\_Control** worksheet to your workbook

1.  Open your workbook.
2.  Open the Demo File
3.  Copy the **Print\_Control** worksheet by Right Clicking on the **Print\_Control** tab, and copy to your workbook.
4.  Run the VBA Code using the “**Setup Print Control Named Formula**” Button

[![](https://chandoo.org/wp/wp-content/uploads/2011/09/Named-Formula.png "Named Formula")](https://chandoo.org/wp/wp-content/uploads/2011/09/Named-Formula.png)

That’s it.

All the code required for the printing is part of the Print\_Control page.

**HOW DOES THE VBA WORK ?**
---------------------------

The following describes the VBA Code driving this worksheet.

To examine this goto VBA (Alt F11)

Select the workbook and double click on Sheet0 (Print\_Control)

The code should appear in the right hand window

If you are unfamiliar with VBA it may be worth going through Chandoo’s [Crash Course in VBA](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/ "Crash Course in VBA")

There are 2 Subroutines and a Function in this system which are documented below

### **Print\_Reports**

This is the main subroutine that drives the printing

It is called by the Print All On Button and when finished returns the user to the Print\_Control worksheet.

All the VBA code is in _RED_,

Comments and notes are in BLACK before the line or section they refer to.

\= = = = = = = = = = = = = = = = = = =

At the start of the Print\_Reports subroutine, setup variables for later use

_Option Explicit_

_Public Sub Print\_Reports()_

_Dim PrintArea As Variant_

_Dim i As Integer_

_Dim j As Integer_

_Dim sht As Long_

_Dim Orientation As String_

_Dim NCopies As Integer_

_Dim PWide As Integer_

_Dim PTall As Integer_

_Dim Footer As String_

_Dim Header As String_

_Dim Sheets As String_

_Dim gRow As Integer_

_Dim gCol As Integer_

_Dim PaperSize As String_

_Dim msg As String_

_Dim tmp As String_

Turn off the Automatic Calculation so that it is faster and isn’t as jerky

_Application.Calculation = xlCalculationManual_

This loads the entire array of the Print\_Control page into an array called PrintArea

_PrintArea = Worksheets(“Print\_Control”).Range(“Print\_Control”).Value_

This sets up a loop for the No of Total Copies of the Whole report

_For j = 1 To \[Copies\].Value_ ‘Loop through the No of Copies

This sets up a loop for the to check each line of the Print Control area

_For i = 1 To UBound(PrintArea, 1)_ ‘Loop through the print area

If the Column Status is On print using that line of settings

_If UCase(PrintArea(i, 3)) = “ON” Then_ ‘When On is enabled Print using the settings

Extract the settings from the stored array, row i

_Header = PrintArea(i, 2)_ ‘Set Header variable

_Orientation = PrintArea(i, 6)_ ‘Set Orientation variable

_PWide = PrintArea(i, 8 )_ ‘Set Pages Wide variable

_PTall = PrintArea(i, 9)_ ‘Set Pages Tall variable

_NCopies = PrintArea(i, 10)_ ‘Set No Copies variable

_gRow = PrintArea(i, 11)_ ‘Set Row Group Expansion

_gCol = PrintArea(i, 12)_ ‘Set Column Group Expansion

_Footer = PrintArea(i, 13)_ ‘Set Footer variable

Check paper sizes against the built in page sizes

_If PrintArea(i, 7) = “A4” Then_

_PaperSize = 9_

_ElseIf PrintArea(i, 7) = “A3” Then_

_PaperSize = 8_

_ElseIf PrintArea(i, 7) = “A5” Then_

_PaperSize = 11_

_ElseIf PrintArea(i, 7) = “Legal” Then_

_PaperSize = 5_

_ElseIf PrintArea(i, 7) = “Letter” Then_

_PaperSize = 1_

_ElseIf PrintArea(i, 7) = “Quarto” Then_

_PaperSize = 15_

_ElseIf PrintArea(i, 7) = “Executive” Then_

_PaperSize = 7_

_ElseIf PrintArea(i, 7) = “B4” Then_

_PaperSize = 12_

_ElseIf PrintArea(i, 7) = “B5” Then_

_PaperSize = 13_

_ElseIf PrintArea(i, 7) = “10×14” Then_

_PaperSize = 16_

_ElseIf PrintArea(i, 7) = “11×17” Then_

_PaperSize = 17_

_ElseIf PrintArea(i, 7) = “Csheet” Then_

_PaperSize = 24_

_ElseIf PrintArea(i, 7) = “Dsheet” Then_

_PaperSize = 25_

_Else_

_PaperSize = 9_ ‘Defaults to A4

_End If_

Activate the relevant sheet

This checks that the sheet exists first

_tmp = PrintArea(i, 4)_

_SheetExists(tmp) is a UDF that’s checks if the sheet exists and returns True or False_

_If Not SheetExists(tmp) Then_

_msg = “Sheet ‘” + PrintArea(i, 4) + “‘ not found.” + vbCrLf + “Check the sheets Name.”_

_msg = msg + vbCrLf + vbCrLf + “Processing will continue for remaining sheets.”_

_tmp = MsgBox(msg, vbExclamation, “Sheet not Found”)_

_Else_

The sheet exists now process

Select the sheet

_Application.Sheets(PrintArea(i, 4)).Select_

Check if it is a Worksheet or a Chartsheet

_If ActiveSheet.Type = -4167 Then_ ‘Its a worksheet

Turn off screen updating

_Application.ScreenUpdating = False_

Select the relevnt area of the sheet

_ActiveSheet.PageSetup.PrintArea = PrintArea(i, 5)_ ‘Select the relevent Print Area of the Sheet

Set Outline levels

_ActiveSheet.Outline.ShowLevels RowLevels:=gRow, ColumnLevels:=gCol_ ‘Set Outline Grouping

Apply print settings

_With ActiveSheet.PageSetup_ ‘Set print settings

_.PrintTitleRows = “”_

_.PrintTitleColumns = “”_

_.LeftHeader = “”_

_.CenterHeader = Header_ ‘User Defined Header (Shift to Left or Right as required)

_.RightHeader = “”_

_.LeftFooter = Footer_ ‘User Defined Footer (Shift to Left or Right as required)

_.CenterFooter = “”_

_.RightFooter = “”_

_.LeftMargin = Application.InchesToPoints(0.1)_

_.RightMargin = Application.InchesToPoints(0.1)_

_.TopMargin = Application.InchesToPoints(1.0)_

_.BottomMargin = Application.InchesToPoints(0.4)_

_.HeaderMargin = Application.InchesToPoints(0.1)_

_.FooterMargin = Application.InchesToPoints(0.3)_

_.PrintHeadings = False_

_.PrintGridlines = False_

_.PrintComments = xlPrintNoComments_

_.CenterHorizontally = False_

_.CenterVertically = False_

_.Draft = False_

_.PaperSize = PaperSize_ ‘ User Defined Paper Size

_.FirstPageNumber = xlAutomatic_

_.Order = xlDownThenOver_

_.BlackAndWhite = False_

_.Zoom = False_

_.FitToPagesWide = PWide_ ‘User Defined No Pages Wide

_.FitToPagesTall = PTall_ ‘User Defined No Pages Tall

_.PrintErrors = xlPrintErrorsDisplayed_

_End With_

Apply page orientation settings

_If Orientation = “L” Then_ ‘User Defined Page Orientation

_ActiveSheet.PageSetup.Orientation = xlLandscape_

_Else_

_ActiveSheet.PageSetup.Orientation = xlPortrait_

_End If_

Turn Screen updating back on

_Application.ScreenUpdating = True_

Finished setting up Worksheet goto the Printing area

_Else_ ‘Its a Chart page

Turn Screen updating off

_Application.ScreenUpdating = False_

Apply print settings

_With ActiveChart.PageSetup_

_.LeftHeader = “”_

_.CenterHeader = Header_

_.RightHeader = “”_

_.LeftFooter = Footer_

_.CenterFooter = “”_

_.RightFooter = “”_

_.LeftMargin = Application.InchesToPoints(0.1)_

_.RightMargin = Application.InchesToPoints(0.1)_

_.TopMargin = Application.InchesToPoints(1#)_

_.BottomMargin = Application.InchesToPoints(0.4)_

_.HeaderMargin = Application.InchesToPoints(0.1)_

_.FooterMargin = Application.InchesToPoints(0.3)_

_.ChartSize = xlScreenSize_

_.PrintQuality = 600_ ‘Change to 300 for Excel 97-03

_.CenterHorizontally = True_

_.CenterVertically = True_

_.Orientation = xlLandscape_

_.Draft = False_

_.OddAndEvenPagesHeaderFooter = False_ ‘Removed from 97/03 Ver

_.DifferentFirstPageHeaderFooter = False_ ‘Removed from 97/03 Ver

_.EvenPage.LeftHeader.Text = “”_ ‘Removed from 97/03 Ver

_.EvenPage.CenterHeader.Text = “”_ ‘Removed from 97/03 Ver

_.EvenPage.RightHeader.Text = “”_ ‘Removed from 97/03 Ver

_.EvenPage.LeftFooter.Text = “”_ ‘Removed from 97/03 Ver

_.EvenPage.CenterFooter.Text = “”_ ‘Removed from 97/03 Ver

_.EvenPage.RightFooter.Text = “”_ ‘Removed from 97/03 Ver

_.FirstPage.LeftHeader.Text = “”_ ‘Removed from 97/03 Ver

_.FirstPage.CenterHeader.Text = “”_ ‘Removed from 97/03 Ver

_.FirstPage.RightHeader.Text = “”_ ‘Removed from 97/03 Ver

_.FirstPage.LeftFooter.Text = “”_ ‘Removed from 97/03 Ver

_.FirstPage.CenterFooter.Text = “”_ ‘Removed from 97/03 Ver

_.FirstPage.RightFooter.Text = “”_ ‘Removed from 97/03 Ver

_.PaperSize = PaperSize_

_.FirstPageNumber = xlAutomatic_

_.BlackAndWhite = False_

_.Zoom = 100_

_End With_

Turn Screen Updating back on

_Application.ScreenUpdating = True_

_End If_

Now Print the active sheet using user defined No. Copies

_ActiveWindow.SelectedSheets.PrintOut Copies:=NCopies, Collate:=True_

_End If_

_End If_

_Next i_

_Next j_

Clear PrintArea array, just in case

_PrintArea = Null_

Turn Auto Calculation back on

_Application.Calculation = xlCalculationAutomatic_

Go back to the Print Control sheet

_Application.Sheets(“Print\_Control”).Select_

_End Sub_

\= = = = = = = = = = = = = = = = = = =

### **The SheetExists Function**

This is a Function that is used by the Print\_Reports subroutine to check if a sheet exists.

\= = = = = = = = = = = = = = = = = = =

_Function SheetExists(SheetName As String) As Boolean_

‘ This function Returns TRUE if the sheet exists in the active workbook

_SheetExists = False ‘_Set default value of SheetExists

_On Error GoTo NoSuchSheet ‘_Set error trapping such that if the sheet doesn’t exist it will exit

Check length of sheet name, if the sheet exists it will return a value, otherwise an error

_If Len(Sheets(SheetName).Name) > 0 Then_

The sheet exists so set SheetExists = True and exit

_SheetExists = True_

_Exit Function_

_End If_

_NoSuchSheet:_

The sheet doesn’t exists so use default SheetExists = False and exit

_End Function_

\= = = = = = = = = = = = = = = = = = =

### **The Setup\_Print\_Control\_Named\_Formula Subroutine**

This is a simple subroutine that sets up the 2 named formula for use the first time a sheet is used.

\= = = = = = = = = = = = = = = = = = =

_Sub Setup\_Print\_Control\_Named\_Formula()_

Setup Named Formula “Print\_Control” which is the table of settings

_ActiveWorkbook.Names.Add Name:=”Print\_Control”, RefersToR1C1:= \__

_“=OFFSET(Print\_Control!R4C2,1,,COUNTA(Print\_Control!R5C2:R24C2),COUNTA(Print\_Control!R4))”_

_ActiveWorkbook.Names(“Print\_Control”).Comment = \__

_“Used by the Print\_Reports Subroutine”_

Setup Named Formula “Copies” which is the No of Copies of the Whole Report

_ActiveWorkbook.Names.Add Name:=”Copies”, RefersToR1C1:= \__

_“=Print\_Control!R26C13”_

_ActiveWorkbook.Names(“Copies”).Comment = “Specifies the No. of Copies for the Print\_Reports Subroutine”_

_End Sub_

\= = = = = = = = = = = = = = = = = = =

**NAMED FORMULA**
-----------------

The code relies on two Named Formulas

### **Copies:**

**\=Print\_Control!$L$27**

### **Print\_Control:**

**\=OFFSET(Print\_Control!$B$4,1,,COUNTA(Print\_Control!$B$5:$B$24),COUNTA(Print\_Control!$4:$4))**

Automatically adjusts the Print\_Control Named Formula for the number of Page Setup lines and Fields to be processed

If you have queries about how any of the above code works, please let me know in the comments below:

**WHAT DOES THE ARRAY “PrintArea” DO ?**
----------------------------------------

The print area array stores the values of the Print\_Control range in a 2 dimensional array which represents the Print\_Control range.

This is done for a few reasons, but simply it is faster as it results in less reading of the worksheet

It also allows more flexibility in the subsequent processing as all the data is in one area.

**DOWNLOADS**
-------------

Download the sample file here [Excel 97-03](https://chandoo.org/wp/wp-content/uploads/2011/09/Print-Areas.xls "Print Areas 97/03")
, [Excel 2007/10](https://chandoo.org/wp/wp-content/uploads/2011/09/Print-Areas.xlsm "Print Areas 07/10")

**WHAT’S NEXT**
---------------

There are a number of parameters used in the Print Setup area which are not used or not used in the 97/03 version.

The code above is easily extended to include these if you desire.

One day when I have a spare moment (Most likely in 2025!) I will add the option for automatic incremental Page Numbers.

**CLOSING**
-----------

This code has saved, my staff and I, hundreds and hundreds of hours over the past decade whilst printing complex Excel workbooks.

This functionality was also one of the more requested issues from our poll of 3 months ago [We Want Your Ideas!](http://chandoo.org/wp/2011/07/22/we-want-your-ideas-results/ "We Want Your Ideas!")

I hope you enjoy it as much as I have ?

**Updates**

I will be extending the functionality of this in the future and so if you have any suggestions, lets hear them in the comments below:

**How have you tackled large print jobs ?**

I look forward to your comments below:

### _**Hui…**_

For a list of my other contributions at Chandoo.org please visit; [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [89 Comments](https://chandoo.org/wp/hui%e2%80%99s-excel-report-printer/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/hui%e2%80%99s-excel-report-printer/#respond)
    
*   Tagged under [page setup](https://chandoo.org/wp/tag/page-setup/)
    , [print](https://chandoo.org/wp/tag/print/)
    , [printing](https://chandoo.org/wp/tag/printing/)
    , [Printing reports](https://chandoo.org/wp/tag/printing-reports/)
    , [Reports](https://chandoo.org/wp/tag/reports/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousExcel Training Recommender – Interactive Excel Tool for you](https://chandoo.org/wp/best-excel-training-for-you/)

[NextParticipate in Microsoft BI DataMashUp Contest & You could win $3000 PrizeNext](https://chandoo.org/wp/microsoft-bi-datamashup-contest/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/hui%e2%80%99s-excel-report-printer/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/hui%e2%80%99s-excel-report-printer/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/hui%e2%80%99s-excel-report-printer/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
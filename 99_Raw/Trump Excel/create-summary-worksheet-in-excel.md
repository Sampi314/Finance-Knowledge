# Quickly Create Summary Worksheet with Hyperlinks in Excel

**Source:** https://trumpexcel.com/create-summary-worksheet-in-excel

---

[Skip to content](https://trumpexcel.com/create-summary-worksheet-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/create-summary-worksheet-in-excel/#below-title)

A lot of my colleagues spend a lot of their time in creating a Summary Worksheet in Excel.

A typical summary worksheet has the names of all the worksheets in different cells and all the names also hyperlinked to these worksheets.

So you can click on a cell with a sheet name (_say Jan, Feb, Mar…_) and it will take you to that worksheet. Additionally, there is also a [hyperlink](https://trumpexcel.com/hyperlinks/)
 on each worksheet that links back to the summary worksheet.

While my colleagues have become super efficient in doing this, it’s still a waste of time when you can do the same thing in less than a second (yes you read it right).

The trick is to [create a short macro](https://trumpexcel.com/excel-macro-examples/)
 that will do it for you.

No matter how many worksheets you have, it will instantly create a summary worksheet with working hyperlinks.

Something as shown below:

![Create Summary Worksheet with Hyperlinks in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20792%20684'%3E%3C/svg%3E)

As you can see in the image above, it instantly creates the summary when you [run the macro](https://trumpexcel.com/run-a-macro-excel/)
 (by clicking on the button). The sheet names are hyperlinked which takes you to the worksheet when you click on it.

##### Create Summary Worksheet with Hyperlinks

All the heavy lifting in creating the summary worksheet is done by a short VBA code. You just need to run the code and take a break as you would have some free time now 🙂

Here is the code:

Sub CreateSummary()
'Created by Sumit Bansal of trumpexcel.com
'This code can be used to create summary worksheet with hyperlinks
Dim x As Worksheet
Dim Counter As Integer
Counter = 0
For Each x In Worksheets
Counter = Counter + 1
If Counter = 1 Then GoTo Donothing
    With ActiveCell
        .Value = x.Name
        .Hyperlinks.Add ActiveCell, "", x.Name & "!A1", TextToDisplay:=x.Name, ScreenTip:="Click here to go to the Worksheet"
        With Worksheets(Counter)
            .Range("A1").Value = "Back to " & ActiveSheet.Name
            .Hyperlinks.Add Sheets(x.Name).Range("A1"), "", \_
            "'" & ActiveSheet.Name & "'" & "!" & ActiveCell.Address, \_
            ScreenTip:="Return to " & ActiveSheet.Name
        End With
    End With
ActiveCell.Offset(1, 0).Select
Donothing:
Next x
End Sub

##### Where to Put this Code?

Follow the steps below to place this code in the workbook:

1.  Go to Developer Tab and Click on Visual Basic. You can also use the keyboard shortcut – **ALT F11.**
    *   If you can find the developer tab in the ribbon in Excel, [click here](https://trumpexcel.com/excel-developer-tab/)
         to know how to get it.![Create Summary Worksheet with Hyperlinks in Excel - VB in Developer Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20692%20131'%3E%3C/svg%3E)
2.  There should be a Project Explorer pane at the left (if it is not there, use Control + R to make it visible).![Create Summary Worksheet with Hyperlinks in Excel - Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20376%20412'%3E%3C/svg%3E)
3.  Go to Insert and Click in Module. This adds a module to the workbook. Also, in the right, you would see the code window appears (with a blinking cursor). ![Create Summary Worksheet with Hyperlinks in Excel - insert module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20409'%3E%3C/svg%3E)
4.  In the module code window, copy and paste the above code.![Create Summary Worksheet with Hyperlinks in Excel - code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20258'%3E%3C/svg%3E)

##### Running the Code

To run this code:

*   Go to Developer Tab –> Code –> Macros. This will open the Macro Dialogue box.![Create Summary Worksheet with Hyperlinks in Excel - Macros](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20689%20133'%3E%3C/svg%3E)
*   Select the Macro CreateSummary and click on Run.![Create Summary Worksheet with Hyperlinks in Excel - Run Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20379%20367'%3E%3C/svg%3E)
*   This will run the macro and create the hyperlinks in the active sheet.

Another way to run the macro is to [insert a button/shape and assign the macro](https://trumpexcel.com/assign-macro-to-button-in-excel/)
 to it. To do this:

*   Insert a shape in the worksheet. Format the shape the way you want. ![Create Summary Worksheet with Hyperlinks in Excel - insert shape](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20581%20196'%3E%3C/svg%3E)
*   Right-click on it and select Assign Macro.![Create Summary Worksheet with Hyperlinks in Excel - Assign Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20272%20381'%3E%3C/svg%3E)
*   In the [Assign Macro](https://trumpexcel.com/run-a-macro-excel/)
     box, select the macro you want to assign to the shape and Click OK.![Create Summary Worksheet with Hyperlinks in Excel - Assign Macro box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20368'%3E%3C/svg%3E)

Now, you can simply click on the shape to run the macro.

_**Download the File from here  
**_[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Create-Index-Summary.xls)

**_Note:_**

1.  I have hard-coded the cell A1 in each sheet, which is hyperlinked to get you back to the summary sheet. Ensure that you change it accordingly if you have something already in A1 cell in each sheet.
2.  The summary does not create a hyperlink for itself (which makes sense as you are already on that sheet).
3.  Run this code when the Summary Worksheet is the active worksheet.
4.  You may want to add some formatting or rearrangement. But I hope this code takes care of the hard part.
5.  Save this workbook as .xls or .xlsm extension, as it contains a macro.

**Other Excel VBA tutorials:**

*   [Get Multiple Lookup Values Without Repetition in a Single Cell](https://trumpexcel.com/multiple-lookup-values-single-cell-excel/)
    .
*   [Task Prioritization Matrix – VBA Application](https://trumpexcel.com/free-excel-templates-excel-list/)
    .
*   [How to Combine Multiple Workbooks into One Excel Workbook](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
    .
*   [Excel VBA Loops – For Next, Do While, Do Until, For Each (with Examples)](https://trumpexcel.com/vba-loops/)
    .
*   [How to Record a Macro in – A Step by Step Guide.](https://trumpexcel.com/record-macro-vba/)
    
*   [How to Quickly Remove Hyperlinks from a Worksheet in Excel.](https://trumpexcel.com/remove-hyperlinks/)
    
*   [Online Excel VBA Course](https://trumpexcel.com/excel-vba-jetpack-course/)
    .
*   [How to Switch Between Sheets in Excel?](https://trumpexcel.com/switch-between-sheets-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

10 thoughts on “Quickly Create Summary Worksheet with Hyperlinks in Excel”
--------------------------------------------------------------------------

1.  Wow, that was amazing, what a great makro, thank you for posting
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-14878)
    
2.  Hi there. Great stuff here! I would like to know if you provide tutorial for extraction of particular cells to be placed in the summary worksheet alongside the worksheet hyperlink that the cell value was extracted from.
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-13738)
    
3.  Thanks for the macro! I have been researching ways to easily create a summary sheet for use by another company member. The link “return to summary” works, to go back to the summary page, but the hyperlinks do not work. There are spaces in most of the sheet names, which I see from other comments may create the problem. How do I fix that? Can I change something in the macro itself? There are over 300 sheets in this file, so doing name changes for the individual sheets is not an option at this point.
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-12472)
    
4.  Thank you! excellent steps by step tutorial all worked as expected!:)
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-12379)
    
5.  The code doesn’t work if the sheet names have spaces. Had to add the single quotes round the sheet names, then it works.  
    Thanks
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-10331)
    
6.  Hi there.. how can I make it work when there are spaces in the sheet name?
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-2136)
    
7.  I was thinking, what happens if the user renames a sheet?
    
    It would be nice, if this macro is made to run, every time, if anyone renames the sheet.
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-1413)
    
8.  Thanks for pointing out the glitch Manda. Have corrected the code and updated the download file. Hope this works fine now.
    
    Feel free to refer to this article in your blog 🙂
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-314)
    
    *   Hi,
        
        Im still getting a reference is not valid error, i have a hyphen in my sheets. Is there a fix for this?
        
        [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-13071)
        
9.  Hi
    
    The macro works brilliantly – kudos. 🙂
    
    Should let you know – the “Back to Summary Tab” hyperlinks don’t actually link back to the Summary sheet, just to A1 on their own sheet, causing a “Reference not valid” error message to appear when you click on them.
    
    Okay for me to refer to your work on my blog with a link to your post? excel-pixie.com/wp  
    Cheers
    
    [Reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#comment-313)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/create-summary-worksheet-in-excel/#respond)

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
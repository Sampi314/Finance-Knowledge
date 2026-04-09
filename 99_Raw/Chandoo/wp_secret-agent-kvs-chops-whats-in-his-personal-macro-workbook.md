# Secret Agent KV's Chops...what's in HIS Personal Macro Workbook? » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/secret-agent-kvs-chops-whats-in-his-personal-macro-workbook

---

*   [Posts by KV](https://chandoo.org/wp/category/posts-by-kv/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Secret Agent KV’s Chops…what’s in HIS Personal Macro Workbook?
==============================================================

*   Last updated on November 18, 2013

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

Yesterday, I talked about how you don’t have to know how to code in order to highly leverage VBA. All you need to know is how to Google, Cut, and Paste. As discussed then, I ‘volunteered’ KV under pain of exposure to empty the contents of his secret satchel onto the virtual table, so that we can rummage through it. So without further ado, please put your hands together and give a warm Chandoo welcome to secret agent KV.

\[Secret transmission starts…\]
===============================

Hello, this is my first guest post on Chandoo.org (or any Excel website for that matter), and I will try to keep it simple, but useful for our readers.

I have been using spreadsheets since 1990, and Excel since 1995 – which sort of makes me a veteran in this sphere of business applications 🙂

One of my favorite topics in Excel is – “How can I make my day-to-day tasks in Excel easier and faster ?”. In fact, this is a topic that I think about in everything to do with computers.

There are many ways one can do this in Excel, but among the more effective and scalable ones, is storing commonly used macros in your Personal Macro Workbook.

This post is about some of the stuff that I have put in my Personal Macro Workbook over the years. You can read more about how to set up a Personal Macro Workbook, in this [excellent tutorial](http://www.rondebruin.nl/win/personal.htm)
 on Ron de Bruin’s website. Like nuclear war, It’s a one-time exercise. And you can easily port it to any other computers that you use – or even share it with your friends and allied spooks.

This is the first bunch of macros which I use most frequently. Hopefully I will get a chance to post some more if this post is found to be good enough 🙂

So here goes.

  

1: Find the value of ActiveCell within selection, or in the whole sheet
-----------------------------------------------------------------------

This is a very useful macro which helps to search for the value in the ActiveCell within the selected range or the whole worksheet (if only ActiveCell is selected).

    
    Sub SearchOnActiveCellContents()
    ' Keyboard Shortcut: Ctrl+Shift+G
        On Error GoTo NotFound
    
        If Selection.Cells.Count > 1 Then
            Selection.Cells.Find _
                    (What:=ActiveCell.Value, After:=ActiveCell, LookIn:=xlValues, _
                     LookAt:=xlPart, SearchOrder:=xlByRows, SearchDirection:=xlNext, _
                     MatchCase:=False, SearchFormat:=False).Activate
        Else
            Cells.Find _
                    (What:=ActiveCell.Value, After:=ActiveCell, LookIn:=xlValues, _
                     LookAt:=xlPart, SearchOrder:=xlByRows, SearchDirection:=xlNext, _
                     MatchCase:=False, SearchFormat:=False).Activate
        End If
    
        Exit Sub
    NotFound:
        MsgBox "No cells found with this cell's contents"
    End Sub
    

  
As you will notice, the macro checks whether the selection is 1 cell or multiple cells, and accordingly executes the Cells.Find command.

2: Filter on value NOT equal to ActiveCell value
------------------------------------------------

This is another handy macro, which filters the current column based on the value of the active cell, except that the filter is applied as “show records NOT equal to the value of the active cell”  
The macro itself is a fairly simple one-line command :

    
    Sub AutoFilterSelectionNOT()
    ' Keyboard Shortcut: Ctrl+Shift+K
        Dim lField As Long
        lField = ActiveCell.Column - ActiveCell.CurrentRegion.Column + 1
        If TypeName(Selection) <> "Range" Then Exit Sub
        Selection.AutoFilter Field:=lField, Criteria1:="<>" & ActiveCell.Value
    End Sub
    

3\. Show or Hide zeros in active sheet
--------------------------------------

This macro toggles the display of zero-value cells on the active sheet.

    
    Sub Hide_Zeros()
    ' Keyboard Shortcut: Ctrl+Shift+Z
        If TypeName(Selection) <> "Range" Then Exit Sub
        ActiveWindow.DisplayZeros = Not ActiveWindow.DisplayZeros
    End Sub
    

4: Show or Hide page-breaks in active sheet
-------------------------------------------

This macro toggles the display of page-breaks on the active sheet.

    Sub ShowHidePageBreaks()
    ' Keyboard Shortcut: Ctrl+Shift+J
    
    If TypeName(Selection) <> "Range" Then Exit Sub
    
    ActiveSheet.DisplayPageBreaks = Not
    ActiveSheet.DisplayPageBreaks
    End Sub
    

  
As the name suggests , this macro will show or hide the display of page breaks on the active sheet.

5: Display the 'GoTo special' xldialog
--------------------------------------

Quite often I find myself needing to use the GoTo Special command.  
Of course, you can do it the way it was designed in Excel – press F5 to display the GoTo dialog box, and click on the Special… button. This takes one keystroke and a mouse-click; or 3 keystrokes (if you don’t use the mouse) 🙂

Or you can display the Goto > Special… dialog box (using a macro) with just 1 click of the mouse or 2 keystrokes (if you pin it on the QAT) !

    
    
    Sub xlSelectSpecial()
    
    On Error GoTo NotFound
        If Selection.Cells.Count = 1 Then
            MsgBox "Select more than 1 cell...", vbExclamation, "Select more cells..."
            Exit Sub
        End If
        Application.Dialogs(xlDialogSelectSpecial).Show
    Exit Sub
    NotFound:
        myMsgText = "No such cells found"
        myTitle = "Not found"
        myConfig = vbOKOnly + vbExclamation
        myMessage = MsgBox(myMsgText, myConfig, myTitle)
    End Sub
    

As you will notice, the macro has an error-checking line in case the type of ‘special cell’ you selected is not found. E.g. if you’re looking for blank cells in the selection, and all the cells in it are non-blank, the macro will display a message accordingly.

The macro also checks whether more than one cell is selected before executing the dialog. The reason for this is that if a single cell is selected, many of the options in the GoTo Special dialog box will execute on the entire ‘UsedRange’ of the spreadsheet, instead of the selected range.  
If you wish, you can comment out the If … End If construct and test the macro to see what I mean.

6: Zoom-in / Zoom-out
---------------------

These macros zoom in or zoom out on the worksheet, in increments of 5%.

    
    Sub MyZoomIn()
    ' Keyboard Shortcut: Ctrl+E
    
        Dim ZP As Integer
        ZP = ActiveWindow.Zoom
    
        If ZP >= 400 Then
            ZP = 400
        Else
            ZP = ZP + 5
        End If
    
        ActiveWindow.Zoom = ZP
    End Sub
    
    Sub MyZoomOut()
    ' Keyboard Shortcut: Ctrl+Shift+E
    
        Dim ZP As Integer
        ZP = ActiveWindow.Zoom
    
        If ZP <= 10 Then
            ZP = 10
        Else
            ZP = ZP - 5
        End If
    
        ActiveWindow.Zoom = ZP
    End Sub
    

  
As you will notice, will increase or decrease the zoom percentage by 5 points each time the macro is executed. The If… Then… Else… constructs are there to prevent an error if the current zoom percentage is already at the maximum or minimum level, when the macro is executed.

That’s all for this post from my side. I hope you will find it useful.

I welcome comments, suggestions for improvement & criticisms from readers on this topic, and the macros I have shared in this post.

\[Secret transmission ended.\]
==============================

Hey, thanks KV for sharing those shortcut-charged shortcuts. I look forward to torturing some more of that ill-gotten wisdom out of you. (While I don’t condone torture, I hate inefficient use of Excel even more. So while it’s going to hurt you more than me, it’s for the greater good.)

About the Author
----------------

KV is an undercover secret agent who spends his time rescuing the world from the crushing weight of evil, bloated spreadsheets.  
[![kv_Casual](https://chandoo.org/wp/wp-content/uploads/2013/11/kv_Casual.jpg)](https://chandoo.org/wp/wp-content/uploads/2013/11/kv_Casual.jpg)

His mild-mannered alter ego - Khushnood Viccaji - is a freelance professional and an expert in Management Information Systems and Business Applications with a focus on Data Management, Analytics, Transformation, Auditing, and Reporting.  
[![kv_Smart](https://chandoo.org/wp/wp-content/uploads/2013/11/kv_Smart.jpg)](https://chandoo.org/wp/wp-content/uploads/2013/11/kv_Smart.jpg)

Both these chaps have a flair for understanding and applying technology in business processes and an ability to present business information in many different ways. And one of them wears lycra.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [23 Comments](https://chandoo.org/wp/secret-agent-kvs-chops-whats-in-his-personal-macro-workbook/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/secret-agent-kvs-chops-whats-in-his-personal-macro-workbook/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [advanced vba](https://chandoo.org/wp/tag/advanced-vba/)
    , [Efficiency](https://chandoo.org/wp/tag/efficiency/)
    , [excel add-ins](https://chandoo.org/wp/tag/excel-add-ins/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [keyboard shortcuts](https://chandoo.org/wp/tag/keyboard-shortcuts/)
    , [Personal Macro Workbook](https://chandoo.org/wp/tag/personal-macro-workbook/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Posts by KV](https://chandoo.org/wp/category/posts-by-kv/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousWhat would James Bond have in his Personal Macro Workbook?](https://chandoo.org/wp/using-personal-macro-workbook/)

[NextFind last day of any month with this simple trick \[formulas\]Next](https://chandoo.org/wp/last-day-of-month-formula/)

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

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
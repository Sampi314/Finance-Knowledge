# Add a Calendar selection tool to an Excel workbook

**Source:** https://chandoo.org/wp/huis-calendar-tool

---

*   [Automation](https://chandoo.org/wp/category/automation/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Hui’s Calendar Tool (as Borrowed from Chandoo)
==============================================

*   Last updated on April 7, 2014

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

In January a friend asked me to assist with a small Excel assignment.

Her company wanted to add a Calendar control to a worksheet so that people could interactively select a date. I have never understood why people like this as nothing is quicker than typing a date as 7/4/14 and letting excel sort it out. But hey, that’s what the client wants.

The issue was that it had to work in every version of Excel from Excel 2002/XP to Excel 2013.

As anybody who has used the Calendar controls in Excel VBA Knows, they rarely work between versions and often require VBA references to be added/changed and DLL’s downloaded to make them work.

This model had to be able to be opened across all the Excel versions from Excel 2002/XP to Excel 13 and even transferred from one version to another regularly.

After struggling with the concept a while I threw away the Calendar Control idea and decided to plagiarise Chandoo’s 2014 Calendar.

Hui’s ~Chandoo’s~ Calendar Tool
-------------------------------

Every year Chandoo releases a Yearly Calendar as a small gift to his readers. The 2014 calendar is [available here](http://chandoo.org/wp/2014/01/02/download-free-2014-calendar-daily-planner-templates/ "2014 Calendar")
.

It has all the facilities of a calendar using simple worksheet functions and Named Formula, and it doesn’t use VBA.

So, why not add a bit of generic VBA and use this as a Calendar selection tool?

The Process
-----------

Chandoo’s 2014 Calendar was stripped down to its absolute basic being 2 worksheets and a number of named Formulas which controlled the calculations.

The idea was to:

1.  Let the user to Select a cell, where they want to enter a date, It can be any cell on any worksheet.
2.  Press a Calendar Button or or Double Click on the cell and be taken to a Calendar.
3.  Select a date in the Calendar.
4.  Have a level of validation/acceptance of certain dates and rejection of other dates.
5.  Be taken back to the original worksheet and have the date placed into the original cell.

The calendar should pop up and be hidden by VBA code and shouldn’t require the user to know how to do that.

The Calendar had to have a level of user ability to modify the selection criteria and obviously the active year.

The calendar shouldn’t be reliant on any Addins, DLL’s or other external files.

Lets have a look at the components.

The Components
--------------

The following description and images use a sample file which you can [Download here](https://chandoo.org/wp/wp-content/uploads/2014/04/Huis-Calendar-Tool.xls "Huis Calendar Tool")
.

The File is compatible with all PC Excel versions but your screens may look slightly different in different versions, mostly colors are rendered slightly differently.

If you use a Mac Excel version, please let us know how this goes?

### The Interface

The Interface is simple, You select a cell where you want to insert a date and press the Calendar Button or Double Click the cell:

[![Cal01](https://chandoo.org/wp/wp-content/uploads/2014/04/Cal01.png)](https://chandoo.org/wp/wp-content/uploads/2014/04/Cal01.png)

The calendar Button uses some simple VBA to store the names of the worksheet and cell where the cursor was when the button was pressed and then opens the Calendar sheet by un-hiding it (making it visible) as per below:

[![Cal02](https://chandoo.org/wp/wp-content/uploads/2014/04/Cal02.png)](https://chandoo.org/wp/wp-content/uploads/2014/04/Cal02.png)

The above image shows the calendar.

This user wanted to only allow Fridays or Saturdays to be selected and so they are manually colored Yellow.

If you select any non-yellow cell – Nothing happens

If you select any yellow cell – That date is returned to your original location

Click on the Year and change it to another value to change years

Selecting the Close button closes the calendar and returns you to your original location with no changes.

You can change the Dates that are allowable to be selectable by either changing the VBA or Selecting Multiple cells and coloring as appropriate.

### The Calendar

This Calendar tool in it’s most basic format consists of three Worksheets **My Worksheet**, **Calendar** and **Mini**

[![Cal03](https://chandoo.org/wp/wp-content/uploads/2014/04/Cal03.png)](https://chandoo.org/wp/wp-content/uploads/2014/04/Cal03.png)

**My Worksheet** is a worksheet where I want to use the date and do my work

**Mini** is a Row by Row version of the calendar, it remains hidden at all times but it is busy in the background calculating the dates

**Calendar** is simply a display of the Mini Data in a convenient 12 Month layout

The **Calendar** worksheet is where the user can select a Date. If the date is Valid (Yellow), the user selected date is returned to the original worksheet and cell, otherwise the user remains on the Calendar worksheet

The relationship between the Mini and Calendar is all handled by Named Formula which the user doesn’t need to worry about

### The VBA

**My Worksheet**

My Worksheet is a user area where the user is doing his work.

[![Cal01](https://chandoo.org/wp/wp-content/uploads/2014/04/Cal01.png)](https://chandoo.org/wp/wp-content/uploads/2014/04/Cal01.png)

The user can invoke the Calendar Tool in two ways

1.  Select any Cell and press the Calendar Button; or
2.  Select any Cell and double click it

If the user uses method 1, pressing the calendar Button calls the Show\_Calendar subroutine

If the user uses method 2, Double clicking a cell,  the **Worksheet\_BeforeDoubleClick()** event is triggered on the My Worksheet VBA Code Module

The Worksheet\_BeforeDoubleClick() event simply calls the Show\_Calendar subroutine

Private Sub Worksheet\_BeforeDoubleClick(ByVal Target As Range, Cancel As Boolean)
  Show\_Calendar
End Sub

The Show\_Calendar() subroutine in the Calendar\_Modules VBA code module subroutine has 2 tasks to perform:

The 2 tasks are to store the location of the cell that the user wants the date in. It is stored in two variables mySht and myRng

These two variables are defined outside the Show\_Calendar() subroutine and are declared as Public

This means they are available to all subroutines in the workbook.

Public mySht As String
Public myRng As String

Sub Show\_Calendar()

  mysht = ActiveSheet.Name
  myRng = ActiveCell.Address

  Sheets("Calendar").Visible = True
  Sheets("Calendar").Select
End Sub

**Calendar**

Once on the Calendar two subroutines control the users interaction.

The **Worksheet\_SelectionChange()** and **Close\_Calendar()** subroutines control the users interactions as described below:

The main interaction is controlled by a **Worksheet\_SelectionChange()** event in the calendar Worksheet VBA Code module.

Put simply it monitors when a selection changes and reacts accordingly

If a user selects multiple cells it is ignored

If a user selects a non-Yellow cell it is ignored

If a user selects a Yellow cell the subroutine sets the original users cell to the value of the selected date and formats the cell as appropriate

Private Sub Worksheet\_SelectionChange(ByVal Target As Range)

If Target.Cells.Count <> 1 Then Exit Sub

If Target.Interior.Color = 65535 Then 'Set Cell Color requirement here
  Sheets(mysht).Range(myRng) = Target
  With Sheets(mysht).Range(myRng)
    .NumberFormat = "m/d/yyyy" 'Set cells Date format here
    .HorizontalAlignment = xlCenter
    .VerticalAlignment = xlCenter
  End With

  Sheets("Calendar").Visible = False
  Sheets(mysht).Select
End If

End Sub

The Close\_Calendar() subroutine is called when the Close Button is selected

It simply hides the Calendar Worksheet and returns the user to the Original worksheet he was working on

Sub Close\_Calendar()

  Sheets("Calendar").Visible = False   Sheets(mysht).Select \\

End Sub

If you want to enable a user to select any date you can either

1\. Set all valid dates to have a color Yellow

2\. Remove the date checking section of the code. Comment out the two Lines colored in Red Below:

Private Sub Worksheet\_SelectionChange(ByVal Target As Range)

If Target.Cells.Count <> 1 Then Exit Sub

'If Target.Interior.Color = 65535 Then 'Set Cell Color requirement here
  Sheets(mysht).Range(myRng) = Target
  With Sheets(mysht).Range(myRng)
    .NumberFormat = "m/d/yyyy" 'Set cells Date format here
    .HorizontalAlignment = xlCenter
    .VerticalAlignment = xlCenter
  End With

  Sheets("Calendar").Visible = False
  Sheets(mysht).Select
'End If

End Sub

The Final Product
-----------------

[![Huis Calendar Tool](https://chandoo.org/wp/wp-content/uploads/2014/04/Huis-Calendar-Tool.gif)](https://chandoo.org/wp/wp-content/uploads/2014/04/Huis-Calendar-Tool.gif)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Other Calendar Posts
--------------------

Chandoo has written a number of posts on calendars, some are shown below:

[http://chandoo.org/wp/2013/11/13/pop-up-calendar-excel-vba/](http://chandoo.org/wp/2013/11/13/pop-up-calendar-excel-vba/)

[http://chandoo.org/wp/2013/04/09/how-to-create-interactive-calendar-to-highlight-events-appointments-tutorial/](http://chandoo.org/wp/2013/04/09/how-to-create-interactive-calendar-to-highlight-events-appointments-tutorial/)

[http://chandoo.org/wp/2012/09/12/interactive-pivot-calendar/](http://chandoo.org/wp/2012/09/12/interactive-pivot-calendar/)

[http://chandoo.org/wp/tag/printable-calendar/](http://chandoo.org/wp/tag/printable-calendar/)

Conclusion
----------

This workbook has been tested in all versions of PC versions of Excel from 2002 to 2013 and it works a treat.

It is an Excel XLS file and runs in compatibility mode in Excel 2007+

You are free to use and extend it as required.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/huis-calendar-tool/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/huis-calendar-tool/#respond)
    
*   Tagged under [calendar](https://chandoo.org/wp/tag/calendar/)
    
*   Category: [Automation](https://chandoo.org/wp/category/automation/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousCP004: Can I Pie Chart in Public? Discussion about Pie charts, their merits and drawbacks, when to use & when to avoid them](https://chandoo.org/wp/cp004-can-i-pie-chart-in-public-discussion-about-pie-charts-their-merits-and-drawbacks-when-to-use-when-to-avoid-them/)

[NextVisualize state to state migration data and you could win an iPad or Galaxy Tab \[Datavis Contest 2014\]Next](https://chandoo.org/wp/visualize-state-migration-contest/)

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
    
    [Reply](https://chandoo.org/wp/huis-calendar-tool/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/huis-calendar-tool/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/huis-calendar-tool/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
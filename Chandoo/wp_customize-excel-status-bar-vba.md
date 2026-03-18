# Show cell difference in Status Bar » VBA Examples » Chandoo.org

**Source:** https://chandoo.org/wp/customize-excel-status-bar-vba

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Show difference between cells in status bar – VBA Example
=========================================================

*   Last updated on September 10, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We can select a few cells in Excel and quickly see their count, sum etc. in the status bar. **Ever wanted to customize the status bar to show** something else, say **_difference_**? You can use VBA add-ins with application level events to achieve this. In this Example, learn how to customize status bar with Excel VBA. We will see how to set up a class module, application event in our personal macro add-in.

![Show difference of selected cells in Excel Status Bar using VBA](https://chandoo.org/wp/wp-content/uploads/2019/09/show-difference-in-status-bar-vba-demo.png)

_Note: This is a reasonably advanced VBA example. If you are a VBA newbie, start with [FREE Excel VBA Crash Course](https://chandoo.org/wp/introduction-to-vba-macros/)
, and come back when you are ready._

If you just want to show difference in a specific worksheet…
------------------------------------------------------------

Then you could use Worksheet\_SelectionChange() Event in that sheet to set Application.StatusBar to what you need.

But our problem is a bit more complicated. **We want to customize status bar** to show difference **in any Excel file**.

Using Excel Add-in to customize status bar
------------------------------------------

Anytime you want to use a macro or automate things in multiple files, you need to create Excel add-ins. While this sounds complicated. making an add-in is rather simple. You just create the necessary VBA code and save the file as “Excel Add-in” type. Once such a file is saved, you can then install this add-in using Developer ribbon > Excel Add-in button. Now, you can use the add-in functionality from any open file.

For the purpose of our status bar customization, we will **[use Personal Macro workbook](https://chandoo.org/wp/using-personal-macro-workbook/)
**.

If you do not yet have a personal macro workbook, go make one. Refer to above link for instructions.

Step by step instructions to add status bar changing code
---------------------------------------------------------

**Step 1: Open Excel, go to Visual Basic Editor** (ALT+F11) and locate your personal macro add-in file.

**Step 2: Insert a class module**. In the personal macro file, insert a class module. Name this module as **_clsApp_**.

Paste below code in the class.

    Public WithEvents app As Application

This adds a variable (property) called app to the class clsApp.

**Step 3: Insert a module**. In this module, we will write necessary code to **make an object** instance of the **_clsApp_**.

Paste this code.

    Option Explicit
    'code originally from https://jkp-ads.com/Articles/buildexceladdin05.asp
    'Variable to hold instance of class clsApp
    Dim mcApp As clsApp
    
    Public Sub Init()
        'Reset mcApp in case it is already loaded
        Set mcApp = Nothing
        'Create a new instance of clsApp
        Set mcApp = New clsApp
        'Pass the Excel object to it so it knows what application
        'it needs to respond to
        Set mcApp.app = Application
    End Sub

**What this code is doing?** As annotated in the comments, this code is simply to initialize the mcApp variable with current Excel application.

**Step 4: Go back to class module and add app level event**. Now, let’s go back to the class module and click on on the drop-down above and select “app” and select the event SheetSelectionChange.

This adds a blank event at app level for SheetSelectionChange.

Paste below code.

    Private Sub app_SheetSelectionChange(ByVal Sh As Object, ByVal Target As Range)
        Application.StatusBar = ""
        On Error GoTo Finish
        If Selection.Cells.Count = 2 Then
            Application.StatusBar = "Diff: " & (Selection.Cells(1) - Selection.Cells(2))
        Else
            Application.StatusBar = ""
        End If
    Finish:
    End Sub

**What’s going on here:** This code simply checks with Selection has two cells. If so, it sets the statusbar to the word “Diff:” followed by actual difference.

In all other cases (including any errors), the status bar is set to empty (which resets it).

**Step 5: Go to ThisWorkbook on the add-in file add code to init**

Finally, we want to load mcApp (our instance for the Excel Application) whenever Excel is loaded. To do this, go to _ThisWorkbook_ on the personal add-in file, double click on it and add the Workbook Open event.

Paste below code in there.

    'code originally from https://jkp-ads.com/Articles/buildexceladdin05.asp
    Private Sub Workbook_Open()
        Application.OnTime Now, "'" & ThisWorkbook.FullName & "'!Init"
    End Sub

That is all. **We have now created an application level event listener** that _monitors any selection changes_ across all open workbooks. If user selects two cells, then it will display the difference between them in the status bar.

### **Here is an illustration of the chain of actions that happen**

![](https://chandoo.org/wp/wp-content/uploads/2019/09/how-application-level-event-listener-works.png)

Show cell difference in status bar – Video Tutorial
---------------------------------------------------

I made a video explaining the entire code and demoed the result. Watch it below if you are still hazy about the process. You can also [watch this on my YouTube channel](https://youtu.be/LuRUNCLiP2g)
.

References & Resources to learn more…
-------------------------------------

Big thanks to Jan Karel Pieterse & late Chip Pearson for excellent info on class module driven application event listeners.

*   [Application Events in Excel](http://www.cpearson.com/Excel/AppEvent.aspx)
     \[cpearson\]
*   [Application Events as part of Excel Add-in](https://jkp-ads.com/Articles/buildexceladdin05.asp)
     \[jkp-ads\]

**[Setting up Personal Macro add-in Workbook](https://chandoo.org/wp/using-personal-macro-workbook/)
**

**More info on Worksheet\_SelectionChange event**

*   [Use SelectionChange to highlight things in Excel](https://chandoo.org/wp/highlight-row-column-of-selected-cell-using-vba/)
    
*   [Show details on demand using VBA](https://chandoo.org/wp/show-details-on-demand-in-excel/)
    

**Learn Excel VBA**

*   [Excel VBA Crash Course](https://chandoo.org/wp/introduction-to-vba-macros/)
     – FREE basic course
*   [Excel VBA Online Classes](https://chandoo.org/wp/vba-classes/)
     – Paid full length course

_This article is inspired from a question_ posted in my Facebook group [by Istiyak](https://www.facebook.com/Chandoo.org/videos/587472155119352/?comment_id=588080228391878)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [3 Comments](https://chandoo.org/wp/customize-excel-status-bar-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/customize-excel-status-bar-vba/#respond)
    
*   Tagged under [application events](https://chandoo.org/wp/tag/application-events/)
    , [class modules](https://chandoo.org/wp/tag/class-modules/)
    , [excel add-ins](https://chandoo.org/wp/tag/excel-add-ins/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [status bar](https://chandoo.org/wp/tag/status-bar/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [vba events](https://chandoo.org/wp/tag/vba-events/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousYummy WAFFLE chart in Power BI](https://chandoo.org/wp/waffle-chart-power-bi/)

[Next#awesome trick – Extract word by position using FILTERXML()Next](https://chandoo.org/wp/extract-words-with-filterxml/)

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
    
    [Reply](https://chandoo.org/wp/customize-excel-status-bar-vba/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/customize-excel-status-bar-vba/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/customize-excel-status-bar-vba/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
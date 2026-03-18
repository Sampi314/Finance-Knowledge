# How to create interactive calendar to highlight events & appointments [Tutorial] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-create-interactive-calendar-to-highlight-events-appointments-tutorial

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

How to create interactive calendar to highlight events & appointments \[Tutorial\]
==================================================================================

*   Last updated on April 9, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

One of the popular uses of Excel is to maintain a list of events, appointments or other calendar related stuff. While Excel shines easily when you want to log this data, it has no quick way to visualize this information. But we can use little creativity, conditional formatting, few formulas & 3 lines of VBA code to create a slick, interactive calendar in Excel. Today, lets understand how to do this.

### But first, a reminder to join my Advanced Excel masterclass in USA

As you may know, I am running my first ever Advanced Excel & Dashboards Masterclass in USA this summer (May / June 2013). We will be doing 2 day interactive sessions on Excel, advanced Excel, interactive charts, pivot tables & dashboards in Chicago, New York, Washington (DC) & Columbus (OH). If you live near any of these cities and want to become awesome in Excel, please consider enrolling in my Masterclass.

[**Click here for details & to book your spot**](http://chandoo.org/wp/resources/aed-masterclass-usa-2013/ "Advanced Excel & Dashboards Masterclass – USA 2013")
 | [Download Masterclass brochure](https://img.chandoo.org/training/usa2013/USA-Advanced-Excel-training-brochure-final.pdf)

### Back to the interactive calendar

Coming back to our topic at hand – interactive calendar, what do we mean by this?

Well, something like below:

![Interactive Event Calendar in Excel - Demo](https://img.chandoo.org/vba/interactive-calendar-masterclass-usa.gif)

How to create an interactive calendar from a set of events
----------------------------------------------------------

### 1\. Collect all the event data in a table

Just enter event data in a table like below:

![Interactive calendar - event data](https://img.chandoo.org/vba/events-appointments-data.png)

### 2\. Set up a calendar in a separate rate

If your events span several months, then you can [use formulas to generate calendar](http://chandoo.org/wp/2012/12/26/download-free-2013-calendar/)
.

In my case, all the events (Masterclass sessions) are in May & June 2013. So I just entered date of May 1st in a cell, dragged it sideways and then re-arranged the cells to make it look like a calendar. At this stage, the calendar should look like this:

![set up a blank calendar first - Interactive calendar](https://img.chandoo.org/vba/setup-blank-calendar.png)

### 3\. Name the calendar range

This is simple. Select all the cells in calendar range and give a name to it. I called mine “calendar”.

### 4\. Assign a cell for identifying which date is selected

Select a blank cell in your workbook, give it a name like “selectedCell”. We will use this to identify which date is selected by user.

### 5\. Write Worksheet\_selectionchange() event

This will help us identify when user selects a cell in “calendar” range. The below 3 line VBA should do. Please attach it to the sheet where your calendar is.

Private Sub Worksheet\_SelectionChange(ByVal Target As Range)
    If Not Application.Intersect(Target, Range("calendar")) Is Nothing Then
       \[selectedCell\] = ActiveCell.Value
    End If
End Sub

Tutorial: [Showing details when user selects a cell](http://chandoo.org/wp/2011/04/07/show-details-on-demand-in-excel/)

### 6\. Set up the formulas to show details when a valid date is selected

Lets say, each event has 4 details associated with it – title, date, venue & description.

Now, we need to show details of the event when user selects a date in the calendar. Since the selected date is in “selectedCell”, we can use [VLOOKUP](http://chandoo.org/wp/2012/03/30/comprehensive-guide-excel-vlookup/)
, [IF](http://chandoo.org/excel-formulas/if.shtml)
, [IFERROR](http://chandoo.org/wp/2011/03/11/iferror-formula/)
 formulas to do this:

*   Fetch event title in a cell if date selected has an event in it. Else keep it blank
    *   \=IFERROR(VLOOKUP(selectedCell, table\_of\_events, event\_title\_column, false),"")
        
*   Fetch rest of event details, but keep them blank if date has no events.

Lets say these 4 details are fetched to cells D1, D2, D3 & D4 cells.

### 7\. In calendar sheet, add 4 text boxes and assign them to cells

Finally, in calendar sheet, add 4 text boxes. Assign them to D1, D2, D3 & D4 cells. Arrange and format them as you fancy.

Tip: to assign a cell to text box, just select the text box, go to formula bar and type =D1 press enter.

### 8\. Set up conditional formatting to highlight selected dates

Finally, add a simple conditional formatting rule to highlight the selected dates in calendar. This is simple. Assuming calendar starts at cell A1,

*   Select the calendar range
*   Go to conditional formatting
*   Add new rule
*   Select rule type as “Use a formula to determine which cells to highlight”
*   type the rule as =A1=selectedCell
*   Set up formatting

PS: in my data above, I have used different formula as we need to highlight 2 dates of a Masterclass even when 1 is selected.

Tip: [Introduction to conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
.

### 9\. Clean up and formatting

Clean up your worksheets and format the calendar so that it looks gorgeous. And you are done!

![Finalized Interactive calendar](https://img.chandoo.org/vba/interactive-event-calendar-in-excel.png)

Download Interactive Calendar Example file
------------------------------------------

[**Click here to download interactive calendar example file**](https://img.chandoo.org/vba/masterclass-interactive-calendar.xlsm)
 and play with it to understand this better.

Examine the formulas in “Calcs” sheet & VBA code so that you can see how this is weaved.

Work with calendar data often, then you are in luck
---------------------------------------------------

If you use calendar data often and are looking for some inspiration, ideas & examples on how to represent it, then check out below examples:

*   [Employee vacation tracker & dashboard](http://chandoo.org/wp/2013/01/24/employee-vacations-tracker-dashboard/)
    
*   [Creating perpetual calendar & event tracker in Excel](http://chandoo.org/wp/2012/12/26/download-free-2013-calendar/)
    
*   [Interactive pivot table calendar & chart in Excel](http://chandoo.org/wp/2012/09/12/interactive-pivot-calendar/)
    
*   [Creating an interactive picture calendar](http://chandoo.org/wp/2012/01/02/picture-calendar-template/)
    
*   [Employee shift calendar template](http://chandoo.org/wp/2011/08/01/shift-calendar-excel-template/)
    
*   [Annual goals tracker](http://chandoo.org/wp/2010/03/01/employee-goal-tracker-excel/)
    

Do you like the interactive calendar?
-------------------------------------

I often use interactive calendars in my dashboards & client projects. Since calendars are very natural way to understand events, they work really well.

What about you? Do you use calendars often? How do you like the above technique? Please share your thoughts & ideas using comments.

PS: And if you are waiting to become awesome in Excel, then wait no more. Book your spot in my upcoming Masterclass. [_Click here_](http://chandoo.org/wp/resources/aed-masterclass-usa-2013/ "Advanced Excel & Dashboards Masterclass – USA 2013")
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [40 Comments](https://chandoo.org/wp/how-to-create-interactive-calendar-to-highlight-events-appointments-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-create-interactive-calendar-to-highlight-events-appointments-tutorial/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [calendar](https://chandoo.org/wp/tag/calendar/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [iferror](https://chandoo.org/wp/tag/iferror/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [masterclass](https://chandoo.org/wp/tag/masterclass/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [tables](https://chandoo.org/wp/tag/tables/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousWhat is your favorite feature of Excel? \[poll\]](https://chandoo.org/wp/your-favorite-feature-poll/)

[NextSome charts try to make you an April fool all the time (or why 3d pie charts are evil)Next](https://chandoo.org/wp/why-3d-pie-charts-are-evil/)

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
    
    [Reply](https://chandoo.org/wp/how-to-create-interactive-calendar-to-highlight-events-appointments-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-create-interactive-calendar-to-highlight-events-appointments-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-create-interactive-calendar-to-highlight-events-appointments-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
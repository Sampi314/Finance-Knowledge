# Adding Macros & Final Touches to Customer Service Dashboard [Part 4 of 4] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/adding-macros-customer-service-dashboard

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Adding Macros & Final Touches to Customer Service Dashboard \[Part 4 of 4\]
===========================================================================

*   Last updated on August 31, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Welcome back_. In final part of **Making a Customer Service Dashboard using Excel** let us learn how to add macros & VBA code that makes our dashboard interactive.

[Designing Customer Service Dashboard](http://chandoo.org/wp/2012/02/22/design-customer-service-dashboard/)
  
[Data and Calculations for the Dashboard](http://chandoo.org/wp/2012/03/14/calculations-for-customer-service-dashboard/)
  
[Creating the dashboard in Excel](http://chandoo.org/wp/2012/04/18/creating-customer-service-dashboard-in-excel/)
  
**Adding Macros & Final touches**

As you can see, there are 2 important macros in this dashboard.  
![Adding Macros & Final Touches to Customer Service Dashboard](https://img.chandoo.org/dashboards/macros-vba-in-customer-service-dashboard.png "Adding Macros & Final Touches to Customer Service Dashboard")

#1: Capturing selected item details
-----------------------------------

Whenever user clicks on an item in the detail area to compare, there is a small macro running behind that tells us what item is selected so that we can trigger our calculations and conditional formats. _**How does it work?**_

Simpler than we think!  
**We use a macro called as Worksheet\_SelectionChange.**

Related: [Introduction Excel VBA](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)

### Understanding Event Macros

There is a special type of macros in Excel called as Event macros (or simple events). For example, if you want to do something whenever user selects cell D14, you can use an event macro. Excel offers various events so that we can initiate certain actions when user selects a cell, clicks on a hyperlink, activates a worksheet, updates a pivot table or finishes some calculation etc.

In our case, we wanted to change the comparison options based on what is selected by user. So we use an event called as Worksheet\_SelectionChange

When you add a selection change macro to any worksheet, excel runs whenever you select a cell in that worksheet. Lets look a simple worksheet selection change macro to understand this:

![Demo of Worksheet_SelectionChange event macro - Excel VBA Customer Service Dashboard](https://img.chandoo.org/dashboards/worksheet-selection-change-demo.gif "Demo of Worksheet_SelectionChange event macro - Excel VBA Customer Service Dashboard")

_**The code for above event:**_

`Private Sub Worksheet_SelectionChange(ByVal Target As Range)   [valSelection] = "You have selected " & Target.Address   End Sub   `

The range _valSelection_ is linked to text box that you saw in demo.

### Event macro in our Customer Service Dashboard

In our dashboard, we have one additional challenge. **We need to run our event macro only if one of the two lists (rndSel1 & rngSel2).**

This is where we use an additional feature of VBA, _Application.intersect() formula._ This checks whether given two ranges overlap and if so, returns the region in overlap.

### Lets look at our event macro:

`Private Sub Worksheet_SelectionChange(ByVal Target As Range)   'This macro is triggered whenever any cell is selected in the Dashboard worksheet`

`'Step #1: If user clicks on a blank cell then do nothing   If ActiveCell.Value = "" Then Exit Sub   'Step#2: See if the selected cell is in left column   If Not (Application.Intersect(ActiveCell, Range("rngSel1").Cells) Is Nothing) Then   'If so, then call setOption1 macro   Call setOption1   'Step #3: See if the selectd cell is in right column   ElseIf Not (Application.Intersect(ActiveCell, Range("rngSel2").Cells) Is Nothing) Then   'If so, then call setOption2 macro   Call setOption2   End If   End Sub`

If you examine the comments, most of what it does should be obvious.

#2: Showing & Hiding help messages
----------------------------------

Adding help feature to complex dashboards makes life simpler for end users. So I always recommend it to my students. But how easy is it to add help?

Well, easier than you think. Just follow below steps:

1.  Add help messages to your dashboard using drawing shape > bubbles
2.  Once all the messages are added, just select all of them and group (right click > group)
3.  Select the group and using name box in Excel, give it a name, in our case the name is _boxHelp_
4.  In a new module, Write a macro (lets call it showHideHelp) to display and hide the boxHelp group.
5.  Now add a small text box with label “Help” on it.
6.  Assign the macro to this help text. (right click on the group, assign macro)

### But what do we put in showHideHelp macro?

Simple, When user clicks on **Help** text, we will just toggle the visibility of _boxHelp group_ using code like this:

`ActiveSheet.Shapes.Range(Array("boxHelp")).Visible = Not ActiveSheet.Shapes.Range(Array("boxHelp")).Visible   `

The **Not** portion toggles the visibility, thus when you click on help button the help gets turned on if it is off (and vice-a-versa)

Download Customer Service Dashboard
-----------------------------------

Download final version of our customer service dashboard using below links:

Excel 2010 version: [**Click here to download the dashboard workbook**](https://img.chandoo.org/dashboards/customer-service-dashboard-v1.xlsm)
  
Excel 2007 version: [**Click here to download the dashboard workbook**](https://img.chandoo.org/dashboards/customer-service-dashboard-v1-xl2007.xlsm)

Examine the VBA Code to learn better.

Future directions for this dashboard…
-------------------------------------

I am happy how this turned out so far. That said, we can make a few advancements to it like:

*   Using Excel 2010 slicers to make the selection of items in comparison area.
*   Adding ability to export dashboard as PDF or PPT
*   Adding qualitative comments to dashboard (automated a la [tweetboard](http://chandoo.org/wp/2009/05/07/tweetboard/ "Tweetboards – Alternative to traditional management dashboards")
     or manual) so that managers can understand what caused the change.
*   Adding customizable time windows. Currently the dashboard shows any 4 week window, but it can become even more powerful by adding custom start and end dates.

Note: Make sure you have gone thru previous 3 parts of this tutorial as well.

[Designing Customer Service Dashboard](http://chandoo.org/wp/2012/02/22/design-customer-service-dashboard/)
  
[Data and Calculations for the Dashboard](http://chandoo.org/wp/2012/03/14/calculations-for-customer-service-dashboard/)
  
[Creating the dashboard in Excel](http://chandoo.org/wp/2012/04/18/creating-customer-service-dashboard-in-excel/)

How would you approach this dashboard?
--------------------------------------

If you were to analyze and design a dashboard for customer service department, how would you approach it? What metrics, information would be very important for you? Please share your ideas and thoughts using comments.

Learn more about Dashboards
---------------------------

If you are looking for examples, information & tutorials on Excel dashboards, you are at the best. At Chandoo.org we have elaborate examples, tutorials, training programs & templates on Excel dashboards, to make you awesome. Please go thru below to learn more:

*   [KPI Dashboards in Excel – 6 part tutorial](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    
*   [**Excel Dashboards**](http://chandoo.org/wp/excel-dashboards/)
     – Information, Examples, Templates & Tutorials
*   [**Excel Dynamic Charts**](http://chandoo.org/wp/tag/dynamic-charts/)
     – Examples, tutorials & inspiration
*   [**Excel School Dashboards Program**](http://chandoo.org/wp/excel-school/)
     – Learn how to create this and other dashboards in Excel

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/adding-macros-customer-service-dashboard/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/adding-macros-customer-service-dashboard/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousAn IF Formula Challenge for you](https://chandoo.org/wp/if-formula-challenge-for-you/)

[NextThank you, I am flying to Australia today!Next](https://chandoo.org/wp/thank-you-going-to-australia/)

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
    
    [Reply](https://chandoo.org/wp/adding-macros-customer-service-dashboard/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/adding-macros-customer-service-dashboard/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/adding-macros-customer-service-dashboard/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
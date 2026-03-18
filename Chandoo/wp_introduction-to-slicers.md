# Excel Slicers - Introduction, what are they, how to use them, tips, advanced concepts, interactive charts & reports using Slicers & Pivot Tables

**Source:** https://chandoo.org/wp/introduction-to-slicers

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Introduction to Slicers – What are they, how to use them, tips, advanced techniques & interactive reports using Excel Slicers
=============================================================================================================================

*   Last updated on November 11, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Slicers** are one of my favorite feature in Excel. And here is a quick demo to show why they are my favorite.

![Introduction to Slicers - what are they, how to use them, tips, advanced techniques and formatting - Excel Pivot Tables & Slicers - Tutorial](https://img.chandoo.org/pivot/slicers/introduction-to-slicers.gif)

Slicers – what are they?
------------------------

Slicers are _visual filters._ Using a slicer, you can filter your data (or pivot table, pivot chart) by clicking on the type of data you want.

For example, let’s say you are looking at sales by customer profession in a pivot report. And you want to see how the sales are for a particular region. There are 2 options for you do drill down to an individual region level.

1.  Add region as report filter and filter for the region you want.
2.  Add a slicer on region and click on the region you want.

With a report filter (or any other filter), you will have to click several times to pick one store. **With slicers, it is a matter of simple click**.

#### See this demo:

![Demo of Excel slicers](https://img.chandoo.org/pivot/slicers/excel-slicer-demo1.gif)

Getting started with Slicers – Video
------------------------------------

Here is a quick 5 minute video tutorial on Slicers. If are just getting started with this AWESOME feature, you must watch the video, NOW. See it below or [head to my YouTube channel](https://youtu.be/ZZ-UGMztoqo)
.

Download Slicer Examples Workbook
---------------------------------

This post is very long and has many examples. **[Please click here to download slicer examples demo workbook](https://chandoo.org/wp/wp-content/uploads/2021/11/slicers.xlsx)
.** It contains all the examples shown in this post and a fun surprise too.

### How to insert a slicer?

Note: Slicers are available only in Excel 2010 and above.

**Adding a slicer in Excel 2010:**

In Excel 2010, you can add a slicer only to pivot tables. To insert a slicer, go to either,

*   Insert ribbon and click on Insert Slicer
*   or Options ribbon (PivotTable Tools) and click on Insert Slicer

**Adding a slicer in Excel 2013 / 2016 / 2019 / 365:**

In Excel 2013 and above, you can add a slicer to either pivot tables or regular tables.

_**Adding slicers to regular tables:**_

When you add a slicer to regular Excel tables, they just act like auto-filters and filter your table data. To add a slicer to regular table, use Insert ribbon > Insert Slicer button.

_**Adding slicers to Pivot tables:**_

To add a slicer, you can do either of these things:

*   Right click on pivot table field you want and choose “add as slicer”  
    ![Add as slicer from Pivot table fields list](https://img.chandoo.org/pivot/slicers/insert-slicer-from-pivot-table-fields.png)
*   Use either analyze or insert ribbon to add the slicer.  
    ![Insert a slicer from Pivot Table Analyze Ribbon](https://img.chandoo.org/pivot/slicers/insert-slicer-from-analyze-ribbon.png)

Single vs. Multi-selection in Slicers
-------------------------------------

You can select a single item or multiple items in slicers. To multi-select,

*   If the items you want are together, just drag from first item to last.
*   If the items you want are not together, hold CTRL key and click on one at a time.
*   You can also click on the “checkbox” icon in slicer header to multi-select items in slicers.

Creating interactive charts with slicers
----------------------------------------

Since slicers talk to Pivot tables, you can use them to create cool interactive charts in Excel. The basic process is like this:

1.  Set up a pivot table that gives you the data for your chart.
2.  Add slicer for interaction on any field (say slicer on customer’s region)
3.  Create a pivot chart (or even regular chart) from the pivot table data.
4.  Move slicer next to the chart and format everything to your taste.
5.  And your interactive chart is ready!

### **Demo of interactive chart using slicer:**

Here is a quick demo.

![Creating interactive charts using Excel slicers - demo](https://img.chandoo.org/pivot/slicers/interactive-chart-with-slicers.gif)

### Linking multiple slicers to same Pivot report

You can add any number of slicers to a pivot report. When you add multiple slicers, each of them plays a role in telling the pivot table what sub-set of data to use for calculating the numbers.

![Multiple slicers linked to one pivot table - explanation](https://img.chandoo.org/pivot/slicers/multiple-slicers-linked-to-one-pivot.png)

### Linking one slicer to multiple pivot tables

You can also link a single slicer to any number of pivot reports. This allows us to build very powerful, cross-filtered & interactive reports using Excel.

To connect multiple pivot tables to single slicer, follow these steps.

1.  **_Optional:_ Give names to each of the pivot tables.** To name the pivot tables, click anywhere in the pivot, go to Analyze ribbon and use the pivot table name field on top-left to give it a name.
    1.  If you don’t name your pivot tables, Excel will give them default names like PivotTable73. This can be confusing once you have more than a few pivot tables.
2.  Right click on the slicer and go to Report Connections (in Excel 2010, this is called as PivotTable connections).  
    ![Report connections - linking slicers to more than one pivot table report](https://img.chandoo.org/pivot/slicers/slicer-report-connections.png)
3.  Check all the pivot tables you want. Click ok.  
    ![Linking multiple pivot tables to a slicer in Excel - how to](https://img.chandoo.org/pivot/slicers/linking-slicers-to-multiple-pivot-tables.png)

Now both pivot tables will respond to the slicer. See this demo:

![Slicer linked to multiple pivot tables - Excel demo](https://img.chandoo.org/pivot/slicers/slicer-multiple-report-connections-demo.gif)

### Linking slicers to more than one chart

You can use the same approach to link one slicer to more than one chart (pivot chart or regular one).

See this demo:

![Multiple interactive charts with slicers - demo](https://img.chandoo.org/pivot/slicers/multiple-interactive-charts-with-slicers-demo.gif)

_You can examine this chart in detail in the **[Slicer Examples workbook](https://chandoo.org/wp/wp-content/uploads/2021/11/slicers.xlsx)
.**_

Capturing slicer selection using formulas
-----------------------------------------

While slicers are amazing & fun, often you may want to use them outside pivot table framework. For example, you may want to use slicers to add interactivity to your charts or use them in your dashboard.

When you want to do something like that, you essentially want the _slicers to talk to your formulas_. To do this, we can use 2 approaches.

*   Dummy (or harvester) pivot table route
*   CUBE formulas route

### **Dummy pivot table route**

This is the easiest way to capture slicer selection into a cell. Using a dummy pivot table, we can find out which items are selected in slicers and use them for some other purpose, like below:

![Capturing slicer selection with Excel formulas - demo](https://img.chandoo.org/pivot/slicers/capture-slicer-selection-with-formulas-demo.gif)

The process is like this:

*   Let’s say you want to know which profession is picked up in the slicer (_so that you can use it in some formulas or charts)._
*   Create another pivot table.
*   Add the profession field to row labels area.
*   Link the slicer to this new pivot table as well (using report connections feature of slicer)
*   Now when you click on the slicer, both original pivot and this new dummy pivot change.
*   Access row labels like regular cells in your formulas to find out which slicer item is selected.

**See this illustration to understand how to set up the formulas:**

![How to find out which items are clicked on slicers using Excel formulas - Explanation](https://img.chandoo.org/pivot/slicers/capture-slicer-selection-formulas.png)

### **CUBE Formula approach:**

This is relevant only if your slicers are hooked up to a data model thru something like Power Pivot, SAS Cubes or _ThisWorkbookModel_ in Excel 2013 or above.

To find out slicer selection, we need to **use CUBERANKEDMEMBER() Excel formula** like this:

\=CUBERANKEDMEMBER(“ThisWorkbookDataModel”, Name\_of\_the\_slicer , item\_number)

Let’s say you have a slicer on Area field, and its named Slicer\_Area (you can check this name from Slicer properties)

To get the first item selected in the slicer, you can use CUBERANKEDMEMBER formule like this:

\=CUBERANKEDMEMBER(“ThisWorkbookDataModel”, Slicer\_Area, 1)

This will return the first item selected on slicer. If there is no selection (ie you have cleared the filter on slicer), the Excel will return “All”.

**Bonus tip:** You can use =CUBESETCOUNT(Slicer\_Area) to count the number of items selected in slicer.

**Bonus tip#2:** By combining CUBESETCOUNT and CUBERANKEDMEMBER formulas, you can extract all the items selected in the slicer easily.

[**Please download Cube Formula Slicer Selection example workbook**](https://img.chandoo.org/pivot/slicers/cube-formula-slicer-selection.xlsx)
 to learn more about this approach.

Note: this file works only in Excel 2013 or above.

Formatting slicers
------------------

Slicers are fully customizable. You can change their look, settings and colors easily using the slicer tools options ribbon.

![Slicer formatting - Demo](https://img.chandoo.org/pivot/slicers/slicer-formatting-demo.png)

Here is a quick FAQ on slicer formatting:

**Q. I have too many items in slicer. How to deal with this problem?**

Simple. See if you can set up your slicer in multiple columns. You can also adjust the height and width of slicer buttons to suit your requirements. If your slicer is still too big, you can adjust the font size of slicer by creating a new style.

![Setting up slicers in multiple columns etc.](https://img.chandoo.org/pivot/slicers/slicer-formatting-columns-etc.png)

**Q. I don’t like the blue color of slicer. What do I do?**

You can switch to another color scheme. Just go to Slicer Tools Options ribbon and pick a style you want.

![Slicer styles and colors](https://img.chandoo.org/pivot/slicers/slicer-styles.png)

_Pro tip: You can create your own style to customize all aspects of a slicer._

**Q. I don’t like the title on slicer. Can I get it rid of it?**

Yes you can. Right click on the slicer and go to “Slicer Settings”. Uncheck _display header_ option to remove the header & clear filter button.

![Removing the headers & items with no data in slicers](https://img.chandoo.org/pivot/slicers/slicer-formatting-removing-header-and-hiding-items.png)

**Q. My slicer keeps showing old products (or categories etc.) that are no longer part of data after refresh. What do I do?**

Simple. Right click on the slicer and choose “Slicer settings”. Check _Hide items with no data_ option.

**Q. I want to make my slicers look good. But I don’t know where to start…**

[Here is an inspiration for you](https://chandoo.org/wp/switch-scenarios-dynamically-using-slicers/)
.

Slicers vs. Report Filters
--------------------------

In a way slicers are like report filters, but _way better_. (Related: [Introduction to Pivot Table Report Filters](http://chandoo.org/wp/2011/04/20/pivot-table-report-filters/)
)

There are few key differences between both.

*   Report filters are tied to single pivot tables. Slicers can be linked to any number of pivots.
*   Report filters are clumsy to work with. Slicers are very easy to use.
*   Report filters may not work very well in a touch screen environment. Slicers are great for touch screen UIs.
*   Report filters take up one cell per filter. Slicers take up more space on the worksheet UI.
*   Report filters can be automated with simple VBA. Slicers require a bit more code to automate.
*   You can access report filter values using simple cell references. Slicer values can be extracted using either dummy pivot tables or CUBE formulas, both of which require extra effort.

Slicers vs. Timelines:
----------------------

If you have a date field in your data, you can also insert a “timeline”. this is a special type of slicer, that works only with date values.

_**Here is a quick demo of Timeline slicer.**_

![Excel timelines quick demo](https://chandoo.org/wp/wp-content/uploads/2021/11/Excel-timelines-quick-demo.gif)

You can also customize the look & feel of Excel Timelines.

The download workbook has an example of timelines.

Slicers & Compatibility
-----------------------

Slicers are compatible with Excel 2010 & above versions of Excel. You can also use Slicers with Excel Online.

If you create a workbook in Excel 2010 (or above) with slicers and email it to a friend using Excel 2007, they will see an empty box where slicer should be.

Slicers work on desktop & web versions of Excel in the same way.

### Download Slicer Examples Workbook

**[Please click here to download slicer examples demo workbook](https://chandoo.org/wp/wp-content/uploads/2021/11/slicers.xlsx)
.** It contains all the examples shown in this post and a fun surprise too.

Also download the [Cube formulas approach for slicer selection extraction workbook](https://img.chandoo.org/pivot/slicers/cube-formula-slicer-selection.xlsx)
 to learn that technique.

### Additional Resources to learn about Slicers

If you like slicers and want to learn creative ways to use them in your work, check out below examples:

*   [Create a fully dynamic dashboard using Pivot Tables & slicers](http://chandoo.org/wp/dynamic-dashboard-video-tutorial/)
    
*   [Use slicer as scenario selection mechanism](http://chandoo.org/wp/switch-scenarios-dynamically-using-slicers/)
    
*   [Slicers + charts for awesome user experience – case study](http://chandoo.org/wp/tax-burden-chart-excel/)
     & [one more](http://chandoo.org/wp/network-relationship-chart/ "interactive network relationships chart with Excel")
    
*   Related: [Introduction to Excel Relationships & Data Model](http://chandoo.org/wp/introduction-to-excel-2013-data-model-relationships/)
    
*   Related: [Introduction to Excel Pivot Tables](http://chandoo.org/wp/excel-pivot-tables-tutorial/)
    
*   Related: [Introduction to Excel Report Filters](http://chandoo.org/wp/pivot-table-report-filters/)
    
*   Related: [Advanced Pivot Table Tips & Tricks](https://chandoo.org/wp/advanced-pivot-tables/)
    

### Do you use Slicers? What are your favorite tips about slicers?

As mentioned earlier, slicers are one of my favorite features of Excel. I use them liberally in my dashboards, charts & workbooks.

**What about you?** Do you use slicers? When do you use them? What are your favorite tips when it comes to using slicers? Please share in the comments area.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [49 Comments](https://chandoo.org/wp/introduction-to-slicers/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introduction-to-slicers/#respond)
    
*   Tagged under [advance](https://chandoo.org/wp/tag/advance/)
    , [CUBE Formulas](https://chandoo.org/wp/tag/cube-formulas/)
    , [data model](https://chandoo.org/wp/tag/data-model/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [excel 2013](https://chandoo.org/wp/tag/excel-2013/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [relationship](https://chandoo.org/wp/tag/relationship/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousCalculating Billy’s total working hours \[solution & discussion\]](https://chandoo.org/wp/calculating-billys-total-working-hours/)

[NextCP037: Error error on the wall, How do I fix you all? – Understanding & Fixing Excel ErrorsNext](https://chandoo.org/wp/cp037-excel-errors/)

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
    
    [Reply](https://chandoo.org/wp/introduction-to-slicers/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introduction-to-slicers/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introduction-to-slicers/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
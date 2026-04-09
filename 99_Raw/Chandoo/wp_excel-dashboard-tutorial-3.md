# Making a Dynamic Dashboard in Excel [Part 3 of 4] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-dashboard-tutorial-3

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Making a Dynamic Dashboard in Excel \[Part 3 of 4\]
===================================================

*   Last updated on May 26, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This is a guest post by _**Myles Arnott**_ from [Clarity Consultancy Services – UK](http://www.clarityconsultancyservices.co.uk/)
.

*   Part 1: [Introduction & overview](http://chandoo.org/wp/2010/03/16/excel-dashboard-tutorial-1/)
    
*   Part 2: [Dynamic Charts in the Dashboard](http://chandoo.org/wp/2010/03/30/excel-dashboard-tutorial-2/)
    
*   Part 3: **VBA behind the Dynamic Dashboard a simple example**
*   Part 4: [Pulling it all together](http://chandoo.org/wp/2010/05/26/excel-dashboard-tutorial-4/)
    

**In this post we are going to look at a simple example of the VBA behind the Dynamic Dashboard.** Essentially we will learn to write macros for doing this:

![Moving Charts in Dynamic Dashboard using VBA](https://chandoo.org/img/ed/moving-objects-with-vba.gif)

The dynamic dashboard VBA example can be downloaded [here](https://chandoo.org/wp/excel-dashboard-tutorial-3/chandoo.org/img/ed/dynamic-dashboard-vba-example.xls)
 \[[Mirror](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/dynamic-dashboard-vba-example.xls)\
\]

### Some VBA essentials

**Defining variables:**  
First we need to define variables “left” and “top” as integers.  
`Dim left As Integer   Dim top As Integer`

**Next we need to set a value for these variables.** To do this I have created two named ranges in the Excel file called Left and Top. To make variable “left” equal to named range Left:  
`left = Range("Left").Value`

and the equivalent for variable “top”  
`top = Range("Top").Value`

**Finally select the shape:**  
`ActiveSheet.Shapes("Rounded Rectangle 1").Select`

**And define its position:**  
`Selection.ShapeRange.top = top   Selection.ShapeRange.left = left`

### So the full code is:

    Sub move_Image()
    Dim left As Integer
    Dim top As Integer
    
    'Define the position values
    
    left = Range("Left").Value
    top = Range("Top").Value
    
    'Select the shape and position it
    ActiveSheet.Shapes("Rounded Rectangle 1").Select
    Selection.ShapeRange.top = top
    Selection.ShapeRange.left = left
    End Sub

This code can be viewed by clicking on macros in the file.

![Assign Macro to Rounded Rectangle Shape so that the Position is adjusted whenever you click on it](https://chandoo.org/img/ed/assign-macro-dynamic-dashboard-excel.png)

Once you have the code ready, you should assign it to the Rounded Rectangle 1, so that whenever you click on the rounded rectangle, the code is run.

### What it does

In the [downloadable file](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/dynamic-dashboard-vba-example.xls)
 in Sheet1, enter values against the Top and Left positions in the input area (blue). Click on the shape to move it to the position you have defined.

### How it works

Clicking on the shape runs macro “move\_Image”.  
The value for the position of the shape is linked from the named range to the variable.  
The macro uses Selection.ShapeRange.top and Selection.ShapeRange.left to determine the position of the shape based on the variable value.

### What Next?

We now know how to move objects using VBA. In the final part of the series learn [how to pull all this together to create the dashboard](http://chandoo.org/wp/2010/05/26/excel-dashboard-tutorial-4/)
.

### Download the complete dashboard

Go ahead and download the dashboard excel file. The dynamic dashboard can be downloaded [here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.xlsm)
 \[[mirror](http://chandoo.org/img/ed/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
, [ZIP Version](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
\]

It works on Excel 2007 and above. You need to enable macros and links to make it work.

### Added by PHD:

Myles has taken various important concepts like Microcharts, form controls, macros, camera snapshot, formulas etc and combined all these to create a truly outstanding dashboard. I am honored to feature his ideas and implementation here on PHD. I have learned several valuable tricks while exploring his dashboard. I am sure you would too.

**If you like this tutorial please say thanks to Myles.**

### Related Material & Resources

*   [Excel Dynamic Charts – Tutorials, Examples and Demos](http://chandoo.org/wp/tag/dynamic-charts)
    
*   [Excel Dashboards – Tutorials & Templates Section of PHD](http://chandoo.org/wp/management-dashboards-excel/)
    
*   [6 Part Tutorial on Making KPI Dashboards in Excel](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    

This is a guest post by _**Myles Arnott**_ from [Clarity Consultancy Services – UK](http://www.clarityconsultancyservices.co.uk/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/excel-dashboard-tutorial-3/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-dashboard-tutorial-3/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [charts](https://chandoo.org/wp/tag/charts/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [excel drawing](https://chandoo.org/wp/tag/excel-drawing/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [kpi dashboards](https://chandoo.org/wp/tag/kpi-dashboards/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousBudget vs. Actual Profit Loss Report using Pivot Tables](https://chandoo.org/wp/budget-v-actual-profit-loss-reports-6/)

[NextWhat are your favorite colors for charts?Next](https://chandoo.org/wp/chart-colors-poll/)

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
    
    [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-3/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-3/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-3/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# Stacked Bar and Indicator Arrow Chart - Tutorial » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/stacked-bar-and-indicator-arrow-chart-tutorial

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Stacked Bar and Indicator Arrow Chart – Tutorial
================================================

*   Last updated on September 14, 2016

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Last week in the Chandoo.org Forums, I was asked could I reproduce the chart below in Excel

[![SBA01](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA01.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA01.png)

Which I did.

This post will describe how to tackle this chart step by step.

You can follow along using some sample data: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2016/09/Stacked-bar-chart-with-Arrow.xlsx)

### **Data**

To produce this chart we are going to use an Excel Stacked Bar chart with two series of data

The first Series will be for the Colored Bars

The second series is for the Arrow and the gap to the left of the arrow

[![SBA02](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA02.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA02.png)

The data required is shown in the above table

The Arrow Value is an input and is the value the Arrow will point to

The data is the values for the colored bars

The Arrow is two calculations that setup the Arrow, the 58 is the offset from zero to the left side of the arrow

The 4 is the width of the arrow. That is the arrow will point to 60 = 58 + 4 /2

The Cumulative Data is required for the Legend

### Chart

In **Excel 2016**

Select the range C3:G4 and goto Insert Chart

Select Bar, Stacked Bar

[![SBA04](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA04.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA04.png)

**In Excel 2010**

Select the range C3:G4 and goto Insert Chart

Select Bar, Stacked Bar

[![sba21](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA21.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA21.png)

Now with the Chart selected goto the Chart Tools, Design Tab

Click on the Switch Row/Column Tab

[![sba22](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA22.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA22.png)

**Excel All Versions**

You should now have a chart like:

[![SBA05](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA05.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA05.png)

Bar 1 is the data and Bar 2 will become the arrow

We don’t need the Charts Title, Legend, Grid Lines or Axis, so select each and press Delete

[![SBA06](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA06.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA06.png)

Next we will add an arrow

The Arrow will be placed as a Fill in the Upper Orange Bar

Select a Blank Cell eg: I3

Then goto the Insert, Shapes Menu and select an Isosceles Triangle

[![SBA07](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA07.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA07.png)

Fill the Arrow with what ever color you want and drag the Handle down so that the arrow points down

[![SBA08](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA08.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA08.png)

To insert the arrow, select the Arrow and press Copy (Ctrl+C)

Now select the Chart and click on the Upper Orange Bar, click on it again until it is the only Bar with Handles Showing, the press Paste (Ctrl+V)

[![SBA09](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA09.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA09.png)

[![SBA10](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA10.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA10.png)

Now select the Upper Blue Bar and set its fill and outline to None

Right Click on any Bar and select Format Data Series

Set the Series Overlap to 100% and set the Gap Width to 0%

[![SBA12](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA12.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA12.png)

Now click on the chart, just above the Blue Bar

When the Resize Handles appear, drag them to resize the chart so that the gap between the Top and Bottom Bars is none

[![SBA13](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA13.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA13.png)

We can now add the labels

Select the Orange Bar and then Select it again until it is the only Bar with Handles

Right Click on it and Add Data Label

[![SBA14](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA14.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA14.png)

Now click on the new Data Label and click on it again until the Handles change as shown below

[![SBA15](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA15.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA15.png)

Now in the Formula Bar enter =Chandoo.org!$C$5 and apply

Right click on the Data Label and select Format Data Labels

Set the Label Position to Inside Base

[![SBA16](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA16.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA16.png)

Now repeat for each of the other Bars

[![SBA17](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA17.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA17.png)

and Finally add a Label to the arrow linking it to cell C2. You have to manually drag the Label to above the arrow.

### Conclusion

Now that you know how to make a Bar Chart with Indicator Arrow, it should take you less than a minute to copy the bar chart, convert it to a Column chart and reformat it to a Column Chart with arrow as shown below

[![SBA18](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA18.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/SBA18.png)

I hope you enjoyed the above tutorial

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [22 Comments](https://chandoo.org/wp/stacked-bar-and-indicator-arrow-chart-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/stacked-bar-and-indicator-arrow-chart-tutorial/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [Bar Chart](https://chandoo.org/wp/tag/bar-chart/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [combination charts](https://chandoo.org/wp/tag/combination-charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [stacked bar](https://chandoo.org/wp/tag/stacked-bar/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousTell me about an analysis problem that you couldn’t solve with Excel?](https://chandoo.org/wp/tricky-analysis-problems-poll/)

[NextSara’s Copy Shop – Break even analysis and what-if modeling in Excel \[Videos\]Next](https://chandoo.org/wp/saras-copy-shop/)

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
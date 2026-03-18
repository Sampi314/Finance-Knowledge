# Visualizing KPI Distributions thru Box Plots - KPI Dashboards using Excel

**Source:** https://chandoo.org/wp/box-plots-excel-dashboards-tutorial

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Adding Box Plots to Show Data Distribution in Dashboards \[Part 6 of 6\]
========================================================================

*   Last updated on January 19, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This is a Guest Post by _**[Robert](http://www.clearlyandsimply.com/)
**_ on Visualization Techniques for Excel KPI Dashboards.

### This 6 Part Tutorial on Management Dashboards Teaches YOU:

[Creating a Scrollable List View in Dashboard](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
  
[Add Ability to Sort on Any KPI to the Dashboard](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
  
[Highlight KPIs Based on Percentile](http://chandoo.org/wp/2008/09/03/excel-kpi-dashboard-percentile-3/)
  
[Add Microcharts to KPI Dashboards](http://chandoo.org/wp/2008/09/10/kpi-dashboards-graphs-excel/)
  
[Compare 2 KPIs in the Dashboards Using Form Controls](http://chandoo.org/wp/2008/10/09/excel-dashboard-visualization-techniques-1/)
  
[](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)
Show the Distribution of a KPI using Box Plots

In this final post we will learn **how to add a box plot to show the distribution of values**

The solution
------------

The most common way in descriptive statistics to visualize the distribution of sets of numerical data is a [box plot](http://en.wikipedia.org/wiki/Box_plot)
. But according to my experience in day to day business, most business people are not familiar with this type of visualization.  
Therefore we try to create a simpler chart which is hopefully easier to understand:

![](https://chandoo.org/wp/wp-content/uploads/2008/10/box-plot-excel-dashboard-visualization.png "box-plot-management-dashboard-visualization")

The light grey bar visualizes the range of all values, the dark grey bar the range of the 10 items displayed on the management dashboard table. The cross shows the total average and – similar to the bullet graphs – the vertical line represents the target. This is less information than a real box whisker plot would provide, but I guess it will be easier to understand.

The implementation
------------------

Download the **[Excel KPI dashboard final workbook](https://chandoo.org/wp/wp-content/uploads/2008/10/kpi-dashboard-revisited-ii.zip)
** and read on how to create a simplified box plot.

1.  Let’s bring our ducks in a row first. Calculate all necessary data to be shown in the box plots: the minimum and maximum of the total data and of the 10 displayed items on the dashboard, the average and the target. The formulas are quite simple. You can find them in the downloaded workbook in `calculation!AZ23:BE27.`
2.  The basis of our visualization is a stacked bar chart with only one category and 4 data series:
    
    1.  the invisible bar (the bar between 0 and the total minimum),
    2.  the left light grey bar (the bar between the total minimum and the minimum of the displayed 10 items),
    3.  the dark grey bar (the bar between the minimum and maximum of the 10 displayed values) and
    4.  the right light grey bar (the bar between the maximum of the 10 displayed items and the total maximum).
    
    Again the formulas to calculate these values are quite simple (see calculation!BF23:BI27).  
    ![](https://chandoo.org/wp/wp-content/uploads/2008/10/box-whisker-plot-excel-data.gif "box-whisker-plot-excel-data")
    
3.  Create a stacked bar chart and format the bars accordingly (no fill color and no border for the invisible bar, light and dark grey fill colors for the other bars).
4.  Add the average and the target values as additional series to the chart and change the chart type of these new series to XY scatter charts (X is the average / target value, Y is a dummy 1). Format the average as a cross (or whatever you choose) and use the error bars to format the target as a vertical line. The method of creating a combination chart of bars and XY scatters is pretty much the same we used in the 4th post of the KPI dashboard series ([here](http://chandoo.org/wp/2008/09/10/kpi-dashboards-graphs-excel/)
    ).
5.  Remove or hide all unnecessary chart elements: no fill color and no border for plot or chart area; no line, tick marks etc. for the vertical axes, etc.
6.  Repeat steps 3 to 5 to create charts for all 5 KPI.
7.  Bring the charts to the dashboard, position them and add a caption to explain the chart elements.

That’s it. Play around with the new feature: change the sort criteria or sort order or scroll up and down the dashboard table and see how the new charts are changing.

Final Remark
------------

This is a simplified version of box plot visualization and works only for data sets with positive values. Of course there is also a more sophisticated way of creating charts like this for any data (positive and negative values, i.e. bars crossing the vertical axis). This is a bit more complicated since you need 8 data series for the bar chart instead of 4 but the principle is exactly the same.

Our final KPI dashboard looks like this (click on it for a larger version):

[![](https://chandoo.org/wp/wp-content/uploads/2008/10/excel-dashboard-small.gif "excel-management-dashboard-small")](https://chandoo.org/wp/wp-content/uploads/2008/10/excel-dashboard-large.png)

What’s next?
------------

With this last part I guess the time may have come to end the series about [Excel Management KPI Dashboards](http://chandoo.org/wp/tag/kpi-dashboards-posts/)
 here and to hand over the further development of this dashboard to the readers of Chandoo.org.  
I do hope the series of 6 posts have been useful for your daily work and provided new ideas. Make sure you have downloaded the [Excel KPI dashboard tutorial workbook](https://chandoo.org/wp/wp-content/uploads/2008/10/kpi-dashboard-revisited-ii.zip)
  
**Thanks for all your comments and appreciations.**  
Last but not least: Chandoo, my friend, once more thank you so much for hosting my ideas at Chandoo.org.  
_Kind regards from Munich  
[Robert](http://www.clearlyandsimply.com/)
_

Chandoo’s note
--------------

If not for Robert’s mail in August suggesting these wonderful ideas as posts in PHD, I would never have learned these things or shared them with you all. I am thankful to him for that.

Well, I am constantly trying to learn new dashboard techniques and I will try to share the worthy ones with you all. Meanwhile if you have a good idea for excel dashboards (or charts, techniques etc.) and would like to share with everyone, feel free to drop a comment or write to me. I will be \*happy\* to feature your ideas.

Further Reading on Dashboards using Excel
-----------------------------------------

Checkout our exclusive section: **[Excel Dashboards](http://chandoo.org/wp/excel-dashboards/)
** for more tutorials, tips, design principles.  
You can also **consider joining my [Excel School](http://chandoo.org/wp/excel-school/)
 program** to learn how to make world-class dashboards.

[![Learn How to make Excel Dashboards - Join Excel School](https://cache2.chandoo.org/content/learn-excel-dashboards-es-4.2.png)](http://chandoo.org/wp/excel-school/ "Learn How to Make Excel Dashboards - Join Excel School Online Training Program by Chandoo")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [27 Comments](https://chandoo.org/wp/box-plots-excel-dashboards-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/box-plots-excel-dashboards-tutorial/#respond)
    
*   Tagged under [box plots](https://chandoo.org/wp/tag/box-plots/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts & Graphs](https://chandoo.org/wp/tag/charts-graphs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [distributions](https://chandoo.org/wp/tag/distributions/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tutorial](https://chandoo.org/wp/tag/tutorial/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousMaking Pie-charts look Sexy – The CNN’s tax burden analysis chart](https://chandoo.org/wp/better-pie-chart-example/)

[NextSoon you can use Excel on the WebNext](https://chandoo.org/wp/soon-you-can-use-excel-on-the-web/)

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
    
    [Reply](https://chandoo.org/wp/box-plots-excel-dashboards-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/box-plots-excel-dashboards-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/box-plots-excel-dashboards-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# KPI Dashboards in Microsoft Excel - Highlighting KPIs based on Percentiles [Part 3 of 6]

**Source:** https://chandoo.org/wp/excel-kpi-dashboard-percentile-3

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

KPI Dashboards – Highlight KPIs Based on Percentile \[Part 3 or 6\]
===================================================================

*   Last updated on January 19, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Creating KPI Dashboards in Microsoft Excel is a series of 6 posts** by [**_Robert_**](http://www.clearlyandsimply.com/)
 from Munich, Germany.

### This 6 Part Tutorial on KPI Dashboards Teaches YOU:

[Creating a Scrollable List View in Dashboard](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
  
[Add Ability to Sort on Any KPI to the Dashboard](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
  
[](http://chandoo.org/wp/2008/09/03/excel-kpi-dashboard-percentile-3/)
Highlight KPIs Based on Percentile  
[Add Microcharts to KPI Dashboards](http://chandoo.org/wp/2008/09/10/kpi-dashboards-graphs-excel/)
  
[Compare 2 KPIs in the Dashboards Using Form Controls](http://chandoo.org/wp/2008/10/09/excel-dashboard-visualization-techniques-1/)
  
[Show the Distribution of a KPI using Box Plots](http://chandoo.org/wp/2008/10/29/box-plots-excel-dashboards-tutorial/)

* * *

The challenge – Adding Percentile Information
---------------------------------------------

![scroll-dashboard-kpi-excel-1](https://chandoo.org/wp/wp-content/uploads/2008/08/scroll-dashboard-kpi-excel-1.png "scroll-dashboard-kpi-excel-1")Let’s get back to our last week’s KPI dashboard example: [Adding sort options to excel dashboards](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
. In today’s post we want our dashboard to take a step forward by adding another data analysis feature. Up to now the user is able to view a window of 10 rows out of a much larger list and to sort by any given decision parameter. But the KPI dashboard falls short if we want to evaluate the performance of the displayed items regarding the other 4 KPIs.

Imagine we are at the top of the list and the table is sorted by KPI 1 (see left). **We see that “Product Name 36” is the TOP performer regarding KPI 1. But how does it perform regarding KPI 3?** The value of 2% is probably rather poor, but how poor? Sure, we can change the sort order to KPI 3 and scroll down until we find product 36 and look at the ranking in the first column. But changing the sort order back and forth is in-convenient, time-consuming and not user-friendly.

The solution
------------

![management-dashboard-with-quartile-info](https://chandoo.org/wp/wp-content/uploads/2008/08/kpi-dashboard-with-quartile-info.png "management-dashboard-with-quartile-info")

One statistical method to examine a list of data is the percentile. A percentile is the value of a variable below which a certain percent of observations fall ([more](http://en.wikipedia.org/wiki/Percentile)
). The 10% percentile of our list of values for KPI 3 returns the threshold at which 10% of all values are smaller than this threshold. We will use this method to classify the values of the KPIs that are not selected as the sort criteria by highlighting the values above the 90% percentile in green (10% best performers) and by highlighting the values below the 10% percentile in red (10% poorest performers).

After the highlighting we are now able to see immediately that Product 36 is best in class regarding KPI 1 but it belongs to the poorest 10% of all products regarding KPI 3.

**[Download the Excel file with KPI Dashboards](https://chandoo.org/wp/wp-content/uploads/2008/09/dashboard-table-scroll-sort-and-brush-v2.xls)
** and read on below how it is done.

The implementation
------------------

Implementation needs a simple [conditional formatting](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
 and the excel spreadsheet function PERCENTILE. The syntax of this function is `PERCENTILE (array, k)`, where ‘array’ is the range with the data and ‘k’ is the percentile value in a range between 0 and 1. `PERCENTILE (A1:A100, 0.10)` returns the threshold at which 10% of all values in the range are smaller than this value and the remaining 90% are larger than this value.

**Here is the description how to change the workbook:**

1.  Add two additional rows to the data worksheet to define the upper and lower percentile value.
2.  Insert five new columns on the dashboard each of them right to the existing column with the data.
3.  To simplify the formula, insert the number of each KPI in the cells below the header (F6 = 1; H6 = 2, and so on).
4.  ![how-quartile-percentile-calculated-excel](https://chandoo.org/wp/wp-content/uploads/2008/08/how-quartile-percentile-calculcated-excel.png "how-quartile-percentile-calculated-excel")Fill the new columns with the following formula (example for cell G8):`=IF (mySortCriteria=F$6,"",   IF (F8>PERCENTILE (Calculation!$K$10:$K$109,Data!$E$5),"<+",   IF (F8<-","")))`
    
    If the actual column is the one the table is sorted by, a blank would be returned. Otherwise: if the value  
    in the cell left is larger than the e.g. 90% percentile, “<+”, if the value is smaller than the 10% percentile “<-” will be returned. For all other values the result of the formula is a blank.
    
5.  ![conditional-formatting-dashboard-percentile-indicator](https://chandoo.org/wp/wp-content/uploads/2008/08/conditional-formatting-dashboard-percentile-indicator.png "conditional-formatting-dashboard-percentile-indicator")  
    Format the new columns with a red font color and add additional formatting that changes the font color to green if the cell value is “<+”.
6.  Finally add a caption under the table to help the user understand what the triangles are representing.

Final remarks
-------------

If you don’t like the triangles, you could easily replace them by a dot or a diamond or whatever you choose. Or you might want to change the colors or put the triangles to the left of the columns instead of the right. If you don’t like the extra columns next to the data, you could also use the described formula to conditionally format the cells with the data (e.g. with red and green fill color).

What’s next?
------------

[Make sure you have downloaded the KPI Dashboards XLS files – Click here](https://chandoo.org/wp/wp-content/uploads/2008/09/dashboard-table-scroll-sort-and-brush-v2.xls)

Up to now we have limited our dashboard to texts and numbers. Of course graphical visualization can always add much value for analysis. See next post: **[Part 4: Add Microcharts to KPI Dashboards](http://chandoo.org/wp/2008/09/10/kpi-dashboards-graphs-excel/)
**

Also, Checkout our [Excel Dashboards Page](http://chandoo.org/wp/excel-dashboards/)
 for more examples and resources.

* * *

_Chandoo’s note: **Robert** is a regular reader of this blog, please leave your comments, questions, appreciations here and he will respond._

[![Learn How to make Excel Dashboards - Join Excel School](https://cache2.chandoo.org/content/learn-excel-dashboards-es-4.2.png)](http://chandoo.org/wp/excel-school/ "Learn How to Make Excel Dashboards - Join Excel School Online Training Program by Chandoo")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [39 Comments](https://chandoo.org/wp/excel-kpi-dashboard-percentile-3/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-kpi-dashboard-percentile-3/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [Charts & Graphs](https://chandoo.org/wp/tag/charts-graphs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [free](https://chandoo.org/wp/tag/free/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [quartile](https://chandoo.org/wp/tag/quartile/)
    , [spreadsheet](https://chandoo.org/wp/tag/spreadsheet/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious6 charts you will see in hell](https://chandoo.org/wp/6-charts-to-never-use/)

[NextMicrocharting in Excel – 7 Alternatives ReviewedNext](https://chandoo.org/wp/microcharting-excel-howto/)

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
    
    [Reply](https://chandoo.org/wp/excel-kpi-dashboard-percentile-3/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-kpi-dashboard-percentile-3/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-kpi-dashboard-percentile-3/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
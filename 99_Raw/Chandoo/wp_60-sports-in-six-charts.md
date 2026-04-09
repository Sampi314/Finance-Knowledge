# 60 sports in six Excel charts - Case study in comparing large data sets

**Source:** https://chandoo.org/wp/60-sports-in-six-charts

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

60 sports in six charts
=======================

*   Last updated on June 10, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

On twitter I follow many charting and visualization related accounts. One of them is [@Andy Kriebel](https://twitter.com/VizWizBI)
, who runs _**Makeover Monday**_. The idea is simple. Every Monday they publish a data-set and ask the community to visualize. Last Monday (7th May, 2018), they have published about **toughest sport by skill** data. This categorizes 60 sports by 10 skill categories to find out which sport is the toughest. Over the weekend, Andy posted [a summary of all toughest sport viz entries](https://www.makeovermonday.co.uk/week19-2018/)
. Many of the entries are made in Tableau. I thought it would be a fun challenge to re-create some of these charts in Excel. The result is this post. **60 sports in 6 charts.** Check out the charts and download workbook to learn more.

First four charts are re-creations of Tableau designs. Last two are mine.

### Chart 1: Scatter plot with random dots

Design by [Andreas Szesztai](https://t.co/apfLaHpuRL)
 ([@](https://twitter.com/AndSzesztai)
)

**Techniques used:**

*   Scatter plot with marker transparency and randomized position ([jitter](https://chandoo.org/wp/2017/08/17/visualize-salary-increases-jitter-plot/)
    )
*   [Drop down form control](https://chandoo.org/wp/2011/03/30/form-controls/)
     for sport selection
*   XY series for labels and boxes ([shape as marker](https://chandoo.org/wp/2015/08/08/shapes-in-charts/)
    )

**Snapshot** (click to enlarge):  
[![Chart 1: Scatter plot with random dots](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-1-demo-60-sports-in-6-charts.png)](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-1-demo-60-sports-in-6-charts.png)

### Chart 2: Scatter plot with skill comparison

Design by [Mark Bradbourne](https://public.tableau.com/views/ESPNSportSkills/ESPNSportSkills?:embed=y&:display_count=yes)
 ([@](https://twitter.com/MarkBradbourne)
)

**Techniques used:**

*   Scatter plot with marker transparency
*   [Drop down form control](https://chandoo.org/wp/2011/03/30/form-controls/)
     for sport selection
*   [Slicers](https://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
     for skill comparison

**Snapshots:**

![Chart 2: Scatter plot with skill comparison - top half](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-2-demo-60-sports-in-6-charts.png)  
![Chart 2: Scatter plot with skill comparison - bottom](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-2-bottom-demo-60-sports-in-6-charts.png)

### Chart 3: Bar code graph

Design by [Lilian Hoang](https://public.tableau.com/views/SportbySkill/SimpleSkills-Sport?:embed=y&:display_count=yes)
 ([@](https://twitter.com/Lilianhx)
)

**Techniques used:**

*   Scatter plot with line [shapes for markers](https://chandoo.org/wp/2015/08/08/shapes-in-charts/)
    
*   [Drop down form control](https://chandoo.org/wp/2011/03/30/form-controls/)
     for sport selection
*   XY series for labels

**Snapshot**:  
![Chart 3: Bar code graph](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-3-demo-60-sports-in-6-charts.png)

### Chart 4: Scatter plot with random dots

Design by [Nils Macher](https://t.co/iKewqVr0N0)
 ([@](https://twitter.com/NilsM09)
)

**Techniques used:**

*   Scatter plot with shape transparency and [jitter](https://chandoo.org/wp/2017/08/17/visualize-salary-increases-jitter-plot/)
    
*   [Drop down data validation](https://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
     for sport selection
*   XY series for labels, grid lines for vertical lines

**Snapshot** (click to enlarge):  
[![Chart 4: Scatter plot with random dots](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-4-demo-60-sports-in-6-charts.png)](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-4-demo-60-sports-in-6-charts.png)

### Chart 5: Table with conditional formatting

Design by Chandoo ([@](https://twitter.com/r1c1)
)

**Techniques used:**

*   [Excel tables](https://chandoo.org/wp/2013/06/26/introduction-to-structural-references/)
     for keeping data
*   [Conditional formatting data bars](https://chandoo.org/wp/2010/05/19/new-features-in-excel-2010-conditional-formatting/)
    
*   [Form controls](https://chandoo.org/wp/2011/03/30/form-controls/)
     to show / hide values
*   [;;; format code for hiding values](https://chandoo.org/wp/2009/06/05/hide-cell/)
    

**Snapshot** (click to enlarge):  
[![Chart 5: Table with conditional formatting](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-5-demo-60-sports-in-6-charts.png)](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-5-demo-60-sports-in-6-charts.png)

### Chart 6: Which sports are similar to your sport?

Design by Chandoo ([@](https://twitter.com/r1c1)
)

**Techniques used:**

*   [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)
     between sport skill values, same concept is used to find clusters in ML or Data Science.
*   [Data validation drop down](https://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
     for sport selection
*   [Panel charts](https://chandoo.org/wp/2010/05/12/introduction-to-panel-charts-using-excel-tutorial-template/)
     and bar graphs with [categories in reverse order](https://chandoo.org/wp/2015/08/10/bar-chart-in-original-order/)
    

**Snapshot** (click to enlarge):  
[![Chart 6- Which sports are similar to your sport?](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-6-demo-60-sports-in-6-charts.png)](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-6-demo-60-sports-in-6-charts.png)

### Download sixty sports in 6 charts workbook

[**Click here to download the workbook**](https://chandoo.org/wp/wp-content/uploads/2018/05/60sports-6charts.xlsx)
. It is beautifully presented and contains heaps of detail. I made liberal use of [VLOOKUP](https://chandoo.org/wp/2012/03/30/comprehensive-guide-excel-vlookup/)
, [INDEX](https://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
 and occasional [SUMPRODUCT](https://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
 along with one odd [Power Query](https://chandoo.org/wp/2015/07/30/intro-to-power-query-podcast/)
 to reshape the data. Have a play with the charts. Check out the formulas and named ranges. Original data is in “Data” tab. Try making your own charts.

### If you want to learn how to create such charts…

If you like these charts and want to learn how to create them, then consider joining in my online video class **50 ways to analyze data.** I am adding 60 sports in 6 charts as new case study the class. You can learn how to go from raw data to beautiful charts like this in the class. [**Click here to know more & sign-up**](https://chandoo.org/wp/resources/50-ways-alternative-payment/)
.

### What is your favorite chart?

I like Chart #1 & 4. Of course, I had loads of fun building Chart #6 too. All in all it was a great exercise to recreate these charts in Excel and see what is possible.

_**What about you?**_ What is your favorite chart? How would you visualize it? Share your thoughts (or charts) in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/60-sports-in-six-charts/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/60-sports-in-six-charts/#respond)
    
*   Tagged under [50 ways course](https://chandoo.org/wp/tag/50-ways-course/)
    , [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [bar graphs](https://chandoo.org/wp/tag/bar-graphs/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [makeover monday](https://chandoo.org/wp/tag/makeover-monday/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [panel charts](https://chandoo.org/wp/tag/panel-charts/)
    , [scatter plot](https://chandoo.org/wp/tag/scatter-plot/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousMay the POWER BI with you \[Star Wars Day Viz\]](https://chandoo.org/wp/force-with-power-bi/)

[NextBeautiful Budget vs. Actual chart to make your boss love youNext](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)

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
    
    [Reply](https://chandoo.org/wp/60-sports-in-six-charts/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/60-sports-in-six-charts/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/60-sports-in-six-charts/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
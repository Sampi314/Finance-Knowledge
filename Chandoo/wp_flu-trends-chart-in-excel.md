# Flu Trends Chart in Excel [Yes, we can edition] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/flu-trends-chart-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    

Flu Trends Chart in Excel \[Yes, we can edition\]
=================================================

*   Last updated on February 24, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Last week I have [reviewed Google’s flu trends chart](http://chandoo.org/wp/2010/01/15/flu-trends-chart-review/)
 and told you why it is an awesome chart. This week, I am going to show you how such a chart can be constructed in Excel.

**First let me show you what I am able to do in Excel:**

![Flu Trends Chart in Excel](https://chandoo.org/img/p/flu-trends-chart-demo.gif)

(compare this with [actual chart on Google](http://www.google.org/flutrends/intl/en_us/us/#US)
)

### How I made the flu-trends chart in excel?

1.  **Data, Data, Data:** Data plays an important role in complex charts like these. The source data is thankfully available for download from Google.  Flu incidence data is available by week (Sunday to Saturday) for every week since 28th Sep, 2003. For each week the data if given for all regions in various columns. But I was not able to use the data “as-is” to construct this chart. I had to massage and rearrange it a bit.
2.  **The main issues is how flu season is classified** (it starts on July and ends in June) and how the data is (we got weekly flu incident data, starting from Sunday to Saturday). The main issue here is each year, the weeks start on different dates. For eg. first Sunday in 2010 was on 3rd Jan where as in 2009 it was on 4th Jan. I tried using WEEKNUM() formula ([examples](http://chandoo.org/wp/?s=weeknum "WEEKNUM formula examples")
    ), but it didn’t work well with the flu season (Jul to Jun). So I did some [basic date math](http://chandoo.org/wp/2008/08/26/date-time-tips-ms-excel/)
     and ended up mapping weeks uniformly across years.
3.  **The next issue is taking one big table of data with dates in rows and regions in columns and transform it** to weeks in rows, years and columns and actual flu data for the selected region in the cells.
4.  **Then I set up 2 cells, one where user would specify “region” and other where a comparison “year” can be selected**. I have used [data validation to control the valid inputs](http://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
    .
5.  **I used the MATCH, INDEX formulas** to fetch corresponding weekly values for all years for selected region. Thanks to [MATCH](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    , [INDEX](http://chandoo.org/wp/tag/index/)
     and [HLOOKUP formulas](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    , this is not such a big task either. And if the optional comparison year is specified, we repeat that years values in another column. Otherwise that column is NA().
6.  Using these columns, **I made a line chart.** Then I cleaned up the chart and formatted the 2009-2010 series in thick blue and rest all in thin light blues. The optional comparison series was colored in red (for contrast). \[related: [line chart examples](http://chandoo.org/wp/tag/line-charts/)\
    \]
7.  **The only remaining piece is to show the heat map of flu intensities** below the chart. For this I have used the very useful 3 color scale [conditional formatting](http://chandoo.org/wp/tag/conditional-formatting/)
     setting in Excel 2007. (of course, I had to setup some extra calculations so that the intensities are normalized across the region / years and change when user selects a new region, but you already guessed it.)  
    ![Excel Conditional Formatting - Heatmaps](https://chandoo.org/img/p/excel-heatmap-conditional-formatting.png)
8.  I choose to drop the colorful legend as it adds little value.
9.  The rest is some formatting and presentation.

### What I learned from this experience?

*   When I looked at Google’s chart, I doubted if it can be created in Excel. But I was wrong. It can be done in excel, and it takes no more than 2 hours.
*   **Data and structure of it play extremely important role in any visualization.**We should understand the data and know how to arrange / transform / massage it, to make better charts.
*   Date formulas are a flu in the nose.
*   Excel 2007 conditional formatting is just awesome. \[[more examples](http://chandoo.org/wp/tag/conditional-formatting/)\
    \]
*   INDEX, MATCH, LOOKUP formulas are very powerful. I \*respect\* them. \[[here is a tutorial](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)\
    \]

### Download flu trends chart and play with it

[Download the file](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/vis-pro/google-flu-trends-chart-excel.xlsx)
 (Excel 2007 only). The file is locked, but there is no password. Play with it and tell me if you like it.

_**Do you like this chart?**_

Have you done something similar in Excel? What was your experience like? Do you like this chart? How would you improve / change it?

**More visualizations using Excel:**

[Olympic Medals by Country](http://chandoo.org/wp/2008/08/06/olympic-medal-country-year-excel-bubble-chart/)
 | [Survey Results Dashboard](http://chandoo.org/wp/2007/06/27/the-art-of-excel-charting/)
 | [Test Cricket Statistics](http://chandoo.org/wp/2008/10/20/excel-dashboard-tutorial/)
 | [Dynamic Charts](http://chandoo.org/wp/tag/dynamic-charts)

PS: After a looong time this post had many “I”s

PPS: Have a good weekend.

[browser.cache.memory.capacity](http://kb.mozillazine.org/Browser.cache.memory.capacity "Browser.cache.memory.capacity")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [31 Comments](https://chandoo.org/wp/flu-trends-chart-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/flu-trends-chart-in-excel/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [cleanup data](https://chandoo.org/wp/tag/cleanup-data/)
    , [data processing](https://chandoo.org/wp/tag/data-processing/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [date axis](https://chandoo.org/wp/tag/date-axis/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [Featured](https://chandoo.org/wp/tag/best-of-phd/)
    , [flu](https://chandoo.org/wp/tag/flu/)
    , [google](https://chandoo.org/wp/tag/google/)
    , [heatmaps](https://chandoo.org/wp/tag/heatmaps/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [line charts](https://chandoo.org/wp/tag/line-charts/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [visualization principles](https://chandoo.org/wp/tag/visualization-principles/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [weeknum()](https://chandoo.org/wp/tag/weeknum/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    

[PrevPreviousUse “Playbill” font to make your incell charts realistic \[quick-tips\]](https://chandoo.org/wp/excel-incell-chart-font/)

[NextExcel School Online Training – More DetailsNext](https://chandoo.org/wp/excel-school-details/)

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
    
    [Reply](https://chandoo.org/wp/flu-trends-chart-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/flu-trends-chart-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/flu-trends-chart-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
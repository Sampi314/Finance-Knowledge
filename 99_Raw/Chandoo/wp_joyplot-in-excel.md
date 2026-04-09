# Joyplot in Excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/joyplot-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

Joyplot in Excel
================

*   Last updated on July 12, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Over on Twitter, I came across [this beautiful chart](https://twitter.com/hnrklndbrg/status/883675698300420098)
, aptly titled – Joyplot. It is the kind of chart that makes you all curious and awed. So I did what any Excel nerd would do. Recreated it in Excel of course. This post takes you thru the process.

> Peak time for sports and leisure [#dataviz](https://twitter.com/hashtag/dataviz?src=hash)
> . About time for a joyplot; might do a write-up on them. [#rstats](https://twitter.com/hashtag/rstats?src=hash)
>  code at [https://t.co/Q2AgW068Wa](https://t.co/Q2AgW068Wa)
>  [pic.twitter.com/SVT6pkB2hB](https://t.co/SVT6pkB2hB)
> 
> — Henrik Lindberg (@hnrklndbrg) [July 8, 2017](https://twitter.com/hnrklndbrg/status/883675698300420098)

First let me share the final outcome.

### Joyplot in Excel – Peak time of the day for sports and leisure

Here is the final overlapped area chart with a bit of formatting thrown in. It is a pretty close imitation of Henrik’s original chart. Click on it to enlarge.

[![joyplot-in-excel](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-in-excel.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-in-excel.png)

### Creating Joyplot in Excel – Tutorial

As you can guess, the chart is a **_just an overlapped area chart_** (ie each area sits behind another, unlike _stacked area chart_ where they are umm, well, stacked!)

Let’s start with a look at data. Henrik’s original data has 10,656 rows, each row containing activity name, time and p value – how much survey respondents enjoyed \[@activity\] at that time.

Here is a snapshot of first few rows.

![joyplot-data](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-data.png)

### Scrubbing and re-arranging the data

As you can see, while this format is excellent for storing, it is very tedious if we want to make one chart with all series. So let’s scrub.

1.  We need to figure out if an activity should be included or not. I am using the same criteria as Henrik’s. Exclude activities with p value less than 0.003 or activity title “Playing sports n.e.c. \*”  (not elsewhere classified)
    1.  To do this, we first pivot the data on activity and max(p). Then filter this pivot two ways – max(p) >=0.003 and label not equal  _Playing sports n.e.c. \*  
        Tip: You may need to enable multiple filters per field in the field settings of row labels._
    2.  We will end up with _28 activities_.
    3.  Then add a helper column to original table that looks up the pivot and tells if an activity should be included or not
2.  Add two more columns to original table to tell peak time and modified time. This will help us in rearranging and sorting the data. Modified time just moves time by 3 hours (Henrik’s chart is plotted from 3AM to 3AM). At this stage our data looks like this:  
    ![joyplot-data-extra-columns](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-data-extra-columns.png)
3.  Now, pivot the data once again. This time,
    1.  exclude activities by using report filter on include? column.
    2.  Set up peak and activity in row labels area, modified time in column labels area and p in values area.
    3.  Arrange the report in tabular format, turn off sub-totals.
    4.  We get this:  
        ![rearranged-data-with-pivot-joyplot](https://chandoo.org/wp/wp-content/uploads/2017/07/rearranged-data-with-pivot-joyplot.png)
4.  Calculate normalized values by dividing each p value with maximum p value for that activity. We can use another range of 28×288 cells to do this. We get this:  
    ![normalized-values](https://chandoo.org/wp/wp-content/uploads/2017/07/normalized-values.png)
5.  **_The next 2 steps may seem confusing._** It will become clear once you look at the charts.
6.  Define an offset value. Start with 0.5. You can change this later. In a separate 28×288 cell range, calculate gaps by multiplying offset with position of an activity. Something like this:  
    ![gaps-joyplot](https://chandoo.org/wp/wp-content/uploads/2017/07/gaps-joyplot.png)
7.  Now, finally calculate activity + gap values by adding up respective cells in each of the 28×288 ranges. We get this:  
    ![actual-plus-gap-values-joyplot](https://chandoo.org/wp/wp-content/uploads/2017/07/actual-plus-gap-values-joyplot.png)

**At this stage, our data is a shape ready for visualizing.**

### Creating and formatting overlapped area chart

The chart creation process has 5 steps.

1.  Select the 28×288 range of cells created in step 7 and insert an overlapped area chart.
2.  Now, copy the gaps range (created in step 6 above) and paste them on to area chart as new series (just ctrl+c your data and select the chart, press ctrl+v)
3.  Adjust the order of series so that each activity is sandwiched by appropriately named gap series
    1.  Tip: adjusting 56 series is painful with the chart select data > move series up/down buttons. Instead, just select the series, look at formula bar. The SERIES formula has last parameter as order. Change this number. It is easy to figure out the number once you try a few.
4.  Change all gap series fill color to white. This instantly creates the floating area chart effect.
5.  Change the colors of activity series. Apply white / off-white border to these series. Your joyplot is ready.

**Quick overview of the chart creation process:**

Let’s examine the result of each those 5 steps with a smaller dataset so you can see how everything fits together. Here is the data for this example:

![sample-data-for-chart-tutorial-joyplot](https://chandoo.org/wp/wp-content/uploads/2017/07/sample-data-for-chart-tutorial-joyplot.png)

1.  Create an overlapped area chart with activity+gaps data. We get this:  
    ![sample-joyplot-step-1](https://chandoo.org/wp/wp-content/uploads/2017/07/sample-joyplot-step-1.png)
2.  Add gaps as new series to chart. You get this:  
    ![sample-joyplot-step-2](https://chandoo.org/wp/wp-content/uploads/2017/07/sample-joyplot-step-2.png)
3.  Move the gap series so that they sandwich activity series. Use Chart Data > Move series up/down buttons or SERIES formula  
    ![sample-joyplot-step-3](https://chandoo.org/wp/wp-content/uploads/2017/07/sample-joyplot-step-3.png)
4.  Apply white color fill formatting for gap series. This creates floating area chart effect as below:  
    ![sample-joyplot-step-4](https://chandoo.org/wp/wp-content/uploads/2017/07/sample-joyplot-step-4.png)
5.  Finally, format the chart by apply some colors and border formatting etc.  
    ![sample-joyplot-step-5](https://chandoo.org/wp/wp-content/uploads/2017/07/sample-joyplot-step-5.png)

So there you go. The final outcome does look joyful.

[![joyplot-in-excel](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-in-excel.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-in-excel.png)

### Alternatives to Joyplot

While joyplot is awesome, it is not easy to make. Fortunately, there are a few simpler alternatives that we can whip up in Excel as soon as you have either the pivot or normalized values.  Below I have shown two such examples. Read about [sparklines](http://chandoo.org/wp/2010/05/18/excel-sparklines-tutorial/)
 or [conditional formatting heatmaps](http://chandoo.org/wp/resources/ways-to-analyze-business-data/)
 for more.

**Joyplot alternative – using sparklines:**

Tip: to get axis on your sparkline, just type the times separated by a single space. Then go to format cell (ctrl+1) and set horizontal alignment to distributed. Viola, Excel will fill the cell by adjusting spaces.

![joyplot-alternative-sparklines](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-alternative-sparklines.png)

**Joyplot alternative – Conditional Formatting Heatmap** 

![joyplot-alternative-heatmap](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-alternative-heatmap.png)

### Download Joyplot Workbook

[**Click here to download Joyplot Excel workbook**](https://chandoo.org/wp/wp-content/uploads/2017/07/joyplot-v1.xlsx)
. Examine the data scrubbing formulas, pivot and chart settings to learn how this is created.

If you are familiar with R, then go thru [Henrik’s R code](https://github.com/halhen/viz-pub/blob/master/sports-time-of-day/2_gen_chart.R)
. It is much shorter than the Excel gymnastics we did with circular pivot table referencing. That said, some of the data re-arrangement could be done with same ease in Power Query too.

### Your thoughts on Joyplot?

The only step we missed in Excel implementation is moving average smoothing of the area charts. It can be easily added as a step between 3 and 4 in data stage.

How do you like Joyplot? Would you create something like this for your business / personal data? Share your stories and thoughts in the comments section.

**More joy for you…**

If you love this, you are going to [enjoy these charts](http://chandoo.org/wp/tag/visualization-projects/)
 too.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [19 Comments](https://chandoo.org/wp/joyplot-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/joyplot-in-excel/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [area charts](https://chandoo.org/wp/tag/area-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [heatmaps](https://chandoo.org/wp/tag/heatmaps/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [sparklines](https://chandoo.org/wp/tag/sparklines/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

[PrevPreviousHow to add a lot of Goal Seeking to a model](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/)

[NextExtract currency amounts from text – Power Query TutorialNext](https://chandoo.org/wp/extract-currency-amounts-from-text-power-query-tutorial/)

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
    
    [Reply](https://chandoo.org/wp/joyplot-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/joyplot-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/joyplot-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
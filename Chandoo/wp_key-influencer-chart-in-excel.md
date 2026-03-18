# How to fake "Key influencers chart" in Excel? » Advanced Charting

**Source:** https://chandoo.org/wp/key-influencer-chart-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

How to fake “Key influencers chart” in Excel?
=============================================

*   Last updated on May 1, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![key-influencer-chart-in-excel-header](https://chandoo.org/wp/wp-content/uploads/2019/05/key-influencer-chart-in-excel-header-1.png)

Recently, Microsoft Power BI introduced a very useful visualization, called **[key influencers visualization](https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-influencers)
.** As the name suggests, this is a chart of key parameters that effect a measure or outcome.

For example, you have customer satisfaction rating as a measure. Now you want to know which aspects of your data impact the ratings most? You can create the key influencer visual and Power BI finds all the top ranking influencers (using rules and machine learning).

**_The output can go like this:_**

![key influencers visualization in power bi](https://chandoo.org/wp/wp-content/uploads/2019/05/key-influencers-visualization-pbi.png)

**How to read this chart?**

Let’s look at top influencer for _rating to be LOW_: If role of the rating person is “Consumer” then their rating is 2.57 times likely to be low than other roles.

Likewise, if company size is <5000, then their rating is 1.48 times likely to be low than other company sizes.

As soon as I saw this chart in Power BI demo, I went…

> **_Hot damn, that looks interesting!!! Can we get this in Excel?_**

Of course, Excel is a good few laps behind Power BI when it comes to data viz. But that won’t stop a data nerd, will it?

So here we go, a faked “key influencer chart in Excel”. Read on to learn how to create this yourself, from almost any data.

Key influencer chart in Excel – demo
------------------------------------

Before we learn how to make this, let me present the chart itself.

![key influencers chart in Excel - quick demo](https://chandoo.org/wp/wp-content/uploads/2019/05/key-influencer-chart-excel-demo.gif)

Create your own key influencer chart in Excel…
----------------------------------------------

So you are ready to make the chart? Just follow below steps and your key influencers will be identified, sorted and presented in a tidy chart.

### Step 1: Arrange your data

This method works with data in one table. You can scale it to a dimensional model (star schema) with some creative pivot tables or cube formulas, but if you have gone that far, then you might as well jump to Power BI and save yourself a lot of agony.

Say your data is in a table like this. **_We want to investigate key influencers (from dimensions) of “Salary” column_**. This data is in a table named _data._

![data for key influencer analysis](https://chandoo.org/wp/wp-content/uploads/2019/05/data-for-key-influencer-chart.png)

### Step 2: Calculate and sort influences

Now that we know our objective, let’s go ahead and crunch some numbers.

First, generate a list of all influences. This step is a bit manual, but not too hard. You can use Power Query to automate it if it gets too much.

**_We get something like this:_**

![calculating influences](https://chandoo.org/wp/wp-content/uploads/2019/05/two-kind-of-calculations.png)

As indicated above, we need to calculate two kinds of averages.

*   _average of each column=criteria_
*   _average of each column<>criteria_

This is easily done by a couple of AVERAGEIFS formulas.

For example,

\=AVERAGEIFS(data\[salary\], data\[Dept\], "Accounting")   
for "Accounting" average pay.

\=AVERAGEIFS(data\[salary\], data\[Dept\], "<>Accounting")    
for all departments except "Accounting"

![may be the formula needs to be smarter....](https://chandoo.org/wp/wp-content/uploads/2019/05/hmm-that-formulas-is-too-manual.png)

### Let’s be smart then..,

Instead of writing formulas with manual criteria, we can tweak the column (data\[Dept\] for ex.) on the fly. After all, we know the column name.

So, let’s use this.

    =AVERAGEIFS(data[Salary],INDEX(data,,MATCH(L5,data[#Headers],0)),M5)

**So what does it do?** This formula calculates average of data\[Salary\] where M5 (Accounting for ex.) is found in the column that has the same header as L5 (Dept).

This is a powerful and elegant use of INDEX formula. [Read this page if your INDEX() finger is weak](https://chandoo.org/wp/index-formula-usage-and-tips/)
.

### Adding other calculations

Now that we have both averages, we can calculate the influence of something like this:

1.  Influence = average of criteria / average of not criteria – 1
2.  Order (rank) of influence = Individual influence’s rank in all influences

We can use simple arithmetic for 1 and RANK.AVG() for 2.

**(Picture A)** **Summary of all the calculations so far…**

![Picture A - important calculations in the key influencer chart](https://chandoo.org/wp/wp-content/uploads/2019/05/formulas-for-key-influencer-chart.png)

Calculation Summary – Picture A

### Step 3: Start making the chart then…

Now that everything is ready, go to Insert ribbon and add Key Influencer chart.

![fake - key influencer icon in ribbon](https://chandoo.org/wp/wp-content/uploads/2019/05/haha-key-influencer-in-ribbon.png)

Of course I’m kidding. There is no such button. But you can insert a 3D donut chart. Or may be not.

So let’s move on then.

The Key Influencer chart demo’d at the start is actually a scatter plot. See below anatomy.

![anatomy of key influencer chart in Excel](https://chandoo.org/wp/wp-content/uploads/2019/05/anatomy-of-key-influencer-chart-excel.png)

### 10 Steps for creating the chart

**(1) Make a scatter plot from “more by” and “influence order” columns**

Select columns 3 & 4 as shown in Picture A and insert scatter plot. We get something like this.

![step 1 - scatter plot - key influencer chart in excel](https://chandoo.org/wp/wp-content/uploads/2019/05/01-scatter-plot-from-more-by-and-influence-order-columns.png)

**(2) Reverse the chart by changing Y (vertical) axis order**

Just select the Y (vertical) axis and go to axis format settings (CTRL+1 shortcut). Now select “Values in reverse order” option.

![reverse items in y axis](https://chandoo.org/wp/wp-content/uploads/2019/05/show-values-in-reverse-order-excel-chart-axis-settings.png)

We get this.

![flipped scatter plot](https://chandoo.org/wp/wp-content/uploads/2019/05/02-reversed-vertical-axis.png)

**(3) Limit vertical axis from 0 to 8**

The scatter plot is showing all influences. We don’t need to see everything. So let’s limit the chart to top 8 influences. To do that, simply enter axis limits as 0 and 8.5 (if you put 8, then the last point will be hugging bottom border of chart and makes it hard to read).

You will end up with this.

![axis trimmed to top 8 items](https://chandoo.org/wp/wp-content/uploads/2019/05/03-trimmed-to-top-8-points.png)

**(4) Replace dots with bubble**

Now draw a bubble shape in the spreadsheet. Copy it (Ctrl+C). Select the dots in the chart and hit paste (CTRL+V). We get nice bubbles instead of dots in the chart. See this quick tut to understand the concept.

![replacing dots with bubbles in scatter plot](https://chandoo.org/wp/wp-content/uploads/2019/05/how-to-change-shape-of-dots-in-scatter-plot-demo.gif)

**(5) Add data labels**

Select the bubbles and add data labels. Show either X value or calculated labels from cells. Center align and adjust font settings if needed. At this point our key influencer chart looks like this:

![after adding labels ](https://chandoo.org/wp/wp-content/uploads/2019/05/04-bubbles-instead-of-dots-with-labels.png)

**(6) Add a dummy series with values just 1 or 2% less than influence**

Now that our bubbles are ready, we need to show an arrow from 0 to the influence amount. To do this, we will use error bars, specifically _100% negative x error bars._ Try saying that three times in a row.

This is easy to get. Simply add a new column to the calculations area. Write =influence – 2% and you get “Dummy for arrows” column.

![dummy for arrows](https://chandoo.org/wp/wp-content/uploads/2019/05/dummy-column-for-arrows.png)

Add this column to the chart. Remember, the Y values will be same as “Influence order” (Column 4 in Picture A)

![after dummy series is added](https://chandoo.org/wp/wp-content/uploads/2019/05/05-dummy-for-arrows-thru-error-bars.png)

**(7) Add 100% negative x-error bars to the dummy series and format them**

![one does not simply...](https://chandoo.org/wp/wp-content/uploads/2019/05/one-does-not-simply-add-100-negative-error-bars.png)

Wait a second. You can’t simply do that. So just add error bars and then,

1.  Remove vertical (Y) error bars
2.  Select horizontal (X) error bars
3.  Format them (CTRL+1 shortcut)
4.  Set bar direction to “Minus”
5.  Error amount to Percentage, 100%
6.  And end style to “No cap”

We end up with this chart.

![negative x-error bars added](https://chandoo.org/wp/wp-content/uploads/2019/05/06-100-negative-x-error-added.png)

While you are at error bar formatting screen, also adjust the bar color and begin arrow type so we get this nice arrowed error bars.

![error bars formatted](https://chandoo.org/wp/wp-content/uploads/2019/05/07-error-bars-formatted-1.png)

**(8) Add another dummy series at -20% for axis labels**

We know that top influencer increases average salary by 8.8%, but we don’t know what that is. Time to fix the problem.

Let’s create our own axis labels. Start by adding a dummy column with =-20% in the calculations area.

Also, create the label we want (this can be column & ” is ” & criteria or something else).

**_You need data like this._**

![axis labels data ](https://chandoo.org/wp/wp-content/uploads/2019/05/dummy-column-for-axis-labels.png)

Once that is ready, add a new series to the chart (from Select Data screen) and set X as “Dummy x for axis label” and Y as Influence Order (column 4 in picture A).

_At this stage, our key influencer visual looks like this:_

![axis labels - points added](https://chandoo.org/wp/wp-content/uploads/2019/05/08-axis-label-series-added.png)

**(9) Add the labels**

Select this new dummy series, add data labels to it. Change label settings so that you can get values from cells (works only Excel 2013 or above). Point to the cells with calculated axis labels.

When everything is set up and formatted, we will have this chart:

![after aixs labels added](https://chandoo.org/wp/wp-content/uploads/2019/05/09-after-addind-axis-labels.png)

**(10) Nearly there, just clean up and format the chart**

Can you feel the rush of creating something beautiful, fun and interesting in Excel? We are almost done. Just clean up the chart. Remove markers from any dummy series that are not needed. Get rid of grid lines. Add background if you want. Color things and our key influencer chart in Excel is ready.

![almost final -  key influencer chart in excel](https://chandoo.org/wp/wp-content/uploads/2019/05/10-clean-up-act.png)

### Final touches – Form control to see positive and negative influences

Of course, the chart is nearly done. But if you want, you can dynamically show either positive or negative influencers. To do that, simply multiply the “More by” column (Column 3 in Picture A) with +1 or -1. +1 for positive influence, -1 for negative. Everything else works just as expected. You can link this to a form control and you will have a dynamic influencers chart.

![adding form control](https://chandoo.org/wp/wp-content/uploads/2019/05/key-influencer-chart.png)

Key Influencer Chart in Excel – Video tutorial
----------------------------------------------

As this is a fairly complex chart, I made a video tutorial explaining all the nuts and bolts. Watch it if you need a hand with the construction.

You can also [see this is on my YouTube channel](https://youtu.be/hO2Dgec13aQ)
.

Download Key Influencers Chart template
---------------------------------------

**[Click here to download the key influencer chart template](https://chandoo.org/wp/wp-content/uploads/2019/05/faking-key-influencer-chart-in-excel.xlsx)
.**

This file contains detailed instructions, sample data and calculations. Use it to learn or modify for your needs.

What next?
----------

If this is the first time you made a complex Excel chart, pat yourself on the back, go for an extra round of your favorite beverage and hug your loved ones.

And oh yeah, continue the journey with these other examples. You will be richly rewarded.

*   [![](https://chandoo.org/wp/wp-content/uploads/2018/05/budget-vs-actual-chart-free-template.png)](https://chandoo.org/wp/budget-vs-actual-chart-free-template)
    
    Budget vs. Actual Chart
    
*   [![](https://chandoo.org/wp/wp-content/uploads/2018/05/60-sports-in-6-charts.png)](https://chandoo.org/wp/60-sports-in-six-charts)
    
    Sixty sports in 6 charts
    
*   [![](https://chandoo.org/wp/wp-content/uploads/2018/04/interactive-chart-in-excel-tutorial.gif)](https://chandoo.org/wp/interactive-charts-tutorial)
    
    Dynamic chart in Excel
    
*   [![](https://chandoo.org/wp/wp-content/uploads/2018/04/cg2018-demo.gif)](https://chandoo.org/wp/visualizing-commonwealth-games-data)
    
    Commonwealth games in a chart
    
*   [![](https://chandoo.org/wp/wp-content/uploads/2017/10/dynamic-histogram-tip.gif)](https://chandoo.org/wp/histograms-pareto-charts-in-excel)
    
    Interactive pareto chart
    
*   [![](https://chandoo.org/wp/wp-content/uploads/2017/08/SNAG-0159.png)](https://chandoo.org/wp/visualize-salary-increases-jitter-plot)
    
    Salary increases in scatter plot
    

How do you like the Key Influencer Chart?
-----------------------------------------

I love the original thing in Power BI. Faking (recreating) it in Excel was fun but not scalable for large or split out data sets. I enjoyed the process immensely and immediately wanted to share it with all.

**_What about you?_** How do you like the key influencers chart in Excel? Share your thoughts in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [5 Comments](https://chandoo.org/wp/key-influencer-chart-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/key-influencer-chart-in-excel/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [error bars](https://chandoo.org/wp/tag/error-bars/)
    , [key influencer chart](https://chandoo.org/wp/tag/key-influencer-chart/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [scatter plot](https://chandoo.org/wp/tag/scatter-plot/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousHow to sort left to right in Excel (quick tip)](https://chandoo.org/wp/howto-sort-left-to-right-in-excel/)

[NextHow many calls we got outside office hours? \[Excel / Power Query homework\]Next](https://chandoo.org/wp/how-many-calls-outside-office-hours/)

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
    
    [Reply](https://chandoo.org/wp/key-influencer-chart-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/key-influencer-chart-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/key-influencer-chart-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
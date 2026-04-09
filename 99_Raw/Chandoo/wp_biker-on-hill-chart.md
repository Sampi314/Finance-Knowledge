# Visualizing target vs. actual progress - Biker on a hill chart » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/biker-on-hill-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

Visualizing target vs. actual progress – Biker on a hill chart
==============================================================

*   Last updated on September 20, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Over the years, we have discussed a [whole](http://chandoo.org/wp/2009/04/05/budget-vs-actual-charts/)
 [heap](http://chandoo.org/wp/2009/12/07/christmas-gift-list/)
 [of](http://chandoo.org/wp/2009/12/17/quick-thermometer-chart/)
 [techniques](http://chandoo.org/wp/2009/12/18/charts-to-compare-targets/)
 [to](http://chandoo.org/wp/2012/06/11/thermo-meter-chart-with-last-year-marker/)
 [visualize](http://chandoo.org/wp/2016/09/12/stacked-bar-and-indicator-arrow-chart-tutorial/)
 budget vs. actual charts. Today let’s take a ride on this slope again and learn another **fun, silly & awesome way to depict target vs. actual progress**.

### Introducing biker on a hill chart

Tada!!!

Biker on a hill!?! Don’t worry, I didn’t fall down on a descent and lose my brain. I am talking about an Excel chart to visualize target vs. actual progress on a time line with biker on a hill analogy. See the chart, you will know:

![biker-on-hill-target-vs-actual-chart-demo](https://chandoo.org/wp/wp-content/uploads/2016/09/biker-on-hill-target-vs-actual-chart-demo.gif)

Looks interesting? Read on to learn how to create this in Excel.

### Get your data

The _biker on a hill_ chart is suitable when you have a huge target that should be achieved in several days, each with individual target. So input data looks like this:

![raw-data-actual-vs-target-biker-on-hill-chart](https://chandoo.org/wp/wp-content/uploads/2016/09/raw-data-actual-vs-target-biker-on-hill-chart.png)

Let’s say this data is in a table named **progress**. As you can guess, first three columns are inputs. Last column is calculated with a simple SUM formula to get cumulative target values. The formula used here is

\=SUM(E3,\[@Target\])

Where E3 refers to the cell above first row.

### Calculate hill and biker co-ords

The hill is a  simple X-Y chart with progress\[Date\] as X and progress\[Target-Cumulative\] as Y.

The tricky part is finding biker co-ordinates. We need 2 sets of values.

1.  Actual biker position based on the amount of work completed.
2.  Target biker position based on the amount of work that _**should have been**_ completed.

Let’s understand the math behind this.

**Actual biker position:**

Y value (actual completed): This is simply SUM(progress\[Completed\])

X value (corresponding date): Now this is tricky. We need to find what date corresponds to the actual progress made based on the set targets.  for this we need to find several things:

*   **Corresponding row #:**  Using MATCH(), we find out what value in the cumulative target column matches the progress completed so far.
*   We will then find two dates between which the progress completed falls between, using MATCH formulas.
*   Finally, we will interpolate the corresponding date between these two dates using simple arithmetic.

**Target biker position:**

Y value (target): Target as of latest date, using either VLOOKUP or INDEX+MATCH

X value (date): this is simply date in **corresponding row #** that is calculated above.

### Create the biker on hill chart

**Step 1: Create an XY chart for the hill**

Setup an XY chart where X=progress\[Date\] and Y=progress\[Target-Cumulative\]. We get this.

![actual-vs-target-biker-on-hill-chart-1](https://chandoo.org/wp/wp-content/uploads/2016/09/actual-vs-target-biker-on-hill-chart-1.png)

**Step 2: Add target & actual bikers**

Add two more series to the chart. Target biker and actual biker using the X&Y values calculated above. We get this.

![actual-vs-target-biker-on-hill-chart-2](https://chandoo.org/wp/wp-content/uploads/2016/09/actual-vs-target-biker-on-hill-chart-2.png)

**Step 3: Replace the dots with biker images**

This is easy. Download a clip art image of cyclist from internet. Paste it on your Excel workbook. Remove any background. Rotate the biker image by 30° or so. As this is not a real life biker on hill, we can afford 30° gradients.

Once you have new rotated biker, reduce the image size if necessary and clone it.

Change colors using format image > Color options ([see here for detail](https://chandoo.org/wp/wp-content/uploads/2016/09/change-image-color-excel.png)
).

_**Essentially, go from the image on left to right.**_

![transform-biker-images](https://chandoo.org/wp/wp-content/uploads/2016/09/transform-biker-images.png)

Now that you have biker images, replace the dots with bikers using following instructions.

1.  Select biker image and copy (Ctrl+C)
2.  Click on the dot in your chart
3.  Press Ctrl+V to paste image
4.  Viola, your chart now shows bikers instead of dots for actual and target values.

At this stage our chart looks like this.

![actual-vs-target-biker-on-hill-chart-3](https://chandoo.org/wp/wp-content/uploads/2016/09/actual-vs-target-biker-on-hill-chart-3.png)

**Step 4: Move the bikers up**

Because Excel places the dot right on the line, the biker image too will be centered on it. So instead of looking a _biker on hill,_ our chart looks like the biker is buried half in the hill. Not good, whether you are a fictional or real biker. So let’s pull the bikers.

We can do this by simply adding an offset value to the Y values. A value of 7 should work. But you can tweak this depending on your chart / image sizes.

Once we fix the calculations, our chart looks like this.

![actual-vs-target-biker-on-hill-chart-4](https://chandoo.org/wp/wp-content/uploads/2016/09/actual-vs-target-biker-on-hill-chart-4.png)

### Extra bells and lights

Bikers are known to pimp their rides with all sorts of doodads. We can show similar enthusiasm for our biker on a hill chart and add few more details. Here is one version after adding _**information about current progress status and forecast date of completion**_.

![actual-vs-target-biker-on-hill-chart-5](https://chandoo.org/wp/wp-content/uploads/2016/09/actual-vs-target-biker-on-hill-chart-5.png)

The math for this is quite boring and simple. So I leave it to your imagination.

### Download Biker on a hill – Target vs. Actual Chart Template

[**Click here to download biker on hill chart**](https://chandoo.org/wp/wp-content/uploads/2016/09/biker-on-hill.xlsx)
. Play with input data to move the biker towards target. Examine calculation section or chart to learn more.

### Thanks GraH for the inspiration

Time for a confession. The biker on a hill chart idea isn’t mine. I got this from GraH, one of our readers. He left a [comment on a recent blog post](http://chandoo.org/wp/2016/09/15/stacked-barcolumn-chart-with-indicator-arrows-advanced/#comment-1288595)
 and I liked the idea. So I wrote this blog post explaining how we can all create a biker on hill chart in Excel.

> Hui rules! But nevertheless, the creativity on this blog and the contribution of the bloggers are inspiring. And really enabling people to be aweSUM in XL, like you say.  
> I followed a training on Excel Dashboards in 2015 and your site was highly recommended by our cool trainer.  
> I became aware that XL can-do much more. Ingredients are a little imagination, dare to experiment and knowledge on how to combine techniques/functions.  
> In short within 2 weeks I will give a 1 hour XL awareness training in my company during open training week. I just sent a teaser with stuff I found here and on other XL-guru’s sites to my HR department. Within the next 5 minutes my proposition was approved. The reply was “Excellent idea!”  
> And the funny thing is that I found an XL soul-mate only a few seats away. Now we make each other crazy with challenges and/or things we learn about XL. The very first thing we made for a manager was _**a biker (representing his team) climbing a mounting (of work) towards the finish (the volume to reach at end of day)**_. Depending on current status, different motivational talk appears in the title. The manager could not believe we just made a simple chart.

**So thanks GraH for the cool idea**.

### How do you visualize target vs. actual progress?

I prefer [conditional formatting icons](http://chandoo.org/wp/2013/07/11/never-use-simple-numbers-in-your-dashboards/)
 and [thermometer charts](http://chandoo.org/wp/2009/12/17/quick-thermometer-chart/)
 for budget / target vs. actual progress charts. Sometimes I use a [bullet chart](http://chandoo.org/wp/2008/07/21/dashboard-bullet-graphs-excel/)
 or [variations of thermometer charts](http://chandoo.org/wp/2012/06/11/thermo-meter-chart-with-last-year-marker/)
 too. I have also used [burndown charts](http://chandoo.org/wp/2009/07/21/burn-down-charts/)
 (same concept as biker on hill charts). I like the biker on hill chart and may use it for some of my upcoming work.

**What about you?** What charts do you use to depict target vs. actual progress? How do you like biker on hill chart? Please share your thoughts and suggestions in the  comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [37 Comments](https://chandoo.org/wp/biker-on-hill-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/biker-on-hill-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [scatter plot](https://chandoo.org/wp/tag/scatter-plot/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

[PrevPreviousStacked Bar/Column Chart with Indicator Arrows – Advanced](https://chandoo.org/wp/stacked-barcolumn-chart-with-indicator-arrows-advanced/)

[NextVisualizing Financial Metrics – Contest WinnersNext](https://chandoo.org/wp/visualizing-financial-metrics-contest-winners/)

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
    
    [Reply](https://chandoo.org/wp/biker-on-hill-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/biker-on-hill-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/biker-on-hill-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
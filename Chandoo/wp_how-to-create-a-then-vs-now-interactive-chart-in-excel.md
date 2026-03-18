# How to create a Then vs. Now interactive chart in Excel? » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-create-a-then-vs-now-interactive-chart-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

How to create a Then vs. Now interactive chart in Excel?
========================================================

*   Last updated on August 6, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

You have been there before.

Trying to compare last year numbers with this year, or last quarter with this quarter.

Today, let us learn how to create an interactive to chart to understand then vs. now.

### Demo of Then vs. Now interactive chart

First, take a look the completed chart below. This is what you will be creating.

![Then vs. Now interactive chart - How to create this in Excel](https://img.chandoo.org/c/then-vs-now-chart-with-details-demo.gif)

### Inspiration for this chart

Before we jump in to Excel and understand how this is done, let me thank NY Times for providing the inspiration for this chart. I saw a similar chart in their [climbing income ladder visualization](http://www.nytimes.com/2013/07/22/business/in-climbing-income-ladder-location-matters.html?_r=1&)
.

Creating Then vs. Now chart in Excel
------------------------------------

### 1\. Arrange data

As usual, the first step is to get the data in to Excel. Structure your data like this.

![Data for Then vs. Now chart](https://img.chandoo.org/c/data-for-then-vs-now-chart.png)

### 2\. Insert a combo box control to select a region

![Insering combo box form control and formatting it - then vs now chart](https://img.chandoo.org/c/formatting-combo-box-form-control-then-vs-now-chart.png)Since our chart will display values for one region at a time, we need a mechanism to let user control which region is displayed. We will use a combo box control do this. Follow these steps.

1.  Go to developer ribbon and insert combo box form control.
2.  Right click on the combo box and go to format control.
3.  Set up input range to list of regions in your data.
4.  Set up cell link to a blank cell in your workbook.

**Related: [Introduction to form controls](http://chandoo.org/wp/2011/03/30/form-controls/)
.**

### 3\. Fetch selected region’s data

Now that we have a combo box to select which region to show in the chart, next step is to fetch data for selected region. You can use either VLOOKUP or INDEX formulas to do it.

**Using VLOOKUP formula:**

_Assuming region name is in **D17**, and data is in **values** table, write:_

\=VLOOKUP(D17, values, 2, false)

to get 2nd column (then sales) value.

**[More on using VLOOKUP formula](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
**

**Using INDEX formula:**

_Assuming region number is in **D16**, and data is in **values** table, write:_

\=INDEX(values\[then\],D16)

### 4\. Create a chart showing then to now movement

Next step is to create a chart that would show a line going from _then value_ to _now value_. Lets take a closer look the line to understand how to make it in Excel.

![Examining then vs now chart - a closer look at how to create it](https://img.chandoo.org/c/closer-look-at-then-vs-now-chart.png)

We can create this chart with either XY (scatter) plot or line chart. Lets go with scatter plot.

**In your workbook, set up a table like this:**

![Then vs. now values for selected region](https://img.chandoo.org/c/then-vs-now-values-for-scatter-plot.png)

Then, select the above and create a scatter plot. Select the scatter plot with connecting lines.

### 5\. Formatting the chart

Since we want to show a thick circle at the beginning of _then value_ and arrow at the end of _now value_, lets go ahead and do the formatting song and dance.

**![Formatting starting point of then vs now chart](https://img.chandoo.org/c/marker-settings-for-beginning-point.png)Formatting the first point:**

1.  Select the first point of then values (you need to click once on it, take 3 deep breaths, click again and sacrifice a goat).
2.  Press CTRL+1 to format the data point.
3.  Go to Marker options and select built in marker and use the circle symbol.

**![Formatting ending point - then vs. now chart](https://img.chandoo.org/c/line-settings-for-ending-point.png)Formatting the last point:**

1.  Select the last point (same as above, but this time sacrifice a chicken)
2.  Format the data point.
3.  Go to line style, select End type and choose arrow.

**![Formatting horizontal axi - then vs now chart](https://img.chandoo.org/c/axis-options-then-vs-now-chart.png)Formatting the horizontal axis:**

1.  Select horizontal (x) axis and press CTRL+1
2.  Set axis minimum to 1, maximum to 6.
3.  Click ok and delete the axis as we do not need it on the chart.

### 6\. Adding “Break-up” of now values chart

This is easy, Just select fetched break-up values for selected region and create a bar chart. Format it as per your fancy.

### 7\. Put everything together

Place the combo box, scatter plot and bar chart together in a nice fashion. Add a surrounding box shape so that everything looks like one report.

Add a descriptive title on the top. If possible, make [chart title dynamic](http://chandoo.org/wp/2010/04/08/smart-chart-legends/)
 so that you can show the selected region name and % change in it.

### 8\. Your Then vs. Now chart is ready

That is all. Your Then vs. Now chart is ready. Go ahead and flaunt it.

![Final Then vs. Now chart with all bells and whistles](https://img.chandoo.org/c/final-then-vs-now-chart.png)

Download the chart workbook
---------------------------

[**Click here to download the chart workbook**](https://img.chandoo.org/d/then-vs-now-interactive-chart.xlsx)
 and play with it. Examine the formulas, chart settings and shapes to understand how this is set up.

Do you make then vs. now charts?
--------------------------------

I think about half the charts made businesses around the world fall in to this category. I make these type of charts all the time. I use a variety of chart types to convey this information. [Thermometer chart](http://chandoo.org/wp/2012/06/11/thermo-meter-chart-with-last-year-marker/ "Thermo-meter chart with Marker for Last Year Value")
, [waterfall chart](http://chandoo.org/wp/2009/08/10/excel-waterfall-charts/ "Waterfall Charts using Excel")
 and [conditionally formatted tables](http://chandoo.org/wp/2013/07/11/never-use-simple-numbers-in-your-dashboards/ "Never use simple numbers in your dashboards (bonus tip: how to fix default conditional formatting)")
 are some of my favorite techniques.

**What about you?** Do you create then vs. now charts? what type of charts do you use? Please share your techniques and ideas using comments.

### Learn more…

If you are not working in a cave or behind a huge stack of desks, chances are your job involves communicating for a living. Go ahead and read-up below articles to learn how to communicate with charts better, when it comes to then vs. now situations.

*   [Budget vs. Actual charts – 14 alternatives](http://chandoo.org/wp/2009/04/05/budget-vs-actual-charts/)
     (a variation of then vs. now)
*   [Us vs. Them – an interactive chart](http://chandoo.org/wp/2009/03/12/comparison-charts-1/)
    
*   [More Budget vs. actual charts](http://chandoo.org/wp/tag/budget-vs-actual/)
    
*   [How to make your charts interactive?](http://chandoo.org/wp/2012/08/02/making-dashboards-interactive/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [40 Comments](https://chandoo.org/wp/how-to-create-a-then-vs-now-interactive-chart-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-create-a-then-vs-now-interactive-chart-in-excel/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [budget vs. actual](https://chandoo.org/wp/tag/budget-vs-actual/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [combo box](https://chandoo.org/wp/tag/combo-box/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [ny times](https://chandoo.org/wp/tag/ny-times/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousPower Pivot online classes – now open for you](https://chandoo.org/wp/power-pivot-online-classes-now-open-for-you/)

[NextHow to find the lowest value? \[Quick tip\]Next](https://chandoo.org/wp/how-to-find-the-lowest-value-quick-tip/)

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
    
    [Reply](https://chandoo.org/wp/how-to-create-a-then-vs-now-interactive-chart-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-create-a-then-vs-now-interactive-chart-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-create-a-then-vs-now-interactive-chart-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
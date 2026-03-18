# Plot your data around the clock [Excel charting idea] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/plot-time-series-data-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Plot your data around the clock \[Excel charting idea\]
=======================================================

*   Last updated on August 15, 2008

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

If your reports include hourly distribution of data like,

*   Customer footfalls in your store
*   Page views of your site
*   Customer service calls to your toll free numbers

here is an interesting charting idea to show the data around the clock (literally)

![excel-time-series-bubble-chart-how](https://chandoo.org/wp/wp-content/uploads/2008/08/excel-time-series-bubble-chart-how.png "excel-time-series-bubble-chart-how")

* * *

**Update:** Visualization pros Jon Peltier and Jorge Camoes took a critical look at this, nearly fainted 😉 at the carnage of a familiar metaphor and posted their awesome reviews here:

> [Rock around the clock](http://peltiertech.com/WordPress/2008/08/14/rock-around-the-clock/)
>  by Jon, he recommends a line chart over this for all the valid reasons  
> [Charting around clock](http://charts.jorgecamoes.com/charting-around-the-clock/)
>  by Jorge, he suggests a neat looking 12 pointed radar chart as an alternative.

Both these are indeed fine examples of how shaking a familiar metaphor (analog clock) or way doing (usual bar chart for 24 hours) can bring a great discussion and excellent alternatives out of passionate people. Do read them 🙂

* * *

**What you are seeing is essentially 2 bubble charts tweaked** to look like wall-clocks with bubbles around the 12 positions.

This can be an interesting addition to your dashboards or daily report. Excited to find out how this is done? read on.

### 1\. Get your data ready to plot it around the clock (circle)

![sample-12-hour-data](https://chandoo.org/wp/wp-content/uploads/2008/08/sample-12-hour-data.png "sample-12-hour-data") Let us build the above graph using fictitious page view data for each of the 12 hours since midnight till noon. The data is shown aside.

In order to create the around the clock affect we need to plot each of these hourly values around a circle at 12 points. Now, without getting all mathemat_icky_ to scare you, lets try to come up with simple explanation to find all the 12 points around the circle:

Assuming the radius of clock or our chart circle is 100,

*   Clock has 12 hour positions, thus each one is 30° (360°/12)
*   The first point’s x value would be: `SIN(30°)*100`
*   and y value would be: `COS(30°)*100`
*   For each of the other 11 points, we just need to use the multiples of 30: 60, 90, 120, .., 360
*   in excel spreadsheet you can find the values by `ROUND(SIN(RADIANS(hour*30))*100,0), ROUND(COS(RADIANS(hour*30))*100,0)`
*   We have to [convert the degrees to radians](http://www.teacherschoice.com.au/Maths_Library/Angles/Angles.htm)
     since SIN(), COS() accept only radians as inputs

Once we are done, the data should look like this:  
![](https://chandoo.org/wp/wp-content/uploads/2008/08/x-and-y-values-bubble-chart.png "x-and-y-values-bubble-chart")

### 2\. Plot the Bubble Chart

![](https://chandoo.org/wp/wp-content/uploads/2008/08/insert-bubble-chart-microsoft-excel.png "insert-bubble-chart-microsoft-excel")This is the easy part, just select the cells containing x,y and page view values and insert new chart, select bubble as the chart type. Make sure you have mentioned the x,y, and bubble sizes in correct places.

The fun part begins after creating the chart, as the dimensions may be skewed and you may get egg like circle, so adjust the dimensions and your 12 hour clock view is ready to go.

Use the same process to create another clock for hours from noon till midnight and juxtapose them on that dashboard or report, send it across to your boss or team, let the conversation begin 😀

### Download the template and play with it

Like this technique, why don’t you download the [**Data Around Clock – Charting Idea excel**](https://chandoo.org/wp/wp-content/uploads/2008/08/excel-bubble-chart-around-clock-idea.xls)
 and play with it. Its available on the standard PAHF license (Poke Around, Have Fun)

**Fun ways to enhance these charts:**

*   Overlay a clock diagram in the background
*   Use sky color for the background, thus one clock has darker shades and other has brighter shades
*   Bubbles themselves can be colored as Sun colors, bright orange to yellow and back to orange

**More on Bubble Charts:** [Why you should star retirement savings really early](http://chandoo.org/wp/2007/04/04/start-early/)
, [Olympic Medals per Country in All Years](http://chandoo.org/wp/2008/08/06/olympic-medal-country-year-excel-bubble-chart/)

**More on charting:** [Hack together a thermometer chart](http://chandoo.org/wp/2008/06/26/thermometer-charts-in-excel-howto/)
, [tell a story with min-max charts](http://chandoo.org/wp/2008/08/11/min-max-excel-charts/)
, [73 awesome chart templates, download and wow](http://chandoo.org/wp/2008/03/28/73-free-designer-quality-excel-chart-templates-grab-now-and-become-a-charting-superman/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/plot-time-series-data-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/plot-time-series-data-excel/#respond)
    
*   Tagged under [bubble charts](https://chandoo.org/wp/tag/bubble-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/visualization/)
    , [clock](https://chandoo.org/wp/tag/clock/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [time series data](https://chandoo.org/wp/tag/time-series-data/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousSimulating Dice throws – the correct way to do it in excel](https://chandoo.org/wp/simulate-dice-throws/)

[NextCharts of the Week \[Aug 15\]Next](https://chandoo.org/wp/cool-infographics/)

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
    
    [Reply](https://chandoo.org/wp/plot-time-series-data-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/plot-time-series-data-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/plot-time-series-data-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
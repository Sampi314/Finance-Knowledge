# Creating a Masterchef Style Clock in Excel [for fun] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/masterchef-style-clock-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

Creating a Masterchef Style Clock in Excel \[for fun\]
======================================================

*   Last updated on July 5, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Jo (wife) likes to watch _Masterchef Australia_ ([link](http://www.masterchef.com.au/)
), a cooking reality show every night. Even though I do not find contestant’s culinary combats comforting, occasionally I just sit and watch. You see, I like food.

The basic premise of the program is _who cooks best in given_ time. To tell people how much time is left, they use a clock that looks like this:

![Masterchef Clock - this is how it looks](https://img.chandoo.org/c/mc/masterchef-clock.png "Masterchef Clock - this is how it looks")

The needle indicates how much time is left (much like a stop clock, with a small twist).

One day, while watching such intense battle, my mind went

*   It be cool to make such a clock using _hmm… Excel?_
*   Wouldn’t it be cool to grill a snapper & eat it than watch someone else do it

While I cannot share my snapper (or pretty much any other food item) with you, I can share my Masterchef style Excel clock with you. So behold,

### Here comes the Masterchef style Clock in Excel

![Masterchef Style Clock in Excel - Demo](https://img.chandoo.org/c/mc/master-chef-clock-demo.gif "Masterchef Style Clock in Excel - Demo")

### How is it cooked?

Don’t you worry. This recipe is not as complicated as a Masterchef recipe. With enough time & trigonometry, anyone can do it.

The clock (chart) has 2 parts. Dial & rotating hand.

While we can create both of them in one chart, I choose the path of least resistance _i.e._ Make one chart each for Dial & Hand and overlap them nicely.

![Masterchef Clock has 2 parts - Dial (a Radar chart) and Hand (an XY chart)](https://img.chandoo.org/c/mc/masterchef-clock-broken-down.png "Masterchef Clock has 2 parts - Dial (a Radar chart) and Hand (an XY chart)")

### Making the Dial

This is simpler than it looks. All we need is numbers 60 thru 5 (60,55,50…10,5) in a range & twelve 1s in another range. Then, we select both and make a radar chart. Once you adjust it, it should look like this:

![Clock dial set up using Radar chart](https://img.chandoo.org/c/mc/how-the-dial-is-setup.png "Clock dial set up using Radar chart")

### Making the Rotating Hand

The hand is nothing but a line on a scatter plot with (0,0) as one point & (x,y) as another point. To calculate (x,y) we need to know how many degrees our hand should be rotated.

Hand of our clock starts at 60 and rotates clock-wise (duh!). That means if the time completed is 5, our clock’s hand should be 300 away from initial position.

Thus, x = sin(300), y = cos(300)

Same in Excel would be SIN(RADIANS(30)), COS(RADIANS(30))

For more on this calculation, refer to [Spoke Chart Technique](http://chandoo.org/wp/2012/07/02/how-to-make-a-spoke-chart/ "How to make a Spoke Chart")
.

### Running the clock (using VBA)

Our job is not done when the clock is assembled. We must give it batteries _thru VBA._

The basic logic for running the clock is simple:

*   When clock is running
*   Check if it next second yet
    *   Move the hand (by modifying the value of done seconds)
*   If not, just wait

You can see the code (and break it if you must) in the download file.

### Download Excel Clock & Play with it

[**Click here to download this clock**](https://img.chandoo.org/c/mc/master-chef-clock.xlsm)
. Examine the macros assigned to the buttons. Play & Pause the clock.

### Do you watch Masterchef?

Of course I am kidding. What I am really keen to know is _**do you make any clock / timer related things in** **Excel?**_ I use timer features often to add animation, count-down features to my workbooks. They work really well.

What about you? Have you used such techniques? What is your experience? Please share using comments.

PS: If you must know, I prefer Amazing Race to Masterchef. I guess I get more pleasure watching people run around globe than run around in a kitchen.

### More Charting Recipes

If you like a well cooked chart, we have got one too many in our pantry. Check out,

*   [Spoke chart in Excel](http://chandoo.org/wp/2012/07/02/how-to-make-a-spoke-chart/ "How to make a Spoke Chart")
    
*   [Grammy bump chart](http://chandoo.org/wp/2011/02/22/the-grammy-bump-chart-in-excel/)
    
*   [Competitive Analysis Chart](http://chandoo.org/wp/2010/10/25/competition-analysis-charts/)
    
*   [Polar Clock in Excel](http://chandoo.org/wp/2008/08/18/donut-clocks/)
    
*   [Data around the clock](http://chandoo.org/wp/2008/08/14/plot-time-series-data-excel/)
    

Or consider joining my Excel School program to cook fine Excel workbooks & charts. [**Click here**](http://chandoo.org/wp/excel-school/ "Excel School Online Training Program from Chandoo.org")
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [25 Comments](https://chandoo.org/wp/masterchef-style-clock-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/masterchef-style-clock-in-excel/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [clock](https://chandoo.org/wp/tag/clock/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [radar charts](https://chandoo.org/wp/tag/radar-charts/)
    , [scatter charts](https://chandoo.org/wp/tag/scatter-charts/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [timer](https://chandoo.org/wp/tag/timer/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

[PrevPreviousFind the last date of an activity](https://chandoo.org/wp/find-the-last-date-of-an-activity/)

[NextVisualizing Roger Federer’s 7th Wimbledon Win in ExcelNext](https://chandoo.org/wp/visualizing-roger-federers-7th-wimbledon-win-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/masterchef-style-clock-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/masterchef-style-clock-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/masterchef-style-clock-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# Celebrating India's Worldcup Cricket Victory - In Excel Dashboard Style! » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/cricket-worldcup-dashboard

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Celebrating India’s Worldcup Cricket Victory – In Excel Dashboard Style!
========================================================================

*   Last updated on April 15, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_I know I am late to the party, but better late than…, uh! forget it._

As the keen readers of our blog knew, I like cricket and I show my enthusiasm by making an [excel dashboard](http://chandoo.org/wp/2008/10/24/sports-statistics-dashboard-in-excel/ "Cricket statistics dashboards in Excel")
 (or [infographic](http://chandoo.org/wp/2010/02/26/sachin-tendulkar-odi-poster/ "Sachin Tendulkar 200 Runs in One Day Internationsl - a Poster")
) whenever Indian team reaches a major milestone. So naturally, I was super excited when we won the ICC Worldcup 2011. Last time Indian won the event was in 1983 and my idea of a dashboard at that time was a bottle of milk and jingo-bell, my favorite shake-to-make-annoying-noise toy. I think our latest world-cup victory deserves something more than that. So here we go.

Excel Dashboard to Celebrate India’s World-cup Victory (2011)
-------------------------------------------------------------

([Click here to see larger version](http://chandoo.org/img/vp/India-wins-cricket-worldcup-excel-dashboard-large.png)
)

![Celebrating India's Worldcup Cricket Victory with Excel Dashboard](https://chandoo.org/img/vp/India-wins-cricket-worldcup-excel-dashboard-snapshot.png)

How is this Dashboard constructed?
----------------------------------

**This dashboard was one of the most difficult ones I built, because I did not know what to put in the dashboard.** I know that the dashboard should reflect our team’s hardwork, journey, outstanding performances but I had no clue which format & layout exposed these qualities. So I took a lot of time drawing up sketches of _possible dashboards_ before hitting on the present layout. Once I came-up with the layout, the actual dashboard took me about 4 hours to make (and may be another 4 for polish).

### Here are some of the techniques used in the dashboard:

*   The dashboard is divided in to 3 areas – Highlights, our journey to the victory and best performances.
*   **Highlights:** This section shows overall summary of all the 9 matches India have played. It shows some interesting statistics, how much our top players contributed to our victory etc.  
    **Techniques used:** All parts of this are made with text boxes and [simple text formulas](http://chandoo.org/excel-formulas/text-functions.html)
    .
*   **Our Journey to victory:** This was the most time consuming & intense part of the dashboard as I made **_this portion interactive_**. The left side shows all the matches we have played by date and the results. When you select a particular match, the right side portion shows a match summary. This includes match venue, result, toss details, India’s top 3 batsmen, top 3 bowlers, photos of India’s best batting & bowling performers, oppositions score, best batsman, bowler, their stats. It also shows the country flags etc.  
    **Techniques used:** The click to select as described in [on-demand charts article](http://chandoo.org/wp/2011/04/07/show-details-on-demand-in-excel/)
    , [conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
    , [picture links](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
    , [more picture links](http://chandoo.org/wp/2009/07/13/product-catalogs/)
    , [LARGE formula](http://chandoo.org/excel-formulas/large.html)
    .  
    The most difficult part of this was to get a _**moving arrow**_ that would change its position based on which match is selected. I did this with [picture links](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
    , [offset formula](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
     and a [dynamic named range](http://chandoo.org/wp/2009/10/15/dynamic-chart-data-series/)
    . (Examine the named range _movingArrow_).
*   **Best performances (top 10):** In this area, I showed the best batting, bowling, catching, partnership performances for all the matches in World-cup (not just India’s matches).  
    **Techniques used:** All the charts are made in Excel 2010 [using solid bar conditional formatting](http://chandoo.org/wp/2010/05/19/new-features-in-excel-2010-conditional-formatting/)
     & picture link based techniques. Later, I just copied them and pasted as images so that they look same in Excel 2007 also.

### Colors & Fonts:

*   I choose the blue color as it is team India’s jersey color. I used orange to contrast the best performances.
*   The fonts are Bookman Old Style & Meriyo UI.

Download the Cricket World-cup Dashboard Excel file:
----------------------------------------------------

[Click here to download the locked workbook](https://img.chandoo.org/d/worldcup-dash-dl.xlsm)
. \[[mirror](http://cid-b663e096d6c08c74.office.live.com/view.aspx/Public/vis-pro/worldcup-dash-dl.xlsm)\
\]

**Why lock it?** I am giving away unlocked version of this workbook + a 36 minute lesson to all the customers who buy [Excel Dashboard Tutorial](http://chandoo.org/wp/training-programs/excel-dashboard-tutorial/)
 or [Excel School Dashboards](http://chandoo.org/wp/excel-school/)
.  So if you want an unlocked copy of this, go ahead and get either of them. (If you have previously bought one of these products, you will receive an email with instructions on downloading your bonus.)

Credits:
--------

All the data for the dashboard came from [espncricinfo.com](http://espncricinfo.com/)
.

Special thanks to _**Ravindra**_, my assistant, for compiling the data.

How do you like the Dashboard?
------------------------------

I was afraid whether I can do justice to our team’s glorious world-cup victory in a dashboard. So I kept on delaying this. But in the end, I am happy with the dashboard. It tells the story of our team’s journey and highlights best performers.

**What do you think?** Did you like this dashboard? How would you have designed it?

As an aside, Many of our readers know only about [_cricket_](http://en.wikipedia.org/wiki/Cricket_%28insect%29)
 that chirps. So I want to ask, did this dashboard make any sense to you?

### Other Awesome Resources on Excel Dashboards:

*   [Excel Info-graphic Poster to Celebrate Sachin’s 200 runs](http://chandoo.org/wp/2010/02/26/sachin-tendulkar-odi-poster/)
    
*   [Excel Dashboard with 10007 comments data](http://chandoo.org/wp/2010/11/24/10k-comments-excel-dashboard/)
    
*   [Excel Dashboard to prove that Hui is awesome](http://chandoo.org/wp/2011/01/14/birthday-gift-hui/)
    
*   More on [Excel Dashboards](http://chandoo.org/wp/excel-dashboards/)
    
*   **Want to make dashboards using Excel – [Join Excel School](http://chandoo.org/wp/excel-school/)
    .**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [32 Comments](https://chandoo.org/wp/cricket-worldcup-dashboard/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/cricket-worldcup-dashboard/#respond)
    
*   Tagged under [camera tool](https://chandoo.org/wp/tag/camera-tool/)
    , [cricket](https://chandoo.org/wp/tag/cricket/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [databars](https://chandoo.org/wp/tag/databars/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [picture link](https://chandoo.org/wp/tag/picture-link/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousHow to make a 5 Star Chart (Similar to Amazon)](https://chandoo.org/wp/how-to-make-a-5-star-chart/)

[NextAre You Ready for Online VBA Classes? I need your help!Next](https://chandoo.org/wp/online-vba-classes-survey/)

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
    
    [Reply](https://chandoo.org/wp/cricket-worldcup-dashboard/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/cricket-worldcup-dashboard/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/cricket-worldcup-dashboard/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
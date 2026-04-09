# Is this a FIFA worldcup of late goals? Lets ask Excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/fifa-worldcup-goal-timing-analysis

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Is this a FIFA worldcup of late goals? Lets ask Excel
=====================================================

*   Last updated on June 25, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Just like millions of viewers around the world, I too have been spending hours watching FIFA world cup football matches on TV. I don’t like spending hours watching TV. But when its FIFA world cup time (which is once every 4 years), I am glued to the idiot box. Blame it on PaWaRa, my school teacher in 8th grade who instilled this passion.

So while watching the match day before yesterday (it was Holland vs. Chile), the commentator said, “This has been a world cup of late goals” as both teams maintained 0-0 until 77 minute mark when Leroy Fer scored a goal for Holland.

That got me thinking,

_**Is this really a world cup of late goals?**_

But I quickly brushed away the thought to focus on the match.

Later yesterday, I went looking and downloaded all the goal data for 2006, 2010 & 2014 FIFA world cup matches (2014 data for first 36 matches).

Lets examine the hypothesis _“2014 has been a world cup of late goals”._

### Attempt 1: Distribution of goals on 90 minute timeline

There have been 147 goals in 2006, 145 goals in 2010 and 117 goals in 2014 (as of 24th June, 2014). Out of all these goals, only 5 goals were scored after the 90 minute mark. So I ignored these 5 goals for our analysis.

Also, I assumed that any goals scored in injury time are part of the 45th minute or 90th minute mark (for simplicity).

One more: I have included data only up to 23rd of June, 2014 – so only first 108 goals of this edition are considered. This reflects accurately the moment commentator made that remark.

Lets see the chart.

![Distribution of goals in fifa worldcup (2006, 2010 & 2014) by time - All goals](https://img.chandoo.org/vp/goal-distribution-all.png)

Each dot depicts a goal. The dots are filled with semi-transparent color, so we can see the density of goals at each point of the 90 minute timeline.

As you can see, there is no clear pattern of late goals in 2014.

While we could see higher density of dots in first half of 2006 & 2010 editions, that can be attributed to having full data vs. partial data (for 2014).

### Attempt 2: % of goals scored in each 15 minute block

May be if we look at % of goals scored in each 15 minute block, we can conclude something.

![Distribution of goals in FIFA worldcup - All goals + 15 minute blocks](https://img.chandoo.org/vp/goal-distribution-all-with-15min-blocks.png)

This gives an indication that 2014 world cup indeed has slow first half. But then you also see conflicting proof with more goals scored in last 30 minutes in 2006 & 2010 editions.

### Attempt 3: What if we consider only first 100 goals in each world cup

Lets remove some noise. The commentator said this has been a world cup of late goals. If we consider only first 100 goals (ie first 30 odd matches) in each world cup may be we can see how 2014 fares compared to 2010 & 2006 editions.

![Goal distribution - FIFA worldcup - first 100 goals in 2006, 2010 & 2014 editions](https://img.chandoo.org/vp/goal-distribution-for-first-100.png)

Here too the chart does not reveal much. If anything, we can conclude that 2006 has clear pattern of high number of goals in first & last 30 mins.

While 2014 has high density in the last 30 mins, it has good distribution throughout the 90 minutes.

### Attempt 4: Lets consider only the first goal of each match

I guess the impression of _slowness_ is created if you have to wait a lot of time to see the first goal in any match. After that usually things pick-up.

So what if we consider only the first goal times in each match.

This is what we get.

![Goal distribution - only first goal in each match - FIFA worldcup - 2006, 2010 & 2014.](https://img.chandoo.org/vp/goal-distribution-first-goal-of-match.png)

Now this is clear. You can see that 2014 has high density in first half. Remember, for 2014 only 36 matches data is considered where as 2010 & 2006 have 64 matches data.

But we can also see the high density of goals in first half for 2006.

If you look at the average wait time for first goal, 2006 is the least with 30 mins and 2014 is in second place.

So if any, we could say 2010 was the world cup of late goals.

### Attempt 5: Cumulative % of goals by minute

If a particular world cup has many late goals, then it will show thru when we plot cumulative goal distribution (as a %).

Here is what we get.

![Cumulative distribution of goals in FIFA worldcup - 2006, 2010 & 2014 editions](https://img.chandoo.org/vp/cumulative-goals-pct-by-minute.png)

From this you can see that 2014 line lags behind 2006 & 2010 for first 60 minutes, before climbing to top place.

This does indicate that 2014 has a lot of late goals.

But the difference is negligible, so we cannot really say much.

### What do you think?

I do feel that _some of the matches are slow to watch._ But this is purely because I have been looking forward to the world cup and could not wait for the action.

**What do you think?** Do you think this has been a world cup of late goals?

Also, tell me what you think about this analysis? Wow or meh?

### About the data

Thanks to [Soccer Worldcups](http://www.thesoccerworldcups.com/world_cups.php)
 & [Wikipedia](http://en.wikipedia.org/wiki/List_of_2014_FIFA_World_Cup_matches)
 from where I obtained this data.

### More like this

If you want to dig a few a more charts and see how they can help you analyze data, check out:

*   [Analyzing 20,000 comments using Excel](http://chandoo.org/wp/2012/07/19/analyzing-20000-comments/)
    
*   [Thank you Sachin, a dashboard on cricket](http://chandoo.org/wp/2013/11/15/srt200/)
    
*   [Visualizing Roger Federer’s Wimbledon victory](http://chandoo.org/wp/2012/07/09/visualizing-roger-federers-7th-wimbledon-win-in-excel/)
    
*   [World education rankings – analyzed](http://chandoo.org/wp/2010/12/20/world-education-rankings-visualization/)
    
*   [More such charts](http://chandoo.org/wp/tag/visualization-projects/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [26 Comments](https://chandoo.org/wp/fifa-worldcup-goal-timing-analysis/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/fifa-worldcup-goal-timing-analysis/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [fifa world-cup](https://chandoo.org/wp/tag/fifa-world-cup/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [scatter plot](https://chandoo.org/wp/tag/scatter-plot/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousVote for your favorite US state migration dashboard](https://chandoo.org/wp/vote-for-your-favorite-us-state-migration-dashboard/)

[NextCP012: Top 10 Excel Keyboard Shortcuts for youNext](https://chandoo.org/wp/cp012-top-10-keyboard-shortcuts/)

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
    
    [Reply](https://chandoo.org/wp/fifa-worldcup-goal-timing-analysis/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/fifa-worldcup-goal-timing-analysis/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/fifa-worldcup-goal-timing-analysis/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
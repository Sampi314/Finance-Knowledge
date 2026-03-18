# Fish Eye Effect for highlighting selection - Is it effective? [Advanced Charting] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/pay-gap-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Fish Eye Effect for highlighting selection – Is it effective? \[Advanced Charting\]
===================================================================================

*   Last updated on May 26, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

A few days back, WSJ ran a visualization titled “[What’s your pay gap?](http://graphics.wsj.com/gender-pay-gap/)
” It depicts median pay gap between female & male workers in 422 different professions in USA. The chart uses fish eye effect to highlight the selected profession. _**See below demo to understand the effect**_.

[https://chandoo.org/wp/wp-content/uploads/2016/05/wsj-fisheye-demo.mp4](https://chandoo.org/wp/wp-content/uploads/2016/05/wsj-fisheye-demo.mp4)

### Discussion: Is the Fish Eye Effect worth it?

In this context, fish eye effect is useless. As we have too much data, the fish eye effect becomes mere eye candy and draws attention away from important matters at hand.

That said, it is a cool idea to use with smaller data sets.

### Implementation: Fish Eye Effect in Excel

Out of curiosity, I wanted to implement the fish eye effect in Excel. We can highlight selected dots using simple algebra. To stretch the chart elements to left & right requires VBA. Since VBA creates portability issues, let’s focus on the algebra based fish eye effect.

_**Here is a quick demo of the final outcome.**_

[https://chandoo.org/wp/wp-content/uploads/2016/05/fisheye-effect-demo.mp4](https://chandoo.org/wp/wp-content/uploads/2016/05/fisheye-effect-demo.mp4)

Assuming you have a bunch of X & Y values (Profession & Salary in this case), to generate the new X&Y values with fish eye effect for a particular X value (say X1),

*   Define gap as an integer value, indicating the gap to either side of highlighted value at X1. For the above example, Gap = 10.
*   Calculate scaling factor for the left side of Fish Eye as (X1-gap)/X1
*   Scaling factor for right side of Fish Eye as (Max X – X1 – gap)/(Max X – X1)
*   Use these scaling factors to calculate new X values for all dots.
*   Create a scatter plot with these new X values and Y values.
*   Apply special formatting to X1 & Y1 values thru another series.
*   Set up a form control or VBA to change X1.
*   Your interactive fish eye chart is ready.

### Alternative: Closing the gaps in Pay Gap Fish Eye chart

Okay, as you can see both original and Excel implementation of Fish Eye charts are mediocre. So let’s improve them. For this type of data, we can use interactive tables so that users can filter, sort and highlight the data any way they want. This allows for flexible exploration of data.

Here is a quick demo of the _interactive table_ style visualization of Pay Gap data.

[![pay-gap-analysis-table-explained](https://chandoo.org/wp/wp-content/uploads/2016/05/pay-gap-analysis-table-explained.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/pay-gap-analysis-table-explained.png)

**Interactive Pay Gap Analysis Table – Construction summary**

*   Construct 5 pivot tables, one for each sort order.
*   Create a slicer on Profession Category and link it to all 5 pivots.
*   Set up a form control to figure out sort order (and dynamically fetch one of the 5 pivot table data sets, using CHOOSE formula)
*   Fetch 20 rows of selected pivot table data (use scroll bar position to determine which 20 rows)
*   Apply conditional formatting to the 20 rows based on criteria specified.
*   Calculate summary information and display it at the top.

**Here are the key ideas used during construction of this:**

*   [Scrollable KPI Dashboard](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
     – for scrollable list.
*   [CHOOSE formula](http://chandoo.org/wp/2014/07/16/introduction-to-choose-function/)
     – for creating dynamic named range
*   [Conditional Formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
     – for highlighting professions
*   [Slicers](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
     for filtering a profession
*   [Form controls](http://chandoo.org/wp/2011/03/30/form-controls/)
     for sorting & highlight option selection

### Video: Fish Eye vs. Interactive Table – Walkthru

Here is a quick video walk thru of both approaches along with some commentary and explanation.

You can [watch the video on our YouTube Channel](https://youtu.be/r5gIt2jDgOw)
 too.

### Download the workbook

[**Click here to download the Fish Eye effect workbook**](https://chandoo.org/wp/wp-content/uploads/2016/05/fisheye.xlsx)
. It contains both fish eye and interactive table visualizations. Examine the calculations tab for all the formulas.

### How would you visualize this data?

Do you like the Fish Eye effect chart? How would you visualize this data? Please share your thoughts and implementations in the comments.

### More case studies

Check out below tutorials and case studies to learn how to visualize complex data in Excel.

*   [How Trump Happened – in Excel](http://chandoo.org/wp/2016/03/02/how-trump-happened-in-excel/)
    
*   [One more gender equality gap chart – improved](http://chandoo.org/wp/2013/11/05/gender-equality-gap-interactive-chart/)
    
*   [Suicides vs. Murders – an interactive chart](http://chandoo.org/wp/2011/09/09/suicides-murders-interactive-chart/)
    
*   [Visualizing world education rankings](http://chandoo.org/wp/2010/12/20/world-education-rankings-visualization/)
    
*   [Analyzing survey data using in-cell charts](http://chandoo.org/wp/2010/04/01/incell-panel-chart/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [3 Comments](https://chandoo.org/wp/pay-gap-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/pay-gap-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [fish eye effect](https://chandoo.org/wp/tag/fish-eye-effect/)
    , [Highlight](https://chandoo.org/wp/tag/highlight/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [visualization principles](https://chandoo.org/wp/tag/visualization-principles/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousExcel Tips, Tricks, Cheats & Hacks – Readers Edition](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-readers-edition/)

[NextShow more of your workbook on screens \[quick tip\]Next](https://chandoo.org/wp/show-more-of-your-workbook-on-screens/)

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
    
    [Reply](https://chandoo.org/wp/pay-gap-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/pay-gap-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/pay-gap-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
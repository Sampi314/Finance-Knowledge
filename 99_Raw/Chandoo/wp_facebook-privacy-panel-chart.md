# Evolution of Privacy Policies on Facebook - a Panel Chart in Excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/facebook-privacy-panel-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

Evolution of Privacy Policies on Facebook – a Panel Chart in Excel
==================================================================

*   Last updated on May 13, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**There is a chart called “[Evolution of Privacy on Facebook](http://mattmckeon.com/facebook-privacy/)
” going around on the web.**_ The chart made by Matt Mckeon, a developer in IBM’s visual communications lab has created quite a stir in the interwebs. You can a small animated version of that chart below:

![Evolution of Facebook Privacy - Animated Chart](https://chandoo.org/img/vp/evolution-of-facebook-privacy.gif)

While _**Matt**_ made a few mistakes with the chart, I think this is a stunning way to depict how facebook privacy policies have changed since 2005.

(**How to read the above chart:** It is radar-like chart, with logarithmic scale for spoke axis. The concentric circles depict number of people – inner most is you, then your friends, friends’ friends, entire facebook and entire internet. Privacy is measured on 9 areas – Name, Picture, Demographics, Extended Profile Data, Friends, Networks, Wall posts, Photos, Likes of you. A portion of the radar is shaded blue if that information is available to that portion by default.

For eg. in 2005 what you liked (likes) is known only to you. But, by 2010 entire internet can know what you liked.

Also, the data is based on Matt’s observations. [More…](http://mattmckeon.com/facebook-privacy/)
)

**I liked this chart and challenged myself to build the same in excel.** Then as I was exploring the data (hidden inside the [source code of his visualization](http://mattmckeon.com/facebook-privacy/facebook-privacy.pjs)
), I had a better idea. “Why not [make a panel chart](http://chandoo.org/wp/2010/05/12/introduction-to-panel-charts-using-excel-tutorial-template/)
“.

So I made this,

### Evolution of Privacy Policies on Facebook

![Evolution of Privacy Policies on Facebook - an Excel Panel Chart](https://chandoo.org/img/vp/evolution-of-privacy-on-facebook-s.png)

\[[click here for a larger version](http://chandoo.org/img/vp/evolution-of-privacy-on-facebook-l.png)\
\]

### How to read this chart?

![Privacy of your name in Facebook - 2005 to 2010](https://chandoo.org/img/vp/privacy-of-your-name-2005-2010-facebook.png)Each panel depicts how privacy policies have changed for one area of privacy since 2005 to 2010. So, for eg. if you are looking at the “Name” panel,

*   Your Name was visible only to 1000 people in 2005 but in 2010, Entire internet (1.8 Billion) can see your name on Facebook.
*   The dull gray color portion shows entire Internet population (it grew from 1B in 2005 to 1.8B in 2010).
*   Red color portion shows how much of internet population can get your data from Facebook.
*   The y-axis is log 10 scale, meaning each increment in y-axis value is actually 10 times more than previous value.
*   The 3 lines indicate your friends, network and entire face book users respectively. Facebook users is shown on top in black color.

### How is this chart made?

1.  After downloading the source code of original visualization by Matt, I just copied the data points from code to excel.
2.  Then I cleaned and [transposed the data](http://chandoo.org/wp/2009/11/18/transpose-excel-rows-columns/)
     so that area charts can be made.
3.  The chart panels are [combo-charts](http://chandoo.org/wp/2009/07/02/secondary-axis-combination-charts-howto/)
     with both areas (red and gray portions) and lines (facebook, network, friend counts).
4.  Once made the first chart, I just duplicated it 8 more times and changed source points. (press CTRL+D to duplicate).
5.  A little bit of alignment and formatting to make it look clean and simple. \[[chart alignment tip](http://chandoo.org/wp/2008/08/28/aligning-charts-objects-excel-layout-tip/)\
    \].

### Known issues in this chart:

1.  The horizontal axis (dates) are not equally spaced. The measurement times and accuracy are unknown.
2.  I am not 100% sure if areas are a good way to depict such data. But they seem ok to me.

### Download the Excel File:

[Click here to download the excel file](https://img.chandoo.org/d/facebook-privacy-panel-chart.xls)
 \[[Excel 2007 version here](https://img.chandoo.org/d/facebook-privacy-panel-chart.xlsx)\
\] with facebook privacy policies excel panel chart. Play with it a bit to understand how it works.

### How would you improve or visualize such data?

I used time as the axis and privacy areas as panels since the message is “how privacy policies have changed since 2005”. But I am sure you would love to explore this data in a different way. Go ahead and get the download file and make your own charts. Then share them using comments.

_**Also, suggest alterations or your impressions on this chart. Discuss.**_

### Other Visualizations Worth a look:

*   [One Day International Cricket Statistics of Sachin Tendulkar – an info-graphic poster](http://chandoo.org/wp/2010/02/26/sachin-tendulkar-odi-poster/)
    
*   [Understanding Flu Trends – a Dynamic Chart](http://chandoo.org/wp/2010/01/22/flu-trends-chart-in-excel/)
    
*   [History of Excel – a timeline visualization](http://chandoo.org/wp/2010/01/13/history-of-excel-timeline/)
    
*   [Many more…](http://chandoo.org/wp/tag/visualization-projects/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/facebook-privacy-panel-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/facebook-privacy-panel-chart/#respond)
    
*   Tagged under [area charts](https://chandoo.org/wp/tag/area-charts/)
    , [Chart Busters](https://chandoo.org/wp/tag/chart-busters/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [facebook](https://chandoo.org/wp/tag/facebook/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [matt mckeon](https://chandoo.org/wp/tag/matt-mckeon/)
    , [panel charts](https://chandoo.org/wp/tag/panel-charts/)
    , [radar](https://chandoo.org/wp/tag/radar/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [transpose](https://chandoo.org/wp/tag/transpose/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

[PrevPreviousIntroduction to Panel Charts using Excel – Tutorial & Template](https://chandoo.org/wp/introduction-to-panel-charts-using-excel-tutorial-template/)

[NextWhat is new in Microsoft Excel 2010? \[Office 2010 Week\]Next](https://chandoo.org/wp/what-is-new-in-excel-2010/)

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
    
    [Reply](https://chandoo.org/wp/facebook-privacy-panel-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/facebook-privacy-panel-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/facebook-privacy-panel-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
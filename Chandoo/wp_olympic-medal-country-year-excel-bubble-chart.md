# Doing the NY times Olympic medals by country year visualization in excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/olympic-medal-country-year-excel-bubble-chart

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Doing the NY times Olympic medals by country year visualization in excel
========================================================================

*   Last updated on August 6, 2008

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

When I saw the [Olympic medals won by each country by year](http://www.nytimes.com/interactive/2008/08/04/sports/olympics/20080804_MEDALCOUNT_MAP.html)
 infographic on nytimes my jaw almost dropped, go ahead see it and come back, I am sure you will love it too.

It is one of the coolest visualizations I have seen in the recent past and I see [infographics](http://chandoo.org/wp/category/cool-infographics/)
 all the time, its my passion.

So, I wanted to see **if this infographic can be done in Excel**, not pixel to pixel, but something close enough to pamper my ego. I was able to create something that looked like this:

![olympic-medals-by-country-excel-chart](https://chandoo.org/wp/wp-content/uploads/2008/08/olympic-medals-by-country-excel-chart.gif "Olympic-medals-by-country-excel-chart")

Download the **[Total Olympic medals won by each country since 1896 excel sheet](https://chandoo.org/wp/wp-content/uploads/2008/08/olympic-medals-won-by-country-excel-chart.zip)
** and play with it.

**If you want to know how this is done, read on** 🙂  

### 1\. My first challenge is to get the Olympic medal data per country

Thankfully, [Olympics site](http://www.olympic.org/uk/games/index_uk.asp)
 has the medal counts by country data for each of the 25 editions of the summer games, \[[click here for 1896](http://www.olympic.org/uk/games/past/table_uk.asp?OLGT=1&OLGY=1896)\
\] I have copy-pasted the data to my sheet.

### 2\. Next challenge is to find average latitude, longitude for all countries in the world

Thankfully [CIA World fact book](https://www.cia.gov/library/publications/the-world-factbook/fields/2011.html)
 has the exact data for each country in a table, another ctrl+c, ctrl+v and I have the data in my sheet. \[slightly refined data can be found on [maxmind](http://www.maxmind.com/app/country_latlon)\
 as well\]

### 3\. Now, the data is not clean

Unfortunately the data copied from Olympics site and CIA fact book doesn’t match as country names were different (USA, United States, United States of America for eg.), country names kept changing (do you know that Australia was called as Australasia sometime back.. :D). So I had to do quite some clean up (mainly using vlookup, filtering unique items etc.)

Finally, I had the data in a tabular format, country names, latitude, longitude, total medals won in rows, Olympic years in columns (1896 to 2004, except 1916, 1940 and 1944 when the games were canceled)

I had to convert latitude and longitude to y and x co-ordinates respectively so that I can plot them on 2 dimensions. I used this logic to do it:

> `x=(180+longitude)*(map-width/360)   y=(90-latitude)*(map-height/180)`

### 4\. Add a scroll bar form control and use it to select the year from 25 Olympic years

This was the easy step. I selected Menu > View > Toolbars > Forms to show the forms toolbar and then inserted a scroll bar control to my sheet. Then I associated it with a cell my sheet and limited the values to change between 1 and 25 (each increment for one of the 25 Olympic years)

![excel-forms-scroll-bar](https://chandoo.org/wp/wp-content/uploads/2008/08/excel-forms-scroll-bar.png "excel-forms-scroll-bar")

Now, I have associated this scroll bar cell to fetch one Olympic years worth of data.

### 5\. Create a bubble chart with the medal data

Now that I have the data in the format of x, y co-ordinates, medal count for each country for the selected year, I have created a bubble chart with this information, showing bubbles at each pair of (x,y) in the list.

### 6\. Finally, show an outline map of the world in the background

![excel-bubble-chart-Olympic-medal-count](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/excel_charts/excel-bubble-chart-olympic-medal-co.png)

The last step was easy, I searched for an outline map of the world and used it as my chart background, even though this is not part of the original NY Times infographic, it helps me in ensuring that the bubbles are indeed shown in the right places.

![olympic-medals-bubble-chart-overlap](https://chandoo.org/wp/wp-content/uploads/2008/08/olympic-medals-bubble-chart-overlap.png "olympic-medals-bubble-chart-overlap")Of course **there are some differences between my infographic of Olympic medal count and that of NY Times’**, mainly,

*   The bubbles overlap, but there is nothing I can do about it without writing additional logic. But as [Nathan points out](http://flowingdata.com/2008/08/06/map-of-olympic-medals-in-bubble-geographic-form/)
    , non-overlapping bubbles may be slightly inaccurate.
*   The other is, color of bubbles doesn’t change based on the continent it belongs to. Well, this can be done by editing the bubble colors manually, so I gave up.
*   Finally, very few countries are omitted in this, mainly due to geopolitical changes, like Germanies getting united, Koreas getting separated, more countries becoming China :D, I did clean up 99% of the data, but there is always a troublesome country you never heard of.

Make sure you download and play with [total Olympic medals won by each country since 1896 excel sheet](https://chandoo.org/wp/wp-content/uploads/2008/08/olympic-medals-won-by-country-excel-chart.zip)

_What do you think of this?_

**Also see:** [The art of excel charting – making ubercool dashboards](http://chandoo.org/wp/2007/06/27/the-art-of-excel-charting/)
  
[Junk the default charts, use this art grade templates instead](http://chandoo.org/wp/2008/03/28/73-free-designer-quality-excel-chart-templates-grab-now-and-become-a-charting-superman/)
  
[Did you fire a bullet graph today?](http://chandoo.org/wp/2008/07/21/dashboard-bullet-graphs-excel/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [39 Comments](https://chandoo.org/wp/olympic-medal-country-year-excel-bubble-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/olympic-medal-country-year-excel-bubble-chart/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/visualization/)
    , [cool](https://chandoo.org/wp/tag/cool/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/tag/cool-infographics/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [experiments](https://chandoo.org/wp/tag/experiments/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [interesting](https://chandoo.org/wp/tag/interesting/)
    , [Olympic medals by country](https://chandoo.org/wp/tag/olympic-medals-by-country/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousVizooalization: 5 things I have learned about visualization at the zoo](https://chandoo.org/wp/visualization-lessons-from-zoo/)

[NextDashboarding Fun – Display Smileys in your excel dashboardsNext](https://chandoo.org/wp/display-smileys-excel-dashboards/)

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
    
    [Reply](https://chandoo.org/wp/olympic-medal-country-year-excel-bubble-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/olympic-medal-country-year-excel-bubble-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/olympic-medal-country-year-excel-bubble-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
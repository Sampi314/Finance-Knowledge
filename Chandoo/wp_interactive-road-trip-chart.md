# Are you ready for 2,000 miles, 15 days & 10 Excel tips road trip? » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/interactive-road-trip-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [personal](https://chandoo.org/wp/category/personal/)
    

Are you ready for 2,000 miles, 15 days & 10 Excel tips road trip?
=================================================================

*   Last updated on June 24, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Learn Awesome Excel Tips while Chandoo is on a road trip](https://img.chandoo.org/rt/2000-miles-10-excel-tips-start-here.png)

Finally my Excel classes in USA are over. It was a lot of fun traveling to new cities, teaching Excel & dashboards to enthusiastic crowds and making new friends. As if that is not fun enough, we (Jo, kids & I) are going on a 2,000 mile, 2 week road trip starting today.

Although I am enjoying all this, I also feel bad for not taking enough time to share new tricks, ideas & techniques with you here. So, I have a wacky, wild & awesome plan for you. _**Join us on our road trip.**_

That is right. You can join me on our road trip and see what I see, learn some pretty cool Excel tricks, all while sipping coffee and stretching legs in the comfort of your office cubicle. No oppressive summer heat, no driving thru a long turn-pike looking for next rest area while your daughter is screaming in the back; ‘daddy, I need to go now.’ or no  drinking three coffees in a row so that you can access free wi-fi and check your email.

So buckle up. Err, I mean unbuckle and join us on this road trip.

### What is going to happen?

Simple. While I am on road, each day I will be posting a new Excel tip or article. I will accompany it with a short snippet of what we are doing, include a photo or two of the beautiful things we are seeing.

### Sounds Exciting, What should I do?

Nothing really. Just follow our journey for next 2 weeks. May be tell your colleagues or friends about it so that they too can enjoy. And if you happen to be in Raleigh or Pittsburgh or DC, ping me. We may be able to catch up.

### So where are we going?

Well, I could tell you all about our Road trip using a map or several bullet points. Heck, I could even use a fancy image to tell you what we are up to. But you know that is not my style. So I have the right thing for you. So I present to you…,

### Interactive Map of our Road Trip

That is right. First take a look at our road trip details:

![Interactive Road Trip Chart in Excel - Demo](https://img.chandoo.org/rt/demo-of-road-trip-calendar.gif)

### How is this chart / map / interactive thingie made?

I wish I can sit here and type out all the little details about this. But I must rush now and pick up our rental car. So here is the recipe in a nutshell.

1.  First I created a Google Map with all the locations we are visiting. ([link](https://mapsengine.google.com/map/edit?mid=zBjd3sIox-qI.k_8TPG4QudOo)
    )
2.  Took a screenshot of the map. Embedded it in to Excel and cropped it.
3.  Assuming the top left of the map is (0,0) and bottom right is (2.2, 3.2) figured out the x,y co-ordinates for all the markers by trial and error. (Hint: apply grid lines at 0.1 so that you can easily find marker positions).
4.  Then created an agenda [table](http://chandoo.org/wp/2009/09/10/data-tables/)
     with below structure.  
    ![Structure of road trip data table - Excel](https://img.chandoo.org/rt/structure-of-road-trip-planner-table.png)
5.  Added a scrollbar form control and set it from 1 to 16. Linked it to a blank cell. (related: [Introduction to form controls](http://chandoo.org/wp/2011/03/30/form-controls/)
    )
6.  Using scrollbar selection, fetched corresponding row details from above table.
7.  Created an XY scatter plot with (x1,y1) and (x2,y2) values for selected row.
8.  Set cropped map image behind the chart’s plot area and resized things until they align ok.
9.  Using text boxes, fetched various details for selected scrollbar value (date, heading, details, Excel tip).
10.  Color and format so that everything looks good.

So there you go. Now, you know how to create your own map / chart / interactive thingie.

### Download Road Trip Interactive chart

[**Click here to download the workbook**](https://img.chandoo.org/rt/road-trip-interactive-chart.xlsx)
 and play with it. Examine the way chart is set up (ungroup it to move things) and various INDEX formulas to understand this better.

### More on Maps & Excel

If you like to combine maps & data, then Excel is not going you help you much (unless you are using either Power View or Geo Flow). But there are a few ways to get maps in Excel. Check out below examples to learn more.

*   [Lithuania at a glance (Choropleth maps in Excel)](http://www.clearlyandsimply.com/clearly_and_simply/2009/01/lithuania-at-a-glance.html)
    
*   [Count-down timer on a map](http://chandoo.org/wp/2011/05/18/vba-classes-countdown-timer/)
    
*   [Visualizing Olympic medals by country](http://chandoo.org/wp/2008/08/06/olympic-medal-country-year-excel-bubble-chart/ "Doing the NY times Olympic medals by country year visualization in excel")
    
*   [Tracking Hurricane Sandy in Excel](http://chandoo.org/wp/2012/10/31/hurricane-sandy-animated-chart/ "Journey of Hurricane Sandy – Animated Excel Chart")
    

So see you tomorrow, from Waynesboro (VA). Until then, stay in your lane and cruise.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/interactive-road-trip-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interactive-road-trip-chart/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [interactive charts](https://chandoo.org/wp/tag/interactive-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [maps](https://chandoo.org/wp/tag/maps/)
    , [personal](https://chandoo.org/wp/tag/personal/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [Scroll Bar](https://chandoo.org/wp/tag/scroll-bar/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [personal](https://chandoo.org/wp/category/personal/)
    

[PrevPreviousWe Want You – Revisited](https://chandoo.org/wp/we-want-you-revisited/)

[NextHow to get VLOOKUP + 1 value?Next](https://chandoo.org/wp/how-to-get-vlookup-1-value/)

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
    
    [Reply](https://chandoo.org/wp/interactive-road-trip-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interactive-road-trip-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interactive-road-trip-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
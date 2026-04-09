# Export YouTube video comments to Excel file? - Free template + Power Query tutorial

**Source:** https://chandoo.org/wp/export-youtube-comments-template

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

How to export YouTube video comments to Excel file? – Free template + Power Query case study
============================================================================================

*   Last updated on May 27, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This week, I am running a contest on YouTube. One of the criteria for picking winners is that they must comment on [my video](https://youtu.be/4K56OSVIzF0)
. So far, I got more than 200 comments. To make my job easier, I want to export video comments to Excel file. Turns out this is easily done once you have a Google developer API key. In this article, let me explain the process how to export Youtube video comments to Excel table.

![Export YouTube comments to Excel](https://chandoo.org/wp/wp-content/uploads/2020/05/export-youtube-comments-to-excel.png)

_You can use this idea to export other data for a video too (views, likes vs. dislikes, listing of all videos in a channel etc.)_

What you need
-------------

You need,

*   The video id
*   Your Google Developer API key – get it from [Dev console](https://console.developers.google.com/)
    
*   _optional – pageToken_ if you want to see comments beyond first 100

The YouTube comments export template
------------------------------------

If you don’t care about the bits & bolts of how this works and just want to use the template, **[please download it here](https://chandoo.org/wp/wp-content/uploads/2020/05/extract-youtube-comments-template.xlsx)
**.

Input these values:

*   Video ID
*   Google API key
*   _optional_ Page Token

Go to comments tab and press ALT+F5 to refresh it.

This template will fetch first 100 comments of any video. If you want more comments:

1.  Fetch the first 100 comments
2.  Make a backup of those comments in a new file
3.  Note the **_nextpageToken_** in the result table column G
4.  Use this value as **page token** for input parameters
5.  Refresh the query and copy the values to backup file
6.  Repeat steps 3 to 5 for every 100 comments

How to get YouTube comments with Power Query?
---------------------------------------------

If you want to know the behind scenes for this little extractor, read on.

### The URL pattern for YouTube Data v3 API

You can use a simple GET request (ie if you paste this URL in a browser or web extract tools like Power Query or Excel’s WEBSERVICE, it will work) to access YouTube Data API ([ref](https://developers.google.com/youtube/v3/docs/commentThreads/list)
).

To see all comment threads in a video, you **use below URL pattern.**

https://www.googleapis.com/youtube/v3/commentThreads?maxResults=100&videoId=VID\_ID&key=\[YOUR\_API\_KEY\]

Notice the red bits. They are the parameters you need.

### How to get the results in Power Query?

**Once you have the necessary parameters** in Power Query – _either by loading an Excel table or setting them up as parameters in PQ,_

Construct the URL by combining parameters with the pattern shown above.

From the URL in a column (named URL), use below code to create a **custom column** to fetch the data.

\=Json.Document(Web.Contents(\[URL\]))

This will fetch a Json document with the entire comment thread tree for first 100 comments.

You want to expand it a few times. This path should work:

Items > Top level comment > Snippet

This will add a bunch of columns with all sorts of detail.

Keep below columns:

*   authorDisplayName
*   authorChannelUrl
*   **_textDisplay_**
*   **_textOriginal_**
*   publishedAt
*   nextPageToken

When done, close & load to see these comments in Excel or Power BI as a table.

How to paginate?
----------------

Unfortunately, the YouTube Data API is not paginated with sequential numbers. Instead you must provide a _pageToken_ with the request to get next 100 comments.

You can build an accumulating function that first gets all the pageTokens with something like [List.Accumulate](https://chandoo.org/wp/multiple-find-replace-list-accumulate/)
.

Once you have such a list, you can then just call the URL for all tokens.

This is just too much hassle for a few hundred comments, but makes perfect sense when you have thousands of comments.

An easier option is to just back-up the data (either manually or thru VBA) and refreshing the query with next page token.

Errors & issues
---------------

**Privacy warning or error:**

![Power Query - Privacy setting (Query editor > File > Query options)](https://chandoo.org/wp/wp-content/uploads/2020/05/privacy-settings-power-query.png)

This is the first one you might encounter. Power Query doesn’t like mixing cell values, parameters etc with web queries. You can **go to Query editor** and adjust query options from File menu to **ignore all privacy warnings**.

You may need to **rebuild the query** to get the results after this step.

**API issues:**

It is a good idea to test the URL from your [Google developer console](https://console.developers.google.com/)
. Make sure you can actually see some results there before trying it with Power Query.

Please also refer to [YouTube API documentation](https://developers.google.com/youtube/v3/docs/)
 for help on the parameters and output formats.

**All other errors:**

I would start by checking my internet connection and errors with either video ID or API key or page token. If all else fails, leave a comment and I will share what I know.

Have you used YouTube API from Excel or Power BI?
-------------------------------------------------

Have you used the Google APIs to build something cool in Excel or Power BI? Please share your experiments in the comment section.

**Other useful Excel templates:**

*   [Calculate distance between places with Google Maps / Bing Maps API in Excel](https://chandoo.org/wp/distance-between-places-excel-maps-api/)
    
*   [Find nearby zip codes using Excel formula](https://chandoo.org/wp/finding-nearby-zipcodes-using-excel-formulas/)
    
*   [Extract Excel cell comments](https://chandoo.org/wp/get-cell-comments/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/export-youtube-comments-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/export-youtube-comments-template/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [api](https://chandoo.org/wp/tag/api/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [web queries](https://chandoo.org/wp/tag/web-queries/)
    , [youtube](https://chandoo.org/wp/tag/youtube/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousCelebrating 50k Subscribers on YouTube + Give away](https://chandoo.org/wp/50k-give-away/)

[NextHow to make an Interactive Chart Slider ThingyNext](https://chandoo.org/wp/interactive-chart-slider-thingy/)

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
    
    [Reply](https://chandoo.org/wp/export-youtube-comments-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/export-youtube-comments-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/export-youtube-comments-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
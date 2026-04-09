# "How Trump happened" in Excel [visualizations] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-trump-happened-in-excel

---

*   [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

“How Trump happened” in Excel \[visualizations\]
================================================

*   Last updated on March 2, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

During last week, an alert reader of our blog, Jørgen emailed me a link to “[How Trump happened](http://graphics.wsj.com/elections/2016/how-trump-happened/)
“.  It is an interactive visualization by Wall Street Journal. Jørgen asked me _**if we could replicate the visualization in Excel**_. My response: “Making a new chart in Excel? Hell yeah!”

**First let’s take a look at the WSJ visualization:**

You may go to [WSJ’s How Trump happened page](http://graphics.wsj.com/elections/2016/how-trump-happened/)
 or see a quick video below. Make sure you are seeing the WSJ link on a computer or tablet. On mobiles it changes to a bar chart.

_If you have trouble watching the video, [click here](https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened-wsj-demo.mp4)
._

[https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened-wsj-demo.mp4](https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened-wsj-demo.mp4)

As you can see, the visualization starts with one hundred voters in each group and shows how they are divided by various issues. It is a very interesting piece of story telling. That said, I am not a fan of it for below reasons:

*   **Misleading:** The visualization suggests that some of the voters who said “YES” for one issue are saying “NO” to another. _For example, 40% Trump voters have >$75,000 income. But when you go next issue (Do you have college degree?), you see 2 % voters moving to NO group. This suggests that out of 40% who have >$75k income, only 2% do not have college degree._ But this is not true. The groups having $75k income and college degree may be completely different (or 100% overlapped).
*   **Time consuming:** We need too much time to digest 10 issues at hand. What more, We are unable to compare issues vs. candidates because of we can’t see everything in one go.
*   **Poorly named:** Last but not least, the visualization is wrongly titled. It doesn’t really explain _how Trump happened?_ It never mentions what motivated the voters to side with Trump, whether Trump’s own campaign promises / manifesto align with the issues these voters worry about. For most of the issues, there are no significant differences between 3 groups of candidates. So how a voter decided to go with Trump is never explained.

### Okay, so how do we create this in Excel?

_We can’t. At least, I can’t_ make a 100% replica of the WSJ chart in Excel. So I went with next closest approximation. Here is the basic approach:

*   We **create a bubble chart with 3 bubbles** – top, bottom and move.
    *   Top bubble shows how many people answered YES for a particular issue
    *   Bottom bubble shows how many answered NO
    *   Move bubble shows people moving from one group to another as we switch between issues.
*   We **fill the bubbles with people shapes** and tile them.
*   Whenever we switch to a new issue,
    *   We calculate the new top & bottom bubble sizes
    *   We figure out the move bubble size and movement direction (ie top to bottom or bottom to top?)
    *   In case of top to bottom movement,
        *   Use VBA to gradually reduce the top bubble while increasing the move bubble
        *   Change the move bubble’s y value from top to bottom
        *   Increase the bottom bubble size while reducing the move bubble size gradually
    *   Do the opposite in case of bottom to top movement.
*   [Use a slicer to capture issue selection](http://chandoo.org/wp/2016/02/08/use-slicers-as-selection-mechanism/)
     and trigger animation VBA.

**Here is a quick demo of this approach:**

Watch this quick video. [Click here](https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened-xl-v1.mp4)
 if you can’t see it.

[https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened-xl-v1.mp4](https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened-xl-v1.mp4)

### An alternative visualization – Trump Tower chart

Let me confess a thing. I don’t like the bubble chart approach. It feels clumsy and complex. So I wanted to try something different. How about **using two ranges of cells and simply filling them up based on how many people said YES and NO**. When we switch to a different issue, we simply move the filled cells from one range to another.

I call this approach, _**the trump tower chart.**_ 

**First, take a look at it:**

![how-trump-happened-xl-v2](https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened-xl-v2.gif)

**How is the Trump Tower constructed?**

Oh, simple. We just go to the bank, take a $ 100 mn loan, go to city council and convince them to allocate acres of land, construct a big, luxurious building, sell the condos for insane prices and bag the profit.

I am kidding. Don’t rush to the bank. We can use Excel to make the chart. Here is the approach in a nut shell.

*   Create two ranges of cells: **top & bottom each with 100 cells**
*   Using conditional formatting, fill up the top range with number of people saying YES and bottom range with number of people saying NO.
*   When user switches to a new issue, using VBA:
    *   Calculate the new Top & Bottom sizes
    *   Calculate the direction of movement
    *   If voters are going from top to bottom, for each voter moving:
        *   Reduce the top range size by 1
        *   Create moving illusion by filling up blank space between ranges
        *   Increase bottom range size by 1
    *   Do the opposite if we are going from bottom to top
*   Set up a scroll bar to enable issue selection. Link the scrollbar to Animate VBA macro

### Isn’t there a better way to visualize this data?

Let’s be honest. The original WSJ chart and both our interactive + animated replicas are not the ideal way to understand this data. These are complex – both to create and read. As we always say, _simplicity trumps._ Or as Trump says, “Let’s make charting great again”. So let me present a chart that is amazingly clear and very easy to make.

**A bar chart will do:**

As you can guess, **a simple bar chart is enough to understand this data**. Should you wish to highlight polarizing issues, you can use conditional formatting to highlight them. See below image:

![how-trump-happened-bar-chart](https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened-bar-chart.png)

### Download “How Trump happened” Excel workbook:

[**Click here to download the how trump happened workbook**](https://chandoo.org/wp/wp-content/uploads/2016/03/how-trump-happened.xlsm)
. It contains all three visualizations. Please enable macros to enjoy them. Examine the code.

### So which one is your favorite?

While I had a lot of fun building the bubble chart & Trump tower versions, I think the bar chart is most useful version.

**What about you?** Which chart do you like most? How would you visualize this data? Please share your thoughts and suggestions in the comments area.

### Build your charting muscle…

Visual story telling is a very compelling medium. Learn how to build awesome charts using Excel. Check out below tutorials and examples:

*   [Is this a FIFA worldcup of late goals? Let’s ask Excel…](http://chandoo.org/wp/2014/06/25/fifa-worldcup-goal-timing-analysis/)
    
*   [A visual  tribute to Sachin Tendulkar, the legendary cricketer](http://chandoo.org/wp/2013/11/15/srt200/)
    
*   [Closing the gaps in this gender equality chart](http://chandoo.org/wp/2013/11/05/gender-equality-gap-interactive-chart/)
    
*   [How tax burden has changed over the years – Replicating NY Times chart in Excel](http://chandoo.org/wp/2012/12/06/tax-burden-chart-excel/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/how-trump-happened-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-trump-happened-in-excel/#respond)
    
*   Tagged under [animation](https://chandoo.org/wp/tag/animation/)
    , [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [data bars](https://chandoo.org/wp/tag/data-bars/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [visualization principles](https://chandoo.org/wp/tag/visualization-principles/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    
*   Category: [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousAutosum many ranges quickly with Multi-select & ALT= \[quick tip\]](https://chandoo.org/wp/autosum-quickly-with-multi-select/)

[NextUnpivot and then pivot for clarity (case study)Next](https://chandoo.org/wp/unpivot-and-pivot-pq/)

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
    
    [Reply](https://chandoo.org/wp/how-trump-happened-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-trump-happened-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-trump-happened-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
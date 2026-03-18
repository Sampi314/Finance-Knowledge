# Introducing...Structured References for PivotTables » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/introducing-structured-references-for-pivottables

---

*   [hacks](https://chandoo.org/wp/category/hacks/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    , [Random](https://chandoo.org/wp/category/uncategorized/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Introducing…Structured References for PivotTables
=================================================

*   Last updated on October 22, 2014

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

Howdy folks. Jeff here, bringing you a Public Service Announcement: Thanks to the magic of VBA , _Structured PivotTable References_ are coming to a PivotTable near you!

[![Formula](https://chandoo.org/wp/wp-content/uploads/2014/10/Formula.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/Formula.gif)

_Structured References for PivotTables? **So what?**_ Well, because **PivotTables** are the best bit of ‘old’ Excel, and **Tables** are the best thing about ‘new’ Excel, and it’s about time their strengths were brought together:

*   **_Tables_** magically expand to accommodate anything you put in them. Even better, because of the automated _Dynamic Named Ranges_ built into Tables – called _Structured Table References_ – any Formulas, Charts, Data Validation lists, or conditional formatting formulas that point to that table will instantly be updated with the latest data. And any PivotTables that point to that table will automatically include the new data whenever you refresh them. (Read more [here](http://chandoo.org/wp/2014/03/28/tables-pivottables-and-macros-music-to-your-ears/ "Tables, PivotTables, and Macros: music to your ears")
    ).
*   **_PivotTables_** allow you to do serious yet effortless number crunching without the need for a single formula. Just as well, because the kinds of formulas you need to replicate what a PivotTable can do easily are often _mind-bogglingly_ complex, and _very_ resource intensive. So using a PivotTable instead of formulas means that people that inherit your spreadsheet are less likely to struggle to follow what you’re doing, and the spreadsheet is less likely to suffer from slow recalculation issues. (Although yes, you will have to refresh that PivotTable from time to time. But that’s a small price to pay.) But there’s a _problem_ with PivotTables: they don’t have any kind of inbuilt Dynamic Named Ranges like Tables do. And so because their structure is very likely to change whenever new data is added or a user decides to filter or rearrange the order or number of field displayed, then any formulas that point at PivotTable ranges will have to be changed _manually_. (With the exception of a single cell in the Data area referenced by the GETPIVOTDATA() function). So PivotTables are great for _getting_ a result, but lousy for _passing on_ those results to other parts of your spreadsheet.

Who knows why MS haven’t already implemeted Structured Referencing for PivotTables. But why wait for Microsoft to get around to it. _Let’s just do it ourselves!_

Download the sample file to see my hand-built _Structured PivotTable Referencing_ in action: [DynamicPivotRanges\_20141019 unprotected](https://chandoo.org/wp/wp-content/uploads/2014/10/DynamicPivotRanges_20141019-unprotected.xlsm)

Open it, enable macros, and you’ll see a PivotTable like this:

[![Pivot](https://chandoo.org/wp/wp-content/uploads/2014/10/Pivot.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/Pivot.gif)

Now, click on the arrow to the right of the name box, and you’ll see this:

[![Name Box](https://chandoo.org/wp/wp-content/uploads/2014/10/Name-Box.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/Name-Box.gif)

As you can see, in my implementation of _Structured PivotTable References_, the automatic name that gets generated is prefixed with the Sheet name for uniqueness and uses a period to separate the Sheetname, PivotTable name, and FieldName. So it differs slightly from the notation that Tables use. But it’s _every bit_ as handy.

For instance, check out what happens when I start typing a formula somewhere:  
[![Formula](https://chandoo.org/wp/wp-content/uploads/2014/10/Formula.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/Formula.gif)

Awesome: That’s pretty much the same kind of thing I get when I want to reference a Table:

[![Formula_Table](https://chandoo.org/wp/wp-content/uploads/2014/10/Formula_Table.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/Formula_Table.gif)

Let’s see if it handles changes in the _structure_ of a PivotTable, shall we? Here, the Pivot is filtered in such a way that only 5 rows of data are returned. I’ve selected the entire State region, so that you can see that this corresponds with the automatically generated _Structured PivotTable Reference_ shown in the Name box:

[![PT 5 items showing](https://chandoo.org/wp/wp-content/uploads/2014/10/PT-5-items-showing.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/PT-5-items-showing.gif)

If I change the City filter to include additional cities, then the data returned grows by a few rows, as you can see below. Check out how the _Structured PivotTable Reference_ automatically updated to accommodate the extra rows:

[![PT 8 items showing](https://chandoo.org/wp/wp-content/uploads/2014/10/PT-8-items-showing.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/PT-8-items-showing.gif)

…and if I change the layout of the PivotTable by bringing in a new field – such as the BloodType field shown below – then as you can see, the _Structured PivotTable Reference_ picks up the change too, and recognizes that the State field has shifted to the right:

[![PT Structure Change](https://chandoo.org/wp/wp-content/uploads/2014/10/PT-Structure-Change.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/PT-Structure-Change.gif)

If you change the Sheet name, then the SheetName part of the _Structured PivotTable References_ syntax get updated next time the Pivot gets refreshed. And if you change the PivotName, then that part of the _Structured PivotTable References_ syntax gets updated immediately. Unfortunately the same doesn’t occur for changes to PivotField names. So if you _change the name_ of a field, any formulas pointing at the associated Structured Reference will need to be updated. This is shown below:  
[![Before rename](https://chandoo.org/wp/wp-content/uploads/2014/10/Before-rename.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/Before-rename.gif)

[![During rename](https://chandoo.org/wp/wp-content/uploads/2014/10/During-rename.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/During-rename.gif)

[![FormulaBar](https://chandoo.org/wp/wp-content/uploads/2014/10/FormulaBar.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/FormulaBar.gif)

[![After rename](https://chandoo.org/wp/wp-content/uploads/2014/10/After-rename.gif)](https://chandoo.org/wp/wp-content/uploads/2014/10/After-rename.gif)

So there you have it: a proof-of-concept implementation of _Structured PivotTable References_. I’ve been using this to create complicated non-PivotCharts from Pivots, such as ScatterPlots (which are not supported in PivotCharts), or to serve up data labels to non-Pivot charts. And also to avoid having to have lots of extra formulas down the side of my PivotTable just to handle growth.

Take it for a spin, and let me know your thoughts and suggestions for improvements in the comments. Who knows…someone at Microsoft might even see this, and think _“Now why didn’t WE think of that?”_

What other functionality is missing from Excel that you’d like to see added?
----------------------------------------------------------------------------

While the things that Excel can do are cool, Excel often makes us jump through an awful lot of hoops – and click through an awful lot of dialog boxes – in order to actually do them. At the same time, there’s lots of things we routinely do that Excel simply doesn’t provide tools handy tools for. The end result is this: for every millisecond that Excel actually does some real work, we’ve probably spent hours ‘prepping’ it to do it.

Whenever we have to do lots of manual steps in order to leverage Excel’s cool inbuilt functionality, then _Excel_ is programming _us_. It’s like some kind of epic experiment in behavioral psychology; and we’re the mice. It should be the other way around.

Fortunately, VBA (Macros) gives us the means to program Excel so that it behaves like we _want_ it too. So if there’s something _you_ would like to see added to Excel, let us know in the comments. We’ll see what we can collectively do to make Excel even greater than it already is!

**—Edit—**  
My pal Doug Glancy actually [wrote a post](http://yoursumbuddy.com/create-pivot-table-named-ranges/)
 on how to do this back in 2012, on my birthday no less. I’d clean forgotten about that post. So be sure to check out Doug’s implementation of this too.

About the author
----------------

[![Jeff](https://chandoo.org/wp/wp-content/uploads/2013/07/Jeff.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/Jeff.png)
  
Yep, that’s me all right. Jeff Weird. Excel Madman.

If you liked this post, then you’ll _love_ my upcoming book: [_Excel for Superheroes and Evil Geniuses_.](http://www.amazon.com/Excel-Superheroes-Evil-Geniuses-Jeff/dp/1615470379)
 Keep a lookout for it in early 2015, and check out my posts on [this blog](http://chandoo.org/wp/category/posts-by-jeff/)
 or over at [Daily Dose of Excel](http://dailydoseofexcel.com/archives/author/jeff-weir/)
 to get a feel for what kinds of things I’ll be covering. The book will give users an excellent overview of how Excel works under the covers, and what tools the interface puts at their fingers right out of the box. And it will ship with free code that will add amazing new features and functionality to Excel. You’ll be an Excel Evil Genius in no time!

Stay tuned…

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [44 Comments](https://chandoo.org/wp/introducing-structured-references-for-pivottables/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introducing-structured-references-for-pivottables/#respond)
    
*   Category: [hacks](https://chandoo.org/wp/category/hacks/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    , [Random](https://chandoo.org/wp/category/uncategorized/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousCP023: My experience with Hudhud Cyclone \[personal story\]](https://chandoo.org/wp/cp023-my-experience-with-hudhud-cyclone/)

[NextBack after a while & 3 announcementsNext](https://chandoo.org/wp/back-after-a-while-3-announcements/)

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
    
    [Reply](https://chandoo.org/wp/introducing-structured-references-for-pivottables/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introducing-structured-references-for-pivottables/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introducing-structured-references-for-pivottables/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
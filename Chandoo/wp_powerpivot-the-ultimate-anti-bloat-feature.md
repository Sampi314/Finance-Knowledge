# PowerPivot - the ULTIMATE anti-bloat feature » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/powerpivot-the-ultimate-anti-bloat-feature

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    

PowerPivot – the ULTIMATE anti-bloat feature
============================================

*   Last updated on October 3, 2013

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

Howdy again, folks. Jeff Weir here, borrowing the keys to the blog off Chandoo again. (Hopefully I don’t scratch it again).

How remiss of me…[jacob](http://chandoo.org/wp/2013/09/29/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447666)
 reminded me in the comments of my previous BLOATED post on [good spreadsheet anti-bloat practices](http://chandoo.org/wp/2013/09/29/i-said-your-spreadsheet-is-really-fat-not-real-phat/ "I said your spreadsheet is really FAT, not real PHAT!")
 that I completely missed one of Excel’s newest and most efficient anti-bloat features: **PowerPivot**. So today’s post is going to rectify that. In less words, I promise.

Does my data look flat in this?
-------------------------------

In Rob Collie’s excellent book _[DAX Formulas for PowerPivot – the Excel Pro’s Guide to Mastering DAX](http://www.powerpivotpro.com/the-book/)
_, Rob makes the point that before PowerPivot came along, Excel pros spent _lots_ of their time ‘flattening’ data in order to feed their pivots. In fact, many Excel Pro’s had _become_ Excel Pro’s largely on the back of those data flattening skills.

What does he mean by ‘flattening’? Well, PivotTables are such finicky eaters that they only like digital Pizza. That is, if you want a PivotTable to _fully_ digest your data directly from the worksheet, then you need to lay that data out in a hierarchical structure that obfuscating geeks like to call a _flat file_. (You or I call a flat file a _table._ That’s why we’re not geeks.)

A PivotTable’s rather restrictive diet reminds me of this joke:  
**Question:** What do you feed someone with ebola, SARS, and Swine flu?  
**Answer:** Anything that fits under the door.

So your picky PivotTable will only eat flat, boring old Tables. In fact, it will only eat ONE table, and that table _better_ have good labeling of all the ingredients (i.e. column headers) or your precious PivotTable will not even open it’s mouth.

Which is a problem, because the BOSS just ordered you to serve up some crazy concoction that isn’t even on your regular menu. The BOSS wants you to mix a little bit of _this_ table with a tiny bit of _that_ table, then add a sprinkling of _some other_ table over the top as garnish. And the BOSS expects you to slam all this into your pre-heated PivotOven for a quick bake at 2.30GHz **for no more than a few minutes**, and then serve it up to the BOSS right away. Because the BOSS is hungry for data, and the BOSS is hungry **NOW, DAMMIT!**

So what did you do? You used as many VLOOKUPS as you have rows in your final flat data-set to join _just one_ column of one of those additional tables onto the first table, didn’t you. And then you repeated this VLOOKUP frenzy for _each and every other_ column that you ended up bringing into your steam-rolled mega-flat pivot-ready data-set. All of which resulted in one very bloated filesize, compared to the original footprint of the underlying tables.

And while you managed to serve up the order just in time, _boy_ did you make a mess back in the kitchen. Formulas everywhere, and the whole joint is slowing down as a result. What’s worse, the BOSS liked the taste of what you just served up. So you’ll be working in the same messy kitchen next week to refresh it, unless you tidy up somehow.

Let’s face it…it’s such a complete mess, that you’re screwed.

Or _are_ you?

PowerPivot….No fast data joint should be without it!
----------------------------------------------------

If PowerPivot was marketed on the Shopping Channel, then some obnoxiously loud voice would say something like this about it:  
**It slices. It dices. It joins. _But wait, there’s more!_  
It cooks. It cleans. It washes up. It takes up practically no bench-space. _But wait, there’s STILL more!_  
**

In fact there’s so _much_ more, that that’s a subject for another post. Fortunately Chandoo already wrote it: [What is Power Pivot – an Introduction](http://chandoo.org/wp/2013/01/21/introduction-to-power-pivot/ "What is Power Pivot – an Introduction ")
. (Chandoo, that title is _way_ too descriptive. You’ll never make Class 1 Geek unless you learn to obfuscate, my man).

Give that link a spin, because this product lives up to it’s hype. Indeed, no _modern_ fast data joint should be without it. Emphasis on _modern_ though, because you’ll need Excel 2010 or later in order to use this bloat-busting add-in.

But back to how it helps with bloat, the subject of this post. PowerPivot cuts through potential bloat, because it is a _lot_ less fussy than Old-School-Pivots about what it eats:

*   It allows you to create pivots on the fly from any mix of multiple data sources – Access, SQL, **Excel Tables**, Web Data, etc – and then effortlessly slice, dice, and navigate to your hearts content.
*   You can incorporate/mash up additional data sources at any point.
*   You can create very powerful calculated fields within PivotTables that simply are not possible to replicate with in traditional pivots.
*   _**All without ship-loads of VLOOKUPS.**_

In fact, Rob Collie – master of both PowerPivot _and_ understatement – has a great video showing how PowerPivot is the answer to _“the dreaded VLOOKUP problem, among other things”_ in his post [Be Gone, Scary VLOOKUP”](http://www.powerpivotpro.com/2013/05/be-gone-scary-vlookup-short-film-by-rob-collie/)
.

So it does away with all those nasty VLOOKUPs. But that’s not the half of it…PowerPivot has some amazing data compression stuff going on under the hood too! (Check out Rob’s post [Surprising Example of PowerPivot Compression](http://www.powerpivotpro.com/2010/02/surprising-example-of-powerpivot-compression/)
 for more on this.)

Okay, I’m convinced. But I’m a little scared, too…
--------------------------------------------------

If you want help to learn PowerPivot, then help is at hand: Check out Chandoo’s [Advanced Excel & Power Pivot Training Classes](http://chandoo.org/wp/resources/learn-power-pivot/)
. Rob Collie puts in a guest appearance in one of the modules, too. (And I think that you get a copy of his great book as part of the course fee.)

But before I return you to your regular schedule, **be warned**: Chandoo has the following public service message on his PowerPivot landing page that you might want to consider, if your boss is attractive as mine is:  
_**Warning: Learning Excel and Powerpivot might suddenly make you boss fall in love with you.**_

Indeed, that is a good warning that I _will_ heed, Chandoo. I’m burning Rob’s PowerPivot books as you read this.

About the Author.
-----------------

Jeff Weir – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure _#VALUE!_

Find out more at [http:www.heavydutydecisions.co.nz](http://heavydutydecisions.co.nz/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/powerpivot-the-ultimate-anti-bloat-feature/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/powerpivot-the-ultimate-anti-bloat-feature/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [large file size](https://chandoo.org/wp/tag/large-file-size/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [powerpivot](https://chandoo.org/wp/tag/powerpivot/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    

[PrevPreviousI said your spreadsheet is really FAT, not real PHAT!](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/)

[NextFormula Forensics No. 035 Average the last 3 values greater than 0Next](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/)

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
    
    [Reply](https://chandoo.org/wp/powerpivot-the-ultimate-anti-bloat-feature/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/powerpivot-the-ultimate-anti-bloat-feature/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/powerpivot-the-ultimate-anti-bloat-feature/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
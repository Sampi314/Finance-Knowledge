# Segmenting customers by revenue in Excel

**Source:** https://chandoo.org/wp/customer-segmentation-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

Did Jeff just chart?
====================

*   Last updated on September 1, 2015

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

**Chandoo:** Did somebody just chart?  
**Jeff:** Yes. Yes I did. More on that later. But first, let’s take a sniff of Mike Alexander’s outliers, shall we?

Over at the bacon bits blog, Mike has an [interesting post](http://datapigtechnologies.com/blog/index.php/highlighting-outliers-in-your-data-with-the-tukey-method/)
 on using something called the Tukey Method to identify outliers in a data set. That article is worth reading for John Walkenbach’s comment alone.

Here’s Mike’s sample dataset, with the data points identified as outliers highlighted in orange:  
[![Chandoo_Visually eyeballing data to identidy outliers_Output](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Visually-eyeballing-data-to-identidy-outliers_Output.png)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Visually-eyeballing-data-to-identidy-outliers_Output.png)

The Tukey method that Mike blogs about constructs a _fence_ around “reasonable” readings, and that fence is described mathematically by an arbitrary numerical factor:  
(Quartile 1) – (Arbitrary\_Factor × IQR)  
(Quartile 3) + (Arbitrary\_Factor × IQR)

Typically a factor of 1.5 is used. Check out Mike’s blog for a detailed explanation of this stuff.

That’s all good, but it also produces a fairly arbitrary cut-off, depending on what factor you use. So rather than using an algorithm to determine outliers, my preference is to sort the data from lowest to highest value, then plot it and look at the resulting shape:  
[![Chandoo_Visually eyeballing data to identify outliers_Data](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Visually-eyeballing-data-to-identify-outliers_Data.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Visually-eyeballing-data-to-identify-outliers_Data.gif)

—Edit— Jon says in the comments:  
_Your line chart would be easier to read if you’d used markers. I use markers to indicate where the data actually IS, and help show that the line only ties the data together and doesn’t indicate more data, until the points are nearly touching._

Trust Jon to chart in my face. But he’s right. So here it is:  
[![Chandoo_Did you just chart_Mikes Data with markers](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Mikes-Data-with-markers.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Mikes-Data-with-markers.gif)

\[Aside: That chart’s done in Excel 2013. What’s weird is that those markers aren’t centered on the line, but seem to sit just above it by a point or two. Whoops, Microsoft.\]

And here it is with data labels, so it’s easier to see the actual values:  
[![Chandoo_Did you just chart_Mikes Data with markers and data labels](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Mikes-Data-with-markers-and-data-labels.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Mikes-Data-with-markers-and-data-labels.gif)

Some may say that the data labels are redundant, because you can gauge the values from the axis. My mature response to that is “Ffffffrrrrrt”. I like the data labels…once I’ve used the line to quickly judge what may be outliers, the labels let me confirm the jump in values without having to move my head back and forth like I’m watching Roger Federer play Andy Murry at Wimbledon.

In fact, maybe I can combine the marker with the labels, and get rid of that axis altogether:  
[![Chandoo_Did you just chart_Mikes Data with combined markers and data labels](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Mikes-Data-with-combined-markers-and-data-labels.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Mikes-Data-with-combined-markers-and-data-labels.gif)

Hey, that looks cool. Anyone going to get Tufte on me?  
—Edit over—

This is akin to making a bunch of actors line up in order of shortest to tallest, and saying:  
_Okay…Elijah, Dominic, Billy, and Sean…you’re shortest. And by golly, you four look a **lot** shorter than the others. You guys can be the Hobbits._  
[![Chandoo_Did you just chart_LOTR cast](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_LOTR-cast.jpg)](http://en.wikipedia.org/wiki/File:Fellowship.JPG)

\[Aside: I recreated the below graph from one a site called SFScope. Check out the outliers at both ends, and click on the picture to visit the original\]  
[![Chandoo_Did you just chart_LOTR graph](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_LOTR-graph.gif)](http://www.sfscope.com/2009/06/characters-in-the-lord-of-the-rings-and-miles-vorkosigan-by-height)

I like this graphical approach. I think it takes less effort to _visually_ identify outliers than to _programatically_ identify them. For instance, let’s look at Mike’s sample data again for a moment:  
[![Chandoo_Did you just chart_Mikes Data with combined markers and data labels](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Mikes-Data-with-combined-markers-and-data-labels.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Mikes-Data-with-combined-markers-and-data-labels.gif)

Looking at this data, I visually identify pretty much the same outliers as Tukey would – points 1,2,3, 19, and 20. In addition, it looks like that 4th data point – with a value of 13 – looks like it has outlier stamped all over _it too_, when you see it in context of the other data.

Another benefit of plotting ranked data is that it also allows you to ask questions about interesting trends within the datapoints that clearly are _not_ outliers. For instance, what’s the deal with the sudden ‘acceleration’ in the trend between datapoints 16 and 17 caused by? Understanding drastic changes within non-outlier points might be worth as much money to a business as understanding the outliers themselves.

Lose the horizontal axis?
-------------------------

Sometimes with larger datasets, that horizontal axis can be distracting, because Excel only has enough space along that axis to display the labels for every _nth_ rank.

For instance, take the below graph, which looks at just how much money an organization receives from each of its customers by way of annual membership subscription each year:  
[![Chandoo_Did you just chart_Subscriptions with axis](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Subscriptions-with-axis.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Subscriptions-with-axis.gif)

See what I mean? You find yourself trying to decipher the trend in the data labels, and this really draws your eye away from the incredible trend shown in the graph above.

So let’s just delete them:  
[![Chandoo_Did you just chart_Subscriptions without axis](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Subscriptions-without-axis.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Subscriptions-without-axis.gif)

That’s much less distracting. Wow: many of our customers hardly subscribe to anything, and a few practically keep this place afloat!

What else can we show on a graph like this?
-------------------------------------------

Sorting your data like this also lends itself to visually segmenting your customers by how much they contribute to your total revenue.

For instance, the below graph shows just how many customers it takes to account for each subsequent 25% of revenue, and what the average annual subscription within each group is. This gives you a real appreciation into just how valuable your larger customers are in comparison to smaller customers:  
[![Chandoo_Did you just chart_Segmented by 25pc](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Segmented-by-25pc.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Segmented-by-25pc.gif)

Wow, half our subscription revenue comes from our Key Accounts and Large Customers groups, who make up just 10% of our subscription base. Let’s be _especially_ nice to _those_ customers. And lots of our effort is spent in servicing small clients that don’t buy much. Can we grow their business? Should we sack some of them as customers, so we can spend that effort finding bigger ones?

Using revenue ‘buckets’ of 25% was a fairly arbitrary choice. What if we designed a chart template that let you dynamically choose _different sized_ revenue buckets, as well as let you use _more_ buckets if you wanted to?  
For instance, looking at the above graph, it looks to me that we have a whole bunch of ‘Tiny Customers’. And we also might want to segment that group of Median customers that all have exactly the same sized subscription into a group of their own.

Well, the chart template I’ve put together for this post lets you do just that:  
[![Chandoo_Did you just chart_more segmentation Excel 2013](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_more-segmentation-Excel-2013.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_more-segmentation-Excel-2013.gif)
  
Wow. Jeff charted _again_. Man, look at all those time-wasting small accounts…they’re about as welcome as a chart in an elevator!

Note that the above graph was produced using Excel 2013. Excel 2013 automatically puts in those grey lines connecting the data lables with the series. Those are called Leader Lines. They rock.

Unfortunately, earlier versions of Excel only use leader lines for pie charts. But fear not, intrepid reader, for my chart template uses a bit of VBA to automatically puts lines in for you using shapes, if you’re using Excel 2010:  
[![Chandoo_Did you just chart_more segmentation Excel 2010](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_more-segmentation-Excel-2010.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_more-segmentation-Excel-2010.gif)

What’s cool about this template is that all the data labels are dynamic: change the ‘breakpoints’ between groups or the number of groups in the ‘Controls’ table \[see screenshot below\], and the details within the data labels are updated _automatically_. Bing!  
[![Chandoo_Did you just chart_controls](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_controls.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_controls.gif)

I modified a version of Jon Peltier’s great [Label Last Point](http://peltiertech.com/WordPress/label-last-point-for-excel-2007/)
 routine to refresh the placement of the data labels. (Thanks, Jon). Here’s the template, so you can play around in the privacy of your own screen:  
[Segmenting customers by revenue contribution\_V1](https://chandoo.org/wp/wp-content/uploads/2014/01/Segmenting-customers-by-revenue-contribution_V1.xlsb)
 \[Not tested in Excel 2007 or earlier\]

Oh yes. I most definitely charted, boss.

Updates
-------

—Update 1—  
Prompted by some great action in the comments below, I whipped up this redesign in both gray and white:  
[![Chandoo_Did you just chart_Redux 3](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Redux-3.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Did-you-just-chart_Redux-3.gif)
  
While I like the grey, I do think it’s harder on the eyes than black text on white background. And I don’t think a grey chart would work well on say a dashboard. But that said, there’s no doubt in my mind that this chart is sexier than my original. Might look nice in the Economist. Here’s a link to the revised sample file: [Segmenting-customers-by-revenue-contribution\_with\_Leader\_Lines V1](https://chandoo.org/wp/wp-content/uploads/2014/01/Segmenting-customers-by-revenue-contribution_with_Leader_Lines-V1.xlsb)

—Update 2—  
Kaiser Fung has some **great** ideas on how to redesign this in his post [Visualizing Uneven Distributions](http://junkcharts.typepad.com/junk_charts/2014/01)
. Go check it out, and be sure to subscribe to both his [Junk Charts](http://junkcharts.typepad.com/junk_charts/)
 blog as well as his [Big Data, Plainly Spoken](http://junkcharts.typepad.com/numbersruleyourworld/)
 blog. Both are gold. Both will make you a better analyst.

Added by Chandoo
----------------

If you like this chart, chances are you are going to love the below too:

*   [Finding non-performing customers using Pivot Tables](http://chandoo.org/wp/2012/10/03/using-pivot-tables-to-find-out-non-performing-customers/)
    
*   [Pareto analysis and charts using Excel](http://chandoo.org/wp/2009/09/02/pareto-charts/)
    
*   [Market segmentation charts using Excel](http://chandoo.org/wp/2009/02/18/market-segmentation-charts-excel/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [55 Comments](https://chandoo.org/wp/customer-segmentation-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/customer-segmentation-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [area charts](https://chandoo.org/wp/tag/area-charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [market segmentation charts](https://chandoo.org/wp/tag/market-segmentation-charts/)
    , [pareto charts](https://chandoo.org/wp/tag/pareto-charts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

[PrevPreviousRight-click from the keyboard, not the mouse.](https://chandoo.org/wp/right-click-from-the-keyboard-not-the-mouse/)

[Next5 reasons why you should learn Power PivotNext](https://chandoo.org/wp/5-reasons-why-you-should-learn-power-pivot/)

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
    
    [Reply](https://chandoo.org/wp/customer-segmentation-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/customer-segmentation-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/customer-segmentation-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
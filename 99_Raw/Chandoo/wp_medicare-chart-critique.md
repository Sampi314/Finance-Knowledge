# We cant Cure Cancer, But we can Cure this Medicare Chart [Chart Busters] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/medicare-chart-critique

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

We cant Cure Cancer, But we can Cure this Medicare Chart \[Chart Busters\]
==========================================================================

*   Last updated on October 20, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This post is from GuestBuster Jeff Weir in our [Chart Busters series](http://chandoo.org/wp/tag/chart-busters/)
.**_

Note: The post slightly longer, but worth every word. Just get a cup of coffee and soak in to this visualization goodness. (Also, click on any image to see its full version)

Over at the [FlowingData](http://flowingdata.com/2009/07/09/health-care-costs-vary-widely-by-region/)
 blog, they’ve been talking about this pretty slick looking [Choropleth](http://en.wikipedia.org/wiki/Choropleth_map)
 Map that shows how Medicare returns vary across the United States:

[![Medicare Chart Critique Figure_1](https://chandoo.org/img/cb/3/Figure_1.png)](http://chandoo.org/img/cb/3/b/Figure_1.png "Medicare Chart Critique Figure_1")

The above shows total Medicare reimbursements in 2006, either by Hospital Referring Region or by State, depending on the radio button. Using the dropdown box, you can change it to this:

[![Medicare Chart Critique Figure_2](https://chandoo.org/img/cb/3/Figure_2.png)](http://chandoo.org/img/cb/3/b/Figure_2.png "Medicare Chart Critique Figure_2")

…which is how the data looks if you overlay it on a Giraffe. Oops, I forgot to rotate it before saying that. Bear with me a moment…

[![Medicare Chart Critique Figure_3](https://chandoo.org/img/cb/3/Figure_3.png)](http://chandoo.org/img/cb/3/b/Figure_3.png "Medicare Chart Critique Figure_3")

There. See the Giraffe now? Good.

A picture is worth a thousand words, or so they say. But is a Choropleth worth the many line charts and [clowns](http://peltiertech.com/WordPress/bad-bar-chart-practices-or-send-in-the-clowns/)
 that you could squeeze into the same valuable screen real estate? Let’s find out, by evaluating what this particular chart does well, and what it does poorly, and whether other charting methods might better convey its information.

Words _and_ music.
------------------

Right off the bat, there’s a simple way that the authors could improve this chart. While they include a description below the chart to point out what the data is, and where it came from, they miss something just as important…what they _concluded_ from all of this. So before we consider adding – say – bullet _graphs_, let’s consider adding some bullet _points_. A few sentences can tell readers important stuff that would otherwise remain hidden in an undownloaded PDF report. Insights like:

*   Care is often _better_ in low-cost areas.
*   Growth in returns are only partly explained by advancing technology, and
*   Differences in growth rates _across_ regions seem largely due to discretionary decisions by physicians that are influenced by the local availability of hospital beds, imaging centres and other resources-and a payment system that rewards growth and higher utilization.

Straight off the bat, this would make the graph a better graph…without even messing with its form.

But mess we must…
-----------------

…because lurking below the chlorophyll green of this Choropleth Map are a few serious charting oversights. Ready? Let’s check ’em out.

_Scale?_ Fail!
--------------

First, check out the legend.

[![Medicare Chart Critique Figure_4](https://chandoo.org/img/cb/3/Figure_4.png)](http://chandoo.org/img/cb/3/b/Figure_4.png "Medicare Chart Critique Figure_4")

Crikey…its bands are as discrete as [Bruno](http://en.wikipedia.org/wiki/Br%C3%BCno_%28character%29)
. Its scale is about as even as my temperament. It varies about as much as =RANDBETWEEN(PaydayBankBalance, UsualOverdraft).

If you fire up Excel and look at the spread covered by each range, you see just how arbitrary the different price bands are:

[![Medicare Chart Critique Figure_5](https://chandoo.org/img/cb/3/Figure_5.png)](http://chandoo.org/img/cb/3/b/Figure_5.png "Medicare Chart Critique Figure_5")

Whoa…the spread of that $9k to $16k band is nearly 15 times larger than two of the other bands. That can’t be good, can it?

Nice profile
------------

If you were to graph financial spread of each group against the aggregated number of Hospital Referral Regions that fall within each spread, you get something like a histogram. The difference between the sizes of these bands is about as different as the number of performers on stage at a Bob Dylan concert in 1964 compared with 1974. See for yourself:

[![Medicare Chart Critique Figure_6](https://chandoo.org/img/cb/3/Figure_6.jpg)](http://chandoo.org/img/cb/3/b/Figure_6.jpg "Medicare Chart Critique Figure_6")
[![Medicare Chart Critique Figure_7](https://chandoo.org/img/cb/3/Figure_7.jpg)](http://chandoo.org/img/cb/3/b/Figure_7.jpg "Medicare Chart Critique Figure_7")

[1964](http://upload.wikimedia.org/wikipedia/commons/f/f0/Bob_Dylan_in_November_1963.jpg)
 [1974](http://upload.wikimedia.org/wikipedia/commons/a/aa/Bob_Dylan_and_The_Band_-_1974.jpg)

Oops, wrong graphic. Try this:

[![Medicare Chart Critique Figure_8](https://chandoo.org/img/cb/3/Figure_8.png)](http://chandoo.org/img/cb/3/b/Figure_8.png "Medicare Chart Critique Figure_8")

Normally histograms have equal widths for each band, but here I want to highlight just how unequal the bands used are. Plus, this lets us regroup the data into evenly spread $1k bands, and overlay it on the first distribution, to see how it compares. Here’s one that I prepared earlier, with the red line as the regrouped data…

[![Medicare Chart Critique Figure_9](https://chandoo.org/img/cb/3/Figure_9.png)](http://chandoo.org/img/cb/3/b/Figure_9.png "Medicare Chart Critique Figure_9")

Vastly different picture isn’t it. The red is kinda like [Data Pig’s heart rate _before_ he eats chocolate covered bacon](http://datapigtechnologies.com/blog/index.php/meat-candy/)
 on Saturdays, and the blue is how his ECG would look when he’s in the ambulance, on the way to the hospital.

This makes it very hard to answer that important question “…compared to _what_?” With such different sized bands, how can we compare one to another? How can we be sure that the distributions within each band will even allow us to?

For instance, take the highest band spread of $9k to $16k: without any further information to go on, we might assume that the median (i.e. middle) value for districts in this category is midway between the $9k to $16k boundaries, like this:

[![Medicare Chart Critique Figure_10](https://chandoo.org/img/cb/3/Figure_10.png)](http://chandoo.org/img/cb/3/b/Figure_10.png "Medicare Chart Critique Figure_10")

But that’s like assuming that Simon and Chartjunkle (oops, Garfunkel) have equal talent. We’d be wrong. _Very_wrong. In actual fact, there’s only three data points to the right of our guessed median line_._ And as for the 55 hospital regions in Group Five that fall to the left of it…well, they all get tarred with the same brush those worst three performers. The _actual_ median for this group is a lot further left, as shown below:

[![Medicare Chart Critique Figure_11](https://chandoo.org/img/cb/3/Figure_11.png)](http://chandoo.org/img/cb/3/b/Figure_11.png "Medicare Chart Critique Figure_11")

This means that over half the data in this 5th band actually falls much closer to the far left of the graph than to the far right of the _same group_ it’s been placed in.

You can see this better if you add a one-dimensional strip plot above the graph, which gives an idea of where the 300 odd values fall within the entire range:

[![Medicare Chart Critique Figure_12](https://chandoo.org/img/cb/3/Figure_12.png)](http://chandoo.org/img/cb/3/b/Figure_12.png "Medicare Chart Critique Figure_12")

Whoa…looks like we’ve got a few outliers to contend with.

What a State we’re in…
----------------------

This seemingly arbitrary ‘bucketing’ effect is exacerbated when aggregating the different hospital regions into State-wide totals. Except this time regions are being penalised by arbitrary _geographical_ boundaries, _as well as_ the arbitrary financial ones above.

Take Texas for example. Aggregating everything up to the State level, Texas appears in that highest band. Yet at the Hospital Referral Region level, one third of its 22 different hospital fall _below_ the national average, and the median for the whole State is around $8,800. So we better be careful making assumptions from a State-wide view, because the Choropleth averages some _very_ diverse costs over some very large chunks of real estate.

To see just how diverse, let’s rank the entire US values from smallest to largest, and highlight where the Texas readings fall within that range:

[![Medicare Chart Critique Figure_13](https://chandoo.org/img/cb/3/Figure_13.png)](http://chandoo.org/img/cb/3/b/Figure_13.png "Medicare Chart Critique Figure_13")

What can we tell from this? Firstly, nearly all regions nationwide fall between $5k and $10k. Secondly, there are a few outliers that really skew the picture at the high end. Thirdly, in the Texas case, the State average is boosted somewhat by 3 Texan districts that happen to be among the worst 10 culprits nationwide – one of which is clearly an outlier at $15k. Unfortunately for the lower cost Texan regions, they’re guilty by geographical association…kinda like being kidnapped and held for a zillion dollar ransom, just because you happen to live in the same State as Bill Gates.

So what do we get by aggregating to State boundaries? Probably more blurring than insight. After all, what good would a weather report be to Texans if it only reported the average weather they could expect as a State! Instead, it’s better to keep the aggregation at the Hospital Referral Region level. That way, we can look at this:

[![Medicare Chart Critique Figure_14](https://chandoo.org/img/cb/3/Figure_14.png)](http://chandoo.org/img/cb/3/b/Figure_14.png "Medicare Chart Critique Figure_14")

…and ask things like “_Wow, why such a difference between Waco and the surrounding bits of Texas?”_ and _“What the hell is Alaska doing there?”_

Legends in the making…
----------------------

What’s far worse that this though is that when looking at the State-wide map, the legend is now really, _really_ wrong.

Here’s the legend next to the actual State-wide figures, for comparison:

[![Medicare Chart Critique Figure_15](https://chandoo.org/img/cb/3/Figure_15.png)](http://chandoo.org/img/cb/3/b/Figure_15.png "Medicare Chart Critique Figure_15")

Whoops…the graph title has changed to reflect we’re now looking at _Medicare spending per beneficiary per **State**_; i.e. State averages. The legend is still looking at Hospital Referral Region averages, which have a much greater spread. For instance, the Choropleth shows six States as being dark green regions, and the legend says they fall somewhere within $9k to $16k. But the actual data shows they fall in a $9.4k to $9.6k range. Oops! Slight misrepresentation, there.

How to fix it
-------------

Obviously this graph really should use a quantitative scale with equal increments; one that changes to reflect the selection that users make. What’s more, colors should have just enough variation so as to highlight any important differences, without being overwhelming or mistaken for camouflage.

But is a Choropleth Map the best way to present this data in the first place? If you want something for people to play with online, then maybe…but if you want to compare things very closely to other things, then maybe not.

For sure, a Choropleth Map looks cool, and it has what [Tusha Metha](http://www.tushar-mehta.com/excel/charts/0301-dashboard-conditional%20shape%20colors.htm)
 calls “natural context”. But from an analytical perspective, a Choropleth only really reports how one thing changes with regards to geography. If geography is a major determinant – or if you want to show people how things look in their own back yard compared to others – then perhaps this is the piece of kit you need. But if there’s other factors that have much more sway on your data than geography, then perhaps not. For instance, we might want to see whether population density plays a significant part in Medicare returns, given the likely economies of scale from providing healthcare to densely populated regions vs. urban regions. Nows the time to break out a scatter plot:

[![Medicare Chart Critique Figure_16](https://chandoo.org/img/cb/3/Figure_16.png)](http://chandoo.org/img/cb/3/b/Figure_16.png "Medicare Chart Critique Figure_16")

Hmmm…looks promising. (Note: I’ve used State-wide data for the above…ran out of time to track down densities in the different Hospital Referral Regions, which is what I’d prefer to do.)

Or we might want to zoom in on the best or worst offenders, and see just how different they are to each other, and to the median value:

[![Medicare Chart Critique Figure_17](https://chandoo.org/img/cb/3/Figure_17.png)](http://chandoo.org/img/cb/3/b/Figure_17.png "Medicare Chart Critique Figure_17")

Conclusion
----------

I think a better, fairer Choropleth Map at the Hospital Referral Region level would be interesting. But I don’t think it would be enough. To quote from Stephen Few’s latest book _Now you see it_: “Color is good at drawing your attention to something if used sparingly, but is one of the ‘pre-attentive attributes’ that is not quantitatively perceived in and of themselves”.

Whereas lines and 2D precision are very precise ways to encode quantitative values.

So when it comes to answering the ‘Compared to what’ question, I don’t think you can beat this:

[![Medicare Chart Critique Figure_18](https://chandoo.org/img/cb/3/Figure_18.png)](http://chandoo.org/img/cb/3/b/Figure_18.png "Medicare Chart Critique Figure_18")

Choropleth Maps in Excel
------------------------

For information on the **implementation** of Choropleth Maps in Excel, check out [Tushar Mehta’s excellent resources](http://www.tushar-mehta.com/excel/charts/0301-dashboard-conditional%20shape%20colors.htm)
.

For more information on the **pros and cons** of Choropleth Maps, check out the [Clearly and Simply blog](http://www.clearlyandsimply.com/clearly_and_simply/2009/06/choropleth-maps-with-excel.html,)
, where Robert has built on Tushar’s excellent approach to produces some great downloadable templates. He also offers advice on potential drawbacks of Choropleth Maps, such as:

*   No visualization of development over time
*   No information on exact values (unless you are implementing tooltips including the data)
*   Very limited direct comparability of the regions
*   Possible perception problems with regards to the size of regions (e.g. Rhode Island on a US map)
*   Possible misinterpretation because the size of a region may have a greater impact on the user’s visual perception than the intensity of the fill color
*   Requirement of real estate on a dashboard

His recommendation: **_carefully consider whether or not a Choropleth Map is the best visualization for your purposes._** Check out his dashboard of [Lithuania at a glance](http://www.clearlyandsimply.com/clearly_and_simply/2009/01/lithuania-at-a-glance.html)
 to see how he mitigates some of the potential problems by incorporating other graphs into the display.

I used Robert’s template to produce this State-wide Choropleth Map of total Medicare spending per enrollee, 2006 using the same Medicare ranges as the Choropleth that’s the subject of this post:

[![Medicare Chart Critique Figure_19](https://chandoo.org/img/cb/3/Figure_19.png)](http://chandoo.org/img/cb/3/b/Figure_19.png "Medicare Chart Critique Figure_19")

…

…then I replotted the graph using data that had been regrouped $1k bands:

[![Medicare Chart Critique Figure_20](https://chandoo.org/img/cb/3/Figure_20.png)](http://chandoo.org/img/cb/3/b/Figure_20.png "Medicare Chart Critique Figure_20")

While I don’t advocate this approach, it’s interesting that even though this is aggregated to State-wide totals, you can see significant differences between the graphs.

Right, that’s it. I’m off to the Hospital to see someone about my writers cramp…

### About the Author

**Jeff** is a Business Analyst from Wellington, New Zealand who has recently discovered a strong interest in Data Visualization. He swears by Edward Tufte and Stephen Few as much as he swears at Excel 2007. He’s so new to advanced Excel, that 2 years ago he had to ask a work friend what the dollar signs in $A$1 meant. Now that he knows that, he’s trying to find out what the dollar signs in $A$2 mean.

### Note from PHD:

Thank you Jeff. Your passion and knowledge is truly outstanding. I have a whole pack of donuts waiting for you.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/medicare-chart-critique/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/medicare-chart-critique/#respond)
    
*   Tagged under [bad charts](https://chandoo.org/wp/tag/bad-charts/)
    , [Chart Busters](https://chandoo.org/wp/tag/chart-busters/)
    , [Chart Busters - Bad Charts are Good for Nothing](https://chandoo.org/wp/tag/chart-busters-bad-charts-are-good-for-nothing/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [choropleths](https://chandoo.org/wp/tag/choropleths/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [heatmaps](https://chandoo.org/wp/tag/heatmaps/)
    , [jeff weir](https://chandoo.org/wp/tag/jeff-weir/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [maps](https://chandoo.org/wp/tag/maps/)
    , [ny times](https://chandoo.org/wp/tag/ny-times/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

[PrevPreviousSumif with multiple conditions \[quick tip\]](https://chandoo.org/wp/sumif-with-multiple-conditions/)

[NextIntroducing PHD Forums (and some other updates)Next](https://chandoo.org/wp/phd-forums/)

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
    
    [Reply](https://chandoo.org/wp/medicare-chart-critique/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/medicare-chart-critique/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/medicare-chart-critique/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# Mapping relationships between people using interactive network chart » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/network-relationship-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Mapping relationships between people using interactive network chart
====================================================================

*   Last updated on August 13, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Today, lets learn how to create an interesting chart. This, called as **network chart helps us visualize relationships between various people**.

### Demo of interactive network chart in Excel

First take a look at what we are trying to build.

![Network Relationships - Interactive Chart in Excel - Demo](https://img.chandoo.org/c/network-relations-chart-demo.gif)

Looks interesting? Then read on to learn how to create this.

Note: thanks to _Hans_ whose email question inspired me to create this chart.

Tutorial to create interactive network chart in Excel
-----------------------------------------------------

Note: **This tutorial requires intermediate-to-advanced Excel knowledge**. So if you are beginner, learn the [basics](http://chandoo.org/wp/excel-basics/)
 & [advanced concepts](http://chandoo.org/wp/advanced-excel-skills/)
 first and then comeback for this.

In order to create this chart in Excel, we need to first understand various ingredients of it.

As you can see, the chart contains these parts:

1.  A set of dots, each representing one stakeholder
2.  A set of grayish thick & dotted lines representing all relationships between people.
3.  A set of green thick & blue dotted lines representing relationships for the selected person.
4.  A slicer for person selection (can be replaced with list box or clickable cells in Excel 2007 or below)
5.  Summary statistics of the selected person

### Getting started with the relationship data

To simplify our tutorial, lets assume we are talking about relationships between just 4 people, named Ash, Billy, Cynthia & Darren.

Our relationship matrix looks like this:

![Data - Relationship matrix - network chart in Excel ](https://img.chandoo.org/c/relationship-matrix-network-graph.png)

*   0 means no relationship
*   1 means weak relationship (for example: Ash & Billy just know each other)
*   2 means strong relationship (for example: Cynthia & Billy are friends)

_[The downloadable workbook](https://img.chandoo.org/c/network-chart-template.zip)
 is created to take up to 20 stakeholders._

### Geometry of the network chart

If we draw the relationships between these 4 people (Ash, Billy, Cynthia & Darren) on a paper, it would look like this:

![Hand-drawn relationship network map](https://img.chandoo.org/c/hand-drawn-network-map.png)

The 2 things we need to determine are,

1.  The location of dots (where person names are printed)
2.  The lines (starting & ending point of lines)

### Plotting dots around circle

We need to plot our dots in such a way that gap between each dot is same.  This will create a balanced chart.

What shape satisfies our need for such equal gaps? _A circle of course._

**Hey wait, I don’t see a circle in the chart you have shown…?**

Thats right. We don’t need to draw a circle. We just need to plot dots around it.

*   So we have 4 stakeholders, we need 4 dots
*   If we have 12 stakeholders, we need 12 dots
*   If we have 20, we need 20 dots.

Assuming the origin of our circle is (x,y), radius is r and _theta_ is 360 divided by number of dots we need,

the first dot (x1,y1) on the circle will be at this position:

x1 = x + r\*COS(theta)

y1 = y + r\*SIN(theta)

\[Related: [How to create a spoke chart in Excel](http://chandoo.org/wp/2012/07/02/how-to-make-a-spoke-chart/)\
\]

Once all the dots are calculated & plugged in to an XY chart (scatter plot), lets move on.

### Plotting the lines

Lets say we have **n** people in the network. So that means, each person can have a maximum of **n-1 relationships.**

So the total possible lines in our chart are n\*(n-1)/2

_We need to divide it by 2 as if A knows B, then B knows A too. But we need to draw only 1 line._

My network chart template is set up to work with up to 20 people. So that means, the maximum number of lines we can have will be **190**

Each line requires a separate series to be added to the chart. That means, we need to add 190 series of data just for 20 people. And that satisfies only one type of line (either dotted or thick). If we want different lines based on type of relationship, then we need to _add another 190 series_.

This is painful & ridiculous.

Fortunately there is a way out.

**We can use far fewer series and still plot the same chart.**

Lets say we have 4 people – A B C & D. For the sake of simplicity, lets assume the co-ordinates of these 4 are

*   A – (0,0)
*   B – (0,1)
*   C – (1,1)
*   D – (1,0)

And lets say, A has relationships with B, C & D.

That means we need to draw 3 lines, from A to B, A to C & A to D.

Now, instead of supplying 3 series for the chart, what if we supply one _long series_ that looks like this:

(0,0), (0,1), (0,0), (1,1), (0,0), (1,0)

That means we are just drawing one long line from A to B to A to C to A to D. Agreed that it is not a straight line, but Excel scatter plots can draw any line as long as you provide a set of co-ordinates.

PS: This is a trick I learned from [Roberto of E90E50](https://sites.google.com/site/e90e50/)
. He used this trick in the winning entry of our recent dashboard contest.

See this illustration to understand the technique.

![Using a single series to draw multiple lines in Excel XY chart](https://img.chandoo.org/c/using-single-series-to-create-3-lines.png)

So instead of 190 series of data for the chart, we just need 20 series.

In the final chart, we actually have 40 + 2 + 1 series of data. This is because,

*   20 lines for weak relationships (dotted lines)
*   20 lines for strong relationships (thick lines)
*   1 line for highlighted person’s weak relationships
*   1 line for highlighted person’s strong relationships
*   1 set of no line & just dots for the people

**How to generate all the 20 series of data:**

This requires following logic:

*   Assuming we need lines for the relationship of person n.
*   That person’s dot location will be (Xn, Yn) and already calculated earlier (in the plotting dots around circle)
*   We need total of 40 rows of data
*   Every odd row will have (Xn, Yn)
*   For every even row
    *   Divide the row number by 2 to get person number (say m)
    *   (Xn,Yn) if there is no relationship between n and m
    *   (Xm,Ym) if there is a relationship

We need [MOD](http://chandoo.org/excel-formulas/mod.shtml)
 & [INDEX](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
 formulas to express this logic in Excel.

Examine the [download workbook](https://img.chandoo.org/c/network-chart-template.zip)
 to understand how its done.

Once all the line co-ordinates are calculated, add them to our scatter plot and format.

_I used a macro to automate the formatting. It can be done manually too, just takes a little patience._

### Slicer for selecting a person

_This works only in Excel 2010 or above._

Select the first 2 columns of relationship matrix & create a pivot table.

Now, insert a slicer on Person name column.

![Slicer for person selection - network chart](https://img.chandoo.org/c/slicer-for-person-selection.png)

Using simple IF formula, extract the selected person name from pivot table (examine download file for the logic).

And using the name, extract the subset of line data to separate range (2 sets of data – one for weak & one for strong relationships)

Add this new data to our scatter plot and format.

Format the slicer (using slicer styles) so that it looks slick.

Related: [formatting slicers using styles](http://datapigtechnologies.com/blog/index.php/getting-fancy-with-your-excel-slicers/)
.

**NOTE About Slicers:** If you change or add any data, you must refresh (from Data ribbon) to update the slicer. This can be automated with a macro, but I want to keep this file macro free.

### \[Alternative\] Selecting a person with form controls

You can use either a [list box](http://chandoo.org/wp/2011/03/30/form-controls/#list-box)
 or a [range of clickable cells](http://chandoo.org/wp/2011/04/07/show-details-on-demand-in-excel/)
. See the 2003 compatible download file for an example of this.

### Summary statistics

Using simple formulas extract statistics for the selected person and show them near the chart.

![Summary statistics - Network chart in Excel](https://img.chandoo.org/c/summary-stats-network-graph-excel.png)

### Adding labels to the chart (person names)

In our chart, we are showing person names instead of regular label like X or Y value. This is done with **value from cells** label feature in Excel 2013.

![Labels for Excel scatter (XY) plot - done using Excel 2013 or add-in in earlier versions](https://img.chandoo.org/c/labels-in-xy-chart.png)

For earlier versions of Excel, I recommend using Rob Bovey’s excellent [XY Chart Labels add-in](http://www.appspro.com/Utilities/ChartLabeler.htm)
.

### Putting it all together

Once everything is ready, clean up the chart, slicer and other elements, put them together. And we are ready to go.

![Relationship Network in an interactive Excel Chart](https://img.chandoo.org/c/network-relationship-chart-excel.png)

Download Network Relationships Interactive Chart Template
---------------------------------------------------------

[**Click here to download the chart template workbook**](https://img.chandoo.org/c/network-chart-template.zip)
. The download is a ZIP file and it contains 3 workbooks – compatible with Excel 2013, 2010 & 2003+. Use the version that you need.

Please examine the formulas & chart settings to understand how it is constructed.

Note: Hit Refresh from Data ribbon to change slicer once you have added or modified data.

### When to use network relationship chart?

A network graph is a good place to explore relationships between people in a project or team. It is especially useful when selecting a sub-set of people from large group to closely work on a project.

### Any alternatives?

There is a popular Excel Add-in named **[NodeXL](http://nodexl.codeplex.com/)
** that can help you visualize and analyze relationships between people in a more in-depth fashion.

Check out [Chord diagram](https://sites.google.com/site/e90e50fx/home/talent-traffic-chart-with-chord-diagram-in-excel)
 & [Cosmograph](https://sites.google.com/site/e90e50fx/home/cosmograph-excel-world-migration-bilateral-flow-chart)
 from E90E50 site for other ways to present this data.

### Do you use these kind of charts?

I have used network charts earlier to depict relationships between various people or things. But I have never created such charts in Excel, I always used either Power Point or some other drawing program to create them. That is why I am excited about this chart. Figuring out the formula & graphing logic was fun.

**What about you?** Have you used such charts before? How do you like the network chart presented here? Please share your thoughts using comments.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [47 Comments](https://chandoo.org/wp/network-relationship-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/network-relationship-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Cos()](https://chandoo.org/wp/tag/cos/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [Scatter Chart](https://chandoo.org/wp/tag/scatter-chart/)
    , [scatter plot](https://chandoo.org/wp/tag/scatter-plot/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [Sin()](https://chandoo.org/wp/tag/sin/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousWhat is the average speed of this road trip? \[homework\]](https://chandoo.org/wp/calculate-average-speed-formula/)

[NextCP017: Top 10 non-Excel MS Office tips for you – Interview with Paul Woods – Office MVP & BloggerNext](https://chandoo.org/wp/cp017-10-non-excel-office-tips/)

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
    
    [Reply](https://chandoo.org/wp/network-relationship-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/network-relationship-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/network-relationship-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
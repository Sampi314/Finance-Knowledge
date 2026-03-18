# A dashboard to visualize this FIFA worldcup [guest post] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/fifa-2014-worldcup-dashboard

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

A dashboard to visualize this FIFA worldcup \[guest post\]
==========================================================

*   Last updated on August 5, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post by **Krishna**, a football lover & one of our readers._ He is also a student of [Chandoo.org online VBA classes](http://chandoo.org/wp/vba-classes/)
.

The wait for lifting the most valued priced in football for Germans was finally over. For a football fan, world cup is best time that is scheduled every four years and that if your favorite team lifting the trophy is like your crush is going on a date with you. 🙂

### A sneak-peek at the final dashboard

Here is the final dashboard (it has more functionality than depicted). Click on it to enlarge.

[![FIFA 2014 Worldcup Excel dashboard](https://img.chandoo.org/dashboards/fifa14db/09.final-fifa-2014-dashboard.png)](https://img.chandoo.org/dashboards/fifa14db/09.final-fifa-2014-dashboard.png)

### Download the dashboard workbook

[**Click here to download the workbook**](https://img.chandoo.org/dashboards/fifa14db/Fifa_14.xlsm)
. Refer to it while reading this article for most benefit.

### How it all began…?

So, after the world cup, I have thought to analyze this tournament using excel. And also [Chandoo’s podcast session 13](http://chandoo.org/session13)
 made me more excited to start on this.  
I have started the by searching for information over net and thanks to [FIFA](http://www.fifa.com/worldcup/statistics/index.html)
 for having all the information at one place.

![FIFA.com website snapshot. It provided me all the necessary data](https://img.chandoo.org/dashboards/fifa14db/01.snapshot-of-fifa-stats.png)

### 1\. Planning of dashboard

I have made some dashboards and I think one of the essential steps to do is to plan what all needs to be represented in our dashboard. Having a checklist helps me to focus more on making it more interactive and creative rather than digging out for the data. In this dashboard, I wanted to show analysis of individual teams, matches played, and comparison of teams. However, I have added the top performers of World Cup in later stages.

### 2\. Collecting data

Having all the data on single site is great, however exporting to excel might seem a bit cumbersome because of formatting issues. So, it’s better to use PowerQuery (a Microsoft add-in) to extract the data from sites. (I came to know about PowerQuery, PowerView and PowerPivot though Chandoo [podcast session 3](http://chandoo.org/session3)
, an interview with Mike Alexander). This provides us the data in tabular form and that saves a lot of time in formatting, especially when you copy from web.

![I used Power Query to import & polish the data](https://img.chandoo.org/dashboards/fifa14db/03.power-query-ribbon.png)

![And this is how the power query imported table looked like](https://img.chandoo.org/dashboards/fifa14db/04.data-after-power-query-import.png)

Once, I have the data for goals scored, I have collected data for other parameters as well and the stats are matched for the respective matches between the teams using [Index-Match](https://chandoo.org/wp/fifa-2014-worldcup-dashboard/(http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left)
.

Now, we have the data related to matches played between the teams.

Similarly collect data for the teams. (FIFA.com has huge resource of information collected for this world cup)

### 3\. What makes a team

Now, we need to make the right graphs for data representation.

For the first part of the dashboard (performance by teams) there are four areas that I wanted to show independently. I was tired of using the form controls. So, I have used the select cells control which requires a small macro and some form of conditional formatting to do the magic. For more on this technique refer to [Interactive Sales Chart tutorial](http://chandoo.org/wp/2012/05/09/interactive-sales-chart-in-excel/)
.

Now for the country selected there should be a flag. Here I have named all the flags with abbreviation of each country. A macro code is used to select the country flag which is the ‘Flag’ (selected cell) cell.

![Flags of the teams in a range of cells](https://img.chandoo.org/dashboards/fifa14db/05.team-flags.png)

### Scatter plot in the dashboard

The chart on the right is scattered plot, where the data points are selected as per the categories selected in the drop-down. I have used Index, Match and Choose functions to select the data points for the all the teams. The pic below is for the “Dribble into penalty area” that is under “Attack”.

![Scatter plot - Dribble into penalty area - how this is made](https://img.chandoo.org/dashboards/fifa14db/06.dribble-into-penalty-area-under-attack.png)  
INDEX($E$2:$AR$34,MATCH($AZ3,$E$2:$E$34,0),MATCH(CHOOSE($AW$16, $AU$15,$AU$16,$AU$17,$AU$18,$AU$19,$AU$20), $E$2:$AR$2,0))

Which is

INDEX($E$2:$AR$34,MATCH($AZ3,$E$2:$E$34,0),MATCH(CHOOSE($AW$16, $AU$15,$AU$16,$AU$17,$AU$18,$AU$19,$AU$20), $E$2:$AR$2,0))  
INDEX($E$2:$AR$34,MATCH(Germany, Teams selected,0), MATCH(Dribble in to penalty area, row headers,0))  
INDEX(Data table,1st row,19th column) = 28

Similarly the data points required for the graph are populated.

![Dribble formula explained](https://img.chandoo.org/dashboards/fifa14db/07.dribble-formula-explained.png)

Now, for finishing, add a small box that gives few details about the team. Here, we need to accommodate all the data in the box that can be done using CONCATENATE or just simply use “&”

![Team details box in the dashboard](https://img.chandoo.org/dashboards/fifa14db/08.team-details-box.png)

For e.g.,

\=”Team: “&linkedCellFlag &CHAR(10) &”Stage: ” &INDEX($E$3:$F$34,MATCH(linkedCellFlag,$E$3:$E$34,0),2)

**linkedCellFlag** :named range for the selected team and Char(10) is required to provide ample space to goto next line.

The output will be (if I selected Germany):

Team: Germany  
Stage: Winners

And similarly use & to add the data into the cells

So putting all together the final output is (yes I am a bot bad in choosing the right color scheme)

[![FIFA 2014 Worldcup Excel dashboard](https://img.chandoo.org/dashboards/fifa14db/09.final-fifa-2014-dashboard.png)](https://img.chandoo.org/dashboards/fifa14db/09.final-fifa-2014-dashboard.png)

### 4\. Match vs. Match ()

So now moving on to the next phase of the dashboard, the analysis of matches played.

Here, when I select two teams, say, Germany vs. Argentina, the match stats for corresponding teams must come up. Here, there are two things that we need to check:

*   When I select Germany as my first team, I need to select all the teams against whom Germany played in this World Cup
*   When selecting the match like GER vs. ARG, we need to have the same result even though I have chosen ARG vs. GER

To solve these two situations I have used the following method:

1.  Make a matrix of the teams played against every other teams as shown below. I have sorted the teams based on groups and using IF,MATCH, IFERROR populate the array as shown below

![Match vs. MATCH() - matrix structure of team performance data](https://img.chandoo.org/dashboards/fifa14db/10.match-vs.match%28%29.png)

**Formula used:**

IFERROR(INDEX($AN$3:$AN$34,IF(AP$2=$AN3,” “, IF(ISNUMBER(MATCH(AP$2,GrpA,0)), MATCH(AP$2,$AO$2:$BT$2,0),””)),1),””)

For case of the selected cell, if, Brazil = Mexico, <<blank>>, If Brazil is part of Group A, then value of the team in header Row (AO2:BT2)

Similar procedure is followed for the other matches

**For the drop down,**

The index number (for eg., Brazil is the 1st team in the drop down bar, hence it has number 1) of the team selected and MOD (number,4) is evaluated. Corresponding teams are added from (i) (if the selected team is Spain, index number is 5, then teams are Chile, Australia and the Netherlands). Similar process is done for teams proceeded into later stages of the tournament is done.

**Evaluation of the match**

For the matches, when we select the teams, let say, Brazil vs. Croatia, here the home team is Brazil and away team in Croatia. So the index number assigned is “1-3”. I have defined the index number for each of the teams using CONCATENATE, INDEX, MATCH functions.  
\=CONCATENATE(MATCH(LEFT(F40,3), $AM$3:$AM$34,0),”-“,(MATCH(RIGHT(F40,3), $AM$3:$AM$34,0)))  
F40= BRA-CRO  
Hence, the formula becomes  
CONCATENATE(MATCH(BRA),$AM$3:$AM$34,0),”-“,(MATCH(CRO),$AM$3:$AM$34,0)))  
CONCATENATE(1,”-“,3)  
Which gives 1-3

In case, I have selected to Croatia first and Brazil second, then I would have it as “3-1”, which doesn’t match with the list of matches. Hence in that case, we need to invert the number to “1-3”.

So finally, got the numbering right, which leaves us to lookup values for each category. So when I have seen initially, the list is too long. So I have decided to subgroup them.

![Grouped cells uses to display match stats](https://img.chandoo.org/dashboards/fifa14db/11.match-stats.png)

On an average the match stats that most of us look are shots, goals, suspension, attacks, procession. However, showing many statistics is often too dangerous. So, I have adjusted to the top stats and sub stats can be viewed if one like to. For example, one wants to look in-depth about goals scored, total attacks and total passes then small box in Column AG (the one highlighted) can be used to hide the rows or show the rows accordingly. A small macro to hide/show rows is sufficient for the same.

### 5\. Where do the teams stand

Now the third part to compare any two teams in the tournament and compare with tournament average. So this would be just a graph with all the data available. So I thought of animating the graph.

Before animation, an important thing to note is to check for the dimension of the variables we are analyzing. Since, all the data is coming on the same graph, plotting goals scored (e.g. 18) and total passes complete (e.g. 4200) in same would not help us. Hence, use total passes complete (in 100s) is to be checked. Similarly for other parameters.

For animation of the graph, I have done a similar as mentioned Chandoo in [Excel VBA classes](http://chandoo.org/wp/vba-classes/)
. (That course is really awesome. If you are looking to know more on excel VBA, I recommend you to join)

![Team comparison chart](https://img.chandoo.org/dashboards/fifa14db/12.team-comparison.png)

### Top 5 teams

![Top 5 teams comparison - FIFA'14 worldcup dashboard](https://img.chandoo.org/dashboards/fifa14db/13.best-of-worldcup.png)

And at last, the comparison of top 5 teams. This is done using INDEX,LARGE formula.

INDEX($E$3:$N$34,MATCH(LARGE($I$3:$I$34,1),$I$3:$I$34,0),1)

In I3:I34, there are values of total goals scored by a team. Here we get Germany

In similar way we can check out for the remaining by substituting 1 with other numbers.

The charts are animated in the similar way as done in the previous graph, although an additional dimension is added.

So this is it. Make final touches by specifying the appropriate hyperlinks to the each section and maintaining the formatting is essential.

Thanks Chandoo for encouraging me to write a guest post.

Added by Chandoo: Thank you Krishna
-----------------------------------

Many thanks to **_Krishna_** for sharing his dashboard file & explanation with all of us. Your work is a proof of how much we can accomplish with Excel.

_**If you like this article,**_please say thanks to Krishna.

### Want to learn how to create dashboards like these?

Then check out:

*   [Excel Dashboards Information & Resources section](http://chandoo.org/wp/excel-dashboards/)
    
*   [10 step process for creating dashboards](http://chandoo.org/wp/2014/07/10/cp014-create-awesome-dashboards/)
    
*   [Making your dashboards interactive – a guide](http://chandoo.org/wp/2012/08/02/making-dashboards-interactive/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/fifa-2014-worldcup-dashboard/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/fifa-2014-worldcup-dashboard/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [animation](https://chandoo.org/wp/tag/animation/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [fifa world-cup](https://chandoo.org/wp/tag/fifa-world-cup/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousStory of my first ever 200KM bike ride (plus an Excel dashboard with ride stats)](https://chandoo.org/wp/200km-bike-ride-story-plus-dashboard/)

[NextCP016: 3 Must have books for aspiring analystsNext](https://chandoo.org/wp/cp016-3-books-for-analysts/)

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
    
    [Reply](https://chandoo.org/wp/fifa-2014-worldcup-dashboard/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/fifa-2014-worldcup-dashboard/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/fifa-2014-worldcup-dashboard/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
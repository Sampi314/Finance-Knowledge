# How your country did in Commonwealth Games - Power BI Viz and Tutorial » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-your-country-did-in-commonwealth-games-power-bi-viz-and-tutorial

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

How your country did in Commonwealth Games – Power BI Viz and Tutorial
======================================================================

*   Last updated on April 17, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Commonwealth games 2018 have ended in the weekend. **Let’s take a look at the games data thru Power BI** to understand how various countries performed.

Here is [my viz online](https://app.powerbi.com/view?r=eyJrIjoiZTA3ZTM2ZGUtMmRjZC00YTZlLWI3MGYtMDI4ZmViMTkwYmQwIiwidCI6IjUzNTA4ZDUyLWQxYjAtNDliMC1iNGJhLTM1MzNjMTI0OWEwMSJ9)
 (or you can see a snapshot below, click on it to expand).

[![](https://chandoo.org/wp/wp-content/uploads/2018/04/cg2018-viz-power-bi.png)](https://chandoo.org/wp/wp-content/uploads/2018/04/cg2018-viz-power-bi.png)

Looks good, isn’t it? Well, read on to know how it is put together.

_This is a high-level tutorial, aimed at Power BI users than newbies. If you are new to Power BI, start with [my Power BI beginners tutorial](https://chandoo.org/wp/2017/09/13/introduction-to-power-bi/)
._

### Commonwealth Games Performance – Power BI Visualization – Tutorial

**Step 1: Define goals for your visualization**

Whenever you are making anything more than a bar chart (come to think of it, even bar charts need a bit of noodling before hand), it is prudent to spend time thinking what you want to accomplish with the visual.

For me the goals are:

*   Understand how various countries have performed in 2018, compare that to previous editions of games (say 2014, 2010 and 2006)
*   See which countries have improved their medal performance from last games
*   Understand how top 10 countries performed – which events they excel in
*   Prepare everything in less than 2 hours

I made a rough sketch of the visualization too. But I deviated quickly once I started playing with the data in Power BI.

**Step 2: Gather the data**

The data for this visualization came from 2 sources:

*   [gc2018.com](https://gc2018.com/)
     for 2018 games data
    *   https://results.gc2018.com/en/all-sports/medal-standings.htm
    *   https://results.gc2018.com/en/all-sports/medallist-by-sport-<country name>.htm
*   [thecgf.com](https://thecgf.com/results/)
     for previous games data
    *   https://thecgf.com/results/games/3052 for 2014
    *   https://thecgf.com/results/games/3046 for 2010
    *   https://thecgf.com/results/games/3026 for 2006 medals

I mashed up most of the data in Power Query, but had to use a bit of _**Python**_ (more on this in a future blog post) as the medalist by sport page (https://results.gc2018.com/en/all-sports/medallist-by-sport-<country name>.htm) has weird formatting with event name as A tag followed by medalists in a table and this was too much to process in PQ.

**Step 3: Set up the data model**

After gathering all the data in PQ, we can bring only relevant tables to Power BI model. I brought below tables:

*   medals – with medal tables for current (2018) and previous three editions of CG games
*   top 10 countries – event level medal data for top 10 countries in 2018
*   Countries – generated table with top 10 country names and their 3 letter abbreviations
*   medal types – typed in table with URLs for medal images and custom sort order of Gold, Silver and Bronze

![](https://chandoo.org/wp/wp-content/uploads/2018/04/commonwealth-games-viz-data-model.png)

**Step 4: Create measures**

Since one of the goals for this visual is to keep everything under 2 hours, I created only basic measures.

*   `` `Medal Count = sum(medals[Medals])` ``
*   `` `Medal Count for 2014 = CALCULATE([Medal Count], 'medals'[Games] IN { "2014" })` ``
*   `` `Medal Count for 2018 = CALCULATE([Medal Count], 'medals'[Games] IN { "2018" })` ``
*   `` `Medal Count (all) = CALCULATE([Medal Count], all(medals[Games]))` ``
*   `` `Country Name = SELECTEDVALUE(medals[Country]) _for showing in tooltip & chart header_` ``
*   `` `% increase - 2014 to 2018 = DIVIDE([Medal Count for 2018]-[Medal Count for 2014], [Medal Count for 2014], 0) _for showing in tooltip_` ``
*   `` `medal count - top 10 = countrows('top 10 countries')` ``
*   `` `total medal count for country = CALCULATE([medal count - top 10], all('top 10 countries'[Event]))` ``
*   `` `medal % = [medal count - top 10] / [total medal count for country]` ``

As you can see, these are basic arithmetic or simple CALCULATE measures. I used the excellent _quick measure_ feature to create the Medal Count for 2014 measure and learned about IN keyword. #awesome

**Step 5: Create visuals**

**_Visual for exploring medal performance by country_**

![](https://chandoo.org/wp/wp-content/uploads/2018/04/matrix-visual-medals-by-country.png)

I started with a simple slicer on games year and a matrix visual by country in rows, medal type in columns and medal count in values. Then I added data bars to the medal count.

_**Visual for exploring change over time:**_

![](https://chandoo.org/wp/wp-content/uploads/2018/04/ribbon-chart-medal-change-over-time.png)

Then I added Ribbon chart with Games, Medal Type and Medal Count to see how total medals have changed over time. When you pick a country from the matrix, this visual updates to show how that country’s performance changed over time.

_**Visual for seeing which countries improved in 2018:**_

![](https://chandoo.org/wp/wp-content/uploads/2018/04/which-countries-have-improved-in-2018-games.png)

I added a scatter chart with  Country as legend, Medal count for 2018 as X and Medal count for 2014 as Y. Then I added **symmetry shading** to this chart from analytics pane. Viola, we can see which countries did well or worse in this round compared to 2014.

_**Visual for tool tip**_

![](https://chandoo.org/wp/wp-content/uploads/2018/04/tooltip-powerbi-explained.png)

I inserted a new page (called Country Medals), changed the format to **Tooltip** and added a few visuals to make it a tool tip for the scatter chart.

Setting up tooltips is still painful, but this is a new feature, so I am sure MS will add more teeth to this power.

_**Linking scatter chart and tooltip**_

Select the scatter chart and from Format pane, set up tooltip to a report page and select Country Medals page.

![](https://chandoo.org/wp/wp-content/uploads/2018/04/linking-tooltip-to-a-chart-powerbi.png)

_**Visual for seeing where top 10 countries excel**_

![](https://chandoo.org/wp/wp-content/uploads/2018/04/top-10-countries-and-their-medals-by-event-area.png)

I added another matrix visual with Event in rows, abbreviated country name in columns and medal % in values. Then I added conditional formatting > Background color scales to spot bigger numbers easily.

This visual and the scatter plot are then linked to a slicer on medal type (Gold / Silver / Bronze) so you can see event performance and change over time for any type of medal.

_**Formatting the visuals**_

The default colors for visuals use Power BI color scheme. I changed the colors to match medals – Gold, Silver and Bronze so that they are easy to spot. Unfortunately, this would not sync across all visuals, so we have to format each of the visuals (well, only two – ribbon chart and bar chart on the tooltip page)

### Download Commonwealth games Power BI Viz

[**Click here to download the workbook**](https://files.chandoo.org/pbix/medal-tally.pbix)
. Examine the query definitions (especially top 10 countries) to learn some quirky ways to work with Power Query. Enable _interactions_ from view ribbon to see how each visual interacts with others. Play with it and mash up your own data to create something equally awesome. If you end up making another viz from this data, feel free to post it in the comments section so we all can see and learn from you.

### Want to learn Power BI? Check out Power BI Play Date

If you like what you have seen and want to learn how to build such cool visualizations and reports for your work, **[sign up for my Power BI Play Date](https://chandoo.org/wp/resources/power-bi-play-date/)
**. We are opening next batch very soon.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [8 Comments](https://chandoo.org/wp/how-your-country-did-in-commonwealth-games-power-bi-viz-and-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-your-country-did-in-commonwealth-games-power-bi-viz-and-tutorial/#respond)
    
*   Tagged under [advanced power bi](https://chandoo.org/wp/tag/advanced-power-bi/)
    , [calculate()](https://chandoo.org/wp/tag/calculate/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [interactive charts](https://chandoo.org/wp/tag/interactive-charts/)
    , [measures](https://chandoo.org/wp/tag/measures/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    , [web queries](https://chandoo.org/wp/tag/web-queries/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousVisualizing Commonwealth games performance – Interactive chart](https://chandoo.org/wp/visualizing-commonwealth-games-data/)

[NextCreate your first interactive chart in Excel with this tutorialNext](https://chandoo.org/wp/interactive-charts-tutorial/)

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
    
    [Reply](https://chandoo.org/wp/how-your-country-did-in-commonwealth-games-power-bi-viz-and-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-your-country-did-in-commonwealth-games-power-bi-viz-and-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-your-country-did-in-commonwealth-games-power-bi-viz-and-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
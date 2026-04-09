# Making interactive charts in Excel - A case study with gender equality gap data - Advanced charting examples

**Source:** https://chandoo.org/wp/gender-equality-gap-interactive-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Closing gaps in this Gender Equality Gap chart…
===============================================

*   Last updated on November 5, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Today lets close some gaps._

Recently I saw [this interesting chart on Economist Daily Charts page](http://www.economist.com/blogs/graphicdetail/2013/10/daily-chart-18)
. This chart is based on World Economic Forum’s survey on how women compare to men in terms of various development parameters. First take a look at the chart prepared by Economist team.

![Gender inequality gaps in G20 countries - chart from The Economist](https://img.chandoo.org/vp/gender-inequality-chart-by-economist.png)

### So what are the gaps in this chart?

This chart fails to communicate because,

*   All country charts look same, thus making it difficult to spot any deviations.
*   We cannot quickly compare one country with another on any particular indicator.
*   It does not [provide a better context](http://chandoo.org/wp/2013/07/11/never-use-simple-numbers-in-your-dashboards/ "Never use simple numbers in your dashboards (bonus tip: how to fix default conditional formatting)")
     (for eg. how did these countries perform last year?)

But criticizing someone’s work is not awesome. Fixing it and making an even better chart, that has awesome written all over it. So that is what we are going to do.

Fixing the gaps in Gender Equality chart
----------------------------------------

First take a look at the improved chart. Play below video.

**[Download this Excel Chart](https://img.chandoo.org/vp/gender-gap-chart-v1.xlsx)
.**

### Step 1: Getting the data for this chart

Although folks at Economist have not included source data, the good people at WEF have provided detailed PDF reports ([2013](http://www.weforum.org/reports/global-gender-gap-report-2013)
, [2012](http://www.weforum.org/reports/global-gender-gap-report-2012)
) where all the data is naked and waiting for us, analyst to pounce and go nuts.

I copy pasted table in to Excel.

While 2012 data loaded alright, 2013 loaded in a weird fashion.

So we move to step 2.

### Step 2: Cleaning the data

I feel dirty every time I clean a piece of data 😉

But I also like it (cleaning part, not feeling dirty part). I learn some techniques when I am working with messy, sticky and disorganized data sets.

The 2013 data is pasted in to Excel in this format.

![2013 gender inequality data looked like this when copy pasted to Excel](https://img.chandoo.org/vp/2013-gender-gap-data-explained.png)

**From this, we need to transform our data to:**

![This is how we want to data to look like so that we can easily analyze and make charts - gender gap chart in Excel](https://img.chandoo.org/vp/transforming-data-what-we-want.png)

If we know magic, we could point our wand at the table and say something like, _Mobiliarbus Datum.  
_

Alas. We are muggles. So lets rely on the most potent magic we know: **Excel formulas.** [Using INDEX + MATCH combination](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
, we can easily convert 2013 data to the format we want.

The actual formula to fetch overall rank (2nd item in the list for each country) is,

\=INDEX(gaps2013,MATCH($B5,gaps2013,0)+1)

**Explanation:**

*   gaps2013 is the range where all the 2013 gender gap survey data is copied
*   B5 contains the name of the country for which we want the data.
*   +1 because we want to get rank, not country name.

For more, read [how to get VLOOKUP + 1 item](http://chandoo.org/wp/2013/06/25/how-to-get-vlookup-1-value/)
.

### Step 3: Set up form controls

Now that we have sparkling clean data, lets create necessary form controls on our output sheet.

![Form controls on our Interactive gender gap Excel chart](https://img.chandoo.org/vp/form-controls-on-gender-inequality-interactive-excel-chart.png)

![Sorting types in our interactive excel chart - gender inequality in G20 countries](https://img.chandoo.org/vp/sorting-types-for-the-gender-chart.png)We need 2 controls.

1.  A combo-box (drop-down) control so that user can select what field to sort the report on.
2.  A set of option buttons to specify which average to compare.

The combo-box is set up to use the list of values shown aside.

Related: [Introduction to Excel Form Controls](http://chandoo.org/wp/2011/03/30/form-controls/)
.

Lets link these to 2 cells, named **sortCol** & **avgType** on a different sheet. Call this sheet as _**calculations**_**.** All our formulas will go here.

### Step 4: Find sort order based on the selected column

This is the tricky part. I am going to give highlights here and point you to a link where you can learn more.

*   Fetch the column we want to sort in a range of cells.

_**If sorting a number column:**_

1.  Make the column unique by adding a very small running fraction.
2.  This ensures that if our data has duplicates, still our formula works.
3.  Find the sort order of each item using RANK() formula.
4.  Refer to [Sorting KPIs using Formulas article](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
     for more on this technique.

_**If sorting a text column:**_

1.  Find the sort order using COUNTIF() formula.
2.  Refer to [sorting text using formulas article](http://chandoo.org/wp/2008/10/22/sorting-text-in-excel-using-formulas/)
    .

![Sorting values using formulas - example - Gender gap in G20 countries - interactive Excel chart](https://img.chandoo.org/vp/sorting-text-or-numbers-using-formulas.png)

### Step 5: Re-arrange all data in the sort order

[Using INDEX formula](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/ "7 reasons why you should get cozy with INDEX()")
, rearrange all data according to the sort order.

### Step 6: Calculate % change values

Based on 2012 & 2013 scores, calculate % change and place them in the last 5 columns.

### Step 7: Calculate averages

Calculate averages (both G20 & all country values) for all the columns and place them somewhere on your calculations worksheet.

Related: [Calculating the average of every nth item](http://chandoo.org/wp/2013/09/05/calculating-average-of-every-nth-value-formula-tips/)
.

### Step 8: Create charts

Here is the process for creating chart for Overall Score (2013). The same process is used to create all the charts.

1.  Select all the numbers in overall score column.
2.  Create a bar chart
3.  Select vertical axis and press CTRL+1 to format it.
4.  Select **“Categories in reverse order.”**
5.  Adjust series gap to 25%
6.  Set horizontal axis min to 0 and max to 1 and remove the axis.
7.  Remove vertical axis, grid lines
8.  Remove title
9.  Fill chart background & plot background with no color.
10.  Set chart outline to no outline.
11.  And you are done!

_See the demo aside to understand the process._

![Steps you need to clean up charts - Gender inequality chart in Excel](https://img.chandoo.org/vp/cleaning-up-a-chart-in-excel.gif)

### Step 9: Add average as secondary series to the chart

Calculate which average to use in the chart based on the _avgType_ value. And fetch that number to a cell.

Now add average to the chart as a line. This can be done by,

1.  Adding average point to the chart as second series
2.  Converting this series to scatter (XY) plot.
3.  Adjusting the X & Y values of the average point.
4.  Adding 100% positive (or negative) error bar
5.  Formatting the error bar to make it look like a line.
6.  Removing any axis, grid lines added in the process.

### Step 10: Oh wow, this is getting long. Have a coffee

I guess this is now a fairly long process. But closing gender gaps (or gaps in the gender gap chart) is never easy. So have a cup of coffee or tea. Rejuvenate and come back.

### Step 11: Create all other charts

Follow the same process and create rest of the charts.

One easy way to create rest of the charts is,

1.  Copy the first chart and paste it elsewhere.
2.  Select the bars and edit the range address in the formula bar.
3.  Select the average point and edit that too.
4.  Adjust axis if needed.
5.  And you are done!

### Step 12: Put everything together

Create a nice table like structure in your output tab and put everything together. Re-size and position the charts as needed. Make sure the colors are nice. Add conditional formatting to highlight column being sorted and you are done!

![Improved gender inequality chart - made in Excel with interactive features](https://img.chandoo.org/vp/improved-gender-inequality-excel-interactive-chart.png)

### Missing Steps

I have deliberately omitted a few steps in this process to keep it simple. For those of you with a keen eye:

*   Using conditional formatting data bars for the % change column.
*   Turning on / off last column in the report based on sort selection using conditional formatting.
*   Adding data labels to the country names based on the sort selection.

Download this Excel chart
-------------------------

[**Click here to download this Excel chart**](https://img.chandoo.org/vp/gender-gap-chart-v1.xlsx)
. Play with it. Explore the chart settings, formats, formulas and controls to understand it better.

Conclusions – What does the Gender Inequality Chart say?
--------------------------------------------------------

After all this analysis, 2 things are clear.

*   In most countries, women have high equality with men when it comes to health or education.
*   The real gap seems to be in politics & economical development of women.

While this may seem like common sense, it also means, World Economic Forum people should measure inequality on some more parameters. There is little point tracking and analyzing indicators related to health or education (especially in OECD or Western countries).

_**What do you think?**_

Want to fill gaps in your Excel knowledge
-----------------------------------------

While no one appreciates gender inequality, we all love awesomeness inequality. There is nothing wrong in wanting to be more awesome than your peers. And here is how you can be unmatched…

*   [Using Panel charts to understand data](http://chandoo.org/wp/2010/05/12/introduction-to-panel-charts-using-excel-tutorial-template/)
    
*   [Spot matrix charts – alternative to radars](http://chandoo.org/wp/2008/10/07/excel-radar-charts-replacement-spot-matrix-download-template/)
    
*   [Analyzing performance of stocks using charts](http://chandoo.org/wp/2011/09/21/analyzing-performance-of-stocks-using-excel-example/)
    
*   [Suicides & Murders data – interactive analysis](http://chandoo.org/wp/2011/09/09/suicides-murders-interactive-chart/)
    
*   [Visualizing world education rankings](http://chandoo.org/wp/2010/12/20/world-education-rankings-visualization/)
    
*   [Survey data analysis with in-cell charts](http://chandoo.org/wp/2010/04/01/incell-panel-chart/)
    

### Want some challenge… How would you analyze this data?

If you want some challenge, go ahead and [download the file](https://img.chandoo.org/vp/gender-gap-raw-data.xlsx)
. It has all the data for 2012 & 2013. Analyze it and share with me your charts. You can email me at chandoo.d@gmail.com or upload your files somewhere and post the links in comments. I would love to see how you can analyze and present this data.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [8 Comments](https://chandoo.org/wp/gender-equality-gap-interactive-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/gender-equality-gap-interactive-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [Charts & Graphs](https://chandoo.org/wp/tag/charts-graphs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [error bars](https://chandoo.org/wp/tag/error-bars/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sorting](https://chandoo.org/wp/tag/sorting/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [visualization projects](https://chandoo.org/wp/tag/visualization-projects/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousWhat areas of Excel scare you most? \[survey\]](https://chandoo.org/wp/what-areas-of-excel-scare-you-most-survey/)

[NextReplace formulas with values using this shortcut \[quick tip\]Next](https://chandoo.org/wp/replace-formulas-with-values/)

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
    
    [Reply](https://chandoo.org/wp/gender-equality-gap-interactive-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/gender-equality-gap-interactive-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/gender-equality-gap-interactive-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# Use Donut Bar Charts to Display Product-wise Sales Breakup - Excel Charting Tutorial & Download

**Source:** https://chandoo.org/wp/donut-bar-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Recipe for a Donut Bar Chart
============================

*   Last updated on September 30, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We all know that bar charts can be used to display values spread across various categories or times. We also know that pie charts / donut charts can be used to display percentage breakup of various quantities in a sum total. How about mashing up both to create a Donut Bar chart?

_“oh, donut what?!? It sounds like a brand new junk food from dunkin’ donuts”_

Well, not really. It is a mash-up or [combo chart](http://chandoo.org/wp/2009/01/05/excel-combination-charts/)
 using which you can display, for eg. sales over last few years along with percentage break-up of individual products. See below to understand.

![Use Donut Bar Charts to Display Product-wise Breakups in Sales](https://chandoo.org/img/c/donut-bar-chart.gif)

In the above chart we have mixed a bar chart with a donut chart and sprinkled it generously with a scroll bar form control.

In this charting tutorial, we will learn how to cook a donut bar chart using Microsoft Excel. Scroll down the page to get the downloadable workbook to see this in action.

Recipe for making a donut bar chart
-----------------------------------

A good donut bar can be healthy while adding variety to your regular menu of charts. To make a neat looking donut bar chart, just follow the recipe.

**Ingredients:**

Sales data (finely chopped – year vs product level), one donut chart, one bar chart, one scroll bar form control and 5 minutes of spare time.

### Step 1: Get your dough, err, data ready

As with any chart, we need the right data in right format to make a perfect donut bar chart.

I have arranged the data for our chart in the below format.

![Data and Format for Donut Bar Chart](https://chandoo.org/img/c/donut-bar-chart-data.png)

The last column shows the values as per scroll bar position. (more on this in the next steps)

### Step 2: Insert a scroll bar control and link it to a cell

![Scrollbar settings for Donut Bar Chart](https://chandoo.org/img/c/scrollbar-settings-donut-bar-chart.png)Go to developer ribbon tab and insert a scroll bar form control. (learn more about [turning on developer toolbar in excel 2007](http://chandoo.org/wp/2009/05/26/excel-2007-productivity-tips/)
)

Once you have the scroll bar, link it to a cell, say B18.

Also, set the scroll-bar minimum value as 1, maximum value as the number of years you have (in our case it is 14) and incremental change to 1.

### Step 3: Determine product-wise breakups and totals based on scroll bar selection

We can use INDEX() excel formula to do this.

**What is INDEX excel formula?**

INDEX formula ([examples](http://chandoo.org/wp/tag/index/ "Example of INDEX Formula")
) returns a specific value from a range of cells by taking the row and column of that range as input. For eg. =INDEX(A1:C10,2,1) will return the value in 2nd row, 1st column, ie, the value in cell A2.

**So, how to write the INDEX formula in our case?**

That is your home work. Just use the kitchen sink to experiment.

Once you are done, the product-wise breakups should be listed in a tabular format like this.

![Scrollbar settings for Donut Bar Chart](https://chandoo.org/img/c/donut-values-based-on-selection.png)

### Step 4: Put everything together and boil for a minute

We have done all the ground work required to make the donut bar chart. Now, We just need to put everything together and make some charts. Here we have 4 small steps.

![steps for making donut bar chart](https://chandoo.org/img/c/donut-bar-chart-recipe.png)

1.  Insert a donut chart using the product-wise breakup data
2.  Insert a bar chart with the yearly totals
3.  Insert another series in the bar chart to show the selected year total. Completely overlap this series with the totals series.
4.  Position everything together.

_**Finally adjust formatting and colors as per your taste.**_

That is all, the donut bar is ready for consumption. Serve hot or chilled. The donut bar tastes great with a cup of coffee.

Download the donut bar chart excel work book and play with it
-------------------------------------------------------------

[Click here](http://chandoo.org/img/d/donut-bar-chart-template.xls "Donut Bar Chart - Template")
 to download the donut bar chart template & workbook. Change the values and chart attributes to understand how this works.

**Also try** a Bar Pie chart, just follow the same recipe, but replace donut with pie.

Please tell me how your donut bar tasted using comments. 🙂

**Recommended charting tutorials for you:**

*   [Comparing Performance using Excel Charts](http://chandoo.org/wp/2009/03/12/comparison-charts-1/)
    
*   [Sales Funnel Charts using Excel](http://chandoo.org/wp/2009/01/09/funnel-chart-excel-tutorial)
    
*   [Make a Matrix Chart with Excel](http://chandoo.org/wp/2008/10/07/excel-radar-charts-replacement-spot-matrix-download-template/)
    
*   [Dynamic Charts using Data Filters](http://chandoo.org/wp/2009/02/12/make-a-dynamic-chart-using-data-filters/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [25 Comments](https://chandoo.org/wp/donut-bar-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/donut-bar-chart/#respond)
    
*   Tagged under [axis labels](https://chandoo.org/wp/tag/axis-labels/)
    , [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [combination charts](https://chandoo.org/wp/tag/combination-charts/)
    , [combo charts](https://chandoo.org/wp/tag/combo-charts/)
    , [donut charts](https://chandoo.org/wp/tag/donut-charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [formatting](https://chandoo.org/wp/tag/formatting/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [rows()](https://chandoo.org/wp/tag/rows/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious5 Things you probably dont know about this site](https://chandoo.org/wp/5-things-you-probably-dont-know-about-this-site/)

[NextUse Cell Styles to Make your Spreadsheet Models User-friendly \[Quick Tip\]Next](https://chandoo.org/wp/use-cell-styles-in-spreadsheet-models/)

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
    
    [Reply](https://chandoo.org/wp/donut-bar-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/donut-bar-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/donut-bar-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
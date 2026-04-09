# Tornado Chart in Excel - Step by Step tutorial & Sample File » Chandoo.org

**Source:** https://chandoo.org/wp/excel-tornado-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Impress with Tornado Charts in Excel
====================================

*   Last updated on October 7, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

It’s tornado season. Don’t freak out, I am talking about Excel tornado charts. **Use them to visualize age and gender-wise KPIs**. Here is a quick demo of interactive tornado chart made in Excel. Watch it and read on to learn how to make your own tornado in a spreadsheet.

![Tornado Chart Excel - Demo](https://chandoo.org/wp/wp-content/uploads/2019/10/tornado-chart-excel-demo.gif)

Demo of tornado chart in Excel – with slicer interactions

When to use Tornado charts?
---------------------------

Tornado charts / population pyramids are very useful in below situations.

*   See population distribution by gender (obviously)
*   Purchase patterns by gender and ages
*   Customer walk-ins by gender and time of day
*   Distribution of time on page by visitor type (customer / prospect)
*   Units purchased by customer types (international vs. domestic)

In general, you can apply this type of charts whenever you have a strong binary category and a detailed dimension (time of day / age / distribution etc.)

How to create tornado chart in Excel?
-------------------------------------

> Just open Excel in your laptop, load your data, go outdoors in Oklahoma (if you live outside Midwestern states then catch a flight to nearest one) and wait for a tornado.

Jokes aside, to tornado charts are nothing but cleverly formatted bar charts. Let me demonstrate how to make them from a sample data of [London’s actual & projected population numbers](https://data.london.gov.uk/dataset/projections/)
.

Watch this video tutorial or read the instructions below to create this chart in Excel.

### Step 1: Calculate necessary numbers for the tornado chart

This depends on your data. For the London population data-set that I am using, we need a summary like this.

![tornado chart calculations - with the help of pivot table](https://chandoo.org/wp/wp-content/uploads/2019/10/calculations-for-tornado-chart-with-pivot-table.png)

I am using a pivot table to make the calculations.

Once you have the numbers by age and gender, we need to turn one of the gender values to negative.

To do this, just create a copy of the _calculations, paste as linked values._ Turn one gender values to negative by using – (minus) sign in the front.

We get this sort of table.

![negative values for one gender - tornado chart calculations](https://chandoo.org/wp/wp-content/uploads/2019/10/linked-cells-from-pivot.png)

Use Paste Links option to get a copy of data. Turn one gender values -ve

### Step 2: Make a stacked bar chart

Select your age by gender (with negative values for one gender) values and insert “stacked bar” chart.

You will get this.

![tornado chart - step 1 - make a stacked bar chart](https://chandoo.org/wp/wp-content/uploads/2019/10/stacked-bar-chart-tornado-1.png)

### Step 3: Format the tornado chart

We are almost done. Just format the chart using below steps.

1.  Set gap between bars to 0 (select any bar, press CTRL+1 to format them and set gap width to 0)
2.  Move vertical axis labels to either low or high position, so that you can read them.
3.  Flip the tornado so you can see age 0 on top and 100 at bottom. To do this, select the vertical axis, go to format and click on “Categories in reverse order” option.
4.  Remove -ve signs from the horizontal axis labels. To do this, select the axis, format and go to “Number” settings. Here, you can tell Excel to omit the -ve sign while displaying labels with special codes. For numbers, you can use the code 0;0;;  
    Related: [For more on custom formatting codes, see this page](https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats/)
    .
5.  Move legend to top
6.  Add relevant chart title and captions if necessary.

Here is a time lapse GIF of the formatting steps.

![tornado chart formatting steps\
](https://chandoo.org/wp/wp-content/uploads/2019/10/tornado-chart-formatting-steps.gif)

Formatting steps for tornado chart

### Step 4: Make it interactive

Now that you have a tornado chart, you can easily make it interactive. Just move the slicer (from step 1) closer to the chart and you have an interactive tornado chart in Excel.

![finished tornado chart](https://chandoo.org/wp/wp-content/uploads/2019/10/excel-tornado-chart.png)

Download Tornado Chart Excel Template
-------------------------------------

**[Click here to download the full tornado chart template](https://chandoo.org/wp/wp-content/uploads/2019/10/tornado-chart.xlsx)
**. Use it to learn how to make these.

Tornado Chart Alternatives
--------------------------

**Histograms and Pareto Analysis**

[![tornado chart alternative - histogram](https://assets.chandoo.org/wp/wp-content/uploads/2017/10/dynamic-histogram-tip.gif)](https://chandoo.org/wp/histograms-pareto-charts-in-excel/)

When you have more than two categories, then try histogram charts. You can explore distribution of all data or make it interactive (with slicers of course). [See this page for details on histograms in Excel](https://chandoo.org/wp/histograms-pareto-charts-in-excel/)
.

**In-cell bar charts – when you have too many categories**

[![tornado chart alternative - in-cell bar chart](https://assets.chandoo.org/wp/wp-content/uploads/2015/09/alternative-3-how-they-spend-it-chart.png)](https://chandoo.org/wp/how-countries-spend-their-money/)

Another option is to make a table visualizing everything. But a table of numbers can be dull. So make them visual with in-cell bar charts. [Here is a case study of survey results](https://chandoo.org/wp/how-countries-spend-their-money/)
 from “how people in various countries spend money?”.

**_[Check out Advanced Charting page](https://chandoo.org/wp/tag/advanced-charting/)
 for more inspiration._**

### Do you make tornado charts?

I create tornado charts often, especially when I am exploring demographic trends.

**What about you?** Do you make tornado charts? If so, how do you make them? Please share your tips and experiences in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/excel-tornado-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-tornado-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [interactive charts](https://chandoo.org/wp/tag/interactive-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [population pyramid](https://chandoo.org/wp/tag/population-pyramid/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [stacked bar](https://chandoo.org/wp/tag/stacked-bar/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousExcel Basics: How to add drop down list to validate data](https://chandoo.org/wp/excel-add-drop-down-list/)

[NextUsing IRR with Data Tables – Modeling Cash-flow Scenarios in ExcelNext](https://chandoo.org/wp/using-irr-with-data-tables/)

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
    
    [Reply](https://chandoo.org/wp/excel-tornado-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-tornado-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-tornado-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
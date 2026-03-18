# Cropped chart: when some values are too big to fit » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/cropped-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Cropped chart: when some values are too big to fit
==================================================

*   Last updated on September 9, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**We know that column charts are excellent for presenting information**. But what if some of the columns are too tall and hijacking the rest. In a previous article, [we discussed few of the approaches](http://chandoo.org/wp/2010/08/20/charts-with-small-and-large-values/)
. Today let’s learn how to build a cropped chart (broken y-axis chart) using Excel, something like this:

![cropped-chart-in-excel](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart-in-excel.png)

Looks interesting? Read on.

Tutorial to create a cropped chart in Excel
-------------------------------------------

### Before we begin: Is this the best chart for this data?

Cropped charts or broken Y-axis charts can be misleading and confusing. That said, in some very rare cases, you may need to use them. My suggestion is simple:

*   See if you can use a regular column chart
*   See if you can use a regular column chart, crop the tall columns at a certain point and fade them using gradient fills. Then apply labels to them so people know which ones are too tall to show on the chart.
*   See if there is any other alternative representation for this data (may be just the numbers in a table?!?)
*   If your boss / client / spouse is adamant about broken y-axis chart / cropped chart, then make one.

### Step 1: Arrange your data

![cropped-chart-values](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart-values.png)Let’s say we have the numbers as shown aside.

We will have to set up some extra calculations to make this  chart. We need to split each column in to 2 portions.

*   Below crop
*   Above crop

But we can do this only for columns that are too tall. Also, we need to know 2 things:

*   At what point we should crop the value – let’s call this _crop_
*   What is the size of crop – let’s call this _size_

We also need to print a cropped symbol (2 zigzag or slant lines) at the location of crop, _if we crop a column._

First, take a look the the calculation setup.

![calculations-for-cropped-chart-explained](https://chandoo.org/wp/wp-content/uploads/2015/09/calculations-for-cropped-chart-explained.png)

The formulas for 3 extra columns are:

Remember, our data starts from **cell B10**.

*   **Crop:** \=IF(B10>crop+size,crop,B10)
*   **Above:** =IF(B10>crop+size,B10-crop-size,0)
*   **Marker:** \=IF(B10>crop+size,crop,NA())

### Step 2: Create a stacked column chart

Select both Crop & Above columns and create a regular stacked column chart. We should get something like this:

![cropped-chart-step2](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart-step2.png)

### Step 3: Add marker series as a line to the chart

Add the marker series (select all the values, copy and paste in to the chart – or use Chart > Select Data > Add option).

Marker series will be added as a stacked column by default.

![cropped-chart-step3-adding-marker-series](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart-step3-adding-marker-series.png)

Right click on it and select change series chart type option.

Change the series to line with markers.

Now, set the line properties to _no line_ so that only markers show up.

At this stage, our cropped chart looks like this:

![cropped-chart-step3-marker-series](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart-step3-marker-series.png)

### Step 4: Replace markers with crop symbol

Draw a crop symbol. Here is one I used:

1.  Draw a box. Fill it with pale white color and remove borders.
2.  Draw 2 horizontal lines and align them to top & bottom edges respectively.
3.  Select all three shapes (2 lines and one box) and group them (right click and group).
4.  Rotate this grouped object a bit.

Copy this object / symbol.

Select the markers on the chart. Press CTRL+V.

Excel replaces the markers with your symbol. (more: [use shapes to enhance your charts](http://chandoo.org/wp/2015/08/08/shapes-in-charts/)
)

At this stage, our chart looks like this:

![cropped-chart-step4-with-crop-symbols](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart-step4-with-crop-symbols.png)

### Step 5: Format the chart

This is easy. Set both crop & above portions to same color. Adjust gap width between columns if necessary.

Play with both _crop_ and _size_ values until you get the perfect chart.

![cropped-chart-step5-formatting](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart-step5-formatting.png)

### Step 6: Add labels to your chart

As you have cropped the columns, the axis is no longer relevant. We either need to replace the axis labels with two sets of values (before crop & after crop) or remove the axis & set data labels.

Setting different axis labels requires a bit more tweaking of the chart.

So, let’s go with data label route.

![data-labels-for-cropped-chart](https://chandoo.org/wp/wp-content/uploads/2015/09/data-labels-for-cropped-chart.png)First remove the vertical axis. To set the labels:

1.  Select the bottom series of the column chart. Right click and choose data labels option.([Click here for a screenshot of this step](https://chandoo.org/wp/wp-content/uploads/2015/09/adding-labels.png)
    )
2.  This adds default labels.
3.  Select the labels and press CTRL+1 to format them
4.  From label options pane, select “Value From Cells” as the source for labels. _Note: This is available only in Excel 2013 or above. For older versions use [XY Labeler add-in by Rob Bevey](http://www.appspro.com/Utilities/ChartLabeler.htm)
    ._
5.  Select the original data (in B10 cell onwards) as the source.
6.  Set up label properties (location, font, font size, color as you see fit)
7.  Done!

That is all. Your cropped chart is ready.

![cropped-chart-in-excel](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart-in-excel.png)

Download cropped chart template
-------------------------------

[**Click here to download cropped chart example workbook**](https://chandoo.org/wp/wp-content/uploads/2015/09/cropped-chart.xlsx)
. The workbook contains all the calculations, full chart and all intermediate steps so that you can learn more.

### Awesome resources on charts

Raise above the rest with these awesome resources on charting:

*   [5 Simple rules to make awesome column charts](http://chandoo.org/wp/2013/08/29/rules-for-making-awesome-column-charts/)
     – [podcast](http://chandoo.org/wp/2015/04/02/cp032-column-chart-rules/)
    
*   [6 Best charts to show progress against a goal](http://chandoo.org/wp/2014/03/10/best-charts-to-show-progress/)
    
*   [Column / bar chart with lower and upper boundary](http://chandoo.org/wp/2014/01/08/bar-chart-with-lower-upper-bounds-tutorial/)
    
*   [Interactive sales chart using Excel](http://chandoo.org/wp/2012/05/09/interactive-sales-chart-in-excel/)
    

**Struggle with charting? Excel School is for you:**

If you are mystified by the Excel charts and spend way more time on them, then consider enrolling in our Excel School program. This will help you learn how to create awesome charts, interactive workbooks, complex dashboards in a structured way.

**[Visit Excel School to know more about this program and enroll](http://chandoo.org/wp/excel-school/)
**.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/cropped-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/cropped-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [broken y axis](https://chandoo.org/wp/tag/broken-y-axis/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [column charts](https://chandoo.org/wp/tag/column-charts/)
    , [combination charts](https://chandoo.org/wp/tag/combination-charts/)
    , [cropped chart](https://chandoo.org/wp/tag/cropped-chart/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousCase Sensitive Lookups](https://chandoo.org/wp/case-sensitive-lookups/)

[NextCP044: My first dashboard was a failure!!!Next](https://chandoo.org/wp/dashboard-failure-story/)

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
    
    [Reply](https://chandoo.org/wp/cropped-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/cropped-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/cropped-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
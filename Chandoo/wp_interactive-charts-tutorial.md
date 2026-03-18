# Create your first interactive chart in Excel with this tutorial » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/interactive-charts-tutorial

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

Create your first interactive chart in Excel with this tutorial
===============================================================

*   Last updated on June 11, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Ever wanted to make a cool, snazzy interactive chart in Excel? Something like this:

![Interactive chart in Excel - howto](https://chandoo.org/wp/wp-content/uploads/2018/04/interactive-chart-in-excel-tutorial.gif)

In this tutorial, learn all about making your very first interactive chart.

[**Click here to download the workbook with chart template**](https://chandoo.org/wp/wp-content/uploads/2018/04/first-interactive-chart-excel.xlsx)
 and all the formulas. Refer to it while reading the article.

Interactive chart in Excel – Tutorial
-------------------------------------

There are several ways to make an interactive chart in Excel. You can use data validation, form controls, slicers, timelines, VBA or hyperlinks. In this tutorial, learn how to make an interactive chart with data validation and slicers. For other techniques, refer to resources section of this post.

### Interactive chart with Data Validation

Let’s say you are the product manager at Billette consumer care. You are looking at historical order quantity data for various products. Your data looks like below:

![Sample data for interactive chart](https://chandoo.org/wp/wp-content/uploads/2018/04/data-for-interactive-chart.png)

Making one chart with all of this is going to be very busy and hard to read. You want to make a dynamic or interactive chart so your boss can choose which product she wants to analyze and understand the order trend.

**Step 1: Make a list of all choices**

*   ![List of option for your users - interactive chart](https://chandoo.org/wp/wp-content/uploads/2018/04/naming-a-range-with-name-box.png)Select all the product names and go to Namebox (top left corner) and type a name like products.
*   Alternatively, you can also list the product names in a separate range and give that a name.

Let’s say we have the products in the _products_ name.

**Step 2: Set up selection mechanism**

*   Decide which cell will have the user selection. Let’s say this is **Q5**. Select the cell and go to Data > Data Validation.
*   Change validation criteria to Allow > List.
*   Type _**products**_ in the Source. Click ok.

![data validation list - interactive chart](https://chandoo.org/wp/wp-content/uploads/2018/04/setting-up-data-validation-for-list.png)

Now, we have way to select product in the cell Q5.

Related: [Excel basics – How to setup in-cell drop downs in Excel](https://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
.

**Step 3: Find out which product is selected**

If we want the name of the product selected, we can simply use _**\=Q5**_. For the rest of calculations, we need the number of the product (ie what is the position of the selected product in **_products_**). For this, we can use MATCH formula, like below.

Type this [MATCH formula](https://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
 in an empty cell like I3.

\=MATCH(Q5, products, 0)

This will return a number, matching the product user has picked.

**Step 4: Calculating order quantity to show in the chart**

Now, assume we have the number of product selected in cell **I3**. Given this, we can calculate picked product’s quantity using a simple [INDEX formula](https://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
:

\=INDEX(data1\[@\[Soap\]:\[Deodorant\]\],$I$3)

If your data is in a normal range, rather than a table, use a formula like this:

\=INDEX(C6:H6,$I$3)

Fill down the formula.

![Using INDEX formula for interactive chart](https://chandoo.org/wp/wp-content/uploads/2018/04/INDEX-formula-for-interactive-chart-explained.png)

Now that we have calculated product quantity values for selected product, if you change I3, you will see values for the relevant product.

**Step 5: Create the chart**

Now that all the background work is done, let’s insert a chart.

Simply select picked product column and insert a column or line chart. We get this:

![Making interactive chart in excel - step 1](https://chandoo.org/wp/wp-content/uploads/2018/04/interactive-chart-in-making-step5.1.png)

First, let’s add axis labels. Right click on the chart and go to select data. Edit horizontal / category labels and select the month column.

Now, remove chart title and chart border (set it to no line). We end up with something like this:

![Making interactive chart in excel - step 2](https://chandoo.org/wp/wp-content/uploads/2018/04/interactive-chart-in-making-step5.2.png)

**Step 6: Bring everything together**

Are you ready for the chart? We are almost done. We just need to bring everything together and our first interactive chart will be kicking and beating.

*   Position the chart under cell Q5 (the data validation selection cell)
*   Go to Insert > Shapes > Rounded Rectangle and draw a nice big rectangle around the chart and Q5.
*   Remove fill color from the shape and adjust the line.
*   Now, when you pick a new product from Q5, your chart will update.

![Making interactive chart in excel - final result](https://chandoo.org/wp/wp-content/uploads/2018/04/interactive-chart-finalized.png)

### Interactive chart with Pivot Table and Slicer

If you are too shy to INDEX + MATCH on weekdays, you can try the Pivot Table approach. This works very well and let’s you make equally amazing interactive charts. See below quick demo.

![interactive chart with Pivot Tables](https://chandoo.org/wp/wp-content/uploads/2018/04/interactive-chart-with-pivot-slicer-demo.gif)

Keep in mind that your data needs to get fit. Rearrange so it looks like this. If you need help, read: [Unpivot data quickly with Power Query](https://chandoo.org/wp/2015/09/29/unpivot-data-with-power-query/)
.

![Data for pivot table slicer interaction](https://chandoo.org/wp/wp-content/uploads/2018/04/data-for-pivot-slicer-interactive-chart.png)

**Step 1: Insert a pivot from your data**

Select your data (month, product and quantity columns) and insert a pivot table.

*   Add Month to row labels area. In newer versions of Excel, this will create date hierarchy – Year, Quarter and Month. If so, drop Quarter.
*   Add Quantity to values area.
*   Right click on Product and add it as a slicer.

![Pivot table setup for interactive charts](https://chandoo.org/wp/wp-content/uploads/2018/04/pivot-table-setup-for-interactive-chart-illustration.png)

Related: [Introduction to Excel Pivot Tables](https://chandoo.org/wp/excel-tutorial/working-with-pivot-tables/)

**Step 2: Insert a pivot chart**

Select any cell inside the pivot and go to Analyze ribbon > Pivot chart. Select either a line or column chart.

We get this:

![pivot chart default behavior](https://chandoo.org/wp/wp-content/uploads/2018/04/pivot-chart-default.png)

_In newer versions of Excel, you can insert a pivot chart directly from data. But I find the pivot table first approach better as you can adjust items you want before charting._

**Step 3: Format the pivot chart**

*   Select the pivot chart and go to Analyze ribbon and turn off Field Buttons.
*   Replace chart title with “Total Order Quantity in last 13 months” or something like that.
*   Set chart border to _No line._
*   Position the slicer adjacent to the chart.
*   Draw a rounded rectangle around the thing
*   Our interactive chart is ready for play.

### Optional makeup hints:

If you want more bang for your chart,

*   **Add a sub-title describing the trend.** Refer to download example file for inspiration. Read: [Give descriptive titles to your charts](https://chandoo.org/wp/2015/08/19/descriptive-titles-on-charts/)
    
*   **Set limits on the vertical axis.** By default Excel will change Y axis limits whenever your pick a product. This can create some distortion of the numbers and confuse your users if they want to compare products. You can format the axis and set limits. Select the axis, press CTRL+1 and set minimum to 0 and maximum to highest possible value (rounded of course). For our example, this could be 2000. This way, only bar heights change, not the axis.
*   **Adjust gap width**. Excel would pick some ridiculous value like 219%. Adjust this to 100% or something like that for less white space on the chart. To do this, click on the columns, press CTRL+1 and from Series options adjust the gap width.

### Create your first interactive chart in Excel – Video tutorial

Check out below video tutorial to understand all these steps in detail. Make sure you practice by downloading the example workbook. Watch it below or [on our YouTube channel](https://youtu.be/ZWDjkWvJrEQ)
.

### Download Excel Interactive Chart workbook

[**Please click here to download interactive chart workbook**](https://chandoo.org/wp/wp-content/uploads/2018/04/first-interactive-chart-excel.xlsx)
. Play with charts and examine formulas to learn more.

**Want more interactive charts?**

Check out below examples to see what else is possible.

*   [Target vs. Actual – Biker on a hill chart](https://chandoo.org/wp/2016/09/20/biker-on-hill-chart/)
    
*   [Then vs. Now chart in Excel](https://chandoo.org/wp/2013/08/06/how-to-create-a-then-vs-now-interactive-chart-in-excel/)
    
*   [How tax burden has changed over time – Interactive chart in Excel](https://chandoo.org/wp/2012/12/06/tax-burden-chart-excel/)
    

### What is your favorite way to make interactive / dynamic charts in Excel?

I used to make charts with formulas all the time. But now a days, I prefer making them with pivot table + slicer route if possible. This reduces the amount of formula work needed and still gives awesome results.

_**What about you?**_ What is your favorite technique for creating interactive charts? Please share in the comments section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/interactive-charts-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interactive-charts-tutorial/#respond)
    
*   Tagged under [column charts](https://chandoo.org/wp/tag/column-charts/)
    , [data validation](https://chandoo.org/wp/tag/data-validation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [drop down lists](https://chandoo.org/wp/tag/drop-down-lists/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [interactive charts](https://chandoo.org/wp/tag/interactive-charts/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousHow your country did in Commonwealth Games – Power BI Viz and Tutorial](https://chandoo.org/wp/how-your-country-did-in-commonwealth-games-power-bi-viz-and-tutorial/)

[NextTop 5 keyboard shortcuts for Excel ChartsNext](https://chandoo.org/wp/charting-shortcuts/)

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
    
    [Reply](https://chandoo.org/wp/interactive-charts-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interactive-charts-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interactive-charts-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
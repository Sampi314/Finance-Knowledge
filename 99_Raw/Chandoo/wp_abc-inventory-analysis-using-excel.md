# ABC Inventory Analysis - Tutorial & Excel Template

**Source:** https://chandoo.org/wp/abc-inventory-analysis-using-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

ABC Inventory Analysis using Excel
==================================

*   Last updated on October 3, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**ABC analysis** is a popular technique to understand and categorize inventories. Imagine you are handling inventory at a plant that manufactures high-end super expensive cars. Each car requires several parts (4,693 to be exact) to assemble. Some of these parts are very costly (say few thousand dollars per part), while others are cheap (50 cents per part). So how do you make sure that your inventory tracking efforts are optimized so that you waste less time on 50 cent parts & spend more time on costly ones?

This is where ABC analysis helps.

We group the parts in to 3 classes.

*   **Class A:** High cost items. Very tight control & tracking.
*   **Class B:** Medium cost items. Tight control & moderate tracking.
*   **Class C:** Low cost items. No or little control & tracking.

Given a list of items (part numbers, unit costs & number of units needed for assembly), how do we _automatically figure which class each item belongs to?_

And how do we generate below ABC analysis chart from it?

![ABC Analysis for inventory tracking & controls - Excel chart & template](https://img.chandoo.org/c/abc-analysis-for-inventory-tracking-excel-chart.png)

That is what we are going to learn. So grab your inventory and follow along.  
(related: [ABC Analysis page on Wikipedia](http://en.wikipedia.org/wiki/ABC_analysis)
)

ABC Analysis using Excel – Step by step tutorial
------------------------------------------------

### 1\. Arrange the inventory data in Excel

Pull all the inventory (or parts) data in to Excel. Your data should have _at least_ these columns.

*   Part Name
*   Unit cost
*   \# of units (if this is blank, just type 1 in all rows)

![Input data format - ABC Analysis for inventory tracking & control using Excel](https://img.chandoo.org/c/abc-analysis-raw-data.png)

Once the data is in Excel, turn it in to a table by pressing CTRL+T. Lets call our data as _inventory._ You can set the table name from Design tab.

(Related: [Introduction to Excel Tables](http://chandoo.org/wp/2009/09/10/data-tables/)
)

### 2\. Calculate extra columns needed for ABC classification

Now comes the fun part. Crunching the inventory data with formulas. _Yummy!_

**Total Cost:** This is just a multiplication of unit cost & # of units columns

**Rank:** We need to figure out what rank each total cost is (in the total cost column). We can use RANK formula for this.

`=RANK([@[Total Cost]],[Total Cost],0)` will tell us the rank for each total cost.

**Cumulative Units:** Once we know the rank of each item, next we need to figure out how many total units are needed for items ranked less or equal.

For example, The number (#) of the third part (PT3959-waes) is 3. Cumulative units for this is 91. _This means, 91 is the total number of units for first three ranked parts (parts # 8, 9, and 16)._

The formula for this is, `=SUMIFS(['# Units],[Rank],"<="&[@['#]])`

Remember, \[@\[‘#\]\] refers to running numbers (1,2,3….4692,4693)

**Cumulative Units %:** This is a percentage of cumulative units in total. The formula is simply,

`=[@[c Units]]/MAX([c Units])`

\[Related: [using structural references in Excel – video](http://chandoo.org/wp/2013/06/26/introduction-to-structural-references/ "Introduction to Structural References")\
\]

**Cumulative Cost & Cumulative Cost %:**

These are similar calculations (instead of units, we calculate cost)

**Explanation of these calculations:**

See below animation to understand how the numbers are crunched.

![Calculations for ABC Inventory analysis - Explained.](https://img.chandoo.org/c/abc-inventory-analysis-calculations-explained.gif)

### 3\. Create Inventory Distribution Chart

Select cumulative units & cumulative cost % columns and create an XY chart. Make sure cumulative units is on horizontal (X) axis and cumulative cost % is on vertical (Y) axis.

Our curve should look something like this.

![ABC Analysis cure - step 1](https://img.chandoo.org/c/abc-analysis-chart-1.png)

### 4\. Set up ABC classification thresholds

Now we need to decide what is the threshold for classes A,B & C.

For most situations, Class A tends to be top 10% of the items.

Class B would be next 20%

Class C would be the last 70%.

But these numbers may change depending on your industry, manufacturing settings.

Lets say, some where in our spreadsheet, user has defined the thresholds for the classes in a range like this:

![ABC threshold values - Inventory tracking & controls using Excel](https://img.chandoo.org/c/abc-threshold-input-range.png)

So `$O$7:$O$9` contains the thresholds.

Next to this range, calculate additional numbers (for plotting A, B & C markers and boxes) like this:

![Calculations for ABC class markers & boxes](https://img.chandoo.org/c/calculations-for-abc-markers-and-boxes.png)

_Examine the download file for exact formulas._

### 5\. Add the ABC items & % total cost columns to chart

Add the extra data to the chart (by right clicking on chart and going to select data box & clicking “Add” button).

Once the new series is added, make sure you format it as markers only so that we get something like this.

### ![ABC inventory analysis chart - step 2](https://img.chandoo.org/c/abc-analysis-chart-2.png)

### 6\. Add Error bars to the ABC markers to get boxes

![Adding error bars  - ABC inventory analysis in Excel](https://img.chandoo.org/c/adding-error-bars-2013-excel.png)This step involves adding error bars to ABC marker series and customizing them.

**In Excel 2013:** Add error bars by clicking on the + button next to chart

**In earlier versions:** Do this from **layout ribbon**

Once error bars are added, customize them (select and press CTRL+1). Set error amount to **Custom** and select the calculated error values as shown below.

![Custom error bar values in Excel - demo](https://img.chandoo.org/c/customizing-error-bars-excel-chart.png)

Once added, format the error bars to show _no cap_ and change line color to something pleasant.

Now we have boxes on the chart.

![ABC inventory analysis chart - step 4 - with ABC boxes](https://img.chandoo.org/c/abc-analysis-chart-4.png)

### 7\. Clean up the chart, add labels & titles

This is where get creative. After some clean up, we can arrive at something like this.

![ABC inventory analysis uisng Excel - final chart](https://img.chandoo.org/c/abc-analysis-for-inventory-tracking-excel-chart.png)

Download ABC Inventory Analysis Template Workbook
-------------------------------------------------

[**Click here to download ABC Inventory Analysis workbook**](https://img.chandoo.org/d/abc-inventory-analysis.xlsx)
. It contains sample data & chart. Examine the formulas & chart settings to learn more. Or if you are in a hurry, replace the sample data with your inventory details and get instant results.

Do you use ABC analysis for inventory tracking & control?
---------------------------------------------------------

I will be honest. I have never worked as inventory controller in a super-car manufacturing plant. That said, I run a business and we do have inventory. Not physical but digital inventory. So I often use analysis like ABC or pareto to quickly figure out where I should focus my efforts.

**What about you?** Do you use techniques like ABC analysis to narrow down to a few items that matter most? How do you do it in Excel? Please share your tips & experiences using comments.

### Add few more techniques to your inventory

Feeling low on your Excel skills inventory? Stock up with below goodies.

*   [Pareto Analysis in Excel – How to & tutorial](http://chandoo.org/wp/2009/09/02/pareto-charts/)
    
*   [Analyzing competition using charts – case study](http://chandoo.org/wp/2010/10/25/competition-analysis-charts/)
    
*   [Track employee vacations & productivity \[dashboard & tutorial\]](http://chandoo.org/wp/2013/01/24/employee-vacations-tracker-dashboard/)
    
*   [Track annual goals & achievements](http://chandoo.org/wp/2010/03/01/employee-goal-tracker-excel/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [44 Comments](https://chandoo.org/wp/abc-inventory-analysis-using-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/abc-inventory-analysis-using-excel/#respond)
    
*   Tagged under [abc](https://chandoo.org/wp/tag/abc/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [analysis](https://chandoo.org/wp/tag/analysis/)
    , [analytical charts](https://chandoo.org/wp/tag/analytical-charts/)
    , [chart formatting](https://chandoo.org/wp/tag/chart-formatting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [error bars](https://chandoo.org/wp/tag/error-bars/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [inventory](https://chandoo.org/wp/tag/inventory/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [pareto charts](https://chandoo.org/wp/tag/pareto-charts/)
    , [scatter plot](https://chandoo.org/wp/tag/scatter-plot/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [tracker](https://chandoo.org/wp/tag/tracker/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousDrag to multi-select slicer items \[quick tip\]](https://chandoo.org/wp/drag-to-multi-select-slicer-items-quick-tip/)

[NextCP021: How to quickly compare 2 lists in ExcelNext](https://chandoo.org/wp/cp021-how-to-quickly-compare-2-lists-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/abc-inventory-analysis-using-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/abc-inventory-analysis-using-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/abc-inventory-analysis-using-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
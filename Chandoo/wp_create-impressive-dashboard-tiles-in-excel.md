# Create impressive dashboard tiles in Excel

**Source:** https://chandoo.org/wp/create-impressive-dashboard-tiles-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

Create impressive dashboard tiles in Excel
==========================================

*   Last updated on March 20, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

If you want to tell the story of how your business / project / charity / thing is going on, then [making a dashboard](https://chandoo.org/wp/kpi-dashboard-revisited/)
 is the best way to go about it. Dashboards can combine heaps of data, insights and messages in to one concise format that fits on to a desktop or table or mobile screen.

But let’s be honest. Creating them in Excel is a lot of work. Even after spending hours on them, they might still look _meh._ So, let me share a trick to make your dashboards look snazzy (without compromising on insights per inch).

**Create dashboard tiles, something like this:**

![dashboard-tiles-excel](https://chandoo.org/wp/wp-content/uploads/2019/03/dashboard-tiles-excel.png)

How to create Excel dashboard tiles
-----------------------------------

Here is a step-by-step process to create dashboard tiles.

### 1\. Calculate necessary numbers and place them in cells

This is simple. Let’s say you want to make a “Total Budget” tile, that reads  
Total Budget  
$420,500

Let’s assume the number 420,500 is in cell C11.

### 2\. Use TEXT formula to convert numbers to the format you want

If you have a number in cell, you can easily format it any way you want. Since we will be using Text boxes and drawing shapes to show numbers on the dashboard tiles, we will not be able to format them using number format options. Hence we will use TEXT formula to turn a simple number 420500 to $420,500.

    =TEXT(C11, "$#,##")

Here are a few TEXT formula examples you can use:

|     |     |     |     |
| --- | --- | --- | --- |
| **Format you want** | **Input** | **TEXT formula** | **Output** |
| Currency format | 420500 | \=TEXT(A1, “$#,##”) | $420,500 |
| Currency with cents | 420500.75 | \=TEXT(A1, “$#,##.00”) | $420,500.75 |
| Percentages | 0.7453 | \=TEXT(A1,”0%”) | 75% |
| Percentage with 2 decimal points | 0.7453 | \=TEXT(A1,”0.00%”) | 74.53% |

**[Learn more about TEXT formula and format options](https://chandoo.org/wp/a-technique-to-quickly-develop-custom-number-formats/)
**.

### 3\. Create a tile using drawing shapes in Insert ribbon

![](https://chandoo.org/wp/wp-content/uploads/2019/03/insert-tile-with-drawing-shape.png)

Time to let your creative juices flow. Head over to insert ribbon and add a drawing shape (or even an image) to create a tile. Here are few examples if you need inspiration.

![blank dashboard tiles...](https://chandoo.org/wp/wp-content/uploads/2019/03/blank-dashboard-tiles.png)

### 4\. Title the tile tastefully

Now that we have a living breathing tile, name it. Just right click on it and “Edit text” to add a tile. Format it to suit rest of your dashboard theme / fonts. Make sure your title is aligned at bottom or top, as we want rest of the space for actual number. This is how your tile should look at the end.

![excel dashboard tiles after adding titles](https://chandoo.org/wp/wp-content/uploads/2019/03/excel-dashboard-tiles-blank.png)

### 5\. Create a text box and link TEXT() output cell to it

Use Insert ribbon and add a text box. Now select the text box and click on formula bar and point to the cell that contains the tile value. See this quick screencast to understand how to do it.

![](https://chandoo.org/wp/wp-content/uploads/2019/03/text-box-linked-to-cell.gif)

### 6\. Format text box

This is the secret part. You can format linked text boxes! So select it and use format options (fonts, sizes, shadows etc.) to format it.

![formatted text for excel dashboard tile](https://chandoo.org/wp/wp-content/uploads/2019/03/text-box-for-tile-after-formatting.png)

### 7\. Overlay text box on top of tile

![example-excel-dashboard-tiles](https://chandoo.org/wp/wp-content/uploads/2019/03/example-excel-dashboard-tiles.png)

Time to flex your finger muscles. We are in for some serious mouse action here. Just drag and drop the text box on top of dashboard tile. Voila, your Excel dashboard tile is ready. If your calculations change, the tile does too. And it looks sleek. How cool is that.

Few more dashboard tile examples
--------------------------------

*   ![](https://chandoo.org/wp/wp-content/uploads/2019/03/dashboard-tiles-explained.png)
    

You can use anything on these tiles. [Sparklines](https://chandoo.org/wp/excel-sparklines-tutorial/)
, tiny charts, [conditionally formatting](https://chandoo.org/wp/conditional-formatting-top-tips/)
, [picture links](https://chandoo.org/wp/how-to-use-picture-links/)
, photos (really) or more numbers. Just use your creativity and Excel trickery to make these tiles shine. Here are few more examples.

Download Excel Dashboard Tiles – Example workbook
-------------------------------------------------

**[Click here to download Excel dashboard tiles workbook](https://chandoo.org/wp/wp-content/uploads/2019/03/dashboard-tiles.xlsx)
**. It has all these tiles, necessary calculations and charts. See the “Making of a tile – steps” to see all the steps for creating such tiles in your workbooks.

Want to make Awesome dashboards? Join Excel School program
----------------------------------------------------------

If you work in data analysis or reporting roles, dashboard skills are vital for success. This is why I created Excel School program. This in-depth, video-tutorial based course will teach you all the skills needed to create world-class dashboards, like this in just hours.

### Example dashboard from Excel School Program

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/sales-performance-dashboard-demo.gif)](https://chandoo.org/wp/excel-school-program/)

Sales Performance Dashboard

**[Click here to know more and join Excel School program](https://chandoo.org/wp/excel-school-program/)
.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/create-impressive-dashboard-tiles-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/create-impressive-dashboard-tiles-in-excel/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [text()](https://chandoo.org/wp/tag/text/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

[PrevPreviousPower BI Webinar, Amsterdam & Australia tours \[update time\]](https://chandoo.org/wp/power-bi-webinar-and-updates-march-2019/)

[NextTop 10 Excel Formulas for any situationNext](https://chandoo.org/wp/top-10-formulas-for-any-situation/)

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
    
    [Reply](https://chandoo.org/wp/create-impressive-dashboard-tiles-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/create-impressive-dashboard-tiles-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/create-impressive-dashboard-tiles-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# How to make an Interactive Chart Slider Thingy » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/interactive-chart-slider-thingy

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

How to make an Interactive Chart Slider Thingy
==============================================

*   Last updated on June 3, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Ok, I will be honest. I have no idea what to call it. May be _Chart Cover Flow?_ But **Interactive Chart Slider Thingy** sounds so better. So let’s go with it. Here it is:

![Interactive Chart Slider thingy - Dynamic Chart in Excel](https://chandoo.org/wp/wp-content/uploads/2020/06/interactive-chart-slider-thingy-demo.gif)

In this article, let me explain the process for creating such an interactive Excel chart display.

What you need?
--------------

You need a few charts, some time and understanding of simple Excel formulas.

Got them all? Let’s roll.

Video – Interactive Excel Chart Slider
--------------------------------------

Although the instructions for this are _not technical_, You will benefit from watching this video before reading further.

Step by step tutorial – Interactive Chart Slider Thingy
-------------------------------------------------------

**Step 1: Position your charts in a range, one chart per cell**

![charts named range](https://chandoo.org/wp/wp-content/uploads/2020/06/charts-in-a-range-of-cells.png)

Select a range of cells and resize them so that each cell can accommodate one chart. Place charts neatly, one per cell. Name this range as **_charts_**_._ Something like this:

_Note:_ While this example shows how to do the ICST (Interactive Chart Slider Thingy, keep up) with 7 charts, you can apply this idea to any number of charts.

**Step 2: Set up scrollbar form control**

Exactly what it says on the box. Using Developer Ribbon > Insert, add a scorllbar form control to your worksheet.

Right click on the control to set its limits from 1 to 7 and link it to a cell.

**Tip:** If you can’t tell your developer ribbon from oven mitten, check out this excellent guide on [Excel form controls](https://chandoo.org/wp/form-controls/)
.

**Step 3: Calculate neighbors**

For our ICST to work, we need to show selected chart in the middle and the neighbors to left & right. We can calculate the neighbor numbers from a given chart number _**n**_ using simple formulas. I am leaving it to your imagination.

If you need some help, here is a demo of how the neighbor numbers:

![calculations for chart neighbors - interactive chart slider](https://chandoo.org/wp/wp-content/uploads/2020/06/demo-of-chart-neighbor-calculations.gif)

**Step 4: Create 7 named ranges, one per chart cell**

Now that we have neighbor numbers and **charts** range (from step 1), we can create 7 named ranges, one per chart.

1.  **mid.chart:** _refers to the chart that goes in the middle. Use =INDEX(charts, linked\_cell\_for\_scrollbar)_
2.  **left1, left2, left3**: are the the neighbors to left. Just use =INDEX(charts, neighbor\_number) pattern.
3.  **right1, right2, right3:** same as left

**Step 5: Time for some linked pictures**

![Linked picture in Excel](https://chandoo.org/wp/wp-content/uploads/2020/06/linked-picture-option.png)

What is that you are saying?  
_Are we there yet?_  
Yes, we are sweetie. Almost there.

Go back to your charts range and pick any cell. Copy it.

Go to the place where you want your final visual. Right click and select Paste Special > Linked Picture.

Tip: **[Here is a quick tutorial on Linked Pictures](https://chandoo.org/wp/how-to-use-picture-links/)
**.

**_After you pasted any cell as linked picture,_**

*   Select the picture.
*   Go to formula bar and type =mid.chart _the name of the selected chart_
*   Copy this picture and paste again
*   Change reference to =left1
*   Continue 5 more times and use the names left2, left3, right1, right2, right3

Now, we have 7 pictures, one per each chart. They are all linked to the scrollbar, so if you slide it, you will see the images change.

**Step 6: Format the picture links**

This is the final step. We just need to format the picture links to mimic album coverflow look. The key steps are,

*   Shadow effect to make the chart look floating
*   Reflection effect
*   3D rotation for non-active charts
*   **Send to back** to move the non-active charts behind

See this illustration to understand typical settings for one of the picture links.

![How to format a picture link](https://chandoo.org/wp/wp-content/uploads/2020/06/formatting-picture-link-for-interactive-chart-slider-thingie.png)

That is all. Your **interactive chart slider thingy** is ready now.

![Interactive Chart Slider thingy - Dynamic Chart in Excel](https://chandoo.org/wp/wp-content/uploads/2020/06/interactive-chart-slider-thingy-demo.gif)

Download Interactive Chart Slider
---------------------------------

**[Click here to download Excel file](https://chandoo.org/wp/wp-content/uploads/2020/06/interactive-sliding-chart-1.xlsx)
** with full interactive chart slider example. Play with it to learn more. Customize the file or copy the ideas to your work.

If you end up creating something cool or funny, please share it in the comments so we all can learn.

More wacky and fun Excel charts
-------------------------------

If you want to spice up your Excel chart life, you’ve come to the right place. Dim the lights, turn on soothing jazz and enjoy these goodies.

**[Grammy Bump Chart](https://chandoo.org/wp/the-grammy-bump-chart-in-excel/)
**

[![Excel - Grammy bump chart](https://chandoo.org/wp/wp-content/uploads/2020/06/grammy-bump-chart-replication-in-excel-demo.gif)](https://chandoo.org/wp/the-grammy-bump-chart-in-excel/)

Explores the bump in album sales after winning prestigious Grammy award.

**[Flu trends chart](https://chandoo.org/wp/flu-trends-chart-in-excel/)
**

[![](https://chandoo.org/wp/wp-content/uploads/2020/06/flu-trends-chart-demo.gif)](https://chandoo.org/wp/flu-trends-chart-in-excel/)

Visually explore and compare flu trends between years & states. Inspired from Google flu trends.

**[Tour de France – Distance vs. Pace](https://chandoo.org/wp/tour-de-france-radial-chart/)
**

[![tour de france radial chart in excel](https://chandoo.org/wp/wp-content/uploads/2019/07/tdf-radial-chart-1.png)](https://chandoo.org/wp/tour-de-france-radial-chart/)

A radial chart to show distance vs. pace in Tour de France.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/interactive-chart-slider-thingy/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interactive-chart-slider-thingy/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [picture link](https://chandoo.org/wp/tag/picture-link/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    

[PrevPreviousHow to export YouTube video comments to Excel file? – Free template + Power Query case study](https://chandoo.org/wp/export-youtube-comments-template/)

[NextHow to make a variance chart in Power BI? \[Easy & Clean\]Next](https://chandoo.org/wp/variance-chart-powerbi/)

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
    
    [Reply](https://chandoo.org/wp/interactive-chart-slider-thingy/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interactive-chart-slider-thingy/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interactive-chart-slider-thingy/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
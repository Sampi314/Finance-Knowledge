# 6 Best charts to show % progress against goal » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/best-charts-to-show-progress

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

6 Best charts to show % progress against goal
=============================================

*   Last updated on May 8, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Back when I was working as a project lead, everyday my project manager would ask me the same question.

_**“Chandoo, whats the progress?”**_

He was so punctual about it, even on days when our coffee machine wasn’t working.

As you can see, _**tracking progress**_ is an obsession we all have. At this very moment, if you pay close attention, you can hear mouse clicks of thousands of analysts and managers all over the world making project progress charts.

![Best charts to show % done against goal - Excel charts](https://img.chandoo.org/c/best-charts-to-show-%25done-against-goal.png)

**So today, lets talk about best charts to show % progress against a goal.**

[**Please download example file**](https://img.chandoo.org/c/best-charts-for-goal-progress-comparison.xlsx)
 and keep it handy while reading the rest of this tutorial.

### Data for these charts

For all these charts, we will use below data:

![Data for best charts to show %done against goal values - Excel charts](https://img.chandoo.org/c/data-for-best-charts-to-show-%25done-against-goal.png)

### Chart #1: Conditional Formatting Icons + % values

![Traffic light icon-sets chart - show % done against goal](https://img.chandoo.org/c/traffic-light-icons-chart-to-show-%25done-against-goal.png)

This is my all time favorite. It is very easy to implement and works really well.

All you have to do is,

1.  Select the % completion data
2.  Go to Home > Conditional Formatting > Icon sets
3.  Select 3 traffic lights
4.  Edit the rule as shown below:  
    
    ![Conditional formatting rules traffic light icon set](https://img.chandoo.org/c/traffic-light-rule-settings-v1.png)
    
5.  Done!

**Why you should use this?**

*   Very easy to set up.
*   Scalable. Works the same when you have 20 or 200 or 2000 items to track.
*   Looks great

![Keep in mind that traffic light icons do not work well when printed or shown to color-blind people](https://img.chandoo.org/c/traffic-light-icons-in-grayscale.png)

**Keep in mind:**

*   The traffic lights in Excel are not great for color-blind people.
*   The traffic lights do not look good when printed in black-and-white (or gray scale)

Related: [Never show simple numbers in your dashboards](https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards/)

### Chart #2: Conditional Formatting Data Bars

![Databars conditional formatting chart - show % done against goal](https://img.chandoo.org/c/databars-chart-to-show-%25done-against-goal.png)

Another easy and quick answer.

1.  Select % completion data
2.  Go to Home > Conditional Formatting > Data bars
3.  _Select Solid Fill if available_.
4.  Done!
5.  Extra step: Adjust maximum bar size to 100% so that you can see relative progress better.

![Conditional formatting rules for databar](https://img.chandoo.org/c/databar-rule-settings-v1.png)

**Why you should use this?**

*   Very easy to set up.
*   Scalable. Works the same when you have 20 or 200 or 2000 items to track.

**Keep in mind:**

*   By default the maximum value in your data takes 100% of the cell width. So make sure you set this to 100% for better depiction of progress.

### Chart #3: In-cell bar charts

![Using REPT formula and in-cell chart - show % done against goal](https://img.chandoo.org/c/incell-chart-to-show-%25done-against-goal.png)

If for some reason you cannot use databars, then rely on [in-cell bar charts](https://chandoo.org/wp/excel-incell-chart-font/)
. These are simple to setup and works great in many situations where conditional formatting may not be an option.

1.  Assuming your % data is in A1,
2.  In adjacent cell (B1),  write = REPT(“|”, A1\*100)
3.  You will get a lot of pipe symbols | in this cell.
4.  Select the cell and change font to **Playbill**
5.  Adjust font size and color if needed.
6.  Done!

**Why you should use this?**

*   Very easy to set up.
*   Scalable. Works the same when you have 20 or 200 or 2000 items to track.
*   Can be handy when making dashboards or reports (where conditional formatting may have limitations)

**Keep in mind:**

*   The font & size has impact on how in-cell chart is displayed. Use either Playbill or Script fonts.

### Chart #4: Pies

![Conditional formatting pie chart icons chart - show % done against goal](https://img.chandoo.org/c/pie-chart-iconset-to-show-%25done-against-goal.png)

Conditional formatting pie charts are a simple alternative to show % progress data.

The process is same as traffic light icons. Make sure you adjust pie icon settings as per your taste.

**Why you should use this?**

*   Very easy to set up.
*   Scalable. Works the same when you have 20 or 200 or 2000 items to track.

**Keep in mind:**

*   Pie chart icons have only 5 stops. So they are not really pies.  
    
    ![Pie chart iconset settings - conditional formatting](https://img.chandoo.org/c/pie-chart-rule-settings-v1.png)
    
*   Not everyone likes pie charts. Make sure your boss / customers dig them.

### Chart #5: Color scales or heat maps

![Color scale or heatmaps to  chart - show % done against goal](https://img.chandoo.org/c/colorscale-or-heatmap-chart-to-show-%25done-against-goal.png)

When you have a lot of items to track, your focus is really on which items are lagging (or leading). In such cases, a color scale (also known as heatmap) can work very well. It colors cells based on their value. _For example, the darker a cell color is, the more that particular project is done_ and _vice-versa_.

**Why you should use this?**

*   Very easy to set up.
*   Scalable. Works the same when you have 20 or 200 or 2000 items to track.

**Keep in mind:**

*   Make sure the color starting & end points are well contrasted. Else the color scale looks bland.
*   By default color scales show the values too. To hide them use ;;; custom cell formatting code ([how to](https://chandoo.org/wp/hide-cell/)
    ).

### Chart #6: Thermometer charts

![Thermometer chart - show % done against goal](https://img.chandoo.org/c/thermometer-chart-to-show-%25done-against-goal.png)

This is my favorite technique. It works very well for data like this.

[Tutorial on how to create thermometer charts](https://chandoo.org/wp/quick-thermometer-chart/)
.

**Why you should use this?**

*   Easy to understand
*   Scalable. Works the same when you have 20 or 200 or 2000 items to track.

**Keep in mind:**

*   If any value is more than 100% the chart may not explain it properly.
*   Make sure the axis min & max are set to 0 and 1 respectively.
*   You need a dummy column with 100% in it to show outline of thermometer.

### Download Examples

[**Click here to download example workbook**](https://img.chandoo.org/c/best-charts-for-goal-progress-comparison.xlsx)
. It contains all these charts.

**Special bonus for you:**

As a bonus, the download workbook also has 5 step tracker to make you awesome in Excel. Go ahead and download now.

### What is your favorite chart to show % progress?

My most favorite chart is thermometer. The next is traffic light icon-set.

**What about you?** Which of these 6 is your favorite? Please share your chart in the chart. If you use something else altogether, please tell me. I am eager to learn from you.

### More on comparison charts

[![Budget vs. Actual Chart](https://chandoo.org/wp/wp-content/uploads/2018/05/budget-vs-actual-chart-free-template.png)](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)

Budget vs. Actual Chart

Just like my project manager, I am sure your manager too loves tracking & comparison. If so, please go thru below articles to learn few more tricks to impress her.

*   [Us vs. Them – compare one value with many using interactive chart](https://chandoo.org/wp/comparison-charts-1/)
    
*   [Best charts to compare budget with actual values](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [Indicating lower & upper bounds on a chart](https://chandoo.org/wp/bar-chart-with-lower-upper-bounds-tutorial/)
    
*   [Customer service dashboard – a case study in comparison](https://chandoo.org/wp/design-customer-service-dashboard/)
    
*   [Exploring Flu trends in excel chart – a case study in heat maps for comparison](https://chandoo.org/wp/flu-trends-chart-in-excel/)
    

Now if you excuse me, I have to report to my new project manager: my wife. She is asking me about the progress of taking down Christmas lights. _And I am still at 9%._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [46 Comments](https://chandoo.org/wp/best-charts-to-show-progress/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/best-charts-to-show-progress/#respond)
    
*   Tagged under [budget vs. actual](https://chandoo.org/wp/tag/budget-vs-actual/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [charting principles](https://chandoo.org/wp/tag/charting-principles/)
    , [comparison charts](https://chandoo.org/wp/tag/comparison-charts/)
    , [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [data bars](https://chandoo.org/wp/tag/data-bars/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [heatmaps](https://chandoo.org/wp/tag/heatmaps/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [pie charts](https://chandoo.org/wp/tag/pie-charts/)
    , [rept](https://chandoo.org/wp/tag/rept/)
    , [thermometer charts](https://chandoo.org/wp/tag/thermometer-charts/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousEasy Website Metrics Dashboard with Excel](https://chandoo.org/wp/website-dashboard-template/)

[NextHow to show positive / negative colors in area charts? \[Quick tip\]Next](https://chandoo.org/wp/positive-negative-colors-in-area-chart/)

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
    
    [Reply](https://chandoo.org/wp/best-charts-to-show-progress/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/best-charts-to-show-progress/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/best-charts-to-show-progress/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
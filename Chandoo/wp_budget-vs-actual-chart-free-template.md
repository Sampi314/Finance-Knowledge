# Free Budget vs. Actual chart Excel Template - Download

**Source:** https://chandoo.org/wp/budget-vs-actual-chart-free-template

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Beautiful Budget vs. Actual chart to make your boss love you
============================================================

*   Last updated on June 10, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Call them by any name – Budget vs. Actual,**_ Target vs. Actual, Goal vs. Progress, KPIs, Performance charts, but they are the bread and butter of business charting. So how about a drop dead gorgeous and insightful chart for your next meeting with the folks upstairs? **Something like this:**

![](https://chandoo.org/wp/wp-content/uploads/2018/05/budget-vs-actual-chart-free-template.png)

Create Budget vs Actual chart with smart labels in Excel – Tutorial
-------------------------------------------------------------------

If you are in a hurry to make such a chart, [download the template](https://chandoo.org/wp/wp-content/uploads/2018/05/budget-v-actual-chart.xlsx)
, plug in your values and you are good to go. For instructions on how to create them in Excel, read along.

### Step 1: Getting the data

Set up your data. Let’s say you have budgets and actual values for a bunch of categories (products, months, departments etc.) in this format. Calculate variance and variance % using simple formulas as shown below.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/raw-data-for-chart.png)

### Step 2: Create a column chart

Simply select your category, budget and actual columns and insert a column chart (clustered). You will get this.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/chat-step-1-just-budget-and-actual-values.png)

### Step 3: Add Budget and Actual data again to the chart

It feels wrong, but trust me on this one. Add budget and actual values to the chart again. We now end up with a cluster of 4 columns per category, as shown below.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/chart-step-2-with-budget-actual-values-duplicated.png)

### Step 4: Change the newly added columns to lines

Right click on either of the newly added columns, choose “Change series chart type” and convert both of them to lines.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/change-series-chart-type.png)

This step looks different in older versions of Excel, where you have to do it for each column. In Excel 2013 or above, you will go to “Combination chart” screen and you can adjust the series types for all series from there.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/changing-columns-to-lines.png)

### Step 5: Add up / down bars to these lines

Select either of the lines and use the + icon to insert up/down bars. In earlier versions of Excel, you need to use either Insert ribbon or menu to do the same.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/adding-up-down-bars.png)

### Step 6: Format up down bars and columns

Quickly adjust the colors of each bar (don’t touch the lines yet) as you see fit.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/after-formatting-up-down-bars.png)

### Step 7: Adjust gap width and series overlap

This is the tricky bit. Use below instructions.

*   Select the columns first. Go to format series (Ctrl+1)
*   Adjust series overlap to 0%
*   Set gap width to 150%
*   Now select the lines
*   Adjust the gap width to 300%
*   Feel free to adjust / experiment with various gap width combinations to see which works best for your eyes.

Your result should look like this:

![](https://chandoo.org/wp/wp-content/uploads/2018/05/after-adjusting-gap-width.png)

### Step 8: Make the lines invisible

Select the lines (one at time) and yell gently _**reducto**_

![](https://chandoo.org/wp/wp-content/uploads/2018/05/no-outline-for-making-lines-invisible.png)

If you are muggle, simply set the outline color to **no line** and you are gold. We get this:

![](https://chandoo.org/wp/wp-content/uploads/2018/05/after-making-lines-invisible.png)

### Step 9: Add a title to your chart and remove unnecessary legend items

Double click on the chart title and type something meaningful. Alternatively, you can also link it to a cell value. To do that, select the title, press = and point to a cell that has the title you want to use.

To remove legend entries, click on the chart legend, now click again on the series 3, hit DEL key. Repeat the process for series 4.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/after-adding-chart-title.png)

### Step 10: Add data labels to both lines

Select the lines one at a time (remember, the lines are invisible, so just click where they are supposed to be or use the format box to select them). Now use the + button to add data labels. In older versions of Excel, you need to use either ribbon or menus to add labels. At this stage, your chart should look like this:

![](https://chandoo.org/wp/wp-content/uploads/2018/05/after-adding-default-labels.png)

### Step 11: Calculate new labels

This is the fun part. Start by setting up rules for what symbol+value you want to show. For example, you may want to show,

*   Thumbs down if the variance is below -5%
*   fingers crossed if the variance is between -5% and 0%
*   OK symbol if variance is positive and less 10%
*   Thumbs up if it is between 10% and 25%
*   Double thumbs up if it is more than 25%

Create a range where your symbol % mapping will go and fill up the symbols using Insert > Symbol option. Select Segoe UI Emoji font to insert cool emojis.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/insert-emojis-excel.png)

Your mapping table should look like this:

![](https://chandoo.org/wp/wp-content/uploads/2018/05/label-symbol-emoji-mapping.png)

_Note the first value. It means we will display thumbs down for all values between -5% and -100%._

Now, let’s calculate the labels. There are two sets of labels. Positive and Negative. This gives you finer control on formatting them. Our raw data area now looks like this:

![](https://chandoo.org/wp/wp-content/uploads/2018/05/raw-data-with-labels-added.png)

Formulas for labels:

*   **Symbol:** \=VLOOKUP(var%, mapping-table, 2) _We are using the approximate lookup technique to get relevant symbol._
*   **Var 1:** \=IF(var%<0, Symbol & TEXT(ABS(var%), “0%”),””)
*   **Var 2:** =IF(var%>=0, Symbol & TEXT(ABS(var%), “0%”),””)

Replace the words var%, mapping-table, Symbol with actual cell references in your workbook.

### Step 12: Plug our smart labels in to the chart

![](https://chandoo.org/wp/wp-content/uploads/2018/05/add-labels-with-values-from-cells.png)Now that we have gorgeous labels, let’s replace the old ones with these.

*   Select first line (budget)’s labels and press CTRL+1 to go to format options.
*   Click on “Value from cells” option and point to Var 1 column.
*   Repeat the process for second line (actual) labels too.

We get this.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/after-changing-labels-to-calculated-values.png)

### Step 13: Adjust label position

We are almost there. Click on the labels and choose position as “Above”.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/label-position-settings.png)

Our kick ass budget vs. actual chart is ready.

![](https://chandoo.org/wp/wp-content/uploads/2018/05/budget-vs-actual-chart-free-template.png)

Download FREE Budget vs. Actual Chart Template
----------------------------------------------

[**Click here to download the chart template**](https://chandoo.org/wp/wp-content/uploads/2018/05/budget-v-actual-chart.xlsx)
. Just type in your data and see the chart. If you want to learn how to make the chart, there are instructions in the workbook too. Scroll down to see them. Have a play and use it in your work to be a hero in front of your boss.

**More such charts for you:**

If you liked that chart, check out these additional resources for more inspiration and wow factor.

*   [Rider on a hill – Dynamic target tracking chart](https://chandoo.org/wp/2016/09/20/biker-on-hill-chart/)
    
*   [6 charts to compare % progress](https://chandoo.org/wp/2014/03/10/best-charts-to-show-progress/)
    
*   [Thermometer chart with last year markers](https://chandoo.org/wp/2012/06/11/thermo-meter-chart-with-last-year-marker/)
    
*   [Gauge chart in Excel](https://chandoo.org/wp/2008/09/09/excel-speedometer-chart-download/)
    
*   [14 charts for budget vs. actual](https://chandoo.org/wp/2009/04/05/budget-vs-actual-charts/)
    

### How do you make your budget vs. actual charts?

For simple data, I use either [databars](https://chandoo.org/wp/2014/03/10/best-charts-to-show-progress/)
 or [thermometer charts](https://chandoo.org/wp/2012/06/11/thermo-meter-chart-with-last-year-marker/)
. For something fancy, I use technique described in this post. It never ceases to amaze my audience.

**What about you?** What charts do you use to make budget vs. actual charts? Please share your thoughts in comments.

### Problem re-creating this chart in Excel?

If you face difficulty making budget vs actual chart in Excel, check:

*   You have Emoji font installed. Windows should have added this by default long ago. The font name is Segoe UI Emoji.
*   Labels are set to Segoe UI Emoji font. In some versions of Excel, emojis are available only on few fonts. If you see funny symbols or boxes with ? inside them, select labels and set the font to Segoe UI Emoji.
*   Any other problem… post a comment so one of our readers or I can help you.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [31 Comments](https://chandoo.org/wp/budget-vs-actual-chart-free-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/budget-vs-actual-chart-free-template/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [budget vs. actual](https://chandoo.org/wp/tag/budget-vs-actual/)
    , [column chart](https://chandoo.org/wp/tag/column-chart/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [emojis in excel](https://chandoo.org/wp/tag/emojis-in-excel/)
    , [text()](https://chandoo.org/wp/tag/text/)
    , [up down bars](https://chandoo.org/wp/tag/up-down-bars/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPrevious60 sports in six charts](https://chandoo.org/wp/60-sports-in-six-charts/)

[NextDistinct count in Excel pivot tablesNext](https://chandoo.org/wp/distinct-count-pivot-tables/)

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
    
    [Reply](https://chandoo.org/wp/budget-vs-actual-chart-free-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/budget-vs-actual-chart-free-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/budget-vs-actual-chart-free-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
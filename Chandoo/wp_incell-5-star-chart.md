# In-cell 5 star chart - tutorial & template » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/incell-5-star-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

In-cell 5 star chart – tutorial & template
==========================================

*   Last updated on August 14, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Whenever we talk about product ratings & customer satisfaction, 5 star ratings come to our mind. Today, let’s learn **how to create a simple & elegant 5 star in-cell chart in Excel.** _**Something like this:**_

![5 star in-cell chart in excel](https://img.chandoo.org/cf/5-star-rating-chart-completed.png)

A while ago, Hui showed us a fun way to create **[5 star charts in Excel using bar charts with 5 star mask](http://chandoo.org/wp/2011/04/13/how-to-make-a-5-star-chart/)
**. I highly recommend reading that article if you want to create a regular chart version of this.

Tutorial for creating a 5 star chart
------------------------------------

### 1\. Meet the data

Here is our data. Very simple. First column has product names. Second column has customer rating – from 1 to 5.

![Data for 5 star chart in Excel](https://img.chandoo.org/cf/5star-rating-excel-chart-data.png)

### 2\. Set up 5 blank columns for the 5 star chart

Let’s create a 5 column grid right next to our data set. This is where the in-cell 5 star chart will go. At this stage our 5 star chart looks like this:

![Add 5 column grid to create in-cell 5 star chart](https://img.chandoo.org/cf/add-5-column-grid-5star-rating-chart-excel.png)

If you haven’t guessed yet, we will be using conditional formatting > star icons to get the 5 star chart.

![Conditional formatting star rating icons](https://img.chandoo.org/cf/conditional-formatting-star-rating.png)

### 3\. Write formulas in the 5 column grid

Now, we need to write formulas to fill up the 5 column grid. We need to formulas to return either 1, 0 or decimal values in the grid depending on the rating for that row.

So, for example, if a product has 3.30 rating, we want to print 1, 1, 1, 0.30 and 0 in 5 columns.

You can use any number of formulas to get this result. The simplest one will be IF formula.

Assuming column C (from C7) has product ratings & row 5 has running numbers 1 to 5 (from cell D5), we can use below formula to get what we want:

\=IF(D$5<=$C7,1,IF(ROUNDUP($C7,0)=D$5,MOD($C7,1),0))

To understand the above formula , see this illustration.

![5 star chart calculations - explained](https://img.chandoo.org/cf/excel-calculations-for-5star-chart-explained.png)

_If you like to avoid IF formulas, here is an alternative:_

\=MAX(($C7>=D$5)\*1,MOD($C7,1))\*(ROUNDUP($C7,0)>=D$5)

_**A challenge for you:** Can you think of any other ways to write this formula?_

### 4\. Apply conditional formatting to the 5 column grid

Select the 5 column grid and apply conditional formatting (Home > Conditional Formatting > New rule)

Set up the rule as shown below:

![Applying conditional formatting rules for 5 star chart](https://img.chandoo.org/cf/conditional-formatting-rules-for-5star-chart.png)

At this stage, our report looks like this:

![5 star in-cell chart in excel - almost done](https://img.chandoo.org/cf/5-star-rating-chart-almost-done.png)

### 5\. Adjust column width and borders

Once the formatting is applied, just clean up the report by adjusting column width (set it to 24 px) and add horizontal borders only.

And our product rating report is ready.

![5 star in-cell chart in excel](https://img.chandoo.org/cf/5-star-rating-chart-completed.png)

Download in-cell 5 star chart template
--------------------------------------

[**Please click here to download the in-cell 5 star chart workbook**](https://img.chandoo.org/cf/5-star-chart.xlsx)
. It also contains a variation of the 5 star chart made with data bars & 5 star mask. Check out both examples to understand how they work.

More in-cell chart tutorials & techniques
-----------------------------------------

In-cell charts are a powerful & lightweight way to visualize your data. Check out below tutorials to one up your awesomeness.

*   [![In-cell funnel charts in Excel](https://img.chandoo.org/c/sales-funnel-chart-incell.png)](http://chandoo.org/wp/2011/09/29/incell-sales-funnel-charts/)
    [Create in-cell charts with markers for target / average](http://chandoo.org/wp/2014/12/03/in-cell-charts-with-markers/)
    
*   [In-cell sales funnel charts](http://chandoo.org/wp/2011/09/29/incell-sales-funnel-charts/)
    
*   [Suicides vs. Murders – story told with in-cell charts](http://chandoo.org/wp/2011/09/09/suicides-murders-interactive-chart/)
    
*   [Another 5 star chart (plus show details on click)](http://chandoo.org/wp/2011/04/07/show-details-on-demand-in-excel/)
    
*   [Exploring survey results in interactive dot-plot chart](http://chandoo.org/wp/2010/04/09/dot-plot-panel-chart/)
    

How would you visualize customer ratings in Excel?
--------------------------------------------------

While 5 star charts are traditional, they dumb-down the data. _**Can you think of other fun ways to visualize customer / product rating data?**_ Please share your thoughts & implementations in the comments.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/incell-5-star-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/incell-5-star-chart/#respond)
    
*   Tagged under [5 Star Chart](https://chandoo.org/wp/tag/5-star-chart/)
    , [awesome august](https://chandoo.org/wp/tag/awesome-august/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [if()](https://chandoo.org/wp/tag/if/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [roundup](https://chandoo.org/wp/tag/roundup/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousWork with charts faster using selection pane & select object tools \[quick video tip\]](https://chandoo.org/wp/using-selection-pane-select-object-tools/)

[NextA simple trick to make your dashboards user friendly Next](https://chandoo.org/wp/dashboard-form-controls-trick/)

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
    
    [Reply](https://chandoo.org/wp/incell-5-star-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/incell-5-star-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/incell-5-star-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
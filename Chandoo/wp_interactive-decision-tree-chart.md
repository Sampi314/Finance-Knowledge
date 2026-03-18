# Interactive Decision Tree Visualization in Excel [Trump vs. Hillary in Swing States] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/interactive-decision-tree-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Interactive Decision Tree Visualization in Excel \[Trump vs. Hillary in Swing States\]
======================================================================================

*   Last updated on October 11, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

It is election time in USA, and that means there is a whole lot of drama, discussions and of course data analysis. There are tons of cool visualizations published on all the data. Previously, we talked about [_“How Trump happened” chart_](http://chandoo.org/wp/2016/03/02/how-trump-happened-in-excel/)
.

Today let’s take a look at the **[beautiful decision tree chart by NY Times](http://www.nytimes.com/interactive/2016/upshot/clinton-trump-paths-to-win-election.html?smid=pl-share&_r=0)
** explaining what would happen if each of the 10 swing states vote for Democrats or Republicans. Go ahead and look at that chart. And when you are done playing with it, come back.

![decision-tree-trump-hillary-nytimes](https://chandoo.org/wp/wp-content/uploads/2016/10/decision-tree-trump-hillary-nytimes.png)

My first thought after looking at the chart is: _Wow, that is cool. I wonder how we can recreate that experience in Excel?_

But as you can guess, making a dynamic tree visualization in Excel is pretty hard. You can create a bubble chart mixed with XY chart to show all the nodes of the decision tree, but as this tree has 2^10 nodes at the bottom level (and 2^11-1 total nodes) our chart would look very clumsy and busy.

So, instead of replicating NY Times chart, **why not make our own version that explains the data?** You can reuse this idea when _**visualizing outcomes of several what-if scenarios**._

### Demo of interactive decision tree chart in Excel

First, take a look at our Trump vs Hillary chart.

![interactive-decision-tree-visualization](https://chandoo.org/wp/wp-content/uploads/2016/10/interactive-decision-tree-visualization.gif)

### How to create a decision tree visualization in Excel – Tutorial

**1\. Arrange decision and outcome data**

In a table (or range) list various decision and outcome combinations. For our case of Trump vs. Hillary in 10 swing states, there will be 2^10 outcomes (1024). Arrange this data in a format like below.

![raw-data-decision-tree](https://chandoo.org/wp/wp-content/uploads/2016/10/raw-data-decision-tree.png)

**2\. Calculate the outcome**

Based on each of the decision combinations, calculate the outcome and add it as a column to your table. Alternatively, you can also type or import the outcome data (along with decision combinations)

**3\. Create a pivot table from your data**

Since we are going to use slicers for user interaction, we need to create a pivot table from all this data.

Add all the decision variables and outcome to row labels area. Rearrange the pivot in _**tabular layout**._ Disable sub-totals and grand totals.

![pivot-table-settings-decision-tree](https://chandoo.org/wp/wp-content/uploads/2016/10/pivot-table-settings-decision-tree.png)

**4\. Add slicers**

Go to Insert > slicer and select all the decision parameters. In our case, we will pick all the 10 state names.

Once all the slicers are inserted, format them.

*   Set up slicer labels in multiple columns
*   Adjust their size
*   Apply a custom style if you prefer.
*   Keep the headers on the slicers for now. We will remove them at a later stage.

_Related: [Comprehensive guide to slicers – what, how, where, when and why](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
_

**5\. Calculate % of outcomes for each candidate**

Now that we have slicers, whenever you make a selection, the pivot table will be filtered. Calculate number of outcomes favoring each candidate and use that to make a stacked bar chart.

![stacked-bar-chart-decision-outcomes](https://chandoo.org/wp/wp-content/uploads/2016/10/stacked-bar-chart-decision-outcomes.png)

**6\. Add bells & whistles**

You can add a few bells and whistles to this pretty slicer controlled stacked bar chart even prettier.

*   Add messages that display %s (or confidence levels etc.) for each outcome.
*   Display the outcome once it is certain (_a la head shot of Hillary or Trump_)

_Related: [Display shapes & images in Excel charts](http://chandoo.org/wp/2015/08/08/shapes-in-charts/)
_

So there you go. Your interactive decision tree visualization is ready.

**Oh, last but not least – resetting all slicers**

This is the only place we need to open the hood of Excel and mess with internal wiring. Just add a simple macro to reset all slicers in the workbook. Then assign this macro to a text box with the text “Reset all” on it.

    
    Sub resetSlicers()
        'Reset all slicers
        
        Dim sC As SlicerCache
        
        For Each sC In ActiveWorkbook.SlicerCaches
            sC.ClearManualFilter
        Next sC
        
    End Sub
    

### Download decision tree visualization workbook

**[Click here to download decision tree visualization example workbook](https://chandoo.org/wp/wp-content/uploads/2016/10/decision-tree.xlsm)
.** Play with the slicers to find outcome of 2016 US election. Copy the ideas to your model / dashboard to showcase outcomes based on user inputs.

_Note: this workbook has VBA. Enable macros to enjoy the reset button._

### How do you visualize decision trees

As I said earlier, making decision trees in Excel is tricky _if not hard._ If you have Power BI, you can use R scripts to make a decision tree. But if you are stuck with Excel, creating a dynamic tree like structure is tricky. That is why, I went with the stacked bar chart approach.

**What about you?** How would you visualize various scenarios and outcomes in Excel? Please share your thoughts and implementations in the comments section.

### Want more? Check out these awesome Excel charts

[![](https://chandoo.org/wp/wp-content/uploads/2016/04/earth-venus-dance-demo-v1.gif)](http://chandoo.org/wp/2016/04/25/earth-venus-cosmic-dance-animated-chart-in-excel/)
Here are few more inspiring Excel charts for you.

*   [Mapping spread of obesity in USA](http://chandoo.org/wp/2016/09/28/mapping-spread-of-obesity/)
    
*   [Earth vs. Venus cosmic dance](http://chandoo.org/wp/2016/04/25/earth-venus-cosmic-dance-animated-chart-in-excel/)
     (pictured aside)
*   [Mapping up & down trends in a time series](http://chandoo.org/wp/2015/07/29/shading-an-area-different-colors-for-up-down-movements/)
    
*   [Narrating story of change](http://chandoo.org/wp/2015/05/18/story-of-change/)
    
*   [Network chart to map relationships between people](http://chandoo.org/wp/2014/08/13/network-relationship-chart/)
    
*   More [advanced charts](http://chandoo.org/wp/tag/advanced-charting/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [5 Comments](https://chandoo.org/wp/interactive-decision-tree-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interactive-decision-tree-chart/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousCurrency format Pivot fields with one click \[Friday VBA\]](https://chandoo.org/wp/currency-format-pivot-fields-with-one-click/)

[NextCP055: “Yes, I am back” edition (and a bonus Excel tip)Next](https://chandoo.org/wp/cp055-yes-i-am-back/)

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
    
    [Reply](https://chandoo.org/wp/interactive-decision-tree-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interactive-decision-tree-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interactive-decision-tree-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
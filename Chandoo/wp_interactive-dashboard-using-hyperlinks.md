# Interactive Dashboard in Excel using Hyperlinks » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/interactive-dashboard-using-hyperlinks

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Interactive Dashboard in Excel using Hyperlinks
===============================================

*   Last updated on August 23, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Last week we learned [how to create dynamic hyperlinks in Excel](http://chandoo.org/wp/2011/07/14/dynamic-hyperlinks-in-excel/ "Create Dynamic Hyperlinks in Excel [Video]")
. Today, I want to show you something even cooler. **An interactive dashboard based on hyperlinks, like this:**

![Interactive Dashboard in Excel - Demo](https://img.chandoo.org/dashboards/interactive-dashboard-in-excel-demo.gif)

_Isn’t it impressive?_

Well, to create something like this, you don’t need a degree in advanced cryogenics. You just need a bunch of data, a chart, a one line macro code and some pixie dust (go easy on pixie dust).

5 Step Tutorial to Create Interactive Dashboard using Hyperlinks
----------------------------------------------------------------

### Step1: Setup your data

It is no wonder that any good chart or dashboard exercise must begin with data setup. So, the first thing we need to do is, to set up our data.  
If you observe carefully, you will realize that we just have one chart and we are changing the chart’s source data based on which option user selected.

So, **assuming you have 4 series of data – sales, expenses, profits & number of customers, _we will add fifth series_**. This will always show data for the series that user selected. Like this,

![Data setup for Interactive Dashboard in Excel](https://img.chandoo.org/dashboards/data-for-dynamic-chart.png)

Lets call the series name in fifth column as “_**valSelOption**_“. Lets assume that we will use some sort of magic to change the series name.

Note: Using this series name, we can fetch the position of the series out of 4 with [MATCH formula](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
. Once you know the position, You can fetch corresponding values [using INDEX() formula](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
.

### Step 2: Create a chart from the series 5

This is very simple. Just create a chart from the data in 5th column as above. You can format this as you want.

### Step 3: Create the dashboard area

This is a bit tricky, but easy too. Just set up 4 column area (since we have 4 charts) such that you can place your chart and mouse-over cells _for selection_. like this,

![Interactive Dashboard Sketch - Marking the areas where user would hover](https://chandoo.org/img/dashboards/interactive-dashboard-sketch.png)

### Step 4: Create Roll-over effect

Now comes the magical part. We need a simple macro or UDF to change the series based on where user pointed the mouse.

_**But how to activate that UDF on mouse rollover?**_

**This is where we can use Hyperlinks.**

Do you know that you can use a UDF as source for hyperlink.  
Just like we can write =HYPERLINK(“http://chandoo.org/”,”Click here”)  
we can also write _\=HYPERLINK(myFunction(),”Click here”)_

And Excel would run your function when user clicks on the link.  
But, there is more to it.  
**Excel would also run the function, when you place your mouse on the link.** _**No need to click!**_

But, seasoned VBA programmers would know that Functions are not allowed to change values in other cells or format them. Well, that restriction does not apply if you use a function from Hyperlink!!!

So, we would write a one line function – highlightSeries(seriesName as Range) and put this code in there.

Public Function highlightSeries(seriesName As Range)  
Range(“valSelOption”) = seriesName.Value  
End Function

This function would take the series name as a variable and assigns it to named range _**valSelOption**_. As the valSelOption changes, so does the data for our chart and then we get new chart.

Now, we just write this hyperlink formula in all the 4 cells, like this:

(Assuming the series names in B3:E3)

`=IFERROR(HYPERLINK(highlightSeries(B3)),"6")`

### Why this formula works?

*   While using a UDF inside HYPERLINK() works the trick, Excel would also throw up a #VALUE! error. To fix it, we use the IFERROR()
*   The number 6 is the down-arrow symbol in webdings font
*   So, _change the cell’s font to webdings_!

Now, drag this formula sideways to fill in all 4 cells.

Note: Word-wrap the hyperlink cells so that the link works when you hover anywhere on the cell, not just the down-arrow symbol.

### Step 5: Add Conditional Formatting to highlight selected series’ name etc.

This is optional, but just as awesome. Once you [add conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
, the dashboard feels slick and interactive.

**That is all. Your interactive dashboard is ready.**

Download the Example Workbook
-----------------------------

[Click here to download the interactive dashboard workbook](https://img.chandoo.org/d/rollover%20hyperlink%20demo.xlsm)
 and play with it. Examine the technique, formulas and UDF code to see how it is weaved together.

Special Thanks to Jordan:
-------------------------

Many thanks to Jordan, who blogged about [this technique on his OptionExplicit VBA blog](http://optionexplicitvba.blogspot.com/2011/04/rollover-b8-ov1.html)
. He reviewed my file and gave me few suggestions too. He made an interactive snake application using this technique. You can [download that file from here](https://files.chandoo.org/free/RollOver2.xlsm)
.

How do you like this technique?
-------------------------------

I like the possibilities of this technique. However, it is also a bit tricky to explain. So I will use it with caution. (Also, I am not sure if this would slow down Excel, but in my experience it did not)

**What about you? Do you like this idea?** Are you going to experiment with it? Please tell me how you are planning to use it thru comments.

More techniques for Dashboard Makers & Analysts
-----------------------------------------------

If you work with Dashboards or data analysis, then you are at the right place. We have a wealth of information, tutorials, examples & ideas for you. Please check out a few below:

*   [Display on demand details in your excel charts](http://chandoo.org/wp/2011/04/07/show-details-on-demand-in-excel/)
    
*   [Cricket World-cup Dashboard in Excel](http://chandoo.org/wp/2011/04/15/cricket-worldcup-dashboard/)
    
*   [New to Dashboards? 33 Resources & Ideas for you](http://chandoo.org/wp/2011/03/25/resources-for-making-dashboards/)
    
*   [**Excel School Dashboards Program** – Learn how to create dashboards using Excel](http://chandoo.org/wp/excel-school/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [205 Comments](https://chandoo.org/wp/interactive-dashboard-using-hyperlinks/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interactive-dashboard-using-hyperlinks/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Dashboard Tutorials](https://chandoo.org/wp/tag/kpi-dashboards-posts/)
    , [hyperlink()](https://chandoo.org/wp/tag/hyperlink/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [udf](https://chandoo.org/wp/tag/udf/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousAccumulated Depreciation using Mixed References](https://chandoo.org/wp/accumulated-depreciation-using-mixed-references/)

[NextWe Want Your Ideas – ResultsNext](https://chandoo.org/wp/we-want-your-ideas-results/)

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
    
    [Reply](https://chandoo.org/wp/interactive-dashboard-using-hyperlinks/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interactive-dashboard-using-hyperlinks/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interactive-dashboard-using-hyperlinks/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
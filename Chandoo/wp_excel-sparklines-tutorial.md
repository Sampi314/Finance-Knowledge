# What are Excel Sparklines & How to use them? - Complete Tutorial & 5 tips

**Source:** https://chandoo.org/wp/excel-sparklines-tutorial

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

What are Excel Sparklines & How to use them? 5 Secret Tips
==========================================================

*   Last updated on April 23, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Of all the charting features in Excel, Sparklines are my absolute favorite.** These bite-sized graphs can fit in a cell and show powerful insights. [Edward Tufte](http://www.edwardtufte.com/)
 coined the term sparkline and defined it as,

> intense, simple, word-sized graphics
> 
> Edward Tufte

![Excel sparklines tutorial and 5 tips](https://chandoo.org/wp/wp-content/uploads/2020/04/excel-sparklines-tutorial.png)

**Sparklines (often called as micro-charts) add rich visualization capability to tabular data without taking too much space.** This page provides a complete tutorial on Excel sparklines along with 5 secret tips.

What is a sparkline?
--------------------

_**A Sparkline is a small chart that is aligned with rows of some tabular data and usually shows trend information.**_

Here is an example of sparklines in a project team status report.

![Example Sparkline Implementation - Project Team Member - Status Report](https://chandoo.org/img/2010/introduction-to-excel-sparklines.png)

Excel Sparklines Tutorial – 3 steps
-----------------------------------

Creating sparklines in Excel is very easy. You follow 3 very simple steps to get beautiful sparklines in an instant.

1.  Select the data from which you want to make a sparkline.
2.  Go to Insert > Sparkline and select the type of sparkline (you have 3 options – line, column and win-loss chart)
3.  Specify a target cell where you want the sparkline to be placed
4.  Optional: Format the sparkline if you want.

Here is a short screen-cast showing you how a sparkline is created.

![How to create sparklines in Excel 2010 - Tutorial](https://chandoo.org/img/2010/howto-make-sparklines-in-excel-2010.gif)

Types of Sparklines in Excel:
-----------------------------

![Types of Sparklines in Excel 2010](https://chandoo.org/img/2010/types-of-sparklines-excel-2010.png)

  
There are 3 basic types of sparklines in Excel 2010. They are,

1.  Line chart
2.  Column chart
3.  Win-loss chart (useful for showing a bunch of wins & losses denoted by 1s and -1s)

Sparkline Formatting and Options – Explored
-------------------------------------------

![Sparkline Formatting Options in Excel 2010](https://chandoo.org/img/2010/sparkline-formatting-options-excel.png)

  
Whenever you select a cell with sparkline in it, you will find a new ribbon called as “Sparklines – Design” ribbon. This is where all the formatting options for sparklines are included. Some of the key formatting / customization options available are,

*   Change the sparkline type – between line, column and win/loss
*   Change the source data / target cells of sparkline
*   Set different colors for first point, last point, highest & lowest points (applicable for column and line chart types)
*   Set axis options (show / hide axis, set min and max value for vertical axis, set axis type to date axis etc.)
*   Group / un-group a bunch of sparklines (you can change formatting options, axis settings en-masse when you group sparklines)
*   Remove sparklines

Sparklines & Missing Data – How does it work?
---------------------------------------------

![Sparklines & Missing Data - Examples](https://chandoo.org/img/2010/sparklines-and-missing-data.png)

*   **Non-numeric data:** If the sparkline source data contains non-numeric data, they are neglected while plotting the sparklines.
*   **Errors & #NA values:** If data has some #NA values, they are neglected
*   **Blanks:** sparkline show blanks as gaps
*   **Zeros:** If data has zeros, zero value is plotted
*   **Data in hidden rows / columns:** If data has some hidden rows / columns, the values are neglected (unless you enable “Show data in hidden cells” option)

Sparklines in Tables & Pivot Tables
-----------------------------------

![Sparklines in Pivot Tables - An Example](https://chandoo.org/img/2010/sparklines-in-pivot-tables.png)

You can add sparklines to [tables](https://chandoo.org/wp/data-tables/)
 and [pivot tables](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
 too. Adding them to pivot tables is a bit tricky but adding sparklines to tables is fairly straightforward and scales nicely.  

5 Tips to use Sparklines better
-------------------------------

Here is a bunch of quick tips & tricks for those of you starting on sparklines.

1.  **You can auto-fill sparklines.** Select the first set of values and add a sparkline. Now copy and past sparklines to auto-fill them based on data in adjacent cells.
2.  **Change their size:** When you adjust row-height or column-width of the cell containing sparkline, the size of sparkline changes too.
3.  **Juxtapose sparklines with conditional formatting icons** to create stunning charts and dashboards.
4.  **If you want to copy a sparkline over to a ppt or document,** you can use “copy as picture” option.
5.  **Enable high / low points** to highlight important values

Sparklines & Compatibility
--------------------------

Sparklines are available since Excel 2010. They work in desktop and web versions of Excel.

What happens when someone opens a file with sparklines in Excel 2007?
---------------------------------------------------------------------

Sparklines don’t show up in if you open the file in older version of Excel (say Excel 2007).

How does Sparklines compare with other alternatives?
----------------------------------------------------

### Sparklines vs. In-cell Charts

[In-cell charts](http://chandoo.org/wp/tag/in-cell-charting)
 are a powerful and lightweight way to create bite-sized visualizations. The main technique is to use REPT formula to repetitively show a bunch of symbols (usually | symbol) to create a small chart. The advantage of this approach is that they work in any version of Excel. But the dis-advantage is that we can make only few types of charts (bar charts, column charts by rotating cell text, dot plots). Also, incell charts require some knowledge of excel formulas and creativity.

This is where Excel Sparklines shine, as they are very easy to create and maintain.

### Sparklines vs. Conditional Formatting

In Excel 2007, MS introduced a bunch of useful [Conditional Formatting](http://chandoo.org/wp/tag/conditional-formatting/)
 options like icons, heat maps that effectively create small visualizations of underlying data. These features are further improved in Excel 2010, 2013 and 2016. While conditional formatting based visualizations are easy to implement and scale very well, there are only few options (a bunch of traffic lights, data bars etc.). This could leave you high and dry if you are looking for rich visualization options. these new features require the actual data to be present in underlying cells (which is a head-ache).

Again, sparklines shine as a simpler and easier alternative.

### Sparklines vs. Shrinking an actual chart

We can take an actual chart, strip it of all the clothing (remove gridlines, axis, legend, titles, labels etc.) and resize it so that it fits nicely in a cell \[[example](https://chandoo.org/wp/excel-sparkline-template/)\
\]. This is the easiest and cleanest way to get sparklines in earlier versions of excel. However this approach has one problem. It doesn’t scale. (ie if you want to get 2 sparklines, you need to do twice the work). Of course, we can write some macros to take care of that, but if you are open to macros, you might as well use SfE and save a lot of trouble. But this approach of shrinking a real chart is better as it gives you full power to customize the underlying chart (add multiple series etc.) which is not available in excel sparklines.

Download Excel Sparklines Tutorial Workbook
-------------------------------------------

**[Click here to download Excel sparklines tutorial workboo](https://chandoo.org/wp/wp-content/uploads/2020/04/sparklines-tutorial-workbook.xlsx)
k**. It shows all three kinds of sparklines in a simple dashboard format. Use the data to create your own sparklines to learn more.

Conclusions on Sparklines
-------------------------

**The sparklines in Excel is certainly a great step forward in the world of data visualization.** It brings ease and consistency to most users who want better visualizations but do not know how to create them. That said, Microsoft hasn’t really introduced any new types of sparklines since 2010. _This is disappointing_. Ideally few more types of sparklines such as these can help with dataviz.

![new types of sparklines I wish Microsoft introduced ](https://chandoo.org/wp/wp-content/uploads/2020/04/new-sparkline-formats-needed.png)

On a lighter note, Kudos to Office Team at MS for not adding any 3D capabilities to these sparklines. That would have unleashed a fresh dose of chart monsters.

**I use sparklines in most of my [dashboards](https://chandoo.org/wp/excel-dashboards/)
 and business reports.**

_**What about you?** What are your thoughts on sparklines? Have you used them? What is your experience like? Please share your ideas, impressions and tips thru comments._

Additional examples on Sparklines:
----------------------------------

![Dynamic Sparklines using Excel](https://chandoo.org/wp/wp-content/uploads/2015/08/dynamic-sparklines-v2.png)

[Dynamic sparklines with just last 30 days data](https://chandoo.org/wp/dynamic-sparklines/)

![regional-trends-analysis-customer-complaints-data](https://chandoo.org/wp/wp-content/uploads/2016/02/regional-trends-analysis-customer-complaints-data.png)

**Sparklines used to analyze regional trends in customer service dashboard – [link](https://chandoo.org/wp/analyzing-customer-complaints-2/)
**

*   [Sparklines vs. SfE Free Add-in – a detailed comparison](http://peltiertech.com/WordPress/sparklines-for-excel-vs-excel-2010-sparklines-guest-post/)
     \[PTS Blog\]
*   [Sparklines for Excel – a fantastic Add-in for generating sparklines in all versions of Excel](http://sparklines-excel.blogspot.com/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [62 Comments](https://chandoo.org/wp/excel-sparklines-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-sparklines-tutorial/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [edward tufte](https://chandoo.org/wp/tag/edward-tufte/)
    , [Excel 2010](https://chandoo.org/wp/tag/excel-2010/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [micro charts](https://chandoo.org/wp/tag/micro-charts/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sparklines](https://chandoo.org/wp/tag/sparklines/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousAdd slope line to XY charts](https://chandoo.org/wp/add-slope-line-to-xy-charts/)

[NextEasy Website Metrics Dashboard with ExcelNext](https://chandoo.org/wp/website-dashboard-template/)

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
    
    [Reply](https://chandoo.org/wp/excel-sparklines-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-sparklines-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-sparklines-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# How to conditionally format visuals in Power BI? » Tutorial » Chandoo.org

**Source:** https://chandoo.org/wp/conditionally-format-visuals-in-power-bi

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    

How to conditionally format visuals in Power BI?
================================================

*   Last updated on July 30, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Do you know that you can apply conditional formatting rules to visuals in Power BI? In this post, let’s learn **how to conditionally format visuals in Power BI.** Something like this:

![How to conditionally format visuals in Power BI](https://chandoo.org/wp/wp-content/uploads/2019/07/howto-conditionally-format-visuals-in-Power-BI.png)

To conditional format charts in Power BI, follow below instructions.

1.  Select the visual you want to apply formatting rules.
2.  Go to Format pane and click on “Data colors”.
3.  When you hover on the label “Default color”, you notice three dots. Click on them to activate “Conditional format” screen.

![Activating conditional formatting feature from data colors - demo](https://chandoo.org/wp/wp-content/uploads/2019/07/data-colors-conditional-formatting-power-bi.gif)

4.  Here you can define a rule for coloring the chart. There are 3 types of conditional formats (as of writing this post in last week of July, 2019). They are,
    1.  Color scales
    2.  Rules
    3.  Field value

### Color scales:

As the name suggests, this will create a continuous color scale from minimum to maximum value. You can opt for diverging scale to include a midpoint color too. I am not a big fan of this for normal charts (although I do use it on tables / matrix visuals).

![Color scale rule for conditional formatting in visuals - demo](https://chandoo.org/wp/wp-content/uploads/2019/07/conditional-formatting-power-bi-rule-types-1.png)

### Rules:

This gives you flexibility to define a rule based logic for coloring. You can write rules to color chart elements based on number or item rules. See this example to understand how to set up a rule to highlight all cities where “Quantity per Transaction” is less than 8.2 in different color.

![Adding rule based conditional formatting - example](https://chandoo.org/wp/wp-content/uploads/2019/07/cf-power-bi-rule-based.png)

Sample rules in Power BI visual conditional formatting

**This is how our final chart would look:**

![Final output of conditional formatting based on rules](https://chandoo.org/wp/wp-content/uploads/2019/07/conditional-formatting-applied-to-visual-demo.png)

Demo of Conditional Formatting in Power BI based on rules

### Field Value:

You can also write a measure (or have a table field) that returns HEX code (or RGB code) for the color you want to use for each chart element. If you have such a measure, you can use Field value based rules to set them. For example, you can create a measure like \[Column Color\] and link it.

\[Column Color\] = IF(\[Quantity per Transaction\]>8.2, "#999999", "#c82222")

When you link this \[Column Color\] measure to the chart on Field value rule, your columns will be either of those colors (#999999 or #c82222) based on the \[Quantity per Transaction\] for each item in the chart.

### How to make rules based on _dynamic values_?

As of now, the conditional formatting in Power BI only accepts rules based on fixed (hardcoded) values. But we can create an intermediate measure to overcome this limitation. For example, we can create a measure like this:

\[Rule outcome for highlighting\] = IF(\[Quantity per Transaction\] > \[QpT Target\], 1, 0)

We can then use \[Rule outcome for highlighting\] in the rules and color based on the fixed values of 0 or 1.

How to conditionally format visuals in Power BI – Video tutorial
----------------------------------------------------------------

If you are still confused or need some guidance, please watch this 10 minute video. It explains all 3 types of conditional formatting with examples. Watch the video below or [**on our YouTube Channel**](https://youtu.be/lhf2tJeiwYw)
.

Download Sample Workbook – Conditional formatting in Power BI
-------------------------------------------------------------

**[Please download the sample file for this tutorial here](http://files.chandoo.org/pbix/cf-power-bi-demo.pbix)
**. You can see a demo of all three types of rules. Feel free to examine the data model, measures or create something on your own to learn how it all works.

### Learn more about conditional formatting in Power BI:

Microsoft has been enhancing conditional formatting feature in Power BI over time. Just recently (in July 2019 release) they have launched support for icon rules (similar to Excel conditional formatting icons) for tables & matrix visuals. Learn more about [conditional formatting in Power BI by reading Power BI docs](https://docs.microsoft.com/en-us/power-bi/desktop-conditional-table-formatting)
.

### More Power BI examples & tutorials:

*   Getting Started: [**What is Power BI?**](https://chandoo.org/wp/what-is-power-bi-power-query-and-power-pivot/)
    
*   Tip: [Creating beautiful reports in Power BI – 5 tips](https://chandoo.org/wp/tips-for-designing-beautiful-power-bi-reports/)
    
*   Full example: **[Employee Turnover dashboard in Power BI](https://chandoo.org/wp/employee-turnover-dashboard-powerbi/)
    **
*   Recommendation: [Best books for learning Power BI](https://chandoo.org/wp/best-excel-power-bi-books/)
    

### Do you use conditional formatting in Power BI?

I have been using CF more often in my Power BI training / work as it is a powerful way to highlight important information without cluttering your reports.

**What about you?** Have you toyed with conditional formatting in Power BI? Got any interesting tips to share? Please post them in the comments.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/conditionally-format-visuals-in-power-bi/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/conditionally-format-visuals-in-power-bi/#respond)
    
*   Tagged under [conditional formatting - Power BI](https://chandoo.org/wp/tag/conditional-formatting-power-bi/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [measures](https://chandoo.org/wp/tag/measures/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    

[PrevPreviousTour de France – Distance & Pace over time – Radial Charts](https://chandoo.org/wp/tour-de-france-radial-chart/)

[NextPivot Tables from large data-sets – 5 examplesNext](https://chandoo.org/wp/pivot-tables-from-large-data-sets/)

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
    
    [Reply](https://chandoo.org/wp/conditionally-format-visuals-in-power-bi/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/conditionally-format-visuals-in-power-bi/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/conditionally-format-visuals-in-power-bi/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
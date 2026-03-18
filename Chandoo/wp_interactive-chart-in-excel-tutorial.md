# How to create an Interactive Chart in Excel? [Tutorial] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/interactive-chart-in-excel-tutorial

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

How to create an Interactive Chart in Excel? \[Tutorial\]
=========================================================

*   Last updated on April 24, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Imagine you have a worksheet with lots of charts. And you want to make it look awesome & clean._

**Solution?**

Simple, create an interactive chart so that your users can pick one of many charts and see them.

**Today let us understand how to create an interactive chart using Excel.**

PS: This is a revised version of almost 5 year old article – [Select & show one chart from many](http://chandoo.org/wp/2008/11/05/select-show-one-chart-from-many/)
.

### A demo of our interactive Excel chart

First, take a look at the chart that you will be creating.

![How to create interactive chart using Excel - Demo](https://cache2.chandoo.org/images/c/interactive-chart-in-excel-demo.gif)

Feeling excited? read on to learn how to create this.

### Solution – Creating Interactive chart in Excel

1.  First create all the charts you want and place them in separate locations in your worksheet. Lets say your charts look like this.  
    ![Create charts in separate ranges like this...](https://img.chandoo.org/c/create-charts-and-place-them-ranges-like-this.png)
2.  Now, select all the cells corresponding to first chart, press ALT MMD (Formula ribbon > Define name). Give a name like `Chart1`.  
    ![Select all cells corresponding to first chart and give them a name like Chart1](https://img.chandoo.org/c/create-a-named-range-for-chart-cells.png)
3.  Repeat this process for all charts you have, naming them like `Chart2`, `Chart3`…
4.  In a separate range of cells, list down all chart names. Give this range a name like `lstChartTypes`.
5.  Add a new sheet to your workbook. Call it “Output”.
6.  In the output sheet, insert a combo-box form control (from Developer Ribbon > Insert > Form Controls)  
    ![Insert combo-box form controls - Excel](https://img.chandoo.org/c/insert-combo-box-form-control.png)
7.  Select the combo box control and press Ctrl+1 (format control).
8.  Specify input range as `lstChartTypes` and cell link as a blank cell in your output sheet (or data sheet).  
    \[Related: [Detailed tutorial on Excel Combo box & other form controls](http://chandoo.org/wp/2011/03/30/form-controls/#combo-box)\
    \]
    
    ![Combo box form control settings - Excel interactive chart tutorial](https://img.chandoo.org/c/combo-box-settings-excel.png)
    
9.  Now, when you make a selection in the combo box, you will know which option is selected in the linked cell.  
    ![Demo of combo box & cell linkage - Excel interactive chart tutorial](https://img.chandoo.org/c/demo-of-combo-box-cell-linkage-excel.gif)
10.  Now, we need a mechanism to pull corresponding chart based on user selection. Enter a named range – `selChart`.
11.  Press ALT MMD or go to Formula ribbon > Define name.  Give the name as `selChart` and define it as  
    `=CHOOSE(_linked_cell_, Chart1, Chart2, Chart3, Chart4)`  
    PS: CHOOSE formula will select one of the Chart ranges based on user’s selection (help).
12.  Now, go back to data & charts sheet. Select Chart1 range. Press CTRL+C to copy it.
13.  Go to Output sheet and paste it as linked picture (Right click > Paste Special > Linked Picture)  
    ![Pasting a picture link - Excel interactive chart tutorial](https://img.chandoo.org/c/paste-linked-picture.png)
14.  This will insert a linked picture of Chart 1.  
    \[Related: [What is a picture link and how to use it?](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)\
    \]
15.  Now, click on the picture, go to formula bar, type =selChart and press enter
16.  Move the image around, position it nicely next to the combo box.
17.  Congratulations! Your interactive chart is ready 🙂

### Video tutorial explaining this chart

Watch below tutorial to understand how to make this chart.

(or [watch it on our Youtube channel](http://youtu.be/rPwzdmTqJrc)
)

Download Interactive Chart Excel file
-------------------------------------

[**Click here to download interactive chart Excel file**](https://img.chandoo.org/d/interactive-chart-in-excel-tutorial.xlsx)
 and play with it. Observe the named ranges (selChart) and set up charts to learn more.

### More Examples of Dynamic & Interactive Charts

If you want to learn more about these techniques, go thru below examples.

*   [Interactive sales analysis chart using Excel](http://chandoo.org/wp/2012/05/09/interactive-sales-chart-in-excel/)
    
*   [Use analytical charts to make your boss fall in love with you](http://chandoo.org/wp/2011/03/16/analytical-charts-tutorial/)
    
*   [Making a dynamic chart with checkboxes](http://chandoo.org/wp/2010/08/31/dynamic-chart-with-check-boxes/)
    
*   [How to make your charts & dashboards interactive – Detailed how to guide](http://chandoo.org/wp/2012/08/02/making-dashboards-interactive/)
    
*   [Lots of examples, tips & downloads on interactive & dynamic charts in Excel](http://chandoo.org/wp/tag/dynamic-charts/)
    

### Do you use interactive charts?

Dynamic & interactive charts are one of my favorite Excel tricks. I use them in almost all of my dashboards, Excel models and my clients are always wowed by them.

**What about you?** Do you use interactive charts often? What are your favorite techniques for creating them? _Please share your tips & ideas using comments._

### Want to learn more? Consider joining my upcoming Dashboards & Advanced Excel Masterclass

I’m very excited to announce my upcoming Advanced Dashboards in Excel Masterclass in USA.

Chandoo.org & PowerPivotPro.com will be hosting this two day, intensive hands-on Masterclass. Enhance your Excel skills to create interactive, dynamic and polished looking dashboards your boss will love. Don’t miss out, this is a one-time opportunity to attend my live workshop in Chicago, New York, Washington DC & Columbus OH in May and June 2013. Places are strictly limited.

**[Click here to know more & book your spot in my Masterclass](http://chandoo.org/wp/resources/aed-masterclass-usa-2013/)
**

Above article is a preview of the tips and tricks you will be learning in the Masterclass.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [109 Comments](https://chandoo.org/wp/interactive-chart-in-excel-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interactive-chart-in-excel-tutorial/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [choose()](https://chandoo.org/wp/tag/choose/)
    , [combo box](https://chandoo.org/wp/tag/combo-box/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [picture link](https://chandoo.org/wp/tag/picture-link/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousChart for wall hygrometric physic (or how to create a chart with custom x axis intervals?)](https://chandoo.org/wp/wall-hygrometric-physic-chart/)

[Next10 Rookie mistakes to avoid when making dashboards Next](https://chandoo.org/wp/10-rookie-mistakes-to-avoid-when-making-dashboards-video/)

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
    
    [Reply](https://chandoo.org/wp/interactive-chart-in-excel-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interactive-chart-in-excel-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interactive-chart-in-excel-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# How to select a random sample from all your data [trick] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-select-a-random-sample-from-all-your-data

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

How to select a random sample from all your data \[trick\]
==========================================================

*   Last updated on January 31, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_The other day, I got a text message (SMS) from one of our readers. It read,_

![How to select random samples from data in Excel?](https://img.chandoo.org/pivot/how-to-select-random-samples-from-data.png)

**So today, let us learn a very easy trick to select random sample from your data.**

### Lets take a look at the data

Since the text message has no actual data, I made up this.

![Random samples needed from this data set](https://img.chandoo.org/pivot/data-for-random-sample.png)

Now, if you just want to select any 10 (or x number of) random items from this list, then your job would very simple.

1.  [Shuffle (or randomly arrange) this list](http://chandoo.org/wp/2008/07/28/shuffle-cells-random-order/)
    
2.  Just pick first 10 items

But our problem is to get 2 random samples per user.

### Selecting random samples from data

Follow below steps.

1.  Add an extra column and fill it with =RAND() formula. _This generates random fraction between 0 and 1._
    
    ![Add RAND() function to the adjacent column](https://img.chandoo.org/pivot/add-rand%28%29-formula.png)
    
2.  Create a pivot table from this data (tutorial: [How to create a pivot table?](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
    )
3.  Add User ID & Case ID as Row labels and Random as value field.  
    ![Pivot table layout for selecting random samples](https://img.chandoo.org/pivot/pivot-table-layout.png)
4.  Click on the filter icon on Case ID column, choose Value filter > Top 10
5.  Filter for top 2 random values. (related: [Filter top 10 values in pivot tables – how to?](http://chandoo.org/wp/2010/12/01/top-10-values-in-dashboards/)
    )
    
    ![Pivot Table value filters - filtering top 2 values](https://img.chandoo.org/pivot/top-2-filter-pivot-table.png)
    
6.  Adjust report layout (Table layout, no sub-totals, no grand totals)
    
    ![Report layout to show just the samples and nothing else](https://img.chandoo.org/pivot/report-layout-setting.png)
    
7.  Done!

![Final random samples - easy and awesome.](https://img.chandoo.org/pivot/random-samples-from-data-using-pivot-tables.png)

### To see new samples

Just select any cell in the pivot table, press ALT+F5. Your pivot table will be refreshed and you get new samples.

That is just easy and awesome!

### Download Example Workbook

[**Click here to download the example file**](https://img.chandoo.org/pivot/random-samples-thru-pivot-tables.xlsx)
. Refresh the pivot table (ALT+F5) to see fresh samples.

### Do you sample your data?

Drawing samples, running experiments, analyzing results are life breath for many businesses. As business data is growing, these analytical skills  are becoming important.

_**How do you draw samples?**_ What techniques you use when analyzing the data? **Please share your stories, experiences & tips using comments**.

### A sample of our awesome collection of Excel tips

Here is a tiny sample of our awesome Excel tips. Don’t hold back, take them all, and [more](http://chandoo.org/wp/archives/)
.

*   [Introduction to Pivot Tables](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
    
*   [How to shuffle a list of values in Excel](http://chandoo.org/wp/2008/07/28/shuffle-cells-random-order/)
    
*   [How to shuffle a list using Formulas](http://chandoo.org/wp/2008/09/23/sort-in-random-order-excel-formulas/)
    
*   [How to generate a random date](http://chandoo.org/wp/2009/12/08/random-dates/)
    , [phone number](http://chandoo.org/wp/2008/11/20/random-phone-number-formula/)
    
*   [Introduction to Excel’s random functions](http://chandoo.org/wp/2011/05/04/dummy-data-random-functions/)
    
*   Case study: [Generating housie (bingo) number cards using Excel](http://chandoo.org/wp/2008/07/16/bingo-housie-ticket-generator-excel/)
    
*   Game: [Simulating Deal or No Deal game in Excel](http://chandoo.org/wp/2008/10/03/download-excel-deal-or-no-deal-game-play/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [18 Comments](https://chandoo.org/wp/how-to-select-a-random-sample-from-all-your-data/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-select-a-random-sample-from-all-your-data/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Filter PivotTables](https://chandoo.org/wp/tag/filter-pivottables/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [rand()](https://chandoo.org/wp/tag/rand/)
    , [random](https://chandoo.org/wp/tag/random/)
    , [sampling data](https://chandoo.org/wp/tag/sampling-data/)
    , [top 10 values](https://chandoo.org/wp/tag/top-10-values/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPrevious5 reasons why you should learn Power Pivot](https://chandoo.org/wp/5-reasons-why-you-should-learn-power-pivot/)

[NextThank you and Excel, We have a new carNext](https://chandoo.org/wp/thank-you-and-excel-we-have-a-new-car/)

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
    
    [Reply](https://chandoo.org/wp/how-to-select-a-random-sample-from-all-your-data/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-select-a-random-sample-from-all-your-data/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-select-a-random-sample-from-all-your-data/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
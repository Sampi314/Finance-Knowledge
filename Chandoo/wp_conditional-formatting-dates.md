# Conditionally Formatting Dates in Excel - How to format dates in excel based on a condition?

**Source:** https://chandoo.org/wp/conditional-formatting-dates

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Conditionally Formatting Dates in Excel \[Part 1 of 2\]
=======================================================

*   Last updated on January 5, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is first part of 2 part series on conditionally formatting dates in excel.  
_

**Conditional formatting is a very useful feature in Excel.** You can use Conditional formatting to tell excel how to format cells that meet certain conditions. For eg. You can use conditional formatting to show all negative values in a range in red color. \[[Learn conditional formatting basics](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)\
\].

**Today we will learn how to use conditional formatting to format dates.**

Click on the below links to jump to relevant section.  
[Excel 2007+ – Conditional Formatting Dates](https://chandoo.org/wp/conditional-formatting-dates/#excel2007-conditional-formatting-dates)
  
[Excel 2003 – Conditional Formatting Dates](https://chandoo.org/wp/conditional-formatting-dates/#excel2003-conditional-formatting-dates)

### Excel 2007+ – Conditional Formatting Dates

![Excel 2007 - Conditional Formatting Dates - menu](https://chandoo.org/img/n/conditional-formatting-dates-excel-2007.png "Excel 2007 - Conditional Formatting Dates - menu")

In Excel 2007, MS introduced several useful shortcuts to conditionally format dates. When you select some cells and click on Conditional Formatting button on ribbon and select “Highlight cells Rules” > “A date occurring”, Excel presents you quick shortcuts to frequent date criteria. This list includes options to format,  
![Excel 2007 - Conditional Formatting Dates](https://chandoo.org/img/n/conditional-formatting-dates-options-in2007.png "Excel 2007 - Conditional Formatting Dates")

*   A Date if it is yesterday
*   Today
*   Tomorrow,
*   In the last 7 days
*   Last week
*   This Week
*   Next Week
*   Last Month
*   This Month
*   Next Month

Using this feature, you can quickly format the dates in your data meeting certain criteria.

This is very useful in situations where you want to highlight for eg. sales in last week. As the dates change, the highlighted values change dynamically.

_Apart from these predefined date conditions, you can define your own conditions using formulas._

### Excel 2003 – Conditional Formatting Dates

Unlike Excel 2007, there are no shortcuts for conditional date formatting in Excel 2003. You have to rely on Conditional Formatting Formulas to do this.

**What is a conditional formatting formula?**  
In excel you can use formulas to determine which cells get the special formatting thru conditional formatting. For eg. a formula like =A1>50 applied over the range A1:A10 will highlight the cells with value more than 50.

**So, to check if the date in cell A1 is yesterday, you can write a simple formula like,**  
`=TODAY()-A1=1.` \[[help on TODAY formula](https://chandoo.org/excel-formulas/today.html)\
\]

![Excel 2003 - Conditional Formatting Dates](https://chandoo.org/img/n/conditional-formatting-dates-excel-2003.png "Excel 2003 - Conditional Formatting Dates")

**Here are some formulas to get you started,**

*   To check if a date is in the last 7 days:  
    `=TODAY()-A1<7`
*   To check if a date is in the current week:  
    `=AND(WEEKNUM(A1)=WEEKNUM(TODAY()), YEAR(A1)=YEAR(TODAY()))`
*   To check if a date is in the current month:  
    `=AND(MONTH(A1)=MONTH(TODAY()), YEAR(A1)=YEAR(TODAY()))`
*   To check if a date is in the last 30 days:  
    `=TODAY()-A1<30`

\[Help on [AND formula](http://chandoo.org/excel-formulas/and.html)\
, [MONTH formula](http://chandoo.org/excel-formulas/month.html)\
, [YEAR formula](http://chandoo.org/excel-formulas/year.html)\
, [IF formula](http://chandoo.org/excel-formulas/if.html)\
\]

Using above formula based conditional formatting you can easily determine if a date meets a given criteria and highlight it.

### A Practical Application – Highlighting Repeat Customers

Let us say you run a small retail store. And you want to give special discounts to all the repeat customers. In your mind _a repeat customer is someone who bought twice from you in last 30 days._ (If the person bought twice but the gap between 2 purchases is more than 30 days they are not repeat customers).

**In tomorrow’s post I will show you how to highlight repeat customers using excel conditional formatting. Stay tuned.  
**

### Learn more about Excel Conditional Formatting

*   [Excel conditional formatting basics](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
    
*   [Using formulas in excel conditional formatting – 5 kickass examples](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
    
*   [Highlight Top 10 items in a list – using conditional formatting](http://chandoo.org/wp/2009/03/17/highlight-top-10-values-conditional-formatting/)
    
*   More tutorials on [Conditional Formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    , [Excel Dates](http://chandoo.org/wp/tag/date-and-time/)
    , [Excel Date Formulas](http://chandoo.org/excel-formulas/date-time-functions.html)
    

### Join our email news letter:

If you like this article, please join our mailing list. You will get an excel tip every weekday. Also, you will get a free copy of my 95 excel tips e-book. **[Click here to join](http://feedburner.google.com/fb/a/mailverify?uri=PointyHairedDilbert&loc=en_US)
**.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [187 Comments](https://chandoo.org/wp/conditional-formatting-dates/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/conditional-formatting-dates/#respond)
    
*   Tagged under [and()](https://chandoo.org/wp/tag/and/)
    , [conditional formatting dates](https://chandoo.org/wp/tag/conditional-formatting-dates/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [excel basics](https://chandoo.org/wp/tag/excel-basics/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [month](https://chandoo.org/wp/tag/month/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [today()](https://chandoo.org/wp/tag/today/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    , [weekday](https://chandoo.org/wp/tag/weekday/)
    , [weeknum()](https://chandoo.org/wp/tag/weeknum/)
    , [year](https://chandoo.org/wp/tag/year/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousSales Dashboards – Visualizing Sales Data – 32 Dashboard Examples & Implementations](https://chandoo.org/wp/sales-dashboards/)

[NextHighlighting Repeat Customers using Conditional Formatting \[Part 2 of 2\]Next](https://chandoo.org/wp/highlight-repeat-customers/)

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
    
    [Reply](https://chandoo.org/wp/conditional-formatting-dates/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/conditional-formatting-dates/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/conditional-formatting-dates/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
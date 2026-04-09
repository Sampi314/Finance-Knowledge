# Highlighting Repeat Customers using Conditional Formatting [Part 2 of 2] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/highlight-repeat-customers

---

*   [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Highlighting Repeat Customers using Conditional Formatting \[Part 2 of 2\]
==========================================================================

*   Last updated on January 5, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is second part of 2 part series on conditionally formatting dates in excel._

![Highlighting Repeat Customers using Conditional Formatting](https://chandoo.org/img/n/repeat-customers-excel-conditional-formatting.png "Highlighting Repeat Customers using Conditional Formatting")In yesterday’s post we have learned [how to conditionally format dates using excel](http://chandoo.org/wp/2010/01/05/conditional-formatting-dates/)
. In this article, you will learn how to use these conditional formatting tricks to highlight repeat customers in a list of sales records.

### The problem: Highlighting repeated customers in a list

Let us say you run a small retail store. And you want to give special discounts to all the repeat customers.

_**Repeat customer** is someone who bought at least twice from you in last 30 days._ (If the person bought twice but the gap between 2 purchases is more than 30 days they are not repeat customers).

### The Data:

Let us assume your sales data has these 2 columns  – customer ID and purchase date. I have shown first few rows here. Let us assume the data is in the range B4:C53.

![Highlighting Repeat Customers using Conditional Formatting - DATA](https://chandoo.org/img/n/repeat-customers-data-table.png "Highlighting Repeat Customers using Conditional Formatting - DATA")

### Finding if a customer is repeat – The Formula:

**If we just want to highlight without considering the purchase dates,**

we can use a simple formula like =COUNTIF($B4:$B53,$B3)>1 in the conditional formatting applied over the range B4:C53.

**But we need to consider the date as well,  
**

hmm, now that is tricky !??

May be time for a sip of that coffee. Go take it, I am waiting..,

_How about the [SUMPRODUCT](http://chandoo.org/wp/tag/sumproduct/)
?_ We all know that [sumproduct formula can be used to test more than one condition](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
.

**The formula:**  
`   =IF(C4>TODAY()-30,IF(SUMPRODUCT(--($B$4:$B$53=B4),--($C$4:$C$53>(TODAY()-30)))>1,"R","N"),"N")`

Now that is one lengthy badass formula. Like [Sergeant Martin Riggs](http://en.wikipedia.org/wiki/Martin_Riggs)
. Bad, but still cool.

**So what is this formula really doing?** It is going to give us “R” if a customer is repeat and “N” if not. See this explanation to understand how it works.

![Highlighting Repeat Customers using Conditional Formatting - Formula](https://chandoo.org/img/n/repeat-customers-excel-formula.png "Highlighting Repeat Customers using Conditional Formatting - Formula")

**_Note:_** the double dashes “–” make the values as 0s and 1s from a bunch of “trues” “falses”. To know why sumproduct is such a beautiful and robust formula [look no further](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/ "Excel Sumproduct Formula - What is it and how to use it?")
.

### The Conditional Formatting

Now that you have figured out the formula to determine a customer is repeat or not, applying conditional formatting is a piece-o-cake.

Just select the range B4:C53, go to conditional formatting and select “formula” option. Now specify the above formula and check if its output is “R” and apply formatting.

I am not telling you how to do this. It is your homework. Go figure!

That is all. Your workbook now highlights repeat customers in the last 30 days. Remember, as you reopen the file a week later, the highlighting logic changes since the date has changed.

### Download the example workbook

**[Click here](http://chandoo.org/img/n/repeat-customers-excel-cf-example.xls)
** to download the example workbook and understand how to highlight repeat customers using conditional formatting. The file works in Excel 2003+.

### What is your experience?

Share your tips and ideas on using conditional formatting with dates. What are the situations you usually face and how to solve them? I am never too old for this, so please share.

### Learn more about conditional formatting

*   [Working with dates & conditional formatting](http://chandoo.org/wp/2010/01/05/conditional-formatting-dates/)
    
*   [Excel conditional formatting basics](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
    
*   [Using formulas in excel conditional formatting – 5 kickass examples](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
    
*   [Highlight Top 10 items in a list – using conditional formatting](http://chandoo.org/wp/2009/03/17/highlight-top-10-values-conditional-formatting/)
    
*   More tutorials on [Conditional Formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    , [Excel Dates](http://chandoo.org/wp/tag/date-and-time/)
    , [Excel Date Formulas](http://chandoo.org/excel-formulas/date-time-functions.html)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/highlight-repeat-customers/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/highlight-repeat-customers/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [conditional formatting dates](https://chandoo.org/wp/tag/conditional-formatting-dates/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [if()](https://chandoo.org/wp/tag/if/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [small business tools](https://chandoo.org/wp/tag/small-business-tools/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [today()](https://chandoo.org/wp/tag/today/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousConditionally Formatting Dates in Excel \[Part 1 of 2\]](https://chandoo.org/wp/conditional-formatting-dates/)

[NextA New Year Resolutions Template that Kicks AssNext](https://chandoo.org/wp/new-year-resolutions-template/)

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
    
    [Reply](https://chandoo.org/wp/highlight-repeat-customers/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/highlight-repeat-customers/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/highlight-repeat-customers/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
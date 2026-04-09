# 5 conditional formatting top tips - Excel basics » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/conditional-formatting-top-tips

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

5 conditional formatting top tips – Excel basics
================================================

*   Last updated on May 13, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Time for another round of unconditional love. Today, let’s **learn about conditional formatting top tips**. It is one of the most useful and powerful features in Excel. With just a few clicks of conditional formatting you can add powerful insights to your data. Ready to learn the top tips? Read on.

### 1\. Highlight matching / missing items in two lists

Everyday millions of people ask – “Which items are common in these two lists?” and then most of them waste several minutes (or hours) comparing the lists. But you can answer the question in just five seconds. It is so simple and elegant.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-01-compare-two-lists-example-data.png)

1.  Select first list.
2.  Hold CTRL key and select the second list. This highlights both lists.
3.  Go to Home > Conditional Formatting > Highlight cell rules > Duplicate values
4.  _Voila_, you can instantly see which values are common in both lists.
5.  Bonus tip: If you want to see which values are unique to each list, just flip the highlight rule from dialog.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-01-compare-two-lists-excel.png)

Related: [Compare two lists in Excel](https://chandoo.org/wp/compare-2-lists-in-excel/)
 \[complete guide\] | [Compare things in Excel – podcast](https://chandoo.org/wp/cp021-how-to-quickly-compare-2-lists-in-excel/)

### 2\. Highlight top 10 items

Once again, a common problem faced by lots of people everyday. _Which items are top / bottom n in this list?_

The answer is simple. Just select your list and apply top / bottom rules.

Let’s say you have monthly customer walk-ins at your store as a list, like below.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-02-highlight-top-10-items-data.png)

You want to know which are top 10 days in November for customer walk-ins.

1.  Highlight walk-ins column
2.  Go to Home > Conditional formatting > Top/bottom rules > Top 10 items..
3.  Click ok (or change the number if you fancy)
4.  Done and done.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-02-highlight-top-10-items-excel.png)

_**Pro tip:**_ The default top / bottom rules only highlight the value column. If you want to highlight entire row or the corresponding date (or other data), you can use a formula based rule, like below:

> Say your data is in A1:B30 and you want to highlight the rows where value in column B is top 10.
> 
> Select your data (A1:B30), go to Conditional formatting > New Rule. Select “Use formula…” option. Type in `=$B1 >= LARGE($B1:$B30,10)` and set up formatting. Click ok and top 10 items in your data will be highlighted.

### 3\. Visualize changes over time with elegant icons

Things change, people change, money changes and most importantly, data changes… all the time. So how do you quickly and elegantly visualize how things have changed over time? Simple, apply conditional formatting icons to spot the changes.

Let’s go back to our store walk-ins example from #2.  We want to see the trend like this:

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-03-changes-over-time-icons.png)

To get this, in the adjacent column, write this simple formula to compare walks-ins with previous day.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-03-changes-over-time-formula.png)

Now, select “Trend” column and go to Conditional formatting > New rule

Select format style as “Icon sets” and apply the rule as shown below.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-03-trend-icons-excel-rule.png)

Bingo, your cute trend icons are ready.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-03-changes-over-time-icons.png)

_**Related pro tip**_: [Don’t just show simple numbers in your reports and dashboards](https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards/)
 | [Web analytics dashboard with conditional formatting & sparklines](https://chandoo.org/wp/website-dashboard-template/)

### 4\. Top customers by category

Time to ramp up the game. Let’s say you run a sporting goods store and you are looking the category-wise units sold to each customer, like below.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-04-top-customer-by-category-data.png)

_**Your question: Which customers are top in each category?**_

Unfortunately, we can’t use default top / bottom rules to answer this question. But we can use a tidy little formula to get the answer. Let’s say our data is in the range **$R$6:$T$124**.

1.  Select your data, go to Conditional Formatting > New Rule
2.  Select “Use a formula…” type of rule
3.  Write the rule `=$T6 = MAX(IF($R$6:$R$124 = $R6, $T$6:$T$124))`
4.  Set up formatting as you want
5.  Done.

**Check out below illustration to understand how this rule works:**

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-04-top-customer-by-category-rule-explained.png)

**And the result is awesome:**

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-04-top-customer-by-category-highlighted-excel.png)

_**Related: [MAXIF formula explained](https://chandoo.org/wp/formula-forensics-no-008/)
**_

### 5\. Highlight values in a range

Often we want to narrow our focus to a small range so we can analyze better. Let’s go back to the store walk-ins example. If you want to highlight all days when the walk-ins are between 145 to 160 (the sweet spot as your manager calls it), you can use the built-in between rule, like below:

1.  Select walk-ins column
2.  Go to Conditional Formatting > Highlight cell rules > Between…
3.  Either type in the range or point to cells containing values.
4.  Done.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-tips-05-values-in-a-range-highlighted.png)

_**Related: [BETWEEN formula in Excel](https://chandoo.org/wp/between-formula-excel/)
**_

### Top 5 conditional formatting tips – Example workbook

[**Click here to download the workbook**](https://chandoo.org/wp/wp-content/uploads/2017/12/cf-basics-5-top-tips.xlsx)
 with all these tips and sample data. Play with it to learn more. Try to implement your own rules to understand CF better.

### What are your top conditional formatting tips?

Over to you. What are your top conditional formatting tips? _Please share them in the comments section_.

**More conditional formatting tips:**

Conditional formatting is one of my favorite Excel features. I talk about it all the time. Check out below tutorials for more awesome tips.

*   [Conditional formatting basics – how to use it?](https://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
    
*   [Become a conditional formatting rock star with these tips](https://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
    
*   [Link conditional formatting with slicers for awesome results](https://chandoo.org/wp/2016/05/11/apply-conditional-formatting-using-slicers/)
    
*   Case study: [Design awesome financial metrics dashboard](https://chandoo.org/wp/2017/02/07/financial-dashboard-tutorial/)
    
*   Case study: [Web analytics dashboard](https://chandoo.org/wp/website-dashboard-template/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [20 Comments](https://chandoo.org/wp/conditional-formatting-top-tips/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/conditional-formatting-top-tips/#respond)
    
*   Tagged under [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [excel basics](https://chandoo.org/wp/tag/excel-basics/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [MaxIf](https://chandoo.org/wp/tag/maxif/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFilter all records for November or 11AM or 2017 \[quick tip\]](https://chandoo.org/wp/filter-all-records-for-november-or-11am-or-2017-quick-tip/)

[NextHow much long service bonus to pay? \[Homework\]Next](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/)

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
    
    [Reply](https://chandoo.org/wp/conditional-formatting-top-tips/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/conditional-formatting-top-tips/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/conditional-formatting-top-tips/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
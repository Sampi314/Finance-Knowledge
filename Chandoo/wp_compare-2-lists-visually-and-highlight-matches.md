# Compare 2 Lists Visually and Highlight Matches » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/compare-2-lists-visually-and-highlight-matches

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Compare 2 Lists Visually and Highlight Matches
==============================================

*   Last updated on October 27, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Comparison is one of the most common things we do with Excel**. Naturally, there are so many ways to compare 2 lists of data using Excel. We have discussed various techniques for comparison earlier too,

*   [Compare 2 lists using conditional formatting](http://chandoo.org/wp/2010/06/17/compare-2-lists-in-excel/)
    
*   [Even faster way to compare lists](http://chandoo.org/wp/2010/07/01/compare-lists-excel-tip/)
    
*   [Compare lists using row differences](http://chandoo.org/wp/2011/02/14/compare-data-row-differences/)
    

**Today, I want to share an interesting comparison problem with you.**

Lets say you run a small shop which sells some highly specialized products. Now, since your products require quite some training before customers can buy them, you keep track of all product queries and arrange demos.

After a hectic week, you are staring at 2 lists. One with product queries, another with product demos.

![Data that you want to compare in Excel](https://img.chandoo.org/cf/actual-data-before-comparison.png)

_**And you have 2 burning questions,**_

1\. Did we finish all the queries we had?  
2\. Should I go get some coffee?

Lets answer question number 2. **_Yes, you can get some coffee. Go, enjoy it now_**

Back already?!? Good. Now, lets answer the question 1.

Compare 2 Lists Visually _using Conditional Formatting_
-------------------------------------------------------

\[Note: this article is inspired by [Reepal’s comment](http://chandoo.org/wp/2010/06/17/compare-2-lists-in-excel/#comment-210540)\
.\]

You would like to highlight the lists as shown below, so that you would know whether each product query is fulfilled or not.

![Comparing 2 lists in excel visually and highlighting matches](https://chandoo.org/img/cf/two-lists-visually-compared-in-excel.png)

### Step 1: Create 2 more lists, with count of products

In order to compare our lists, we need some help. We will create 2 more lists like this:

![Additional lists we created to help us in highlighting the values ](https://img.chandoo.org/cf/count-of-values-using-countif-formula.png)

**How do we generate these lists?**

Assuming our original data is in B6:B33 and D6:D33,

1.  In a blank cell (lets say in F6), write =B6&COUNTIF(B$6:B6,B6)
2.  This gives the count of first product up to that point, ie, Fired Forks1.
3.  Now drag & fill the formula down until F33
4.  Do the same in column H, but use the formula =D6&COUNTIF(D$6:D6,D6)
5.  Fill this until H33

### Step 2: Name these new lists

Now that we have created 2 more lists, lets give them names. Select the range F6:F33, go to Formula ribbon and click on “Define Name”. Name the range **_count1s_**

Do the same for range H6:H33 and name it **_count2s_**

### Stpe 3: Apply Conditional Formatting to First List (Product Queries)

Now that we have done all the background work, lets visually compare the data. Select the first list (B6:B33) and go to Conditional Formatting > New Rule

We need to write a rule such that we would highlight all the items in list 1 whenever there is a match in list 2.

![Conditional Formatting Rule to Highlight the values after comparing](https://chandoo.org/img/cf/conditional-formatting-rule-for-list1.png)

_**The rule is =COUNTIF(count2s,$F6)>0**_

It means, _is the value in F6 present in 2nd list?_  
in other words, _does the first product query has a corresponding product demo?_

Set the formatting as you want. Click ok.

### Step 4: Apply conditional formatting to Second List

Use the same logic, but this time the rule becomes =COUNTIF(count1s,$H6)

### That is all, we have visually compared the two lists.

If you feel like, you can go back for one more cup of coffee.

Download Example Workbook
-------------------------

[**Click here to download the example workbook – Compare 2 lists visually**](https://img.chandoo.org/d/compare-2-lists-visually.xlsx)
 and play with it. Examine the formulas in columns F & H. Also examine the conditional formatting rules to understand how this works.

How do you compare lists of data?
---------------------------------

For me comparison is an everyday task. I rely in several techniques, some quick and dirty, others a bit more elaborate. For quick comparisons, I use either [row differences](http://chandoo.org/wp/2011/02/14/compare-data-row-differences/)
 or [highlight duplicates rule](http://chandoo.org/wp/2010/07/01/compare-lists-excel-tip/)
. For elaborate comparisons, I use [COUNTIF](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)
, [VLOOKUP](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
 or other formula based techniques.

**What about you?** How do you compare lists of values? What techniques and tips you suggest. _**Please share using comments.**_

Want to learn Excel Formulas?
-----------------------------

If you want to learn Excel formulas so that you can compare, analyze and present better, then please consider joining my Excel Formula Crash Course. This is an 8 hour online training program aimed to make you awesome in Excel formulas. We teach more than 40 every day formulas with loads of real-world examples, practice material & homework.

[**Click here to know more**](https://chandoo.org/wp/compare-2-lists-visually-and-highlight-matches/chandoo.org/wp/training-programs/formula-crash-course/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/compare-2-lists-visually-and-highlight-matches/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/compare-2-lists-visually-and-highlight-matches/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [comparison](https://chandoo.org/wp/tag/comparison/)
    , [countif()](https://chandoo.org/wp/tag/countif/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [goto special](https://chandoo.org/wp/tag/goto-special/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousTell us what you would like to learn in our Excel for PMs course \[Survey\]](https://chandoo.org/wp/excel-for-pm-survey/)

[NextUsing an Array Formula to Find and Count the Maximum Text Occurrences in a RangeNext](https://chandoo.org/wp/using-array-formulas-to-find-count/)

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
    
    [Reply](https://chandoo.org/wp/compare-2-lists-visually-and-highlight-matches/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/compare-2-lists-visually-and-highlight-matches/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/compare-2-lists-visually-and-highlight-matches/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# Compare 2 lists of Data in Excel - Tutorial & Download Example

**Source:** https://chandoo.org/wp/compare-2-lists-in-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Become a Comparison Ninja – Compare 2 Lists in Excel and Highlight Matches
==========================================================================

*   Last updated on August 19, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Comparison of lists of data is something that we do all the time.** Today, lets learn a few tricks that you can apply immediately to compare 2 lists using Excel.

This post discusses how to compare two lists with formula based rules. If you just want to [**quickly highlight common values, click here**](https://chandoo.org/wp/compare-lists-excel-tip/)
.

If you want to [**compare two tables (based on multiple columns), see this**](https://chandoo.org/wp/compare-two-tables/)
.

_**We will learn how to compare 2 lists of data in 3 + 1 different ways.**_ (click on links to jump to that section of post)

1.  [Highlight items that are only in first list](https://chandoo.org/wp/compare-2-lists-in-excel/#first-list-only)
    
2.  [Highlight items that are only in second list](https://chandoo.org/wp/compare-2-lists-in-excel/#second-list-only)
    
3.  [Highlight items that are in both lists](https://chandoo.org/wp/compare-2-lists-in-excel/#both-lists)
    
4.  [Search and highlight matches in both lists](https://chandoo.org/wp/compare-2-lists-in-excel/#search-items)
     _**– Home Work**_

### Understanding the Comparison Logic:

Whenever you compare 2 sets of values, there are 3 possibilities, as shown in the illustration below:

![Comparing two sets of values - theory](https://chandoo.org/img/cf/comparing-lists-in-excel-theory.png)

Apart from looking like  circles drawn by hulk with a crayon, these circles show important concepts of set theory in simplest form.

\[there is a fourth possibility of a value not being in either lists, we omit that for now\]

### What you need to compare 2 lists?

1\. Of course, you need 2 lists of data. But, just to make formulas simpler and easier to read, lets name the 2 lists as `lst1` and `lst2`.

Lets assume your data looks like this:

![Compare 2 lists of Data in Excel - Tutorial & Download Example](https://chandoo.org/img/cf/compare-lists-in-excel-data.png)

2\. Also, you should know [how to use COUNTIFS Excel Formula](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
, it is so awesome, I wonder why MS hasn’t called it `MAGIC()` ?

_**So in order to find-out if a value is in list 1 only,**_ we use a formula like `=COUNTIFS(lst2,value)=0`.

This checks whether “value” occurs anywhere in lst2 and returns false if that is the case.  (it assumes that value is already in lst1).  

### Highlighting Items that are in First List Only

![Compare and highlight values in first list only](https://chandoo.org/img/cf/highlight-values-in-first-list-only-compare-lists-in-excel.png)

1.  ![Conditional Formatting Formula to Compare 2 lists in Excel](https://chandoo.org/img/cf/compare-lists-conditional-formatting-formula.png)Select values in first list (assuming the values are in `B21:B29`)
2.  Go to conditional formatting > add rule (related: [conditional formatting basics](http://chandoo.org/wp/excel-conditional-formatting-basics/)
    )
3.  Select the rule type as “formula”
4.  Write a rule like this: `=COUNTIFS(lst2, B21)=0`
5.  Double check the reference and make sure it is relative (and not like $B$21). Select the reference and press F4 repeatedly to change it to relative reference
6.  Set the formatting you want.
7.  Click ok.
8.  All done. You should see values _**only**_ in first list highlighted.

### Highlighting Items that are in Second List Only

![Compare and highlight values in second list only](https://chandoo.org/img/cf/highlight-values-in-second-list-only-compare-lists-in-excel.png)

1.  Select values in second list (assuming the values are in `C21:C28`)
2.  Go to conditional formatting > add rule (related: conditional formatting basics)
3.  Select the rule type as “formula”
4.  Write a rule like this: `=COUNTIF(lst1, C21)=0`
5.  Repeat steps 5-8 as above.

### Highlighting Values in Both Lists:

![Compare and highlight values in both lists](https://chandoo.org/img/cf/highlight-values-in-both-lists-compare-lists-in-excel.png)

Now, it gets interesting as you should apply conditional formatting individually to both lists.

1.  Select values in first list (assuming the values are in `B21:B29`)
2.  Set the conditional formatting rule as `=COUNTIF(lst2,B21)>0`
3.  Apply formatting as you want.
4.  Now select second list (assuming the values are in `C21:C28`)
5.  Set the conditional formatting rule as `=COUNTIF(lst1,C21)>0`
6.  Again, apply formatting as you want.
7.  That is all.

### Searching for a value and Highlighting Matched Items in Both Lists – Your Homework:

This is another common thing we do. We want to find-out a given value (say in A1) is in the both lists, first list or second list and highlight all the matches. Like this:

![Search and highlight a value in multiple lists](https://chandoo.org/img/cf/searching-for-a-value-in-2-lists.gif)

Of course, doing this is very straightforward in Excel once you understand the above 3 things. So I am leaving this as your home work.

Go ahead, figure this out, practice it on a workbook. When you are satisfied with your result, post the answers here. **Discuss!**

### Download Example Workbook on Comparing 2 Lists in Excel:

[Go ahead and download the example workbook on comparing 2 lists in excel](https://img.chandoo.org/d/compare-2-lists.xls)
. \[[download from mirror](http://cid-b663e096d6c08c74.office.live.com/view.aspx/Public/compare-2-lists.xls)\
\]

It also contains the answer to homework above. _**Play with it and become comparison ninja**_.

### How do you compare lists in Excel?

I often have to compare values in multiple lists (for eg. customers of one product vs. another, defect status this month vs. last month etc.). I use formulas to compare with-in table. And if I want to highlight the matches, I use CF.

**What about you?** How do you compare lists of values in Excel? What formulas do you use? _**Please share your techniques and tips using comments.**_

### More Tips & Tutorials on Excel Conditional Formatting:

1.  [5 tips to make you a conditional formatting rock star](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
    
2.  [Highlighting repeat customers using Excel](http://chandoo.org/wp/2010/01/06/highlight-repeat-customers/)
    
3.  [Working with Dates & Conditional Formatting](http://chandoo.org/wp/2010/01/05/conditional-formatting-dates/)
    
4.  [Searching and Visually highlighting values using Conditional Formatting](http://chandoo.org/wp/2009/03/31/search-with-conditional-formatting/)
    
5.  [Highlighting top 10 values in Excel](http://chandoo.org/wp/2009/03/17/highlight-top-10-values-conditional-formatting/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [112 Comments](https://chandoo.org/wp/compare-2-lists-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/compare-2-lists-in-excel/#respond)
    
*   Tagged under [comparison](https://chandoo.org/wp/tag/comparison/)
    , [countif()](https://chandoo.org/wp/tag/countif/)
    , [data visualization](https://chandoo.org/wp/tag/data-visualization/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [search](https://chandoo.org/wp/tag/search/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousSuper-mini Quick Update on Excel School](https://chandoo.org/wp/update-on-excel-school/)

[NextWhat new chart types you want to see in Excel? \[poll\]Next](https://chandoo.org/wp/new-charts-poll/)

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
    
    [Reply](https://chandoo.org/wp/compare-2-lists-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/compare-2-lists-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/compare-2-lists-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
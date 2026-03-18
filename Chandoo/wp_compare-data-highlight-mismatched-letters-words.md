# Compare 2 sets of data by letter or word & highlight mismatches [vba] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/compare-data-highlight-mismatched-letters-words

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Compare 2 sets of data by letter or word & highlight mismatches \[vba\]
=======================================================================

*   Last updated on December 15, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We analysts like to compare. If you ever want to keep an analyst busy, just give her 2-3 options. She won’t return to your desk until the cows come home. My wife uses this trick all the time. Picture this:

\[In late 2013\]  
Me: I want to buy a new phone  
She: Do you want Nexus 5 or Galaxy S5 or iPhone 5s?

_Its late 2014 and I am not done comparing._

So today, let’s talk about an interesting comparison scenario.

### Comparing by letter or word

Imagine you are looking at 2 lists like this and you want to know where items differ. Not **which items,** but where.

![Compare 2 lists of data and highlight mismatched letters or words in Excel - How to?](https://img.chandoo.org/vba/match-2-sets-of-data-by-letter-or-word-in-excel.png)

That means, you want to know which letters or words in each line are different.

### VBA to the rescue

Unfortunately, none of the standard features of Excel (formulas, conditional formatting, pivot tables etc.) can help us with this situation. But we don’t have to give up. We can use a simple [VBA macro](http://chandoo.org/wp/excel-vba/)
 to instantly compare 2 lists and highlight mismatched letters or words.

\[Related: [How to compare 2 lists in Excel, a quick round up of techniques](http://chandoo.org/wp/2014/10/02/cp021-how-to-quickly-compare-2-lists-in-excel/ "CP021: How to quickly compare 2 lists in Excel")\
\]

**A quick demo of our comparison macro:**

![Compare two texts in Excel and highlight unmatched letters or words using VBA Macros - Demo](https://img.chandoo.org/vba/compare-2-texts-by-letter-word-demo.gif)

### How does this macro work?

When you set out to create macros like this, the first step is to define basic algorithm (logical steps in plain English). To compare 2 sets of data, we need to do below:

1.  For each item in list 1
2.  Get corresponding item in list 2
3.  If they don’t match
4.  For word match
    1.  For each word in first text
    2.  Get corresponding word in second text
    3.  Compare
    4.  If not matched, highlight in red color
    5.  Repeat for other words
5.  For letter match
    1.  Find the first mismatched letter
    2.  Highlight all the letters from that point in second text
6.  Repeat for next item in list 1
7.  Done

Once you write down this logic, we simply go ahead and implement it in VBA code.

The exact workings of the macro are somewhat complex. So I made a video explaining how the code works & what it can do. Please watch it below.

### Video explaining the comparison macro

\[see [this video on our YouTube Channel](http://youtu.be/_sOS2uZPfrA)\
\]

### Download Example Workbook

[**Click here to download the comparison macro workbook**](https://img.chandoo.org/vba/match-2-columns.xlsm)
. Examine the code to understand how it is constructed. Feel free to extend it to suit your work needs.

### Do you compare lists like this?

Every now and then, I end up having a situation where I need to compare by letter or word. I find VBA macro based solution to be perfect for this.

**What about you?** Do you compare lists? Where do you struggle with such comparisons? How would you use this macro? _**Please share your thoughts & tips in comments.**_

### Become incomparable, learn VBA

While VBA is pretty powerful & awesome, not many venture beyond the basic recorded macros. You can transform the work, career & skills by learning VBA. It is not at all difficult and anyone can learn it. Start with below links.

*   [Introduction to VBA & 5 part crash course](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/ "What is VBA & Writing your First VBA Macro in Excel [VBA Crash Course Part 1 of 5]")
    
*   [What is a macro and how to get started with VBA](http://chandoo.org/wp/2014/10/09/cp022-whats-a-macro-introduction-to-excel-vba-macros-automation/ "CP022: What’s a Macro? Introduction to Excel VBA, Macros & Automation")
    
*   [40+ Example VBA macros](http://chandoo.org/wp/excel-vba/examples)
    
*   Course: **[Online VBA Classes from Chandoo](http://chandoo.org/wp/vba-classes/)
    **

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [40 Comments](https://chandoo.org/wp/compare-data-highlight-mismatched-letters-words/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/compare-data-highlight-mismatched-letters-words/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [comparison](https://chandoo.org/wp/tag/comparison/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [duplicates](https://chandoo.org/wp/tag/duplicates/)
    , [Highlight](https://chandoo.org/wp/tag/highlight/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousExcel to the Next Level by Mastering Multiple Occurrences](https://chandoo.org/wp/multiple-occurrences-lookup-and-extraction/)

[NextMerry Christmas & Happy New Year 2015 \[Holiday Gift Inside\]Next](https://chandoo.org/wp/merry-christmas-happy-new-year-2015-holiday-gift-inside/)

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
    
    [Reply](https://chandoo.org/wp/compare-data-highlight-mismatched-letters-words/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/compare-data-highlight-mismatched-letters-words/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/compare-data-highlight-mismatched-letters-words/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
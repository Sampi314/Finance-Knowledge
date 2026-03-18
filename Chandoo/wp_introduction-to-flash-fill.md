# Clean data quickly with Flash Fill » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/introduction-to-flash-fill

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Clean data quickly with Flash Fill
==================================

*   Last updated on July 31, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![flash-fill-excel](https://chandoo.org/wp/wp-content/uploads/2015/07/flash-fill-excel.png)Excel has many powerful & time-saving features. **Even by Excel’s standard, Flash Fill is magical**. Introduced in 2013, Flash Fill is a rule engine to Excel’s fill logic. Every time you type something in a cell, Excel will try to guess the pattern and offers to fill up the rest of cells for you. That is some serious time saving magic.

Let’s understand what Flash Fill is and few sample use cases.

### Flash Fill, a smart rule engine

**Flash fill listens to your every key stroke and tries to guess what you are doing**. Remember [Clippy](https://en.wikipedia.org/wiki/Office_Assistant)
 from Office 97? Think of Flash Fill as Clippy’s less annoying & invisible cousin. Once Flash Fill identifies a pattern in your data entry, it offers a way to type rest of the data for you. If you accept the suggestion, the rest of the cells are automatically filled up.

Flash fill may not be a convenient option for simple patterns (like 1,3,5… or a bunch of dates or month names). But once you go beyond the realm of simple patterns, Flash Fill can be very useful.

_Especially, when it comes to cleaning data_.

### Example 1 – Extracting numbers from text

Let’s say you are looking at some text data and want to extract the number portion.

Now, there is no simple way to do this. Any formula or VBA approach can be tedious.

But see what happens when you unleash Flash Fill on this unruly data.

![flas-fill-extract-first-number-from-text](https://chandoo.org/wp/wp-content/uploads/2015/07/flas-fill-extract-first-number-from-text.gif)

### Example 2 – Extracting first name from list of names

Again, writing a formula can be tricky ( `LEFT(name, FIND(" ",name))` should work – [more here](http://chandoo.org/wp/2010/01/19/usernames-from-email-formulas/)
).

But Flash Fill is faster and simpler. Just type the first few names and let Flash Fill do its magic.

![flash-fill-extract-first-name](https://chandoo.org/wp/wp-content/uploads/2015/07/flash-fill-extract-first-name.png)

### Example 3 – Writing a bunch of formulas

Humor me with a scenario where you have customer names and you must lookup some corresponding data. Obviously you plan to [use VLOOKUP](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
 for this. But the lookup table has other plans. Instead of customer name, the lookup table has firstname-initial\_of\_lastname.  So for Bill Gates, the lookup table lists the name as Bill-G.

Of course, you can write a complex VLOOKUP. But why bother? Use Flash Fill to do the dirty work for you.

See below illustration to understand how this works.

![vlookups-written-with-flashfill](https://chandoo.org/wp/wp-content/uploads/2015/07/vlookups-written-with-flashfill.png)

Once the lookups are written, you can use FIND REPLACE (Ctrl+H) to add = at the front.

### Flash Fill tips & tricks:

*   **Press CTRL+E** to trigger flash fill. Excel will look at previously typed data and guesses the rest.
*   To ignore Flash Fill suggestion, press ESC.
*   By default, Flash Fill will be always listening and offers suggestions whenever it can. If you want to disable this, Use File > Options > Advanced and uncheck “Automatically Flash Fill” option. [Click here for a screenshot of this process](https://chandoo.org/wp/wp-content/uploads/2015/07/disable-automatic-flash-fill-howto.png)
    .

### Do you Flash Fill?

Flash Fill is a fun and powerful way to clean data and get what you want. I use it often, when dealing with complex datasets.

**What about you?** Do you Flash Fill? When do you use it? Please share your tips and use cases in the comments.

If you have never Flash Filled, go ahead and try it today. See the magic yourself and share your story in the comments.

Remember, **your comments on this post qualify for $31 amazon gift card giveaway**.

### More fun & powerful ways to fill data:

If you like Flash Fill, check out below tutorials for more powerful ways to automate data entry & cleanup processes.

*   [Unleash pattern power fill Excel auto fill](http://chandoo.org/wp/2015/01/20/unleash-the-pattern-power-with-excel-fill-quick-tip/)
    
*   [Quickly fill all blank cells in a table with data](http://chandoo.org/wp/2011/10/17/fill-blank-cells-in-a-table/)
    
*   [How to convert text to dates](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)
    

_This post is part of our [Awesome August](http://chandoo.org/wp/resources/awesome-august/)
 Excel Festival._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [42 Comments](https://chandoo.org/wp/introduction-to-flash-fill/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introduction-to-flash-fill/#respond)
    
*   Tagged under [auto fill](https://chandoo.org/wp/tag/auto-fill/)
    , [awesome august](https://chandoo.org/wp/tag/awesome-august/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [flash fill](https://chandoo.org/wp/tag/flash-fill/)
    , [keyboard shortcuts](https://chandoo.org/wp/tag/keyboard-shortcuts/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousCP040: Intro. to Power Query – What is it and how to get started – with Miguel Escobar](https://chandoo.org/wp/intro-to-power-query-podcast/)

[NextHow to create dynamic sparklines for latest 30 days Next](https://chandoo.org/wp/dynamic-sparklines/)

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
    
    [Reply](https://chandoo.org/wp/introduction-to-flash-fill/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introduction-to-flash-fill/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introduction-to-flash-fill/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
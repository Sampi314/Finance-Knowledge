# Finding if a cell has 7 in it... [Pattern matching in Excel] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/cell-has-given-number

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Finding if a cell has 7 in it… \[Pattern matching in Excel\]
============================================================

*   Last updated on October 19, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Imagine you work at MI5 as a HR officer. **You want to find all agents who have license to kill (licence 7)**. Your data looks like this:

![sample-data-pattern-match](https://chandoo.org/wp/wp-content/uploads/2016/10/sample-data-pattern-match.png)

_**How would you go about it?**_ 

If you filter the list or use FIND() or SEARCH() formulas, you will end up with agents who also have licenses 77, 17 or _not7_. So how would you solve this problem?

Of course, you do what any smart person does. You summon Excel and ask it nicely by using some wicked pattern matching logic.

### Finding all cells with 7 in them

Assuming the licenses are in column \[licenses\], you can use below formula to check if it has 7:

**Step 1:** Make an extra column, say \[Two more commas\] and use this formula.

`=", "&[@licenses]&", "`

**Step 2:** Now use below formula to find if a license has 7 in it:

`=COUNTIFS([@[Two more commas]] , "* 7,*") > 0`

This formula returns TRUE if \[@licenses\] has 7.

**So how does it work?**

There are three cases for licenses with 7 in them, as shown below.

![finding-sevens](https://chandoo.org/wp/wp-content/uploads/2016/10/finding-sevens.png)

Once we prefix & suffix COMMASPACE to this, we end up with a text that has the pattern:

`<COMMA SPACE number><COMMA SPACE number>...`

Now, we simply look for the pattern SPACE7, in this by using the \* wildcard along with COUNTIFS.

`=COUNTIFS([@[Two more commas]], "* 7,*")`

We add a check to see if the count is greater than ZERO (_ie did we find the pattern?_)

So there you go. Now you can find the agent who can nab the targets.

_Related: [Using wildcards \* ? in Excel VLOOKUP & other functions](http://chandoo.org/wp/2010/11/01/using-wildcards-with-vlookup/)
 | [Introduction to SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
_

### Adding a few plot twists

Now, your MI5 career would be awfully boring, if there are no plot twists. So Q calls you in to her office and says, _“We need a list of all agents who have any of the licenses 7, 65 or 63. Oh, while you are at it, tell me which agents have all three licenses.”_

Damn you Q  
the evil is you  
for making me do  
work I don’t want to

_Damn you Q._

_Added later:_ Okay, My James Bond knowledge is not very good. M is the boss of MI5, not Q. So let’s assume M calls you in to her office and gives you this task. As usual, you go:

Why do this M?  
Everything is ho hum  
and then you come  
to tell my work is not yumm

Why do this M?

So you are back to your desk. Now the licenses to find are in a named range called _list._ 

You can use COUNTIFS() pattern find logic to get the answer.

For sake of simplicity, let’s assume that you have a new column in your data table called as \[Two more commas\]

**Does the agent have any of the licenses in _list?_**

`=SUMPRODUCT(COUNTIFS([@[Two more commas]],"* "&list&",*"))>0`

The internal COUNTIFS returns an array of values, which the SUMPRODUCT simply adds up.

**Does the agent have all of the licenses in _list?_**

`=SUMPRODUCT(COUNTIFS([@[Two more commas]],"* "&list&",*")) = COUNTA(list)`

Now, let’s hope Q doesn’t add more plot twists. And if she does, you can always post them in the comments so internet can solve them.

_Related: [Introduction to Excel SUMPRODUCT function](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
_

### How would you find license to kill?

I am sure COUNTIFS is not the only way to do this. So what would you do in this case? Will you use formulas / VBA or Power Query? Or something else altogether? _**Go ahead and share your approach in the comments section.**_

_Note: Thanks to Brian who emailed me this problem._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [21 Comments](https://chandoo.org/wp/cell-has-given-number/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/cell-has-given-number/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [wildcards in excel](https://chandoo.org/wp/tag/wildcards-in-excel/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousCP055: “Yes, I am back” edition (and a bonus Excel tip)](https://chandoo.org/wp/cp055-yes-i-am-back/)

[NextHow many formulas should you learn? \[Weekend Poll\]Next](https://chandoo.org/wp/how-many-formulas-should-you-learn/)

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
    
    [Reply](https://chandoo.org/wp/cell-has-given-number/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/cell-has-given-number/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/cell-has-given-number/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
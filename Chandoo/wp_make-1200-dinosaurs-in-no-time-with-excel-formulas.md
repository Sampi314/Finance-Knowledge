# Make 1,200 dinosaurs in no time with Excel [formulas] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/make-1200-dinosaurs-in-no-time-with-excel-formulas

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Make 1,200 dinosaurs in no time with Excel \[formulas\]
=======================================================

*   Last updated on January 29, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

It seems spreadsheets & dinosaurs on a collision course. How else can you explain Jon’s [XKCD Velociraptor problem solved with Excel](http://peltiertech.com/solve-xkcd-velociraptor-problem-with-excel/)
 and now this. _Debby_, an alert reader of our blog sent me this email yesterday.

> I need an algebraic formula to solve this in Excel
> 
> I have 5 heads, 5 bodies, 4 arm sets, 4 leg sets and 3 tails. I need to see if I can create 1000 dinosaurs from these, and if that’s too many AND I need the 5 digit groupings to prove it and create them.  
> basically Xa\*Xb\*Xc\*Xd\*Xe=1000 – I’m not supposed to go over 1200. \[…\] And then I want the 5 digit combinations if possible – right now they are trying to do the combinations by hand – would be awesome if we could do it in Excel.

### Ladies & gentlemen, let’s fire up Excel

There are two problems to solve.

(1) How many dinosaurs can be made?

(2) Listing of all such dinosaurs.

The first one is easy.

We just multiply the number of heads, bodies, arms, legs & tails. I know this sounds biologically impossible. But in math everything is possible. So we get =5x5x4x4x3 = 1200

That means, given the body part variations, we can generate 1,200 dinosaurs. Some of them may be hideous, but 1,200 of them nevertheless.

### Making 1200 dinosaurs in Excel

This is very simple. We just use the MakeDinosaur() formula in Excel.

Of course, I am kidding. There is no MakeDinosaur(). Instead, we can use the all powerful [INDEX()](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
.

Let’s say, we have listed the various parts in a range like this:

![dinosaur-part-choices](https://chandoo.org/wp/wp-content/uploads/2016/01/dinosaur-part-choices.png)

Now, each of those ranges are conveniently named as _heads, bodies, arms, legs_ and _tails_.

![dinosaur-combinations](https://chandoo.org/wp/wp-content/uploads/2016/01/dinosaur-combinations.png)Next, in an empty column, we list 1200 running numbers. _Side note: we could do away with this step and [use ROWS() function](http://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/)
. But dinosaurs don’t mind helper columns._

Let’s say, these running numbers are in H4:H1203.

We now use our T-rex sized INDEX formula.

\=INDEX(heads,(H4-1)/240+1) & INDEX(bodies,MOD((H4-1)/48,5)+1) & INDEX(arms,MOD((H4-1)/12,4)+1) & INDEX(legs,MOD((H4-1)/3,4)+1) & INDEX(tails,MOD((H4-1),3)+1)

This generates all combinations of dinosaurs.

Let’s dissect the t-rex. Shall we?

*   The formula is a concatenation of five INDEX functions.
*   Each fetching one body part _viz_ head, body, arm, leg or tail

#### Head portion:

**Formula:** INDEX(heads,(H4-1)/240+1)

**What it does?** There are 5 head choices and 1200 possible dinosaurs. That means, each type of head is attached to 240 (1200/5 = 240) dinosaurs.

So, we simply take the number in H4, divide it with 240 and figure out which head to use.

#### Body portion:

**Formula:** INDEX(bodies,MOD((H4-1)/48,5)+1)

**What it does?** So we now have 240 possible dinosaurs with a given head. And we have 5 types of body. That means 48 dinosaurs per each type of body _given a head type._ 

We could use INDEX(bodies, MOD(H4-1,240)/48 +1) to get the corresponding body number.

Alternatively, we can use the simplified version  INDEX(bodies,MOD((H4-1)/48,5)+1)

**Why does it work?** That is for you to figure out. There is a reason we are not extinct yet.

**Remaining parts:**

We use similar logic to fetch other body parts.

### Download the dinosaurs

[Download the 1,200 dinosaurs](https://chandoo.org/wp/wp-content/uploads/2016/01/make-1200-dinos.xlsx)
. Be careful, #14321 is a bit loony. She almost bit my shift key.

### How would you make ’em dinosaurs?

Of course, we could use VBA, other formulas to make these nasty reptiles. What would you do if someone asks you create a few dinosaurs? Share your recipe in the comments.

### Stop stomping & start succeeding @ spreadsheets

Do you resort to manic stomping and rampage when a spreadsheet goes astray? Take things into control. Sharpen your spreadsheet skills. Check out below pages:

*   [Advanced Excel skills and techniques](http://chandoo.org/wp/advanced-excel-skills/)
    
*   [Important formulas for analysts](http://chandoo.org/wp/2013/01/16/top-10-formulas-for-aspiring-analysts/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [6 Comments](https://chandoo.org/wp/make-1200-dinosaurs-in-no-time-with-excel-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/make-1200-dinosaurs-in-no-time-with-excel-formulas/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [rows()](https://chandoo.org/wp/tag/rows/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousFormat charts quickly with chart styles & color themes \[quick tip\]](https://chandoo.org/wp/using-chart-styles-color-themes/)

[NextUse slicers to create a cool selection mechanism \[quick tip\]Next](https://chandoo.org/wp/use-slicers-as-selection-mechanism/)

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
    
    [Reply](https://chandoo.org/wp/make-1200-dinosaurs-in-no-time-with-excel-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/make-1200-dinosaurs-in-no-time-with-excel-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/make-1200-dinosaurs-in-no-time-with-excel-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
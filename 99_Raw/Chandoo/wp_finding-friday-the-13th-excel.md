# Finding Friday the 13th using Excel (and learning cool formulas along way) » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/finding-friday-the-13th-excel

---

*   [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Finding Friday the 13th using Excel (and learning cool formulas along way)
==========================================================================

*   Last updated on January 13, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Not that I have friggatriskaidekaphobia or anything. But since today is Friday & 13th, lets put our Excel skills to test and **find out when the next Friday the 13th is going to be**.

(trivia: [Check this for some interesting facts about Friday the 13th](http://en.wikipedia.org/wiki/Friday_the_13th)
)

Finding Next Friday the 13th using Excel Formulas – Approach 1
--------------------------------------------------------------

Lets say, you have a date in cell C3, and you want to find out when the next Friday, the 13th is going to be starting the date in cell C3.

The first approach I can think of is pretty straight forward.

![Finding Friday the 13th using Excel](https://img.chandoo.org/f/friday-13th-calculations-formula.png)We list all the 13ths in a column and find the next 13th which is also a Friday. For this,

1.  In cell E3, we write =MONTH(C3)
2.  In cell F3, we write =YEAR(C3)
3.  We use these 2 cells to refer to the month and year of the starting date.
4.  Then, we write in an empty cell =DATE($F$3,$E$3+ROWS($A$1:A1),13) – lets say this cell is E5
5.  This gives us the 13th date of next month, from the start date in cell C3.
6.  Now, lets drag this formula and fill it down, for say, next 100 cells to get next 100 _13ths_.
7.  The ROWS($A$1:A1) portion generates continuous numbers from 1 thru 100 and thus we get next 100 _13ths_.  
    For more on this technique, read – [Using ROWS() to generate a series of numbers](http://chandoo.org/wp/2009/08/17/rows-and-columns-excel-formulas/)
    

Once all the 13ths are listed, in an adjacent column, we can use WEEKDAY() formula to see if the 13th is a Friday – WEEKDAY(E5)=6

This column will have a bunch of TRUE & FALSE values.

Now to find the next Friday the 13th, we just look for TRUE value in this column (say F5:F104) use it to derive the date.

So this formula =DATE(F3,E3+MATCH(TRUE,$F$5:$F$104,0),13) should give us the next Friday, the 13th.

**Break up of above formula:**

1.  MATCH(TRUE,$F$5:$F$104,0) tells us the position of first TRUE value (_ie_ first Friday, the 13th in our list)
2.  DATE(F3,E3+Match value, 13) gives the date of next Friday, the 13th
3.  Remember, F3 contains the year and E3 the month of starting date you entered in C3.

Finding Friday the 13th, 2nd Approach
-------------------------------------

While above approach works fine, it requires a few helper columns. So I got thinking, how can we write a one shot formula that gives us next Friday, the 13th date?

**First the formula:**

_This is an array formula._

{ =DATE(YEAR($C$3), MATCH(TRUE, WEEKDAY(DATE(YEAR($C$3),MONTH($C$3)+ROW($A$1:$A$100), 13))=6,0) + MONTH($C$3),13) }

Scary formula indeed. We may have to coin a word for fear of long excel formulas – **_doubleXLformulaphophia_**.

**How does this formula work?**

Before understanding the portions of this formula, we need to understand the approach.

This formula uses similar thinking as of earlier formula. Just that it shrinks all those helper columns to an array and works the magic.

To find next Friday, the 13th, we need to list down next few 13ths and check which one is a Friday. Since Excel lookup formulas always return the first match, we find the first such Friday.

**Parts of the formula:**

*   To get the next 100 13ths, we use, DATE(YEAR($C$3),MONTH($C$3)+ROW($A$1:$A$100), 13)

When used in an array formula, this gives us the 13th days of next 100 months.

(aside: technically, we do not need next 100 months. As per Wikipedia, the maximum gap between successive Friday, the 13ths is 14 months. [_more_](http://en.wikipedia.org/wiki/Friday_the_13th#Occurrence)
)

Also, note that we are using ROW() formula, not ROWS(), as we want all the row numbers for first 100 rows as an array.

*   Once we have these 100 dates, we just check for their Friday_ness_ with, WEEKDAY(100 dates))=6

This formula returns a 100 TRUE & FALSE values. TRUE, whenever the date is a Friday, FALSE, when it is not.

*   Then, we find the first TRUE value (_ie_ first occurrence of Friday, the 13th in next 100 months) with, MATCH(TRUE, next 100 dates’ Friday_ness_, 0)

This gives us the position of next TRUE value.

*   Finally, we use that to construct the date of next Friday, the 13th – DATE(YEAR($C$3), MONTH($C$3) + first TRUE value, 13)

**And that is how we find the next Friday the 13th based on the start date in cell C3**.

### Important Note:

Both approaches only search for Friday, the 13th starting next month of the date in C3. If C3 has a date prior to 13th and the 13th of that month is a Friday, the 13th, it would not be considered. For example, if you enter 10-JAN-2012 in C3, both formulas would find next Friday the 13th as April 13, 2012 **_not Jan 13, 2012_**.

Download Friday, the 13th Example Workbook
------------------------------------------

I have made a colorful (and almost gory) download workbook. Even if you do not want to learn this, I suggest downloading the file, for fun!

[**Click here to download**](https://img.chandoo.org/d/friday-13th-formulas.xlsx)
 the Friday, 13th calculations workbook & play with it.

Bonus: It has homework too!

Your Homework
-------------

Finally some homework to wrap up this week.

_Write a formula to find the maximum gap between consecutive Friday, the 13ths in next 5 years, from a starting date in cell C3._

Please post your answers in comments so that we all can learn.

Checkout more Formula Forensics
-------------------------------

Once in a while, we take a complex real world (or as in this case, gory world) problem and write an equally scary formula. Then, we go great lengths breaking it down and explaining it. We call this as Formula Forensics. Much like forensics in CSI, without ultra zoom & hot chicks. You can check out some of our recent adventures here:

1.  [Using an array formula to count maximum occurrences of a text](http://chandoo.org/wp/2011/10/31/using-array-formulas-to-find-count/)
    
2.  [Counting specific words in a multi-cell range](http://chandoo.org/wp/2011/11/07/formula-forensics-002/)
    
3.  [Extracting a list of items from a larger list by criteria](http://chandoo.org/wp/2011/11/18/formula-forensics-003/)
    
4.  … [More formula forensics](http://chandoo.org/wp/category/formula-forensics/)
    

PS: It is also Hui’s birthday today. Lets wish him many more years of fun, happiness & Excel craze.

PPS: Finding his next birthday is going to be simple, we just write =DATE(2013,1,13) 😛

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [22 Comments](https://chandoo.org/wp/finding-friday-the-13th-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/finding-friday-the-13th-excel/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [month](https://chandoo.org/wp/tag/month/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [rows()](https://chandoo.org/wp/tag/rows/)
    
*   Category: [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousAnnouncing Online VBA Classes from Chandoo.org, Please Join Today](https://chandoo.org/wp/join-vba-classes/)

[NextSix Quick UpdatesNext](https://chandoo.org/wp/six-quick-updates/)

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
    
    [Reply](https://chandoo.org/wp/finding-friday-the-13th-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/finding-friday-the-13th-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/finding-friday-the-13th-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
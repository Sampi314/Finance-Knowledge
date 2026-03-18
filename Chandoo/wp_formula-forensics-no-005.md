# Zebra Stripes and Checker-Board - Conditional Formatting

**Source:** https://chandoo.org/wp/formula-forensics-no-005

---

*   [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensics No. 005 – Zebras and Checker-Boards
=====================================================

*   Last updated on December 12, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

This week in Formula Forensics we’ll look at, Zebra Stripes and Checker-board Conditional Formatting.

This idea is inspired by a number of posts over the past few years asking about zebra stripes but specifically BobR who in in June 2011, also asked about Checkerboards in the post: [Want to be an excel conditional-formatting Rock Star](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/ "Excel Conditional Formatting")
, Comment No. 154.

_I got the conditional format for alternating row and column colors,_

_Is there a conditional format to make it a checkerboard whereas the cell A2 will remove either the conditional for the row or column and then alternately to A4, B1, B3 etc?_

Chandoo responded fairly quickly with this Conditional Formatting formula:

\=IF(MOD(ROW(),2)=1,MOD((ROW()-1)\*8+COLUMN(),2)=0,MOD((ROW()-1)\*8+COLUMN(),2)=1)

Unbeknownst to Chandoo I posted this about a minute later:

\=ISODD(ROW()+COLUMN())

Both formula correctly answer BobR’s question.

So today we’re going to pull apart Zebra Stripes and Checker Boards and see what makes them tick.

As always you can follow along in a download file here: [Download File](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebras-and-Checker-boards.xls "Zebras and Checker-board Download")
.

ZEBRA STRIPES
-------------

Zebra Stripes as Conditional Formatting is simply applied using a simple formula within Conditional Formatting.

\=MOD(ROW(),2)=0

Conditional Formatting requires a formula that returns a boolean “True” to apply a format or a Boolean “False” to not Apply a format.

So the formula is better read as: If MOD(ROW(),2)=0

And  If MOD(ROW(),2)=0, the formula will evaluate as True

This is best evaluated as 3 columns on a worksheet.

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebra1.png "Zebra1")](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebra1.png)

In cells

**B5:B10** The formula \=Row() returns the Row Number

**C5:C10** The formula \=Mod(Row() ,2) returns the Mod of Row Number, divided by 2

The Mod function returns the remainder of the division of the Row Number divided by 2,

So in Row 5, Mod(Row(),2) = Mod(5, 2) = 5/2 = 2 Remainder 1 = 1

and in Row 6, Mod(Row(),2) = Mod(6, 2) = 6/2 = 3 Remainder 0 = 0

**D5:D10** The formula \=Mod(Row() ,2)=0 checks the remainder against the value 0

This is what evaluates to either True or False depending on the Row number.

Where the Values are True the Format will be applied (Even Rows)

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebra2.png "Zebra2")](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebra2.png)

The Conditional Formatting can be applied to Odd Rows If the Formula is slightly altered

\=Mod(Row() ,2)=1

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebra3.png "Zebra3")](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebra3.png)

Similarly the formatting can be applied to Columns using

\=MOD(COLUMN(),2)=0/1

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebra4.png "Zebra4")](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebra4.png)

CHECKER BOARDS
--------------

RobR received two responses to his Checker-Board Conditional Formatting request.

\=IF(MOD(ROW(),2)=1,MOD((ROW()-1)\*8+COLUMN(),2)=0,MOD((ROW()-1)\*8+COLUMN(),2)=1)

and

\=ISODD(ROW()+COLUMN())

Lest see what’s inside these two formula.

\=IF(MOD(ROW(),2)=1,MOD((ROW()-1)\*8+COLUMN(),2) =0, MOD( (ROW() -1)\*8+COLUMN(),2)=1)
--------------------------------------------------------------------------------------

This is a simple If Formula with 3 components

\=IF(MOD(ROW(),2)=1,MOD((ROW()-1)\*8+COLUMN(),2)=0,MOD((ROW()-1)\*8+COLUMN(),2)=1)

If Condition        MOD(ROW(),2)=1

Value if True:     MOD((ROW()-1)\*8+COLUMN(),2)=0

Value if False:    MOD((ROW()-1)\*8+COLUMN(),2)=1

The If Condition is already known to us, as it’s the same formula used in the Zebra Stripes above.

It evaluates to True when it is on an Odd Row.

So when it is an Odd numbered Row Excel will look at MOD((ROW()-1)\*8+COLUMN(),2)=0

And when it is an Even numbered Row Excel will look at MOD((ROW()-1)\*8+COLUMN(),2)=1

We can notice that these are the same formulas which have a different ending of \=0 and \=1

MOD((ROW()-1)\*8+COLUMN(),2)=0

This section Takes each Row subtracts 1 and then multiplies this number by 8. This can be expressed as simply as saying multiply the Row \* 8.

This will always return an Even Number and could have been simplified to Row()\*2

MOD((ROW()-1)\*8+COLUMN(),2)=0

The next bit adds the column number to the previous Even Number.

So now this part will be Odd when the column is Odd and Even when the column is Even.

MOD((ROW()-1)\*8+COLUMN(),2)=0

The remainder of the formula is the same as the Zebra Stripes formula.

An Odd Number (Odd Columns) in the section above will return a 1 as the result of =Mod(Odd,2)

An Even Number (Even Columns) in the section above will return a 0 as the result of =Mod(Odd,2)

When evaluated against 0 will return True for Even Columns and False for Odd Columns.

Now the exact same happens in the False section of the If formula except that it is evaluated against 1.

\=ISODD(ROW()+COLUMN())
-----------------------

I tackled this problem from a different direction to Chandoo.

Knowing that Even + Even = Even and Even + Odd = Odd and that the row and Column Numbers increase in each direction by 1 each Row/Column, it was simply a matter of adding the Row and Column numbers together and checking if it was Odd or Even

The Excel function IsOdd() and IsEven() both return a Boolean “True” if the contents are Odd or “Even” respectively. This negates an external truth check as described above.

This is easily shown by adding a formula to the Checker area

\=Row()+Column()

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/CheckerHui1.png "CheckerHui1")](https://chandoo.org/wp/wp-content/uploads/2011/12/CheckerHui1.png)

**Excel 2003**: The above formula won’t work in Excel 2003.

Try this instead =Mod(Row()+Column(),2)=1

  

If the alternate shading is required a switch to

\=ISEVEN(ROW()+COLUMN())

Does the trick.

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/CheckerHui2.png "CheckerHui2")](https://chandoo.org/wp/wp-content/uploads/2011/12/CheckerHui2.png)

**Excel 2003**: The above formula won’t work in Excel 2003.

Try this instead \=Mod(Row()+Column(),2)=0

  

Learn More About Conditional Formatting Here:
---------------------------------------------

[http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)

and

[http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)

and

[http://chandoo.org/wp/2008/10/14/more-than-3-conditional-formats-in-excel/](http://chandoo.org/wp/2008/10/14/more-than-3-conditional-formats-in-excel/)

DOWNLOAD
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2011/12/Zebras-and-Checker-boards.xls "Zebras and Checker-board Download")
.

**OTHER POSTS IN THIS SERIES**
------------------------------

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensics 001](http://chandoo.org/wp/2011/10/31/using-array-formulas-to-find-count/ "Taruns problem")
 – Tarun’s Problem

[Formula Forensics 002](http://chandoo.org/wp/2011/11/07/formula-forensics-002/ "Joyces' Question")
 – Joyce’s Question

[Formula Forensics 003](http://chandoo.org/wp/2011/11/18/formula-forensics-003/ "Lukes Reward")
 – Lukes Reward

[Formula Forensics 004](http://chandoo.org/wp/2011/11/30/formula-forensics-no-004/ "Freds Problem")
 – Freds Problem

We Need Your Help !
-------------------

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post as Luke did in [Formula Forensics 003](http://chandoo.org/wp/2011/11/18/formula-forensics-003/ "Formula Forensics 003")
. or this post.

If you have a formula that you don’t understand and would like explained but don’t want to write a post also send it in to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
 or [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [17 Comments](https://chandoo.org/wp/formula-forensics-no-005/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-no-005/#respond)
    
*   Tagged under [Check-Board](https://chandoo.org/wp/tag/check-board/)
    , [column()](https://chandoo.org/wp/tag/column/)
    , [if()](https://chandoo.org/wp/tag/if/)
    , [iseven()](https://chandoo.org/wp/tag/iseven/)
    , [IsOdd()](https://chandoo.org/wp/tag/isodd/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [row()](https://chandoo.org/wp/tag/row/)
    , [Zebra Stripes](https://chandoo.org/wp/tag/zebra-stripes/)
    
*   Category: [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousIntroduction to Spreadsheet Risk Management](https://chandoo.org/wp/spreadsheet-risk-management-introduction/)

[NextLearn Any Area of Excel using these 80 LinksNext](https://chandoo.org/wp/learn-excel-by-topic/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-005/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-005/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-005/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
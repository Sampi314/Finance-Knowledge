# INDEX Formula in Excel - How to use it, tips & examples

**Source:** https://chandoo.org/wp/index-formula-usage-and-tips

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

7 reasons why you should use INDEX() formula in Excel
=====================================================

*   Last updated on February 11, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Of all the hundreds of formulas & thousands of features in Excel, INDEX() would rank somewhere in the top 5 for me. It is a versatile, powerful, simple & smart formula. Although it looks plain, it can make huge changes to the way you analyze data, calculate numbers and present them. It is so important that, whenever I teach (live or online), I usually dedicate 25% of teaching time to INDEX().

Today lets get cozy. Lets start a fling (a very long one). Lets do something that will make you smart, happy and relaxed.

![INDEX formula - Usage, examples & Tips](https://img.chandoo.org/f/index-formula-usage-tips.jpg)

Understanding INDEX formula
---------------------------

In simple terms, INDEX formula gives us value or the reference to a value from within a table or range.

While this may sound trivial, once you realize what INDEX can do, you would be madly in love with it.

### Few sample uses of INDEX

1\. Lets say you are the star fleet commander of planet zorg. And you are looking at a list of your fleet in Excel (even in other planets they use Excel to manage data). And you want to get the name of 8th item in the list.

INDEX to rescue. Write =INDEX(list, 8)

2\. Now, you want to know the captain of this 8th ship, which is in 3rd column. You guessed right, again we can use INDEX,

\=INDEX(list, 8,3)

### Syntax of INDEX formula

INDEX has 2 syntaxes.

1\. INDEX(range or table, row number, column number)

_This will give you the value or reference from given range at given row & column numbers._

2\. INDEX(range, row number, column number, area number)

_This will give you the value or reference from specified area at given row & column numbers._

It may be difficult to understand how these work from the syntax definition. Read on and everything will be clear.

7 reasons why INDEX is an awesome companion
-------------------------------------------

Whether you are in planet zorg managing dozens of star fleet or you are in planet earth managing a list of vendors, chances are you are wrestling everyday with data, pleasing a handful of managers (and clients), delivering like a rock star all while having fun. That is why you should partner with INDEX. It can make you look smart, resourceful and fast, without compromising your existing relationship with another human being.

### Data used in these examples

For all these examples (except #6), we will use below data. It is in the table named _sf._

![Data used in INDEX formula examples](https://img.chandoo.org/f/index-examples-data.png)

### Reason 1: Get nth item from a list

You already saw this in action. INDEX formula is great for getting nth item from a list of values. You simply write =INDEX(list, n)

### Reason 2: Get the value at intersection of given row & column

Again, you saw this example. INDEX formula can take a table (or range) and give you the value at nth row, mth column. Like this =INDEX(table, n, m)

### Reason 3: Get entire row or column from a table

For some reason you want to have the entire or column from a table. A good example is you are analyzing star fleet ages and you want to calculate average age of all ships.

You can write =AVERAGE(age column)

or you can also use INDEX to generate the age column for you. _Assuming the fleet table is named **sf** and age is in **column 7**_

write =AVERAGE(INDEX(sf, ,7))

Notice empty value for ROW number. When you pass empty or 0 value to either row or column, INDEX will return entire row or column.

Likewise, if you want an entire row, you can pass either empty or 0 value for column parameter.

### Reason 4: Use it to lookup left

By now you know that [VLOOKUP()](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
 cannot fetch values from columns to left. It does not matter if the person looking up is _the_ star fleet commander.

But INDEX along with MATCH can fix this problem.

Lets say you want to know which ship has maximum capacity.

1.  First you find what is the maximum capacity =MAX(sf\[Capacity (000s tons)\])
2.  Then you find position of of this capacity in all values =MATCH(max\_capacity, sf\[Capacity (000s tons)\],0)
3.  Now, extract the corresponding ship name =INDEX(sf\[Ship Name\], max\_capacity\_position)

Or in one line, the formula becomes

\=INDEX(sf\[Ship Name\], MATCH( MAX(sf\[Capacity (000s tons)\]), sf\[Capacity (000s tons)\], 0))

For more tips read [using INDEX + MATCH combination](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)

### Reason 5: Create dynamic ranges

So far, your reaction to INDEX’s prowess might be ‘meh!’. And that is understandable. You are of course star fleet commander and it is difficult to please you. But don’t break-up with INDEX yet.

You see, the true power of INDEX lies in its nature. While you may think INDEX is returning a value, the reality is, INDEX returns a reference to the cell containing value.

So this means, a formula like =INDEX(list, 8) looks like it is giving 8th value in list.

But it is really giving a reference to 8th cell.

Since the result of INDEX is a reference, we can use INDEX in any place where we need to have a reference.

_Sounds confusing?_

For example, to sum up a list of values in range A1:A10, we write =SUM(A1:A10)

Now, in that formula, both A1 and A10 are _**references**_.

Since INDEX gives a reference, we can replace either (or both) A1 & A10 with INDEX formula and it still works.

so =SUM(A1 : INDEX(A1:A50,10))

will give the same result as =SUM(A1:A10)

Although the INDEX route appears overly complicated, it has other applications.

**Example 1: SUM of staff in first x ships**

Lets say you want to sum up staff in first ‘x’ ships in the sf table.

Since ‘x’ changes from time to time, you want a dynamic range that starts from first ship and goes up to _xth_ ship.

Assuming ‘x’ value is in cell M1 and first ship’s staff is in cell G3,

\=SUM(G3:INDEX(sf\[Staff count\], M1))

will give the desired result.

**Example 2: A named range that refers to all ship names in column A**

Many times you do not know how much data you have. Even star fleet commanders are left in dark. Lets say you are building a new ship tracking spreadsheet. Since your fleet is ever growing, you do not want to constantly update all formulas to refer to correct ranges.

_For example,_ the ship names are in column A, from A1 to A_n_. And you want to create a named range that points to all ships so that you can use this name elsewhere.

If you define the lstShips =A1:A10, then after you add 11th ship, you must edit this name. And you hate repetitive work.

One solution is to [use OFFSET formula](http://chandoo.org/wp/2012/09/17/offset-formula-explained/)
 to define the dynamic range,

like =OFFSET(A1, 0,0, COUNTA(A:A),1)

While this works ok, since OFFSET is volatile function, it will recalculate every time something changes in your workbook. Even when someone replaces a bolt on landing gear of USS Enterprise.

This will eventually make your workbook slow.

That is where INDEX comes.

You see, INDEX is a non-volatile function\*.

So you can create lstShips that points to,

\=A1: INDEX(A:A, COUNTA(A:A))

\*Even though INDEX is non-volatile, since we are using it in defining a range reference, Excel recalculates the lstShips every time you open the file. ([reference](http://www.excelhero.com/blog/2011/03/the-imposing-index.html)
).

### Reason 6: Get any 1 range from a list of ranges

INDEX has another powerful use. You can get any one range from many ranges using INDEX.

Since you are a successful, smart & resourceful star fleet commander, you got promoted. Now you manage fleet of several planets.

And you have similar ship detail tables for each planet in a workbook. And you want to calculate average age of any planet’s ships with just _one formula_.

Again INDEX to rescue.

![Using INDEX formula to get one of many ranges](https://img.chandoo.org/f/index-formula-used-to-get-one-of-many-ranges.png)

Assuming you have 3 different tables – planet1, planet2, planet3

and selected planet number is in cell C1,

write =AVERAGE(INDEX((planet1,planet2,planet3),,,C1))

The reference (planet1,planet2,planet3) will point to all data and C1 will tell INDEX which planet’s data to use.

_Pretty nifty eh?!?_

### Reason 7: INDEX can process arrays

INDEX can naturally process arrays of data (without entering CTRL+Shift+Enter).

For example you want to find out how much staff is in the ships whose captain’s name starts with “R”.

write =SUM(INDEX((LEFT(sf\[Captain\],1)=“r”)\*(sf\[Staff count\]),0))

Although LEFT(sf\[Captain\],1)=”r” and sf\[Staff count\] produce arrays, since INDEX can process arrays automatically, the result comes without CTRL+Shift+Enter

_Where as if you use SUM alone =SUM((LEFT(sf\[Captain\],1)=”r”)\*(sf\[Staff count\])) you have to press CTRL+Shift+Enter_ to get correct results.

**Other formulas: SUMPRODUCT & MATCH too can process arrays automatically.**

Download Example Workbook & Get close with INDEX
------------------------------------------------

Since you are going to ask, “I want to spend sometime alone with INDEX in my cubicle right now!”, I made an example workbook. It explains all these powerful uses of INDEX. [**Go ahead and download it**](https://img.chandoo.org/f/index-examples.xlsx)
.

Get busy with INDEX.

How to use INDEX in Excel – Video
---------------------------------

In this video, learn how to use INDEX formula in Excel with many real-world examples. You can also [watch it here](https://youtu.be/kly0uPIM4IU)
.

Why do you love INDEX?
----------------------

I love INDEX(). If we get a dog, I am going to call her INDEX.

Updated on Feb 2024: We did get a dog, but we call her Excel!

That is how much I love the formula. Almost all my dashboards, complex workbooks and anything that seems magical will have a fair dose of INDEX formulas.

**What about you?** Do you use INDEX formula often? What are the reasons you love it? Please share your tips, usages and ideas on INDEX using comments.

### Learn more about INDEX & other such lovely things in Excel

If you are whistling uncontrollably after reading so far, you are in for a real treat. Check out below articles to become awesome.

*   [INDEX + MATCH Combination](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
    
*   [Introduction to SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
    
*   [Dynamic Array formulas](https://chandoo.org/wp/dynamic-array-functions/)
     in Excel (especially FILTER) is a good alternative to INDEX
*   [XLOOKUP formula](https://chandoo.org/wp/xlookup-examples/)
     can do much more than INDEX
*   More examples of [advanced Excel formulas](http://chandoo.org/wp/formula-forensics-homepage/)
     & [INDEX](http://chandoo.org/wp/tag/index/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [89 Comments](https://chandoo.org/wp/index-formula-usage-and-tips/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/index-formula-usage-and-tips/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousUsing Arrays To Update Table Columns](https://chandoo.org/wp/using-arrays-to-update-table-columns/)

[NextHow to Solve an Equation in ExcelNext](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/index-formula-usage-and-tips/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/index-formula-usage-and-tips/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/index-formula-usage-and-tips/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# Modeling tiles in a room using Excel Conditional Formatting » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/modeling-tiles-in-a-room-using-excel-conditional-formatting

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Modeling tiles in a room using Excel Conditional Formatting
===========================================================

*   Last updated on April 22, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Last week we learned how to answer questions like, “[How many tiles in a room?](http://chandoo.org/wp/2014/04/14/feet-inches-arithmetic-in-excel/ "Multiplying 24ft 9inches with 6ft 3inches using Excel")
” using Excel. We learned about CONVERT function and fraction number format settings in Excel.

**But why stop at calculation?** We can even **model a room full of tiles**, thanks to Excel’s grid nature.

So today, we will learn how to create a room layout like this using Excel:

![Demo of Tiles in a room Excel model](https://img.chandoo.org/cf/tiles-in-a-room-model-using-excel-demo.gif)

_**If you like the demo, read on to learn.**_

### Step 1: Set up input cells

![Inputs for room & tiles model in Excel](https://img.chandoo.org/cf/floor-tiles-model-inputs.png)To model tiles in a room, we need 4 inputs. Lets call them by below names.

*   room.length
*   room.width
*   tile.length
*   tile.width

### Step 2: Calculate number of tiles required

The basic formula for calculating total tiles required is this:

\=ROUNDUP((room.length\*room.width)/(tile.length\*tile.width), 0)

_But this formula yields in an unrealistic solution_ as we do not want to have fractional tiles everywhere. So, a better way to calculate this is,

\=ROUNDUP(room.length / tile.length,0) \* ROUNDUP(room.width / tile.width,0)

Although this formula is technically correct, **you may save a few tiles if you rotate the them**.

That is,

ROUNDUP(room.length / tile.width,0) \* ROUNDUP(room.width / tile.length,0) can be smaller than ROUNDUP(room.length / tile.length,0) \* ROUNDUP(room.width / tile.width,0) in some cases, as shown in above demo.

**So we need a way to flip tile dimensions if that saves us a few bucks**. That is done by,

### Step 3: Flipping tile dimensions with a switch

Insert a check box and link to a blank cell, say F6.

\[Related: [How to use a check box in Excel](http://chandoo.org/wp/2011/03/30/form-controls/#check-box)\
\]

Now, using F6 value (either TRUE or FALSE), flip the values of tile.length & tile.width using IF() formula.

### Step 4: Create a 100×100 grid

Although you can model the floor plan of entire Buckingham palace in Excel, lets restrict ourselves to rooms of size 100×100.

Select 101 columns and resize them small enough so you can see all of them in a single screen, like 10 pixels wide.

Select 101 rows and adjust their height so that you can see as many of them as possible in a single screen (10 pixels tall should do).

Type running numbers in first column & row. The final grid looks this this:

![Floor tiles model in Excel by setting up 100x100 cell grid](https://img.chandoo.org/cf/floor-tiles-grid.png)

### Step 5: Modeling the room layout using conditional formatting

So we have a big 100×100 grid where we need to draw

*   Outer boundary for the room as per room.length & room.width
*   Inner tile boundaries as per tile.length & tile.width

**Set up conditional formatting rules for room boundary**

There are 4 rules required.

1.  Draw vertical left border if the topmost row = 1
2.  Draw vertical right border if the topmost row = room.length
3.  Draw horizontal top border if the left-most column = 1
4.  Draw horizontal bottom border if the left-most column = room.width

Below, see one of the rules.

![Conditional formatting rule for room boundary explained](https://img.chandoo.org/cf/floor-tiles-model-conditional-formatting-rule-for-room-boundary-explained.png)

You can find other conditional formatting rules in the downloadable workbook.

### Step 6: Modeling Tiles using conditional formatting

While we need 4 rules for the room boundary, we just need 2 rules for tile boundaries.

1.  Draw vertical right border if the topmost row value is divisible by tile.length
2.  Draw horizontal bottom border if the left-most column value is divisible by tile.width

_We do **not need rules for vertical left border or horizontal top border** because they will be drawn by previous tile._

See one of the rules below:

![Conditional formatting rule for tile borders explained](https://img.chandoo.org/cf/floor-tiles-model-conditional-formatting-rule-for-tile-boundary-explained.png)

That’s all. Our room model is ready. Go ahead and see how it looks when tile it.

### Download Example Workbook

[**Click here to download room tiles model workbook**](https://img.chandoo.org/cf/modeling-a-room-for-tiles.xlsx)
 and play with it. Examine the conditional formatting rules to understand it better.

### Do you apply Conditional Formatting in such creative ways?

I personally think conditional formatting is as good as honey, mangoes or dark chocolate. I love to use a dollop of it in all my Excel recipes.

**What about you?** Do you use conditional formatting for anything out-of-box 😉 like this? **Please share your tips using comments.**

### Want more? Check out these conditional formatting examples

If you want more on conditional formatting you are in luck. Check out,

*   [Gantt chart using Excel conditional formatting](http://chandoo.org/wp/2009/06/16/gantt-charts-project-management/)
    
*   [Baby feeding schedule using conditional formatting](http://chandoo.org/wp/2009/10/12/baby-feeding-chart/ "Baby Feeding Chart using Excel")
    
*   [Todo list using Excel conditional formatting](http://chandoo.org/wp/2013/01/07/todo-list-with-priorities/)
    
*   [Making data entry forms awesome with conditional formatting](http://chandoo.org/wp/2011/02/07/data-entry-forms-with-conditional-formatting-and-validation/)
    
*   [Searching data using conditional formatting](http://chandoo.org/wp/2009/03/31/search-with-conditional-formatting/)
    
*   [Market segmentation charts with conditional formatting](http://chandoo.org/wp/2009/02/18/market-segmentation-charts-excel/)
    
*   More examples on [conditional formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [16 Comments](https://chandoo.org/wp/modeling-tiles-in-a-room-using-excel-conditional-formatting/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/modeling-tiles-in-a-room-using-excel-conditional-formatting/#respond)
    
*   Tagged under [Check Box](https://chandoo.org/wp/tag/check-box/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [roundup](https://chandoo.org/wp/tag/roundup/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousThere are Easter Eggs in this Excel file!!!](https://chandoo.org/wp/easter-eggs-2014/)

[NextCP006: How to be a better analyst? – Road map for getting better at Data Analysis & Improving your career prospectsNext](https://chandoo.org/wp/cp006-become-better-analyst/)

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
    
    [Reply](https://chandoo.org/wp/modeling-tiles-in-a-room-using-excel-conditional-formatting/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/modeling-tiles-in-a-room-using-excel-conditional-formatting/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/modeling-tiles-in-a-room-using-excel-conditional-formatting/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
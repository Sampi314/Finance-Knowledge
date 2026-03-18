# Print Housie Tickets Free - Excel Template for Housie Tickets (Bingo Tickets)

**Source:** https://chandoo.org/wp/bingo-housie-ticket-generator-excel

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Bingo / Housie Ticket Generator in Excel
========================================

*   Last updated on November 4, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![generate-bingo-tickets-in-excel](https://chandoo.org/wp/wp-content/uploads/2008/07/generate-bingo-tickets-in-excel.gif "generate-bingo-tickets-in-excel")I am fascinated by board games. They provide immense fun, anyone can enjoy them, they are unpredictable and best of all they are great value for money. That is why whenever I get sometime I experiment with simulating games to know them better \[read [Why Monopoly board game is not as random as it appears](http://chandoo.org/wp/2007/02/25/is-monopoly-fair/)\
\]. So, out of curiosity I have created an excel sheet that can generate bingo / housie (housey) tickets – 24 of them at a time. To get new set of tickets you would hit F9 (recalculate).

**[Click here to download the bingo / housie ticket generator](https://chandoo.org/wp/wp-content/uploads/2019/11/bingo-housie-ticket-generator-excel-sheet.xlsx)
.**

Note that these are Bingo UK / India / Australia variant I am talking about, not the US 5\*5 type of bingo tickets.

**Read on if you want to know how this is done:**

According to [Wikipedia:](http://en.wikipedia.org/wiki/Bingo_(UK))

> A typical housie/bingo ticket .., contains fifteen numbers, arranged in nine columns by three rows. Each row contains five numbers and four blank spaces. Each column contains either one, two, or very rarely three, numbers:
> 
> \* The first column contains numbers from 1 to 9,  
> \* The second column numbers from 10 to 19,  
> \* The third 20 to 29 and so on up until the last column, which contains numbers from 80 to 90.

I have removed number “90” from the list in order to reduce some complexity in generating the tickets.

The problem is now to “generate 15 random number between 1 to 89 and fill them in 15 random spots in a grid of 3 rows by 9 columns such that each row has exactly 5 numbers”

Now I could write a function in VBA to do this, but I wanted to do this _only_ using formulas. So I started breaking the problem.

### The first challenge is to select any random 5 cells in a 9 cell row

Once we select any random 5 cells in a 9 cell row, we will fill them with bingo numbers. Now, excel has a function to generate random numbers between 1 to 9 (`=round(rand()*9,0)`), but this is not good for us since each time we call this function we will get a random number between 1 to 9, where as we need a 5 random numbers without repetition between 1 to 9. The function is _memoryless_ and could repeat numbers when called 5 times.

Instead we can list all the possible “5 cells with numbers and others are empty” [combinations](http://betterexplained.com/articles/easy-permutations-and-combinations/)
 of a 9 cells region and select a random combination every time. There are essentially 9C5 i.e. 126 ways in which you can select any 5 cells out of 9 cells (_without repetition of course_).

So I listed all these combinations in a table and then randomly selected one of the combinations. You can see the first five such combinations in the image below:

![Selecting any five cells out of nine cells](https://chandoo.org/wp/wp-content/uploads/2008/07/combinations-9c5-selecting-any-five-cells-out-of-9.gif "combinations-9c5-selecting-any-five-cells-out-of-9")

Selecting any five cells out of nine cells

Now I created a 3\*9 region and filled the cells with 1s or 0s, “1” when the cell in bingo ticket is supposed to have a value and “0” if the cell is empty as shown below:

![raw-3-by-9-bingo-cell-grid-in-excel](https://chandoo.org/wp/wp-content/uploads/2008/07/raw-3-by-9-bingo-cell-grid.gif "raw-3-by-9-bingo-cell-grid")

### Next challenge is to show random values in each cell

The trick here is that first column in our 3\*9 bingo ticket has any number(s) from 1 to 9, second column has any number(s) from 10 to 19 …

Again, the challenge is the numbers should not repeat, otherwise we could simply use `rand()*10, rand()*10+10, rand()*10+20 ...` to generate the numbers.

This time it gets even more trickier because each column can have either no values, or 1 value or 2 values or 3 values.

The ticket generation logic now looks like:

*   If the column has no values in it, then we will leave all the cells in that column of bingo ticket empty
*   If the column has 1 value, we will generate any random number from that column’s range of possible values (1-9, 10-19,20-29,…80-89) and place it in the cell that is supposed to have a value and leave other cells empty.
*   If the column has 2 values, we will generate 2 random numbers without repetition from that column’s range of possible values and place them in cells that are supposed to have them
*   If the column has 3 values, we will generate 3 random numbers without repetition from that column’s range of possible values and place them in cells that are supposed to have them

As you can see, it is easy when the column has no or 1 value in it. But when the column has 2 or 3 I used the combinations trick described earlier.

First I created all 2 number combinations and 3 number combinations. Since the numbers on Bingo ticket are always sorted from top to bottom in a column, I just had to list down 45 combinations (10C2) for 2 numbers and 120 combinations (10C3) for 3 numbers.

The rest of the details are small enough that I can leave them to your imagination. So when the ticket is generated, it looks like this:

![final-bingo-housey-ticket-printed-using-excel](https://chandoo.org/wp/wp-content/uploads/2008/07/final-bingo-housey-ticket-printed-using-excel.gif "final-bingo-housey-ticket-printed-using-excel")

Remember to [download housie / bingo ticket generator excel sheet and print your tickets at home](https://chandoo.org/wp/wp-content/uploads/2019/11/bingo-housie-ticket-generator-excel-sheet.xlsx)
. Just F9 to generate new set of tickets. _Un-hide the rows from 43 if you want to see how this is done._

Like this post: [Join our newsletter](https://chandoo.org/wp/subscribe/)
 to get more yummy Excel stuff.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [118 Comments](https://chandoo.org/wp/bingo-housie-ticket-generator-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/bingo-housie-ticket-generator-excel/#respond)
    
*   Tagged under [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [bingo](https://chandoo.org/wp/tag/bingo/)
    , [board games](https://chandoo.org/wp/tag/board-games/)
    , [fun](https://chandoo.org/wp/tag/fun/)
    , [games](https://chandoo.org/wp/tag/games/)
    , [hacks](https://chandoo.org/wp/tag/hacks/)
    , [housie](https://chandoo.org/wp/tag/housie/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [numbers](https://chandoo.org/wp/tag/numbers/)
    , [spreadsheet](https://chandoo.org/wp/tag/spreadsheet/)
    , [technology](https://chandoo.org/wp/tag/technology/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousIncell Bar charts – Revisited](https://chandoo.org/wp/incell-bar-charts-revisited/)

[NextWorst bar chart ever? – World’s Most Expensive Places to Have SxxNext](https://chandoo.org/wp/worst-bar-chart-ever/)

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
    
    [Reply](https://chandoo.org/wp/bingo-housie-ticket-generator-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/bingo-housie-ticket-generator-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/bingo-housie-ticket-generator-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
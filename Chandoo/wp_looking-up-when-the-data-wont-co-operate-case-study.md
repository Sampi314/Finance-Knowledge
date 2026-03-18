# Looking up when the data won't co-operate (case study) » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study

---

*   [Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Looking up when the data won’t co-operate (case study)
======================================================

*   Last updated on November 4, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Occasionally we deal with data that is so uncooperative that we might as well give up and go back to calculators & ledger books.

Recently I found myself in such a situation and learned something new.

### Introducing … data that won’t play nice

Drum roll please. Here is a data-set that I got from somewhere.

![2D Lookup problem - Example dataset](https://img.chandoo.org/f/2d-lookup-problem-data-structure.png)

### The problem – build a lookup formula

And the problem. Oh, simple. Write a lookup formula to find how many customer walk-ins we have on any given day.

_**But how?**_

After wrestling with a few variations of VLOOKUP, INDEX, MATCH, OFFSET… I found the right formula for this occasion.

### SUMIFS Formula

That’s right, the good old (well, its just 7 years old, born in 2007 Excel) is the one that works in this situation.

Assuming our data is in the range:

*   B4:H15
*   Even rows (4,6,8…14) containing date
*   Odd rows (5,7,9…) containing customer walk-ins
*   And lookup date is in L5

We can use this SUMIFS formula:

\=SUMIFS(B5:H15,B4:H14,**L5**)

to find out how many customers walked in to the store on the lookup date.

### How does this formula work?

See this illustration.

![2D Lookup formula with SUMIFS - how it works](https://img.chandoo.org/f/2d-data-lookup-formula-how-it-works.png)

Since [SUMIFS (and SUMIF too) formula works in 2D](http://chandoo.org/wp/2010/04/27/2d-sumif-formula/ "SUMIF works in 2D too [quick tip]")
, our formula works elegantly.

### Any caveats?

There are a couple of problems with this formula.

1.  It works for looking up numbers only
2.  It doesn’t work if any of the numbers are same as dates we are looking up. For example 15th October 2014 is 41927, so we have a data point that is also 41927, then our SUMIFS result would be wrong.

### A better formula?

If you want a formula that works with any type of data, then of course we can come up with one.

_**That is your home work.**_

Go ahead and figure it out and share your magic potions in the comments.

_**Here is a clue:** If we cant go somewhere directly, we can go indirectly, if we know the address._

### Download Example Workbook

[**Click here to download the example workbook**](https://img.chandoo.org/f/2d-data-lookup-formula.xlsx)
. Examine the formula in cell L6 to understand how this works.

### How do you deal with such data?

Badly shaped data is everywhere. Not a week goes by when I don’t come across poorly structured data. Thanks to Excel, I can alter the shape of _almost_ any data. My favorite techniques are – [text import](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)
, power query, formulas, [pivot tables](http://chandoo.org/wp/excel-pivot-tables/)
, [remove duplicates](http://chandoo.org/wp/2009/06/22/remove-duplicates/)
 & [go to special](http://chandoo.org/wp/2012/03/12/go-to-special/)
.

**What about you?** How do you deal with poorly structured data? What tools do you deploy to alter the fitness levels of your data? Please share your thoughts and tips in comments.

**Don’t forget about the formula challenge.**

### Excel not co-operating? Its time you tamed it

Data that is messy, bosses with high expectations, coffee machines that don’t work are everywhere. Fortunately Excel can fix 2 of those 3 problems. (Sorry folks, there is no fixCoffeeMachine() macro, yet.)

Learn a few Excel tricks & concepts and you could be on your way to taming messy data & demanding bosses. Start with these:

*   [SUMIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
    
*   [VLOOKUP formula](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
    
*   [SUMPRODUCT formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
    
*   [INDEX + MATCH formula](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
    
*   [The VLOOKUP Book](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/chandoo.org/wp/resources/the-vlookup-book/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [41 Comments](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/#respond)
    
*   Tagged under [2d lookup](https://chandoo.org/wp/tag/2d-lookup/)
    , [address](https://chandoo.org/wp/tag/address/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [homework](https://chandoo.org/wp/tag/homework/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [iseven()](https://chandoo.org/wp/tag/iseven/)
    , [IsOdd()](https://chandoo.org/wp/tag/isodd/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousWhat would you wear to an Excel themed Halloween party?](https://chandoo.org/wp/excel-halloween-costumes/)

[NextReady to use Excel Dashboard Templates – Official TrailerNext](https://chandoo.org/wp/excel-dashboard-templates-official-trailer/)

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
    
    [Reply](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
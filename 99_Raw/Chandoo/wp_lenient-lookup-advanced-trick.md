# Lenient lookup [Advanced Formula Trick] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/lenient-lookup-advanced-trick

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Lenient lookup \[Advanced Formula Trick\]
=========================================

*   Last updated on September 13, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

We all know [VLOOKUP (or INDEX+MATCH)](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
 as an indispensable tool in our Excel toolbox. But what if you want the lookups to be a little gentler, nicer and relaxed?

Let’s say you want to lookup the amount $330.50 against a list of payments. There is no exact match, but if we look 50 cents in either direction, then we can find a match. Here is a demo of what I mean.

![demo of lenient (flexible) lookup](https://chandoo.org/wp/wp-content/uploads/2018/09/lenient-lookup.gif)

Unfortunately, you can’t convince VLOOKUP to act nice.

_Hey VLOOKUP, I know you are awesome and all, but can you cut me some slack here?_ 

VLOOKUP is tough, reliable and has a cold heart. Or is it?

In this post, let’s learn how to do lenient lookups.

### Data for the problem

Let’s say you have a simple 2 column table like this. Our table is uninspiringly named _data._

![Data for lenient lookup](https://chandoo.org/wp/wp-content/uploads/2018/09/data-for-lenient-lookup.png)

Lenient lookup – setting up the formula
---------------------------------------

Our input amount is in cell **C3**.

Let’s say when looking up for the amount, we want to follow this logic.

1.  If an exact match is found, return that
2.  Else, see if we can find anything with in 50 cents either side (you can change 50 to whatever you want)
3.  If nothing can be found, we want to return “Not found” or similar message

**Formulas to use:**

1: we can use good old INDEX+MATCH

2: we can use array based INDEX+MATCH

3: we can use IFERROR.

Let’s put everything together.

Our lenient lookup formula (array):

> `=IFERROR( INDEX(data[Client], IFERROR(MATCH($C$3,data[Amount],0), MATCH(1, (data[Amount]>($C$3-0.5))*(data[Amount]<($C$3+0.5)),0) ))   ,"Not found")`

**How does it work?**

Let’s go inside out.

**MATCH($C$3,data\[Amount\],0):** this formula simply looks for C3 in data\[Amount\] column and returns the position.

**MATCH(1, (data\[Amount\]>($C$3-0.5))\*(data\[Amount\]<($C$3+0.5)),0):** This array formula checks for 1 (TRUE) by looking at data\[Amount\] between C3-0.5 and C3+0.5

The formula has two Boolean arrays multiplied and it returns a bunch of 1s & 0s.

MATCH then picks up the first such amount.

**Inner IFERROR(MATCH(…), MATCH(…)):** This acts like a fail-safe switch. If there is no exact match (first one), then lenient match (second one) will be used.

**Outer IFERROR():** If no matches are found (exact or lenient) then “Not found” will be printed.

As this is an array formula, you need to press CTRL+Shift+Enter to get the result.

Related material – read these if you have questions about the formula techniques used above:

*   [INDEX+MATCH formulas explained](https://chandoo.org/wp/how-to-lookup-values-to-left/)
    
*   [Boolean checks in array formulas – SUMPRODUCT tutorial](https://chandoo.org/wp/advanced-sumproduct-queries/)
    
*   [IFERROR formula – tutorial](https://chandoo.org/wp/iferror-formula/)
    

Other lenient / almost lookup problems
--------------------------------------

There are few more variations to this technique. Let’s review them.

Note: all of these are array formulas, so press CTRL+Shift+Enter.

### Ignore decimal portion

We lookup just the whole number portion of the value to find match.

**Formula:** \=INDEX(data\[Client\], MATCH(G7, INT(data\[Amount\]),0))

**Notes on how it works:**

*   INT() turns data\[Amount\] column to whole numbers.
*   We then lookup the amount (G7) and return the match

### Amount is at least _something,_ client name begins with S

**Formula:** =INDEX(data\[Client\], MATCH(1, (data\[Amount\]>=G8)\*(LEFT(data\[Client\],1)=”S”),0))

*   We use a different Boolean structure with >= and LEFT() formulas. The output will be a bunch of 1s & 0s.
*   INDEX+MATCH for find the first such value (G8)

### Closest Amount to input

This is interesting. We use MIN & ABS to find closest amount to input value (G10) and return the client’s name.

**Formula:** \=INDEX(data\[Client\], MATCH(MIN(ABS(data\[Amount\]-G10)), ABS(data\[Amount\]-G10),0))

*   ABS(data\[Amount\]-G10) gives a bunch of absolute (positive) values. The smallest of these will closest to G10.
*   MIN() finds the smallest value
*   MATCH looks up the minimum value from ABS(data\[Amount\]-G10)
*   INDEX gives corresponding client’s name

Download lenient lookup example workbook
----------------------------------------

[**Click here to download the example workbook**](https://chandoo.org/wp/wp-content/uploads/2018/09/lenient-lookups.xlsx)
. The file contains sample data, several examples of these techniques and additional resources to learn. Give it a go.

### More ways to lookup

[![Looking up when data won't co-operate - Matrix lookup with a twist](https://img.chandoo.org/f/2d-data-lookup-formula-how-it-works.png)](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/)
Lookups are an essential part of any data analysis work you do in Excel. Pick up some nifty tricks from these links.

*   Basics:
    *   [VLOOKUP, INDEX & MATCH Formulas](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
        
    *   [Wildcard lookups](https://chandoo.org/wp/using-wildcards-with-vlookup/)
        
*   Advanced:
    *   [Range lookup  – find which range contains input value](https://chandoo.org/wp/range-lookup-excel/)
        
    *   [Lookup only even rows – an odd lookup problem](https://chandoo.org/wp/odd-lookup-formula/)
        
    *   [Pricing tier lookup](https://chandoo.org/wp/pricing-tier-lookup-formula/)
        
    *   [Matrix lookup with a twist](https://chandoo.org/wp/looking-up-when-the-data-wont-co-operate-case-study/)
        

### Got a lookup tip to share?

Have some lookup stories to tell? I am listening. Please post them in comments.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/lenient-lookup-advanced-trick/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/lenient-lookup-advanced-trick/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousMy top 5 tips for designing beautiful Power BI reports](https://chandoo.org/wp/tips-for-designing-beautiful-power-bi-reports/)

[NextHow many people used their entire sick leave entitlement? \[Power Query / Excel homework\]Next](https://chandoo.org/wp/sick-leave-usage-problem/)

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
    
    [Reply](https://chandoo.org/wp/lenient-lookup-advanced-trick/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/lenient-lookup-advanced-trick/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/lenient-lookup-advanced-trick/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
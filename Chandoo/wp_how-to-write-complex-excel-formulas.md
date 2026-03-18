# How to write complex Excel formulas (hint: it's a lot like LEGO) » Chandoo

**Source:** https://chandoo.org/wp/how-to-write-complex-excel-formulas

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to write complex Excel formulas (hint: it’s a lot like LEGO)
================================================================

*   Last updated on December 9, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Do you want to know the secret to building complex, advanced Excel formulas? Here it is… 👇

Get inspiration from LEGO.

Confused? Let me demonstrate.

Calculating Student with Highest GPA
------------------------------------

Let’s build a formula to calculate the student with best GPA out of a table like this:

![students-and-gpas](https://chandoo.org/wp/wp-content/uploads/2021/12/students-and-gpas.png)

Our data is in columns C& D, in the range **C6:D45.**

1.  We can easily lookup the name of a student with GPA of say, 3.53, using lookup formulas like [XLOOKUP](https://chandoo.org/wp/xlookup-examples/)
    .
2.  We can also calculate the maximum (best) GPA using the MAX formula.

When you combine the Ideas 1 & 2, just like you combine LEGO, you create a third formula that gets the name of student with highest GPA.

So the final formula would be:

				
					`=XLOOKUP(MAX(D6:D45),D6:D45,C6:C45)`
				
			

And now, you can do the happy dance.

![dancing legoman](https://chandoo.org/wp/wp-content/uploads/2021/12/dancing-legoman.gif)

How about second highest GPA Student?
-------------------------------------

We can extend this idea to get the name of student with second highest GPA. Instead of MAX, we need to use LARGE function. Like this:

				
					`=XLOOKUP(LARGE(D6:D45, 2),D6:D45,C6:C45)`
				
			

In the above formula, LARGE(…, 2) returns the second highest GPA.

You can use the same concept to get third highest or second lowest (use SMALL(…,2)).

The LEGO way of building complex formulas...
--------------------------------------------

Just as there are a few basic building blocks in LEGO (well, nowadays, you can find a weird block shaped like dragon’s eyeball to fit in your harry potter set, but you get my point), we can also construct a complex formula from few basic ingredients.

Keep this construction tips in mind…

*   Break down the complex problem to small manageable chunks
*   Write down formulas for these chunks
*   If you need to repeat some logic, consider using either helper cells, or the new LET() function
*   Utilize the power of Excel references (absolute - $A$1, relative A1, mixed - A$1, $A1 and finally structural (table\[column\]) to write shorter & simpler formulas
*   Try newer formulas like FILTER, UNIQUE, SORT, LAMBDA etc. to get results easily
*   Take time to learn new techniques - such as spill ranges, LAMBDAs, data type driven formulas
*   When you have time, challenge yourself to figure out _another_ formula to solve the problem

5 Examples of how to build complex formulas
-------------------------------------------

If you are curious about this, then definitely watch my video. It shows how to write **advanced formulas** with Excel. See it below or [on my YouTube channel](https://youtu.be/Y3DEt7P62G8)
.

Sample Workbook - 5 Complex Formulas
------------------------------------

If you would like to practice these formulas, here is [the sample workbook](https://chandoo.org/wp/wp-content/uploads/2021/12/complex-excel-formulas-5-real-world-examples.xlsx)
. 

Up for a challenge? Then, go ahead and write a **_different_** formula for top 5 students with GPA.  
Share your answers in the comments section.

Want more inspiration? Check out below examples:
------------------------------------------------

There are heaps of **advanced formula examples** on chandoo.org. Start with below and see how you can twist the same 2×2 block in umpteen ways.

*   [Formula Forensics](https://chandoo.org/wp/formula-forensics-homepage/)
     – a series of amazing Excel formula trickery
*   [Multi-condition Lookups](https://chandoo.org/wp/multi-condition-vlookup/)
     – using good old VLOOKUP in creative ways
*   [10 Advanced IF formula tricks](https://chandoo.org/wp/advanced-if-tricks/)
     – the trusty IF can do wonders
*   [Dynamic Array Formulas](https://chandoo.org/wp/dynamic-array-functions/)
     – HOT HOT HOT – You must try these.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [3 Comments](https://chandoo.org/wp/how-to-write-complex-excel-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-write-complex-excel-formulas/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [formulas](https://chandoo.org/wp/tag/formulas-2/)
    , [index](https://chandoo.org/wp/tag/index-2/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [xlookup](https://chandoo.org/wp/tag/xlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousSorting values in Olympic Medal Table style \[Quick Tip\]](https://chandoo.org/wp/sorting-values-in-olympic-medal-table-style/)

[NextMerry Christmas & Happy New Year 2022Next](https://chandoo.org/wp/merry-christmas-happy-new-year-2022/)

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
    
    [Reply](https://chandoo.org/wp/how-to-write-complex-excel-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-write-complex-excel-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-write-complex-excel-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
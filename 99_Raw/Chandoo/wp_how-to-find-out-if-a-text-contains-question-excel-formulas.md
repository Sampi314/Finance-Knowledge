# How to find out if a text contains question? [Excel formulas] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-find-out-if-a-text-contains-question-excel-formulas

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to find out if a text contains question? \[Excel formulas\]
===============================================================

*   Last updated on July 17, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Few days back, I ran my first ever webinar, on a topic called, “How to be a BETTER Analyst?” ([here is the replay link](http://chandoo.org/wp/resources/webinar-replay/)
, in case you missed it).  It was a huge success. More than 1,100 people attended the live webinar and hundreds more watched the replay. As part of the webinar, we had interactive Q&A. Viewers posted their questions and I replied to as many of them as I can.

After the webinar, I wanted to make sure I covered all the questions. So I downloaded the chat history. There were more than 700 messages in it. And I am not in the mood to read line by line to find-out the questions. A good portion of chat messages were not questions but stuff like ‘hello everyone, I am from Idaho’, ‘Wow, Chandoo has beard!”, “Enjoying a beer in Belgium while watching webinar” etc. So I wanted a quick way to flag the messages as question or not.

![finding-if-cell-has-question-in-it](https://chandoo.org/wp/wp-content/uploads/2015/07/finding-if-cell-has-question-in-it.png)

I did what any sensible Excel analyst would do.

_I made myself a hot cup of coffee, started playing games on my iPhone while sipping it._

Of course after a cup of coffee and a bout of Candy Crush, I wrote simple Excel formula to find-out if the text in a cell is question or not. Let me share the formula & logic with you.

### Let’s take a look at the data

This is how the downloaded chat history looked like when imported to Excel. The column on right is where we need to write formula to find out if the comment is a question or not.

For the sake of simplicity, assume this data is in column B, starting with cell B5.

### The logic for identifying questions

In real life, finding if the other person is asking a question or just saying something can be tricky. For example, last evening my wife said, “Shall we go shopping?” and I assumed it was a question and said “no”. Apparently, it wasn’t a question. You can guess the rest.

![question-words](https://chandoo.org/wp/wp-content/uploads/2015/07/question-words.png)Unlike real life, in Excel, we can come up with good enough approximation to nail down questions.

For example, if a cell contains any of the below words, we can say it is a question.

> `What, why, how, who, when, where, is it, can I, can you, which, is this, are you, can we, are we, am I`

This is a pretty good way to separate questions from non-questions.

Let’s assume all the question words are maintained in a named range called _`q.words`_

### Writing the formula

So here is the formula to check if a cell contains question or not.

`=SUMPRODUCT(COUNTIFS(B5,"*"&q.words&"*"))>0`

**How does this formula work?**

Remember, B5 is the cell in question (no pun).

We need to see anywhere in B5, one of the question words occur.

This is where [COUNTIFS formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
 helps. It can count how many times a value has occurred in a range.

In our case, if B5 contains any of the question words. Note that B5 can contain other text too (apart from question words).

The formula `COUNTIFS(B5,"*"&q.words&"*")` will return an array of size 15 (as q.words contains 15 question words).

Let’s assume B5 has the text – “Why didn’t you take your wife to shopping?”

So, our `COUNTIFS(B5...)` will return the array `{0;1;0;0;0;0;0;0;0;0;0;0;0;0;0}`

The second item is 1 because second question word is **Why**.

If B5 has this text – “How I wish I took my wife to shopping. Can I take her now?”

`COUNTIFS(..)` will return this array `{0;0;1;0;0;0;0;1;0;0;0;0;0;0;0}` because it found the question words **How** and **Can I**.

_**But we don’t want the array…**_

You are right. We don’t need the array of 15 elements. We just want to know if _any_ of the questions are present in the B5 cell.

So, we pass this array to [SUMPRODUCT](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
, which sums up all the numbers and tells us single value.

We then check if this value is >0 or not.

So there you have it. A formula to find out if a cell has question or not.

### A question for you…

**Do you conduct text analysis using Excel?** What techniques do you use? Please share your approach & formulas in the comments.

### Bonus material for text analysis using Excel

If you deal with lots of text data, you will find below resources very useful.

*   [Finding patterns in Text – case study problem](http://chandoo.org/wp/2012/12/14/find-text-pattern/)
    
*   [Extracting file name from full path](http://chandoo.org/wp/2012/10/24/extract-file-name-from-path/)
    
*   [Analyzing search keywords & finding word frequency](http://chandoo.org/wp/2009/04/29/analyze-search-keywords-excel/)
    
*   [Analyzing 20,000 comments – Case study](http://chandoo.org/wp/2012/07/19/analyzing-20000-comments/)
    
*   [Sentiment analysis of text using Excel](http://datapigtechnologies.com/blog/index.php/quantifying-subjective-text-with-sentiment-analysis/)
    
*   [More on text processing & analysis using Excel](http://chandoo.org/wp/tag/text-processing/)
    

Now if you excuse me, I need to take my wife for shopping. 🙂

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [14 Comments](https://chandoo.org/wp/how-to-find-out-if-a-text-contains-question-excel-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-find-out-if-a-text-contains-question-excel-formulas/#respond)
    
*   Tagged under [countifs](https://chandoo.org/wp/tag/countifs/)
    , [excel formulas](https://chandoo.org/wp/tag/excel-formulas/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [text processing](https://chandoo.org/wp/tag/text-processing/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousQuickly filter a table by combination of selected cell values using VBA](https://chandoo.org/wp/filter-a-table-by-combination-of-values/)

[NextCP039: May the FOR Loop be with you – Introduction to For Loops in Excel VBANext](https://chandoo.org/wp/cp039-for-loop-vba/)

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
    
    [Reply](https://chandoo.org/wp/how-to-find-out-if-a-text-contains-question-excel-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-find-out-if-a-text-contains-question-excel-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-find-out-if-a-text-contains-question-excel-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
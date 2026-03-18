# Excel Animation without Macros! » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-animation-without-macros

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel Animation without Macros!
===============================

*   Last updated on November 30, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Today we will learn an interesting animation technique that _ONLY_ uses, … wait for it …, Excel Formulas.** That is right, we will use simple formulas to animate values in Excel.

Intrigued? Confused? Interested?

First see these Excel animation demos:
--------------------------------------

### Animated icons & fill-color

![Animated Icons & Cell Fill Color in Excel - Demo](https://chandoo.org/img/cf/animated-icons-colors-excel.gif)

### Animated In-cell Charts

![Animated Incell charts - Excel](https://chandoo.org/img/cf/animated-incell-charts.gif)

**[Click here to download the workbook](https://img.chandoo.org/d/animation-without-macros.xlsx)
 with these examples.**

What is the secret sauce behind this animation?
-----------------------------------------------

Take 1 portion of crushed basil leaves, 2 portions of  grounded roasted coffee beans and mix them with hot water. Add enough sugar and throw it away. 😛

Now, come back to your excel workbook and use circular references to generate the animation effect.

### Understanding how Circular References & Iterative Calculation Mode work

In order to get this animation, you should be familiar with two excel magic spells – [Circular References](http://chandoo.org/wp/2010/09/16/excel-circular-references/)
 & Iterative Calculations. In simple terms,

**Circular Reference:** is when a cell refers to itself in the formula. For eg. in cell A1, if you write =A1+1, it is a circular reference. The reference can be both direct or in-direct (ie you can refer to cell B1, which refers to A1 again).

**Iterative Calculation:** If a cell has circular reference, excel can quickly go in to infinite loop (not the [place](http://maps.google.com/maps?q=1+Infinite+Loop,+Cupertino,+Santa+Clara,+California+95014&hl=en&client=firefox-a&ie=UTF8&cd=1&geocode=FcajOQIdYvO5-A&split=0&sll=37.0625,-95.677068&sspn=23.875,57.630033&hq=&hnear=1+Infinite+Loop,+Cupertino,+Santa+Clara,+California+95014&z=17)
 where Apple is head-quartered). To avoid this, we use _**iterative calculation mode**_. When you enable this mode, excel solves the cell references only a certain number of times.

**[Here is an excellent guide on circular references](http://chandoo.org/wp/2010/09/16/excel-circular-references/)
.**

### How to enable iterative calculation mode?

Simple, go to Excel options > Formulas and then select iterative mode. Change the number of iterations to a large value (so that we can see some animation). Like this:![Enable Iterative Calculation mode to get Circular References work](https://chandoo.org/img/cf/iterative-claculation-mode-settings.png)

### How to use Circular References & Iterative Mode for Animation?

It doesn’t take a lot of coffee to conclude that using circular references & iterative mode of calculation, we can increment a cell value from 1 to 100 (or 4000, if you fancy).

Assuming you want to increment the value in A1 from 0 to 100, and A2 is used to control the animation (ie if you type “Yes” in a2, only then we increment the values).

In cell A1, we write =IF(A2=”yes”,IF(A1>=100,A1,A1+1),0)

If iterative mode is enabled, when you enter _**yes**_ in cell A2, you can see the value in A1 going from 0 to 100, _very fast._

Now, if you change the formula to =IF(A2=”yes”,IF(A1>=**4000**,A1,A1+1),0), you can see the cell value in A1 going up from 0 to 4,000 in a few seconds.

### But, what about animation?!?

Now that we have the cell A1 changing its value when we want, we just need to link this with conditional formatting to get some magic.

**For eg. you  can [apply conditional formatting](http://chandoo.org/wp/excel-tutorial/using-conditional-formatting/)
 on A1 with the following rule to change cell color as the value increases.**

![Conditional Formatting Color Scale Settings for Animation](https://chandoo.org/img/cf/conditional-formatting-color-scale-settings.png)

Similarly, you can use the value in A1 to draw [in-cell charts](http://chandoo.org/wp/tag/in-cell-charting/)
 that grow as the value changes in A1.

_**Just let your imagination run wild.**_

Where can you use such animation?
---------------------------------

**Animation is a powerful attention grabber**. I think you can use this type of animation in [dashboards to display alerts](http://chandoo.org/wp/2010/05/25/alerts-in-dashboards/)
. For eg. you can highlight portions of dashboard that changed when a different product (or month) is selected.

That said, **I strongly recommend against overuse of animation effects.** They can quickly become annoying. Not to mention, they are cumbersome to maintain (and add little value).

What are the limitations of Circular Reference based animation?
---------------------------------------------------------------

*   **You must enable iterative mode of calculation.**
*   **This doesn’t work with charts**. Excel charts do not pick up cell values unless the calculation is finished. So you cannot plug values in to charts to expect animated charts. If you are curious to build one, see Daniel’s [animated business charts example](http://www.excelhero.com/blog/2010/05/animated-business-chart.html)
    .
*   **This can slowdown your workbook:** Whenever you run the animation, excel is going to do thousands of calculations and this will slowdown your workbook.

Download Excel Animation Workbook
---------------------------------

I have put together a simple workbook showcasing several examples of this technique. **Download and play with it.**

[Excel 2007 link](https://img.chandoo.org/d/animation-without-macros.xlsx)
 | [Excel 2003 link](https://img.chandoo.org/d/animation-without-macros.xls)

_(Make sure you have turned on the iterative mode.)_

Do you find this technique interesting?
---------------------------------------

To be frank, I find this technique more amusing than useful. But I wrote about it anyway as it shows what is possible with excel. It can be useful in situations where there is too much information and you need to call users attention to something.

**What about you? Do you see any practical applications for this technique? Share your ideas and opinions thru comments.**

More Excel Magic
----------------

*   [What is a circular reference – a comprehensive guide](http://chandoo.org/wp/2010/09/16/excel-circular-references/)
    
*   [Using Excel to generate timestamps](http://chandoo.org/wp/2009/01/08/timestamps-excel-formula-help/)
    
*   [Dynamic Charts – Select a chart to show it](http://chandoo.org/wp/2008/11/05/select-show-one-chart-from-many/)
    
*   More examples on [Dynamic charts](http://chandoo.org/wp/tag/dynamic-charts)
    , [Conditional Formatting](http://chandoo.org/wp/tag/conditional-formatting/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [50 Comments](https://chandoo.org/wp/excel-animation-without-macros/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-animation-without-macros/#respond)
    
*   Tagged under [animation](https://chandoo.org/wp/tag/animation/)
    , [circular formulas](https://chandoo.org/wp/tag/circular-formulas/)
    , [circular references](https://chandoo.org/wp/tag/circular-references/)
    , [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [in-cell charting](https://chandoo.org/wp/tag/in-cell-charting/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [rept](https://chandoo.org/wp/tag/rept/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHomework – When does Thanksgiving Day occur on same date again?](https://chandoo.org/wp/when-does-thanksgiving-day-occur-on-same-date-again/)

[NextShow Top 10 Values in Dashboards using Pivot TablesNext](https://chandoo.org/wp/top-10-values-in-dashboards/)

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
    
    [Reply](https://chandoo.org/wp/excel-animation-without-macros/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-animation-without-macros/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-animation-without-macros/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
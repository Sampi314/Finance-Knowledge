# Excel Circular References - What are they, How to use them, Examples & Dealing with Circular References

**Source:** https://chandoo.org/wp/excel-circular-references

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

A round-up on Circular References
=================================

*   Last updated on June 5, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Excel Circular References - What are they, How to use them, Examples & Dealing with Circular References](https://img.chandoo.org/f/excel-circular-references-guide.jpg)_**Here is a little experiment to freak out excel.**_

Go to cell C3 and write =C3 and press Enter. Excel would throw up nasty message saying, “_Microsoft did not know what to do. We have a sent a support engineer to your home, but he is stuck at the round-about near your house._”

**Well, not really. But what you did when you wrote the formula =C3 in cell C3 was, you created a circular reference.**

### What is a Circular Reference & why use them?

> A circular reference is created when you refer to same cell either directly or indirectly.

**We use circular references when we need circular references.**

### Excel Circular Reference Example:

For eg. (borrowed from [John Walkenbach’s Excel 2010 Bible](http://www.amazon.com/gp/product/0470474874?ie=UTF8&tag=poinhairdilb-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0470474874)
), lets say you run a fictitious company named Sky is the Ltd.

**And you have a strange policy of donation 10% of your profits after tax to charity**.

_**But, in your country, charity donations are tax exempt (they are expenses).**_

`So charity = 10% * after tax profits`  
`after tax profits = (revenues - expenses - charity)*(1-tax rate)`

**![Excel Circular References - an example](https://chandoo.org/img/f/circular-reference-example.png)**

_**By definition, charity refers to after tax profits, which refers to charity, thus creating a circular reference.**_

_Now, how would you find out how much to donate to charity?_

Simple, we write formulas with circular references, like this:

![Excel Circular References in Formulas - an example](https://chandoo.org/img/f/excel-circular-reference-example.png)

_**But wait, just when you press enter after writing the formulas, Excel would scream bloody and curse your entire family for having a circular reference in your worksheet.**_

### Enabling Iterative Calculation Mode

You must enable what they call _**iterative calculation mode**_ before the formulas work. For this we must go to Excel Options.

**In latest versions of Excel,![Enable Iterative Calculation mode to get Circular References work](https://img.chandoo.org/f/excel-options-iterative-calculation.png)**

*   Click on Office button
*   Go to Excel Options, this is analogous to opening the bonnet of your car, but just a bit more confusing.
*   Locate the “Formulas” on the left, click on it
*   Now, check the “Enable iterative calculation”. This way you are telling Excel to evaluate references iteratively, up to 100 times (default).
*   Click ok, close the bonnet. That is all.

**In per-historic versions of Excel,**

*   Go to Menu > Tools > Options > Calculation Tab
*   Check Iterative Calculation box. (see image)

Once you do this, your formulas will work nicely and you will find that the required charity donation to be made.

### How to avoid Circular References?

As you can understand circular references are a pain in cell. You may want to get rid of them altogether. Thankfully, with careful inspection and a mug of coffee, you can reduce most circular references to simple formulas. For eg, in the above case, we can calculate charity amount directly by using the following equations.  
![Remove or Avoid Circular References using Better Formulas](https://chandoo.org/img/f/use-arithmetic-to-remove-circular-references.png)

But, keep in mind that, in few cases, circular references may be required. For eg. if you want to [add timestamps to your workbook](http://chandoo.org/wp/2009/01/08/timestamps-excel-formula-help/)
.

### How to locate Circular References?

_**Do you know that you can find all the circular references in a workbook?**_

Whenever you see circular reference warning message, just go to formula ribbon and click on error checking options. You can see all the circular references there.

![Locate Circular References in an Excel Sheet](https://chandoo.org/img/f/locating-circular-references.png)

_Note: In Excel 2003, you can see the same from circular reference toolbar (Menu > View > Tool-bars > Circular Reference)_

### Examples & More Resources on Circular References:

*   [Add timestamps to your workbook](http://chandoo.org/wp/2009/01/08/timestamps-excel-formula-help/)
    
*   [Team Todo List template in Excel](http://chandoo.org/wp/2009/06/25/todo-lists-project-tracking-tools/)
    
*   [Circular References & Other Repetitive Calculation Features in Excel](http://www.decisionmodels.com/calcsecretsk.htm)
    
*   [Solve Circular References instead of using them](http://www.sumwise.com/blog/solve-circular-references/)
    

### Do you do circular references?

I try to avoid circular references whenever possible. But in some rare cases, I think a circular reference gives elegant, shorter solution than a non-circular variation of it.

_**What about you?**_ Do you use circular references often? What are the reasons / uses of them according to you? _**Please share your experience, tips thru comments.**_

PS: Here is a [very useful link on circular references](http://chandoo.org/wp/2010/09/16/excel-circular-references/)
.

PPS: Monalisa pic source [is here](http://www.dominiek.eu/blog/?p=102)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [50 Comments](https://chandoo.org/wp/excel-circular-references/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-circular-references/#respond)
    
*   Tagged under [circular formulas](https://chandoo.org/wp/tag/circular-formulas/)
    , [circular references](https://chandoo.org/wp/tag/circular-references/)
    , [errors](https://chandoo.org/wp/tag/errors/)
    , [examples](https://chandoo.org/wp/tag/examples/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [references](https://chandoo.org/wp/tag/references/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel School is Open – Join Today](https://chandoo.org/wp/excel-school-is-open-join-today/)

[NextYou are invited \[personal\]Next](https://chandoo.org/wp/birthday-invitation/)

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
    
    [Reply](https://chandoo.org/wp/excel-circular-references/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-circular-references/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-circular-references/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
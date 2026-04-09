# Introduction CHOOSE Excel Function What is Excel CHOOSE formula, how to use it?

**Source:** https://chandoo.org/wp/introduction-to-choose-function

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

CHOOSE() me, an introduction to Excel CHOOSE function
=====================================================

*   Last updated on November 23, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Today lets learn about Excel CHOOSE() function.**_

### CHOOSE eh? What does it do?

To understand CHOOSE() and appreciate its uses, lets invent an imaginary boss-subordinate pair.

Jasmine is the boss. She is, well, lets call her _peculiar._ She likes olives, Tuesdays & color Red. She hates potatoes.

Martin is the faithful butler of Jasmine. He is obedient, quirky and tall. He likes lotuses, Fridays & color blue. He hates potassium.

### Enter Jasmine’s scarf problem:

Jasmine likes to wear a different colored scarf every weekday. She likes to wear Red colored scarf on Mondays & Tuesdays. She likes to put on the blue polka dot scarf on Wednesdays. On Thursdays, she wears her olive colored scarf. On Fridays & Saturdays, she prefers the lovely orange blue scarf. Sundays are no scarf days.

_No wonder she is peculiar._

On the first day of his job, Martin understood this schedule. Although he did raise his eyebrows (in bewilderment) more than once, he knew a butler should never question.

So everyday, soon after waking up, Martin would open up the list of _scarf requirements,_ and figure out the scarf for that day. He would then neatly lay it out on Jasmine’s bed while she is in the shower.

**_Soon this all got boring._**

So Martin thought, _“Wouldn’t it be cool if I can feed the scarf schedule to a computer so it automatically told me which scarf to choose everyday morning!.”_

Martin reached out to his ninja computer friend who knew how to do this.

**_YOU._**

### Your Excel solution for Jasmine’s scarf problem

After hearing the entire story, raising eyebrows a few times and looking at Martin with eyes full of pity, you set out to create an Excel workbook that told him which scarf to pick on any given date.

_It is simple & elegant_.

In the Cell B3, you wrote =TODAY()

_so that everyday A3 will tell what is the latest date._

In B4, you wrote =WEEKDAY(B3)

Then in B5, you wrote a lengthy nested IF formula to figure out the scarf of the day.

**Scarf of the day formula:**

`=IF(B4=1,"No scarf",IF(B4<=3,"Red scarf",IF(B4=4,"Blue polka dot scarf", IF(B4=5,"Olive colored scarf","Orange blue scarf"))))`

Martin couldn’t be happier. Now that he has an awesome Excel file telling him what scarf to pick everyday, he has one less thing to worry.

**BUT….**

Soon after your Excel file, Jasmine had to replace the polka dot scarf with yellow striped one (she slipped an olive on the scarf while eating and it left a permanent mark).

While at it, she also changed the schedule.

And now, Martin is back to square one.

Late that week, he explained the problem to you over a drink. You quickly modified the file to suit new scarf of the day scenario.

The formula now looked like this:  
`   =IF(B4=1,"No scarf",IF(OR(B4=2,B4=4),"Red scarf",IF(B4=3,"Yellow striped scarf", IF(B4=5,"Olive colored scarf","Orange blue scarf"))))`

_**Thats when you got thinking.**_

The nested IF formula is awfully long and clumsy to maintain. _May be there is a better one?!?_

### Enter CHOOSE formula, built for scarf of the day & more

CHOOSE() formula works beautifully for situations like this.

Instead of the long & clumsy nested IF formula, you could simply write a choose formula.

**Syntax of the CHOOSE formula:**

The CHOOSE formula is simple to write.

`=CHOOSE(some number, value 1, value 2, value 3....)`

and CHOOSE will pick a value based on _some number._

For example,

`=CHOOSE(3,"Chandoo.org","makes","you","awesome")`

will result in **you.**

**Scarf of the day CHOOSE Formula:**

For our scarf of the day, the choose formula looks like this:

`=CHOOSE(B4,"No scarf","Red scarf","Yellow striped scarf", "Red scarf","Olive scarf","Orange blue scarf","Orange blue scarf")`

(or this if you want it for schedule prior to olive accident, `=CHOOSE(B4,"No scarf","Red scarf","Red scarf","Blue polka dot scarf", "Olive scarf","Orange blue scarf","Orange blue scarf")` )

### Okay, what else can CHOOSE() do?

CHOOSE cant make you tall, rich or beautiful yet. But, it can do few more things.

Here is one such powerful example.

**Fetch one range from many using CHOOSE**

We can use CHOOSE() to fetch one of the many ranges, like this:  
`   =SUM(CHOOSE(2, A1:A10, B1:B10,C1:C10,D1:D10))`

This will result in the sum of the **2nd** range, _ie_ B1:B10.

Here is an interesting example of this:

### How many values can CHOOSE take?

CHOOSE() can take up to 254 different values and return one of them based on the _index number (first parameter)._

**What if I have more than 254?**

Forget 254. Anytime you want to choose one value from more than a few (say 10), CHOOSE formula becomes tedious (as you have to select individual value cells or type them).

For all such cases (ie when you have list of values more than 10), I suggest [using INDEX()](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/ "7 reasons why you should get cozy with INDEX()")
. It is a powerful & versatile formula designed to handle situations like this.

### Example workbook:

[**Here is the example workbook on CHOOSE**](http://1drv.ms/1jwv8Uw)
. When you click the link, it opens Excel inside browser so you can practice this anywhere.

### Do you CHOOSE?

I write CHOOSE() formulas often. It is a simple formula and I find several uses for it.

What about you? Do you use CHOOSE()? What are some of your favorite uses of it? _Please share your thoughts using comments._

### More examples on CHOOSE

Check out these additional examples to learn more:

*   [Learn 5 IF formula tricks](http://chandoo.org/wp/2008/06/09/what-the-if-learn-6-cool-things-you-can-do-with-excel-if-functions/)
    
*   [Using CHOOSE formula to calculate thanksgiving date](http://chandoo.org/wp/2009/11/25/findout-thanksgiving-date/)
    
*   [Using CHOOSE formula to create dynamic charts](http://chandoo.org/wp/2013/04/23/interactive-chart-in-excel-tutorial/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [24 Comments](https://chandoo.org/wp/introduction-to-choose-function/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introduction-to-choose-function/#respond)
    
*   Tagged under [choose()](https://chandoo.org/wp/tag/choose/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [excel basics](https://chandoo.org/wp/tag/excel-basics/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [Nested If](https://chandoo.org/wp/tag/nested-if/)
    , [today()](https://chandoo.org/wp/tag/today/)
    , [weekday](https://chandoo.org/wp/tag/weekday/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHere is a simple solution to your forgetful, leaky brian – “Just put it in a spreadsheet”](https://chandoo.org/wp/here-is-a-simple-solution-to-your-forgetful-leaky-brian-just-put-it-in-a-spreadsheet/)

[NextHow fireworks animated chart is made Next](https://chandoo.org/wp/fireworks-chart-video-tutorial/)

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
    
    [Reply](https://chandoo.org/wp/introduction-to-choose-function/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introduction-to-choose-function/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introduction-to-choose-function/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
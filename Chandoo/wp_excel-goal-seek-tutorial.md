# Excel Goal Seek Tutorial - Learn how to use goal seek feature by building a retirement calculator in Excel

**Source:** https://chandoo.org/wp/excel-goal-seek-tutorial

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [personal finance](https://chandoo.org/wp/category/personal-finance/)
    

Build a Retirement Calculator using Excel (learn how to use Goal Seek as a bonus)
=================================================================================

*   Last updated on October 15, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This post is part of **[spreadcheats](http://chandoo.org/wp/tag/spreadcheats)** series._

**Today we will learn a fascinating little feature in excel called “goal seek”.**

But what good is a feature if we cant find a use for it? So we will build a simple retirement calculator using excel.

Before plunging in to the complex retirement calculations, let us spend a bunch of words understanding what this goal seek is all about.

### What is goal seek in excel?

![goal-seek-excel-help](https://chandoo.org/wp/wp-content/uploads/2009/07/goal-seek-excel-help.png "goal-seek-excel-help")**We can think of goal seek as opposite of formulas.** Formulas tell you what is the output of a bunch of variables used in an equation (for eg. sumproduct is an equation involving + and \*). **Goal seek tells you what inputs you need to give in order to get certain output.**

For example, you can use goal seek to solve a linear equation or find the internal return rate (IRR) of an investment.

Now that you understand goal seek, let us plan your retirement. 🙂

### Make a financial model to estimate your monthly savings to meet retirement goals.

![Retirement Planning Worksheet using Excel](https://chandoo.org/img/l/retirement-calculator-worksheet.png)

(Note: the image shows commas according to Indian currency formatting.)

In order to proceed, we would need some data, like,  
(1) What is your current age?  
(2) What is your expected retirement age?  
(3) How much do you think you will spend every month when you retire (of course in today’s prices)  
(4) Your expectation of inflation (%)?  
(5) Your expected return (%) on investments?

Once the data is available, we will need to calculate the following,

_I have shown the worksheet on the right with some dummy data._  
(6) The yearly expenses at the time of retirement: (3) \* (1+(4))^((2)-(1))\*12  
(7) Corpus required to generate the above amount every year (and leave the principle behind): (6)/(5)

_(**If these calculations are overwhelming**, download the excel retirement calculator workbook [here](https://chandoo.org/wp/wp-content/uploads/2009/07/retirement-calculator-excel.xlsx)
_.)

We know how much corpus is needed.

We can use [FV() formula](http://chandoo.org/excel-formulas/fv.html)
 to determine the future value of a series of payments made periodically and compounded at a given interest rate.

**We know how much the FV() out come should be, but we don’t know how much the input (monthly investment) should be.**

_**This is where goal seek is going to help us.**_

Let us assume the monthly investment amount will be in cell A5. Let us also assume, the interest rate is in cell A4, retirement age is in A3, current age is in A2.  
We will write the FV formula in cell A6 like this = `-FV(A4/12,(A3-A2)*12,A5)`  
(we have to negate FV since it uses weird accounting notations)

Since the cell A5 is blank, the FV will show the value as 0.

Now, we will use goal seek to find out how much cell A5 should have so that A6 will be calculated to the corpus amount required.

Go to Data tab and click on What if analysis and select goal seek. (In excel 2003, it should be in tools menu)

**See this screen cast to understand how the goal seek works:**  
![Retirement Savings Estimation using Excel Goal Seek](https://chandoo.org/img/l/retirement-calculator-using-excel.gif)

The goal seek window has 3 inputs. The cell you need to change. The cell you want to set and the value to set.

Once you use the goal seek it will find the correct (or closest) value to meet the goal and displays it. If you press OK, the value will be placed in the cell (in our case, in A5)

That is all.

### Download the Retirement Calculator Excel Worksheet and play with it

[Click here](https://chandoo.org/wp/wp-content/uploads/2009/07/retirement-calculator-excel.xlsx)
 to download the retirement calculator worksheet. Follow the instructions in the workbook to see this example for yourself. Change values to find the amount that you need to save.

### Do you find goal seek feature useful?

What do you do with excel goal seek? Do you use it in your modeling, planning worksheets? Tell me your experiences and ideas using comments.

### Additional resources:

*   [Read remaining posts in Spreadcheats series](http://chandoo.org/wp/tag/spreadcheats/)
    : Become a spreadsheet guru by learning these nifty hacks.
*   [Excel financial formulas – Help on NPV, FV, PV and more](http://chandoo.org/excel-formulas/financial-functions.html)
    
*   [Understand why you should start early when it comes to retirement savings](http://chandoo.org/wp/2007/04/04/start-early/)
    
*   [Buy or rent calculator in Excel](http://chandoo.org/wp/2007/02/12/find-out-whether-you-need-a-house-or-not-in-60-seconds/)
     – calculate returns on property investments

PS: the retirement calculation steps are derived from [this excellent article on smart investor](http://www.jagoinvestor.com/2009/07/6-steps-of-doing-retirement-planning-by.html)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [32 Comments](https://chandoo.org/wp/excel-goal-seek-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-goal-seek-tutorial/#respond)
    
*   Tagged under [examples](https://chandoo.org/wp/tag/examples/)
    , [financial formulas](https://chandoo.org/wp/tag/financial-formulas/)
    , [FV](https://chandoo.org/wp/tag/fv/)
    , [goal seek](https://chandoo.org/wp/tag/goal-seek/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [personal finance](https://chandoo.org/wp/tag/personal-finance/)
    , [retirement planning](https://chandoo.org/wp/tag/retirement-planning/)
    , [solver](https://chandoo.org/wp/tag/solver/)
    , [spreadcheats](https://chandoo.org/wp/tag/spreadcheats/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tutorials](https://chandoo.org/wp/tag/tutorials/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [personal finance](https://chandoo.org/wp/category/personal-finance/)
    

[PrevPreviousCharting Lessons from Optical Illusions](https://chandoo.org/wp/charting-lessons-from-optical-illusions/)

[NextTime to showoff your VBA skills – Help me fix ActiveSheet.Pictures.Insert snafuNext](https://chandoo.org/wp/activesheet-pictures-insert-help/)

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
    
    [Reply](https://chandoo.org/wp/excel-goal-seek-tutorial/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-goal-seek-tutorial/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-goal-seek-tutorial/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
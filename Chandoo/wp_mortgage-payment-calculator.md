# Mortgage Payment Calculator using Excel

**Source:** https://chandoo.org/wp/mortgage-payment-calculator

---

*   [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Interactive Mortgage Calculator to know how much you can borrow (with Excel)
============================================================================

*   Last updated on February 20, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Today we will build a mortgage payment calculator using excel.** But we will not build a boring excel sheet, we will build a mortgage calculator that is easy to play with.

**A mortgage payment is a monthly installment that you pay towards a loan.** Any mortgage loan will typically have,

*   loan amount
*   duration of the loan (also called as tenure of mortgage) in years
*   interest rate (APR) per year

Given these 3 parameters, we can easily determine the monthly installment amount (this will be the same amount for all months during loan tenure)

_**We are going to use Excel’s form controls (more on this below) to build a mortgage payment calculator like this:**_  
![Mortgage Payment Calculator](https://chandoo.org/img/c/mortgage-payment-calculator.gif "Mortgage Payment Calculator - using Excel")

Why you should not be boring and use the form controls
------------------------------------------------------

A [form control](https://chandoo.org/wp/form-controls/)
 is a button or check box or scrollbar or some other click-able thing you see in Windows. **Do you know that you can add the very same controls to Excel spreadsheet to make the it interactive?**

For example,

*   instead of asking a user to enter “yes” or “no” in a cell, you can ask them to click a check box.
*   instead of taking “age” in a cell, you can use a scroll bar and set the values from 0 to 100.

**This way of gathering inputs is more fun, engaging and interactive.**

Now that you find form controls hot and attractive, lets proceed and make a house loan payment calculator.

How is mortgage payment calculated?
-----------------------------------

As I said above, any mortgage (or housing loan) will have 3 parts – loan amount (p), loan tenure (n) and annual interest rate (r).

**Given the values of P, N and R, we can find the monthly payments using Excel’s PMT formula** like this:

`=PMT(R/12,N*12,P)`

\[Related: [PMT formula syntax & examples](https://chandoo.org/excel-formulas/pmt.shtml)\
\]

\[Related: [Amortization Schedule in Excel](https://chandoo.org/wp/loan-amortization-schedule-in-excel/)\
\]

We are dividing interest rate (R) by 12 since R is annual interest rate and we make monthly payments.

We are multiplying loan duration (N) with 12 since we are going to make monthly payments.

Making the mortgage calculator in Excel
---------------------------------------

We will use scroll-bar controls to take numeric inputs required (P,N and R) for the payment calculation. And we feed these values to PMT formula to find the monthly installment amount.

### Step 1: Add a Scroll-bar Control

**We will use this scroll bar to take “loan amount” input.** To keep it simple, we will ask users to enter input in ‘000s. So, if the loan is $120,000, the input should be 120.

First add a scroll-bar form control to your excel sheet. To do this go to Developer Ribbon > Insert > Scroll-bar Form Control in Excel (related: [enable developer toolbar in Excel](https://chandoo.org/wp//excel-2007-productivity-tips/)
)

**Add a Scroll-bar Control**

![Adding a scroll-bar control in Excel using Developer Ribbon](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3192.png)

Once selected, just add the control to spreadsheet by clicking anywhere.

### Step 2: Set Properties for this Scroll-bar

**To set the properties for the scrollbar control, right click on it and go to “format control” option.** Now go to “Control” tab.

Here set minimum and maximum values for the scroll bar. To keep our model simple, just set minimum as 35 and maximum has 500.

Also, select a cell to link the scrollbar. When you do this, excel links the scroll bar to the selected cell. So whenever scroll bar is updated the cell gets updated too (and _vice-a-versa_). See this illustration:

![Set Properties for this Scroll-bar - Excel](https://chandoo.org/img/c/formatting-scrollbar-control-excel.png)

### Step 3: Add Remaining Scroll bars

Repeat the same steps for 2 other scroll bars. One for interest rate and one for loan tenure.

Make sure you set the minimum and maximum values in a reasonable range.

### Step 4: Plug the values in to PMT formula

Now that the scroll bars are ready, just write the PMT formula. Assuming you have linked scroll bars like this:

*   Loan amount in cell A1
*   Interest rate in cell A2
*   Loan tenure (years) in cell A3

**The formula will be,**

`**=PMT((A2/12)%,A3*12,A1)**`

Remember, PMT returns value in negative numbers (as it is the amount we need to pay, not get). But you can make it positive (for display purposes) by multiplying it with -1 like this `= -PMT((A2/12)%,A3*12,A1)`

### Step 5: Play with your Model

Now your mortgage payment calculator is ready. You can play with it by testing various combinations and finding monthly payments. You can easily see what happens when you increase loan tenure or decrease interest rate.

![Mortgage Payment Calculator](https://chandoo.org/img/c/mortgage-payment-calculator.gif "Mortgage Payment Calculator - using Excel")

Download Excel Mortgage Payment Calculator
------------------------------------------

**[Here is the excel mortgage payment calculator file](http://chandoo.org/img/d/excel-mortgage-payment-calculator.zip)
**. Download and play with it.

Bonus – Making an Amortization Schedule
---------------------------------------

You can easily extend this model to add an amortization schedule to see how much of each monthly payment is towards principal and how much is for interest.

*   You can calculate principal portion for any month using PPMT formula like this `=PPMT(R/12,M,N*12,P)`. Here “M” is the month for which you want principal amount.
*   You can calculate interest portion for any month using IPMT formula like this `=IPMT(R/12,M,N*12,P)`.

Full tutorial: [Loan Amortization Schedule with Excel](https://chandoo.org/wp/loan-amortization-schedule-in-excel/)
.

### Do you love form controls?

Do you [use form contro](https://chandoo.org/wp/excel-vba/user-forms/)
[ls](https://chandoo.org/wp/form-controls/)
 in your spreadsheets? I find them pretty intuitive and use them wherever I can. I have made many complex spreadsheet models easy to understand and work with by just adding form controls. The beauty is that, they require no programming or anything. You just add them and link them to a cell.

**What about you?** Do you love form controls? Where do you use them most?

**Learn More about Excel Form Controls:**

*   [Make a comparison chart using scroll bars](https://chandoo.org/wp/comparison-charts-1/)
    
*   [Create a check box in excel](https://chandoo.org/wp/add-checkbox-excel/)
    
*   [Make a donut bar chart using form controls](https://chandoo.org/wp/donut-bar-chart/)
    
*   _**[More form control examples](http://chandoo.org/wp/tag/form-controls/)
    **_

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [24 Comments](https://chandoo.org/wp/mortgage-payment-calculator/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/mortgage-payment-calculator/#respond)
    
*   Tagged under [amortization schedule](https://chandoo.org/wp/tag/amortization-schedule/)
    , [calculations](https://chandoo.org/wp/tag/calculations/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [financial formulas](https://chandoo.org/wp/tag/financial-formulas/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [IPMT()](https://chandoo.org/wp/tag/ipmt/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [mortgage](https://chandoo.org/wp/tag/mortgage/)
    , [personal finance](https://chandoo.org/wp/tag/personal-finance/)
    , [PMT()](https://chandoo.org/wp/tag/pmt/)
    , [PPMT()](https://chandoo.org/wp/tag/ppmt/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExtract usernames from E-mail IDs \[using LEFT and FIND formulas in Excel\]](https://chandoo.org/wp/usernames-from-email-formulas/)

[NextUse “Playbill” font to make your incell charts realistic \[quick-tips\]Next](https://chandoo.org/wp/excel-incell-chart-font/)

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
    
    [Reply](https://chandoo.org/wp/mortgage-payment-calculator/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/mortgage-payment-calculator/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/mortgage-payment-calculator/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
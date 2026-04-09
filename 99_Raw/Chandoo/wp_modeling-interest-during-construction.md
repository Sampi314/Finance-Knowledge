# Modeling Interest During Construction (IDC) - Excel Project Finance » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/modeling-interest-during-construction

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Modeling Interest During Construction (IDC) – Excel Project Finance
===================================================================

*   Last updated on July 28, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post written by **Paramdeep** from Pristine__. Chandoo.org runs Financial Modeling School program in partnership with Pristine Careers. Visit [Financial Modeling School](http://chandoo.org/wp/financial-modeling/)
 to learn more and sign-up for our newsletter._

_**Who is not interested in buying a new house?**_ Owning a (at least the first one) house is like a dream come true for most! If you have ever bought (or thought of buying) a house in a building that is yet to be constructed, you would realize that there are clearly two parts of the business for the developer – the construction period (which is when the building is being built for the first 2-3 years) and the operations/ sales period (after the construction, they would sell or lease the building).

As we **[discussed last time](http://chandoo.org/wp/2011/02/08/introduction-to-project-finance-modeling-in-excel/ "Introduction to Project Finance using Excel")
**, one of the key aspects of any Infrastructure/ Real Estate Project is the long gestation period of the project. Typically in the construction period the project would utilize all the cash and when the operations/ sales period starts, the costs are almost zero as compared to the revenue being generated from the project.

![Typical Construction Project Timelines - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/01.typical-construction-project-timelines.png "Typical Construction Project Timelines - Project finance modeling in Excel")

### So what’s the big deal about the cash flow structure?

One of biggest concern in the construction period (Lets say it runs for 3 years) is that it consumes all your cash. If my total cost of building the project is going to be USD 30 Million (Spread equally over the three construction years), my Profit and Loss Statement would look something like:

### P&L (all figures in USD Mi)

![Typical Construction Project Timelines - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/01.typical-construction-project-profit-loss.png "Typical Construction Project Timelines - Project finance modeling in Excel")

But my building is not yet built (hence I cannot sell it), so I can take this as a Work In Progress (WIP) to my balance sheet (more about this can be learnt from accounting books and we would also be delving into this concept in detail in our training). But one thing is for sure, I would have a cash deficit of USD 10 Mn in the first year and a similar situation would continue for the first three years (till the point construction is complete and you start selling/ operations).

Typically, these projects also have a large amount of debt. For example, if I am expecting to construct the building for USD 30 Mn, I would try to take a bank loan of at least USD 20 Mn.

If you were a bank, the decision making of whether to lend money is taken on the interest and principal repaying capacity. If as a bank I analyze your P&L, I find that you have no cash to pay me my interest and principal! Traditional bankers lend you money ONLY if you can EASILY pay me back my money (typically look at a ratio of (interest + repayment) amount to the cash generated – called coverage ratio). If you can’t do that – I will not lend!

### So how do Banks view this?

As a banker, I understand that you are going to construct for 3 years and that is when you need my money (And would not be able to pay me interest). So I agree to not take interest and principal repayment as cash each year. But I cannot let go of this money!

Think of it as – I let you take additional loan to fund this payment! For example, let us assume:

Interest Rate prevailing: 10% per year

Loan amount in first year: USD 10 Mn

1.  So Interest on this loan: USD 1 Mn
2.  Now you can’t pay me back, so take additional loan (In first year itself) of USD 1 Mn
3.  That means total loan: USD 11 Mn (10 that you originally took and 1 that you took to pay the interest)
4.  That means interest is actually USD 1.1 Mn (Instead of the original 1 Mn)
5.  That means that effective loan: USSD 11.1 Mn (11 that we had calculated earlier and 0.1 to fund this gap)
6.  So interest: USD 1.11 Mn
7.  So effective Loan amount: USD 11.11

… and so on

There is a clear circular logic in this concept – My loan changes interest and interest changes loan

### Interpreting the circular logic

Summarizing our thoughts:

*   When an asset is developed, and there is a considerable period between the start of a project and its completion, the interest costs related to the construction are generally included in the cost of the asset, that is, the interest cost is capitalized
*   The capitalization period ends when the asset is ready for use
*   While modeling in excel, Interest During Construction (IDC) introduces a circular loop into the sheet due to the circular references explained below (1-2-3-4)

o Equity and Grant commitments can be either a specific amount, or a certain percentage of the total project funds required (that is, a fixed percentage in the capital structure)

![Interest During Construction Circular References Explained - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/02.interest-during-construction-circular-references-explained.png "Interest During Construction Circular References Explained - Project finance modeling in Excel")

\[Tip: [Learn more about Excel Circular References](http://chandoo.org/wp/2010/09/16/excel-circular-references/)\
.\]

### The Case – Modeling Interest During Construction in a typical Real Estate Project

Let us consider the construction period of a project at place X, where government wants to build a hospital.

The costs of the project are stated below:

![Interest During Construction Cost Of Project - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/03.interest-during-construction-cost-of-project.png "Interest During Construction Cost Of Project - Project finance modeling in Excel")

The government is ready to provide a grant of USD 50 Mn in the project and the project builder has to infuse equity of USD 100 Mn in the project  
![Interest During Construction Project Funding - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/04.interest-during-construction-project-funding.png "Interest During Construction Project Funding - Project finance modeling in Excel")

The shortfall in the funds can be funded through debt.

A complete model for financing has to be prepared for the construction period.

### The Concept

The basic concept behind the model is pretty simple

### **Total cash outflow in a year = Total Cash Inflow in the year**

1.  So the first step is to calculate the cash outflow in all the years. This cash outflow also includes the cost of paying the interest (which we would not know in the first pass).
2.  As a next step, we find the amount available to us through the equity and grants.
3.  We know that cash inflow has to be equal to cash outflow for all years.
4.  Whatever is the shortfall, we raise debt to fund it.
5.  Calculate the cumulative debt
6.  We calculate the interest on this debt.
7.  Whatever is the interest on the debt, we plug it back in the project cost (and hence introduce the circular logic in the model)

### Step I: Getting the Cash Outflow (Project Costs)

Based on the case, calculate the cash required in each year.

![Interest During Construction Calculating Cashflows 1 - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/05.interest-during-construction-calculating-cashflows-1.png "Interest During Construction Calculating Cashflows 1 - Project finance modeling in Excel")

We know the costs of each of the items and what should be the contribution in each year. Multiply the values to get the amounts in each year!

In the same step, we add all the costs (Including the Interest During Construction, though we don’t know it right now)

![Interest During Construction Calculating Cashflows 2 - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/06.interest-during-construction-calculating-cashflows-2.png "Interest During Construction Calculating Cashflows 2 - Project finance modeling in Excel")

### Step II: Getting the Cash Available (through Equity and Grants**)**

Based on the equity and grant infusion schedule, we calculate the cash inflows  
![Interest During Construction Calculating Cash Available 1 - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/07.interest-during-construction-calculating-cash-available-1.png "Interest During Construction Calculating Cash Available 1 - Project finance modeling in Excel")

### Step III: Cash Inflow = Cash Outflow

Since the cash outflow has to be matched with cash inflow, we make the total project cost in all years equal to funding in the year

![Interest During Construction Calculating Cashflows 3 - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/08.interest-during-construction-calculting-cashflows-3.png "Interest During Construction Calculating Cashflows 3 - Project finance modeling in Excel")

### Step IV: Fund the shortfall through debt

Since the only source to fund the shortfall is debt, lets raise the debt as the total fund needs less whatever is available through equity and grants

![Interest During Construction Finding The Shortfall - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/09.interest-during-construction-finding-the-shortfall.png "Interest During Construction Finding The Shortfall - Project finance modeling in Excel")

### Step V: Calculate the total debt outstanding

Since there is no way that we can pay the debt in the construction time, we make the outstanding debt as the cumulative debt raised (See me use a trick to accumulate!)

![Interest During Construction Total Debt Outstanding - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/10.interest-during-construction-total-debt-outstanding.png "Interest During Construction Total Debt Outstanding - Project finance modeling in Excel")

### Step VI: Calculate the interest on the debt

Since we have taken money from the bank, we need to pay an interest on it. The interest rate is given to us, let us link the amount to the interest to calculate the interest.  
![Interest During Construction On Debt - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/11.interest-during-construction-on-debt.png "Interest During Construction On Debt - Project finance modeling in Excel")

### Step VII: The Circular Logic (Plugging back the interest in the project cost)

Since the interest is also a cost of the project (and we are not paying it back to the bank each year), we take it to the project cost.

![Interest During Construction Error Output In The Model - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/12.interest-during-construction-error-output-in-the-model.png "Interest During Construction Error Output In The Model - Project finance modeling in Excel")

Out here, if you notice, excel starts a circular calculation and updates all the values! This can be verified by looking at the bottom left of excel and noticing this sign of “calculate”

![Calculating Interest During Construction - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/13.calculating-interest-during-construction.png "Calculating Interest During Construction - Project finance modeling in Excel")

### Beware! Circular References can be dangerous!

What we have achieved in this tutorial is one of the most intricate concepts in project finance -Interest During Construction (IDC). We have also used a fairly advanced function in excel – Circular loops. But please note that circular loops in excel is a dangerous tool. If by chance your excel sheet gets an erroneous value, the error would propagate through the model and there is no way for the model to recover back from the error, unless you know where the circular loop is and you delete and go back from there. For example, if I change 10% interest to “ten”,

![Interest During Construction Warnings 1 - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/14.interest-during-construction-warnings-1.png "Interest During Construction Warnings 1 - Project finance modeling in Excel")

I figure that my model is corrupt (It was expecting a numeric input and I gave a string!). But I can go back to 10%, my model does not go back!!

![Interest During Construction Writing The Circular Logic Formulas - Project finance modeling in Excel](https://chandoo.org/img/fm/pf2/15.interest-during-construction-writing-the-circular-logic-formulas.png "Interest During Construction Writing The Circular Logic Formulas - Project finance modeling in Excel")

I leave it as a homework for you to figure out, how to go back to a stable state!! 🙂

I will give you a trivial solution (close the sheet and open it again) :). You figure out, where the circular loop is and delete those lines and break it to come back!!

**_In the meanwhile, happy modeling!!_**

### Project Finance Modeling – Templates to download

I have created a template for you, where the assumption numbers are given and you have to link the complete model!

**[You can download the same from here](https://img.chandoo.org/fm/pf2/Q_IDC.xls)
.** You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can [**download this filled template**](https://img.chandoo.org/fm/pf2/A_IDC.xls)
 and check, if the information you recorded, matches mine or not! 🙂

I am just doing that for the single sheet model and recommend that you do the same for multi-sheet model as a homework problem. If you face any issue, post your excel with the exact problem and we can discuss the way to move forward.  
[![Project Finance Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/project-finance-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "Project Finance Modeling using Excel - Online Classes by Chandoo.org & Pristine")

### Next Steps

This series gives you a flavor of how project finance modeling is done and an idea about specific nuances in modeling for long gestation projects. I do hope to see you in the **[financial modeling school](http://chandoo.org/wp/financial-modeling/)
**.

### Join our Financial Modeling & Project Finance Classes

We are glad to inform that our new financial modeling & project finance modeling online class is ready for your consideration.

**[Please click here to learn more about the program & sign-up.](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
**  
For any queries regarding the cash impact or financial modeling, feel free to put the comments in the blog or write an email to [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/modeling-interest-during-construction/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/modeling-interest-during-construction/#respond)
    
*   Tagged under [circular formulas](https://chandoo.org/wp/tag/circular-formulas/)
    , [circular references](https://chandoo.org/wp/tag/circular-references/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [financial formulas](https://chandoo.org/wp/tag/financial-formulas/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [pristine](https://chandoo.org/wp/tag/pristine/)
    , [project finance](https://chandoo.org/wp/tag/project-finance/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousQuickly Compare Data using Row Differences](https://chandoo.org/wp/compare-data-row-differences/)

[NextPrinting Excel Reports via a Word DocumentNext](https://chandoo.org/wp/printing-excel-reports-via-a-word-document/)

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
    
    [Reply](https://chandoo.org/wp/modeling-interest-during-construction/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/modeling-interest-during-construction/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/modeling-interest-during-construction/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
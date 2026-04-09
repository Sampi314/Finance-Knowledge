# Building Inputs & Assumptions Sheets - Excel Financial Modeling - Part 3

**Source:** https://chandoo.org/wp/assumptions-financial-modeling-excel

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Building Inputs & Assumptions Sheets – Excel Financial Modeling \[Part 3 of 6\]
===============================================================================

*   Last updated on July 28, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post written by Paramdeep from [Pristine](http://edupristine.com/)
. Chandoo.org is partnering with Pristine to bring an excel financial modeling online training program for you._

### _![Building Inputs & Assumptions Sheets - Excel Financial Modeling Part 3 of 6](https://chandoo.org/img/fm/financial-model-assumptions-inputs.png)This is Part 3 of 6 on Financial Modeling using Excel_

**In this tutorial we are going to learn how to build assumptions & input sheets in our excel financial model.** The 6 parts of this tutorial are,

1.  [Introduction to Financial Modeling](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
    
2.  [Building a layout for Project Evaluation Model – Best practices](http://chandoo.org/wp/2010/07/28/financial-model-layout-best-practices/)
    
3.  **Building Inputs and Assumptions Sheet**
4.  [Building Projections for Project Evaluation](http://chandoo.org/wp/2010/09/02/modeling-cashflow-projections-for-project-evaluation/)
    
5.  [Modeling the Cash Flow Statement and Projections](http://chandoo.org/wp/2010/09/02/modeling-cashflow-projections-for-project-evaluation/)
    
6.  [Putting it all together – Final Project Evaluation Model](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
    
7.  **[Join our Financial Modeling Classes](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
    **

### First a story: Charlie and Chocolate Factory

> _**Would you invest in my chocolate factory?**_ It is just a $1,000 investment (And I would give you all the chocolate that you want for free!!)! I am going to produce 10,000 chocolates per year, which costs me $ 1,000 and I would be able to sell them for $ 1,010 in the market. Would you invest your money in my project?

You can just do a back of the envelop calculation to figure out that it would take me a hundred years to return back your money (Even if you were to charge no interest).

Believe me – Most of the decisions in finance are as simple as that! 😉 Its just that the numbers are obscure and figuring out the right numbers from the client takes a lot of time!

The first step for any meaningful evaluation is assimilating the facts CORRECTLY. In the world of finance (especially investment banking, equity research, etc.), for most of the analysis work you don’t need to be PHD material or a (ironically!!) researcher. Typically the work that is required to be done (as far as modeling in concerned) is quite routine. The skill that is highly in demand is consistency and an eye for detail.

As a banker your task starts by questioning each and every number that your client is giving you and recording it correctly. For comparisons, you start with ball park (industry) numbers and do some back of the envelop calculations to ascertain the feasibility of the project or the valuation numbers.

### Figuring out relevant information

In finance there are two cardinal rules:

*   Cash is the king
*   Cash today is more important than cash tomorrow

Whatever affects the above two is going to have an impact on the valuation of the firm. So while evaluating any business proposal (or company), you should record all the facts that affect the cash and its timing.

For example, if we were to just pick an instance from the case ([download here](https://img.chandoo.org/fm/financial-modeling-case.pdf)
), which reads as:

> I have done a thorough analysis and found out that the minimum initial investment needed in starting such kind of factory would be around **USD** **400 Mn (which includes the cost of machinery which has depreciation @ 20% every year and would also have a salvage value of 20mn after 10 years) and a starting working capital of $100mn which is 40% of revenue)**.

Then what is important from valuation perspective is the USD 400 Mn that goes out as investment (If it is all cash). Since it goes out on day 1, it is all the more important.

The depreciation is just an accounting concept (allocation of the huge cash that you invested to different accounting periods). It should have NO impact on the valuation of the project (as it does not affect the cash and also does not affect its timing). But when accountants create P&L, they deduct the depreciation from your EBITDA. So when you start the valuation, you should put that back in the cash available (and hence to record the information on depreciation).

Layout for Assumptions & Inputs
-------------------------------

Creating a layout which can help you record the cash and its timing in a structured manner can help you eliminate the possibility of errors in your model. Typically you can categorize the recording of information in the following heads:

*   ### **Initial investment that would be required to start the project (Investment decision)**
    

![Investment Assumptions - Financial Modeling using Excel](https://chandoo.org/img/fm/investment-assumptions-financial-modeling-excel.png)

*   ### **How much of money is locked in the business apart from the plant and machinery (Working capital as investment)**
    

![Working Capital Assumptions - Financial Modeling using Excel](https://chandoo.org/img/fm/working-capital-assumptions-financial-model-excel.png)

*   ### **How are you going to get your cash back (The operations)**
    

![Profit & Loss - Operations Assumptions - Financial Modeling using Excel](https://chandoo.org/img/fm/p-l-assumptions-excel-financial-modeling.png)

*   ### **How are you going to mix your equity and debt and what are the costs you pay for each**
    

![Valuation Assumptions - Financial Modeling using Excel](https://chandoo.org/img/fm/valuation-assumptions-financial-model.png)

Once you have recorded the relevant information, you should draw out the timing of cash as well to figure out the valuation.

### Templates to download

I have created a template for you, where the subheadings are given. You have to read the business case ([here](https://img.chandoo.org/fm/financial-modeling-case.pdf)
) and figure out which numbers go where. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

**[Download the blank assumptions sheet](http://chandoo.org/img/d/ProjectEvaluation-Building-assumptions-participant.xls "project evaluation - assumptions worksheet - blank")
**

**![Assumptions & Inputs Sheet - Blank - Financial Modeling using Excel](https://chandoo.org/img/fm/assumptions-worksheet-financial-modeling.png)  
**

Also you can download this filled template and check, if the information you recorded, matches mine or not!

**[Download the completed assumptions sheet](http://chandoo.org/img/d/ProjectEvaluation-Building-assumptions-solutionkey.xls "project evaluation - assumptions worksheet - filled")
**.

I am just doing that for the single sheet model and recommend that you do the same for multi-sheet model as a homework problem. If you face any issue, post your excel with the exact problem and we can discuss the way to move forward.  
[![Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/financial-modeling-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "inancial Modeling using Excel - Online Classes by Chandoo.org & Pristine")

### Next Steps

In the next installment, we would see, how we can calculate the cash that the project is going to earn in each financial period. It would mean using the recorded information and finding the items that contribute to cash change (and that don’t) and also the exact financial period, when that cash would flow in. For maximum benefit from the series, please try to fill it on your own and fill in the other parts of the model as well.

**Read previous part of this series – [Building a Layout for Valuation – Best Practices](http://chandoo.org/wp/2010/07/28/financial-model-layout-best-practices/)
**

### Join our Financial Modeling Classes

We are glad to inform that our new financial modeling & project finance modeling online class is ready for your consideration.

**[Please click here to learn more about the program & sign-up.](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
**

### How do you prepare assumptions sheet?

We are very eager to learn from. Tell us how you go about building assumptions sheet and how you switch between various assumption scenarios. **Please share using comments.**

### Added by Chandoo:

**Thank you Paramdeep & Pristine:**

Many thanks to Paramdeep and Pristine for making this happen. I am really enjoying this series and learning a lot of valuable tricks about financial modeling.

**If you like this series, say thanks to Paramdeep. I am sure he can take any amount of appreciation without choking.**

### Join our Newsletter

_**If you are new here, consider [joining my newsletter](http://feedburner.google.com/fb/a/mailverify?uri=PointyHairedDilbert&loc=en_US)
**, because I can send you updates when new articles are posted (plus you get a cool e-book with 95 excel tips, FREE)_

This article is written by [Pristine](http://edupristine.com/)
. The author can be contacted on [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)
.  
_Pristine is an awesome training institute for CFA, PRIMA, GARP etc. They have trained folks at HSBC, BoA etc. Chandoo.org is partnering with Pristine to bring an excel financial modeling online training program for you._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [17 Comments](https://chandoo.org/wp/assumptions-financial-modeling-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/assumptions-financial-modeling-excel/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pristine](https://chandoo.org/wp/tag/pristine/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow do you make charts when you have lots of small values but few extremely large values? \[Debate\]](https://chandoo.org/wp/charts-with-small-and-large-values/)

[NextExcel Everest – Recommended Excel Training ProgramNext](https://chandoo.org/wp/excel-everest-review/)

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
    
    [Reply](https://chandoo.org/wp/assumptions-financial-modeling-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/assumptions-financial-modeling-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/assumptions-financial-modeling-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
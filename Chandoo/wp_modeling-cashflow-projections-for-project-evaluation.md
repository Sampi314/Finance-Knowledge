# Modeling & Building Cash-flow Projections for Project Valuation - Financial Modeling using Excel - Part 4&5

**Source:** https://chandoo.org/wp/modeling-cashflow-projections-for-project-evaluation

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Modeling & Building Cash-flow Projections for Project Valuation \[Part 4,5 of 6\]
=================================================================================

*   Last updated on July 28, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post written by Paramdeep from [Pristine](http://edupristine.com/)
. Chandoo.org is partnering with Pristine to bring an excel financial modeling online training program for you._

### _![Modeling & Building Cash-flow Projections for Project Evaluation](https://chandoo.org/img/fm/modeling-cashflow-projections-project-valuation.png)This is Part 4 and 5 of 6 on Financial Modeling using Excel_

**In this tutorial we are going to learn how to build assumptions & input sheets in our excel financial model.** The 6 parts of this tutorial are,

1.  [Introduction to Financial Modeling](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
    
2.  [Building a layout for Project Evaluation Model – Best practices](http://chandoo.org/wp/2010/07/28/financial-model-layout-best-practices/)
    
3.  [Building Inputs and Assumptions Sheet](http://chandoo.org/wp/2010/08/23/assumptions-financial-modeling-excel/)
    
4.  **Building Projections for Project Evaluation**
5.  **Modeling the Cash Flow Statement and Projections**
6.  [Putting it all together – Final Project Evaluation Model](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
    
7.  **[Join our Financial Modeling Classes](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
    **

If you remember my last tutorial, I had discussed that there are just two cardinal rules:

*   Cash is the king
*   Cash today is more important than cash tomorrow

We will focus on the first principle today and we will delve in the second principle in the next tutorial to value the project.

**By far the most important exercise in any integrated (e)valuation model is to get your cash projections right.** This would mean going from your accounting profit (which is usually on [accrual basis](http://en.wikipedia.org/wiki/Comparison_of_Cash_Method_and_Accrual_Method_of_accounting)
) projection to the actual cash that the company would earn. One of the simplest examples would be:

Let’s say you buy a plant worth USD 1,000,000 in FY 10 in cash. Now this plant is going to give you benefit for the next 10 years. So it would be wise to allocate its cost to all the 10 years, when it’s going to give you the benefit! This allocation of cost to 10 years is called depreciation (which would be USD 100,000 per year for the next 10 years).

But please note – Although you are recognizing the costs in 10 years, but all your cash went out in the first year. Thus when you prepare the cash flow of the project you have to make these adjustments!

What all adjustments would be required?
---------------------------------------

*   All non cash expenses are added back to the profit  
    ![Add non cash expenses back - Modeling & building cashflow projections](https://chandoo.org/img/fm/add-non-cash-expenses-1.png)
*   All increase in liability is like a source of fund (cash up) and increase in assets takes away cash from you  
    ![Add non cash expenses back -2 - Modeling & building cashflow projections](https://chandoo.org/img/fm/add-non-cash-expenses-2.png)

### Updating the integrated model to incorporate investments

One of the huge cash flow that occurs in the project is due to the initial capital expenditure (capex). This would usually be an important part of cash flow in any manufacturing company. Apart from the initial capex, whenever you are investing in any competing business of your own, you also lose the opportunity to earn from that project.

Working capital investment also takes cash away from the company. This could comprise of investment in inventories, accounts receivables, etc. But please note that working capital by itself does not take away cash, **it is the increase in working capital that sucks cash.**

**![Investments - Modeling & Building Cash-flow Projections for Project Evaluation](https://chandoo.org/img/fm/modeling-investments-project-valuation.png)  
**

### Updating the integrated model to incorporate P&L for the project

Profit and loss statement gives indication of the business of the company. In our current evaluation model, we have assumed a starting revenue, and then a year on year growth in the revenue (Typically most of the models that you see in investment banking would make similar assumptions).

Variable expenses are assumed to be a %age of the revenues.

The important part to note while linking this part of the model is:

*   You should always link the numbers to the assumptions area (which is demarcated in blue font), so that if anybody wants to analyze any changes, they can easily do that
*   You should take care of the referencing ($ protection for rows and columns)

![Profit - loss - Modeling & Building Cash-flow Projections for Project Evaluation](https://chandoo.org/img/fm/modeling-profit-loss-project-valuation.png)

### Updating the integrated model to calculate the free cash flow to the project

The most important part of the model is to estimate the free cash flow to the project. As discussed earlier, adjustments have to be made to the PAT/ EBIT to get to the free cash flow.

I typically start here from Earning before Interest and Tax (EBIT) but if you want, you can start with PAT as well. Essentially the logic is that all the earnings before interest and tax go to the capital investors (Debt holders take interest and equity holders take the PAT). If I reduce from it the share of government, I am left with the portion of profit for the complete project – That is why you see the EBIT multiplied by (1- Tax Rate).

Again depreciation is added back as it is not a cash expense and Capex is reduced in the first year. Please note that this reduces the returns from the project as a huge cash is reduced in the first year itself, instead of equal small amounts being paid each year.

![Free Cash Flow - Modeling & Building Cash-flow Projections for Project Evaluation](https://chandoo.org/img/fm/modeling-free-cashflow-project-valuation.png)

### Templates to download

I have created a template for you, where the subheadings are given and you have to link the model to get the cash numbers! You can download the same from here**:**

**[Download Blank Cash-flow Projection Sheet](https://img.chandoo.org/d/ProjectEvaluation-Projecting-Cash-Participant.xls)
**

You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can download this filled template and check, if the information you recorded, matches mine or not!  **🙂**

**[Download Solution Cash-flow Projection Sheet](https://img.chandoo.org/d/ProjectEvaluation-Projecting-Cash-Solution-Key.xls)
  
**

I am just doing that for the single sheet model and recommend that you do the same for multi-sheet model as a homework problem. If you face any issue, post your excel with the exact problem and we can discuss the way to move forward.  
[![Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/financial-modeling-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "inancial Modeling using Excel - Online Classes by Chandoo.org & Pristine")

### Next Steps

In the last installment, we would see the impact of timing of cash and how the project can be valued. We would be using functions like NPV, IRR and analyzing the assumptions behind the same. For maximum benefit from the series, please try to fill it on your own and fill in the other parts of the model as well.

**Read next part of this series – [Putting it all together – Final Project Evaluation Model](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
**

### What best practices do you follow while making cash-flow projections?

We are very eager to learn from. Tell us how you go about modeling cash-flows? **Please share using comments.**

### Join our Financial Modeling Classes:

Chandoo.org is partnering with Pristine to bring an online financial modeling training program for you. **[Click here to know more & join our class](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
.**

### Added by Chandoo:

**Thank you Paramdeep & Pristine:**

Many thanks to Paramdeep and Pristine for making this happen. I am really enjoying this series and learning a lot of valuable tricks about financial modeling.

**If you like this series, say thanks to Paramdeep. I am sure he can take any amount of appreciation without choking.**

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

*   [10 Comments](https://chandoo.org/wp/modeling-cashflow-projections-for-project-evaluation/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/modeling-cashflow-projections-for-project-evaluation/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [online excel training](https://chandoo.org/wp/tag/online-excel-training/)
    , [pristine](https://chandoo.org/wp/tag/pristine/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to cook a delicious dynamic chart that will have your boss drool](https://chandoo.org/wp/dynamic-chart-with-check-boxes/)

[NextAugust 2010 – Best Month Ever (and 2 charting tips inside)Next](https://chandoo.org/wp/best-month-ever-aug/)

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
    
    [Reply](https://chandoo.org/wp/modeling-cashflow-projections-for-project-evaluation/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/modeling-cashflow-projections-for-project-evaluation/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/modeling-cashflow-projections-for-project-evaluation/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
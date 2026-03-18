# Reconcile debits & credits using Solver [Advanced Excel] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/reconcile-debits-credits-solver

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Reconcile debits & credits using Solver \[Advanced Excel\]
==========================================================

*   Last updated on August 18, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Here is a tricky problem often faced by accountants and finance professionals:** Let’s say you have 5 customers. Each of them need to pay you some money. Instead of paying the total amount in one go, they paid you in 30 small transactions. The total amount of these transactions matches how much they need to pay you. But you don’t know which customer paid which amounts. _**How would you reconcile the books?**_

If you match the transactions manually, it can take an eternity – after all there are more than 931 zillion combinations (5^30).

This is where solver can be handy. **Solver can find optimal solution for problems like this** before you finish your first cup of coffee.

Reconcile debits & credits using solver model – Tutorial
--------------------------------------------------------

### Step 1. Set up your solver model

In a blank sheet, list credits along a column and debits on the top in few columns, as shown below:

In the blank grid, Solver will fill 0 or 1 indicating whether credit in that row is matched with debit in that column or not.

This area is (C6:G35 in my workbook) is known as _variable cell range_ in Solver model.

There are 2 rules to be followed when matching debits to credits:

*   A credit can be matched with only one debit – _ie sum of any row in C6:G35 range can be 1, at most._
*   Total reconciled amount should be less than or equal to total credits – _ie sum of any column in C6:G35 should be less than values in C5:G5 (debits)._

To facilitate these rules, also known as _constraints_ in solver parlance, let’s use column H & row 36.

*   Write =SUM(C6:G6) in H6 and fill down the formula.
*   Write =SUMPRODUCT($B$6:$B$35,C$6:C$35) in C36 and drag sideways to fill the formula in rest of the columns.

**Our solver model should look like this:**

![reconcile-debits-credits-solver-model-workbook-screenshot](https://chandoo.org/wp/wp-content/uploads/2015/08/reconcile-debits-credits-solver-model-workbook-screenshot.png)

### Step 2: Set up optimization cell

To do its work, solver needs an optimization cell. Our goal is to maximize the amount of reconciled amount. So, in a blank cell write =SUM(C6:G36). This will be our optimization cell.

### Step 3: Launch solver

Select the optimization cell (in my workbook, this is J6) and go to Data > Solver. _(If you do not have solver,_ **[enable it using these instructions](http://chandoo.org/wp/2011/05/11/using-solver-to-assign-item/)
**.)

Set up solver model as:

1.  Objective is to to maximize J6.
2.  Variable cells are C6:G35
3.  Constraints
    *   C6:G35 should be binary (o or 1)
    *   C36:G36 should be <= C5:G5
    *   H6:H35 should be <= 1
4.  Solver method is **_Simplex LP_** (our problem is linear)

![match-debits-credits-solver-parameters](https://chandoo.org/wp/wp-content/uploads/2015/08/match-debits-credits-solver-parameters.png)

When you are ready, Click **Solve**. Solver should take few minutes to find the solution.

### Step 4: Examine the result

![solver-solution-reconcile-debits-credits](https://chandoo.org/wp/wp-content/uploads/2015/08/solver-solution-reconcile-debits-credits.png)

Once solver finds an answer, it will show **Solver Results** dialog. Click ok (you may also look at the sensitivity report). This loads the solver solution in to variable cell range.

![solver-solution-reconcile-debits-and-credits](https://chandoo.org/wp/wp-content/uploads/2015/08/solver-solution-reconcile-debits-and-credits.png)

Analyze the numbers and enjoy.

### What if Solver solution is not optimum?

Occasionally, Solver fails to find optimum solution for linear problems with integer constraints. In such cases, try again by adjusting constraints & precision.

Download example workbook
-------------------------

[**Please click here to download the example workbook**](https://chandoo.org/wp/wp-content/uploads/2015/08/reconcile-data.xlsx)
. Play with the solver model to learn more.

Other ways to reconcile data
----------------------------

If you deal with reconciliation problems, check out below examples to learn more:

*   [Match transactions using formulas](http://chandoo.org/wp/2014/06/06/matching-transactions-using-formulas-accounting/)
    
*   [Matching transactions using VBA macros](http://chandoo.org/wp/2014/06/10/matching-transactions-pivot-tables/)
    
*   [Compare 2 lists using Excel conditional formatting](http://chandoo.org/wp/2010/06/17/compare-2-lists-in-excel/)
    
*   [Introduction to VLOOKUP formula – the easiest way to reconcile data](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
    
*   [Use SUMPRODUCT to consolidate revenues](http://chandoo.org/wp/2011/07/12/sumproduct-function-to-consolidate-revenues/)
    

### How do you reconcile data?

Solver is a powerful way to reconcile data. It does take some time to set up the model and configure solver, but once your model is ready, Solver does all the heavy lifting.

**What about you?** What methods do you use to reconcile data? Please share your thoughts and tips in the comment section.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [11 Comments](https://chandoo.org/wp/reconcile-debits-credits-solver/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/reconcile-debits-credits-solver/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [awesome august](https://chandoo.org/wp/tag/awesome-august/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [reconcile](https://chandoo.org/wp/tag/reconcile/)
    , [solver](https://chandoo.org/wp/tag/solver/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousUse mail merge to create custom letters, invoices, labels and more](https://chandoo.org/wp/introduction-to-mail-merge/)

[NextGive descriptive titles to your charts for best resultsNext](https://chandoo.org/wp/descriptive-titles-on-charts/)

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

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ
# Create Cash Flow Forecast (Excel Tutorial + Template)

**Source:** https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial

---

How to Create a Cash Flow Forecast in Microsoft Excel
=====================================================

*   ![Jacek Polewski](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-0c5b42d9d6e4.png) [Jacek Polewski](https://www.challengejp.com/blog/author/adminchallengejp-com/ "Posts by Jacek Polewski")
    
*   September 14, 2020January 2, 2026

Last Updated on January 2, 2026

Building a solid Cash Flow Forecast is vital in business planning, especially when presenting your model to investors or managing funding needs over time.

In this guide, I’ll show you how to build a monthly cash flow forecast using Microsoft Excel. We’ll start by listing business drivers, then forecast revenues and costs, calculate funding requirements, and finally estimate investor returns using Excel formulas.

You’ll also learn how to test your model with scenario analysis and build out supporting financial statements.

You can [download my Cash Flow Forecast Template](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial#download-cash-flow-model-template)
 to follow the examples in this guide. Or [watch the video tutorial](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial#cash-flow-forecast-video-tutorial)
 at the end of this post.

Table of Contents

Toggle

Step 1. Define Key Business Drivers in Your Assumptions Sheet
-------------------------------------------------------------

Start by creating a dedicated **Assumptions Sheet** in your Excel workbook. This page becomes the foundation of your model and serves as a “control panel” for updating inputs later on.

For example, [my Cash Flow Forecast Template](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial#download-cash-flow-model-template)
 divides assumptions into key areas such as:

*   **General inputs** (e.g., start date, currency, forecast length),
*   **Revenue drivers** (e.g., units sold, pricing, sign-up fees),
*   **Cost drivers** (e.g., headcount, salaries, CAC, overhead).

Use a comment column to explain where each input comes from — historical data, market benchmarks, or experience.

[![Excel spreadsheet showing key business assumptions for cash flow forecast](https://www.challengejp.com/wp-content/uploads/2020/09/step1-cash-flow-assumptions.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step1-cash-flow-assumptions.png)

Screenshot #1: Cash flow assumptions sheet summarizing key drivers with explanations for each input.

Group smaller inputs under a single line, such as **Other Costs**, to avoid overcomplicating the model. You can break those out into detail on a supporting tab if needed.

Step 2. Build a Monthly Cash Flow Forecast Spreadsheet
------------------------------------------------------

Start your Cash Flow Forecast by building a monthly model on a dedicated spreadsheet. Place the **timeline** at the top and structure the rows into key forecast sections, such as:

*   Revenues,
*   Direct and general operating costs,
*   Headcount and salaries,
*   Capital expenditures (CAPEX).

Each section should begin with a relevant driver. For example, this could be monthly customer counts or units sold in the revenue section. Multiply those using the appropriate pricing input from your **Assumptions Sheet** to calculate forecast income.

[![Excel model linking user growth and revenue assumptions](https://www.challengejp.com/wp-content/uploads/2020/09/step2a-cash-flow-user-revenue.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step2a-cash-flow-user-revenue.png)

Screenshot #2a: User and pricing model for calculating monthly recurring revenue in the cash flow forecast.

Link all calculations directly to the assumptions tab so the model remains flexible and easy to audit.

[![Operating and capital cost forecast in Excel cash flow model](https://www.challengejp.com/wp-content/uploads/2020/09/step2b-cash-flow-model-excel.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step2b-cash-flow-model-excel.png)

Screenshot #2b: Operating and capital expense breakdown tied to employee headcount and inflation assumptions.

It’s best to use a **simple linear growth trend** and divide the forecast into phases (e.g., launch, ramp-up, maturity) rather than overcomplicating it with complicated growth formulas.

Turn on Excel’s **Freeze Panes** to improve usability so headers and timelines stay visible while scrolling.

📥 The revenue projections in [my Cash Flow Forecast Template](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial#download-cash-flow-model-template)
 include **sign-up fees** and **monthly recurring revenue**. You can modify or expand these based on your business model.

Step 3. Use Excel Formulas (SUM, IF, COUNTIFS) to Automate Your Forecast
------------------------------------------------------------------------

You only need a handful of Excel formulas to build a functional Cash Flow Forecast. In most cases, **SUM**, **IF**, **SUMIFS**, and **COUNTIFS** will cover nearly everything you need for revenue, cost, and summary calculations.

Use the IF formula to model conditional outcomes, such as pricing based on launch phase or discount scenarios. To roll monthly results into quarterly or annual summaries, use SUMIF or SUMIFS. Link the Year and Month rows to the formula criteria.

[![Excel SUMIF formula used in financial modeling](https://www.challengejp.com/wp-content/uploads/2020/09/step3-sumif-formula-excel.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step3-sumif-formula-excel.png)

Screenshot #3: Example of using the SUMIF function to aggregate monthly revenue by year.

There’s no need to over-engineer your model. Clear logic and transparency are preferable to overcomplicated formulas, primarily if someone else reviews or invests based on your spreadsheet.

More advanced functions like INDEX or OFFSET are occasionally helpful in consolidating projects or dynamic data pulls, but they aren’t critical for a solid first version.

Step 4. Summarize Forecasts with Charts and Error Checks
--------------------------------------------------------

Once your cash flow calculations are complete, summarize the results clearly and visually. Charts are beneficial for showing the big picture and making your model easy to explain.

For example, use Excel graphs to plot:

*   **Primary axis:** revenues and cumulative cash flow over time
*   **Secondary axis:** number of customers or units sold

This combination shows both financial performance and business growth in a single view.

💡 Use [Excel’s Copy as Picture](https://support.microsoft.com/en-us/office/create-a-picture-from-cells-a-chart-or-an-object-in-excel-5545100b-65f7-4caf-ac12-7a56f4a4e7b6#:~:text=Copy%20data%20as%20a%20picture,then%20click%20Copy%20as%20Picture.)
 feature to paste clean images into Microsoft PowerPoint or Word \[external link\].

It’s also important to build **internal checks** into your model. Add validation rows confirming the totals (like revenue or costs) match the detailed sheets, and the summary output – simple SUM and IF formulas should be enough to catch errors before they escalate.

[![Annual summary of forecast cash flow in Excel](https://www.challengejp.com/wp-content/uploads/2020/09/step4-cash-flow-model-summary.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step4-cash-flow-model-summary.png)

Screenshot #4: An example of an annual cash flow summary in [my model template](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial#download-cash-flow-model-template)
.

Organizing your forecast into summary tables and graphs makes it easier for your target audiences to understand and trust the projections.

Step 5. Forecast Equity Requirements and Use of Funds Breakdown
---------------------------------------------------------------

Once your cash flow forecast is complete, estimate the amount of external funding — usually equity — that the business will require.

[My Cash Flow Forecast Template](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial#download-cash-flow-model-template)
 calculates the **equity financing requirement** by deducting cumulative forecast revenues from cumulative costs up to the breakeven point. The funding gap represents the total amount of investment needed.

[![Equity funding requirements and use of funds breakdown in Excel](https://www.challengejp.com/wp-content/uploads/2020/09/step5-equity-requirement-use-funds.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step5-equity-requirement-use-funds.png)

Screenshot #5: Equity requirement calculation with cost allocation for planned funding use.

The above screenshot shows the **use of funds** breakdown based on cost categories. For example, if your forecast shows that 50% of early-stage costs are marketing expenses, allocate 50% of the investment raised to marketing.

Step 6. Estimate Enterprise Value Using DCF and EBITDA Multiples
----------------------------------------------------------------

Once the cash flow forecast and funding needs are precise, the next step is to estimate the **enterprise value** and potential **exit returns**.

For example, you could calculate enterprise value using two standard methods:

*   **Discounted Cash Flow (DCF):** Future free cash flows projected and discounted back to present value using a discount rate that reflects risk. Later years may use a lower rate as the business matures and risk decreases.
*   **EBITDA Multiplier:** The final year’s EBITDA multiplied by an industry-specific multiple to estimate the business’s sale value at exit. This method is more straightforward and intuitive, especially for investors familiar with standard valuation benchmarks.

[![Discounted Cash Flow model with terminal value in Excel](https://www.challengejp.com/wp-content/uploads/2020/09/step6-dcf-model-example.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step6-dcf-model-example.png)

Screenshot #6: DCF valuation model using discount rates and long-term growth assumptions.

Higher multipliers mean a stronger emphasis on future earnings and greater sensitivity to performance assumptions.

🌐 Remember to benchmark your model’s inputs (like the EBITDA multiplier) and results against the [industry’s peers](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html)
\[external link\].

Step 7. Add Financial Metrics: NPV, IRR, and Breakeven Points
-------------------------------------------------------------

To make your cash flow model investment-ready, add a summary of **key financial metrics**. These numbers help stakeholders evaluate your business plan’s potential risk and reward.

Important metrics to include:

*   **NPV (Net Present Value):** The value of future cash flows discounted to today, reflecting the time value of money and project risk.
*   **IRR (Internal Rate of Return):** Expresses the expected annualized return on equity investment.
*   **Equity Financing Requirement:** Total external funding needed based on forecast cash flows.
*   **Breakeven Points:** When the business achieves profitability (EBITDA breakeven) and cash flow positivity (Cash Flow breakeven).

You can calculate **NPV** and **IRR** directly in Microsoft Excel using the built-in NPV and IRR formulas.

[![Equity return metrics (IRR and NPV) in Excel cash flow model](https://www.challengejp.com/wp-content/uploads/2020/09/step7-cash-flow-returns.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step7-cash-flow-returns.png)

Screenshot #7: Equity return metrics including IRR and NPV based on projected financials.

Also, add margin percentages (e.g., Gross Margin, EBITDA Margin) alongside your revenue and cost projections to highlight business efficiency. Also, make sure your margins align with industry benchmarks — or be ready to explain why they differ.

🔍 _For a deeper dive into modeling IRR and NPV in project-based forecasts_, check out [my Project Finance Model tutorial](https://www.challengejp.com/blog/project-finance-model-excel-tutorial/)
.

Step 8. Run Sensitivity Analysis and Test Best/Worst Case Scenarios
-------------------------------------------------------------------

Once your forecast is complete, run a **sensitivity analysis** to understand how changes in key assumptions impact your financial outcomes.

For example, [my Cash Flow Forecast Template](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial#download-cash-flow-model-template)
 includes three input columns per driver in the **Assumptions Sheet** to easily switch between base case, upside, and downside scenarios. This setup makes it simple to test how adjusting **growth rates**, **pricing**, or **costs** affects cash flows and investor returns.

[![Scenario analysis sheet in Excel for sensitivity testing](https://www.challengejp.com/wp-content/uploads/2020/09/step8-cash-flow-scenarios.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step8-cash-flow-scenarios.png)

Screenshot #8: Scenario sheet with assumptions for testing base, best, and worst case cash flow impacts.

When choosing which assumptions to stress-test, focus on the drivers influencing your model’s results most. For example, a change in **customer acquisition cost** will often have a much greater impact on cash flows and funding needs than a slight variation in **staff salaries**.

Running a thoughtful **sensitivity analysis** improves the quality of your model and builds confidence with investors and stakeholders by showing that you have considered both upside potential and downside risks.

Step 9. Add Linked P&L, Balance Sheet, and Cash Flow Statements
---------------------------------------------------------------

Building a complete cash flow forecast also means including the three core **financial statements**:

*   **Profit and Loss Statement (P&L):** shows revenues, costs, and net profit over time.
*   **Balance Sheet:** tracks assets, liabilities, and equity, providing a snapshot of the business’s financial position.
*   **Cash Flow Statement:** categorizes cash movements into operations, investments, and financing activities.

[![Excel profit and loss statement with cash flow linkage](https://www.challengejp.com/wp-content/uploads/2020/09/step9-cash-flow-pnl-statement.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step9-cash-flow-pnl-statement.png)

Screenshot #9: Profit and loss statement with linked depreciation and capex from the cash flow sheet.

Link these statements dynamically within your financial model. For example, feed monthly **revenue forecasts** directly into the Profit & Loss Statement, and flow **capital expenditures** through both the Balance Sheet and the Cash Flow Statement. Adjust cash flow timing based on changes in **working capital** items such as receivables and payables.

Step 10. Add Debt Financing: Interest, Repayments, and Impact on Returns
------------------------------------------------------------------------

After building an equity-funded forecast, adding **debt financing** to your cash flow model is often valuable. Properly modeling debt allows you to lower the upfront equity requirement and improve overall return metrics.

When modeling debt, make sure to include:

*   **Interest calculations:** based on the outstanding loan balance and the applicable interest rate.
*   **Debt amortization:** scheduled principal repayments over time, using a structure like equal monthly payments or a balloon repayment at maturity.
*   **Impact on financial statements:** interest expenses should flow into the P&L, while principal repayments affect the Balance Sheet and the financing section of the Cash Flow Statement.

[![Debt financing model with interest and repayment in Excel](https://www.challengejp.com/wp-content/uploads/2020/09/step10-cash-flow-debt-model-example.png)](https://www.challengejp.com/wp-content/uploads/2020/09/step10-cash-flow-debt-model-example.png)

Screenshot #10: Debt forecast illustrating interest expense and principal repayments in [my cash flow forecast model](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial#download-cash-flow-model-template)
.

Adding debt affects both cash flow dynamics and return metrics. While it usually reduces the **Equity Financing Requirement** and enhances **Return on Equity (ROE)**, it also creates fixed repayment obligations that the business must meet even during downturns.

📊 See [**my Financial Model with Debt Financing**](https://www.challengejp.com/blog/financial-model-debt-financing-excel-tutorial/)
 tutorial for another example of modeling repayment schedules and investor returns.

📌 Recap: 10 Steps to Build a Cash Flow Forecast Spreadsheet
------------------------------------------------------------

Follow these 10 essential steps to create a complete, flexible cash flow forecast in any spreadsheet tool:

1.  **Define Business Drivers and Set Up the Assumptions Sheet.** Organize all key inputs — pricing, units sold, headcount, and forecast timeline — in a centralized assumptions tab.
2.  **Build a Monthly Cash Flow Forecast Spreadsheet.** Structure your forecast across a multi-month timeline, linking revenues, costs, salaries, and CAPEX.
3.  **Use Key Formulas (SUM, IF, COUNTIFS) to Automate Forecasting.** Keep calculations clean and transparent using simple, reliable formulas for flexible modeling.
4.  **Summarize Forecasts with Charts and Error Checks.** Use tables and graphs to visualize trends, and add validation checks to ensure data consistency.
5.  **Forecast Equity Requirements and the Use of Funds Breakdown.** Calculate your total funding need and show capital allocation across major cost categories.
6.  **Estimate Enterprise Value (DCF & EBITDA Multiples).** Project potential exit value using discounted cash flow analysis and industry valuation benchmarks.
7.  **Add Financial Metrics (NPV, IRR, Breakeven Points).** Include investor-focused metrics to highlight returns, risk, and financial performance.
8.  **Run Sensitivity Analysis with Upside/Downside Scenarios.** Stress-test your model by adjusting key assumptions and measuring the impact on cash flow and returns.
9.  **Add Linked P&L, Balance Sheet, and Cash Flow Statement.** Build the three core financial statements with dynamic links to reflect model assumptions.
10.  **Add Debt Financing (Interest, Repayments & Loan Impact).** Model optional loans to reduce equity needs and evaluate how debt affects cash flow and return metrics.

📥 Download My Cash Flow Forecast Template
------------------------------------------

This is the Excel model used throughout the tutorial—built to help you structure monthly forecasts, assess funding needs, and analyze equity returns. It’s fully linked, editable, and ready to customize for your projects.

The file includes all core components of a complete financial forecast:

*   **Assumptions Sheet** — centralizes all model inputs for easy edits.
*   **Cash Flow Model** — monthly revenues, costs, salaries, and capex forecasts.
*   **Use of Funds** — calculation of funding requirements and allocation.
*   **Financial Statements** — linked Profit and Loss, Balance Sheet, and Cash Flow Statement.
*   **Equity Returns and Valuation** — IRR, NPV, DCF, and enterprise value calculations.
*   **Debt Modeling** — optional debt financing layer with repayment calculations.
*   **Sensitivity Analysis** — scenarios built into the model structure.

$43.36 AUD – Download My Cash Flow Forecast Template  
Secure Checkout | Instant Download | 30-Day Money-Back Guarantee

  

[€24.00 – Download My Cash Flow Forecast Template](https://www.challengejp.com/checkout/?add-to-cart=1964)
  
Secure Checkout | Instant Download | 30-Day Money-Back Guarantee

The file is in Excel format, but you can easily convert it to Google Sheets if needed.

👁️ **[View full template details](https://www.challengejp.com/product/cash-flow-forecast-template/)
**

Video Tutorial on How to Use the Cash Flow Forecast Template
------------------------------------------------------------

Follow along step-by-step in my complete video tutorial, where I show you how to build and customize a Cash Flow Forecast using Microsoft Excel. In the video, you’ll learn:

*   How to structure your timeline and financial drivers.
*   How to link key assumptions to dynamic cash flow outputs.
*   How to model funding needs, including debt financing scenarios.
*   How to stress-test your model and prepare it for presentation.

By the end of the tutorial, you’ll know how to use my Cash Flow Forecast Template to plan liquidity needs and communicate financial projections.

▶️ [Watch on YouTube](https://youtu.be/MZP4xHw5yzU)

<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span>﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span>﻿</span>

Get in Touch
------------

[![jacek polewski challengejp](https://www.challengejp.com/wp-content/uploads/2020/07/jp_photo-300x200.jpg)](https://www.challengejp.com/about/)
Hi, I’m Jacek. I help businesses and investors build practical and easy-to-use spreadsheet models.

If you have questions about Cash Flow Forecasting, financial modeling, or Excel best practices, feel free to [get in touch](https://www.challengejp.com/contact/)
.

You can also explore my [One-to-One Financial Modeling Training](https://www.challengejp.com/services/financial-modelling-data-training/)
 or [Financial Modeling Services](https://www.challengejp.com/services/financial-modelling/)
 if you need personalized support.

Explore Other Tutorials
-----------------------

Continue building your skills with these tutorials:

*   [**Merger and Acquisition Model**](https://www.challengejp.com/blog/merger-acquisition-model-excel-tutorial/)
     — Models post-deal cash flows, synergies, and funding strategies.
*   [**Capital Investment Plan**](https://www.challengejp.com/blog/capital-investment-plan-excel-tutorial/)
     — Connects capex phasing to cash flow and full P&L structure.
*   [Project Finance Model](https://www.challengejp.com/blog/project-finance-model-excel-tutorial/)
     — Build a complete project finance model in Excel, including cash flow, debt, and return analysis.
*   [Power BI Financial Planning & Analysis Dashboard Tutorial](https://www.challengejp.com/blog/power-bi-financial-planning-analysis-dashboard-tutorial/)
     — Build a fully integrated FP&A model in Microsoft Power BI, combining P&L, cash flow, balance sheet, and forecasting logic into a dynamic planning dashboard.
*   [**Power BI Sales Analysis & Forecast Dashboard Tutorial**](https://www.challengejp.com/blog/power-bi-sales-analysis-forecast-dashboard-tutorial/)
     — builds a full sales reporting and forecasting model in Microsoft Power BI with DAX measures, product-level KPIs, and interactive what-if parameters.

[→ View all tutorials](https://www.challengejp.com/services/tutorials/)

Tags:[Cash Flow Forecasting](https://www.challengejp.com/blog/tag/cash-flow-forecasting/ "Cash Flow Forecasting")
[Excel Tutorial](https://www.challengejp.com/blog/tag/excel-tutorial/ "Excel Tutorial")
[Financial Modelling](https://www.challengejp.com/blog/tag/financial-modelling/ "Financial Modelling")

1 thought on “How to Create a Cash Flow Forecast in Microsoft Excel”
--------------------------------------------------------------------

1.  ![](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-2caa84dbc2e6.png)
    
    Annaline [April 11, 2021 at 9:20 am](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial/#comment-930)
    
    Thank You !!!
    

Comments are closed.

  

**Redirecting to FastSpring for secure payment and local tax handling in your region...**

You’ll see challengejp.onfastspring.com in your address bar.
# Real Estate Investment Forecast (Excel Tutorial + Template)

**Source:** https://www.challengejp.com/blog/how-to-create-real-estate-investment-model-excel-tutorial

---

How to Create a Real Estate Investment Forecast
===============================================

*   ![Jacek Polewski](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-0c5b42d9d6e4.png) [Jacek Polewski](https://www.challengejp.com/blog/author/adminchallengejp-com/ "Posts by Jacek Polewski")
    
*   June 30, 2022January 2, 2026

Last Updated on January 2, 2026

Building a Real Estate Investment Forecast in Microsoft Excel will help you forecast cash flows, evaluate profitability, and analyze returns. In this tutorial, I’ll guide you step-by-step — from building a rental and sales forecast to projecting operational, investment, and financing cash flows.

Finally, you’ll also learn how to estimate investment returns, stress-test your model, and build a balance sheet that connects everything.

To follow along, you can [download my Real Estate Investment Model Template](https://www.challengejp.com/blog/how-to-create-real-estate-investment-model-excel-tutorial#download_real_estate_investment_model_template)
. For a full walkthrough, [watch the video tutorial](https://www.challengejp.com/blog/how-to-create-real-estate-investment-model-excel-tutorial#real_estate_investment_model_video_tutorial)
 at the end of this post.

Table of Contents

Toggle

Step 1. Forecast Property Construction Timeline and Unit Completions
--------------------------------------------------------------------

The first step in building a Real Estate Cash Flow Model is to set up a **monthly construction timeline**. Create a spreadsheet that shows how the property build progresses month by month.

Start by setting a **target number of properties** to complete, defining the **construction period**, and phasing the build so that some properties can generate income before the project’s completion.

You can split property cash flows into two categories:

*   **Sales Income** — proceeds from selling properties shortly after completion.
*   **Property Rental** — monthly income generated from rented units.

[![Real estate property build progress forecast in Excel](https://www.challengejp.com/wp-content/uploads/2022/06/step1-property-build-progress.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step1-property-build-progress.png)

Screenshot #1: The model phases monthly property completions to drive revenue, cost, and investment projections.

Calculate completed units by multiplying the **number of addressable properties** by a **build progress rate** — creating a dynamic foundation for revenue forecasting.

Step 2. Project Monthly Rental Income from Properties
-----------------------------------------------------

After building your construction timeline, the next step is forecasting **rental revenues**. To calculate monthly rental income, multiply the completed properties by the **average monthly rent** per unit.

To calculate the average monthly rent, [my real estate model](https://www.challengejp.com/blog/how-to-create-real-estate-investment-model-excel-tutorial#download_real_estate_investment_model_template)
 multiplies **the annual yield percentage assumption** and a property’s **average open market value**. Dividing the result by twelve gives the estimated monthly rent.

For example, if the open market value of a property is $240,000 and the assumed yield is 5.0%, the monthly rental income would be $1,000:

_(5.0% × $240,000) ÷ 12 = $1,000._

[![Real estate rental income forecast based on yield](https://www.challengejp.com/wp-content/uploads/2022/06/step2-real-estate-income-forecast.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step2-real-estate-income-forecast.png)

Screenshot #2: Rental revenue is calculated using property market value and a target yield to derive monthly rental income.

Increase the rental income over time in line with **property value appreciation**, keeping future cash flows realistic.

Step 3. Estimate Fixed and Variable Rental Operating Costs
----------------------------------------------------------

After forecasting rental income, the next step is to project **operating costs** for your real estate investment. Operating expenses generally fall into two categories: **variable costs** and **fixed costs**.

Variable costs change with growth and depend on the number of properties rented or sold. For example, you could calculate **property maintenance expenses** by multiplying the number of rented units and an assumed cost per unit, making them a variable expense in the cash flow forecast.

Fixed costs, on the other hand, are more stable. Multiply the overall headcount by an **average monthly salary** to calculate central staffing costs. These costs are treated as fixed expenses because they are less sensitive to short-term changes in the number of rented properties.

[![Real estate operating cost forecast including salaries and maintenance](https://www.challengejp.com/wp-content/uploads/2022/06/step3-rental-operating-expenses-forecast.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step3-rental-operating-expenses-forecast.png)

Screenshot #3: This expense forecast separates fixed staff costs from variable rental operating expenses linked to property count.

To keep forecasts realistic, include **inflation adjustments** for both variable and fixed costs.

Step 4. Forecast CAPEX Based on Property Build Schedule
-------------------------------------------------------

Forecasting **capital expenditure (CAPEX)** is a key part of any real estate investment model. To estimate monthly build costs, multiply the total number of planned units by the **average construction cost per unit** and spread the resulting expenses across the construction timeline.

For example, if the project involves building 100 properties at an average cost of $240,000 each, and the construction takes 24 months, the monthly capital expense would be $1,000,000:

_(100 units × $240,000 per unit ÷ 24 = $1,000,000 per month)._

[![Monthly capex projection in a real estate model](https://www.challengejp.com/wp-content/uploads/2022/06/step4-real-estate-capex-model.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step4-real-estate-capex-model.png)

Screenshot #4: The forecast spreads capex based on units built per month and an average construction cost per property.

The above example assumes that overall build costs are distributed linearly over time, although you could apply more advanced phasing if needed.

🏗️ _To see how construction phasing and capital forecasts work in other industries,_ my [Capital Investment Plan tutorial](https://www.challengejp.com/blog/capital-investment-plan-excel-tutorial/)
 walks through project-based CAPEX models.

Step 5. Project Property Sales Revenues and Net Profit
------------------------------------------------------

Many real estate projects generate cash flow through **property sales** and rental income. Allocate a portion of completed properties to a for-sale pool and estimate the sales proceeds by multiplying the properties sold and the **average open market value**.

[My Real Estate Investment Model Template](https://www.challengejp.com/blog/how-to-create-real-estate-investment-model-excel-tutorial#download_real_estate_investment_model_template)
 uses a mix of two approaches to capture the associated expenses:

*   **Property sale costs calculated as a percentage of gross revenue** — with a set portion of the selling price deducted as an expense,
*   **Fixed property sale cost per unit** — with a set dollar amount for each sale.

[![Real estate cash flow from property sales in Excel](https://www.challengejp.com/wp-content/uploads/2022/06/step5-real-estate-sale-cash-flow.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step5-real-estate-sale-cash-flow.png)

Screenshot #5: Sales cash flow combines unit sales, market value, build cost, and sales expenses to estimate net profit.

Estimate the **capital cost basis** by multiplying the number of properties sold by their historical build cost. Finally, calculate the **sales profit** by subtracting both direct selling costs and original build costs from the total sales proceeds.

💼 _For examples of modeling cash inflows from multiple sources,_ see my [Project Finance Model tutorial](https://www.challengejp.com/blog/project-finance-model-excel-tutorial/)
 — especially useful if your project includes multiple cash flow sources.

Step 6. Analyze Rental Property Profitability and Payback
---------------------------------------------------------

Understanding the **profitability** of each rental property is critical for evaluating the success of a real estate investment. To do this, create a simple calculator that compares the **average rental revenues** to the **average operating costs** per unit.

Create a link to rental income and cost assumptions to estimate the **net annual revenue** generated by each property. Depending on whether you want a pure cash flow view or an accounting-based analysis, you can include or exclude **depreciation charges** from the calculation.

[![Real estate rental profitability and payback calculator](https://www.challengejp.com/wp-content/uploads/2022/06/step6-real-estate-investment-calculator.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step6-real-estate-investment-calculator.png)

Screenshot #6: This profitability calculator in [my real estate model](https://www.challengejp.com/blog/how-to-create-real-estate-investment-model-excel-tutorial#download_real_estate_investment_model_template)
 shows investment breakeven and rental income per unit using yield and cost inputs.

Finally, estimate **breakeven metrics**, showing how long it takes to recover the initial construction cost through net rental income. Notice that occupancy rates and **average rental periods** can significantly impact payback time and investment profitability.

Step 7. Add Debt Financing and Build Levered vs Unlevered Cash Flows
--------------------------------------------------------------------

Including **debt financing** in a real estate investment model can significantly lower the upfront **equity requirement**, making projects more feasible. Adding debt will reduce the initial cash outlay but introduce **future obligations** through loan repayments and interest expenses.

Produce two versions of monthly cash flows:

*   **Unlevered Cash Flows** — reflecting revenues and costs without considering any debt financing,
*   **Levered Cash Flows** — incorporating the effects of loans with drawdowns, interest expenses, and principal repayments.

[![Real estate cash flow with and without debt financing](https://www.challengejp.com/wp-content/uploads/2022/06/step7-real-estate-cash-flow-forecast.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step7-real-estate-cash-flow-forecast.png)

Screenshot #7: Unlevered and levered cash flows compare investment requirements and debt servicing impacts over time.

📥 Download [my Real Estate Investment Model Template](https://www.challengejp.com/blog/how-to-create-real-estate-investment-model-excel-tutorial#download_real_estate_investment_model_template)
 and see how to customize key loan parameters, including percentage of build costs financed by debt, interest rate, loan term, and repayment periods.

Step 8. Build a Linked Balance Sheet for the Real Estate Project
----------------------------------------------------------------

A complete **real estate investment model** should include a **balance sheet** that ties together cash flows, profits, assets, and liabilities. To build a balance sheet in Excel, make sure that the **Cash Flow Statement** and the **Profit and Loss Statement** are fully interconnected — so that changes in one area automatically update the others.

Firstly, link the **capital expenditure** forecast from the investment cash flows to the asset side of the balance sheet. Then, adjust the resulting figure for **depreciation** based on the Profit and Loss calculations.

[![Real estate investment balance sheet template](https://www.challengejp.com/wp-content/uploads/2022/06/step8-real-estate-balance-sheet.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step8-real-estate-balance-sheet.png)

Screenshot #8: This balance sheet model tracks assets from capital expenditure and adjusts liabilities through loan drawdowns and repayments.

Finally, on the liabilities side, track **long-term debt** by adding any new debt raised and subtracting principal repayments. Interest expenses flow through to retained earnings to ensure the balance sheet’s reconciliation.

Additionally, depending on the accounting rules, you may need to allocate some **property build costs** to **inventory (stock)** for properties intended for sale.

🔍 _For a clear overview of accounting treatment for properties intended for sale,_ this [guide on Stock vs. Inventory](https://www.educba.com/stock-vs-inventory/)
 \[external link\] outlines key differences.

Step 9. Evaluate Cash Flows and ROI with IRR, NPV, and Terminal Value
---------------------------------------------------------------------

Once your cash flow projections are complete, the next step is to evaluate the cash flow forecast and **investment returns**.

Firstly, organize the model’s output into three standard cash flows from:

*   **Operations**, summarizing inflows and outflows from rental activities, maintenance expenses, staff salaries, administrative costs, and property sales adjustments.
*   **Investment**, covering capital expenditures and proceeds from property sales.
*   **Financing**, capturing debt funding, principal repayments, and equity injections.

[![Cash flow from operations in a real estate investment model](https://www.challengejp.com/wp-content/uploads/2022/06/step9a-real-estate-operations-cash-flow.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step9a-real-estate-operations-cash-flow.png)

Screenshot #9a: This statement summarizes net operating cash flows adjusted for depreciation, interest, and sales gains/losses.

There are a few methods to value a real estate project. For example, you could divide the **rental revenue or income** by a **rental yield assumption** to calculate **the terminal value** and estimate the project’s long-term value.

[![Real estate return analysis using IRR and NPV](https://www.challengejp.com/wp-content/uploads/2022/06/step9b-real-estate-investment-return-analysis.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step9b-real-estate-investment-return-analysis.png)

Screenshot #9b: This return analysis in [my real estate model](https://www.challengejp.com/blog/how-to-create-real-estate-investment-model-excel-tutorial#download_real_estate_investment_model_template)
 calculates terminal value from rental yields and uses Excel’s IRR and NPV functions to assess investment performance.

Step 10. Stress Test Assumptions with Sensitivity Analysis
----------------------------------------------------------

The final step in building your real estate model is to **stress-test your assumptions** and understand its sensitivity to key variables like market prices, interest rates, or build costs.

Start by placing your main model inputs next to the cash flow summary so you can see the impact of changes in real-time. Then, test different scenarios and analyze how shifting one or more assumptions impacts outputs such as equity requirements or return metrics.

[![Excel data table sensitivity analysis for real estate](https://www.challengejp.com/wp-content/uploads/2022/06/step10-real-estate-investment-sensitivity-analysis.png)](https://www.challengejp.com/wp-content/uploads/2022/06/step10-real-estate-investment-sensitivity-analysis.png)

Screenshot #10: This Excel data table evaluates how key assumptions—like interest rate or property costs—impact IRR and equity needs.

Use Excel’s built-in **data tables** to summarize the results. For example, test how the **interest rate** and **property build cost** affect the **required equity** and the **internal rate of return (IRR)**.

📌 Recap: 10 Steps to Build a Real Estate Investment Forecast
-------------------------------------------------------------

Here’s a recap of the steps covered in this tutorial — from forecasting build progress to calculating returns and testing your assumptions:

1.  **Forecast Property Construction Timeline.** Map out how many units will be completed each month across the project duration.
2.  **Project Rental Income from Properties.** Estimate monthly rental revenues based on property value and yield assumptions.
3.  **Estimate Rental Property Operating Costs.** Forecast both fixed and variable expenses, such as maintenance and staffing.
4.  **Forecast Property Capital Investment (CAPEX).** Calculate total construction costs and spread them over the build timeline.
5.  **Project Sales Revenues from Property Disposals.** Estimate cash inflows from sold units, adjusted for cost and profit margin.
6.  **Analyze Rental Property Profitability.** Build a calculator to assess net income and payback period per rental unit.
7.  **Add Debt Financing to Your Real Estate Model.** Reduce upfront equity needs and account for loan repayments and interest.
8.  **Build a Balance Sheet for Your Real Estate Project.** Tie together assets, liabilities, and retained earnings with linked statements.
9.  **Evaluate Cash Flows and ROI from Your Real Estate Project.** Use NPV, IRR, and terminal value to assess long-term profitability.
10.  **Stress-Test Your Real Estate Financial Model.** Examine how key assumptions affect cash flow, risk exposure, and investor returns.

📥 Download My My Real Estate Investment Model Template
-------------------------------------------------------

This is the complete Excel model used in the tutorial—pre-built to forecast property construction, rental income, sales revenues, financing, and returns. All statements are linked and automated, so you can focus on adjusting assumptions and analyzing results.

The file includes:

*   **Monthly Cash Flow Forecast** — covers rental and sales income, plus all associated costs.
*   **Debt Financing Schedule** — with principal repayments, interest, and loan fees.
*   **Depreciation and Tax Tabs** — split by rental and for-sale units.
*   **Annual Profit & Loss and Balance Sheet** — tracking long-term asset value and liabilities.
*   **Rental Profitability Calculator** — analyzes an average property’s return and breakeven period.
*   **Built-In Sensitivity Analysis** — easily stress-test your key assumptions.

$57.82 AUD – Download My Real Estate Investment Model Template  
Secure Checkout | Instant Download | 30-Day Money-Back Guarantee

  

[139.00zł – Download My Real Estate Investment Model Template](https://www.challengejp.com/checkout/?add-to-cart=2912)
  
Secure Checkout | Instant Download | 30-Day Money-Back Guarantee

The template is in Excel format and easily convertible to Google Sheets if needed.

👁️ **[View full template details](https://www.challengejp.com/product/real-estate-investment-model-template/)
**

Video Tutorial on Using the Real Estate Investment Model
--------------------------------------------------------

You can follow along with my complete video walkthrough, where I explain step by step how to use the Real Estate Investment Model Template.

In this video, I cover:

*   How to phase property construction and link it to rental and sales forecasts.
*   How to estimate CAPEX, operating costs, and profitability per property.
*   How to integrate loans, depreciation, and tax into a complete model.
*   How to calculate IRR, NPV, and stress test your assumptions using data tables.

▶️ [Watch on YouTube](https://youtu.be/CkVrHx-nT1Q)

<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span>﻿</span>

Get in Touch
------------

Hi, I’m Jacek. I’m passionate about building financial models that work. I hope this tutorial helped you better understand how to create a Real Estate Investment Forecast.

Feel free to [reach out](https://www.challengejp.com/contact/)
 if you have questions about financial modelling, Excel techniques, or structuring forecasts for your projects.

You can also explore my [other tutorials](https://www.challengejp.com/services/tutorials/)
 or check out my [**One-to-One Training**](https://www.challengejp.com/services/financial-modelling-data-training/)
 and [**Financial Modeling Services**](https://www.challengejp.com/services/financial-modelling/)
 for personalized support.

_Disclaimer: This tutorial is for informational and educational purposes only and should not be considered professional advice._

Explore More Financial Modeling Tutorials
-----------------------------------------

Want to dive deeper into financial modelling? Here are more tutorials you might find helpful:

*   [**Capital Investment Plan**](https://www.challengejp.com/blog/capital-investment-plan-excel-tutorial/)
     — Translate capital expenditures into long-term revenue and cash flow forecasts.
*   [**Project Finance Model**](https://www.challengejp.com/blog/project-finance-model-excel-tutorial/)
     — Understand how to consolidate multiple real estate or infrastructure projects under one financial model.
*   [**Telecom Investment Model**](https://www.challengejp.com/blog/telecom-financial-model-excel-tutorial/)
     — Forecast customer growth, build infrastructure CAPEX plans and calculate investment returns.
*   [**Cash Flow Forecast in Microsoft Excel**](https://www.challengejp.com/blog/cash-flow-forecast-excel-tutorial/)
     — Learn how to project revenues, costs, and working capital for dynamic forecasting.
*   [**Financial Model with Debt Financing**](https://www.challengejp.com/blog/financial-model-debt-financing-excel-tutorial/)
     — Add loans to your model and track repayments, interest, and equity requirements.

[→ View all tutorials](https://www.challengejp.com/services/tutorials/)

Tags:[Cash Flow Forecasting](https://www.challengejp.com/blog/tag/cash-flow-forecasting/ "Cash Flow Forecasting")
[Excel Tutorial](https://www.challengejp.com/blog/tag/excel-tutorial/ "Excel Tutorial")
[Financial Modelling](https://www.challengejp.com/blog/tag/financial-modelling/ "Financial Modelling")

  

**Redirecting to FastSpring for secure payment and local tax handling in your region...**

You’ll see challengejp.onfastspring.com in your address bar.
# Subscription Model Forecast (Excel Tutorial + Template)

**Source:** https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation

---

How to Create a Subscription Model Forecast with Churn Calculations
===================================================================

*   ![Jacek Polewski](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-0c5b42d9d6e4.png) [Jacek Polewski](https://www.challengejp.com/blog/author/adminchallengejp-com/ "Posts by Jacek Polewski")
    
*   May 26, 2021January 2, 2026

Last Updated on January 2, 2026

In this step-by-step tutorial, you’ll learn how to build a Subscription Model Forecast with Churn Calculations using Microsoft Excel.

We’ll start by forecasting customer acquisition and growth. Then, we’ll walk through how to estimate customer churn, calculate customer lifetime value (LTV), and understand their impact on cash flow and equity returns.

You can [download my Subscription Model Template](https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation#download_subscription_model_template)
 to follow along with the same spreadsheet and examples used in this guide. Or [watch the video tutorial](https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation#subscription_model_video_tutorial)
 at the end of this post.

Table of Contents

Toggle

Step 1. Forecast Customer Acquisition and User Growth
-----------------------------------------------------

Your customer numbers form the foundation of any subscription model, so let’s start by building a **customer acquisition forecast**.

Open your spreadsheet and show how your user base will grow over time. Begin with **month-over-month growth** to keep the forecast simple. Once the basic model works, you can experiment with more advanced growth curves.

Break down monthly customer data into key categories:

*   **Acquired Customers** – New users or subscribers who joined during a specific month,
*   **Churned Customers** – Users who unsubscribed or left your service,
*   **Upgrades/Downgrades** – Users who switched between subscription tiers (e.g., moving from a basic plan to a premium one).

For example, start with 500 new subscribers and increase them monthly using a fixed growth rate. You can also include a growth period assumption after which the model naturally flattens, simulating market saturation.

[![An example of a customer acquisition model in Excel.](https://www.challengejp.com/wp-content/uploads/2021/05/step1-customer-acquistion-model.png)](https://www.challengejp.com/wp-content/uploads/2021/05/step1-customer-acquistion-model.png)

Screenshot #1: An example of a Customer Acquisition Forecast in [my subscription model](https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation/)
. The spreadsheet assumes subscribers on two pricing plans and estimates retention, churn, and upgrades for each group separately.

Consider splitting customers into distinct cohorts if your subscription model includes multiple pricing tiers (e.g., free vs. premium). Free users often behave differently from paying ones, so tracking users according to their tier gives you a more accurate picture of customer behavior and revenue potential.

Step 2. Calculate and Forecast Customer Churn and Retention
-----------------------------------------------------------

The churn rate measures the number of customers who leave your service. To calculate it, divide the number of users who unsubscribed during a given period by the number of users at the start of that period.

You can track customer behavior using two key metrics:

*   **Sign-Up Retention Rate** — the proportion of users who stay or renew after a sign-up or trial period,
*   **Monthly Churn Rate** — the percentage of paying users who leave the service each month.

Although both metrics reflect customer behavior, you should track pre- and post-sign-up behavior separately. For instance, it’s common to see a sharp drop in users after a free trial ends. However, those who convert into paying customers tend to churn at a lower and more stable rate.

To predict the number of retained users, multiply acquired customers by the sign-up retention rate. To forecast monthly churn, apply the churn rate to the number of users at the start of each month.

Step 3. Forecast Recurring and One-Time Subscription Revenue
------------------------------------------------------------

Use your customer acquisition model to calculate subscription revenues by separating one-time and recurring income. The split helps identify patterns in cash flow and explain revenue changes more clearly.

Start with **sign-up revenue**: multiply the sign-up fee by the number of new customers acquired in each period.

Then, calculate **recurring revenue** by multiplying the number of active customers by the applicable subscription fee.

Include a price increase index to adjust average revenue per user (ARPU) to account for inflation or planned price updates.

[![A spreadsheet with an example of a customer revenue model.](https://www.challengejp.com/wp-content/uploads/2021/05/step3-customer-revenue-model.png)](https://www.challengejp.com/wp-content/uploads/2021/05/step3-customer-revenue-model.png)

Screenshot #2: An example of Customer Revenue Model. The spreadsheet assumes different pricing for first-time and regular subscribers.

Notice that the example above repeats the monthly fee assumptions, allowing you to see what pricing applies in each period.

💡 _For more on modeling subscription pricing and user-based revenue forecasts,_ see this [my Marketing Investment Plan tutorial](https://www.challengejp.com/blog/how-to-create-marketing-investment-plan-excel-tutorial/)
, which shows how pricing assumptions impact CAC, CLV, and returns.

Step 4. Model Variable Customer Costs and Per-User Expenses
-----------------------------------------------------------

To make your subscription model more realistic, incorporate variable customer costs—expenses that scale with the number of users and reflect the cost of delivering your service.

[My Subscription Model Template](https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation#download_subscription_model_template)
 divides these costs into two categories:

*   **One-Off Variable Customer Costs** – expenses related to acquiring a customer, such as advertising or sign-up bonuses,
*   **Recurring Variable Customer Expenses** – ongoing costs directly tied to active users, such as hosting, licensing, or revenue share fees.

You can model recurring expenses in two ways.

First, calculate **percentage-based costs**—such as royalties or revenue share—as a proportion of subscription revenue.

Then, add **per-user fixed costs** by multiplying the number of users by a set amount for each period. This combination helps simulate both scalable and predictable operational expenses.

Include a cost increase index to account for inflation or changes in vendor pricing over time.

[![A spreadsheet with an estimate of customer variable costs.](https://www.challengejp.com/wp-content/uploads/2021/05/step4-customer-direct-cost-estimate.png)](https://www.challengejp.com/wp-content/uploads/2021/05/step4-customer-direct-cost-estimate.png)

Screenshot #3: A spreadsheet with a calculation of Customer Variable Cost. The costs are linked directly to new customers, monthly revenue, or monthly subscribers.

The example above applies customer acquisition costs to new sign-ups while calculating monthly recurring costs using a fixed dollar amount per active user and revenue share.

Step 5. Calculate Customer Lifetime Value (LTV) Using Revenue and Churn Assumptions
-----------------------------------------------------------------------------------

Now that you’ve modeled churn and subscription revenue, use those assumptions to calculate customer lifecycle and lifetime value (LTV), two essential metrics for evaluating long-term profitability.

The **customer lifecycle** measures how long, on average, a user stays subscribed. Multiply that figure by your subscription revenue per user to estimate **customer lifetime value**—the total revenue an average user will contribute over their time with your service.

[![A customer lifetime value calculator.](https://www.challengejp.com/wp-content/uploads/2021/05/step5a-customer-lifetime-value-calculator.png)](https://www.challengejp.com/wp-content/uploads/2021/05/step5a-customer-lifetime-value-calculator.png)

Screenshot #4: A Customer Lifetime Value Calculator. The lifetime calculation in [my subscription model](https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation#download_subscription_model_template)
 is directly linked with retention and churn, and derived from revenue and cost assumptions.

You can also visualize the customer lifecycle with a simple cohort analysis. For example, start with 100 new users and illustrate how churn reduces the customer base over time.

[![A graph with an illustration of a customer lifecycle.](https://www.challengejp.com/wp-content/uploads/2021/05/step5b-customer-lifecycle-graph.png)](https://www.challengejp.com/wp-content/uploads/2021/05/step5b-customer-lifecycle-graph.png)

Screenshot #5: A monthly illustration of the Customer Life Cycle based on a cohort of 100 new users. The number of users erodes over time due to initial retention and monthly churn.

Step 6. Include Operating and Product Development Costs in Cash Flow Forecast
-----------------------------------------------------------------------------

Extend your model to include general operating costs and capital expenditures and complete your subscription cash flow forecast.

To forecast staff costs, start with a **monthly headcount projection** and multiply it by your average salary assumption. Then, include any additional expenses directly tied to staffing.

Next, add **operating expenditures** like rent, general marketing, utilities, and administrative overhead. Depending on your model’s complexity, these recurring expenses can be fixed as recurring monthly costs or scaled to business size.

Don’t forget product development costs, especially if you’re building or maintaining software. Most of them will belong to **capital expenditures (CAPEX)**. However, some R&D spending may fall under operating costs depending on your accounting approach.

Include a salary and cost increase index to reflect inflation or expected cost growth over time.

[![A spreadsheet with a subscription cash flow forecast.](https://www.challengejp.com/wp-content/uploads/2021/05/step6-subscription-cash-flow-spreadsheet.png)](https://www.challengejp.com/wp-content/uploads/2021/05/step6-subscription-cash-flow-spreadsheet.png)

Screenshot #6: An example of a Subscription Cash Flow Forecast. Employee cost is linked to headcount assumption. General opex increases with inflation.

To forecast net cash flow, subtract variable costs, operating expenses, and development spending from customer revenue. Then, track the cumulative total to identify your lowest cash position, indicating your equity or funding requirement.

Step 7. Summarize and Visualize Subscription Model with Charts and Return Metrics
---------------------------------------------------------------------------------

Wrap up your model by aggregating the monthly subscription cash flow into an **annual summary**. For example, [my Subscription Model Template](https://www.challengejp.com/blog/how-to-create-subscription-model-with-churn-calculation#download_subscription_model_template)
 uses a SUMIFS formula in Excel to roll up the monthly data. This approach gives you the flexibility to switch between monthly, quarterly, or yearly views with minimal changes.

Include charts that visualize the relationship between key metrics—such as how subscriber growth impacts revenue and cash flow. You can also break down revenue by payment plan type to better illustrate cohort behavior and pricing structure.

[![A summary of a subscription cash flow forecast.](https://www.challengejp.com/wp-content/uploads/2021/05/step7-subscription-cash-flow-summary.png)](https://www.challengejp.com/wp-content/uploads/2021/05/step7-subscription-cash-flow-summary.png)

Screenshot #7a: A Subscription Cash Flow Forecast Summary with a list of assumptions. Assumptions placed next to the table for easier input testing.

To complete the financial picture, add a fundamental equity return analysis. You could estimate exit value using an **EBITDA multiple**. Then, calculate the **Net Present Value (NPV)** and **Internal Rate of Return (IRR)** using Excel’s [NPV](https://www.excel-easy.com/examples/npv.html)
 and [IRR](https://www.excel-easy.com/examples/irr.html)
 formulas \[external links\].

[![An example of a return on equity calculation in Excel.](https://www.challengejp.com/wp-content/uploads/2021/05/step8-equity-returns-calculation-example.png)](https://www.challengejp.com/wp-content/uploads/2021/05/step8-equity-returns-calculation-example.png)

Screenshot #7b: An example of Equity Return Calculation. The template calculates exit proceeds using an EBITDA multiplier and estimates returns with NPV and IRR formulas.

The Return on Investment analysis will help evaluate how your cash flows perform under different growth, revenue, churn, and cost assumptions.

Step 8. Stress Test Subscription Model Using Scenario Analysis and Assumption Blocks
------------------------------------------------------------------------------------

Once you have completed your model, stress-testing is essential. Place your key assumptions—such as churn rate, customer acquisition cost, and pricing—next to the summary table so you can quickly see how small changes impact overall results. Focus on metrics like **cumulative cash flow**, **peak cash need**, **equity requirement**, and **investor returns**.

Testing different scenarios helps identify weak spots in your model and highlights performance risks you may face as your business scales. For example, assess how a higher churn rate reduces revenue and shortens customer lifetime or how an increase in acquisition cost lowers equity returns.

Make sure your customer revenue model leaves a healthy margin—enough to cover general operating costs and ongoing product development or CAPEX.

🔍 _If you’re looking to go deeper into churn-based forecasting,_ [my Excel Cohort Analysis tutorial](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/)
 helps visualize retention over time and analyze the impact of churn patterns on LTV and cash flow.

📌 Recap: 9 Steps to Build a Subscription Model Forecast with Churn Calculations
--------------------------------------------------------------------------------

Here’s a quick recap of the steps to build a complete Subscription Model Forecast with Churn Calculations:

1.  **Forecast Customer Acquisition to Build Your Model.** Project user growth using simple month-over-month assumptions as the foundation for your model.
2.  **Calculate and Predict Customer Churn.** Use churn and retention rates to estimate how long customers stay and how many leave each period.
3.  **Forecast Subscription Revenue.** Calculate sign-up and recurring revenues separately to reflect onboarding spikes and predictable income.
4.  **Add Variable Customer Cost Calculations.** Model per-customer costs, one-time and recurring, include inflation adjustments over time.
5.  **Use a Customer Lifetime Value Calculator.** Estimate LTV based on churn and revenue inputs and analyze how each customer contributes to cash flow.
6.  **Add General and Development Expenditures.** Incorporate staffing, operating costs, and product development spend to create a complete cash flow forecast.
7.  **Summarize Your Subscription Model.** Aggregate monthly data into an annual view and visualize key financial and user metrics with charts.
8.  **Stress-Test Your Subscription Model.** Test sensitivity to pricing, churn, and CAC assumptions to ensure your model holds up under real-world scenarios.

By following these steps, you’ll create a robust, flexible Subscription Model that helps you forecast cash flows, evaluate profitability, and support strategic planning.

📥 Download My Subscription Model Template
------------------------------------------

Download the Excel template used in this tutorial, with calculations from customer growth and churn to revenue forecasting and equity returns.

Inside the file, you’ll find everything you need to build and stress-test your subscription model:

*   **Subscription Cash Flow Model** – Calculates user growth, churn, revenue, and total cash flow, including CAC, staffing, OPEX, and CAPEX.
*   **Customer Lifetime Value (CLV) Calculator** – Estimates LTV using revenue, churn, and cost assumptions with visual retention analysis.
*   **Subscription Model Summary** – Aggregates monthly forecasts into annual views with IRR, NPV, and built-in stress testing.
*   **Balance Sheet** – Projects assets and liabilities using depreciation and working capital based on the cash flow model.

$77.09 AUD – Download My Subscription Model Template  
Secure Checkout | Instant Download | 30-Day Money-Back Guarantee

  

[179.00zł – Download My Subscription Model Template](https://www.challengejp.com/checkout/?add-to-cart=2206)
  
Secure Checkout | Instant Download | 30-Day Money-Back Guarantee

The template is in Excel format and easily convertible to Google Sheets if needed.

👁️ **[View full template details](https://www.challengejp.com/product/subscription-model-template/)
**

Video Tutorial on Building a Subscription Model with Churn
----------------------------------------------------------

Follow along in my step-by-step video tutorial, where I show you how to build and customize a complete Subscription Model with Churn Calculation using Microsoft Excel. In the video, you’ll learn:

*   How to forecast customer acquisition and churn using simple growth assumptions.
*   How to calculate subscription revenues and model lifetime value (LTV).
*   How to estimate customer costs, staffing, and capital spend to project cash flow.
*   How to build equity returns and stress test key assumptions like pricing and retention.

By the end of the tutorial, you’ll know how to use my Subscription Model Template to forecast growth, evaluate profitability, and plan for funding needs.

▶️ [Watch on YouTube](https://youtu.be/wkYl4VfWRng)

<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span>﻿</span>

Get in Touch
------------

[![jacek polewski challengejp](https://www.challengejp.com/wp-content/uploads/2020/07/jp_photo-300x200.jpg)](https://www.challengejp.com/about/)
Hi, I’m Jacek. I’m passionate about spreadsheets and financial models, and I hope this tutorial helped you build a clearer, more effective Subscription Model Forecast.

If you have questions about Excel techniques, forecasting, or financial modeling, feel free to [get in touch](https://www.challengejp.com/contact/)
.

You can also explore my other tutorials for step-by-step guidance or check out my [**One-to-One Training**](https://www.challengejp.com/services/financial-modelling-data-training/)
 and [**Financial Modeling Services**](https://www.challengejp.com/services/financial-modelling/)
 for personalized support.

_Disclaimer: This tutorial is for informational and educational purposes only and does not constitute professional advice._

Explore More Tutorials
----------------------

Want to dive deeper into financial modeling? Here are more tutorials you might find helpful:

*   [**Analyze and Forecast Customer Churn and Revenue**](https://www.challengejp.com/blog/power-bi-customer-churn-revenue-forecast-tutorial/)
     – Build a churn/retention model in Power BI using DAX, cohort analysis, and interactive forecasts.
*   **[Marketing Investment Plan](https://www.challengejp.com/blog/how-to-create-marketing-investment-plan-excel-tutorial/)
    ** – See how marketing spending translates into user acquisition and how churn impacts ROI.
*   **[Telecom Financial Model](https://www.challengejp.com/blog/telecom-financial-model-excel-tutorial/)
    ** – Explore how churn, customer lifetime, and revenue streams drive infrastructure project returns.
*   **[Power BI Marketing Performance & Forecast Dashboard](https://www.challengejp.com/blog/power-bi-marketing-performance-forecast-dashboard/)
    ** — Create a Power BI dashboard to track campaign performance, model customer growth, and forecast marketing ROI with DAX-driven metrics.
*   **[Excel Cohort Analysis](https://www.challengejp.com/blog/excel-churn-retention-cohort-analysis/)
    ** – Dive into user cohorts to analyze retention and churn patterns over time.

[→ View all tutorials](https://www.challengejp.com/services/tutorials/)

Tags:[Cash Flow Forecasting](https://www.challengejp.com/blog/tag/cash-flow-forecasting/ "Cash Flow Forecasting")
[Excel Tutorial](https://www.challengejp.com/blog/tag/excel-tutorial/ "Excel Tutorial")
[Financial Modelling](https://www.challengejp.com/blog/tag/financial-modelling/ "Financial Modelling")

  

**Redirecting to FastSpring for secure payment and local tax handling in your region...**

You’ll see challengejp.onfastspring.com in your address bar.
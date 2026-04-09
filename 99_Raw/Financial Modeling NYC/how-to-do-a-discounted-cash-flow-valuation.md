# How to Do a Discounted Cash Flow Valuation: DCF Model Training

**Source:** https://www.financial-modeling.com/how-to-do-a-discounted-cash-flow-valuation

---

[Skip to content](https://www.financial-modeling.com/how-to-do-a-discounted-cash-flow-valuation#content "Skip to content")

How to Do a DCF (Discounted Cash Flow) Valuation: A Step-by-Step Guide to DCF Model Training
============================================================================================

![A picture of hundred dollar bills - Discounted cash flow - Financial modeling New York](https://www.financial-modeling.com/wp-content/uploads/2025/04/discounted-cash-flow-new-york-2048x1365.jpg "discounted-cash-flow-new-york")

Introduction: What Is Discounted Cash Flow and How to Do a DCF [Valuation](https://www.financial-modeling.com/glossar/valuation/)

----------------------------------------------------------------------------------------------------------------------------------

[Discounted cash flow (DCF)](https://www.financial-modeling.com/glossar/discounted-cash-flow/)
 valuation is a fundamental technique used by investors, analysts, and [corporate finance](https://www.financial-modeling.com/glossar/corporate-finance/)
 professionals to determine the intrinsic value of a company or [asset](https://www.financial-modeling.com/glossar/asset/)
. This method relies on estimating a business’s expected future cash flows and discounting them back to their present value using a discount rate that reflects the risk of those cash flows. Unlike market-based valuation like a comparable company analysis, DCF valuation focuses on the company’s ability to generate cash flow in the future, independent of market sentiment. This guide to the discounted cash flow method will walk you through each step, from projecting unlevered free cash flows (UFCF) to calculating terminal value.

Understanding the DCF Method and Why Analysts Use DCF Models
------------------------------------------------------------

The discounted cash flow method is based on the principle of the time value of money: a dollar today is worth more than a dollar received in the future. Analysts use discounted cash flow to estimate the net present value value of a company based on its forecast cash flow generation. The key benefit of using DCF analysis is that it provides a detailed, intrinsic view of a company’s value based on its underlying financial performance. This type of financial model is particularly effective for companies with steady cash flow generation and predictable growth.

Unlike valuation methods like a comparable company analysis which is market-driven, a DCF calculation relies entirely on internal cash flow projections and assumptions about risk and return. The model is that the value of a business is equal to the value of the cash flows it can generate, discounted to present value.

Step 1: Projecting Free Cash Flow and Unlevered Free Cash Flow in a Financial Model
-----------------------------------------------------------------------------------

The first step in building a DCF model using Excel is to forecast the company’s [unlevered free cash flow (UFCF)](https://www.financial-modeling.com/glossar/unlevered-free-cash-flow/)
 for a defined projection period, usually 5 to 10 years. Unlevered free cash flow is used to measure the cash flows available to all capital providers, including debt and [equity](https://www.financial-modeling.com/glossar/equity/)
 holders. This is calculated using the company’s [income statement](https://www.financial-modeling.com/glossar/income-statement/)
 and [cash flow statement](https://www.financial-modeling.com/glossar/cash-flow-statement/)
, adjusting for non-cash expenses, capital expenditures, and changes in [working capital](https://www.financial-modeling.com/glossar/working-capital/)
.

You can also project free cash flow to equity (FCFE) if you’re conducting an equity-focused valuation. Regardless of the approach, the goal is to estimate future cash flows the company is expected to generate.

**Formula: Unlevered Free Cash Flow (UFCF)**

UFCF = EBIT × (1 – Tax Rate) + Deferred Tax + [Depreciation](https://www.financial-modeling.com/glossar/depreciation/)
 & [Amortization](https://www.financial-modeling.com/glossar/amortization/)
 + Other Non-Cash Items + Change in Net Working Capital – Capital Expenditures

**Where:**

*   **EBIT** stands for Earnings Before Interest and Taxes. To calculate unlevered free cash flow, we adjust EBIT for taxes but exclude interest payments, making it a capital structure–neutral measure of a company’s operating performance
*   **Deferred Tax and Other Non-Cash Items** include temporary accounting differences and adjustments that affect reported earnings but not actual cash flows
*   **Depreciation & Amortization** are non-cash charges that reduce taxable income but do not represent actual cash outflows
*   **Capital Expenditures** represent the cash outflows required to maintain or expand the company’s fixed assets
*   **Change in Net Working Capital** reflects changes in [current assets](https://www.financial-modeling.com/glossar/current-assets/)
     and liabilities (excluding cash and debt)

**Key steps:**

*   Forecast revenue growth and operating margins.
*   Estimate capital expenditures and working capital needs.
*   Adjust for taxes and depreciation.

Step 2: Calculating the Discount Rate Using the [Weighted Average Cost of Capital (WACC)](https://www.financial-modeling.com/glossar/weighted-average-cost-of-capital/)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The discount rate reflects the required rate of return an investor expects, adjusted for risk. In an unlevered DCF, the appropriate discount rate is the **Weighted Average Cost of Capital (WACC)**, which blends the cost of equity and the after-tax cost of debt based on their relative proportions in the capital structure.

To estimate the **cost of equity**, analysts typically use the **[Capital Asset Pricing Model (CAPM)](https://www.financial-modeling.com/glossar/capital-asset-pricing-model/)
**:

> *   A standard estimate for the **U.S. [market risk](https://www.financial-modeling.com/glossar/market-risk/)
>      premium** is typically around **5.0%–6.5%**.
> *   The **risk-free rate** is usually based on the yield of a long-term U.S. Treasury bond (e.g., 10-year).
> *   **Beta** measures the company’s sensitivity to market movements.

The **WACC** formula is:

> *   **Equity** = Market value of equity
> *   **Debt** = Market value of debt
> *   **Cost of Debt** is estimated based on the yield to maturity (YTM) of the company’s [long-term debt](https://www.financial-modeling.com/glossar/long-term-debt/)
>      or current borrowing rates, adjusted for the marginal tax rate.
> *   For U.S. corporates, **WACC typically ranges between 7% and 10%**, though it varies by industry and company risk profile.

Using a discount rate that accurately reflects the company’s risk profile is critical to a reliable valuation. The higher the perceived risk, the higher the discount rate, and the lower the **present value** of the company’s **expected future cash flows**.

Step 3: Estimating Terminal Value in a Discounted Cash Flow Valuation
---------------------------------------------------------------------

Terminal value represents the value of the business beyond the explicit forecast period and is a key driver in any DCF valuation. There are two main approaches to estimating terminal value:

**1\. Gordon Growth Model (Perpetuity Growth)**: Assumes cash flows beyond the projection period grow at a constant rate forever.

Where:

*   **g**: The **perpetual growth rate**, typically **1%–3%** for mature companies
*   **Discount Rate**: The **WACC (Weighted Average Cost of Capital)**

**2\. Exit Multiple Method**: Applies a valuation multiple (like EV/EBITDA) to the final year’s cash flow.

Terminal value captures the cash flows after the explicit forecast period and must be discounted to present value using the same WACC.

Choosing the right method depends on the business type and availability of comparable company data. The terminal value often represents more than 50% of the total discounted cash flow model, so accurate assumptions are critical for high-quality [financial analysis](https://www.financial-modeling.com/glossar/financial-analysis/)
.

Step 4: Discount the Cash Flows to Present Value Using the Discounted Cash Flow Formula
---------------------------------------------------------------------------------------

Now that you have the projected UFCFs and the terminal value, the next step is to discount the cash flows using the WACC. This means calculating the present value of each year’s unlevered free cash flow and the terminal value.

This step is the heart of the discounted cash flow valuation. Discounted cash flows are calculated using either a simple discounting formula or Excel functions like NPV and XNPV.

The discounted cash flow formula for a single year is:

**DCF = Cash Flow / (1 + r)^n**

Where:

*   Cash Flow = forecasted FCF for that year
*   r = discount rate (WACC)
*   n = year number

Summing these present values gives you the enterprise value. This value represents the total value of the company before adjusting for debt and cash.

Step 5: Completing the DCF Calculation to Determine Enterprise and Equity Valuation
-----------------------------------------------------------------------------------

With the total present value of all forecasted cash flows and the terminal value, you’ve arrived at the **enterprise value**. To determine the [equity value](https://www.financial-modeling.com/glossar/equity-value/)
:

*   Subtract net debt (debt minus cash and equivalents).
*   Add non-operating assets if applicable.
*   Divide by diluted shares outstanding to get the per-share value.

The result gives you the intrinsic value of the company’s equity. This value using DCF provides a comprehensive view of a company’s worth based on its ability to generate future cash flows.

### Using [Sensitivity Analysis](https://www.financial-modeling.com/glossar/sensitivity-analysis/)
 to Test a DCF Model in Excel

DCF models depend heavily on assumptions, so it’s important to run sensitivity analyses. Adjust key variables like:

*   WACC (discount rate)
*   Terminal growth rate
*   Revenue growth

A well-built model Excel template should include data tables or charts to show how these inputs affect the final valuation.

Additionally, it is industry standard to cross-check the DCF results against valuation techniques like a comparable company analysis. This helps ensure the DCF output is within a reasonable range.

### Avoiding Common Mistakes in DCF Analysis and [Financial Modeling](https://www.financial-modeling.com/glossar/financial-modeling/)

Even seasoned analysts can make errors when using the DCF method. Watch out for:

*   Overly aggressive growth assumptions
*   Ignoring changes in working capital
*   Misestimating the discount rate
*   Incorrectly handling circular references in Excel

The most common issue? Overestimating a company’s future operating cash flow that’s not supported by past performance or industry benchmarks. Ensure you forecast a company’s future cash based on historical trends and reasonable expectations.

Conclusion: A Practical Guide to the Discounted Cash Flow Method and Different DCF Methods
------------------------------------------------------------------------------------------

A discounted cash flow analysis is one of the most powerful tools in valuation, but it requires care and precision. By learning how to build a DCF model step by step, you can conduct a DCF analysis that truly reflects a company’s financial health and potential amount of cash a company can generate over time.

Whether you’re using the DCF method for a real-world investment decision or as part of a financial modeling and valuation analyst exam, remember: the strength of your output lies in the quality of your inputs, or as you’ll hear it on an [investment banking](https://www.financial-modeling.com/glossar/investment-banking/)
 floor, “junk in, junk out” (alternative choice of words is highly likely here!). A good DCF model training, a well-structured Excel template, and a clean list of Excel shortcuts will go a long way.

As you practice building a DCF model using a DCF model template or from scratch, remember the fundamentals: the DCF valuation is a type of financial model used to determine the value of the cash flows a company is expected to generate in the future. 

If you want hands-on practice building a DCF model from scratch, feel free to [contact us](https://www.financial-modeling.com/how-to-do-a-discounted-cash-flow-valuation#)
 — we’d love to help you sharpen your skills.d 3-statement model. In this case study, you’ll learn how to build a detailed debt schedule and seamlessly integrate it into a dynamic financial model. Explore firsthand how a company’s debt is integrated into a full-scale analysis and enhance your modeling skills!

Do you have an inquiry? Schedule a free initial consultation

[Schedule a consultation here](tel:01737209772)
 [info@financial-modeling.com](mailto:info@financial-modeling.com)

**Opening hours**

**Appointment** by  
prior arrangement

****ADDRESS****

777 McCarter Hwy, Newark, **NJ**  
1541 NE 42nd Ct, Pompano Beach, **FL**  

**Telephone**

[+1-754-249-7916](tel:+1(754)2497916)

**E-Mail**

[info@financial-modeling.com](mailto:info@financial-modeling.com)

[](https://www.financial-modeling.com/how-to-do-a-discounted-cash-flow-valuation# "Scroll back to top")
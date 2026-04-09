# Adjusted Present Value (APV)

**Source:** https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv

---

Table of Contents

*   [What is Adjusted Present Value (APV)?](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#what-is-adjusted-present-value-apv)
    

*   [How Debt and Equity Affect the Value of a Project](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#how-debt-and-equity-affect-the-value-of-a-project)
    
*   [APV and Financial Modeling](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#apv-and-financial-modeling)
    
*   [Adjusted Present Value Assumptions](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#adjusted-present-value-assumptions)
    
*   [Unlevered Cost of Capital](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#unlevered-cost-of-capital)
    
*   [The Adjusted Present Value for Valuation](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#the-adjusted-present-value-for-valuation)
    
*   [Download CFI's Free Adjusted Present Value (APV) Template](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#download-cfis-free-adjusted-present-value-apv-template)
    
*   [Applications of Adjusted Present Value](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#applications-of-adjusted-present-value)
    
*   [Other Metrics: WACC and FTE Methods](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#other-metrics-wacc-and-fte-methods)
    
*   [Additional Resources](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/#additional-resources)
    

Adjusted Present Value (APV)
============================

Using the NPV and the present value of debt financing costs to value a company or project

Written by [Tim Vipond, FMVA](https://corporatefinanceinstitute.com/author/tim-vipond/)

Published April 21, 2018

Read Time 5 minutes

What is Adjusted Present Value (APV)?
-------------------------------------

Adjusted Present Value (APV) is used for the [valuation](https://corporatefinanceinstitute.com/resources/valuation/valuation/)
 of projects and companies. It takes the [net present value (NPV)](https://corporatefinanceinstitute.com/resources/knowledge/valuation/npv-formula/)
, plus the present value of [debt financing costs](https://corporatefinanceinstitute.com/resources/valuation/cost-of-debt/)
, which include interest tax shields, costs of debt issuance, costs of financial distress, financial subsidies, etc.

So why do we use Adjusted Present Value instead of NPV in evaluating projects with debt financing? To answer this, we first need to understand how financing decisions (debt vs. equity) affect the value of a project. 

[![Adjusted Present Value (APV) Example in Excel](https://cdn.corporatefinanceinstitute.com/assets/adjusted-present-value-apv-example-calculation.png)](https://corporatefinanceinstitute.com/resources/financial-modeling/adjusted-present-value-template/)

Download the [Adjusted Present Value Template](https://corporatefinanceinstitute.com/resources/financial-modeling/adjusted-present-value-template/)
.

### How Debt and Equity Affect the Value of a Project

The value of a project financed with debt may be higher than that of an all equity-financed project since the cost of capital often decreases with leverage, turning some negative NPV projects into positive ones. Thus, under the NPV rule, a project may be rejected if it is financed with only equity but may be accepted if it is financed with some debt. 

The Adjusted Present Value approach takes into consideration the benefits of raising debt (e.g. interest tax shield), which NPV does not do. As such, APV analysis is preferred in highly leveraged transactions.

![Adjusted Present Value - Image of Value-Price Scale](https://cdn.corporatefinanceinstitute.com/assets/multiples-analysis.jpeg)

### APV and Financial Modeling

In [financial modeling](https://corporatefinanceinstitute.com/resources/financial-modeling/what-is-financial-modeling/)
, it is common practice to use Net Present Value with the firm’s Weighted Average Cost of Capital as the discount rate, which determines the unlevered value of the firm (its [enterprise value](https://corporatefinanceinstitute.com/resources/valuation/what-is-enterprise-value-ev/)
) or the unlevered value of a project.

The present value of net debt is deducted to arrive at equity value, if that’s what is desired. See a comparison of [equity value vs enterprise value](https://corporatefinanceinstitute.com/resources/valuation/enterprise-value-vs-equity-value/)
.

To learn more, [launch our financial modeling courses](https://corporatefinanceinstitute.com/collections/financial-modeling/)
!

### Adjusted Present Value Assumptions

We make the following simplifying assumptions before using the APV approach in the valuation of a project:

1.  The project’s risk is equal to the average risks of other projects within the firm, which is also the risk of the firm. In other words, the project in question is a “typical” project that the firm usually takes on. In this case, the relevant discount rate for the project is based on the risk of the firm.
2.  Corporate taxes are the only important market imperfection at the level of debt chosen. This means that we focus only on the interest tax shields and ignore the effects generated by the costs of debt issuance and financial distress.
3.  All debt is perpetual.

### Unlevered Cost of Capital

The APV method uses [unlevered cost of capital](https://corporatefinanceinstitute.com/resources/valuation/unlevered-cost-of-capital/)
 to discount free cash flows, as it initially assumes that the project is fully financed by equity.

To find the unlevered cost of capital, we must first find the project’s [unlevered beta](https://corporatefinanceinstitute.com/resources/valuation/unlevered-beta-asset-beta/)
. Unlevered beta is a measure of the company’s risk relative to that of the market. It is also referred to as “asset beta” because, without leverage, a company’s equity beta is equal to its asset beta.

To retrieve a company’s beta, we can look up the company on financial resource sites such as Bloomberg Terminal or [CapIQ](https://corporatefinanceinstitute.com/resources/valuation/capiq/)
.  If the company is not listed, we can find a comparable company that is listed instead.

The unlevered cost of capital is calculated as:

Unlevered cost of capital (rU) = Risk-free rate + beta \* (Expected market return – Risk-free rate).

### The Adjusted Present Value for Valuation

The APV method to calculate the levered value (VL) of a firm or project consists of three steps:

#### Step 1

Calculate the value of the unlevered firm or project (VU), i.e. its value with all-equity financing. To do this, discount the stream of FCFs by the unlevered cost of capital (rU).

#### Step 2

Calculate the net value of the debt financing (PVF), which is the sum of various effects, including:

*         PV(Interest tax shields) – our main focus
*         PV(Issuance costs)
*         PV(Financial distress costs)
*         PV(Other market imperfections)

#### Step 3

Sum up the value of the unlevered project and the net value of debt financing to find the adjusted present value of the project. That is, VL = VU + PVF.

### Download CFI’s Free Adjusted Present Value (APV) Template

Enter your name and email in the form below and download our free Adjusted Present Value (APV) template now!  

   Download Now

### Applications of Adjusted Present Value

The APV method is most useful when evaluating companies or projects with a fixed debt schedule, as it can easily accommodate the side effects of financing such as interest tax shields. APV breaks down the value of a project into its fundamental components and thus provides useful information needed to refine the transaction and monitor its execution.

[Leveraged buyouts (LBOs)](https://corporatefinanceinstitute.com/resources/valuation/leveraged-buyout-lbo/)
, where one firm acquires another firm using debt to finance the purchase, are a classical situation where APV is used. The APV method is the most practical for this situation because of the changing capital structure.

### Other Metrics: WACC and FTE Methods

[Weighted average cost of capital (WACC)](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
 is also a widely accepted method of valuation and can be used in valuing levered firms. Comparably, it has a simpler structure.

A firm’s WACC is calculated as: ![WACC Formula](https://cdn.corporatefinanceinstitute.com/assets/APV-1.png) 

Where D = the firm’s debt and E = firm’s equity, both at market values.

rD = cost of debt, rE = cost of equity, τ = tax rate.

The project value is computed by discounting streams of the firm’s free cash flow with WACC.

The **Flow to Equity (FTE)** method calculates the firm’s levered [cash flow](https://corporatefinanceinstitute.com/resources/knowledge/valuation/what-is-free-cash-flow-fcf/)
 to equity (LCFE) using the following formula:

LCFE = Unlevered Cash Flow – Interest × (1 – tax rate),

LCFE is then discounted with rE to get the value of equity.

Total value is VL = E + D.

Both the WACC and FTE methods operate under the assumption that the firm will keep a fixed [debt-to-equity ratio (D/E)](https://corporatefinanceinstitute.com/resources/commercial-lending/debt-to-equity-ratio-formula/)
, implying that the firm will continue to raise debt at the same cost into the future. Realistically, however, this is often not the case. If D/E changes over time, WACC will also change, making the use of this method difficult. In general, if D/E remains constant over time, the WACC or FTE methods are easier to implement. However, the APV method is more practical when dealing with a complex debt schedule.

### Additional Resources

Thank you for reading CFI’s guide to Adjusted Present Value (APV). To keep learning and mastering your corporate finance skills, we highly recommend these relevant articles:

*   [What is the WACC Formula?](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
    
*   [FCFF vs FCFE Reconciliation Template](https://corporatefinanceinstitute.com/resources/financial-modeling/fcff-vs-fcfe-reconciliation-template/)
    
*   [Leveraged Buyout](https://corporatefinanceinstitute.com/resources/valuation/leveraged-buyout-lbo/)
    
*   [Unlevered Beta](https://corporatefinanceinstitute.com/resources/valuation/unlevered-beta-asset-beta/)
    
*   [Unlevered Cost of Capital](https://corporatefinanceinstitute.com/resources/valuation/unlevered-cost-of-capital/)
    
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

Get Certified for Financial Modeling (FMVA)®

Gain in-demand industry knowledge and hands-on practice that will help you stand out from the competition and become a world-class financial analyst.

[Learn More](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fadjusted-present-value-apv%2F&summary=Adjusted+Present+Value+%28APV%29 "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fadjusted-present-value-apv%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)](https://twitter.com/intent/tweet?text=Adjusted+Present+Value+%28APV%29&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fadjusted-present-value-apv%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fadjusted-present-value-apv%2F&summary=Adjusted+Present+Value+%28APV%29 "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/ "Copy link")
    

[Corporate Finance Institute](https://corporatefinanceinstitute.com/)

[Back to Website](https://corporatefinanceinstitute.com/)

0 search results for ‘’

People also search for: excel power bi esg accounting balance sheet fmva real estate

Explore Our Certifications

[Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

[Commercial Banking & Credit Analyst (CBCA)®](https://corporatefinanceinstitute.com/certifications/commercial-banking-credit-analyst-certification-cbca/)

[Capital Markets & Securities Analyst (CMSA)®](https://corporatefinanceinstitute.com/certifications/capital-markets-securities-analyst-cmsa/)

[Certified Business Intelligence & Data Analyst (BIDA)®](https://corporatefinanceinstitute.com/certifications/business-intelligence-data-analyst-bida/)

[Financial Planning & Wealth Management Professional (FPWMP)®](https://corporatefinanceinstitute.com/certifications/financial-planning-and-wealth-management-fpwm-program/)

[FinTech Industry Professional (FTIP)®](https://corporatefinanceinstitute.com/certifications/fintech-industry-professional/)

Resources

[Mastering Excel Shortcuts for PC and Mac Work Smarter in Excel with Keyboard Shortcuts If you're still reaching for the mouse every few seconds, it's time to level up. The best Excel keyboard...](https://corporatefinanceinstitute.com/resources/excel/excel-shortcuts-pc-mac/)

[Financial Modeling Guidelines CFI’s free Financial Modeling Guidelines is a thorough and complete resource covering model design, model building blocks, and common tips, tricks,...](https://corporatefinanceinstitute.com/resources/financial-modeling/free-financial-modeling-guide/)

[SQL Data Types What are SQL Data Types? The Structured Query Language (SQL) comprises several different data types that allow it to store different types of information...](https://corporatefinanceinstitute.com/resources/data-science/sql-data-types/)

[Structured Query Language (SQL) What is Structured Query Language (SQL)? Structured Query Language (known as SQL) is a programming language used to interact with a database....](https://corporatefinanceinstitute.com/resources/data-science/structured-query-language-sql/)

[See All Resources See All](https://corporatefinanceinstitute.com/resources/)

Popular Courses

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/adjusted-present-value-apv/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
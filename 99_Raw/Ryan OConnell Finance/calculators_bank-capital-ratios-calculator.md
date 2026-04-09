# Bank Capital Ratio Calculator | Basel III Capital Adequacy | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/bank-capital-ratios-calculator

---

Bank Capital Ratio Calculator
=============================

Basel III Capital Adequacy Analysis

Compute CET1, Tier 1, Total Capital, and Leverage ratios with simplified risk weights

Embed This Calculator

Enter Bank Data
---------------

###### Capital Components

CET1 Capital ?

$M 

Common Equity Tier 1 capital ($M)

AT1 Capital ?

$M 

Additional Tier 1 capital ($M)

Tier 2 Capital ?

$M 

Tier 2 supplementary capital ($M)

###### Asset Breakdown

Cash & Treasuries ?

$M 

Risk weight: **0%**

GSE/Agency Securities ?

$M 

Risk weight: **20%**

Residential Mortgages ?

$M 

Risk weight: **50%**

Commercial Loans ?

$M 

Risk weight: **100%**

Past-Due Loans ?

$M 

Risk weight: **150%**

Other Assets ?

$M 

Risk weight: **100%**

###### Regulatory Settings

G-SIB Surcharge ? 0% (Not a G-SIB) 1.0% 1.5% 2.0% 2.5% 3.5%

Global Systemically Important Bank surcharge

Reset to Defaults

##### Risk Weight Summary

| Asset Category | Weight |
| --- | --- |
| Cash & Treasuries | **0%** |
| GSE/Agency Securities | **20%** |
| Residential Mortgages | **50%** |
| Commercial Loans | **100%** |
| Past-Due Loans | **150%** |
| Other Assets | **100%** |

Simplified weights inspired by Basel III and U.S. regulatory practice

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Capital Adequacy Results

Status vs. Selected Thresholds Pass

Risk-Weighted Assets $60,250M

Total Exposure $95,500M

CET1 Ratio 13.28% Pass

Tier 1 Ratio 15.77% Pass

Total Capital 19.09% Pass

Leverage Ratio 9.95% Pass

CET1 Surplus vs. Required CET1 $3,782.5M

### Formula Breakdown

RWA = Σ(Asseti × Risk Weighti)

Capital Ratio = Capital / RWA

### Capital Adequacy Thresholds

| Ratio | Minimum | Buffer | Status |
| --- | --- | --- | --- |
| CET1 | 4.5% | 7.0% | Pass |
| Tier 1 | 6.0% | 8.5% | Pass |
| Total Capital | 8.0% | 10.5% | Pass |
| Leverage | 3.0% | 5.0% | Pass |

### RWA Breakdown by Asset Category

### Model Assumptions

*   Risk weights are simplified approximations inspired by Basel III and U.S. regulatory practice
*   RWA is a simplified credit-risk-only proxy; excludes market-risk and operational-risk RWA
*   Leverage exposure uses on-balance-sheet assets only (excludes off-balance-sheet items, derivatives, SFTs)
*   AT1 and Tier 2 inputs are assumed fully eligible after applicable deductions, caps, and amortization
*   G-SIB surcharge is met with CET1 capital; adjusted Tier 1 and Total targets shown are presentation targets only
*   Single-period point-in-time analysis with static portfolio composition
*   No countercyclical capital buffer (CCyB) included
*   5% leverage threshold reflects U.S. well-capitalized standard; Basel G-SIB leverage buffer (3% + surcharge/2) is below 5% for all selectable surcharge buckets
*   Excludes jurisdiction-specific overlays (U.S. stress capital buffer, SLR/eSLR, CCAR)
*   For educational purposes only. Not financial advice. Regulatory conventions simplified.

Understanding Bank Capital Adequacy
-----------------------------------

### What Are Bank Capital Ratios?

**Bank capital ratios** measure the financial strength and resilience of banking institutions by comparing their capital buffers to their risk exposures. Regulators use these ratios to ensure banks can absorb losses during economic downturns without becoming insolvent, thereby protecting depositors and the broader financial system.

### The Basel III Framework

Basel III, developed by the Basel Committee on Banking Supervision, is the global regulatory standard for bank capital adequacy. It introduces three pillars of capital measurement:

*   **CET1 Ratio (Common Equity Tier 1):** The highest-quality capital (common stock + retained earnings - goodwill) divided by risk-weighted assets. Minimum: 4.5%, with a 2.5% conservation buffer.
*   **Tier 1 Ratio:** CET1 plus Additional Tier 1 capital (preferred stock, CoCos) divided by RWA. Minimum: 6.0%.
*   **Total Capital Ratio:** All capital tiers divided by RWA. Minimum: 8.0%.
*   **Leverage Ratio:** Tier 1 capital divided by total exposure (non-risk-weighted). Minimum: 3.0%.

Core Formulas

**RWA** = Σ(Asseti × Risk Weighti)  
**CET1 Ratio** = CET1 Capital / RWA  
**Leverage Ratio** = Tier 1 Capital / Total Exposure  
All ratios expressed as percentages

### Understanding Risk Weights

Risk weights reflect the relative credit risk of different asset categories. Cash and government securities carry a 0% weight (treated as zero-risk in this simplified model), while commercial loans carry 100% and past-due loans 150%. The risk-weighted approach means a bank holding mostly government bonds needs less capital than one with a commercial loan portfolio of the same size.

**Key Insight:** The leverage ratio acts as a backstop to risk-weighted ratios. It prevents banks from gaming risk weights to minimize capital requirements while still carrying large total exposures.

### Prompt Corrective Action (U.S.)

In the United States, the Prompt Corrective Action (PCA) framework triggers escalating regulatory responses as capital falls:

*   **Well-capitalized:** CET1 ≥ 6.5%, Tier 1 ≥ 8%, Total ≥ 10%, Leverage ≥ 5%
*   **Adequately capitalized:** Meets minimums but below well-capitalized
*   **Undercapitalized:** Below minimums — capital restoration plan required
*   **Critically undercapitalized:** Tangible equity ≤ 2% of assets — FDIC may close the bank

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/bank-capital-ratios-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is the CET1 ratio and why does it matter?

The Common Equity Tier 1 (CET1) ratio measures a bank's highest-quality capital — common stock and retained earnings, minus goodwill and intangibles — relative to its risk-weighted assets. Basel III requires a minimum CET1 ratio of 4.5%, with an additional 2.5% capital conservation buffer (met with CET1 capital) bringing the effective target to 7.0%. Banks falling below this target face automatic restrictions on dividends and bonus payments.

### How are risk-weighted assets (RWA) calculated?

Risk-weighted assets assign a regulatory risk weight to each asset category based on its perceived credit risk. This calculator uses simplified weights inspired by Basel III and U.S. regulatory practice: government securities at 0%, agency securities at 20%, residential mortgages at 50%, commercial loans at 100%, and past-due loans at 150%. The RWA is the sum of each asset multiplied by its assigned risk weight, providing a standardized measure of regulatory credit risk exposure. Actual Basel III weights are more granular.

### What are the Basel III minimum capital requirements?

Basel III establishes three minimum capital ratios: CET1 at 4.5%, Tier 1 at 6.0%, and Total Capital at 8.0% of risk-weighted assets. The 2.5% Capital Conservation Buffer sits above these minimums, effectively raising target levels to 7.0%, 8.5%, and 10.5% respectively. Banks operating below the buffer face automatic constraints on capital distributions.

### What is the leverage ratio and how does it differ from capital ratios?

The leverage ratio divides Tier 1 capital by total exposure, providing a non-risk-based backstop to the risk-weighted capital ratios. Unlike capital ratios that use risk-weighted assets (where safer assets count less), the leverage ratio treats all on-balance-sheet assets equally regardless of perceived risk. Basel III requires a minimum 3% leverage ratio. In the United States, insured depository institutions are generally considered well-capitalized at 5% or above. This calculator uses on-balance-sheet assets as a simplified exposure measure; full Basel III leverage exposure is broader.

### What is the G-SIB surcharge?

The Global Systemically Important Bank (G-SIB) surcharge is an additional capital buffer required for the largest, most interconnected banks. Basel III assigns G-SIBs to buckets with surcharges of 1.0%, 1.5%, 2.0%, 2.5%, or 3.5% of RWA, met with CET1 capital. This surcharge increases the effective CET1 target — for example, a bank with a 1.5% G-SIB surcharge must maintain CET1 of at least 8.5% (4.5% + 2.5% CCB + 1.5% G-SIB). G-SIBs also face a Basel leverage buffer of 50% of their surcharge above the 3% minimum, though this calculator uses the higher 5% U.S. well-capitalized threshold for the leverage ratio.

### What happens when a bank falls below minimum capital requirements?

In the United States, banks that fall below minimum capital requirements face increasingly severe regulatory action under the Prompt Corrective Action (PCA) framework. Undercapitalized banks must submit capital restoration plans and face asset growth restrictions. Significantly undercapitalized banks cannot pay above-market deposit rates and need approval for new branches. Critically undercapitalized banks (tangible equity below 2% of total assets) may be closed by the FDIC. Other jurisdictions have analogous supervisory intervention frameworks.

##### Disclaimer

This calculator is for educational purposes only and uses simplified Basel III-style risk weights. Actual regulatory capital calculations involve more granular risk weights, off-balance-sheet exposures, derivatives netting, and jurisdiction-specific overlays. Consult official regulatory guidance and professional advisors for compliance purposes.

Related Calculators
-------------------

[![Professional finance illustration representing Interest Rate Gap & Duration Gap Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Interest Rate Gap & Duration Gap Calculator\
\
Analyze interest rate risk with gap analysis.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/interest-rate-gap-calculator/)

[![Professional finance illustration representing Loan Loss Provision & Credit Risk Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Loan Loss Provision & Credit Risk Calculator\
\
Calculate loan loss provisions and credit risk reserves.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/loan-loss-provision-calculator/)

[![Professional finance illustration representing Money Multiplier Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Money Multiplier Calculator\
\
Compute the money multiplier from reserve requirements.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/money-multiplier-calculator/)

Contact Me
----------

Have a question or want to work together? Fill out the form below and we’ll get back to you as soon as possible.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20378'%3E%3C/svg%3E)

Contact Form Demo

First Name

Last Name

Email

Subject

Your Message

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy)
 and [Terms of Service](https://policies.google.com/terms)
 apply.

Submit Form
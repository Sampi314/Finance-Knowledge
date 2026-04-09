# Financial Modeling Interview Questions: The Complete 2026 Guide - Financial Modeling New York

**Source:** https://www.financial-modeling.com/financial-modeling-interview-questions-guide

---

[Skip to content](https://www.financial-modeling.com/financial-modeling-interview-questions-guide#content "Skip to content")

Financial Modeling Interview Questions: The Complete 2026 Guide
===============================================================

![](https://www.financial-modeling.com/wp-content/uploads/2026/02/interview-questions-finance.jpg)

Whether you are preparing for an [investment banking](https://www.financial-modeling.com/glossar/investment-banking/)
 analyst interview, a [private equity](https://www.financial-modeling.com/glossar/private-equity/)
 associate role, or a corporate development position, one thing is certain: you will be tested on [financial modeling](https://www.financial-modeling.com/glossar/financial-modeling/)
. Not conceptually — technically. Interviewers will give you a blank spreadsheet and a set of assumptions and watch what you build. This guide covers the questions you are most likely to face, organized by model type, along with the answers that separate strong candidates from the rest.

How Financial Modeling Interviews Actually Work
-----------------------------------------------

There are three formats you will encounter:

*   **Conceptual questions:** “Walk me through a DCF.” “How do the three statements link?” These test whether you understand the logic.
*   **Excel case studies:** You are given a data package and 2–4 hours to build a model. These test speed, structure, and accuracy under pressure.
*   **Live modeling tests:** Build a model in real time, on screen, while the interviewer watches. This is the hardest format and the most common at elite firms.

The questions below prepare you for all three.

DCF Modeling Questions
----------------------

### “Walk me through a DCF.”

The most common interview question in all of finance. The clean answer: A DCF values a business by projecting its unlevered free cash flows over a forecast period — typically five to ten years — then calculating a terminal value to capture everything beyond that horizon. Both are discounted back to the present using WACC, which reflects the blended cost of debt and [equity](https://www.financial-modeling.com/glossar/equity/)
 in the capital structure. The result is enterprise value; subtract net debt to get [equity value](https://www.financial-modeling.com/glossar/equity-value/)
 and divide by diluted shares outstanding to arrive at a per-share intrinsic value.

### What is WACC and what drives it?

WACC — Weighted Average Cost of Capital — is the blended required return for the entire capital structure. It is driven by: the cost of equity (calculated via CAPM: risk-free rate + beta × equity risk premium), the after-tax cost of debt (pre-tax rate × (1 − tax rate)), and the target capital structure weights. Changes in [leverage](https://www.financial-modeling.com/glossar/leverage/)
, credit rating, or [market risk](https://www.financial-modeling.com/glossar/market-risk/)
 all shift WACC.

### What is the difference between a 10-year and a 5-year projection period?

A longer projection period reduces the proportion of value coming from the terminal value — which is more speculative — and forces you to model the business in more detail. Use the period that aligns with a natural inflection point: end of a contract cycle, full ramp-up of a new product, or normalization of margins. Most DCFs use 5 years for mature businesses and 10 years for high-growth or cyclical companies.

### How do you calculate terminal value, and what are the risks?

Two methods: **Gordon Growth Model** (FCF × (1 + g) / (WACC − g)) and **Exit Multiple** (terminal year EBITDA × an EV/EBITDA multiple). The exit multiple method is more common in practice because it anchors to observable market data. The risk: terminal value often represents 60–80% of total enterprise value in a DCF, making the model highly sensitive to your WACC and growth rate assumptions. Always run a sensitivity table on these two inputs.

Three-Statement Model Questions
-------------------------------

### How do the three [financial statements](https://www.financial-modeling.com/glossar/financial-statements/)
 link together?

Net income from the [income statement](https://www.financial-modeling.com/glossar/income-statement/)
 flows into [retained earnings](https://www.financial-modeling.com/glossar/retained-earnings/)
 on the [balance sheet](https://www.financial-modeling.com/glossar/balance-sheet/)
 and is the starting point for the [cash flow statement](https://www.financial-modeling.com/glossar/cash-flow-statement/)
. [Depreciation](https://www.financial-modeling.com/glossar/depreciation/)
 and [amortization](https://www.financial-modeling.com/glossar/amortization/)
 — a non-cash charge on the income statement — is added back on the cash flow statement. Capital expenditures on the cash flow statement increase PP&E on the balance sheet. The ending cash balance on the cash flow statement equals cash on the balance sheet. The balance sheet must always balance: Assets = Liabilities + Equity.

### If depreciation increases by $10, walk me through the impact on all three statements.

Income statement: EBIT falls by $10, pre-tax income falls by $10, taxes fall by $4 (assuming 40% rate), net income falls by $6. Cash flow statement: net income down $6, D&A add-back up $10, net operating cash flow up $4. Balance sheet: cash up $4, PP&E net down $10, total assets down $6. Equity down $6 (retained earnings). Both sides down $6 — balanced.

### What is the plug on the balance sheet?

Cash. In a properly built model, cash is calculated as the residual after all other balance sheet items are determined. If the balance sheet does not balance, something else is wrong — not the cash figure. A common mistake is to hard-code cash instead of letting it float, which hides errors.

LBO Modeling Questions
----------------------

### Why would a private equity firm use leverage in an [acquisition](https://www.financial-modeling.com/glossar/acquisition/)
?

Leverage amplifies equity returns. If you acquire a company for $100 using $60 of debt and $40 of equity, and the company is worth $120 at exit, your equity value has grown from $40 to $60 — a 50% return on equity despite only a 20% increase in enterprise value. The debt acts as a return amplifier. The risk is that the company must generate enough free cash flow to service and repay the debt.

### What IRR would a PE firm typically target in an LBO?

The industry convention is 20%+ IRR over a 3–5 year holding period, with a MOIC of 2.0–3.0x. Top-tier firms may target 25%+ on individual deals. Below 15% IRR, most institutional LPs would question whether the illiquidity premium over public markets is justified.

### How does paying down debt increase equity returns in an LBO?

Debt paydown increases equity value directly: Enterprise Value at exit minus Net Debt equals equity value. Every dollar of debt paid down from operating cash flows — without any change in EBITDA or exit multiple — increases the sponsor’s equity proceeds dollar-for-dollar. This is why free cash flow conversion is so critical in LBO underwriting.

Excel and Mechanics Questions
-----------------------------

### What Excel function do you use to calculate IRR?

XIRR, not IRR. IRR assumes equal time periods between cash flows — which almost never holds in a real deal where the initial investment and exit proceeds occur on specific calendar dates. XIRR accepts actual dates and is the professional standard.

### How do you handle circular references in a financial model?

The most robust method is a circularity toggle: a named cell set to 1 or 0. When the toggle is 0, interest expense is calculated on the prior period’s debt balance (breaking the circularity). When 1, it uses the current period’s balance. Alternatively, enable iterative calculations in Excel settings — but this can mask errors and is not recommended for complex models.

### What is the difference between VLOOKUP and INDEX/MATCH?

VLOOKUP can only look to the right of the lookup column and breaks when columns are inserted. INDEX/MATCH can look in any direction, is more flexible, and does not break with structural changes. In professional models, INDEX/MATCH is the standard. Know both, use the latter.

How to Prepare: The Honest Answer
---------------------------------

Reading interview guides is a starting point. But the gap between knowing the answers and demonstrating them cleanly under time pressure — on a blank spreadsheet, with an interviewer watching — is where most candidates fail. The only preparation that actually works is building models repeatedly until the process becomes automatic.

At Financial Modeling New York, our 1-on-1 sessions replicate live interview conditions: blank spreadsheet, timed exercise, real-time feedback on structure, logic, and error correction. We have prepared candidates for Goldman Sachs, KKR, Apollo, and Blackstone. Most candidates need three to five sessions to reach interview-ready speed and accuracy.

Frequently Asked Questions
--------------------------

### How far in advance should I start preparing for a modeling test?

Six to eight weeks if you have limited modeling experience. Four weeks if you have built models professionally but not under timed conditions. Two weeks is the absolute minimum — and only if you are already fast and accurate.

### Do boutique banks test modeling differently than bulge brackets?

Boutiques often go deeper on a specific model type relevant to their focus (e.g., restructuring, energy, healthcare). Bulge brackets test breadth — three-statement, DCF, LBO, comps — in a single session. Both reward clean structure and logical assumptions over complexity.

### Is there a standard format for financial modeling tests?

No universal standard, but most tests follow a similar pattern: a fictional company with financials, a set of operating assumptions, and instructions to build a specific model. The key variable is time: some firms give 2 hours, others give 4. Always ask in advance.

**→ Ready to sharpen your modeling skills before your next interview? Our 1-on-1 coaching sessions are designed for exactly this — contact Financial Modeling New York to schedule your first session.**

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

[](https://www.financial-modeling.com/financial-modeling-interview-questions-guide# "Scroll back to top")
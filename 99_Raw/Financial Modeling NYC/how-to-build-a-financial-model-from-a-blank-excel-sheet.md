# How to Build a Financial Model from Scratch in Excel

**Source:** https://www.financial-modeling.com/how-to-build-a-financial-model-from-a-blank-excel-sheet

---

[Skip to content](https://www.financial-modeling.com/how-to-build-a-financial-model-from-a-blank-excel-sheet#content "Skip to content")

How to Build a Financial Model from a Blank Excel Sheet
=======================================================

![](https://www.financial-modeling.com/wp-content/uploads/2025/12/how-to-excel-model.jpg)

Building a financial model from a blank Excel workbook is a core competency for analysts in IB, PE, and [corporate finance](https://www.financial-modeling.com/glossar/corporate-finance/)
. Regardless of transaction type or business model, the objective is always the same: construct a **transparent, auditable, and fully linked** model that can support [valuation](https://www.financial-modeling.com/glossar/valuation/)
, diligence, and decision-making.  
This article provides a rigorous, repeatable framework for building such a model from scratch — using IB-standard structure, disciplined sequencing, and a clean technical architecture.

**The “Blank Sheet to Model” Framework**
----------------------------------------

Every professional model follows the same structural backbone:

| **Component** | **Purpose** |
| --- | --- |
| **Model Infrastructure** | Enforce structure, reduce errors, control versioning |
| **Assumption Architecture** | Define all drivers _before_ inserting formulas |
| **Operating Schedules** | Build revenue, COGS, Opex, CapEx, [Working Capital](https://www.financial-modeling.com/glossar/working-capital/) |
| **Financing Engine** | Model debt, interest, repayments, and [equity](https://www.financial-modeling.com/glossar/equity/)<br> flows |
| **Three Statements** | Integrate all schedules into IS, CF, and BS |
| **Outputs** | Produce KPIs, FCF, valuation, scenarios, sensitivities |

This structure is consistent across IB, PE, VC, and corporate operating models.

**Step-by-Step Procedure**
--------------------------

### **Step 1 — Set Up the Workbook Infrastructure**

**Objective:** create consistency, enforce integrity, and prevent error propagation.

#### **1.1 Sheet Architecture**

Use a logical, top-down flow:

*   **Assumptions**
*   **Operating Schedules**
*   **Financing**
*   **Three Statements**
*   **Outputs**

#### **1.2 Formatting Conventions**

*   Inputs = **blue**
*   Formulas = **black**
*   External links = **green**
*   Checks = **red**

#### **1.3 Time Axis**

*   Place all periods in a single row.
*   Reference this row everywhere — never duplicate period logic.

#### **1.4 Validation Checks**

*   [Balance sheet](https://www.financial-modeling.com/glossar/balance-sheet/)
     balance
*   Circularity flags
*   Sign checks for cash flows
*   Revolver usage tests

#### **1.5 Versioning**

Include a header with:

*   Version number
*   Date
*   Analyst initials
*   Notes on changes

**Best Practice:** Never mix inputs and formulas on the same sheet.

### **Step 2 — Build the Assumptions Sheet**

The assumptions sheet becomes the **single source of truth** for the entire model.  
  
Group inputs into clean, auditable blocks:

| **Category** | **Examples of Inputs** |
| --- | --- |
| **Operational Drivers** | Units sold, price, churn, utilization, capacity |
| **Cost Structure** | % of revenue, cost per unit, headcount, salaries |
| **Investment** | CapEx, useful life, maintenance vs. growth CapEx |
| **Working Capital** | DSO, DIO, DPO, turnover assumptions |
| **Financing** | Interest rates, revolver rules, [amortization](https://www.financial-modeling.com/glossar/amortization/) |
| **Tax** | Statutory rate, NOL attributes |

**Rule:** All downstream schedules must reference this sheet exclusively.

### **Step 3 — Build the Operating Schedules**

Construct schedules **left to right**, ensuring traceability and clean dependency chains.

#### **3.1 Revenue Schedule**

*   Start with **Volume × Price**.
*   Add business-model adjustments (e.g., churn, discounts, FX, downtime).
*   Present revenues by product, segment, or geography.

#### **3.2 COGS Schedule**

*   Tie cost/unit assumptions to utilization and capacity.
*   Exclude [depreciation](https://www.financial-modeling.com/glossar/depreciation/)
     (belongs only in CapEx/D&A).

#### **3.3 Opex Schedule**

*   Personnel: **Headcount × cost per FTE**.
*   Other opex: use % of revenue only when the business model supports it.

#### **3.4 CapEx and Depreciation**

*   Split between **maintenance** and **growth** CapEx.
*   Depreciation logic: `Depreciation = (Opening PP&E + New CapEx – Disposals) / Useful Life`

#### **3.5 Working Capital**

Use days or turnover methods:

*   AR = Revenue × DSO / 365
*   Inventory = COGS × DIO / 365
*   AP = COGS × DPO / 365

**ΔNWC** feeds directly into the [Cash Flow Statement](https://www.financial-modeling.com/glossar/cash-flow-statement/)
.

### **Step 4 — Build the Financing Engine**

#### **4.1 Debt Schedule**

Model a clean, auditable roll-forward:

*   Opening debt
*   Revolver draws
*   Mandatory amortization
*   Optional repayments
*   Closing debt

Interest expense = **average debt balance × [interest rate](https://www.financial-modeling.com/glossar/interest-rate/)
**.

#### **4.2 Equity Schedule**

For transactions:

*   Sponsor equity
*   Management rollover
*   Preferred equity instruments

For corporate models:

*   [Dividends](https://www.financial-modeling.com/glossar/dividends/)
    
*   Share repurchase programs
*   Issuances

### **Step 5 — Build the Three [Financial Statements](https://www.financial-modeling.com/glossar/financial-statements/)
**

#### **5.1 [Income Statement](https://www.financial-modeling.com/glossar/income-statement/)
**

*   Revenue → EBITDA
*   EBITDA → EBIT (via depreciation & amortization)
*   EBIT → EBT (via interest)
*   EBT → Net Income (via taxes)

#### **5.2 Cash Flow Statement**

*   **CFO:** Net Income + D&A – ΔNWC
*   **CFI:** CapEx
*   **CFF:** Debt flows, equity flows, dividends

Check: **Cash roll-forward = change in cash on the Balance Sheet**.

#### **5.3 Balance Sheet**

Reference all supporting schedules:

| **Balance Sheet Item** | **Source** |
| --- | --- |
| PP&E | CapEx schedule |
| Working Capital | WC schedule |
| Debt | Debt schedule |
| Equity | [Retained earnings](https://www.financial-modeling.com/glossar/retained-earnings/)<br> roll-forward |

Final check: **Assets = Liabilities + Equity**.

* * *

### **Step 6 — Create Outputs and Analysis Modules**

Typical IB/PE deliverables:

*   **Free Cash Flow** (unlevered and levered)
*   **Valuation:**
    *   DCF
    *   Trading comps
    *   Transaction comps
*   **Sensitivity tables:**
    *   WACC × terminal growth
    *   Revenue growth × margins
    *   [Leverage](https://www.financial-modeling.com/glossar/leverage/)
         × exit multiple
*   **Scenarios:**
    *   Base / downside / upside
    *   Toggled through assumption switches

**Practical Mini-Case Example — SaaS Model Skeleton**
-----------------------------------------------------

### **Assumptions**

*   Starting subscribers: **100k**
*   Monthly churn: **3%**
*   ARPU: **$20**
*   CAC: **$60**
*   DSO: **30 days**
*   CapEx: **5% of revenue**

### **Revenue Logic**

Subscriber roll-forward:

    Ending Subs = Starting Subs × (1 − Churn) + New Subs
    

Revenue:

    Revenue = ARPU × Average Subs × 12
    

### **COGS & Margin Structure**

*   COGS = **25% of revenue**
*   EBITDA margin = **30%**

### **Working Capital**

*   AR = Revenue × 30 / 365
*   No inventory, minimal AP → ΔNWC driven by AR only.

### **Outputs**

Free Cash Flow:

    FCF = EBITDA – CapEx – ΔNWC – Taxes
    

Sensitivity variables:

*   Churn ±1%
*   ARPU ±10%
*   CAC ±15%

This skeleton generalizes to most subscription-based models.

**Common Pitfalls & Analyst Best Practices**
--------------------------------------------

### **Frequent Errors**

*   Mixing assumptions with calculations
*   Hardcoding numbers inside formulas
*   Inconsistent time axis or mismatched period structures
*   Circularity from interest or revolver logic
*   Failure to test model under stress conditions

### **Best Practices**

*   Build **left → right**, **top → bottom**
*   Use consistent naming conventions
*   Keep formulas short; break into helper rows when needed
*   Add diagnostic checks:
    *   Balance sheet balance
    *   Cash reconciliation
    *   Revolver flags
*   Stress-test before handover

**Actionable Summary**
----------------------

*   Start with infrastructure: sheet layout, color codes, time axis, checks.
*   Build a clean, centralized assumption architecture.
*   Develop operating schedules before touching the three statements.
*   Layer in financing only once operating logic is stable.
*   Assemble IS → CF → BS with strict linking discipline.
*   Add outputs (FCF, valuation, sensitivities) once the core model is stable.

Following this process produces **audit-ready IB/PE-grade models** with minimal rework and maximum transparency.  

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

[](https://www.financial-modeling.com/how-to-build-a-financial-model-from-a-blank-excel-sheet# "Scroll back to top")
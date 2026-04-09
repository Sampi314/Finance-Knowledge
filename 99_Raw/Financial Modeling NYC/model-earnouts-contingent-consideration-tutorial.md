# Earnout Modeling: Excel Tutorial for M&A Pros

**Source:** https://www.financial-modeling.com/model-earnouts-contingent-consideration-tutorial

---

[Skip to content](https://www.financial-modeling.com/model-earnouts-contingent-consideration-tutorial#content "Skip to content")

Earnout Modeling Myths Exposed – Model Them Right or Watch Your LBO Unravel
===========================================================================

![](https://www.financial-modeling.com/wp-content/uploads/2026/03/earnout-modeling-myths.jpg)

Earnouts bridge [valuation](https://www.financial-modeling.com/glossar/valuation/)
 gaps in M&A by tying contingent payments to post-close performance metrics like EBITDA or revenue thresholds, recorded as liabilities under US GAAP/IFRS with fair value adjustments flowing through P&L. This tutorial equips you with Excel formulas to model earnouts dynamically – from probability-weighted payouts to 3-statement impacts, covenant interactions, and IRR sensitivity – ensuring bankable accuracy for diligence.

Earnout Structures & Triggers
-----------------------------

Earnouts pay if targets hit (e.g., $20M EBITDA in Year 1). Key types:

*   **Binary**: All-or-nothing (e.g., $10M if threshold met).
*   **Tiered**: Scaled (e.g., 0-50% payout on 80-120% achievement).
*   **Capped/Collared**: Min $5M, max $25M.

**Valuation Methods**: Scenario-based (probability-weighted DCF) or Monte Carlo for complex paths.  
  
**Standards**: Fair value at close (ASC 805 US GAAP/IFRS 3); revalue quarterly with gains/losses in Other Income.​[](https://breakingintowallstreet.com/kb/ma-and-merger-models/earnout-accounting/)
​

Step 1: Set Up Inputs & Probability Table
-----------------------------------------

Create a dedicated **Earnout Tab** with scenarios.  
  
**Inputs:**

text`Metric: EBITDA Y1 Target: $20M Payout per $1M: $2M (scaled) Cap: $30M Probability: Base 40%, Down 30%, Up 30%`

**Probability Table:**

text`Scenario | EBITDA | Achievement % | Payout | Prob | Exp Value Base     | $20M   | 100%          | $20M   | 40%  | $8M Down     | $15M   | 75%           | $15M   | 30%  | $4.5M Up       | $25M   | 125%          | $25M   | 30%  | $7.5M Weighted |        |               |        | 100% | $20M`

**Formula**: `=SUMPRODUCT(Payout_Range, Prob_Range)`

Step 2: Link to [Income Statement](https://www.financial-modeling.com/glossar/income-statement/)

-------------------------------------------------------------------------------------------------

Earnout hits P&L via fair value changes.  
  
**Initial Recognition (Close):**

text`Contingent [Liability](https://www.financial-modeling.com/glossar/liability/)  BS = Expected Payout PV (discount 10-15%) Goodwill = Purchase Price + FV(Earnout) - Net Assets`

**Revaluation (Q/E):**

text`ΔFV = New Exp Payout PV - Prior FV Income Stmt: Gain/Loss on Contingent Consid. = -ΔFV (Buyer view)`

**Excel**: `=IF(EBITDA>Target, MIN(Payout,Cap), Payout*(EBITDA/Target))`  
  
**Tax**: Non-deductible initially; changes may be.

Step 3: [Balance Sheet](https://www.financial-modeling.com/glossar/balance-sheet/)
 & Cash Flow Linkage
-------------------------------------------------------------------------------------------------------

**BS Impact:**

text`Cont. Liability += Payouts due [Equity](https://www.financial-modeling.com/glossar/equity/)  adjusts via [Retained Earnings](https://www.financial-modeling.com/glossar/retained-earnings/)  (through NI)`

**CF Statement:**

text`Cash Flow from Ops: No direct (non-cash reval) Financing: Actual payouts reduce Cash, Liability`

**Dynamic Formula** (Yearly Payout):

text`Payout Cash = MIN(Expected Payout, Available Cash post-Debt Svc)`

In LBOs, payouts compete with debt service – model as revolver draw if needed.[](https://www.wallstreetoasis.com/forum/private-equity/how-do-you-model-an-earn-out-in-an-lbo-model)
​

Step 4: 3-Statement Roll-Forward
--------------------------------

Integrate into full model:  
  
**IS → NI → RE → BS Equity**  
**BS Liability → Payout → CFS Financing → Cash → Revolver**  
  
**IRR Sensitivity**:

| Earnout Payout | Base IRR | Stress IRR |
| --- | --- | --- |
| $0  | 28% | 22% |
| $20M | 24% | 18% |
| $30M (Cap) | 21% | 15% |

**Pro Check**: Ensure DSCR >1.2x post-earnout in stress cases.

Step 5: Advanced: Monte Carlo & Covenants
-----------------------------------------

For precision, use Data Table or VBA for simulations.[](https://cbvinstitute.com/wp-content/uploads/2021/03/Presentation-Contingent-Considerations-Mar-4-2021.pdf)
​  
  
**Covenant Interaction**: Earnouts count as debt for [Leverage](https://www.financial-modeling.com/glossar/leverage/)
 tests (Total Debt + Earnout FV).[](https://www.wallstreetoasis.com/forum/private-equity/how-do-you-model-an-earn-out-in-an-lbo-model)
​  
  
**GAAP/IFRS Nuance**: Revals non-operating; exclude from EBITDA covenants.

Case: Tech SaaS [Acquisition](https://www.financial-modeling.com/glossar/acquisition/)
 Gone Sideways
-----------------------------------------------------------------------------------------------------

$150M SaaS buyout with $50M earnout on Y1-Y2 Revenue ($40M/$50M targets). Buyer models 60% probability.  
  
**Pre-Model Error**: Static $30M liability → overstated IRR.  
  
**Fixed Model**:

*   Y1 Rev miss ($35M): Reval down → $10M gain → NI boost.
*   Y2 Hit: $50M payout → Cash out, Liability zero.
*   Result: Realistic IRR 22% vs. 28% optimistic.

Financial-modeling.com’s frameworks bake this in from Day 1, linking earnouts to full 3-statements for audit-proof diligence.

Earnouts Breaking Your Model’s Logic?
-------------------------------------

Static earnout lines create circularities and covenant risks that kill deals in diligence.  
  
Financial-modeling.com provides battle-tested Excel templates and training to model contingent consideration seamlessly – from fair value calcs to LBO integration – trusted by PE firms for bank-financeable outputs.

FAQ: Earnout Modeling Essentials
--------------------------------

**How to record earnouts under US GAAP?**  
As contingent liability at FV on BS; quarterly revals to P&L as gain/loss on contingent consideration.[](https://breakingintowallstreet.com/kb/ma-and-merger-models/earnout-accounting/)
​​  
  
**Do earnouts affect EBITDA covenants?**  
No, revals are non-operating; but payouts impact cash and leverage tests.[](https://www.wallstreetoasis.com/forum/private-equity/how-do-you-model-an-earn-out-in-an-lbo-model)
​  
  
**Best Excel formula for tiered earnout?**  
MIN(Cap, Target\*PayoutRate + MAX(0, (Actual-Target)\*Acceleration)).[](https://breakingintowallstreet.com/kb/ma-and-merger-models/earnout-accounting/)
​  
  
**Monte Carlo vs. Scenario for valuation?**  
Monte Carlo for multi-year paths; scenarios suffice for binary/annual triggers.

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

[](https://www.financial-modeling.com/model-earnouts-contingent-consideration-tutorial# "Scroll back to top")
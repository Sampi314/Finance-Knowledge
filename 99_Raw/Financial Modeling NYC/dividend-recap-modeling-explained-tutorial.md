# Dividend Recap Modeling: Excel Tutorial + IRR Boost

**Source:** https://www.financial-modeling.com/dividend-recap-modeling-explained-tutorial

---

[Skip to content](https://www.financial-modeling.com/dividend-recap-modeling-explained-tutorial#content "Skip to content")

Dividend Recap Modeling Explained: Why Smart PE Firms Use It to Turbocharge IRR
===============================================================================

![](https://www.financial-modeling.com/wp-content/uploads/2026/03/dividend-recap-modeling.jpg)

A dividend recapitalization (dividend recap) lets a [private equity](https://www.financial-modeling.com/glossar/private-equity/)
 (PE) firm extract cash from a [portfolio](https://www.financial-modeling.com/glossar/portfolio/)
 company early by loading it with new debt, paying a special dividend to investors while keeping control. This LBO variant boosts internal IRR without selling the [asset](https://www.financial-modeling.com/glossar/asset/)
, but demands bulletproof cash flow modeling to avoid covenant breaches.[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
​

Core Mechanics: How Dividend Recaps Generate Returns
----------------------------------------------------

Picture a €100M LBO of a stable industrial firm with €20M EBITDA. PE sponsors finance it 60% debt (€60M at 6% interest), 40% [equity](https://www.financial-modeling.com/glossar/equity/)
 (€40M). Post-Year 2 operational improvements push EBITDA to €25M. Instead of waiting 5 years for an exit, they refinance: Issue €50M new Term Loan B at L+400bps, repay existing debt partially, and distribute €40M dividend to LPs. Equity base drops to zero – IRR jumps from 25% to 35% annualized.[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
​  
  
This hinges on senior debt capacity (typically 3.0-4.0x trailing EBITDA) and total [leverage](https://www.financial-modeling.com/glossar/leverage/)
 headroom under bank covenants. In our [financial modeling](https://www.financial-modeling.com/glossar/financial-modeling/)
 courses at financial-modeling.com, we stress circularity breakers and debt schedules that dynamically resize tranches based on [pro forma](https://www.financial-modeling.com/glossar/pro-forma/)
 leverage ratios.[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
​

Step-by-Step: Building a Dividend Recap in Excel
------------------------------------------------

Start with a 3-statement [LBO model](https://www.financial-modeling.com/glossar/lbo-model/)
 ([Income Statement](https://www.financial-modeling.com/glossar/income-statement/)
, [Balance Sheet](https://www.financial-modeling.com/glossar/balance-sheet/)
, Cash Flow). Use revolver drawdowns for timing; integrate a debt waterfall with mandatory prepayments from excess cash flow (50% EBITDA sweep standard).

1.  **Sources & Uses Table**  
    Set initial LBO: €60M Term Loan A (5-year amortizing), €40M Revolver, €40M Sponsor Equity. Uses: €100M Enterprise Value + €5M Fees.
2.  **Debt Schedule with Recap Trigger**
    *   Column for each facility: Beginning Balance, Scheduled Amort, Mandatory Prepayments, Optional Prepayments, Draws, Ending Balance.
    *   Recap in Year 2: MIN(Debt Capacity, Existing Debt + New Issuance). New Debt = Dividend Size / (1 – Fees). Update uses table dynamically.[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
        ​
3.  **Dividend Payment Logic**  
    \=IF(Year=2, Proceeds – Existing Debt Repaid – Fees, 0). Flow to Equity Cash Flow line; reduce Sponsor Equity on BS to zero.
4.  **Returns Calculation (MOIC/IRR)**  
    \=IRR(Equity Inflows + Dividend + Exit Proceeds). Exit assumes 8.0x EBITDA multiple; model MoM multiples compression over hold period.
5.  **Sensitivity Tables**
    *   IRR vs. Entry Multiple (6.5x-9.0x) and Recap Timing (Y1-Y4).
    *   Leverage at Recap (3.5x-5.0x) vs. EBITDA Growth (5-15%).

But here’s the trap: Overlever a recap, and interest coverage dips below 2.0x – covenants trip, forcing asset fire-sale. We audit models for this in our M&A training, enforcing debt incurrence tests.[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
​

Dividend Recap vs. Standard LBO: Key Model Differences
------------------------------------------------------

| Feature | Standard LBO | Dividend Recap LBO |
| --- | --- | --- |
| **Equity Returns Driver** | Exit only (5Y hold) | Dividend + smaller exit |
| **Debt Schedule** | Single refinancing | Multi-tranche issuance mid-hold |
| **Risk Profile** | Operational leverage | [Financial leverage](https://www.financial-modeling.com/glossar/financial-leverage/)<br> spikes |
| **IRR Impact** | 20-30% baseline | +5-15% uplift if timed right |
| **Modeling Complexity** | revolver + 1 TL | TL A/B/C + PIK toggle [](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)<br>​ |

In practice, a PE client approached us post-LBO for a recap model ahead of lender meetings. Their base case ignored PIK debt optionality; we rebuilt with scenario switches (80% cash pay / 20% PIK at recap), proving 1.8x coverage and securing €75M new paper – dividend flowed immediately.[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
​  
  
**Book a 1:1 model review:** Spot recap pitfalls in your Excel before lender calls reject it. Our experts deliver bank-grade templates.  
  
Secure your edge: Schedule an expert feedback for transaction-ready precision.

FAQ: Dividend Recap Modeling Essentials
---------------------------------------

**When is the optimal timing for a dividend recap?**  
Typically Year 2-3 post-LBO, after EBITDA ramps 15-25%. Requires 3.5x+ debt capacity and 2.0x+ projected interest coverage.[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
​  
  
**How do you model recap debt capacity limits?**  
Cap at 4.0-5.0x Total Net Leverage or 1.5-2.0x First Lien, whichever tighter. Use MIN(EBITDA multiple, covenant tests).[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
​  
  
**What if covenants block the recap?**  
Build incurrence tests: Pro forma [compliance](https://www.financial-modeling.com/glossar/compliance/)
 post-recap (e.g., Coverage >2.0x). Add PIK toggle for flexibility.[](https://online-firmenbuch.com/companys/schreinerei-holzstolz-gmbh)
​  
  
**Does dividend recap dilute management equity?**  
No – sponsors often retain control via recap shares. Model as preferred dividend to LPs only.

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

[](https://www.financial-modeling.com/dividend-recap-modeling-explained-tutorial# "Scroll back to top")
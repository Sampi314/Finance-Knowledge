# PE Case Study: $150M Distribution LBO (Step-by-Step)

**Source:** https://uplevered.com/private-equity-case-study-distribution-lbo

---

[Skip to content](https://uplevered.com/private-equity-case-study-distribution-lbo#content "Skip to content")

Distribution businesses live and die by working capital. In this case study and Excel walkthrough, we tackle a $150â€¯million distributor LBO to see what makes these deals unique_._ Weâ€™ll walk through the downloadable hands-on model to show how improving day-to-day operations, like vendor rebates and route density, drive returns. **Download the Excel model now to follow along.**

**TL;DR — Distribution LBO Case Study ($150M Middle-Market Deal)**

What you’ll build: A complete LBO model for a $150M TEV distribution company with $20M EBITDA.

**5 tasks, 60 minutes:**

1.  Entry valuation — TEV at 7.5×, EV bridge to equity value
2.  Sources & uses — senior debt, sub debt, sponsor equity, transaction fees
3.  Operating model — 3-year revenue build, margin assumptions, ΔNWC
4.  Debt schedule — mandatory amort, cash sweep, interest expense
5.  Returns — exit at Year 5, MOIC and IRR at base/upside/downside

What ‘done’ looks like: S&U balances, BS balances every period, FCF drives debt paydown, returns fall in a reasonable range (2.0–3.0× MOIC, 15–25% IRR for a MM deal).

Download the Distribution Mini-LBO Model (Excel)
------------------------------------------------

Enter your email to unlock the model instantly. (No spam. Unsubscribe anytime.)

*   Fully built debt schedule + ABL revolver mechanics
*   Returns bridge + sensitivities (multiple / leverage / margin)
*   Clean, interview-ready formatting + inputs section

LBO Form for Dist (#13)

Get the Template

**Unlocked.** Click below to download:

[Download the Distribution Mini-LBO (XLSX)](https://uplevered.com/private-equity-case-study-distribution-lbo/?ul_distlbo_dl=1&cb=1775732007684)

If the download doesnâ€™t start, open the link in a new tab.

**Contents** [hide](https://uplevered.com/private-equity-case-study-distribution-lbo#)

[1 Download the Distribution Mini-LBO Model (Excel)](https://uplevered.com/private-equity-case-study-distribution-lbo#Download_the_Distribution_Mini-LBO_Model_Excel)

[2 Why distribution LBOs are different](https://uplevered.com/private-equity-case-study-distribution-lbo#Why_distribution_LBOs_are_different)

[3 Base Case Frame (the Deal in Numbers)](https://uplevered.com/private-equity-case-study-distribution-lbo#Base_Case_Frame_the_Deal_in_Numbers)

[4 Excel Walkthroughâ€” Build the Model](https://uplevered.com/private-equity-case-study-distribution-lbo#Excel_Walkthrougha_Build_the_Model)

[5 Hands-On Tasks](https://uplevered.com/private-equity-case-study-distribution-lbo#Hands-On_Tasks)

[6 Recommendation â€” invest or pass?](https://uplevered.com/private-equity-case-study-distribution-lbo#Recommendation_a_invest_or_pass)

[7 Further Reading](https://uplevered.com/private-equity-case-study-distribution-lbo#Further_Reading)

[8 Related Technical Guides](https://uplevered.com/private-equity-case-study-distribution-lbo#Related_Technical_Guides)

[9 Stay sharp. Subscribe to Deal Flow Bullet.](https://uplevered.com/private-equity-case-study-distribution-lbo#Stay_sharp_Subscribe_to_Deal_Flow_Bullet)

Why distribution LBOs are different
-----------------------------------

Distribution is a **working-capital sport**. Cash gets tied up in AR and inventory while suppliers still want to be paid. The **cash conversion cycle (CCC) = AR days + Inventory days âˆ’ AP days**; small day-shifts unlock (or consume) real dollars and move the **revolver** in/out. Everything below is geared to make that dynamic obvious in your model.

### Rebates (make P&L â‰  cash obvious)

**What they are:** Vendor volume discounts that **reduce COGS on the P&L now** but **pay in cash later**. The gap sits in **rebates receivable** (generally **excluded from ABL collateral**). **EBITDA is not cash flow**, soâ€”donâ€™t count on rebates to service debt until they hit cash.

**Model it like this (simple and explicit):**

*   P&L: show **COGS (gross)** and **less: rebates** (separate line â†’ transparent GM%).
*   Balance sheet: add **Rebates Receivable** (grows when you accrue, shrinks when paid).
*   Cash flow: make sure **Î” Rebates Receivable** flows inside **Î”NWC**.
*   Borrowing base: **exclude** rebates receivable from **eligible AR**.

**Quick mental math:** Every **$1.0M** of rebate accrual lifts **EBITDA** now but **$0** cash until it pays.

**Why this matters:** EBITDA can run **ahead of cash** in rebate-heavy periods; lenders **exclude** rebate receivables from ABL, so they **wonâ€™t fund debt service** until paid.  
**Model checkpoint:** You should see a **Rebates Receivable** line, **Î”NWC** capturing its change, and **BB** that **doesnâ€™t count** it; recheck **FCCR** when rebates receivable climbs.

### Asset-Based Lending (ABL) & availability (define the constraint)

**What it is:** A revolver secured by working capital.

Borrowing Base (BB): 0.85 Ã— eligible AR + 0.50 Ã— eligible Inventory â†’ Availability = MIN(BB, Facility Cap).

> **Borrowing Base (BB):** 0.85 Ã— eligible AR + 0.50 Ã— eligible Inventory â†’ Availability = MIN(BB, Facility Cap)
> 
> **Unused availability:** Availability âˆ’ Revolver EOP.

**The trap:** Sales/AR surge â†’ **BB up**, but you **draw** more to fund it; **unused availability can shrink**. The **facility cap** can bind before BB does.

**Model moves:**

*   Build a **BB block** with advance rates and **cap**.
*   Compute **Unused Availability**; **traffic-light** troughs (e.g., < ~$3mm = red).
*   Interest on **average** revolver; revolver = **cash plug** to min cash.

**Tiny example:** AR + **$5.0M** â†’ BB + **$4.25M** (85%). If you need the cash, youâ€™ll **draw $4.25M** and **unused availability** likely **falls**.

**Why this matters:** In distributors, **availability** (not theoretical BB) is often the **binding liquidity constraint**.  
**Model checkpoint:** Show **BB**, **Cap**, **Availability**, **Unused Availability**, and **Peak Revolver**; flag cap-bound periods (BB > Cap) and low headroom.

### Working-capital intensity (AR / Inventory / AP) (give a cheat sheet)

**Cash-Conversion-Cycle (CCC) basics:** **CCC = DSO + DIO âˆ’ DPO**. Shorter = better. Growth without turn improvements **consumes cash** and **forces revolver draws**.

**Per $100M cheat sheet (order of magnitude):**

*   **AR Â±5 days** â‰ˆ **Â±$1.37M** cash (5/365 Ã— $100M sales).
*   **Inventory Â±10 days** â‰ˆ **Â±$2.05M** cash if COGS â‰ˆ $75M (25% GM).
*   **AP Â±5 days** â‰ˆ **Â±$1.03M** cash (5/365 Ã— $75M).

**Model moves:**

*   Drive **AR/Inv/AP $** from **DSO/DIO/DPO** each year.
*   Flow **Î”NWC** to cash; link AR/Inv to **BB**; AP reduces **cash need**.
*   Add a **before/after mini-table** (e.g., **45/45/20 â†’ 40/35/25**).

**Why this matters:** Tiny day shifts move **millions of dollars**; without better turns or longer payables, **growth eats cash**.  
**Model checkpoint:** Run a mini-sensitivity (**Â±5d DSO, Â±10d DIO, Â±5d DPO**), watch **Î”NWC**, **revolver plug**, **FCCR**, and **Unused Availability** react.

### Route density & delivery optimization (convert ops into EBITDA)

**What it is:** More drops per route + tighter territories **lower delivery cost** (fuel, drivers, wear). Itâ€™s a **low-capex** lever.

**How to model (honest version):**

*   Phase **SG&A % reduction** (e.g., **+30â€“50 bps** EBITDA margin over **12â€“24 months**).
*   Include small enablement spend in **opex/capex** (routing software, dispatch rules).
*   Savings flow **EBITDA â†’ FCF â†’ lower revolver / higher FCCR**.

**Tiny example:** On **$200M** sales, **30 bps** SG&A save = **$0.6M** EBITDA; in a 10% cash interest world, thatâ€™s meaningful covenant headroom.

**Why this matters:** Routing tweaks create **repeatable EBITDA**, improving debt service **without** big capex.  
**Model checkpoint:** Confirm savings arenâ€™t double-counted; ensure they hit **EBITDA** and then reduce **revolver** / lift **FCCR** over time.

### Inventory optimization & product mix/scale (cash + margin)

**Two buckets, two effects:**

1.  **Turns (cash today):**
    *   DIO â†“ **10 days** can free **$2â€“3M** per **$100M** sales (assume ~25% GM).
    *   Model: lower **Inventory days** â†’ **Î”NWC inflow**; note **BB** may **shrink** but **liquidity improves** (less borrowing).
2.  **Mix & scale (margin every day):**
    *   Private label / price discipline / scale rebates can add **+50â€“150 bps** GM.
    *   Model: gradual **GM% lift** and **rebate % step-up**; rebates still **lag** in cash (receivable grows first).

**Guardrails:** Donâ€™t over-tightenâ€”stockouts can hit revenue and **raise DSO** (disputes, short ships).

**Why this matters:** **Turns** give **cash today**; **mix/scale** add **margin daily**â€”together they drive faster **deleveraging**.  
**Model checkpoint:** When **DIO falls**, check **Inventory $â†“**, **BBâ†“**, **Unused Availabilityâ†‘**; model **GM%** and **rebate %** ramps with a **rebates receivable lag** in **Î”NWC**.

Base Case Frame (the Deal in Numbers)
-------------------------------------

Letâ€™s set up the base case. **Industrial Inc.** is a regional industrial distributor with $25â€¯million in LTM EBITDA being acquired for 6.0Ã— EV/EBITDA, or $150â€¯million enterprise value. Weâ€™ll finance it with a combination of equity and debt, including an asset-based revolver to fund working capital. Key deal parameters:

**Deal Frame:**

| **Metric** | **Year 0** (2025) | **Year 5** (2030) |
| --- | --- | --- |
| EBITDA | $25M | ~$38M |
| EV / EBITDA | 6.0Ã— | 6.0Ã— |
| **Enterprise Value** | $150M | ~$230M |
| Net Debt | $75M | ~($20M) |
| **Sponsor Equity** | **($80M**) | **$245M** |

**Other Considerations:**

*   **Transaction Fees:** 3% of purchase enterprise value
*   **Debt Structure:**
    *   $75â€¯million senior term loan (@9% interest); optional prepayments with excess cash
    *   $5â€¯million ABL revolver draw (@6% interest)
        *   $30â€¯million revolver limit, tied to borrowing base (85% of AR + 50% of Inventory); $5MM drawn as close
*   **Tax Rate:** 25% (for cash tax calculations)
*   **Capex:** ~2â€“3% of sales (maintenance capex to keep operations running)
*   **Working Capital Assumptions:** AR Days 40 (improve to 35 by exit); Inventory Days 45 (improve to 40); AP Days 20 (stretch to 25). These improvements are phased in over the hold period.
*   **Rebate Policy:** Vendor rebates net against COGS in EBITDA, but cash receipt lags (rebates create a receivable that collects with delay).

This base case assumes no immediate multiple arbitrage â€“ entry and exit multiples are both ~6.0Ã—. A strong ops team at your firm is proficient at value creation, which will drive returns from EBITDA growth and debt paydown (operations and working capital wins). Now, onto the fun part â€“ building the model to see how it plays out.

**Overview of base case returns:**

| **Metric** | **Year 5** (2030) | **Industry Average Targets** |
| --- | --- | --- |
| Internal Rate of Return (IRR) | 25.1% | 25.0% |
| Multiple of Invested Capital (MOIC) | 3.1Ã— | 3.0Ã— |

Excel Walkthroughâ€” Build the Model
------------------------------------

In this section, weâ€™ll build a simplified LBO model step-by-step, focusing on the mechanics unique to a distributor. You can follow along in the provided Excel, which has an **â€œAssumptions & Questionsâ€?** tab and a **â€œMini\_LBOâ€?** tab where the model lives. Weâ€™ll highlight key formulas and logic as we go. Buckle up â€“ youâ€™ve got about an hour to complete this template, and by the end youâ€™ll deeply understand the moving pieces of a $150M distribution LBO.

### Sources & Uses

We start with the **Sources & Uses** table â€“ the transactionâ€™s funding roadmap. This lays out where the money comes from (sources) and how itâ€™s spent (uses) to close the deal.

![Sources and uses for distribution LBO Case Study with ABL Revolver, Senior Term Loan.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_sources-and-uses.webp)

Notice the term loan and revolver **3.2Ã— EBITDA** = sponsor equity of 3.2Ã— â€“ a moderate leverage deal. .

**Uses (total = $160M, 6.4Ã— EBITDA):**

*   **Purchase Enterprise Value:** **$150M** _(6.0Ã— on $25M EBITDA)_
*   **Transaction Fees:** **$5M** _(legal, banking, diligence)_. Note fees and min cash are equity-funded
*   **Minimum Cash to Balance Sheet:** **$5M** _(Day-1 operating cushion)_

**Sources (total = $160M, 6.4Ã— EBITDA):**

*   **Sponsor Equity:** **$80M** _(3.2Ã—)_ â€” **funds the $5M fees** and part of purchase price
*   **Senior Debt (Term Loan @ ~9%):** **$75M** _(3.0Ã—)_
*   **ABL Revolver Draw (@ ~5â€“6%):** **$5M** _(0.2Ã—)_ â€” **plugs to minimum cash**

**At-a-glance leverage at close (x EBITDA):**

*   **Gross debt:** **3.2Ã—** (3.0Ã— term + 0.2Ã— ABL)
*   **Equity:** **3.2Ã—**
*   **Total sources/uses:** **6.4Ã—**

**Why this matters:** This layout makes three things explicit: (1) **fees are equity-funded**, (2) the **revolver is a small plug** to meet **min cash**, and (3) youâ€™re underwriting **moderate leverage** (3.2Ã—) with plenty of ABL headroom for working-capital swings.

**Model checkpoint:**

*   **Sources = Uses** tie to **$160M**.
*   **xEBITDA column** totals **6.4Ã—** on both sides.
*   **Fees** shown in Uses and **covered by equity** (not by ABL).
*   **Opening balances** after close: **Cash â‰ˆ $5M**, **Term Loan $75M**, **Revolver $5M**, **Equity $80M** â†’ **Net debt â‰ˆ $75M (3.0Ã—)**.

One check: after funding, the companyâ€™s opening balance sheet will have ~$5â€¯M cash (minimum), $75â€¯M term debt, $5â€¯M revolver debt drawn, and $80â€¯M equity. Net debt is $75 M ($80â€¯M less $5â€¯M cash). This will be close to matching the $150â€¯M EV, but note there is usually a slight difference because fees/min cash distort a bit.

* * *

### Borrowing Base & Availability (ABL)

The **borrowing base (BB)** caps how much we can draw on the ABL based on working-capital collateral. Itâ€™s collateral math first, then a facility cap.

![Borrowing base setup using 85% of AR and 50% of inventory; rebates receivable shown but excluded from eligibility; operating NWC balances and AR/Inv/AP day assumptions visible.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_abl-borrowing-base.webp)

![](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_working-abl-1.webp)

#### **Eligibility & formulas**

*   **BB** = **85% Ã— eligible AR** + **50% Ã— eligible Inventory**  
    _(explicitly exclude rebates receivable and any ineligibles/reserves)_
*   **Availability** = **MIN(BB, Facility Cap)**
*   **Unused Availability** = **Availability âˆ’ EoP Revolver**

#### **Your model (what it shows)**

*   **Facility cap:** **$30mm**
*   **Close (2025A):** **BB â‰ˆ $28mm** â†’ **Availability â‰ˆ $28mm**; **EoP ABL = $5mm** â†’ **Unused â‰ˆ $23â€“24mm**
*   **AR +30d shock (2028P):** AR balance jumps; **BB â‰ˆ low-to-mid $30s** but the **cap binds**, so **Availability â‰ˆ $29â€“30mm**; **EoP ABL â‰ˆ $3mm** â†’ **Unused â‰ˆ $27mm**
*   **Post-shock:** BB normalizes (**~$29â€“32mm**) and availability remains under the **$30mm** cap

#### **Why it matters**

*   In a collections shock, **collateral (BB) can rise**, but **availability** is still **capped**â€”so the **headroom you can actually use** is what matters.
*   In your base build, **unused availability stays ample (>~$25mm)**, even when the cap binds. If revolver **usage** rises faster than collateral, **unused** can tighten **even as BB climbs**.

#### **Model checkpoints**

*   **Rebates receivable**: shown on the BS, **excluded from BB**, and **Î”Rebates** flows through **Î”NWC**.
*   Debt schedule shows **BB**, **Availability (cap-limited)**, **Unused**, and **EoP ABL** (e.g., close: **~$28 / ~$28 / ~$24 / $5**; shock: **~$35 / ~$29â€“30 / ~$27 / $3**).
*   Revolver is the **cash plug**; **optional term prepay** occurs **only when ABL = 0** and **cash > min**.

### Working Capital Days Schedule

This section converts **day counts â†’ dollar balances** and then computes **Î”NWC â†’ cash**.

**Formulas (annual):**  
AR = Revenue Ã— **DSO/365**â€ƒ|â€ƒInventory = COGS Ã— **DIO/365**â€ƒ|â€ƒAP = COGS Ã— **DPO/365**  
Operating NWC = **AR + Inventory + Rebates Receivable âˆ’ AP âˆ’ Accrued Exp.**  
Î”NWC = **NWCâ‚œ âˆ’ NWCâ‚œâ‚‹â‚?** (cash **use** if positive, **source** if negative)

![Working-capital days schedule (AR/Inv/AP) for distribution lbo case study](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_working-capital-days_pre.webp)

#### Pre-improvement snapshot (2025A)

*   **Days:** **AR 40d**, **Inventory 45d**, **AP 20d**
*   **Rebates receivable:** **2.0% of COGS** (on BS, _excluded from ABL_, cash lags P&L)

**Target glide path (post-improvement)**

*   **AR** steps down to **35d** by **2029+**
*   **Inventory** tightens to **40d** and holds
*   **AP** stretches to **25d** and holds
*   **Rebates receivable** ramps to **3.0% of COGS** by **2028** and holds (still excluded from ABL)

One-year shock (2028P)

*   **Collections slow:** **AR jumps to 65d** for one year, then normalizes

#### What your model shows (balances, $mm)

*   **AR:** 21.9 â†’ 22.3 â†’ 22.4 â†’ **41.2** (shock) â†’ 22.9 â†’ 23.6 â†’ 24.3 â†’ 25.0
*   **Inventory:** 19.7 â†’ 19.9 â†’ 19.8 â†’ 19.5 â†’ 20.1 â†’ 20.7 â†’ 21.3 â†’ 22.0
*   **AP:** 8.8 â†’ 9.9 â†’ 11.1 â†’ 12.2 â†’ 12.6 â†’ 13.0 â†’ 13.3 â†’ 13.7
*   **Rebates receivable:** 3.2 â†’ 3.9 â†’ 4.6 â†’ 5.3 â†’ 5.5 â†’ 5.7 â†’ 5.8 â†’ 6.0
*   **Operating NWC:** **34.1 â†’ 33.6 â†’ 32.7 â†’ 50.4 â†’ 32.3 â†’ 33.3 â†’ 34.3 â†’ 35.3**  
    _(% of sales on sheet: **17.0% â†’ 15.9% â†’ 14.7% â†’ 21.8% â†’ 13.6% â€¦**)_

**Cash implications (Î”NWC â†’ cash):**

*   **2028 shock:** NWC **+~$18mm** (32.7 â†’ 50.4) = **~$18mm cash outflow**, drives a revolver draw
*   **2029 normalization:** NWC **âˆ’~$18mm** (50.4 â†’ 32.3) = **~$18mm cash inflow**, repays revolver and enables optional term prepay
*   Across the hold, the glide **40/45/20 â†’ 35/40/25** steadily **releases cash** vs. a no-improvement case

**Why this matters:** In distribution, **tiny day shifts move millions**. The one-year AR spike shows how quickly **liquidity can tighten** even when the underlying business is fine.

#### Model checkpoints (tie-outs)

*   **Days drive dollars:** AR/Inv/AP balances come **only** from DSO/DIO/DPO.
*   **Î”NWC** feeds FCF directly (cash **use** if positive).
*   **Rebates receivable** sits on BS, **excluded from ABL**; **Î” rebates** is included in **Î”NWC**.
*   **Revolver = cash plug:** draws in **2028**, repays in **2029** (min cash maintained).
*   Keep a mini before/after banner visible: **2025A â†’ 2029+: AR 40â†’35 | Inv 45â†’40 | AP 20â†’25**.

![Working-capital days schedule (AR/Inv/AP) with Year-3 AR +30d shock (AR days 65) driving AR to ~$41M; rebates receivable ramps to 3% of COGS; AP stretches to 25 days.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_working-capital-days_Post.webp)

#### Change in NWC â€” one-paragraph explainer

Each year, **Î”AR + Î”Inventory âˆ’ Î”AP** flows into the cash bridge as **Î”NWC**. Improving **AR days** or **Inventory days** creates **inflows** (balances shrink relative to sales). Extending **AP days** is also an **inflow** (youâ€™re borrowing from suppliers). Conversely, growth that builds AR/inventory is a **cash outflow**. Thatâ€™s why the model subtracts **Î”NWC** in FCF: if working capital increases, it **consumes cash**; if it falls, it **releases cash**â€”critical in Year 1 post-close and in the **2028 shock â†’ 2029 normalization** sequence.

* * *

### Free Cash Flow Calculation (how to read this block)

This block converts the P&L into cash and then shows how cash moves through the debt stack. We start at **EBITDA**, subtract **cash taxes, cash interest, capex**, and the **change in operating NWC** (AR, inventory, AP, and rebates receivable), to get **FCF before debt service**. Then we take **mandatory amortization**, let the **revolver act as the cash plug**, and use any residual to make **optional prepayments** on the term loan (subject to cash minimums and no revolver balance).

![Free cash flow bridge: EBITDA grows from $29M to $40M; taxes, interest, capex, and Î”NWC shown; shock year revolver draw; large optional repayments in rebound years; cash balance rises.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_lbo-fcf-outputs.webp)

_Note the 2028P AR shock (Î”NWC outflow) triggers a revolver draw; the 2029P normalization reverses it and accelerates optional term prepay._

**Key mechanics**

*   **Rebates** reduce COGS (so margin improves) but **cash is delayed** â€” the increase in rebates receivable is included in Î”NWC (use of cash).
*   **Interest** is calculated on average balances; it steps down as debt is repaid.
*   **Capex** is maintenance-like (low for distributors; your model rounds it to ~$4â€“$6MM/yr).

#### What your model shows (numbers line up with your table)

*   **EBITDA** grows from **$29MM â†’ $40MM** from year 1 to year 5.
*   **Cash taxes** run about **25% of EBIT** (rising with profits).
*   **Capex** stays steady at **~$4â€“$6MM** per year.
*   **Î”NWC** drives the story:
    *   **2028P shock:** AR days jump for one year â†’ **Î”NWC = (18)** (i.e., **$18MM outflow**), so **FCF before debt service** dips to **$3MM** and the **revolver draws $3MM** to fund the gap.
    *   **2029P normalization:** AR days snap back â†’ **Î”NWC = +18** (inflow), **FCF before debt service** rebounds to **$39MM** and the **revolver repays (3)**.
    *   Outside the shock year, Î”NWC is modest (**~$1MM** outflow each year) as AR/Inv tighten and AP stretches (your glide path 40/45/20 âžœ 35/40/25).
*   **After amortization**, you generate **$11â€“$25MM** of **FCF after debt service**.
*   **Optional prepay** sweeps excess cash to the term loan whenever (i) the revolver is **$0** and (ii) **cash > minimum**. Thatâ€™s why you see **(7), (17), (5), (36)** in the prepay row â€” the 2029P surge is the Î”NWC reversal being swept to debt.
*   **Ending cash** builds once debt is largely down: **~$5MM** flat early, then **$21MM / $46MM / $71MM** as optional prepay winds down.

**Plain-English takeaway:** in a distributor, small changes in **days** swing **Î”NWC** by eight figures, which flips revolver usage and optional paydowns year-to-year even when EBITDA is steady. Your one-year AR spike makes that visible without breaking the model.

**Model guardrails (built-in)**

*   **Revolver is the plug.** It draws to cover cash shortfalls and repays on excess cash, but never exceeds **availability** or goes below **$0**; **minimum cash** is respected.
*   **Optional prepay logic.** Only fires when **EoP ABL = 0** _and_ **cash > min**. Prepay is capped at **(BOP term + current mandatory)** so you canâ€™t over-repay.
*   **Î”NWC includes rebates.** **Rebates receivable** are **excluded from the ABL BB** but **included in Î”NWC**, so a rebate ramp is a **cash use** even as EBITDA rises.

> If something looks off:  
> â€¢ **Unused availability < 0?** Your draw is being capped by the facilityâ€”check the **BB** and **cap**.  
> â€¢ **Term prepay happening while ABL > 0?** Sweep condition is misappliedâ€”ensure prepay is gated by **EoP ABL = 0**.  
> â€¢ **Cash building while ABL > 0?** Youâ€™re likely hitting **min cash** or availability; confirm the **revolver repay** logic.

* * *

### Debt Paydown

**Objective:** See how cash flows through the **revolver (ABL)** and **term loan**, and confirm the sweep only pre-pays term when the revolver is at **$0** and **cash > min**.

![Debt schedule with ABL borrowing base, availability and unused availability; senior term loan amortizes from $75M to ~$8M by 2030; interest expense falls; FCCR and net-leverage improve.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_debt_schedule.webp)

_Pay attention to whether and when the revolver fully pays off and if any term prepayment happens (it should only prepay when revolver = $0 and excess cash beyond $5M exists â€“ as we set in our logic)._

#### How the model works

*   **Revolver is the plug.** Draws to keep **min cash** in shock years; repays first when thereâ€™s excess cash. Never exceeds **availability** (MIN\[BB, facility cap\]) and never drops below **$0**.
*   **Mandatory amortization:** **1%**/yr on the term loan (typical).
*   **Optional sweep:** After revolver = **$0** and cash > **$5mm**, excess goes to **term prepay** (capped at remaining principal so you canâ€™t over-repay).
*   **Interest on average debt:** Term @ **9%**, ABL @ **6%**, both on **average** balances for the year.

#### What your model shows (year-by-year highlights)

*   **2025A:** ABL starts **$5mm** and repays to **$0**; term goes **$75 â†’ $67mm** (-$1mm mandatory, **\-$7mm** optional).  
    _Interest â‰ˆ $7mm; Net Debt/EBITDA ~ **3.0x**; FCCR **2.4x**; Unused availability **~$24mm**._
*   **2026P:** Strong FCF; term **$67 â†’ $50mm** (-$1mm mandatory, **\-$17mm** optional).  
    _Interest â‰ˆ $6mm; leverage **2.2x**; FCCR **3.4x**._
*   **2027P:** Term **$50 â†’ $44mm** (-$1mm mandatory, **\-$5mm** optional).  
    _Interest â‰ˆ $4mm; leverage **1.4x**; unused availability **~$29mm**._
*   **2028P (AR +30d shock):** Working-capital outflow forces **EoP ABL â‰ˆ $3mm**; sweep pauses.  
    _Availability limit binds at **$30mm**; unused availability still **~$27mm**; interest stable._
*   **2029P (normalization):** Revolver repays **(3)** to **$0**; big Î”NWC inflow drives **term prepay (-$36mm)** â†’ term **$44 â†’ $8mm**.  
    _Interest â‰ˆ $4mm; Net Debt/EBITDA **~0.1x**; FCCR **5.2x**._
*   **2030Pâ€“2032P:** Term is cleared (**$8 â†’ $0**), cash builds (**$21 / $46 / $71mm**), Net Debt turns **negative** (net cash).  
    _Interest drops to â‰ˆ **$1mm** then **~0**; coverage ratios become very high._

#### Do this (reader tasks)

*   **Confirm sweep logic:** no term prepay in **2028P** while **EoP ABL > 0**; big prepay occurs in **2029P** once ABL hits **$0** and cash > min.
*   **Check interest math:** Total interest â‰ˆ `9% Ã— avg Term` + `6% Ã— avg ABL` (your totals fall **$7 â†’ $1mm** as debt declines).
*   **Validate headroom:** **Unused availability** never negative; **EoP ABL â‰¤ Availability** each year.
*   **Watch covenants:** **FCCR** stays above **~1.1Ã—** (your path: **2.4Ã— â†’ 5.2Ã— â†’ 18.0Ã—**); **Net Debt/EBITDA** trends down to **<1.0Ã—** and then net cash.

#### Why it matters

Distributors live and die by **working-capital swings**. The schedule shows the classic ABL pattern: the revolver **zigzags** with AR/Inventory timing, while the sweep retires **term debt** aggressively once liquidity normalizesâ€”driving most of the multiple-safe return via **deleveraging** rather than heroic growth.

* * *

### Stress Test â€” AR **+30 days** for one year

**Objective:** Show how a one-year collections slip ripples through **Î”NWC**, **revolver usage**, and **availability** (cap binding).

![Working-capital days schedule with Year-3 AR +30d shock (AR days 65) driving AR to ~$41M; rebates receivable ramps to 3% of COGS; AP stretches to 25 days](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_working-capital-shock.webp)

_Notice that although our borrowing base went up with AR, the **constraint** was actually the availability limit and the businessâ€™s own need for cash â€“ a stark reminder that base â‰  cash in hand._

#### Do this

*   Set **ARShock = 30** (applies to **2028P** only).
*   Recalculate; keep all other assumptions the same.
*   Note **Î”NWC**, **FCF before/after debt**, **EoP ABL**, **Unused availability**, and **IRR/MOIC**.

#### What happens in your model

*   **AR days** jump **40 â†’ 65** in **2028P**; **AR balance** spikes to **~$41mm** (from ~22mm).
*   **Î”NWC â‰ˆ +$18mm (use of cash)** â†’ **FCF before debt** dips to **~$3mm**.
*   The **revolver draws ~+$3mm** (cash plug) to keep min cash.
*   **Borrowing base** rises to **~$45mm**, but the **facility cap ($30mm) binds**:
    *   **Availability limit â‰ˆ $30mm**
    *   **EoP ABL â‰ˆ $3mm**
    *   **Unused availability â‰ˆ $27mm** (ample headroom)
*   **2029P normalization:** AR days revert; **Î”NWC â‰ˆ âˆ’$18mm (inflow)** â†’ revolver repays **(3)** to **$0**, and a large **term prepay (âˆ’$36mm)** fires.
*   Returns take a **modest hit** (timing only): you should see a **small IRR dip** with **MOIC unchanged** at exit.

#### Checkpoints (tie-outs)

*   **Î”NWC row:** ~**+18** in **2028P**, **âˆ’18** in **2029P**.
*   **Debt schedule:** **BB ~45 / Availability 30 / Unused ~27 / EoP ABL ~3** in the shock year.
*   **Covenants:** **FCCR** remains comfortably **\> 1.2Ã—** throughout (your path sits multiple turns above).
*   **No over-advance:** **EoP ABL â‰¤ Availability**; Unused never negative.

#### Why it matters

In ABLs, **collateral can rise while usable headroom is capped**â€”what matters is **unused availability** and the revolverâ€™s ability to **bridge timing shocks** without tripping covenants. The next yearâ€™s normalization often **over-delivers cash**, accelerating **term paydown** and restoring trajectory.

What happens when AR days spike? First, AR balance balloons because customers are slower to pay â€“ cash gets sucked out of the business to fund this receivable growth. Our borrowing base will **increase** (more AR means more collateral), but thatâ€™s not exactly good news â€“ it just means the bank will lend us more _because we need it_. In Year 3 of our model, AR days go from ~35 to 65 for the shock. The borrowing base formula yields a much higher number (say it jumps from ~$30M to ~$45M). However, remember the facility cap is $30M, so any base beyond $30M doesnâ€™t help â€“ weâ€™re still limited to $30M of total revolver borrowing.

The company will draw heavily on the revolver to cover payables and expenses during this cash crunch. In our model, we see the **revolver peak** usage in Year 3. Unused availability tightens: even though the base was theoretically $45M, the cap means max $30M credit; if we end up borrowing, say, $25M, then only $5M is left undrawn. The liquidity headroom shrinks, which is dangerous â€“ one more hit and youâ€™re at the ceiling.

This AR shock also **dents IRR**. Why? Because the extra borrowing incurs more interest and the principal wonâ€™t get fully repaid until the customer pays up in Year 4. That means higher debt at exit or less cash to pay down term debt. In our scenario, the equity IRR might drop a few percentage points versus the base case due to this one-year shock. Itâ€™s a classic distribution risk: growth or an external shock can **force borrowing and delay deleveraging**, harming returns.

When things normalize in Year 4, AR days go back down, releasing cash (as customers catch up payments). The revolver then gets paid back down quickly with that inflow. However, some damage is done in terms of interest cost and lost time.

* * *

### Equity Value Bridge

Letâ€™s step back and see how the value is created in this deal. The **Equity Value Bridge** breaks down the sources of equity gain from entry to exit: how much came from EBITDA growth, how much from multiple change, and how much from debt paydown.

**Essentially shows:** how equity grows from **close â†’ exit** via three levers:

1.  **EBITDA growth (EV)**
2.  **Multiple change (EV)**
3.  **Net debt paydown / excess cash**

![Equity value bridge (base): Start equity $71M; EBITDA growth adds $79M EV; multiple delta 0; net debt paydown adds $95M; exit equity $245M; tie check implied.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_equity-value-bridge.webp)

#### **Formulas (no cell refs):**

*   **Start Equity** = equity value at **close** (TEV âˆ’ net debt at close)  
    _Note:_ because **fees/min cash are equity-funded**, **Start Equity** can be **< sponsor equity check**. Thatâ€™s why your bridge starts at **~$71mm** even though total equity raised at close was higher.
*   **EBITDA Growth (EV)** = (Exit EBITDA âˆ’ Entry EBITDA) Ã— **Exit multiple**
*   **Multiple Î” (EV)** = (Exit multiple âˆ’ Entry multiple) Ã— **Entry EBITDA**
*   **Net Debt Paydown / Excess Cash** = NetDebt\_Close âˆ’ NetDebt\_Exit
*   **Exit Equity (check)** = **sum of the above** (should tie to modelâ€™s exit equity)

#### **Your base case (matches the chart):**

*   **Start Equity:** **$71mm**
*   **EBITDA Growth (EV):** **$79mm**
*   **Multiple Î” (EV):** **$0mm** _(you keep the same multiple at entry and exit)_
*   **Net Debt Paydown / Excess Cash:** **$95mm**
*   **Exit Equity (tie):** **$245mm**

> The bridge adds cleanly: **71 + 79 + 95 = 245** (no plug), confirming the math.

#### **Why these bars move (distribution context):**

*   **EBITDA growth** comes from **pricing/rebate capture** (rebates net against COGS), **gross-margin lift**, and **route/Inventory Optimize** efficiencies (lower SG&A and DIO).
*   **Deleveraging** is powered by steady FCF and **working-capital release** (AR/Inv down, AP up) after the one-year AR shock normalizes.
*   **Multiple** is held flatâ€”typical for steady distributorsâ€”so **returns are earned operationally**.

#### **Do this (reader task):**

*   Confirm **Exit Equity** on the bridge equals the equity value in your Year-5 outputs.
*   Flip the **exit multiple** scenario (Â±1.0Ã—) and watch only the **Multiple Î”** bar move.
*   Toggle the **AR shock** off and note how the **Net Debt Paydown** bar grows (more cash swept to term).

#### Why it matters:

This bridge mirrors the classic LBO value levers: **EBITDA growth, multiple arbitrage, and debt paydown**. It forces you to quantify what drove the equity return. In distribution deals, youâ€™ll typically see a hefty portion from EBITDA growth (via margin expansion and maybe some tuck-in acquisitions) and good chunk from debt paydown (if operations throw off cash). Multiple expansion is often not a given in a steady industry like this, so you have to **earn** your return operationally.

### Paper LBO â€” sanity check (does the full build make sense?)

Before declaring victory, we ensure our detailed model makes sense with a back-of-envelope â€œpaper LBOâ€? and key credit metrics. This is a sanity check section.

![Returns strip: 2030 exit at 6.0Ã—; EBITDA ~$38M â†’ EV ~$229M; net debt ~$16M; sponsor equity ~$245M; base IRR 25.1% and MOIC 3.1Ã—.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_equity-returns.webp)

**Quick math (back-of-envelope):**

*   **Equity in:** ~$80 sponsor check (fees/min cash funded with equity).
*   **Equity out:** **$245mm** (Year-5, 6.0Ã— exit on ~$38mm EBITDA minus ~$16mm net debt).
*   **MOIC:** **$245 / $80 â‰ˆ 3.1Ã—** (matches model).
*   **IRR:** **~25% over 5 years** (your returns block shows **25.1%**).

**Liquidity & covenants:**

*   **Peak revolver draw:** **$5mm** at close; **$3mm** in the AR-shock year; otherwise **$0**.
*   **Min unused availability:** **~$24mm** (close), **~$27mm** during the shockâ€”headroom never negative even when the **cap binds**.
*   **FCCR (min):** **~2.4Ã—** (well > typical 1.1Ã— threshold).
*   **Binding constraint:** neither covenant nor availability actually trips; **availability** comes closest in the shock year, so thatâ€™s the _watch_ item.

**What moves the return:**

*   **Deleveraging** and **EBITDA growth** are the big bars in the bridge; **multiple** is flat.
*   The one-year AR spike **pulls IRR down a touch** (timing), but normalization the next year **over-delivers cash** and accelerates the sweepâ€”MOIC is basically unchanged.

**Sensitivities (how to read your grids):**

*   In the **multiple grid**, moving **Â±1.0Ã—** on exit typically shifts IRR by **~3â€“5 pts** and MOIC by **~0.2â€“0.4Ã—**.
*   In the **exit year grid**, slipping exit by a year trims IRR (same MOIC over longer time); pulling exit forward boosts IRR.
*   Highlight the cell corresponding to your base case so readers can orient quickly.

**Screenshot cues:**

*   Place the **Returns strip** (MOIC/IRR table) first, then the **two sensitivity heatmaps**. Caption:  
    _â€œBack-of-envelope matches the build: ~3.1Ã— / ~25% at 6.0Ã— exit. Headroom stays positive even in the AR shock; FCCR never breaches.â€?_

**One-liner conclusion:**  
_The detailed model passes the paper-LBO sniff test: **3.1Ã— MOIC / 25% IRR** with ample ABL cushion and healthy FCCRâ€”returns are earned via operations and deleveraging, not multiple expansion._

If the paper LBO math doesnâ€™t roughly match the modelâ€™s outputs (for MOIC/IRR), somethingâ€™s off. But assuming itâ€™s in line, weâ€™ve validated the model.

Finally, consider the exit: at 6.0Ã— exit on the higher EBITDA, the buyerâ€™s getting a company with better working capital metrics and lower debt. Would you pay more than 6Ã— for that improvement? Possibly â€“ and that could be upside if we assumed any multiple expansion. But as disciplined underwriters, we donâ€™t bank on it; itâ€™s gravy if it happens.

![IRR/MOIC two-way sensitivity by entry vs. exit multiple; base intersection at 7.5Ã—/7.5Ã— highlighted (IRR ~20.7%, MOIC ~2.6Ã—); higher exit multiples increase returns.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_sensitivity1.webp)

![IRR/MOIC sensitivity by exit year at selected entry multiple; earlier exits show higher IRR; base 2029/2030 cells highlighted; MOIC increases with longer holds.](https://uplevered.com/wp-content/uploads/2025/08/150m-distribution-lbo_sensitivity2.webp)

* * *

Hands-On Tasks
--------------

Download the model and work through these mini-exercises. Take a screenshot of each result (top of the relevant block) and jot 1â€“2 lines of explanation.

### 1) Borrowing base at close

**Do:** Using the AR & inventory balances at close, compute the ABL **borrowing base** and **availability**.  
**Formula:** **BB = 85% Ã— AR + 50% Ã— Inventory**; **Availability = MIN(BB, $30mm cap)**; **Unused = Availability âˆ’ EoP ABL**.  
**Expect:** BB â‰ˆ **$28â€“29mm**; Availability â‰ˆ **$28â€“29mm**; **EoP ABL = $5mm**; **Unused â‰ˆ $24mm**.  
**Screenshot:** Borrowing-base table (AR/Inv, advance %, cap, unused).

### 2) Extra inventory tightening (liquidity impact)

**Do:** Improve **inventory days by 10** (e.g., Year 1 to **35d**, gliding to **~25d** by Year 5).  
**Explain:** You should see a **one-time Î”NWC inflow**, **lower ABL BB**, **less revolver usage**, and **earlier term prepay**. Liquidity **improves** even though the BB shrinks.  
**Screenshot:** Working-capital days (before/after) and FCF block showing Î”NWC change.

### 3) Collections shock: AR **+30 days** for one year

**Do:** Set **ARShock = +30** for the designated shock year.  
**Report:** **Î”NWC** (use), **peak EoP ABL (~$3mm)**, and **minimum unused availability (~$27mm)**. Note that the **$30mm cap binds**, but headroom stays positive.  
**Screenshot:** WC table (with 65d AR) and debt lines for **Availability / Unused / EoP ABL**.

### 4) Sweep logic check (prepay only when ABL = 0)

**Do:** Verify thereâ€™s **no term prepay** in the shock year (ABL > 0), and a **large prepay** when AR normalizes (ABL = 0 and cash > min).  
**Expect:** Prepay pauses in the shock year; resumes next year with a **big sweep**.  
**Screenshot:** Debt schedule (EoP ABL, optional prepay row).

### 5) Build the equity value bridge by hand

**Do:** Using model outputs, compute:

*   **Start Equity** (equity value at close)
*   **EBITDA Growth (EV)** = (Exit EBITDA âˆ’ Entry EBITDA) Ã— Exit multiple
*   **Multiple Î” (EV)** = (Exit âˆ’ Entry multiple) Ã— Entry EBITDA
*   **Net Debt Paydown / Excess Cash** = NetDebt\_Close âˆ’ NetDebt\_Exit  
    **Tie-out:** Sum to the modelâ€™s **Exit Equity** (**â‰ˆ $245mm** in base). _Your bars should be ~**$71 / $79 / $0 / $95** â†’ $245_.\*  
    **Screenshot:** The bridge chart/table.

### 6) Paper-LBO sanity

**Do:** With just entry/exit numbers, compute **MOIC** and **IRR**, and pull: **min FCCR**, **min unused availability**, **peak revolver**.  
**Expect (base):** **~3.1Ã— MOIC**, **~25% IRR**; **FCCR â‰¥ ~2.4Ã—**; **unused availability stays positive** even in the shock year; **peak ABL â‰ˆ $3â€“5mm**.  
**Decide:** Which was the binding constraint at the troughâ€”**availability** or **FCCR**? (In this case, **availability** came closer to binding.)

### What to turn in (1 page)

*   6 small screenshots (one per task)
*   A bullet under each with the number(s) you observed and your **one-sentence** explanation

_Tip: If something doesnâ€™t reconcile, check the guardrails: revolver as the plug, prepay only when **ABL = 0** and **cash > min**, rebates receivable **excluded from BB** but **included in Î”NWC**._

* * *

Recommendation â€” invest or pass?
----------------------------------

So, do we invest in Industrial Inc. at 6.0x, or pass? **Our recommendation: a cautious invest.** The base case delivers a solid ~3.1Ã— MOIC / ~25+% IRR over five years, driven by achievable operational tweaks (better pricing, working capital cleanup) rather than heroic assumptions. The companyâ€™s cash generation is strong enough to deleverage steadily â€“ fixed charge cover stays above 2.0Ã— and ABL availability never fully maxes out in our projections.

Key risks revolve around liquidity and execution: a single large customer stretching payments could strain the revolver, and margin improvement requires discipline in pricing and routing.

We propose two mitigants: **(1) Lock in pricing durability** via multi-year contracts or surcharges so that gross margin gains (like that 300 bps from rebate and pricing initiatives) stick. **(2) Maintain ABL headroom** by aggressively managing receivables â€“ maybe offer early-pay discounts to customers or use credit insurance for big accounts. And **(3) invest in route optimization tech** to cement those cost savings in deliveries (higher route density translates to permanent margin lift). With these in place, the downside (liquidity crunch or margin squeeze) is manageable, and the upside â€“ a well-oiled distributor that could even sell for a premium â€“ is attractive.

In summary, this distribution LBO isnâ€™t a get-rich-quick story; itâ€™s a steady operational play. But by turning operational dials, we create a path to a respectable return. For hands-on investors who know how to squeeze cash from the balance sheet, Industrial Inc. is a buy.

Further Reading
---------------

*   **[LBO Modeling Traps: 5 That Can Kill Your IRR](https://uplevered.com/lbo-modeling-traps/#:~:text=Real,king%E2%80%94and%20working%20capital%20eats%20cash)
     â€“ UpLevered (2025)** â€“ Highlights common pitfalls like underestimating working capital needs (e.g., high-growth â€œcash trapsâ€? in distributors) and how to avoid them.
*   **[Maximizing Working Capital Performance for Distributors](https://distributionstrategy.com/wp-content/uploads/2022/08/DSG-Maximizing-Working-Capital-Performance-for-Distributors.pdf#:~:text=with%20sales,There%20have%20been)
     â€“ Distribution Strategy Group (2022)** â€“ Free report by Al Bates on how inventory and AR growth can strain distributor cash flow, and strategies to improve cash conversion.
*   **[Everything You Need to Know About Asset-Based Lending (ABL)](https://blog.popularbank.com/07-03-2025/asset-based-lending-abl/#:~:text=Within%20the%20lending%20agreement%2C%20the,other%20assets%20with%20liquid%20value)
     â€“ Popular Bank (2025)** â€“ Overview of ABL facilities, typical advance rates, and why companies (like distributors) use asset-based loans for working capital.
*   **[Mastering Rebate Accounting Challenges](https://www.phocassoftware.com/resources/blog/rebate-accounting#:~:text=Payable%20rebates%20are%20usually%20recognized,impact%20on%20the%20financial%20statement)
     â€“ Phocas Software (2024)** â€“ Discusses vendor rebate accounting, the impact on financials and working capital, and why timing matters â€“ relevant to modeling distributor EBITDA vs cash flow.
*   **[Delivery Route Density and Profitability](https://www.alexanderjarvis.com/what-is-delivery-density-in-ecommerce/#:~:text=,5%20miles%20of%20target)
     â€“ Alexander Jarvis (n.d.)** â€“ Explains how improving delivery route density can cut costs ~20% and increase margins, illustrating the operational lever in distribution logistics.

Related Technical Guides
------------------------

*   [How to Build an LBO Model — the step-by-step guide this case applies](https://uplevered.com/how-to-build-an-lbo-model/)
    
*   [Net Operating Working Capital — model ΔNWC correctly in a distribution business](https://uplevered.com/net-operating-working-capital/)
    
*   [Enterprise Value vs Equity Value — the EV bridge feeding entry valuation](https://uplevered.com/enterprise-value-vs-equity-value/)
    
*   [LBO Modeling Traps — common errors to watch for in this build](https://uplevered.com/lbo-modeling-traps/)
    
*   [Private Equity Value Levers — decompose what actually drives this deal’s return](https://uplevered.com/private-equity-value-levers/)
    
*   [Middle-Market Definition — the size band and deal dynamics behind this $150M case](https://uplevered.com/middle-market-definition/)
    
*   [Private Equity DPI — how dividend recaps accelerate cash-on-cash returns](https://uplevered.com/private-equity-dpi/)
    
*   [Browse All Technical Guides — full library of PE frameworks, models, and career resources](https://uplevered.com/content/)
    

Stay sharp. Subscribe to Deal Flow Bullet.
------------------------------------------

PE frameworks, deal analysis, and career intel for middle-market practitioners. Free, once every month or so.

Newsletter Canonical Auto

Subscribe

**TL;DR — Distribution LBO Case Study ($150M Middle-Market Deal)**

What you’ll build: A complete LBO model for a $150M TEV distribution company with $20M EBITDA.

**5 tasks, 60 minutes:**

1.  Entry valuation — TEV at 7.5×, EV bridge to equity value
2.  Sources & uses — senior debt, sub debt, sponsor equity, transaction fees
3.  Operating model — 3-year revenue build, margin assumptions, ΔNWC
4.  Debt schedule — mandatory amort, cash sweep, interest expense
5.  Returns — exit at Year 5, MOIC and IRR at base/upside/downside

What ‘done’ looks like: S&U balances, BS balances every period, FCF drives debt paydown, returns fall in a reasonable range (2.0–3.0× MOIC, 15–25% IRR for a MM deal).

*   March 2026 — Fixed indexing issues, added TL;DR, cross-links, update log
*   Model v1.0 — September 2025 — Original publication and Excel template

×

Before you go — Deal Flow Bullet drops every Friday.
----------------------------------------------------

Weekly PE frameworks and deal analysis for middle-market practitioners. Subscribe in 5 seconds.

Newsletter Canonical Auto

Subscribe
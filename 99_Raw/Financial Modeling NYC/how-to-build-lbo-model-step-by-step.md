# How to Build an LBO Model: Step-by-Step Tutorial for Finance Professionals - Financial Modeling New York

**Source:** https://www.financial-modeling.com/how-to-build-lbo-model-step-by-step

---

[Skip to content](https://www.financial-modeling.com/how-to-build-lbo-model-step-by-step#content "Skip to content")

How to Build an LBO Model: Step-by-Step Tutorial for Finance Professionals
==========================================================================

![](https://www.financial-modeling.com/wp-content/uploads/2026/02/LBBO-modeling.jpg)

The leveraged buyout model is one of the most tested, most feared, and most misunderstood tools in all of finance. Ask any analyst who has been through a [private equity](https://www.financial-modeling.com/glossar/private-equity/)
 interview process, and they will tell you the same thing: knowing how to build an [LBO model](https://www.financial-modeling.com/glossar/lbo-model/)
 from scratch — cleanly, quickly, and without guidance — is the single skill that separates candidates who get offers from those who do not.

This tutorial walks you through exactly how to build a professional LBO model in Excel, from the initial assumptions to the investor returns waterfall. No templates, no shortcuts. Just the model, built the right way.

What Is an LBO Model?
---------------------

A leveraged buyout model is a financial model used to evaluate the [acquisition](https://www.financial-modeling.com/glossar/acquisition/)
 of a company primarily financed with debt. The private [equity](https://www.financial-modeling.com/glossar/equity/)
 firm (the sponsor) contributes a relatively small amount of equity — typically 30 to 40 percent of the purchase price — and funds the rest with senior debt, subordinated notes, or other instruments. The model answers one central question: **can the sponsor generate an acceptable return (typically 20%+ IRR) given the purchase price, capital structure, and projected operating performance?**

Why Every Finance Professional Needs to Know LBO Modeling
---------------------------------------------------------

LBO models are no longer exclusive to private equity. You will encounter them in:

*   **[Investment banking](https://www.financial-modeling.com/glossar/investment-banking/)
    :** Sell-side M&A processes regularly include an LBO analysis as part of the buyer universe [valuation](https://www.financial-modeling.com/glossar/valuation/)
    
*   **Private equity:** Every deal evaluation begins here
*   **Corporate development:** Understanding what financial sponsors can pay informs strategic bidding
*   **Interviews:** Goldman Sachs, KKR, Blackstone, and virtually every bulge bracket and PE shop test this

The 6 Core Components of an LBO Model
-------------------------------------

Before you open Excel, understand the architecture. Every LBO model has six interconnected sections:

### 1\. Transaction Assumptions

This is your entry point. Define the purchase price (expressed as an EBITDA multiple), the financing structure (debt-to-equity split), and key terms for each debt tranche — [interest rate](https://www.financial-modeling.com/glossar/interest-rate/)
, [amortization](https://www.financial-modeling.com/glossar/amortization/)
 schedule, maturity. Get this section wrong and every downstream calculation is worthless.

### 2\. Sources and Uses of Funds

A simple but critical schedule that confirms how the deal is funded (sources: senior debt, mezzanine, sponsor equity) and where the money goes (uses: equity purchase price, transaction fees, refinancing of existing debt). Sources must equal uses — always.

### 3\. Operating Model (3-Statement Projection)

Project the [income statement](https://www.financial-modeling.com/glossar/income-statement/)
, [balance sheet](https://www.financial-modeling.com/glossar/balance-sheet/)
, and [cash flow statement](https://www.financial-modeling.com/glossar/cash-flow-statement/)
 for the holding period — typically five years. The key driver here is EBITDA growth. Keep your assumptions defensible: revenue growth linked to industry benchmarks, margin expansion tied to specific operational initiatives, not wishful thinking.

### 4\. Debt Schedule

This is where most junior analysts struggle. Build a debt schedule that tracks opening balance, cash sweep (mandatory and optional amortization), PIK interest (if applicable), and ending balance for every tranche. The cash flow available for debt repayment flows directly from your operating model — this is what creates the model’s circularity, which you must handle with a toggle or iterative calculation.

### 5\. Exit Assumptions

Define the exit year (typically year 3–5) and the exit multiple. Most LBO models use a multiple of EBITDA consistent with the entry — a conservative assumption. From this, derive the enterprise value at exit, subtract net debt, and arrive at the equity proceeds to the sponsor.

### 6\. Returns Analysis (IRR and MOIC)

Two metrics define LBO success: **[Internal Rate of Return (IRR)](https://www.financial-modeling.com/glossar/internal-rate-of-return/)
** and **Multiple on Invested Capital (MOIC)**. IRR measures the annualized return on equity invested. MOIC measures the total cash returned relative to equity invested. A 20%+ IRR with a 2.0x+ MOIC over five years is the traditional benchmark for a successful buyout.

Step-by-Step: Building the Model in Excel
-----------------------------------------

Here is the build sequence used in all training sessions at [Financial Modeling](https://www.financial-modeling.com/glossar/financial-modeling/)
 New York:

1.  **Set up your tab structure:** Assumptions | Sources & Uses | Income Statement | Balance Sheet | Cash Flow | Debt Schedule | Returns
2.  **Hard-code your transaction assumptions** in a clearly labeled input section (blue font convention)
3.  **Build Sources & Uses** — confirm it balances before moving on
4.  **Project the income statement** — revenue, COGS, [operating expenses](https://www.financial-modeling.com/glossar/operating-expenses/)
    , EBITDA, D&A, EBIT, interest expense (placeholder for now), taxes, net income
5.  **Link the cash flow statement** — start with net income, add back D&A, model [working capital](https://www.financial-modeling.com/glossar/working-capital/)
     changes, arrive at free cash flow available for debt repayment
6.  **Build the debt schedule** — link interest to ending balances (this creates the circular reference), use a circularity toggle
7.  **Close the balance sheet** — [retained earnings](https://www.financial-modeling.com/glossar/retained-earnings/)
     ties net income, debt balances tie to the debt schedule, cash is your plug
8.  **Build the returns waterfall** — exit enterprise value, minus net debt, equity proceeds to sponsor, calculate IRR and MOIC
9.  **Add a sensitivity table** — IRR across entry multiple vs. exit multiple, and entry multiple vs. revenue growth

The Most Common LBO Modeling Mistakes
-------------------------------------

*   **Forgetting the cash sweep:** In a real LBO, excess cash goes to repay debt. Models that omit optional debt paydown overstate [leverage](https://www.financial-modeling.com/glossar/leverage/)
     at exit and understate returns
*   **Ignoring fees:** Transaction fees (advisory, financing) and management fees meaningfully reduce equity returns and are frequently omitted in quick models
*   **Broken circularity:** Interest expense depends on the debt balance, which depends on cash available to repay, which depends on net income after interest — a true circular reference. If you do not handle this correctly, your model crashes or gives nonsense results
*   **Flat EBITDA margins:** PE firms acquire companies with a specific operational thesis. A model showing flat margins from year 1 to year 5 signals to interviewers that you do not understand the business case

Frequently Asked Questions
--------------------------

### How long does it take to build an LBO model from scratch in an interview?

Most PE interviews expect a basic LBO shell in 30–60 minutes. A full working model with a debt schedule and returns analysis in 2–3 hours. The only way to hit these benchmarks is deliberate practice with a timer.

### Do I need to know accounting to build an LBO model?

Yes. A solid understanding of how the three [financial statements](https://www.financial-modeling.com/glossar/financial-statements/)
 link together is a prerequisite. If your balance sheet does not balance, the interview ends there.

### What Excel functions are most important for LBO modeling?

XIRR (for IRR calculation), SUMIF, IF with circular reference toggles, and structured table referencing. INDEX/MATCH for dynamic lookups. Know these cold.

### Should I use a template for LBO practice?

Only after you have built one from scratch at least ten times. Templates teach you to fill boxes, not to think. Interviewers give you a blank spreadsheet and a set of assumptions — not a template.

Where to Go From Here
---------------------

The gap between understanding an LBO conceptually and building one cleanly under time pressure — on a blank spreadsheet, with an interviewer watching — is wider than most candidates expect. Reading articles helps. Building models under guided supervision with real-time feedback on structure, logic, and presentation is what actually moves the needle.

At Financial Modeling New York, our 1-on-1 LBO sessions walk you through the full build process, cover every mistake in real time, and replicate the exact pressure of a live interview. Most candidates go from a broken model to a clean, interview-ready build in two to three sessions.

**→ Schedule a session and build your first clean LBO model with an expert — contact us today.**

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

[](https://www.financial-modeling.com/how-to-build-lbo-model-step-by-step# "Scroll back to top")
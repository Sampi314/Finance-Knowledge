# Presenting a fresh perspective on assessing credit losses of CLO portfolios - Alter Domus

**Source:** https://alterdomus.com/insight/presenting-a-fresh-perspective-on-assessing-credit-losses-of-clo-portfolios

---

[Skip to content](https://alterdomus.com/insight/presenting-a-fresh-perspective-on-assessing-credit-losses-of-clo-portfolios/#content)

News

Presenting a fresh perspective on assessing credit losses of CLO portfolios
===========================================================================

* * *

Rudolph Bunja

Head of Portfolio Credit Risk

26 January 2023

![Data reflected in eyeglasses, symbolizing analysis and expertise in fund administration services.](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%202560%201440%22%3E%3C/svg%3E)

As structured finance market participants are aware, notes issued by collateralized loan obligations (CLOs) introduce varying credit exposures to the underlying corporate leverage loan portfolio based on the relevant notes’ cashflow priority. This therefore offers investors the opportunity to participate in this asset class based on their own risk and cash flow preferences.

An assessment of how the underlying risk is distributed across the notes is fundamental for investors and other market participants. Obviously where that risk comes to bare and CLO credit losses are incurred, there are challenges to estimate and allocating that loss. To explore this complex issue and to come to an understanding of the outcome of credit loss, we ask two fundamental questions:

Firstly, how is the total portfolio credit loss allocated across the CLO’s notes? And, secondly, what is the total loss of the underlying portfolio that is to be allocated to the CLO’s notes?

Based on our analysis, we find that:

*   The first loss equity tranche absorbs most of the estimated portfolio credit losses.
*   Estimating portfolio credit losses is as much an art as a science and is subject to significant judgment.
*   Excess interest and other structural deal features could materially reduce the estimated portfolio credit loss and the allocation of such losses across the CLO’s notes – translation: the answers to the questions above could vary substantially once excess interest and structural deal features are considered.

**A Simple Example to Demonstrate CLO Complexities**

In order to illustrate both the complexities of estimating portfolio credit losses and how the estimated loss distribution of an underlying pool of leveraged loans may be allocated across a CLO’s capital structure, we have created a simple example. To begin, we assume a static portfolio of loans that is well diversified, with certain homogeneous characteristics (e.g., credit quality, maturity, seniority) and has a total par amount equal to the amount of CLO notes issued. 

Furthermore, we assume the CLO has a simple capital structure with three classes of notes (Class A, B, and equity) paid in order of straight sequential seniority. For simplicity, we ignore interest payments and discounted cashflows. We assume no interest on the collateral, nor on the CLO’s tranches.

This assumption is an important building block to gain a good understanding of how losses are measured and allocated to the CLO’s tranches. These assumptions will ensure that the total credit loss of the portfolio will equal the aggregate credit losses allocated to the CLO’s tranches.

Relaxing these assumptions, which may be considered for possible future research, is relevant since excess interest is typically available to a CLO where the cash flow priority rules serve first to reduce the amount of portfolio credit loss that is allocated to the notes and secondly reorder the allocation of the remaining losses.

Thus, to a certain extent, our simplified CLO is a ‘worst case scenario’ for the notes. In our stylized example, the only credit enhancement for the CLO’s notes is through overcollateralization (OC) based on the par amount of the underlying loans, similar in structure to a [CLO overcollateralization test](https://alterdomus.com/insight/understanding-the-impact-of-excess-interest-on-clo-portfolios/)
. In this case, the total amount of principal that can be distributed across the tranches is equal to those received on the loans. By extension, the total credit losses of the underlying portfolio are equal to the credit losses that are allocated to the CLO’s tranches in our simplified case.

Equation #1: Losses Allocated to the CLO Tranches = Total Portfolio Credit Loss

Importantly, as you read on, we’ll introduce an extended equation that represents the true nature of CLOs by incorporating excess interest.

**How are Portfolio Credit Losses Allocated?**

Figure 1 displays a hypothetical portfolio loss distribution where the thresholds along the x-axis indicate the relevant notes’ amount of credit enhancement based on the capital structure. Each notes’ probability of loss and EL are indicated by the curve exceeding its amount of credit enhancement and the cumulative probability within each notes’ thresholds, respectively. The maximum amount of loss is equal to the total amount of notes. 

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20576%22%3E%3C/svg%3E)

As to be expected, the more senior the note, the lower the likelihood of loss which is indicated by the ‘tail’, whereas the equity absorbs most of the CLO portfolio’s EL as we see in Figure 1. In actuality, the equity absorbs over 95% of the total loss in this example. Note also that the ELs across the notes is equal to the EL of the underlying pool. So, here’s our first insight:

_Equity tranche absorbs the vast majority of portfolio losses_

**How are Portfolio Credit Losses Estimated?**

The weighted average probability of default (‘PD’) and loss given defaults, which are represented by the credit quality of the pool, define the mean of Figure 1, while the shape of Figure 1 is based on various diversification elements (e.g., issuer/sector exposure). Estimation of these variables is not an easy task.  
  
For example, what PD should be used to map to a credit quality of a borrower? Also, what duration should be assumed (e.g., stated maturity or expected life) as historical default rates indicate that default rates and credit losses increase with time horizons. This leads us to the second challenge in performing this analysis – namely, what is the assumed credit loss of the underlying CLO?

To a casual reader, the expected credit loss of the underlying portfolio may simply be the product of the average PD of the underlying collateral multiplied by the average loss rate. But let’s be a bit more precise by referencing historical credit loss observations\[1\].  
  
Table 1 below shows cumulative default rates for corporate debt over a 5-year, 6-year and 7-year horizon for select speculative grade ratings. We have highlighted the B1 row, as an example, assuming our stylized CLO consists of B1-rated corporate issuers.

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20576%22%3E%3C/svg%3E)

Using a 7-year weighted average life (‘WAL’) and a B1 rating the expected default rate is roughly 15.44%. Assuming an average recovery of 50%, this would translate into an expected loss rate of 7.72% (15.44% \* 50% loss rate). Note that recovery rates are also subject to change depending on market conditions. For simplicity, in this paper we assume that recovery rates are fixed at 50%.

Historically, a 50% recovery rate for a first lien senior secured loan is a conservative estimate – especially since in our stylized example we assume that the portfolio loans are rated one rating sub-category higher than the PD rating. However, the assumption of which WAL and which PD to use is not that simple.

_Why not use the actual WAL and actual WARF?_  
  
CLOs are subject to a WAL test. Practically speaking, CLO managers endeavor to actively manage the portfolio such that there is a cushion between the portfolio’s _actual_ WAL and the test level. Like the WAL test, CLOs typically have an average credit quality test (Weighted Average Rating Factor or ‘WARF’).

In this example, we can assume the test has been set to the B1 rating level. CLO managers will also endeavor to manage their portfolio to maintain a cushion between the _actual_ WARF and the test level. As a result, CLOs will typically be managed to have true PDs that are lower than those indicated by their test levels.

Further reducing the WAL of a CLO portfolio are underlying corporate loan prepayments – both scheduled and unscheduled. Prepayments would further reduce the WAL of the portfolio, which by extension reduces PD and credit losses.  

_Which combination of WARF, WAL, and WAS to use?_  
  
CLOs typically allow managers the flexibility to offset collateral quality test cushions. The WARF tests, for example, will often vary based on the Weighted Average Spread (‘WAS’) and other portfolio characteristics. These tradeoff opportunities are often documented in a dynamic matrix within the CLO.  
  
Excess spread is often a critical component of the CLO. These tradeoff options, illustrated in Table 2\[2\] below, give us some hints about the reduction in the EL of the portfolio after considering the effects of excess spread, or WAS.

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20683%22%3E%3C/svg%3E)

For example, assume a CLO with a given diversity of 50, the WARF could be as low as 2091 (with a WAS of 2.95%) and as high as 2904 (with a WAS of 3.95%). The difference translates into a one third reduction in the portfolio’s WARF and EL due to excess interest of 100bps – excess interest matters!

This example highlights the importance of excess spread in estimating ELs for the CLO’s notes. Excess interest reduces the amount of CLO portfolio losses that are allocated to the notes – a topic for possible future research. Which leaves us with the following further insights:

*   Estimating CLO portfolio principal credit losses is very difficult to assess and could change dynamically.
*   Excess interest reduces the total losses to the CLO’s tranches – i.e., total losses allocated to the tranches is less than the total portfolio  
    credit losses.

The last insight allows us to update Equation #1 with Equation #2 below, which is more accurate in estimating net portfolio losses that are to be absorbed by the CLO’s notes.

Equation #2: Losses Allocated to CLO Tranches = Total Portfolio Credit Losses – Excess Interest

**Items for considerations**

In contrast to the above stylized example where we demonstrated some of the fundamental challenges in measuring credit losses, CLOs are more complex. They include intricate cashflow waterfalls that segregate interest and principal collections, which incorporate key structural features (e.g., OC tests) within the cashflow waterfall that can have implications for the notes.

An assessment of these features, which is beyond the scope of this paper, would be part of a more comprehensive analysis of portfolio losses and allocation of those losses to CLO notes. We would expect that these features to reduce the CLO’s portfolio losses and to skew the allocation of the reduced losses to favor the more senior notes.

**In Conclusion**

Estimating credit losses for a CLO portfolio is not an easy task. Various assumptions need to be made, including the appropriate WAL and PD (or WARF). With simple and reasonable assumptions, we’ve shown that estimated portfolio loss rates could vary significantly. Allocation of losses across the tranches adds another layer of complexity though we showed that the equity tranche will bear the brunt of the portfolio losses – over 95% in our stylized CLO.

CLOs incorporate features that could further reduce the underlying portfolio losses and change the allocation of those losses. We described how excess interest reduces portfolio credit losses that are allocated to the tranches, and that structural features such as OC tests can reduce the amount of the loss that is allocated to the non-equity tranches. In summary, we conclude that:

*   The first loss equity tranche absorbs most of the estimated portfolio credit losses.
*   Estimating portfolio credit losses is as much an art as a science and is subject to significant judgment.
*   Excess interest and other structural deal features could materially reduce the estimated portfolio credit loss and the allocation of such losses across the CLO’s tranches.

* * *

\[1\]Default statistics are obtained from Moody’s latest Annual Default Study dated February 8, 2002 – [researchdocumentcontentpage.aspx (moodys.com)](https://www.moodys.com/researchdocumentcontentpage.aspx?docid=PBC_1316376)
  
\[2\] [See Morningstar CLO Commentary: Dynamic Matrix Provides Increased Transparency to CLO Market Participants, September 2017](https://www.moodys.com/researchdocumentcontentpage.aspx?docid=PBC_1316376)

*   [Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Falterdomus.com%2Finsight%2Fpresenting-a-fresh-perspective-on-assessing-credit-losses-of-clo-portfolios%2F&title=Presenting%20a%20fresh%20perspective%20on%20assessing%20credit%20losses%20of%20CLO%20portfolios)
    
*   [Email this Page](https://x.com/share?url=https%3A%2F%2Falterdomus.com%2Finsight%2Fpresenting-a-fresh-perspective-on-assessing-credit-losses-of-clo-portfolios%2F&text=Presenting%20a%20fresh%20perspective%20on%20assessing%20credit%20losses%20of%20CLO%20portfolios)
    
*   [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Falterdomus.com%2Finsight%2Fpresenting-a-fresh-perspective-on-assessing-credit-losses-of-clo-portfolios%2F&title=Presenting%20a%20fresh%20perspective%20on%20assessing%20credit%20losses%20of%20CLO%20portfolios)
    

Key contacts
------------

#### Rudolph Bunja

United States

Head of Portfolio Credit Risk

 [![Contact by email](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E)](https://alterdomus.com/cdn-cgi/l/email-protection#144661707b78647c3a56617a7e75547578607166707b7961673a777b79)[![Contact by phone](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E)](tel:13475238961)

Insights
--------

![Technology data on screen plus fountain pen and notepad](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20683%22%3E%3C/svg%3E)

AnalysisApril 9, 2026

#### Consistency at Scale: Private Equity’s Data Challenge

[Read article](https://alterdomus.com/insight/consistency-at-scale-private-equity-data/)

[](https://alterdomus.com/insight/consistency-at-scale-private-equity-data/)

![Location in New York](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20683%22%3E%3C/svg%3E)

AnalysisApril 7, 2026

#### The $12.9 Million Hidden Cost of Fragmented Data

[Read article](https://alterdomus.com/insight/the-12-9-million-hidden-cost-of-fragmented-data/)

[](https://alterdomus.com/insight/the-12-9-million-hidden-cost-of-fragmented-data/)

![Gherkin architecture](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201024%20683%22%3E%3C/svg%3E)

AnalysisApril 1, 2026

#### When Borders Become Background: Operating Across Jurisdictions

[Read article](https://alterdomus.com/insight/operating-across-jurisdictions-private-markets/)

[](https://alterdomus.com/insight/operating-across-jurisdictions-private-markets/)
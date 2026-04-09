# Private Equity Waterfall Models: European vs American Structures, Carry and Clawback

**Source:** https://www.financial-modeling.com/private-equity-waterfall-model-european-vs-american-carry-clawback

---

[Skip to content](https://www.financial-modeling.com/private-equity-waterfall-model-european-vs-american-carry-clawback#content "Skip to content")

Waterfall Modeling for Complex GP/LP Structures: European vs. American Distribution Methods
===========================================================================================

![A woman with an umbrella in front of a waterfall. Financial modeling, New York.](https://www.financial-modeling.com/wp-content/uploads/2025/11/Waterfall-Financial-Modeling-GL-LP-Structures.jpg)

Waterfall models are the financial engine that calculates how cash distributions from a [Private Equity](https://www.financial-modeling.com/glossar/private-equity/)
 (PE) fund’s investments are split between the **General Partner (GP)**—the fund manager—and the **Limited Partners (LPs)**—the investors. Understanding these distribution methods, particularly the differences between **European** and **American** waterfalls, is critical for accurately modeling the fund’s economics, including **Carried Interest (Carry)** and **Preferred Return hurdles**.

* * *

1\. The Components of the Waterfall
-----------------------------------

The goal of the waterfall is to ensure LPs recover their capital and achieve a minimum return before the GP earns any incentive fee (Carry).

### A. The Hurdle Rate (Preferred Return)

This is the minimum annual return (often $7\\%$ to $9\\%$ IRR) that the LPs must receive on their invested capital before the GP can participate in the profits.

### B. Carried Interest (Carry)

This is the GP’s share of the profits, typically $20\\%$ of all profits generated above the hurdle rate.

### C. Clawback Provision

This provision protects the LPs. If the GP receives carried interest distributions early in the fund’s life, but later investments perform poorly, the **Clawback** forces the GP to repay the excess Carry distributions back to the fund so that the LPs still achieve their agreed-upon minimum return across the **entire fund life**.

* * *

2\. The Core Difference: European vs. American Waterfalls
---------------------------------------------------------

The distinction between the two primary distribution methods lies in the scope against which the distributions are tested.

### A. American Waterfall (Deal-by-Deal Approach)

In an American Waterfall, the GP can begin taking carried interest **on a deal-by-deal basis**, as soon as a single successful investment is exited.

*   **Mechanism:** Cash flows from a single exited investment are distributed until the LPs receive their capital related to _that specific investment_ plus the preferred return on that capital. Once that hurdle is cleared for the deal, the GP takes their $20\\%$ Carry from the remaining profits of that deal.
*   **Advantage for GP:** The GP receives incentive fees earlier in the fund’s life, enhancing their internal [liquidity](https://www.financial-modeling.com/glossar/liquidity/)
    .
*   **Risk for LPs:** Since the GP takes Carry early, the risk of a future **Clawback** is significantly higher if later deals fail. The GP must set aside reserves or post a guarantee.

### B. European Waterfall (Whole-Fund Approach)

In a European Waterfall, the GP cannot receive any Carried Interest until the LPs have received back **all of their invested capital** across **all investments** in the fund, plus the preferred return on that cumulative capital.

*   **Mechanism:** Distributions from early exits flow entirely to the LPs until $100\\%$ of their total contributed capital is returned, plus the aggregate preferred return. Only after the **entire fund’s** capital and hurdle are cleared does the GP begin participating in the profits.
*   **Advantage for LPs:** Provides maximum capital protection and drastically reduces the probability of a Clawback, as the fund must be profitable on an aggregate basis before the GP profits.
*   **Modeling Implication:** Requires tracking the **cumulative distributions** against the **cumulative contributions** and the aggregate preferred return.

* * *

3\. Detailed Walkthrough: Carried Interest Calculation Tiers
------------------------------------------------------------

Regardless of the method (European or American), the actual cash distribution is typically structured sequentially across four tiers after an investment exit.

| **Tier** | **Name** | **Allocation Goal** | **Split** |
| --- | --- | --- | --- |
| **Tier 1** | **Return of Capital** | Return $100\\%$ of invested capital. | $100\\%$ to LPs |
| **Tier 2** | **Preferred Return** | Satisfy the LP hurdle rate (e.g., $8\\%$ IRR) on the capital in Tier 1. | $100\\%$ to LPs |
| **Tier 3** | **Catch-up** | Bring the GP’s cumulative share of profits (Carry) up to the full $20\\%$. | $100\\%$ to GP |
| **Tier 4** | **Profits Split** | Distribute the remaining cash. | $80\\%$ to LPs, $20\\%$ to GP |

### The Catch-up Tier (Tier 3)

This tier is necessary to ensure the GP receives $20\\%$ of the total profits _after_ the LPs receive their preferred return.

*   **The Logic:** Since the LPs received $100\\%$ of the profits in Tiers 1 and 2, the Catch-up tier directs all profits (typically until the GP’s $20\\%$ share is fully “caught up”) entirely to the GP.
*   **Calculation:** The total distribution required to the GP in the Catch-up tier is calculated to ensure that the GP’s cumulative take equals $20\\%$ of the total profits _since the fund’s inception_.

* * *

4\. Modeling the Complexity: Clawback Mechanics
-----------------------------------------------

The Clawback is the ultimate financial guarantee in the waterfall and must be modeled to reflect the worst-case scenario.

### A. Clawback Trigger

The Clawback is only executed at the **liquidation of the entire fund** (usually 10-12 years).

*   **The Test:** If at the fund’s liquidation, the GP’s cumulative Carried Interest received exceeds $20\\%$ of the fund’s _total net profits_ (after all capital and preferred returns are paid to LPs), the Clawback is triggered.

$$\\text{Clawback Amount} = \\text{GP Cumulative Carry Received} – (20\\% \\times \\text{LP Cumulative Profit})$$

### B. Modeling the Provision

In a comprehensive waterfall model, the analyst must track a running **Cumulative Clawback [Liability](https://www.financial-modeling.com/glossar/liability/)
** on the GP’s side.

*   **American Waterfall Focus:** The liability tracking is most critical here, as the GP begins taking cash much earlier. The model must reserve for the hypothetical possibility that the current Carry taken would need to be repaid if the remaining [portfolio](https://www.financial-modeling.com/glossar/portfolio/)
     performed poorly.
*   **Guarantees:** The GP typically provides a **Clawback Guarantee** backed by an escrow account or by the firm’s capital, ensuring that the LPs’ money is protected even if the fund manager has already spent the distributed Carry.

Mastering these distribution mechanics is essential for accurately pricing a PE fund and understanding the true alignment of incentives between the General Partner and the Limited Partners.  

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

[](https://www.financial-modeling.com/private-equity-waterfall-model-european-vs-american-carry-clawback# "Scroll back to top")
# Weighted Average Cost of Capital

**Source:** https://edbodmer.com/weighted-average-cost-of-capital

---

There are four parts to the discussion of WACC and cost of capital.  In the first section I discuss how the debt beta can be derived from bond ratings and how big conceptual and practical mistakes can be made by assuming that the debt beta is zero or close to zero.  In the second section I introduce a  cash flow proof of WACC where the enterprise value is split into components and the present value of separate cash flows at different discount rates reconciles with a WACC table.  The third section explains how the long and painful debate about how to address interest tax shields should be resolved through using net of tax debt in the capital structure and an interest rate that is not adjusted for taxes. The final section explains how, if you are going to use the traditional WACC formulas, you should make adjustments to correctly reflect the value of the tax shield.

> [Debt Beta from Credit Spreads Rather than Assuming Zero Debt Beta](https://edbodmer.com/debt-beta-and-credit-spreads/)

> [Proof of Using Ku or WACC without Interest Tax Shield](https://edbodmer.com/proof-of-using-debt-net-of-tax-in-capital-structure-and-pre-tax-interest-rate/)

> [Resolution of Tax Shield on Interest Expense in WACC](https://edbodmer.com/resolution-of-tax-shield-on-interest-expense-in-wacc/)

> [Adjustment to WACC from Correct Application of Tax Shields](https://edbodmer.com/application-of-wacc-in-dcf/)

### WACC, Tax Shields, Debt Beta, Target Capital Structure and Circularity

If you are like me, when you study how to apply the WACC in a DCF model you can be frustrated. When you read about applying the WACC in financial articles written by academics with dense equations and esoteric theory your confusion will without question increase. Some articles suggest that you must use APV and discounting tax shields at the all-equity cost of capital. Most write down a seemingly sophisticated formula for Be and Bu as a function of Bd and the tax rate. This lesson set addresses many of the issues including application of a target capital structure, un-levering and re-levering beta, resolving an apparent circularity problem and valuing the tax shields created by interest. The video below introduces some of the issues.

I have tried to demonstrate that these WACC issues are really not very difficult and do not require a whole bunch of seemingly complex formulas that seem to come from nowhere. Instead I use a couple of simple and hopefully clear-headed ideas along with simple excel models to prove the ideas. Rather than working through the technical formulas without much real explanation, the files and videos in this section demonstrate how to prove a few key concepts. The models are simple financial models. Construction of the models is demonstrated in videos. Key conclusions of the financial model proofs and the theory that I hope is explained in simple terms include:

**1\. Tax Shields from Interest Deductibility in WACC Can Be Resolved with Gross and Net Capital Structures.** The excessive discussion about how to value tax shields associated with debt is a colossal waste of time. When you recognize that the tax shield is equivalent to a reduction in the coupon rate on debt, the proof of how to treat the tax shield becomes clear. The market value of debt to the corporation is reduced to when the coupon rate falls and the equity value increases. For example if debt was 1,000 at with an interest rate of 10% and the coupon rate is reduced to 6%, the market value of debt decreases form 1,000 to 600. If the opportunity cost of debt for providers of funds is 10% both before and after the coupon rate decrease, the value of the debt declines to 60 of interest/10% or 600. This example is just the same as the tax effects of the interest shield at a 40% tax rate. Using the simple an basic principles that the fixed cost to the corporation is reduced from the tax shield and that the opportunity cost to providers of debt does not change from the corporate tax rate, the following equations quantify the tax shield. The second method is equivalent to the traditional WACC implementation.

Tax Shield Percent = Gross Observed Market Debt to Capital \* tNet Equity Percent = Gross Equity Observed/(1-Tax Shield Percent)  
Net Debt Percent = 1- Net Debt Percent  
Ku = Kd \* Net Debt Percent + Ke \* Net Equity PercentKe = \[Ku – Kd \* Net Debt Percent\]/Net Equity Percent  
Bu = Bd \* Net Debt Percent + Be \* Net Equity PercentBe = \[Bu – Bd \* Net Debt Percent\]/Net Equity Percent

**2\. Beta on Debt Should be Derived from Bond Yields**: The beta on debt is generally assumed away in considering the WACC. But the debt beta can be derived from the credit spread on debt given the EMRP and Rf. For example, the historic spread on BBB bonds is about 2% and the gearing of BBB companies is about 55%. This implies the beta on debt or Bd is given by the equation Cd = Rf + EMRP x Bd. Restating the equation implies that CSd = EMRP x Bd and Bd = CSd/EMRP. If the credit spread is 2% and the EMRP is 4%, the the Bd is .5. Data on the relationship between debt to capital and credit ratings can be used to derive the beta on debt as a function of the market capital structure

Total Interest Rate = Rf + Credit Spread  
Total Interest Rate = Rf + EMRP \* Debt Beta  
Credit Spread = EMRP \* Debt Beta  
Debt Beta = Credit Spread/EMRP  
Net Debt Percent = 1- Net Debt Percent  
**3\. Bd Should Vary with the Capital Structure in Computing Be and Bu.** Even though this is obvious, it is virtually never done in practice. S&P standards for the leverage and credit rating and published credit spreads can be used to establish Bd that varies with capital structure. When the varying credit spreads are applied, the effects on the relationship between Be and Ke and the capital structure are dramatic. The cost of equity at high leverage is dramatically reduced which reflects the call option premium that is inherent in the Ke and the put option cost that is part of the Kd.

Bu = Bd \* Net Debt Percent + Be \* Net Equity Percent, where Bd is a function of Gross Debt/Capital  
Be = \[Bu – Bd \* Net Debt Percent\]/Net Equity Percent, where Bd is a function of Gross Debt/Capital

**4\. Circularity in WACC and Valuation from Tax Shield can Easily be Avoided.** As the equity to capital ratio is computed using the market value of equity and, in turn, the market value of equity requires a value of WACC that is in turn driven in part by the equity to capital ratio. This implies a circular reference seems to exist. This is not much of a problem when the Bu and Ku is established from a comparison set of companies. The remaining circular reference from re-levering the beta can be easily resolved.

**5\. Target versus Actual Capital Structure Does Not Matter With No Interest Tax Shield.** If there is no tax shield, the WACC should not change if you use different capital structure assumptions because the cost of equity changes to compensate for risk created by gearing. This means that without taxes, use of a target capital structure in the context of DCF is not beneficial, necessary or relevant in terms of accuracy or theory. Without the interest tax shield, when the cost of equity is derived from re-levering the unlevered beta using the market value of debt at the valuation date, the result is exactly the same as if the company moves to a target capital structure.

**6\. APV does not add anything new to valuation.** Correct application of the WACC accounts for all items in the bridge between equity value and enterprise value in the WACC calculation. Investment bankers typically do this with using net debt rather than gross debt in computing WACC. Similar adjustments to the WACC should be made for associated investments not included in EBITDA, the fair value of derivatives, discounted operations and any other items.

Video Explanations for Lesson 4 – Application of WACC in the DCF
----------------------------------------------------------------

Video explanations include theory and some background APV does not add anything new to valuation. Correct application of the WACC accounts for all items in the bridge between equity value and enterprise value in the WACC calculation. Investment bankers typically do this with using net debt rather than gross debt in computing WACC. Similar adjustments to the WACC should be made for associated investments not included in EBITDA, the fair value of derivatives, discounted operations and any other items.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Cost of Capital Subject |     | File Reference |     | Video Link |
|     |     |     |     |     |
| Interest Tax Shield Part 1 with Introduction to Net of Tax Method |     | Interest Shield Exercise |     | [https://www.youtube.com/watch?v=G6BBvAFHJGo](https://www.youtube.com/watch?v=G6BBvAFHJGo) |
| Demonstrate that Net of Tax Method in Capital Structure Values Tax Shield |     | Interest Shield Exercise |     | [https://www.youtube.com/watch?v=9LKppeYudVU](https://www.youtube.com/watch?v=9LKppeYudVU) |
| How to Compute Ku with Net of Tax Method |     | Un-lever and Re-lever with Tax Shield |     | [https://www.youtube.com/watch?v=jaLOx3RJFkc](https://www.youtube.com/watch?v=jaLOx3RJFkc) |
| Overview of How Debt Beta Influences WACC |     | Theory of Debt Beta and WACC |     | [https://www.youtube.com/watch?v=n\_csEtMHveA](https://www.youtube.com/watch?v=n_csEtMHveA) |
| Demonstrates use of Interpolate Function |     | Mechanics of Debt Beta and WACC |     | [https://www.youtube.com/watch?v=Bvp0ruVYBSw](https://www.youtube.com/watch?v=Bvp0ruVYBSw) |
| How to Compute Ku with Net of Tax and Debt Beta |     | Unlever and Re-lever with Varying WACC |     | [https://www.youtube.com/watch?v=7ny67y-EpR8](https://www.youtube.com/watch?v=7ny67y-EpR8) |
| Demonstrates Valuation with WACC and Net of Tax Method |     | Growth Rate, Tax Shields and WACC |     | [https://www.youtube.com/watch?v=oKNmQ9fimZc](https://www.youtube.com/watch?v=oKNmQ9fimZc) |
| Shows Bias in WACC from Growth |     | Circularity, WACC and Ku |     | [https://www.youtube.com/watch?v=2EPd8\_yi\_0M](https://www.youtube.com/watch?v=2EPd8_yi_0M) |
| Shows how to Use Goal Seek to Resolve Bias |     | WACC Growth and Goal Seek |     | [https://www.youtube.com/watch?v=JEahjlc8QFs](https://www.youtube.com/watch?v=JEahjlc8QFs) |
| Demonstrates that Target Capital Structure is Irrelveant without Tax Shield |     | Target Capital Structure without Taxes |     |     |
| How to Resolve Target Capital Structure with Tax Shield |     | Target Capital Structure with Tax Shield |     | [https://www.youtube.com/watch?v=PkIsIOtAqy4](https://www.youtube.com/watch?v=PkIsIOtAqy4) |
| ……………………………………………………………………………………………………………………………. | …   | ……………………………………………………………. | …   | ………………………………………………………………………………………… |

Files and Assessment for Lesson 4 – Application of WACC in the DCF
------------------------------------------------------------------

The files associated with the videos demonstrate how to make appropriate adjustments to the DCF model. For this lesson I did not include exercises as part of the individual files. Instead, if you want credit for completing the lesson set, you should fix the Disney case study that is part of the case study page. Alternatively, you can go to the corporate model page and fix the DCF page in the various models. You should include a page where you find betas and correctly compute the all equity and debt betas using the net of tax capital structure. You should then compute the value of the company using the net of tax capital structure and subtract the net of tax debt. All you have to do then is to send me 40 Euro and you will get your name on the success page. If you have ever taken one of my courses in person, you do not have to pay the fee.

I you want the following files that work through WACC issues, send me an e-mail at edwardbodmer@gmail.com and ask for the resource library.  You can find the files in the WACC section.

Debt Beta.xlsm

Target Capital Structure.xlsm

Tax Effects of Interest in Valuation Exercise.xlsm

Valuation Circularity.xlsm

WACC and Growth working.xlsm

WACC and Growth with Goal Seek Macro.xlsm

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1309&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10004&rand=0.18458621218273563)
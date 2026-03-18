# Declining companies: Value drivers

**Source:** https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/decliningvaluedrivers.htm

---

 [![littlebook](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/Budimage/littlebook.gif)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook.htm)
 The Little Book of Valuation
===============================================================================================================================================================================================

Declining companies: Value Drivers
==================================

Going concern value
-------------------

To value a firm as a going concern, we consider only those scenarios where the firm survives. The expected cash flow is estimated only across these scenarios and thus should be higher than the expected cash flow estimated in the modified discounted cash flow model. When estimating discount rates, we make the assumption that debt ratios will, in fact, decrease over time, if the firm is over levered, and that the firm will derive tax benefits from debt as it turns the corner on profitability. This is consistent with the assumption that the firm will remain a going concern. Most discounted cash flow valuations that we observe in practice are going concern valuations, though they may not come with the tag attached.

            A less precise albeit easier alternative is to value the company as if it were a healthy company today. This would require estimating the cashflows that the firm would have generated if it were a healthy firm, a task most easily accomplished by replacing the firm’s operating margin by the average operating margin of healthy firms in the business. The cost of capital for the distressed firm can be set to the average cost of capital for the industry and the value of the firm can be computed. The danger with this approach is that it will overstate firm value by assuming that the return to financial health is both painless and imminent.

Likelihood of Distress
----------------------

A key input to this approach is the estimate of the cumulative probability of distress over the valuation period. In this section, we will consider three ways in which we can estimate this probability. The first is a statistical approach, where we relate the probability of distress to a firm’s observable characteristics – firm size, leverage and profitability, for instance – by contrasting firms that have gone bankrupt in prior years with firms that did not. The second is a less data intensive approach, where we use the bond rating for a firm, and the empirical default rates of firms in that rating class to estimate the probability of distress. The third is to use the prices of corporate bonds issued by the firm to back out the probability of distress.

a. Statistical Approaches: The fact that hundreds of firms go bankrupt every year provides us with a rich database that can be examined to evaluate both why bankruptcy occurs and how to predict the likelihood of future bankruptcy. One of the earliest studies that used this approach was by Altman (1968), where he used linear discriminant analysis to arrive at a measure that he called the Z score. In this first paper, that he has since updated several times, the Z score was a function of five ratios:

Z = 0.012 (Working capital/ Total Assets) + 0.014 (Retained Earnings/ Total Assets) + 0.033 (EBIT/ Total Assets) + 0.006 (Market value of equity/ Book value of total liabilities) + 0.999 (Sales/ Total Assets)

Altman argued that we could compute the Z scores for firms and use them to forecast which firms would go bankrupt, and he provided evidence to back up his claim. Since his study, both academics and practitioners have developed their own versions of these credit scores.  Notwithstanding its usefulness in predicting bankruptcy, linear discriminant analysis does not provide a probability of bankruptcy.

b. Based upon Bond Rating: Many firms, especially in the United States, have bonds that are rated for default risk by the ratings agencies. These bond ratings not only convey information about default risk (or at least the ratings agency’s perception of default risk) but they come with a rich history. Since bonds have been rated for decades, we can look at the default experience of bonds in each ratings class. Assuming that the ratings agencies have not significantly altered their ratings standards, we can use these default probabilities as inputs into discounted cash flow valuation models. What are the limitations of this approach? The first is that we are delegating the responsibility of estimating default probabilities to the ratings agencies and we assume that they do it well. The second is that we are assuming that the ratings standards do not shift over time. The third is that table measures the likelihood of default on a bond, but it does not indicate whether the defaulting firm goes out of business. Many firms continue to operate as going concerns after default. 

c. Based upon Bond Price: The conventional approach to valuing bonds discounts promised cash flows back at a cost of debt that incorporates a default spread to come up with a price. Consider an alternative approach. We could discount the expected cash flows on the bond, which would be lower than the promised cash flows because of the possibility of default, at the riskfree rate to price the bond. If we assume that a constant annual probability of default, we can write the bond price as follows for a bond with fixed coupon maturing in N years.

Bond Price = ![](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/decliningvaluedrivers_files/image002.png)

This equation can now be used, in conjunction with the price on a traded corporate bond to back out the probability of default. We are solving for an annualized probability of default over the life of the bond, and ignoring the reality that the annualized probability of default will be higher in the earlier years and decline in the later years. While this approach has the attraction of being a simple one, we would hasten to add the following caveats in using it. First, note that we not only need to find a straight bond issued by the company – special features such as convertibility will render the approach unusable – but the bond price has to be available. If the corporate bond issue is privately placed, this will not be feasible. Second, the probabilities that are estimated may be different for different bonds issued by the same firm. Some of these differences can be traced to the assumption we have made that the annual probability of default remains constant and others can be traced to the mispricing of bonds. Third, as with the previous approach, failure to make debt payments does not always result in the cessation of operations. Finally, we are assuming that the coupon is either fully paid or not at all; if there is a partial payment of either the coupon or the face value in default, we will over estimate the probabilities of default using this approach.

Consequences of Distress
------------------------

Once we have estimated the probability that the firm will be unable to make its debt payments and cease to exist, we have to consider the logical follow-up question. What happens then? As noted earlier in the chapter, it is not distress per se that is the problem but the fact that firms in distress have to sell their assets for less than the present value of the expected future cash flows from existing assets and expected future investments. Often, they may be unable to claim even the present value of the cash flows generated even by existing investments. Consequently, a key input that we need to estimate is the expected proceeds in the event of a distress sale. We have three choices:

1.    Estimate the present value of the expected cash flows in a discounted cash flow model, and assume that the distress sale will generate only a percentage (less than 100%) of this value. Thus, if the discounted cash flow valuation yields $ 5 billion as the value of the assets, we may assume that the value will only be $ 3 billion in the event of a distress sale.

2.    Estimate the present value of expected cash flows only from existing investments as the distress sale value. Essentially, we are assuming that a buyer will not pay for future investments in a distress sale. In practical terms, we would estimate the distress sale value by considering the cash flows from assets in place as a perpetuity (with no growth).

3.    The most practical way of estimating distress sale proceeds is to consider the distress sale proceeds as a percent of book value of assets, based upon the experience of other distressed firms.

Note that many of the issues that come up when estimating distress sale proceeds – the need to sell at below fair value, the urgency of the need to sell – are issues that are relevant when estimating liquidation value.
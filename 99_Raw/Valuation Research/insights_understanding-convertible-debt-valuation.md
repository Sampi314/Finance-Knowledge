# ​Understanding Convertible Debt Valuation | Valuation Research

**Source:** https://www.valuationresearch.com/insights/understanding-convertible-debt-valuation

---

[](https://twitter.com/home?status=Understanding%20Convertible%20Debt%20Valuation%3A%20https://www.valuationresearch.com/insights/understanding-convertible-debt-valuation/)
[](mailto:?subject=Understanding%20Convertible%20Debt%20Valuation&body=I%20thought%20you%20might%20find%20this%20article%20interesting:%20https://www.valuationresearch.com/insights/understanding-convertible-debt-valuation/)
[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.valuationresearch.com/insights/understanding-convertible-debt-valuation/&title=Understanding%20Convertible%20Debt%20Valuation&source=Valuation%20Research)

_Estimated reading time: 7 minutes_

Convertible notes (or convertible bonds) are hybrid securities with debt-like and equity-like features. The convertible noteholders receive the stated coupon and principal and the option to convert the notes into shares of stock. Like a straight debt security, a convertible note has a notional (or principal) amount, coupon payments, and a stated maturity. Unlike a straight debt security, a convertible note allows the holder to exchange or convert the bond for a specified or predetermined number of shares of the company’s stock.

The conversion price is the price at which the convertible note can be converted into the company’s shares. The conversion price is usually higher than the stock price as of the issuance date. The conversion ratio is estimated as the number of shares the convertible note is convertible into. The formula below demonstrates the relationship between the conversion ratio and the conversion price:

CR = N/CP where,  
CR is the conversion ratio.  
N is the notional or principal amount.  
CP is the conversion price.

Convertible notes have characteristics that make them attractive to both issuers and investors (or holders). Investors find them attractive because of the potential equity upside, and the downside protection provided by coupon and principal payments. In addition, convertible notes are alternatives to straight debt securities at a time of generally low interest rates, which can potentially provide extra profit for investors through the conversion feature.

From the issuers’ perspective, convertible notes are appealing since they allow for a lower coupon than a straight debt security due to the conversion feature provided to the holders. In addition, a significant increase in a convertible note’s value is often due to the increase in the stock price. In such a case, while the issuer’s liability has increased, the issuer is already benefiting from the increase in the stock price. In other words, the convertible notes help the issuers match their assets and liabilities more effectively.

Convertible notes are often issued by medium-sized public and growing companies since they effectively raise capital. While private companies sometimes issue convertible debt securities, convertible notes with more standardized features are generally issued by public companies.

A convertible note may have additional contractual features such as call-ability and put-ability. Call-ability is the ability of the issuer to call a convertible bond at a predetermined price, which could be a function of principal and accrued interest. Put-ability is the holder’s right to redeem the convertible note at a predetermined price, which could also be based on the principal and accrued interest.

There could be various conversion features for a convertible note, such as holding periods, market conditions (e.g., stock price threshold), and downward protection resets (e.g., dividend protection features that decrease the conversion price upon certain dividend payments). The conversion option is usually unavailable immediately after the issuance, and the holders are generally restricted for certain holding periods after the issuance. In addition, certain market conditions like stock price thresholds could exist over specific timeframes. For instance, the conversion may only occur in the quarter subsequent to the one during which a certain price threshold is met. Alternatively, the conversion could only be permitted when a price threshold is met over a certain period, say 20 out of 30 consecutive days.

### Valuation Models for Convertible Notes

In general, the convertible note models may be classified based on their approach to the two factors below:

*   Underlier (or underlier input)
    *   Some valuation models, such as Ingersoll’s, use the aggregate fair value of the company’s invested capital as the underlier input.
    *   Most valuation frameworks, however, consider the common stock price (or the equity value) as the underlier.
*   The stochastic process for the underlier. There are two broad categories applicable to the stochastic processes used in convertible note models:
    *   Geometric Brownian Motion (GBM) Process (or other Wiener processes)
    *   Jump Diffusion Process

In practice, the valuation frameworks for convertible bonds mostly use the GBM stochastic process on the stock price as the underlier. The GBM is the underlying stochastic process used in modeling the stock price in the Black-Scholes model. On the other hand, the Jump Diffusion Process is a stochastic process that accounts for the probability of an upward or downward shock in the stock price and is less frequently used to model convertible notes.

In the absence of dividends and borrowing costs, it is never economically optimal to exercise a call option before the expiration date. Similarly, it can be demonstrated that it is not optimal to convert a convertible note before its maturity in the absence of dividends and borrow costs. Therefore, in the absence of dividends and borrow costs, a convertible note can be considered a combination of a straight debt and a call option.

If holding to maturity is not necessarily optimal, the convertible note is no longer a simple bundle of straight debt and call options. In such cases, the decision-making on the part of the holder would incorporate the options available to the issuer, and vice versa. For example, if the debt is callable by the issuer or putable by the holder, an early exit could be optimal. Similarly, in the presence of dividends and borrow costs, holding on to the convertible debt may lead to a decrease in the value of the stock, thereby decreasing the conversion value. In these cases, more complicated models such as risk-neutral lattice models, need to be implemented.

Lattice models are usually approximations of the GBM process, which incorporate an optimal decision-making framework by backward induction. The fair value at each node of the lattice is either the discounted value of the payoff from subsequent nodes for a hold strategy or the immediate payoff from conversion, callability, or putability. The payoff from the conversion is discounted at the risk-free rate while the payoffs that are a function of the principal and accrued interest are discounted with the straight debt rate. This approach was formalized by Tsiveriotis and Fernandez.

To further clarify, let’s consider a general case for a convertible note with dividends, callability and putability features. For each node of the lattice tree at maturity, the holder will either convert the notes or opt to receive the principal and coupon. For each previous node, the issuer will either call the note, as long as the prepayment amount is less than the present value of future payoffs or do nothing. If the note is called by the issuer, the holder will select the optimal choice among taking the prepayment, putting the note, or converting the note. If the issuer does not call the note, on the other hand, the holder will select the optimal choice among holding on to the note, putting the note, or converting the note. This process is applied to the entire nodes of the lattice tree until the fair value of the note is estimated at node 0, which is the valuation date.

### Main Inputs to the Convertible Debt Model

*   **Stock Price:** This is the issuer’s stock price as of the valuation date.
*   **Conversion Price:** This is a contractual price. While one may convert at any time, one would generally not convert before reaching the conversion price since it will be a sub-optimal conversion.
*   **Maturity:** This is the contractual date at which the convertible note matures.
*   **Market condition for conversion or callability (if any):** In some cases, a certain price, which is usually defined at a premium to the conversion price, has to be satisfied before the holder may convert the note. This condition may be implemented as a single threshold price which is estimated through a Monte Carlo simulation model.
*   **Dividend Yield:** This is the issuer’s dividend yield as of the valuation date.
*   **Borrow Cost:** This is the cost to short the issuer’s stock. This input is economically similar to the dividend yield input and is mostly relevant for stocks with relatively large short positions. The overnight borrowing rate can be obtained from financial data providers like SunGard. Alternatively, one may use the put-call parity to derive the term structure of the borrowing cost. This method, however, is based upon the availability of certain data such as near-the-money call and put options with sufficient trading volume and small bid-ask spreads across different expiration dates. If there is a need for separating the dividends and borrow costs, a reliable dividends forecast needs to be available as well.
*   **Volatility:** This input is usually estimated based on the historical and/or implied volatility measures of the issuer’s stock price. In addition, a discount is applied to the estimated historical/implied volatility to capture the effect of volatility skew.
*   **Straight Debt Yield:** This input is used to discount the principal and the coupons of the convertible note.

### Valuation Requirements for Convertible Notes

The issuer of the convertible note may be required to bifurcate the fair value of the convertible bond into (1) the fair value of the straight debt (liability portion) and (2) the fair value of the conversion feature (equity portion) as part of ASC 820 requirements. In some cases, companies are required to perform this bifurcation exercise for all subsequent reporting periods as well.

The straight debt yield input into the convertible debt valuation model, like the lattice model above, is solved so that the aggregate fair value of the convertible note is equal to the proceeds as of the issuance date. This estimated straight debt yield would further be corroborated by estimating a range of straight debt yields based on traded, non-convertible, and otherwise comparable debt securities. Comparable debt securities are ideally debt securities in the same geographical location, similar industry and credit ratings, and issued by companies with comparable invested capital.

After the straight debt yield is estimated, the straight debt portion will be valued using an income approach whereby the coupons and principal are discounted based on the straight debt yield. The conversion value will be estimated according to the “with and without” method by subtracting the straight debt fair value from the aggregate fair value of the convertible note.

If the bifurcation exercise is performed as of a subsequent valuation date, a similar framework will be used with the exception that the aggregate fair value of the convertible debt is equal to the traded value of the bond. The traded value could be retrieved from financial data sources such as Bloomberg. If the convertible bond is not traded on an exchange, the straight debt yield as of the valuation date will be estimated as a function of (1) the movements in the yield market from issuance date to the valuation date, (2) the changes in the credit quality of the issuer from the issuance date to the valuation date, and (3) the straight debt yield as of the issuance date.

For more information regarding convertible debt valuations and other valuation services for [complex securities](https://www.valuationresearch.com/services/alternative-asset-valuations/complex-securities/)
, we welcome you to contact article author, [Amir Alerasoul](https://www.valuationresearch.com/professionals/amir-alerasoul/)
, or a [VRC Professional.](https://www.valuationresearch.com/professionals/)

* * *

### Contributors

[![Amir Alerasoul](https://www.valuationresearch.com/wp-content/uploads/2022/08/AmirAlerasoul269x269.jpg)\
\
### Amir Alerasoul\
\
Managing Director\
\
![](https://www.valuationresearch.com/wp-content/themes/FoundationPress-master/src/assets/images/vrc_icon_i_40.png)](https://www.valuationresearch.com/professionals/amir-alerasoul/)

### Related Posts

 

[Charitable Gift Valuations Before Business Sale](https://www.valuationresearch.com/insights/charitable-gift-valuations-before-business-sale/)

[Three Approaches to Valuing a Privately-Held Company](https://www.valuationresearch.com/insights/three-approaches-valuing-privately-held-company/)

[The Evolution of Private Credit Markets in the U.S. and Europe](https://www.valuationresearch.com/insights/the-evolution-of-private-credit-markets-in-the-us-and-europe/)

[VRC's John Czapla and Parag Patel Featured in Private Funds CFO](https://www.valuationresearch.com/insights/evergreen-fund-valuations-private-funds-cfo/)

[Retail Access and Private Markets: Valuation Considerations from the SEC Roundtable](https://www.valuationresearch.com/insights/private-markets-retail-access-valuation-governance-sec-roundtable/)

[Building Scalable Private Funds: Strategic Insights on 3(c)(1) and 3(c)(7) Exemptions](https://www.valuationresearch.com/insights/building-scalable-private-funds-strategic-insights-3c1-and-3c7-exemptions/)

[VRC’s Parmeswaran Published in Private Funds CFO](https://www.valuationresearch.com/insights/vrcs-parmeswaran-published-in-private-funds-cfo/)

[The Shift to Daily Valuations: Trends, Drivers, and Best Practices](https://www.valuationresearch.com/insights/shift-to-daily-valuations-trends-drivers-and-best-practices/)

[Evolving Earnouts: Shorter Horizons, Higher Hurdles, and Rising Complexity](https://www.valuationresearch.com/insights/evolving-earnouts-shorter-horizons-higher-hurdles-rising-complexity/)

[AICPA Releases Comprehensive Stock Compensation Guide Draft](https://www.valuationresearch.com/insights/aicpa-releases-comprehensive-stock-compensation-guide-draft/)

[Heckerling 2026: Key Estate and Gift Valuation Insights](https://www.valuationresearch.com/insights/heckerling-2026-key-estate-and-gift-valuation-insights/)

[Sapnas, Smith Published in Business Valuation Resources](https://www.valuationresearch.com/insights/bvr-asa-conference-highlights-2026/)
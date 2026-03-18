# Debt Characteristics - Examples, Templates

**Source:** https://macabacus.com/operating-model/debt-characteristics

---

Debt Characteristics
====================

The first step in building our debt schedule is to enter assumptions related to the characteristics of any debt and preferred stock financing. These assumptions include interest rates, conversion prices for convertible securities, and scheduled amortization for debt requiring periodic repayment of principal.

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

Debt Maturities
---------------

Revolving credit facilities have no required amortization over the term of the facility, and preferred stock has no specified maturity date or mandatory periodic repayment, so we have excluded these instruments from the required repayment schedule. Expressing debt amortization as percentages of original face value in this schedule, rather than specifying a maturity year for each instrument, affords greater flexibility. For example, the former approach better accommodates debt that has 5% scheduled amortization for four years, followed by a bullet repayment of 80% in the fifth year.

Interest Rates
--------------

Floating interest rates are more common for senior debt than subordinated debt and preferred stock. In our model, we assume that the revolving and senior credit facilities have floating rates expressed as spreads to LIBOR, and that subordinated debt instruments and preferred stock pay fixed interest. Our interest rate assumptions are illustrative, and may not reflect current market conditions.

Circuit Breaker / Average Interest
----------------------------------

Interest is normally computed on average balances. As we continue to build our debt schedule, the model will become circular because interest expense and preferred dividends reduce net income, which reduces cash flow available for debt repayment, which affects period-end debt balances, which affects average debt balances, which affects interest expense, and so on. Circularity may prevent the model from recovering from an anomaly, resulting in #VALUE! and/or other Excel errors. We can eliminate circularity, and thereby allow the model to correct itself, by toggling off average interest with a “circuit breaker.” With average interest turned off, interest expense and income are computed using beginning-of-period balances. After the model is restored and errors are corrected, you can switch the circuit breaker back to the average interest. We will link our circuit breaker to the rest of the model in  
[Step 9](https://macabacus.com/operating-model/interest-expense-preferred-dividends)
.

Cash Sweep
----------

If the borrower has excess cash and the terms of the debt provide for early repayment at the borrower’s option, the borrower may use excess cash to periodically repay debt ahead of schedule. This is called “cash sweep.” A revolving credit facility always provides for early repayment, while bonds and preferred stock do not. Other debt instruments may or may not provide for unlimited cash sweep, and some may provide for limited cash sweep (e.g. only up to 50% of the outstanding balance may be repaid early). We have set up our cash sweep assumptions as percentages, rather than binary Yes/No inputs, to support limited cash sweep, but you would only enter 100% or 0% here—effectively, binary inputs—unless you knew that the debt terms provided for limited cash sweep.

Discover more topics
--------------------

[Webinar: The AI Edge in Investment Banking](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

Join experts from Macabacus & LSEG to learn practical insights about AI’s influence on the future of banking.

[Read more](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

[DCF Excel Template](https://macabacus.com/excel/templates/discounted-cash-flow)

Elevate your investment analysis with our free DCF model template. Understand discounted cash flow principles and perform accurate valuations in Excel.

[Read more](https://macabacus.com/excel/templates/discounted-cash-flow)

[Operating Model Excel Template](https://macabacus.com/excel/templates/operating-model)

Download our free operating model Excel template. Forecast revenue, expenses, and key financial metrics for better decision-making.

[Read more](https://macabacus.com/excel/templates/operating-model)

[LBO Excel Model](https://macabacus.com/excel/templates/lbo-model-short)

Try LBO modeling with our comprehensive Excel template. Understand key concepts, calculate returns, and gain actionable insights.

[Read more](https://macabacus.com/excel/templates/lbo-model-short)
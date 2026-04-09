# Interest Rates in Different Currencies and Inflation Rates

**Source:** https://edbodmer.com/interest-rates-in-different-currencies-and-inflation-rates

---

This page presents an analysis of borrowing money in different currencies where the inflation rate is very different in local currency then in an international currency such as USD.  For example, if the inflation rate is 16% in Nira and is 1.5% in USD, how does an interest rate of 23% in Nira compare with an interest rate of 7% in USD.

In particular if the credit spread above the base rate in USD is 4%, this would be equivalent to a much higher credit spread in local currency in the example above because the credit spread as well as the base rate should be adjusted for inflation. Of course if the cash flows or the revenues are in USD, it would be dangerous to borrow in local currency because of currency risk.

To demonstrate how to perform the analysis, the excel file below works through an example with two currencies.  In the example as with other cases where there is more than one currency in terms of costs, it is best to start with a PPP exchange rate and present all of the cash flows in two currencies.

**[Excel File with Case Study of Corporate Analysis Including Multiple Debt Issues and Currency Adjustments](https://edbodmer.com/wp-content/uploads/2021/05/Financial-Model-Bio-Foods-17042021v2.xlsx)
**

[Excel File that Addresses Advanced Issues Including Alternative Currencies and Translation Adjustments in Models](https://edbodmer.com/wp-content/uploads/2021/05/Advanced-Course.xlsm)

Step 1: Working with Forward Exchange Rates and Computing Implied Interest Rates
--------------------------------------------------------------------------------

When working with multiple currencies, you can first put the currencies at the top of the sheet and evaluate the implied inflation rates. In the example below, we have gathered the forward exchange rate and then used the INTERPOLATE function. Note that the cash flow is stated in USD and the debt service is also in USD. But we assume that the loan is in EUR. In rows 17 to 19 we assume that the interest rate in EUR is 1.5% which you can use to compute the implied interest rate in USD. To do this you can:

1.  Compute the change in the exchange rate
2.  Add 1 to the EUR interest rate
3.  The implied interest rate is the USD Exchange Rate divided by the 1+EUR index
4.  Compute the PV of debt Service in USD
5.  Compute the debt service in EUR
6.  Convert the initial loan into EUR — from the 634 to 530
7.  Check the IRR in EUR — It should be the interest rate

![](https://edbodmer.com/wp-content/uploads/2021/04/image-77.png)

Put the translation adjustment in USD. You can use the following steps:

1.  Take the model currency and divide it by the currency of the debt
2.  Compute the change in the ratio
3.  Multiply the change by the opening balance stated in the local currency for the model and do not put it in the debt schedule for the currency.

Note that when you do this the closing balance of the loan in EUR — the currency of the loan — and in USD — the currency of the model — are both zero.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-79.png)

Here, I am illustrating my method for evaluating a formula. You need to have the GENERIC MACROS file open and then you can press ALT, u.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-78.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2043&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9704&rand=0.6806335577328286)
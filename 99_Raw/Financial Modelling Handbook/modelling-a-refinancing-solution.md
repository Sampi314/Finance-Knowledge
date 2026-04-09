# Modelling a refinancing - solution

**Source:** https://www.financialmodellinghandbook.org/modelling-a-refinancing-solution

---

Once we’ve adjusted the senior debt calculations to facilitate early repayment, building the rest of the refinancing logic involves copying existing calculations we created for senior debt.

We’ll need the following elements:

*   Refinancing facility sizing/drawdown
*   Senior debt repayment
*   Refinancing facility interest
*   Refinancing facility repayment
*   Refinancing facility ratios

For each of these, I have simply copied the logic from the senior debt calculations. However, the key difference for the refinancing is including the “Refinancing active” switch. This allows us to activate and de-activate the refinancing easily.

We’ll also need to wire up the new line items onto the financial statements and deal with any other issues that come up.  

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/1-3.jpg)

Each of the calculation blocks for refinancing drawdown, interest and repayment has been updated to include the switch.

I’ve done the same for the refinancing facility ratios. If the facility is not active, we don’t want to report and refi facility ratios.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/2-3.jpg)

Don’t forget the add the new ratios to the output sheet.

Don’t forget the tax impact.
----------------------------

Remember that our tax calculation takes into account the maximum interest deduction. We, therefore, need to include the refinancing interest in the calculation.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/3-3.jpg)

What impact does our refinancing have on IRR?
---------------------------------------------

Our hypothesis was that even a 10-year refi facility would improve shareholder returns, even if the debt sizing DSCR and interest remain the same as the original senior facility.

Looking at the output sheet, we can see that the refi has boosted IRR by around 4%.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/4-3.jpg)

We can see why this is from the cash flow statement.

By the time we reach the end of the second operating year, $66.3m of senior debt is outstanding. Sizing the refinancing facility at a 1.30 DSCR for an additional ten-year period, we can draw $76.7m of refi facility. This creates a $10m surplus at the refinancing date.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/5-4.jpg)

In the next chapter, we’ll go on to test our other hypotheses. We should see higher IRRs if we increase the repayment period of refinancing, reduce the interest cost or reduce the debt sizing DSCRs.

The solution for this bonus chapter is available in the file pack you'll receive when you [purchase the handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
. See file _4.58 FMH refi END 01a._  

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero-8.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

Comments
--------

Sign in or become a Financial Modelling Handbook member to join the conversation.  
Just enter your email below to get a log in link.

 Send a log in link Great! Please check your inbox (or spam folder) for a log in link. Something didn't work. Please try again.

Sorry, comments couldn't be loaded. It looks like this account is not currently active.

### Subscribe to Financial Modelling Handbook

Don’t miss out on the latest financial modelling guides. Sign up now to get access to the library of members-only guides.

[jamie@example.com\
\
Subscribe](https://www.financialmodellinghandbook.org/modelling-a-refinancing-solution#/portal/signup)
# Modelling a refinancing - model set up

**Source:** https://www.financialmodellinghandbook.org/modelling-a-refinancing-model-set-up

---

The first stage in setting up our model to handle a refinancing is to address the fact that we will not service the existing senior debt facility after the refinancing date.

We therefore need:

*   A revised repayment period flag
*   Revised interest and principal repayment calculations that de-activate after the refinancing date
*   An additional line item on our cashflow statement to show the repayment of the senior debt on the refinancing date.
*   A new corkscrew for the refinancing facility balance
*   Adjusted cover ratios calculations to take account of the shorter repayment period

The start file for this bonus chapter is available in the file pack you'll receive when you [purchase the handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
. See file _4.57 FMH refi BEG 01a._

Start with when - creating the flags we need.
---------------------------------------------

Getting our thinking straight about timing is a useful start in any modelling task. To support the refinancing calculations, we need three new flags:

*   A flag to tell us when the refinancing is happening
*   A revised senior debt repayment period flag that takes account of the refinancing happening and which shorts the senior debt repayment period
*   A refinancing facility repayment period flag based on our input of the repayment period.

These are all types of flags we have created before; therefore, copying existing calculations and changing the ingredients and labels should be easy and quick by now.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/1-1.jpg)

The timesheet, updated to include our three new flags.

Cutting short senior debt service if the refinancing is active
--------------------------------------------------------------

We want a single switch in the model to activate or de-active the refinancing facility. As a test, once we’ve completed building the refinancing calculations, we will deactivate the refi, and our outputs should align precisely with where we were before we started the refi modelling.

If the refinancing is active, we will no longer make debt service payments on the senior debt. We, therefore, need to change the senior debt repayment period flag to achieve this. I’ve included a block which changes the repayment flag if the refinancing is active.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/2-2.jpg)

I’m switching this flag out with the original senior debt repayment period flag. That way, if the refi is active, we will only make the original senior debt interest and principal payments in the periods before the refinancing.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/3-2.jpg)

Placeholder for senior debt repayment on the cashflow statement
---------------------------------------------------------------

On the refinancing date, we’ll pay back the existing senior debt. I’ve included a placeholder on the financial statements to show that repayment. Remember to adjust the annual financial statements and the output sheet to show the new cash flow line.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/4-2.jpg)

Set up the refinancing facility balance
---------------------------------------

I’ve added a four-line corkscrew using the macro and labelled the upward and the downward flow. I’ve hacked in a repayment value in the senior debt repayment and a matching amount in the refinancing facility corkscrew. I’ll replace these later; at the moment, I just want to check that everything flows through and the balance sheet keeps balancing.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/5-3.jpg)

Don’t forget the cover ratios
-----------------------------

If we don’t update the flag used to calculate our DSCRs for senior debt, we’ll end up with errors in the ratio calculation. The senior debt has been paid off, so there is zero debt service, but the ratio date flag hasn’t been changed, so the ratio continues to try and calculate.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/6-2.jpg)

Swap in our new adjusted senior debt repayment period flag to address this.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/7.jpg)

And so our model is set up, ready to handle a refinancing process.

We’re ready to go on and model the refinancing drawdown, interest and repayment amounts. This is all repetition of calculations you’ve already seen.

The file completed to this point for this bonus chapter is available in the file pack you'll receive when you [purchase the handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
. See file 4.57 FMH refi END 01a_._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero-7.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-a-refinancing-model-set-up#/portal/signup)
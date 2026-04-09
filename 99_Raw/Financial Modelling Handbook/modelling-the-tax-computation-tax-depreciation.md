# Modelling the tax computation - tax depreciation

**Source:** https://www.financialmodellinghandbook.org/modelling-the-tax-computation-tax-depreciation

---

Generally, tax authorities specify what companies can deduct for plant and equipment and other depreciable assets.

In some places, this has names like "capital allowances". In others, it's just plain "tax depreciation".

You'll often find different depreciation rates for different kinds of assets. Sometimes authorities will allow 100% of an asset to be written off for tax in the period the asset is acquired to achieve specific economic policy goals.

Our tax advisor has informed us that depreciation is on a declining balance basis with a 5% per quarter tax depreciation rate. If there is any residual tax value at the end of the project concession, it can be claimed in full in that period.

Let's walk through what this would look.

Download the start file for this assignment:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

  
Step 1: Set up a new "Tax depreciation" section & add a corkscrew.
---------------------------------------------------------------------

Use Skill 8 to add a corkscrew

Let's call the corkscrew "Asset value for tax".

![](https://www.financialmodellinghandbook.org/content/images/2022/02/1-1.jpg)

  
This is somewhat a mirror of the accounting asset value corkscrew on the asset sheet. There the upward flow is capex, and the download flow is accounting depreciation. But here, it's "allowable capex" - i.e. allowable for tax purposes. And the downward flow is "tax depreciation", which we are about to calculate.

The initial value will be the amount of the original book value of the asset that is allowable for tax. All of the asset book value is allowable in this fictitious jurisdiction. We can copy the link from the accounting asset balance corkscrew.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/2.jpg)

Step 2: Calculate tax depreciation.
-----------------------------------

The ingredients we need are:

*   Our tax depreciation rate (5%) as a new input
*   The beginning balance  of the Asset value for tax - a link to the beginning balance in the corkscrew
*   A final period operating period flag to allow us to write off any residual value in that period.

Step 3: Connect tax depreciation into the downward flow of the corkscrew
------------------------------------------------------------------------

In each period, the calculation will show a tax depreciation amount based on 5% of the remaining balance after the previous period's tax deprecation is charged.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/3.jpg)

  
Review
---------

It's helpful at this point to compare tax depreciation with accounting depreciation. We can use the skills we've already sheet to put two line items on the same chart.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/4.jpg)

  
This chart shows a timing difference between Tax depreciation and Accounting depreciation. We will come back to this difference when we look at Deferred Tax later shortly.

Lastly, we connect our Tax Depreciation line into our Taxable Profit calculation, then let's move on to look at how much of the debt interest we can deduct for tax.

Download the model complete to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--80.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

* * *

  

  

  

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-the-tax-computation-tax-depreciation#/portal/signup)
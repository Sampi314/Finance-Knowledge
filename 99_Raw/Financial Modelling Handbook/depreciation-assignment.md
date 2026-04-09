# Modelling depreciation - assignment

**Source:** https://www.financialmodellinghandbook.org/depreciation-assignment

---

Download the start file for this assignment.

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

* * *

At present, in our model, we have recognised an asset value of $100m at the transaction date. If we chart the balance of fixed assets, we can see that this balance stays constant over the life of the project:

![](https://www.financialmodellinghandbook.org/content/images/public/images/948bffc0-bd83-409b-b203-38b1964fa05d_1254x919.jpeg)

The case tells us that we should depreciate this asset on a straight-line basis over 25 years. Below you will find some guidance notes on calculating depreciation. We will walk through the process step by step in the next chapter.

Before we do that, let's make sure we have a hypothesis about how this will affect our model. In particular - will depreciation affect IRR?

Depreciation is a non-cash item. It will only appear on our income statement.

The "double entries" for depreciation that will ensure our balance sheet continues to balance will be as follows:

*   The asset side of the balance sheet: Fixed Asset book value will reduce by the amount of the depreciation
*   The liability side of the balance sheet: Retained earnings will decrease by the amount of the depreciation

The cash flow statement will not be directly affected at all.

I commonly hear people, especially in the PF sector, saying that the income statement doesn't matter; only the cashflows matter.

But how and when can the income statement impact cashflows?

Please take a minute and think through what you believe will happen to IRR when we add depreciation into our income statement.

There are only three options:

*   IRR will increase
*   IRR will stay the same
*   IRR will decrease

Which do you think it is? Why?
------------------------------

Be honest with yourself and make sure you have a hypothesis with clear reasoning. I'll share my view with you at the start of the next chapter. We can then compare against our modelled results.

In the meantime, here are some guidance notes for modelling depreciation. As usual, skip ahead if you want to tackle this unaided.

Guidance notes for modelling depreciation
-----------------------------------------

*   We only need to worry about depreciating the $100m initial balance at this stage. We don't yet have ongoing capex that will require depreciation. We'll come back to that later.
*   You will need a new flag. "Useful life of fixed asset" is a reasonable label. My approach will be to copy the Operating Period flag and replace the ingredients.
*   The 25-year Useful life of the asset will drive both the flag and the calculation of depreciation. Remember that we will charge depreciation quarterly, so you will need to divide the annual amount by 4.
*   Once you have calculated depreciation, sign switch it. You will connect the positive version into the Fixed asset corkscrew as the downward flow. There should be a placeholder in the corkscrew. You will link the negative version to the income statement. Again, there is a placeholder. Those two links are our double-entry accounting in practice!

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--137.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/depreciation-assignment#/portal/signup)
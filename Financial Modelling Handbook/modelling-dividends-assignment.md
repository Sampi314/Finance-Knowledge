# Modelling dividends - assignment

**Source:** https://www.financialmodellinghandbook.org/modelling-dividends-assignment

---

I said earlier in the book that it's useful to have a balancing balance sheet as early as possible in the model build. It helps us ensure that we are keeping our accounting and the internal consistency of our model on track.

Similarly, it's helpful to add key metrics to our model early in the process. In particular, IRR is a valuable metric to add early.

The reason for this comes back to the idea of always having a hypothesis. An essential part of our hypothesis, especially in transaction modelling, is "what is this going to do to IRR?". Having that question in your head and asking it each time you make a change is a very useful habit to get into.

It will enhance your intuitive understanding of modelling in general, and your model in particular, if you can continually try to predict what effect changes will have on IRR.

To calculate IRR, we first need to calculate dividends.

We will assume for this first pass at modelling dividends that shareholders want to get their model out as quickly as possible and make quarterly distributions of all available cash flow.

Later we may need to amend this calculation to allow additional complexity in the distribution dynamics. For example:

*   Distributions restrictions due to lender covenants
*   Minimum cash balance requirements to keep the company liquid and provide a cash buffer
*   Timing of distributions - for example, annual rather than quarterly distributions.

We are, however, going to observe the general requirement that we can only distribute the minimum of available retained earnings and available cash. Since dividends are the distribution of profits, we should only be distributing to the extent that there are positive retained earnings in the business. Similarly, we will only be able to distribute to the extent that there is cash. We could, in theory, borrow to make a distribution, but the act of borrowing would increase our cash on hand, and therefore the amount we could distribute; the rule would still apply.

Modelling dividend  - guidance notes.
-------------------------------------

As usual - skip these notes if you want to try the modelling yourself unaided.

Step 1: You will first need to set up two calculations - one to determine the available earnings and one to determine the available cash.

Step 2: For each one, you'll need to determine how much was in the business at the start of the period and how much was added or reduced during the period. For example, if you start the period with 100 of retained earnings and have 50 of Profit After Tax in the period, the total amount you could distribute will be 150. Similarly, if you started the period of 200 cash but had a negative cash flow of 75 in the period, you will only have 125 available to distribute at the end of the period.

Step 3: Once you have determined the earnings and cash available, take the minimum in each period.

Step 4: Remember that either available cash or available earnings could be a negative number. You could not, however, have a negative dividend. Therefore, you'll need to restrict the dividend calculation so that a negative number is impossible.

Step 5: Once you have calculated the dividend amount, flow it into the retained earnings and the cash corkscrews. Dividends reduce both at the same time.

Always have a hypothesis:
-------------------------

Looking at your model now, before you model dividends, what is the maximum amount of dividend that this model could pay?

* * *

Download the start file for this assignment:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--89.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-dividends-assignment#/portal/signup)
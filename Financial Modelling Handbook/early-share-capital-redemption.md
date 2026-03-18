# Early share capital redemption

**Source:** https://www.financialmodellinghandbook.org/early-share-capital-redemption

---

So here’s your assignment.

Can you restructure your model so that you first pay whatever dividend you can, given the profit restrictions on dividend payments? Then whatever cash is left in the period, you make an early redemption of share capital.

There’s a limit, though; you have to maintain a minimum of $1m in share capital in the business. There will always be some minimum share capital requirement. This minimum varies from place to place.

The reference file for this bonus chapter is available in the file pack you'll receive when you [purchase the handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
. See file _4.60 FMH early BEG 01a._

If you’re tackling this yourself, here’s a hint before you begin: you’ll need to change the order of the cashflows on the waterfall - you’ll want to pay dividends first and then test to see what cash is available to pay share capital. Just like the refinancing facility itself, you’ll want this “option” to make an early share capital redemption to be something you can easily activate or de-active using a switch. Have a go before you review the solution.

### Early share capital redemption solution.

There’s a little bit of model rewiring required for this assignment.

Firstly we need to switch the order of payments on the cash cascade. We want to pay as much dividend as possible given the profit restriction. And then, if there is remaining cash in the period, pay out as much as possible as early share capital redemption, given our minimum share capital requirement.

My updated cashflow statement looks like this:

![](https://www.financialmodellinghandbook.org/content/images/2022/11/1-5.jpg)

Let’s walk through the revised share capital redemption calculations block by block:

![](https://www.financialmodellinghandbook.org/content/images/2022/11/2-5.jpg)

We are maintaining the existing final period share capital redemption calc. We don’t know how much share capital will be redeemed in the early periods. We do know we will have at least $1m left and so this will need to be repaid in the final period.

In rows 22 to 25, we calculate the maximum share capital that can be redeemed by looking at the actual share capital balance and subtracting the minimum share capital requirement. This will mean that we always maintain a minimum of $1m.

Row 27 to 29 is crucial. In this row block, we are testing to see how much cash is available for share capital redemption. This is similar to the block we created for the dividend calculation. We’re looking at the beginning cash balance and adding the Cash flow available for share capital redemption in the period. This gives us the total cash available in the business after everything, including dividends, has been paid.

In rows 31 to 33, we compare the maximum share capital that can be redeemed, with the cash available. We take the lower of those two.

In the final block, in rows 35 to 39, we create the switch which will allow us to activate or deactivate the early share capital redemption.

Finally, we also need to adjust our retained cash balance. Instead of Cash flow available for dividends as the upward flow, and dividends as the downward flow, we replace them with the share capital ingredients since they are now the final ingredients in our cash cascade.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/3-5.jpg)

With this structure in place, looking at our cash flow statement, we can see that the surplus cash created by the refinancing can all now be distributed.

This gives us a boost to our incoming investor IRR from 13.13% in the previous scenario (with no early share capital redemption), to 13.72% with the early share capital redemption.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/4-5.jpg)

This seems to be doing the job, so let’s go back now and test our hypothesis that, with the ability to distribute the surplus cash, increasing the term of the refinancing should increase our IRR

The solution for this bonus chapter is available in the file pack you'll receive when you [purchase the handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
. See file 4.60 FMH early END 01a_._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero-10.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/early-share-capital-redemption#/portal/signup)
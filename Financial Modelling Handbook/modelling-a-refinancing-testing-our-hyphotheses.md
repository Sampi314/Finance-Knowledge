# Modelling a refinancing - testing our hypotheses

**Source:** https://www.financialmodellinghandbook.org/modelling-a-refinancing-testing-our-hyphotheses

---

We’re now able to use the model for the kind of exploratory analysis that is needed to support the real transaction. A well-built financial model is a great negotiating tool. If we know ahead of time which elements of the refinancing package make the most difference to our returns, we know where to focus on our negotiations.

In this imaginary situation, we don’t yet have terms for our refinancing; we’re just exploring what impact repayment term, debt margin and debt sizing DSCR all have on our returns.

So far we have modelled a 10-year refinancing, using the same interest margin and debt sizing DSCR we used for our senior. We’ve seen that this gives a roughly 4% boost to the “all equity” IRR.

This means that if we were to pay a premium size to hit 12% IRR as the incoming investor, we’d also see a boost to our returns.

Challenge: can you set up the IRR calc for the incoming investor which shows the IRR we’d obtain if we size our premium at hit 12%, then later achieve a refinancing?

Have a go using the reference model for this section: 4.59 FMH test BEG 01a

### IRR for incoming investor

To measure the IRR for the incoming investor we first need to “de-activate” the refinancing. We’re not going to price the refinancing into our premium calculation; we’re exploring how refinancing could boost our returns later.

I’m therefore setting up a scenario with the refinancing switched off, to begin with.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/1-4.jpg)

I’m creating a new IRR calc for the incoming investor, with the premium paid to hit 12% “locked” as an input.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/2-4.jpg)

This shows 12%, as I would expect. I’m adding this to the output sheet as a new key metric. (Go back to your key skills from Chapter 2 if you need a reminder of how to add metrics to the Output sheet).

I’m now able to run the refinancing scenario and see how this changes my IRR.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/3-4.jpg)

Although I am interested in the “all equity IRR” - I’m more interested in _my_ IRR as the incoming investor.

Let’s now look at this metric when we run different scenarios on the refinancing repayment period. Remember - hypothesis first. I’m assuming that if I increase the refi repayment period, I’ll have a greater debt capacity for the refi; this will increase the size of the refi and the amount of surplus that can be paid to investors at the refi date, boosting my IRR.

I’m going to run scenarios on 11, 12, 13 and 14-year refi, comparing to my original 10-year refi.

It’s useful here to use the scenarios in the input sheet, rather than change the base case assumptions.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/4-4.jpg)

Don’t forget to solve the model with a case run. Here’s my output sheet with the cases run, and stored:

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/5-5.jpg)

This is why we have a hypothesis first: if the model doesn’t react the way we thought either we don’t understand the model/business dynamics as well as we thought we did, or the model is wrong.

If I chart my incoming investor IRR against refinancing debt term, it looks like this:

![](https://www.financialmodellinghandbook.org/content/images/2022/11/6-3.jpg)

We get an initial boost in IRR with an 11-year refi, but then our returns decline with an increased repayment period.

What the hell? This is not what we expected, but remember, this is great data. Assuming the model is calculating correctly, the model is telling us something about the dynamics of the business.

It’s our job to dig in now and find out what’s happening.

Use your own model to see if you can come up with an explanation for this before you read on.

The solution for this bonus chapter is available in the file pack you'll receive when you [purchase the handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
. See file _4.59 FMH test S1 01a._

### Why is the IRR going down with an increased debt term?

The key to understanding this is to look at the retained cash chart. With the 14-year refi active, the chart looks like this:

![](https://www.financialmodellinghandbook.org/content/images/2022/11/7-1.jpg)

Retained cash with 14-year refinancing

We can see that the refinancing is generating a surplus, but we are unable to distribute this surplus to investors as a dividend due to having insufficient retained earnings.

We are therefore undertaking the refinancing, and thereby increasing our debt service, but the cash surplus generated at the refinancing date is just sitting on the balance sheet.

This is a classic problem in Project Finance/infrastructure modelling; our business is capital intensive and therefore we have a relatively high depreciation charge. This lowers retained earnings relative to cash and causes us to have a “trapped cash” situation.

There are a number of ways to tackle this which I cover in my Project Finance training courses. For now, let’s just look at one such option - early redemptions of share capital.

My revised hypothesis is that if I can repay share capital early, it will release the trapped cash that I can’t get out as a dividend, and I should then see the relationship I was expecting between refinancing debt term and investor IRR.  

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero-9.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-a-refinancing-testing-our-hyphotheses#/portal/signup)
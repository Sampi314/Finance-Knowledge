# Why we use calculation blocks in financial models: Part 1

**Source:** https://www.financialmodellinghandbook.org/calculation-blocks-part-1

---

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

We are going to build a model together based on a solar acquisition case study. One of our first jobs will be to model electricity generation revenue.

If you've ever seen a model before, you'll be familiar with something that looks like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/34828302-26b7-481e-a4eb-dde1504bc302_2382x622.jpeg)

The modeller here has calculated revenue in a single line. They have used lots of off sheet references. Most likely, this is what you've seen in most models you've looked at in the past.

Here’s the formula in full:

\= InpC!$F$36 / InpC!$F$55 \* InpC!$F$34 \* InpC!$F$35 \* IF(Time!M$90=1, 1/((1+InpC!$F$33) ^ (Time!M$56-1)), 0) \* @IF(Time!M$90=1, INDEX(InpC!$F28:$F31,Time!M$51), 0) \* InpC!$F$54 \* Time!M$90

### What's good about this?

It's compact. We have only taken up one row in the model.

### What's not good about this?

It's horrible to read and make sense of. To understand the formula, we have to hunt around the model to find each component.

Without going to the input sheet and looking, I have no way of knowing that the first item that the formula is referencing (InpC!$F$36) is the power tariff. I have to go to the input sheet, find that item, see what it is, see what the value is, then come back to where I started. And I have to repeat the process for each item within the formula.

Our conscious brains can hold between 4 and 7 chunks of information at a time. Given how long some formulas are, it won't be long before we run out of mental storage space.

If I chart revenue, I get a profile like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/274cc78b-43aa-4403-85f2-f3e7e8d8d2ef_2282x1650.jpeg)

What is causing the spikes? What is causing the downward slope? Looking at just this formula, I have no way of knowing which of the ingredients are causing these effects.

So apart from the fact that it only takes up one row, there is very little to recommend this approach to writing formulas in models.

Here is the same calculation, laid out in blocks.

![](https://www.financialmodellinghandbook.org/content/images/public/images/4c97b06e-2900-4454-84a0-cd1932362bcf_2464x1458.jpeg)

You can see that the formula in row 41 gives the same answer as the calculation in row 8. You can therefore see that this is the same calculation. It's just the layout that's different.

The difference is that when we lay the calculation out in blocks, we can see all the precedents.

At this point, you may be thinking, "Holy crap, Kenny, you've just taken 30 rows to do a calculation that you could do in one." And that is the "downside" of this approach - it uses rows. But rows are free. There isn't a row shortage. And the advantages outweigh any downside of overly abundant row usage.

### So what's good about this approach?

Readability:

1.  The formula is much, much shorter. The reader requires much less work to figure out what the formula is doing.
2.  All of the ingredients driving electricity generation are right next to the calculation. With their labels. And their values. I have to read them. No paging around the model. No trying to hold lots of facts in my head simultaneously.

![](https://www.financialmodellinghandbook.org/content/images/public/images/0c1d0d09-c7b7-4010-8868-e9e7bb5d7a84_2246x686.jpeg)

One of the ways I've made the formula simpler is by breaking it up into several smaller, easier to understand steps.

For example, I have broken out the calculation of electricity generation into a separate block with its own ingredients. The result of this calculation block is feeding into my revenue block. I can review a simple formula while having immediate visibility over the components.

![](https://www.financialmodellinghandbook.org/content/images/public/images/1332937b-81d6-4054-9552-1964cd32162a_2170x794.jpeg)

Since all the ingredients are now visible, I can see the line items causing revenue to have the profile I saw in the chart. I can see this without hunting around the model and spending time trying to figure it out. It's all right in front of me.

I can see that the Seasonality adjustment is responsible for the spikes in revenue. I can see that degradation is responsible for the downward slop in revenue.

Next up, we'll look at what goes into building a calculation block.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero-2.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/calculation-blocks-part-1#/portal/signup)
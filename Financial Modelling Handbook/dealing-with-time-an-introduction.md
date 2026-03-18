# Dealing with time: An introduction to flags

**Source:** https://www.financialmodellinghandbook.org/dealing-with-time-an-introduction

---

Time is central to any financial model.
---------------------------------------

Let's take any debt instrument. We need to know "how much" debt we will include. We also need to answer several "When" questions:

*   When will the debt be drawn?
*   When will repayment start?
*   When will repayments end?
*   On what dates will repayments occur?

Remember that there are two questions we always have to answer about anything that we're modelling: "How much?" and "When?"

Answering the "when" questions will take up a significant amount of our modelling logic.

Download the worked example file:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Looking first at our revenue example calculation:

![](https://www.financialmodellinghandbook.org/content/images/public/images/f016dbe2-c802-4c36-bfc1-4b5d8348ca6a_2986x944.jpeg)

In this block, we use the Operating Period flag to tell the calculation when it should include revenue. We can't show any revenue until the period after the transaction date. As it's a 25-year contract, we should not show any revenue after the 25 years.

Benefit of separating
---------------------

One of our design objectives is to keep our formulas as short and straightforward as possible. Modelling flags as separate, distinct items in our model has several benefits:

**We don't have to keep repeating logic.**
------------------------------------------

Numerous line items in our model will be affected by the 25 year fixed contract duration. If I don't use a flag for this, I must keep repeating the logic in every calculation.

It keeps formulas shorter.
--------------------------

Separating the "How much" logic from the "When" logic makes our formulas shorter. In the above example, the revenue formula is:

$F33 \* $F34 / $F35 \* J36 \* J37. 

The part that deals with time is "\* J37".

If we didn't include a flag, our formula would look like the example below:

![](https://www.financialmodellinghandbook.org/content/images/public/images/8713a449-12d9-4425-ab55-9f6f12cb4285_3072x920.jpeg)

Note that the formula is now a good deal longer:

IF( AND(M2 > InpC!$F19, Ops!M2 <= Time!$F87), $F41 \* $F42 / $F43 \* M44, 0). 

And I'd have to keep repeating the first part of the formula every time I wanted to apply the "Operating Period" logic.

1s or 0s
--------

Flags are always either a 1 or a 0. They are a 1 to indicate that something is happening. They are a zero to show that that something isn't happening.

Multiply or IF
--------------

We always include the flag as an ingredient in our calculation block. We then have two choices as to when we use the flag. We can either multiply by the flag or use an IF statement.

Multiplying by the flag
-----------------------

In our worked example file for this section, we have multiplied by the flag in calculating revenue. Doing this causes the revenue to be zero in any period outside our pre-determined operating period. Multiplying by the flag is the simplest way of applying the logic to a calculation and is the preferred option where possible.

Using an IF statement
---------------------

![](https://www.financialmodellinghandbook.org/content/images/public/images/d7dab37f-3802-4b98-9ad0-135d9ef1582a_3028x866.jpeg)

In the discounting example above, we are using an IF statement. An IF statement is a good choice since we want the calculation to do two different things depending on the flag status. We want our discounting base date to be at the Financial Close / transaction date. We, therefore, know that we want the discount factor to be one on this date. In each period after that, we want the calculation to look at the previous period's discount factor and apply a further one period of discounting.

Time sheet
----------

It can be helpful to keep all the flags together on the time sheet. This is just for ease of finding the flags. Some of the flags will be used many times in the model. If all the flags are in the same place, it will be easier to find them when we need them.

Some people recommend putting the flags into the header rather than linking to a timesheet. There's nothing wrong with this approach. It's not my preference as I don't like to take up valuable screen real estate with lots of rows at the top of my sheet containing flags. Plus, I usually have dozens of the flags in my model. I'd therefore be constantly facing the decision of which ones to include in my header. That's not valuable thinking time in my book.

**The good news is that there are only five kinds of flags you ever need to model. We'll go through each one in the next chapter.**

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--120.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/dealing-with-time-an-introduction#/portal/signup)
# Q&A: How to calculate period interest rates

**Source:** https://www.financialmodellinghandbook.org/q-a-how-to-calculate-period-interest-rates

---

_Hi Kenny.  
Many thanks for this incredible material.  
I've got a doubt regarding the calculation of the quarterly interest. I thought that the conversion from annual interest to a smaller period interest shouldn't be just a division. I thought that you should always consider the time value of money. Therefore the calculation would be:  
((annual interest + 1 ) ^ ( # days/ days in a year) )- 1  
Is my understanding correct?  
Thanks  
Sergio_

* * *

Hi Sergio,

This is a great question and an area of common misunderstanding.

The calculation we use to convert an annual interest rate to a period interest rate depends on:

*   How the annual interest rate has been expressed and whether the interest is being rolled up into the debt balance
*   The day count convention used to define what a year is for interest purposes.

### How the rate has been expressed.

The rate has been expressed as an _effective interest rate._ To convert from an effective interest rate to a period rate, you would decompound it using the calculation you mention in your question.

Let's ignore day count conventions for the moment. If you had an effective annual rate of 6%,  being compounded in four equal quarterly amounts, the amount of interest that would be charged each quarter would be per your formula:

_Where Rp is the period rate and Ra is the annual rate:  
_Rp = (1 + Ra) ^ (1 / 4) - 1

The rate has been expressed as a _nominal rate._ If this is the case then we do not decompound to calculate the period rate. This is the case that you are seeing in the case study model.

In this case, the interest is being _paid_ quarterly and is _not compounding_ or rolling up into the debt balance.

In this case, again assuming equal quarters, the amount of interest would be given by:  
Rp = Ra / 4

However, we also have to take into account the day count convention being used to express the interest rate.

### Day count convention

There are different day count conventions for different financial products in different markets. You'll see these expressed as, for example, act/360 or act/365. When calculating the period rate, it's important to be sure of the day count convention being used to express the annual rate. With an act/360-day count convention, you would use 360 as the "days in year" for the conversion.

To calculate a period rate from an annual nominal act/360 rate:

Rp = Ra / 360 \* DaysInPeriod

To calculate a period rate from an annual effective act/360 rate:

Rp = (1 + Ra) ^ (DaysInPeriod / 360) - 1

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--153.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/q-a-how-to-calculate-period-interest-rates#/portal/signup)
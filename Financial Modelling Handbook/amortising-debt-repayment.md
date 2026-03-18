# Debt modelling -  Amortising principal repayment

**Source:** https://www.financialmodellinghandbook.org/amortising-debt-repayment

---

* * *

Download the lesson start file:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

An amortising debt repayment profile refers to one where debt service, the sum of interest and principal, are equal over the debt term.

With an amortising debt profile, we'll repay less debt principal in the initial periods and more later. Previously we had level principal repayment meaning total debt service was high in the initial periods. Moving to level debt service should help us with the problem of not having enough cash in the early periods for the large debt service amount.

**How will this affect IRR?**

Less debt service in the early periods and more debt service in later periods should be good for our IRR since cash can be distributed to equity earlier.

How to model a "level debt-service" amortising debt profile
-----------------------------------------------------------

While it's possible to do this with Excel functions, I find it to do it manually, especially when we have a changing periodic interest rate, as we have here.

The way we do this is to use the debt interest rate to calculate a discount factor. We then add the discount factors up and divide the debt by the sum of the discount factors. This gives us the amount of debt service charged every period on the debt.

Let's see it in action.

![](https://www.financialmodellinghandbook.org/content/images/public/images/8987fedb-7fb3-44e8-9f11-90dbbea57b27_2062x842.jpeg)

We use the financial close date as our base date for calculating the discount factor. This is because it's the debt that we draw down the debt.

The formula, therefore, starts with testing to see if the financial close date flag is one. If so, the discount factor is one. If not, the formula looks at the previous period's discount factor and applies one further period of discounting, using the debt interest rate.

We only want to add up the discount factors during the debt repayment period. We, therefore, use the debt repayment flag and a SUMPRODUCT function.

![](https://www.financialmodellinghandbook.org/content/images/public/images/3b7e1d90-b163-4e2d-aa4a-495b0edfa21f_2316x956.jpeg)

We then divide the original debt amount by the sum of the discount factors to get the periodic debt service amount.

And then use the debt repayment period flag to place the debt service on the timeline...

![](https://www.financialmodellinghandbook.org/content/images/public/images/ee399d6b-3033-48de-96bd-818e2075fdf9_2370x906.jpeg)

Now that we know the debt service amount, we can deduct the interest to determine the principal repayment amount.

![](https://www.financialmodellinghandbook.org/content/images/public/images/dd66111d-22cd-45b2-8f8b-c076e0da12e6_2536x1692.jpeg)

At this stage of the process, we're getting the wrong principal repayment amount. The model shows c. $75m rather than the $70m, which should be the amount of debt paid back.

That's because the debt balance is still based on the level principal repayment profile, which is currently connected to the model. Therefore we deducted the wrong amount of interest from the debt service.

Our next step is to wire the amortising principal repayment into the placeholder that we left for it so that we can switch to that profile.

Once the profile has been switched to number 2, and the amortising profile is driving the debt balance, the interest calculation changes, and we get a repayment amount of $70m.

![](https://www.financialmodellinghandbook.org/content/images/public/images/1a21cfcf-3b91-420c-876e-fa23e2519363_2566x738.jpeg)

If we now chart debt service, we can see that we have achieved our objective of level debt service. The second line on the chart shows the principal repayment profile which starts lower and then increases:

![](https://www.financialmodellinghandbook.org/content/images/public/images/03574c2e-1451-4f3e-ab15-7aebc1899a8d_2462x1756.jpeg)

If we add CFADS to this chart, again with a simple copy and paste, we can see that we still have a problem of insufficient cashflows in multiple periods:

![](https://www.financialmodellinghandbook.org/content/images/public/images/886b2525-5813-48cf-8f7a-f4815186c620_1262x924.jpeg)

Our revenue seasonality is still causing a problem for debt repayment.

Reviewing our output sheet, we can see that IRR has gone up. This is in line with our earlier expectations. It’s also interesting to note that the IRR has gone up despite the fact that we are paying more debt interest. The higher level of interest paid is due to the fact that we are paying less principal in the early years, and so the debt is being paid down more slowly.

This current repayment profile would not be acceptable to lenders. To allow us to determine what would be acceptable we will next look at specific lender metrics.

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--133.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/amortising-debt-repayment#/portal/signup)
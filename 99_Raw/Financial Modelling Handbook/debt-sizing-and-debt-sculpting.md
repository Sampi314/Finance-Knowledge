# Debt modelling - Debt sizing & debt sculpting

**Source:** https://www.financialmodellinghandbook.org/debt-sizing-and-debt-sculpting

---

Download the lesson start file:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Until now, we have used the 70% leverage input given in the case. Leverage is only one of the metrics that lenders will use to determine the maximum debt capacity.

They will also use "affordability" ratios like Debt Service Cover Ratio.

We are using the leverage % to determine the amount of debt and then calculating the resulting debt service cover ratio.

We will change that now and determine the amount of debt using the minimum DSCR, and then calculate the resulting leverage.

We are also going to use the ratio to determine the debt service. If lenders require a certain ratio in every period, we can use that to determine what debt service level is required to meet the ratio.

Let's walk through it.

Step 1: Calculate debt service at the target ratio
--------------------------------------------------

We have already seen that DSCR is calculated by dividing Cash Flow Available for Debt Service, by Debt Service.

DSCR = CFADS / Debt service.

Since we know CFADS (it's on our cash flow statement), we can rearrange the formula to determine the level of Debt service required to meet a certain coverage ratio.

Let's say that lenders require a ratio of 1.3x.

Our first step is to calculate the maximum debt service in each period, given the target ratio of 1.3x.

Given that DSCR is an "affordability ratio" - looking only at the cash flows in each period, we can only consider the CFADS during the debt term.

Our first step, therefore, is to calculate CFADS during the debt term:

![](https://www.financialmodellinghandbook.org/content/images/public/images/9a954d48-e8b9-4654-acb5-cdbef88eb281_1131x384.jpeg)

We can then use this to calculate debt service at the target ratio. We divide the CFADS by the target ratio to calculate the debt service.

![](https://www.financialmodellinghandbook.org/content/images/public/images/884bc168-29d6-475a-8923-f2eb9f1d89f0_1183x391.jpeg)

Step 2: Bring up the senior debt discount factor
------------------------------------------------

Next, we want to figure out the amount of debt drawn at the transaction date that will generate the debt service we have calculated. This will be the maximum debt capacity of the business.

For this, we need to discount the debt service using the period debt interest rate as our discount rate.

We have already created a Senior debt discount factor when calculating the amortising debt profile.

Since we need this discount factor for both calculations, I will move it further up the debt sheet. As your model build progresses, don't be afraid to move calculations around to improve the structure and flow of the model. Remember when you are moving calculations around, use Ctrl+x to cut rather than Ctrl+c to copy.

![](https://www.financialmodellinghandbook.org/content/images/public/images/42bdf946-2484-46b4-a62b-b78bbdf5d962_1112x458.jpeg)

Step 3: Calculate debt capacity
-------------------------------

Now that I have both the ingredients I need, I can calculate the debt capacity by multiplying the debt service in each period by the discount factor for that period. SUMPRODUCT is an efficient function to use for this.

![](https://www.financialmodellinghandbook.org/content/images/public/images/e53f2828-f57f-4ca3-955a-1aab5b48904b_1033x541.jpeg)

We can see that using the target ratio for debt sizing gives us a higher debt amount than our initial assumption around leverage.

Typically lenders will provide minimum DSCR and maximum leverage constraints. If the maximum leverage were 70%, we would not be able to borrow more than that even if the DSCR debt sizing indicated that we could.

Step 4: Switch between DSCR and leverage debt sizing
----------------------------------------------------

I want my model to easily switch between DSCR based debt sizing and a straightforward leverage percentage input as we have now.

I'm therefore introducing a simple switching mechanism.

![](https://www.financialmodellinghandbook.org/content/images/public/images/8536f5db-458d-4991-aae9-e3b56209db46_967x493.jpeg)

Step 5: Calculate periodic principal repayment amount to maintain the target ratio.
-----------------------------------------------------------------------------------

When we calculated the amortising debt profile, we first calculated the period debt service and then deducted the interest to arrive at the principal repayment amount.

We have now calculated the periodic debt service to maintain our target ratio. We can use the same approach of deducting interest from this debt service profile to calculate the principal repayment amount that will give us a constant DSCR.

![](https://www.financialmodellinghandbook.org/content/images/public/images/c4381f64-a6b7-4b39-badf-de6d1f53c1da_1056x664.jpeg)

Once we have deducted interest to calculate the principal repayment amount, we can wire that into our "principal repayment selection" block and choose profile 3.

We can see that our IRR has gone up as expected, and our ratios are at 1.30 in every period.

![](https://www.financialmodellinghandbook.org/content/images/public/images/5e2ff6e4-7ae9-48a5-a534-ee58f5dbf723_1231x405.jpeg)

To achieve this, the profile of debt service has changed dramatically:

![](https://www.financialmodellinghandbook.org/content/images/public/images/f2ba1cc9-9420-48ff-9c55-9e4bda64fe77_1269x922.jpeg)

However, we can see a problem with the principal repayment amount in the first period. There is insufficient cash flow in the first period to even pay the interest on the debt without breaching our minimum ratio. Therefore, our calculation yields a positive principal payment, which doesn't make any sense.

I could have set the assumptions in the model up to prevent this from happening, but this kind of issue is common when building models. It's not a problem or error with the model. It's the model telling us that there is a problem in the business that needs to be solved. And solving that problem requires a commercial / structuring solution.

In the next chapter, we'll look at some options for fixing this.

Download the model completed to this stage:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--81.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/debt-sizing-and-debt-sculpting#/portal/signup)
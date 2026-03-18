# Equity premium on acquisition

**Source:** https://www.financialmodellinghandbook.org/modelling-equity-premium-on-acquisition

---

We're now ready to turn to the critical question that has driven the building of this model in the first place.

As a reminder, from the case:

Sponsors plan to sell 40% of the business to an investment partner. You are being asked for your offer to purchase 40% of the common stock of the Project Company (ProjectCo). Your offer will take the form of a premium that you are willing to pay to acquire this share in the Project.

You would be looking to secure an Equity IRR of 12% on the investment.

We already have an IRR calculation in the model.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/1-13.jpg)

We can think of this as the "all equity par" IRR.

With an investment of $22.9m and the dividends flow currently in the model, the IRR will be 20.08%.

Our question is what premium we'd be willing to offer to achieve a 12% IRR. It would be usual for an investor coming in later in the process who has not taken development or construction risk to accept a lower IRR.

How to calculate the premium
----------------------------

The definition of IRR is the discount rate that makes the net present value equal to zero. If we set up an NPV calculation and input the current IRR as the discount rate, we'd get an NPV of zero. If we input a lower discount rate, we'd get a higher NPV. Therefore if we did this with the target IRR of 12% as our discount rate, this would give us the premium we'd be willing to pay to acquire the cashflows and achieve a 12% IRR.

### Step 1: Calculate the cash flows for the incoming investor.

We are looking to buy 40% of the project. We will put in 40% of the par value of the equity and get 40% of the dividends in return. The first step is to calculate those cashflows, taking 40% of the full equity cashflows.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/2-9.jpg)

### Step 2: Calculate the discount factor

  
We can then replicate the calculation we used for the senior debt discount factor, using the period rate for the incoming investor cash flows.

Since we've used the XIRR function for the "all equity IRR", we'll take the length of period into account when calculating our discount factor.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/3-9.jpg)

### Step 3: Calculate the present value at a 12% discount rate  

We'll use the simple SUMPRODUCT method we've used before.

We can see that an incoming investor looking to achieve a 12% IRR should be willing to pay a premium of $7.966m over the par value of the equity.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/4-6.jpg)

### Step 4: Section end checklist

In testing this calculation, we'll ensure that increasing the IRR should reduce the premium and vice versa. It's also worth putting the IRR into the calculation to ensure that it gives us a zero NPV.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/5-7.jpg)

We'll also want to put the premium onto our output sheet as it's the key metric in the model.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/6-2.jpg)

As ever, run through the Section completion checklist.

Download the financial model complete to this point.

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--77.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-equity-premium-on-acquisition#/portal/signup)
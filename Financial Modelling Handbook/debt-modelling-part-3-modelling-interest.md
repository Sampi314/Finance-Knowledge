# Debt modelling part 3: Modelling interest

**Source:** https://www.financialmodellinghandbook.org/debt-modelling-part-3-modelling-interest

---

Download the lesson start file:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
_

* * *

In our modelling case, we are told that we have an all-in annual interest rate of 6.3% (made up of a 2.5% swap rate plus a 3.8% senior debt margin).

We're also told that the period interest rate will be calculated based on an actual / 360-day count convention.

This means that the quarterly interest rate will be calculated as the annual rate / 360 \* days in the quarter.

Let's walk it through.

Step 1: Grab the number of days in the period
---------------------------------------------

We have already calculated this and used it in the working capital calculation.

I can therefore copy the link from that sheet using Skill 4

Step 2: Add the necessary inputs
--------------------------------

These are the swap rate (2.5%), the margin (3.8%), and the number of days in the year given the day count convention (360).

**Step 3:** Calculate the period rate based on the formula above.
-----------------------------------------------------------------

![](https://www.financialmodellinghandbook.org/content/images/public/images/768b5d6f-3d68-4b06-be07-4b4af7e82ecf_2206x592.jpeg)

Step 4: Create the interest payment block
-----------------------------------------

Now that we have the period rate, we must multiply by the correct balance. The beginning balance is the correct one to use in this case since principal repayments are made at the end of the period.

![](https://www.financialmodellinghandbook.org/content/images/public/images/84a067a5-8d9e-43a0-b566-c8e51d2c6ea2_2276x1384.jpeg)

Step 5: Sign switch and link into financial statements
------------------------------------------------------

Debt interest goes through both the income statement and the cash flow statement. Thereby reducing (liability) and cash (asset) by the same amount.

I can copy the sign switch line from debt principal as it's the closest one.

![](https://www.financialmodellinghandbook.org/content/images/public/images/a8d88976-4fe3-4be3-8986-6e1eab9ade51_2888x1112.jpeg)

Step 6: Check IRR impact
------------------------

We stated previously that IRR was overstated since we hadn't modelled interest, thereby making the debt free money.

It's worth a quick check on IRR to ensure that the IRR went down when we added interest into our model.

![](https://www.financialmodellinghandbook.org/content/images/public/images/21e962e8-3421-44e7-aa8f-9502e035bbd7_2560x892.jpeg)

Our output sheet confirms that IRR has reacted in the way we would expect.

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
_

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--135.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/debt-modelling-part-3-modelling-interest#/portal/signup)
# Debt modelling - Debt service coverage ratio

**Source:** https://www.financialmodellinghandbook.org/debt-service-coverage-ratio-dscr

---

Download the lesson start file:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

For mortgages, lenders will apply a maximum loan to value ratio to ensure that home buyers also have sufficient "equity" in the home. They will also apply a multiple of borrowers earnings to determine the affordability of the mortgage.

It's not dissimilar in a business like this.

The "loan to value" ratio in this instance is given by the maximum leverage that lenders are willing to see in the business. Lenders will determine the "affordability" using a Debt Service Coverage Ratio, or DSCR.

DSCR is defined as Cash flow Available for Debt Service / Debt Service.

There can be different time periods that this ratio can be calculated over. The ratio is also sometimes forward-looking, sometimes backwards looking.

It measures the ratio of cash available to pay debt to the debt due.

Typically lenders will look at both the minimum and average values of the ratio. Average DSCR can sometimes be defined as the average of the periodic ratios, or it can be total CFADS over the term of the debt, dividend by the total debt service.

Modelling this ratio is relatively straightforward as we already have the ingredients from previous work that we've done.

We will calculate the three-month historic DSCR.

**Step 1:** Gather your ingredients.
------------------------------------

You need:

*   Cash flow available for debt service (from the cash flow statement)
*   Debt service (we have already added this to our debt sheet
*   Senior debt repayment period flag.

![](https://www.financialmodellinghandbook.org/content/images/public/images/e022b1b0-4d95-4f61-8559-aa7ca2863b78_1344x359.jpeg)

**Step 2:** Calculate the period ratio.
---------------------------------------

It's helpful in this calculation to use an IF statement referring to the flag. If it's not a ratio calculation date, the IF statement returns "na" rather than zero. When we calculate the minimum and average ratios, the periods in which there is no ratio will be ignored by the MIN and AVERAGE functions.

![](https://www.financialmodellinghandbook.org/content/images/public/images/7280d42a-8069-474d-974e-df9adb8b6572_1242x427.jpeg)

Step 3: Calculate the minimum ratio and the average of the periodic ratios
--------------------------------------------------------------------------

Using the MIN and AVERAGE functions.

![](https://www.financialmodellinghandbook.org/content/images/public/images/b30a1bd3-05ea-4785-823e-3ba7b6e698b1_1343x430.jpeg)

We can see that the minimum ratio is below 1. This is another way of observing what we have already seen; in the first period, there is not enough cash flow to make the debt service payments due in that period.

If we chart the 3m DSCR, we can see a wide seasonal swing, reflecting the high seasonality in revenues.

![](https://www.financialmodellinghandbook.org/content/images/public/images/20de734f-df88-4d50-82d0-34d13d4f345e_1277x936.jpeg)

We can see that the ratio falls below 1 in multiple periods. This means that the business does not have sufficient cash to pay debt in these periods. This is not a base case that project sponsors could present to lenders.

The average ratio is relatively healthy, though, and within the range of what would be required on a project like this. We will see in the next chapter how we can use the ratio to calculate the debt capacity of the business and profile debt service to ensure that we always meet the minimum cover ratio requirement.

**Step 4:** Add the ratios to the output sheet.
-----------------------------------------------

Using skill 12, link the ratios to the Output sheet so that we can continue to track them as we have been doing our IRR. These are critical metrics for lenders, and we want to ensure we keep an eye on them.

![](https://www.financialmodellinghandbook.org/content/images/public/images/7d130b56-c7a6-4c4a-8fdd-9050ce53a67a_973x244.jpeg)

* * *

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--126.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/debt-service-coverage-ratio-dscr#/portal/signup)
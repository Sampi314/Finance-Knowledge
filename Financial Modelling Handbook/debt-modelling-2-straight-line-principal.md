# Debt modelling 2: Straight-line principal repayment

**Source:** https://www.financialmodellinghandbook.org/debt-modelling-2-straight-line-principal

---

* * *

Download the lesson start file:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Modelling the straight-line principal repayment of debt is like modelling straight-line depreciation.

So similar, in fact, that we can copy the same structures we used to model that.

Step 1: Copy the Useful life of asset flag.
-------------------------------------------

I used Ctrl+shift+= to insert the copied cells immediately below the Useful life of asset flag.

![](https://www.financialmodellinghandbook.org/content/images/public/images/c9eb30d9-26bb-4a2e-a463-7c7f02190336_2128x1082.jpeg)

Step 2: Change the ingredients within the flag calculation & re-label where necessary
-------------------------------------------------------------------------------------

I need to swap out the "Useful life of asset" link with a "Senior debt repayment period" link. I, therefore, first create this on the input sheet.

![](https://www.financialmodellinghandbook.org/content/images/public/images/ab38c332-3954-41a4-bcae-d151b4422bd7_1912x1082.jpeg)

We replace the Useful life of asset link, re-label the calculations, and relink the final debt repayment period date into the flag calculation block.

![](https://www.financialmodellinghandbook.org/content/images/public/images/c0799ee5-2228-4032-a816-80e741d8d7a7_2388x438.jpeg)

All using Skill 2 to create our links.

Step 3: Copy the depreciation calculations from the asset sheet.
----------------------------------------------------------------

Since the calculation structure is the same, we can reuse the block we have already created.

First copy the block on the asset sheet:

![](https://www.financialmodellinghandbook.org/content/images/public/images/5b0bc5b4-c714-4a87-abb6-f4d8326593f2_2510x884.jpeg)

Then paste it onto our Debt sheet again.

Again I'm using Ctrl+Shift+= to insert the rows and move everything down the sheet.

All we need to do next is make a series of link replacements and then re-label the calculation to "Senior debt senior debt principal repayment."

I've deleted the sigh switch for now as I'm not ready to put this straight onto the financial statements.

![](https://www.financialmodellinghandbook.org/content/images/public/images/21bed258-3f8e-48a9-a4e1-2cf4cd638c9b_2244x780.jpeg)

We will look at three possible repayment profiles. I want to be able to switch between them easily.

I'm therefore adding a block with the straight-line profile and two placeholders. Using the INDEX function, I'm setting up this block to change the profile that's feeding through to the model.

![](https://www.financialmodellinghandbook.org/content/images/public/images/861bc804-7eaf-4773-bdc4-3b5eed8ff86d_2226x1120.jpeg)

There are multiple ways to achieve this using CHOOSE, OFFSET or an IF function. I prefer INDEX for this purpose as:

*   it's simple and traceable and will return an error if I choose an impossible number (unlike OFFSET)
*   its range will stretch if I add more rows (unlike CHOOSE or a nested IF)
*   it's short (unlike a nested IF)

Step 4: Wire principal repayment into our model.
------------------------------------------------

Principal repayment will affect both sides of our balance sheet:

*   Linking principal repayment to our cash flow statement will reduce the amount of cash on the asset side of the balance sheet.
*   Linking principal repayment to our senior debt balance will reduce the amount of debt on the liability side of our balance sheet.

Wiring the principal repayment into the cash flow causes error checks to activate since our balance sheet is no longer balancing.

![](https://www.financialmodellinghandbook.org/content/images/public/images/6b1863b1-2351-4d4f-8530-ced450876c23_2912x1054.jpeg)

We sort this out quickly when we wire the principal repayment into the corkscrew and thereby reduce the liability side of the balance sheet by the same amount as we have reduced the asset side:

![](https://www.financialmodellinghandbook.org/content/images/public/images/94cb064a-c09e-4e27-84ec-6d1c93df2629_2420x708.jpeg)

Step 5: As ever, run our section completion checklist.
------------------------------------------------------

Note: when running my section completion checklist, I noted the placeholder in the debt corkscrew. As this is not a "revolving" facility, there will not be further drawdowns of the debt facility. I have therefore removed the upward flow placeholder from the corkscrew:

![](https://www.financialmodellinghandbook.org/content/images/public/images/2f42283b-0f56-4d76-a29a-367e1171826e_2354x454.jpeg)

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--82.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/debt-modelling-2-straight-line-principal#/portal/signup)
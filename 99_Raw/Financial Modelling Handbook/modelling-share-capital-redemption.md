# Modelling share capital redemption

**Source:** https://www.financialmodellinghandbook.org/modelling-share-capital-redemption

---

Setting up the redemption of share capital is very straightforward. So straightforward that we will not follow the customary "assignment/solution" structure.

We're just going to get it done.

The essential requirement is that we pay back whatever share capital is outstanding in the last period of the concession. At this stage, we will wind up the project company.

The ingredients we need are:

*   the balance of share capital and
*   the last operating / forecast period flag

The accounting will be as follows, where X is the amount of share capital outstanding in the last period (currently $100m but that could change):

*   On the asset side of the balance sheet: Cash will reduce by X
*   On the liability side of the balance sheet: Share capital outstanding will reduce by X

Before we walk through it, you guessed it; how will this move IRR?

Share capital redemption will return an additional $100m of cash to shareholders. Compared to previous versions of the model, we are now only returning this in the last period of the model. Therefore the IRR must be greater than it currently is (8.47%) but less than before we modelled depreciation (13.48%). And I expect that it will be close to the lower end of that range due to the time value of money and the negative effect of back ending the $100m of cash compared to previous profiles.

Download the start file for this assignment, and let's take a look.

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Step 1: Create the calculation block
------------------------------------

Create links (Skill 2) to the Share capital beginning balance and the Last forecast period flag.

Step 2: Create the calculation
------------------------------

Incredibly simple: A \* B

Step 3: Sign switch
-------------------

Copy the sign switch from the Tmp sheet or other handy nearby location.

![](https://www.financialmodellinghandbook.org/content/images/public/images/67c9810a-a545-41f7-931d-a724fc27f846_2452x1048.jpeg)

Step 4: Wire it up.
-------------------

The positive version of share capital goes into the corkscrew as the downward flow. This impacts the liability side of our balance sheet.

The negative version goes on to our cash flow statement. There's a placeholder there for it. This impacts the asset side of our balance sheet (by reducing cash).

![](https://www.financialmodellinghandbook.org/content/images/public/images/1b634e39-dfb6-41fe-b4ba-e96ac8baa978_3062x1182.jpeg)

Note: screenshot shows last operating period - column DH!

Our balance sheet will continue to balance.

Step 5: IRR impact
------------------

If you recalculate now, you'll notice that the IRR doesn't change.

We need to also include the $100m into the Equity IRR calculation. We left a placeholder there previously.

Once we wire it in by creating a link, we can see the impact on IRR.

![](https://www.financialmodellinghandbook.org/content/images/public/images/3f636f74-22d7-46e9-8341-26ab5651ce27_2010x840.jpeg)

The IRR increases. But not to previous levels due to the time value of money.

Step 6: Section completion checklist.
-------------------------------------

Don’t forget.

* * *

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

* * *

Review
------

We have returned the original investment to shareholders at the end of the 25 years. However, the business is still sitting on a lot of cash:

![](https://www.financialmodellinghandbook.org/content/images/public/images/1cab9f80-802f-447f-995e-3a259072959b_2408x1762.jpeg)

F11 quick chart of retained cash

Depreciation is causing earnings to be lower than cash flow by $1m in every quarter. Over 25 years this is building up to $100m of cash in the bank.

Clearly, this is quite inefficient.

Next, we are going to see if we can get that IRR back up again by introducing some leverage into our capital structure, and reducing the amount of share capital that our intrepid shareholders need to invest.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--84.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-share-capital-redemption#/portal/signup)
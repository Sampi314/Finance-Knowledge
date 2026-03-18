# Wiring up the financial statements in a financial model

**Source:** https://www.financialmodellinghandbook.org/wiring-up-the-financial-statements

---

Modelling objectives:
---------------------

*   Set up the Retained earnings and Retained cash balances;
*   Start our model build with a balancing balance sheet;

Learning objectives:
--------------------

*   Understand why retained earnings and cash are crucial to integrating the three financial statements;
*   Understand why it's helpful to model these items first - before anything else;
*   Understand that dividends affect both earnings and cash;
*   Understand why we don't yet have a timing difference between earnings and cash;
*   Start to consider what could change later to introduce a timing difference between earnings and cash.

* * *

Where to begin?
---------------

Our Start Model has the basic infrastructure that it's helpful to have in any model. But we haven't "modelled" anything yet. And so the big question is - "where do we begin"?

In theory, we could begin anywhere. We could start to model revenue; we could also just as easily start with fixed assets. Wherever we start, we will be missing ingredients. But we know we can address that by using placeholders that we can replace later.

I recommend that you start with setting up your retained earnings and retained cash balances. These two balance mechanisms are core to how the three financial statements in our model "hang together" and affect each other.

**What is retained cash?**
--------------------------

Let's start by thinking of our personal finances.

In a given month we have some income from our salary. We have various costs - rent, food, car, entertainment etc. If by the end of the month, there is money left over from our salary after paying all those costs, our bank balance will go up by the amount that's left.

It's the same in any business.

There is cash received by the business in the period, and cash is used by the business. If the cash received is greater than the cash used, the amount of cash in the bank will increase. In modelling, we call that "Retained Cash". You can think of it simply as cash in the bank.

Retained cash, being an amount of money belonging to the business, we'll appear on the "Asset" side of the balance sheet.

Let's look at the structure of our cash flow statement:

![](https://www.financialmodellinghandbook.org/content/images/public/images/4f8b2967-f64c-4002-89f6-6b99eeaa328a_1356x1018.jpeg)

This is a "Financing cashflow" layout, also known as a Cashflow Waterfall. It's helpful for modelling as it shows the hierarchy of payments. We'll see more of this cash flow statement layout in later volumes of the Handbook when we look at Project Finance and Corporate Finance modelling.

We start with cash inflows from customers, and then we have various outflows. The fact that "Cashflow available for dividends" is at the bottom of the cash flow statement reflects that equity typically gets paid last.

The business could distribute any cash left it has paid all other costs as a dividend to shareholders. If we don't pay it out as a dividend, the only place that cash can go is into the bank.

**What is retained earnings?**
------------------------------

Retained cash is real. It's actual honest to god money in the bank.

Retained earnings is slightly more conceptual.

Let's look at the structure of our income statement.

![](https://www.financialmodellinghandbook.org/content/images/public/images/c5878d60-5a5e-4ee1-afc8-914a06bacf34_1396x644.jpeg)

There are a few differences between the line items on our income statement and the line items on our cash flow statement. We'll cover these differences later.

For now, we can say that, just like our cash flow statement, our income statement deals with flows of value passing through the business in a given period.

We start with revenue, then gradually deduct costs until we get down to Profit After Tax. If there is any profit left after tax has been paid, the only remaining place it can go is to pay a dividend to shareholders.

If we choose not to pay a dividend, what happens to that profit?

Just like our "Cash Flow Available for Dividend", if we don't distribute the Profit After Tax to shareholders, we "retain" it in the business. Whereas leftover cash goes into "Retained Cash," i.e. cash in the bank, excess undistributed profit will go into "Retained earnings".

Retained Earning is the balance of earnings, or profit, that we have not _yet_ distributed. The business exists to make a profit for its shareholders. Therefore any profit that the company has not yet distributed to shareholders is a liability on the balance sheet; it is profit that the business "owes" to the shareholders. It will likely be required to distribute in the future.

For this reason, Retained Earnings is on the liability side of the balance sheet. It is money owed to Shareholders.

Setting up our Retained Cash and Retained Earnings balances.
------------------------------------------------------------

### Step 1: Use a placeholder to add some numbers onto the income and cash flow statements.

It's helpful to deal with some actual numbers. Since we have not yet modelled revenue or cash receipts, let's use placeholder values to get started.

I'm adding 100 in every operating period as a placeholder on the financial statements to give us some actual numbers to play with.

![](https://www.financialmodellinghandbook.org/content/images/public/images/6e246a13-9286-4166-8005-cc18f5b2a362_2292x950.jpeg)

Since we don't have any costs, the 100 of "revenue" in each period drops straight to Profit After Tax.

I have added $100,000 in each period. We have a quarterly model running for 25 years. Therefore the total revenue we have added is $10,000,000. Remember that the Standard Monetary Unit in our model is USD 000s.

Doing the same on the Cashflow statement, the 100 of "cash received" in every period drops straight to "Cashflow available for Dividend" since we have not modelled any cash outflows.

![](https://www.financialmodellinghandbook.org/content/images/public/images/af54993d-7c76-4c21-baaf-94c981f85b36_2280x962.jpeg)

If we add the same amount of cash inflow at the top of the income statement, we can see that USD 10,000,000 also drops straight "Cashflow available for dividend" since we have not modelled any other costs at present.

At present, thanks to the placeholders we have set up, revenue and cash received are the same in both amount and timing. In reality, many businesses experience a timing lag between when invoices are issued and paid. When we come back to model this shortly, we will not see the same numbers on the income and cash flow statements.

### Step 2: Set up a new sheet called "Equity"

Core Skill 9: How to set up a new worksheet

### Step 3: Set up two new balance corkscrews

If you copied the Tmp sheet, you already have a corkscrew "for free" on the sheet.

Core Skill 8: How to set up a new balance corkscrew

We will call the first corkscrew "Retained earnings" and the other "Retained cash".

![](https://www.financialmodellinghandbook.org/content/images/public/images/4ea95bbb-af9e-4171-81f5-275e8e5c4b7a_2206x1102.jpeg)

### Step 4: Flow Profit After Tax as the upward flow in the Retained earning balance.

Core Skill 2: How to create a link

![](https://www.financialmodellinghandbook.org/content/images/public/images/1832617a-7a7e-4b52-ac80-ceae7f606a4d_2174x1130.jpeg)

### Step 5: Flow Cash available for dividends as the upward flow in the Retained cash balance.

Core Skill 2: How to create a link

![](https://www.financialmodellinghandbook.org/content/images/public/images/0abbdf2a-3d56-4974-8157-414cf92ead1c_2162x1062.jpeg)

### Step 6: Rename the downward flow for each corkscrew as "Dividends paid".

Core skill 3: How to create a placeholder.

![](https://www.financialmodellinghandbook.org/content/images/public/images/c0689c81-0c82-4a1f-8869-8e668c36a2ab_2388x1082.jpeg)

### Step 7: Add the closing balances for Retained Cash and Retained earnings onto the balance sheet.

![](https://www.financialmodellinghandbook.org/content/images/public/images/1a739021-bedc-46d3-9c47-4479ed0ef23f_2628x1248.jpeg)

### Step 8: Review

We now have our financial statements' core "plumbing" in place. Net cash flow in the period flows into our bank account and appears on the asset side of our cash flow statement. Undistributed earnings flow into our Retained Earnings balance and appear on the liability side of our balance sheet.

Net cash flow and undistributed earnings are currently the same value. This is causing the asset and liability side of our balance to increase by the same amount. This means that our balance sheet continues to balance in every period.

What would we expect to see if we chart our retained earnings or retained cash balance?

We have already seen that our total Profit after tax is $100m. And it's going up by the same amount every period.

We'd therefore expect to see Retained earnings going up in a straight line until it reaches $100m.

Use Skill 11 to create a quick chart and test the hypothesis.

![](https://www.financialmodellinghandbook.org/content/images/public/images/306a3c5e-56e9-410c-9558-31efd1d687bc_2508x1826.jpeg)

We can also see several change alerts on our output sheet. Now that we have added some values, our live values are different from our stored values. We'll leave this for now until we have some line items modelled then we will start to track our changes.

![](https://www.financialmodellinghandbook.org/content/images/public/images/69d10cb0-614e-4405-b949-9c8afc797a2d_2192x1346.jpeg)

* * *

Download the model complete to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--147.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/wiring-up-the-financial-statements#/portal/signup)
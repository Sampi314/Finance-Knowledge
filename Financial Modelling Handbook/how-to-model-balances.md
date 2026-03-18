# How to model balances

**Source:** https://www.financialmodellinghandbook.org/how-to-model-balances

---

Every line item in your model is either a flow or a balance.

You can think of a flow as an amount of value passing through the business during a period. You can think of a balance as an amount of value in the business at a point in time. The time in question is usually the start or the end of a period.

A bathtub analogy is helpful here.

![](https://www.financialmodellinghandbook.org/content/images/public/images/8c19e3f5-f717-4f45-9d10-451a52aeb0ea_512x512.png)

Water flows into the bath from the tap (or faucet for our North American readers). It flows out through the plughole in the bottom. The amount of water in the bath is the balance at any given time. The rates of flow in and out of the bath will impact the balance.

All balances share these same features.

There is an amount of the balance at the start of the period. There can be upward or downward flows during the period. And as a result, there is an amount of balance at the end of the period.

Because all balances share the same features, we model them all in the same way.

We use a standard calculation block structure called a corkscrew.

Download the worked example file for this chapter:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

The basic corkscrew calculation block has four lines. The first line shows the balance at the beginning of the period. Then there is an upward flow, a downward flow, and the resulting balance at the end of the period.

![](https://www.financialmodellinghandbook.org/content/images/public/images/e7a0b8da-2c0d-4fe3-ae05-abb6dfe572b9_2996x914.jpeg)

Every balance you can think of has a flow that makes it go up and a flow that makes it go down.

### Accounts receivable?

*   Upward flow: Revenue/invoices issued
*   Downward flow: Cash received / invoices paid

### Debt?

*   Upward flow: Debt drawdowns
*   Downward flow: Debt repayment

### Fixed assets?

*   Upward flow: Capex
*   Downward flow: Depreciation.

Why it's called a corkscrew
---------------------------

The beginning of period balance is always equal to the closing balance from the previous period.

The end of period balance equals the beginning of period balance, plus the upward flow, less the downward flow.

If we trace dependents on the beginning and ending balances, the flow looks like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/48f5cc1f-4eaf-4db8-852d-e449d5552d2f_3038x832.jpeg)

The name "corkscrew" comes from this period by period winding logic flow.

Calculate the balances, not the flows.
--------------------------------------

The purpose of the corkscrew is to calculate the balance. Its purpose is not to calculate the flows. We should never calculate the flows in the middle of the corkscrew. Flows should be calculated in separate calculation blocks and then fed into the corkscrew

Sometimes, the flow depends on the balance.
-------------------------------------------

It does. And when this happens, the appropriate balance (often the opening balance) should be linked to the calculation block where we calculate the flow. See the example below. In working capital calculations, the flow is an ingredient in calculating the balance. (Don't worry about what's going on here - we'll get into working capital calculations in specific detail later in the book).

**Balance labelling**
---------------------

A simple rule that we should always follow in our labelling is that no two line items should have the same label. We, therefore, have to label our balances differently. Accountants use "brought forward" and "carried forward". I often see modellers use this abbreviated to "bf" and "cf". This can be hard to notice and introduces the risk of linking to the wrong one later.

![](https://www.financialmodellinghandbook.org/content/images/public/images/e8a67a6e-c441-4f6a-b345-2635dfaf2ffe_2298x370.jpeg)

You'll notice in our labelling that the beginning balance has "BEG" added to the label. The closing balance has nothing. This is because we will link the closing balance to our financial statements. Our balance sheet will only contain links to closing balances at the bottom of corkscrews throughout the model. We, therefore, want them to be presentable. The beginning balances will only ever be in our model's "engine room". While we will use them to drive other calculations, they won't appear on financial statements. We use a big ugly label to instantly know if we are looking at or linking to a beginning of period or end of period balance.

Descriptive labels
------------------

You may be tempted to save a little time and just label the rows "Opening balance" or "closing balance". Don't. Always include reference to the specific name of the balance. You will have many balances in a typical model. It's not helpful if they are all called "balance". I'm surprised at how often I see this, even in professionally built models.

The opening balance is always the closing balance from the previous period.

Never give in to the temptation to screw with the opening balance. It will trip you up later. See Chapter X on technical debt.

Column I
--------

Our opening balance row is always looking back one period. Did I mention that the opening balance should always be the closing balance from the previous period? Column I exists in the model to allow this look back even in the first timing column. It's a small, narrow, empty column that just exists to enable the look to back in corkscrews to happen consistently across the timeline, without risk of pointing at a label or a row total or whatever junk you feel like putting on the left-hand side of your model.

![](https://www.financialmodellinghandbook.org/content/images/public/images/a93ec0f2-d718-4af6-b481-4e27c4a42dae_2316x374.jpeg)

Column D labelling
------------------

You may notice at this point that the downward flow is a positive number. As we'll discuss later, all of the numbers in the calculation area of our model are positive by default. We'll talk more about this in Chapter X and explain why we keep all numbers positive by default in the calculation sheets of the model.

Since all numbers are positive, it’s not always clear when we are adding and subtracting rows in calculation blocks. Column D exists to allow helper labels, as you see below. This is not essential, and in all honesty, I often forget.

![](https://www.financialmodellinghandbook.org/content/images/public/images/32324b24-82f5-4470-acd4-7fe91053efaf_2850x420.jpeg)

Borders
-------

Corkscrews are not "standard" calculation blocks with a group of links followed by a calculation. We put borders around corkscrews so that they are immediately visually identifiable. We can add borders to a block by selecting the block, then pressing Ctrl+Shift+d. This keystroke is from the Productivity Pack and will add top and bottom borders to the selected block of cells.

Dealing with an "initial balance" - the 7 line corkscrew
--------------------------------------------------------

The 4 line corkscrew assumes that we are starting from a zero balance at the start of the model. This is like assuming that we start filling the bath from empty. If we are filling a water container, there could already be some water in the container before we start. The same is true of balances.

For example, if we are modelling an acquisition, there could already be some receivables on the books. This would be an initial balance at a point in time, separate from the period by period flows being modelled.

The seven link corkscrew adds two new ingredients. One is "how much", one is "when". The "how much" ingredient is the initial balance. The "when" ingredient is a flag telling the corkscrew to "inject" the initial balance. In many of our models, we inject the initial balance into the closing balance line, but it is possible to inject it into the beginning balance if required.

![](https://www.financialmodellinghandbook.org/content/images/public/images/39971da7-05e8-4a6b-bc59-dbe776991e9a_2972x960.jpeg)

You can see here that rather than just being equal to the beginning balance plus the upward flow less the downward flow, the 7 line corkscrew contains an IF statement in calculating the closing balance. This IF statement says that if it's the correct date to recognise the initial balance, do so, otherwise let the closing balance be equal to the beginning balance plus the upward flow, less the downward flow as before.

In [Core Modelling Skill 8](https://www.financialmodellinghandbook.org/adding-a-balance-corkscrew/)
 we will look in detail at how to build a new corkscrew in seconds each time you need one.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--118.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/how-to-model-balances#/portal/signup)
# Modelling debt - concepts and assignment

**Source:** https://www.financialmodellinghandbook.org/modelling-debt-concepts-and-assignment

---

There is information in the case about the "Senior Debt" that is available for the project.

Firstly, what on earth do we mean by  "Senior debt"?
----------------------------------------------------

In highly structured & leveraged transactions, as we would see in Project Finance, there can be multiple "layers" of debt. These layers are arranged into a hierarchy. The hierarchy determines the priority of payments. Senior debt holders will be paid first, before junior debt holders. Junior debt holders will be paid before equity. This prioritisation of payment affects the cost of the debt. Since senior debt has priority over other capital providers, it represents lower risk capital and is, therefore, cheaper than junior debt. Similarly, junior debt is cheaper than equity.

What information do we have about the debt?
-------------------------------------------

We have the following information in the case about the debt financing for the project:

*   We don't yet have complete information on the credit package but believe the project will be around 70% debt-financed
*   The project has entered into a long term interest rate swap at 2.5%. There will also be a margin of 3.8% per annum. The total cost of debt is equal to the interest rate swap plus the margin. We will go into more detail on interest rate swaps at a later date.
*   We will calculate interest using an actual / 360 day count convention

Debt modelling can involve a lot of complexity. We will unpack some of that complexity in future volumes of the handbook. Modelling debt always comes down to dealing with these four topics:

*   Modelling the debt balance. Corkscrew at the ready.
*   Modelling the debt drawdown (the upward flow in the balance corkscrew)
*   Modelling the debt repayment (the downward flow in the balance corkscrew)
*   Modelling the debt interest. Always modelled as an interest rate multiplied by a balance.

In future volumes of the handbook, we will unpack this topic in much more detail.

The notes below will help you get started with each of these elements. As usual, we'll walk through them one by one in the next chapter.

Step 1: Modelling the debt balance
----------------------------------

*   Copying the Template sheet to create a new debt sheet will give you a corkscrew in place already.
*   Relabel the upward flow and the downward flow.

Step 2: Modelling the debt drawdown
-----------------------------------

*   Some debt structures allow one initial drawdown or several initial drawdowns during an "availability period" and then a defined repayment period during which no further drawdowns are possible. Your domestic mortgage is like this; it's not a facility you can continue to tap into when you need cash.
*   Other facilities can be drawn continuously, like a personal credit card or overdraft.
*   In this case, the debt is made available in one drawdown at the transaction date. We can use the "initial balance" structure in the corkscrew to bring this drawdown into the corkscrew.
*   We will first calculate the drawdown using a 70% input multiplied by the $100m total project cost amount.
*   If you put this balance onto the balance sheet, you will find that your balance sheet is now unbalanced by $70m in every period. This is because we will also need to adjust our share capital drawdown to take into account the amount of the debt now being used to finance the project.

Step 3: Modelling the debt repayment
------------------------------------

There are several different possible profiles of debt repayment.

The case simple tells us that the debt is repaid quarterly. We are going to consider three possible repayment profiles:

*   Straight-line - with equal principal repayments in every quarter
*   Amortising - with equal debt service in every quarter. "Debt service" is what we call the combined payment of interest and principal.
*   Sculpted - where we vary the principal repayments to align with the cash available in each period.

We will begin with level principal repayment. To model this, we divide the amount of debt by the number of periods and show the same principal amount in each period. This is the easiest to model but, as we'll see, may not be the most economically advantageous for the business.

Step 4: Modelling the debt interest
-----------------------------------

*   We always model debt interest as an interest rate multiplied by a balance. While this seems simple, there can be complexity around what rate to use and which balance.
*   There are whole books & financial qualifications around interest rate conventions and calculations.
*   For now, it's enough to know that debt interest is usually calculated with reference to a "day count convention". This is used to derive a "period interest rate" (i.e. a quarterly rate) from an annual rate.
*   With an actual / 360 day count convention, to determine a quarterly rate from an annual rate, we would divide by 360 and multiply by the number of days in the year.
*   There is also complexity around which balance to use in the interest rate calculation. This is a function of the timing of the principal repayment. In our case, the debt principal and interest are paid at the end of each quarter. There are no payments within the quarter. Therefore the debt balance at the beginning of the quarter is the balance in place for the whole of the quarter. Therefore the opening balance is the appropriate rate to use for calculating interest. If the business were making debt repayments within the quarter, this would not be the case.

Download the start model for this lesson and get started.  
_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--83.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-debt-concepts-and-assignment#/portal/signup)
# Accounts Receivable - assignment

**Source:** https://www.financialmodellinghandbook.org/accounts-receivable-assignment

---

* * *

**Note: This lesson begins from the completed model from the Revenue section:**

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

This section gives you some useful notes and pointers to help you start modelling Accounts Receivable.

If you are feeling brave, take a run at modelling it without reviewing these notes.

If you get stuck, first check the notes. As a last resort, look at the solution in the next chapter.

**1 Accounts receivable is a balance**
--------------------------------------

You immediately know as soon as you hear that you're modelling a balance that you need a corkscrew.

Use Skill 8 to create a corkscrew.

Think about what you should name the upward flow and downward flows in the balance corkscrew. If you don't know, go back to the last chapter and figure out what makes Accounts receivable increase and what makes it decrease.

**2 The three key numbers you need to model**
---------------------------------------------

For this section, your target is to model these three line items:

*   Revenue
*   Accounts receivable balance
*   Cash received.

You already have Revenue.

Either forecast the accounts receivable balance and use it to calculate cash received. Or forecast the cash received and use it to calculate the Accounts Receivable balance.

Abbreviations:

ARn = Current period Accounts Receivable balance

ARn-1 = Previous period Accounts Receicable balance

ARdays = Accounts Receivable days

D = Days in Period

R = Revenue

CFr = Cashflow from current period invoices

CFn = Total cashflow for the period

#### **Method 1: Inferring cash flow from the Accounts Receivable balance.**

To approach the modelling this way, first calculate the forecast accounts receivable balance. Then use that balance to infer the current period cash flow.

You will need two calculation blocks:

Calculation 1: ARn = R / D \* ARdays

Calculation 2: CFn = R - ARn + ARn-1

You may be tripped up here by the need to include the previous period's Accounts Receivable balance (ARn-1) in the calculation. Hint: this is the opening balance - you therefore already have this line item in your corkscrew)

#### Method 2: Inferring the Accounts Receivable balance from the cash flow

You can also begin by forecasting the amount of cash collected from the invoices issued in the current period. You can then use that to calculate the total cash received. Again you'll need the previous period's Accounts Receivable balance.

You will still need two calculation blocks:

Calculation 1: CFr = R / D \* (D - ARdays)

Calculation 2: CFn = CFr + AR(n-1)

I have shown both methods in the solution case model.

3 Wiring up the financial statements.
-------------------------------------

You will need to:

*   link the cash received through to the cash flow statement.
*   link the accounts receivable balance to the balance sheet.

When you recalculate the model, you should find that the balance sheet now balances. We are now correctly accounting for the timing difference between Revenue and cash received from invoices.

4 Direct vs indirect cashflow
-----------------------------

We have put the cash received number directly onto the cash flow statement. When we connect the cash flow like this, it's known as a Direct cash flow. Later in the book, we will come back to look at Indirect cashflows, where we start from Income Statement items and make adjustments.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--145.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/accounts-receivable-assignment#/portal/signup)
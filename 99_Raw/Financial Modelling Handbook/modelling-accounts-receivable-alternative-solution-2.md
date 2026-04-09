# Modelling accounts receivable - alternative solution 2

**Source:** https://www.financialmodellinghandbook.org/modelling-accounts-receivable-alternative-solution-2

---

We frequently have to model situations where we have material differences in payment lag for different customers or different products.

The solution for this bonus chapter is available in the file pack you'll receive when you [purchase the handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
. See file _4.54 FMH AR ALT2 END 01a._

We're maintaining the assumption that we set up in our previous tutorial that the accounts receivable delay is longer than the model timeline. We have a monthly model, with invoices being paid over four months.

The data we need here is a profile of when, typically, invoices are paid. For the sake of this example, I've broken this down with broad %s. This could be a per customer or per product type calculation that you need to do.

I've used the same structure to model the initial balance profile. The input assumptions are different because we have a longer and profiled payment lag.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/1-17.jpg)

The more significant difference is in the profiling of forecast cash receipts.

The underlying function used is the same as our previous example, using XLOOKUP to implement the delay.

We are now using a bigger "2D" block to cascade the calculation and apply the different %s.

In each row, from rows 72 to 77, we apply a different payment lag, from one to six months, using the same XLOOKUP structure as before. We then multiply this amount by the % of invoices paid with that payment lag.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/2-12.jpg)

You could adapt this calculation so that the inputs gave the % of revenue and payment lag for a series of customers or product types. I've applied it to all revenue.

In row 78, we add up each of the profile receipts lines. Here, the row totals are crucial information, assuring us that the total receipts add up to the forecast revenue.

From there, we add the forecast receipts to the profile of initial balance receipts to give us the total cash received from invoices. We flow this into the cash flow and corkscrew as before.

As this calculation is more complex, there is a greater risk of error. We may therefore want to add an error check to this calculation to ensure that the total invoice receipts is equal to total revenue. We'll come back to this when we look at error checks later.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero-4.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-accounts-receivable-alternative-solution-2#/portal/signup)
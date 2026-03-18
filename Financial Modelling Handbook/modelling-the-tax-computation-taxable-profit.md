# Modelling the tax computation - taxable profit

**Source:** https://www.financialmodellinghandbook.org/modelling-the-tax-computation-taxable-profit

---

Now that we have our helpful Tax memo, we can model the Tax payments for Aurelius Power.

When we calculate Taxable profit, it's common to start from Profit Before Tax, add back the accounting items that are not deductible for tax purposes, then deduct the accounting items.

Although this can seem a little long-winded, it gives anybody reviewing the model a clear view of how you have handled these items.

Our calculation will therefore be:

Profit Before Tax  
plus: Accounting Depreciation  
plus: Senior Debt Interest  
less: \[Tax depreciation\]  
less: \[Allowable interest deduction for tax\]  
equal: Taxable profit / (Tax losses arising)

![](https://www.financialmodellinghandbook.org/content/images/2022/02/1.jpg)

We will placeholder the last two items as we have not yet calculated those. I'm already preparing to deal with tax losses by labelling that a negative number in this calculation means that we have a tax loss.

Note that in the company's actual tax disclosure, the computation would be: to _add back the disallowed interest_ rather than add back all interest and claim the allowable interest. It gives the same result as what we have now, but in practice what we have done would be done in a separate working.

OK - let's press on with calculating Tax Depreciation.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--168.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-the-tax-computation-taxable-profit#/portal/signup)
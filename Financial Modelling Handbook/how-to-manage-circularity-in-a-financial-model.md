# How to manage circularity in a financial model

**Source:** https://www.financialmodellinghandbook.org/how-to-manage-circularity-in-a-financial-model

---

Circular models will not calculate. Therefore if you have a circularity in your model, there are three main options.

Option 1: Switch on iterative calculations.
-------------------------------------------

You'll find this under Options / Formulas. What we're doing here is asking Excel to continue to calculate until the values converge on a solution. We tend to avoid this option.

There are a few reasons for this:

*   Excel will warn you the first time you introduce a circularity. If you introduce a second circularity, you will not receive any warning. But each additional circularity will slow down your model.
*   Using iterative calculation to resolve a circularity requires a convergent solution. This is not always the case, and so you can have a model that does not converge on a stable output. Every time you calculate the model, you get different results.
*   Activating iterative calculations happens at the application level, meaning that all open workbooks will run in iterative mode.
*   You have to keep activating iterative calculations every time you open the model.

Option 2: Find an algebraic solution.
-------------------------------------

This is sometimes possible, but not always. If possible, this is the preferred option, as it will remove the circularity from Excel.

Option 3: Create a "copy/paste" macro that breaks the circularity.
------------------------------------------------------------------

This is the option we will look at to break the circularity in our model.

There is a fourth option which is to create a User Defined Function. Ed Bodmer has written about this and has many excellent resources on this website which I highly recommend. You'll find his work at [https://edbodmer.com/](https://edbodmer.com/?ref=financialmodellinghandbook.org)

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--124.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

  

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
Subscribe](https://www.financialmodellinghandbook.org/how-to-manage-circularity-in-a-financial-model#/portal/signup)
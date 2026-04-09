# Q&A: Why does my balance sheet not balance when I introduce an RCF balance?

**Source:** https://www.financialmodellinghandbook.org/q-a-why-does-my-balance-sheet-not-balance-when-i-introduce-an-rcf-balance

---

_Hello, I thank you very much for your work teaching us with great precision the financial modelling tools. I have a question : The initial RCF balance is currently 0 in the model, but if I put an initial RCF balance of 10,000, then it will have an imbalance on the balance sheet of 10,000, in the liabilities. So is there an error in the assets that seem to not be linked to inital RCF balance. Best regards, Adrien_

* * *

Hi Adrien,

Thanks for your question on [modelling a revolving credit facility](https://www.financialmodellinghandbook.org/revolving-credit-facility/)
.

I think your model is reacting exactly as expected. If you enter an initial balance of 10,000 on the RCF, you have created a liability with no corresponding balancing elsewhere on the balance sheet. Therefore your liabilities will be 10,000 more than your assets. Your balance sheet won't balance - but that's as it should be.

If you draw down on any debt facility, you will increase your cash by that amount. The mechanism for the RCF, as it's been modelled in the examples given, is that it's drawn to meet any cash shortfall you may have. And so, the "balancing entry" will be an increase in cash equal to the amount of the debt draw. This is effected in your model by increasing the debt balance by the amount of the drawdown and flowing the drawdown onto the cash flow statement, which increases the cash balance, and keeps the balance sheet balanced.

Does this help?

Best

Kenny    

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--38.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/q-a-why-does-my-balance-sheet-not-balance-when-i-introduce-an-rcf-balance#/portal/signup)
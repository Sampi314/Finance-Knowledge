# Q&A: Row anchoring in calculations

**Source:** https://www.financialmodellinghandbook.org/q-and-a-row-anchoring-in-calculations

---

_Hello Kenny,_

_While calculating the electricity generation revenue, why did we not fix the complete cell reference for power tariff and units in thousand and instead just fixed the column reference? Why didn’t we use $F$29 instead of $F29? Thanks, Shreyal_

* * *

Hi Shreyal,

is a great question. It would be easier just to hit F4 once!

However, we want to build our calculation blocks so that if we need the same kind of calculation again, we can just copy the block. If we row anchor references within our calculation (whether that's to constant or series items), we cannot copy the calculation block easily since the calculation will continue to refer to the ingredients in the old block.

I explain this in a bit more detail here:

[The Financial Modelling Handbook Core modelling skill 7: Copying a calculation block](https://www.financialmodellinghandbook.org/copying-a-calculation-block/)

Let me know if this makes sense and answers your question. Best Kenny

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--160.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/q-and-a-row-anchoring-in-calculations#/portal/signup)
# Q&A: Why does copy across stop?

**Source:** https://www.financialmodellinghandbook.org/q-a-why-does-copy-across-stop

---

_Hi Kenny,_

_I can successfully create links for "Compound degradation" and "seasonality adjustment". However, in both cases, when I click Ctrl + Shift + a, the macro only copies across the next two columns (which are the constant and unit columns). When I enter the formula for electricity generation and use Ctrl + Shift +a, the macro has no problem copying the formula across the entire timeline. The problem only arises with the two inputs._

_Any suggestions, please._

_Many thanks, Richard_

Hi Richard,

Thanks for the question.

This is by design! Remember that there are [two types of line items in a model](https://www.financialmodellinghandbook.org/the-building-blocks-of-a-financial-model/)
 - everything is either a constant or a series. With constants, there are only three "components"; the row label, the value, and the unit. Therefore the copy across macro is set up to be aware when you are linking to a constant and stop after the unit. There's no need for additional blank links all the way across the timeline. This also helps with making constants more easily visible.

See this demo of creating a link to a constant input, vs creating a link to a series input. In both cases I have used Ctrl+Shift+q to create the link and Ctrl+Shift+a to copy across:

![](https://www.financialmodellinghandbook.org/content/images/2023/01/1.gif)

ca

Does this help?

Best

Kenny

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--36.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/q-a-why-does-copy-across-stop#/portal/signup)
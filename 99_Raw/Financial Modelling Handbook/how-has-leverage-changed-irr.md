# How has leverage changed IRR?

**Source:** https://www.financialmodellinghandbook.org/how-has-leverage-changed-irr

---

Download the start file for this section:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

By funding 70% of the project with cheaper capital, we have decreased the weighted average cost of capital. We should therefore see an increase in the Equity IRR.

When I look at the output sheet, that's not what I'm seeing:

![](https://www.financialmodellinghandbook.org/content/images/public/images/092a9e9d-75e2-44b8-8782-4e42db9684f7_2352x646.jpeg)

Why is this?

**Take a few minutes to review the model and formulate your hypothesis as to why IRR has gone down when we introduced leverage.**

You may want to write your hypothesis down to keep you honest.

Read on below when you’re ready.

* * *

Remember - if we get a result that runs contrary to our hypothesis either:

*   a. our understanding of the dynamics of the model is flawed
*   b. there is an error in the model

In this case, if our hypothesis is wrong, it would mean that decades of Corporate Finance theory is also mistaken. In this case, I think it's more likely that our model is wrong.

Looking at our IRR calculation, we can see the cause of our error.

![](https://www.financialmodellinghandbook.org/content/images/public/images/0ffc32aa-cd08-46d5-9b90-5ba2259f0a51_2430x890.jpeg)

The IRR calc still assumes $100m of capital invested while now showing only $30m of capital being returned to shareholders. Dividends are also lower due to cash being used to pay debt principal.

We can correct this by replacing the link to the $100m initial share capital input to our calculated value after we deduct the amount funded by debt:

![](https://www.financialmodellinghandbook.org/content/images/public/images/a369f54c-0ba1-455f-82a4-ec0e49300aae_2242x898.jpeg)

The makes quite a dramatic difference.

Clearly, this IRR is overstated since we have not yet modelled debt interest, and so effectively, the cost of debt in our model at present is zero. That would, of course, give very impressive equity returns.

Sadly, the cost of debt is never zero. So let's turn now to modelling interest.

* * *

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--136.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/how-has-leverage-changed-irr#/portal/signup)
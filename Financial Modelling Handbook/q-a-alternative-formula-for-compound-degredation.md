# Q&A: Alternative formula for compound degradation

**Source:** https://www.financialmodellinghandbook.org/q-a-alternative-formula-for-compound-degredation

---

_Hello there,_

_My understanding of degradation is that the first year we operate at 100% capacity and then we loose each year the percentage capacity that is in cell F10. If this is correct i came up with another formula:_

_J12\*(1-(J11-1)\*$F$10)_

_So this basically is the time flag multiplied by 100% - (the year operating-1)\*degradation._

_In first year we have 100%-(1-1)0,05%=100% Year 2 100%-(2-1)\*0,05%=99,50% and on_

_Is this correct or not ? At the end i have a slight difference in electricity revenue, mine are at 370 419 000._

_Othman_

* * *

Hi Othman,

Thanks for this. Always good to test things out for yourself and make sure you're happy with how the formula is working. With your formula, you are deducting a constant amount each year. i.e. performance is reducing at a steady rate of 0.05% per annum. In the formula I've used, performance is reducing by 0.5% of the previous period's performance. This means that over time, my formula will give a slightly higher level of performance than yours since the amount of the reduction is decreasing over time. This is due to my calculation taking 0.5% of a smaller number each time. Does that make sense?

See this chart comparing the results over time. My formula is the red line, yours is the blue - and I've extended the time period to show the difference better:

![](https://www.financialmodellinghandbook.org/content/images/2023/01/1-2.jpg)

The formula I've used is labelled "Compound degradation" to make it clear that this is a "compounding" rather than linear effect.

Hope this helps!

Best

Kenny

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--39.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/q-a-alternative-formula-for-compound-degredation#/portal/signup)
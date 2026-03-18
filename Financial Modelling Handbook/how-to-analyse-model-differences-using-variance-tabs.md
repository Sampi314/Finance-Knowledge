# How to analyse model differences using variance reports

**Source:** https://www.financialmodellinghandbook.org/how-to-analyse-model-differences-using-variance-tabs

---

For example, let's say we use the sample model from this chapter to test the impact of changing from sculpted to straight-line debt repayment.

![](https://www.financialmodellinghandbook.org/content/images/2022/04/1.jpg)

The output sheet tells us that the IRR will reduce by 55 bps. This is valuable information, but often we need more detail to understand why output numbers are changing.

The variance tabs can help us with this kind of analysis.

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

* * *

How to use the variance tabs
----------------------------

### 1\. Run the model in the "start case". In our model, that's the case with sculpted debt repayment.

It's worth ensuring that you have an output track saved in this case so that you can also compare differences at a high level.

### 2\. Select the rows you want to analyse in more detail to understand the delta caused by the input or scenario change.

In our case, we want to examine the impact on the shareholder cashflows.

![](https://www.financialmodellinghandbook.org/content/images/2022/04/2.jpg)

### 3 Run the Variance tabs macro

Ctrl+shift+9

Two new sheets will be added to your model. Each will carry the original sheet name, plus a suffix:

![](https://www.financialmodellinghandbook.org/content/images/2022/04/3.jpg)

**Ref** \- this contains a hard-coded copy of the lines you selected at the previous step. Similar to the way the output sheet works, this provides our reference data for the model as it currently is.

**Var** - this contains a calculation comparing the "live" line items you initially selected with the hard-coded Ref version.

### 4 Change to the scenario you wish to compare.

In our case, we want to switch to straight-line debt repayment, which we do on the Input sheet in row 47

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/4.jpg)

Once we recalculate or resolve the model, the Ref sheet shows how our selected rows have changed.

Importantly we can see these changes over time. It provides valuable additional analytical data to help us better understand the output changes.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/5.jpg)

It can be helpful to chart these changes. For example, the profile of equity cashflow differences due to the change in debt sculpting looks like this:

![](https://www.financialmodellinghandbook.org/content/images/2022/04/6.jpg)

We can also do additional analysis using the calculated delta lines. For example, it can be helpful when looking at equity cashflows to look at the cumulative differences over time:

![](https://www.financialmodellinghandbook.org/content/images/2022/04/7.jpg)

In this case, we can see that while total dividends are higher when we apply straight-line debt repayment, the cumulatively equity cashflows are lower in the early periods. This paints a much clearer explanatory picture of why the IRR is lower with straight-line debt repayment.

The variance tabs are handy for testing our explanatory hypotheses about changes in the model.

* * *

Download the end file for this section:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--60.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/how-to-analyse-model-differences-using-variance-tabs#/portal/signup)
# Modelling the tax computation - thin capitalisation

**Source:** https://www.financialmodellinghandbook.org/modelling-the-tax-computation-interest-deduction-thin-capitalisation

---

Companies are financed with a mixture of debt and equity. This financing is also sometimes referred to as the company's "capitalisation"

Thin capitalisation refers to the situation where a company has a high level of debt compared to its equity.

Since interest is often deductible for tax, companies can potentially lower their tax bill by maximising interest.

For example, owners can provide company debt in the form of shareholder loans. Where this is the case, owners can set the interest rate on this debt. A high interest rate, were it all deductable, would mean a lower tax bill.

Thin capitalisation rules, or "thin cap rules" as they are sometimes called,  refer to restrictions placed on companies around the deduction of interest for tax purposes. Thin cap rules are one type of interest restriction, but there are other types.

Jurisdictions structure their thin capitalisation rules differently. Some places, a debt to equity limit and only allow interest deduction below a certain level. Some specify a percentage of interest that companies can deduct. Others set a maximum allowable rate of interest.

Let's assume that we've found that in our fictional jurisdiction, there is a thin capitalisation restriction based on a debt to equity ratio of 2 to 1. The debt charged on interest above this ratio cannot be charged.

Example
-------

If we have equity of 100 and debt of 300, we have a debt to equity ratio of 3x.

Since the maximum debt to equity ratio for interest deduction is 2x, we can only deduct interest on 200 worth of debt. This means that 66% of the debt interest (200 / 300) is not deductible.

For the capitalisation calculation, we can include retained earnings in our definition of equity.

Let's see how this looks in the model.

Download the start file for this section:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Step 1: Calculate total equity
------------------------------

WE need links to both the share capital and retained earnings balances. The quickest place to get those is off the balance sheet!

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/1-2.jpg)

We can then add those up to calculate total equity.

Step 2: Calculate maximum debt given thin cap ratio.
----------------------------------------------------

First, I'll add the ratio as an input and multiply it by the calculated equity balance.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/2-1.jpg)

Step 3: Calculate maximum debt as % of actual debt
--------------------------------------------------

  
We can only deduct interest that relates to the maximum allowable debt. Therefore, my next step is to calculate maximum debt as a % of the actual debt.

For this calculation, we need the debt repayment period flag. If we don't limit the calculation using this flag, we'll get a DIV/0 error when we divide by the periods in which there is no debt.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/3-1.jpg)

At this point, it's worth a quick check of the calculation to see what it looks like.

Another F11 quick chart is helpful here.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/4-1.jpg)

  
We can see that we pay down the debt, the allowable debt size starts to become much larger as a % of the actual debt. We can only deduct up to a maximum of 100% of the debt. We will therefore introduce this as a constraint in the calculation.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/5-1.jpg)

Charting shows the impact of this change:

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/6.jpg)

Step 4: Calculate the maximum interest deduction
------------------------------------------------

Using the positive version of our senior debt interest link, we can now calculate the maximum interest deduction for tax purposes.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/7.jpg)

Step 5: Connect into the Taxable profit calculation block.
----------------------------------------------------------

  
Our taxable profit line shows that the accelerated tax depreciation leads to "negative taxable profit", or Tax losses,  in the early periods.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/8-1.jpg)

Next, let's look next at dealing with those tax losses.

Download the model complete to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--105.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

  

  

Comments
--------

Sign in or become a Financial Modelling Handbook member to join the conversation.  
Just enter your email below to get a log in link.

 Send a log in link Great! Please check your inbox (or spam folder) for a log in link. Something didn't work. Please try again.

  Loading...

### Subscribe to Financial Modelling Handbook

Don’t miss out on the latest financial modelling guides. Sign up now to get access to the library of members-only guides.

[jamie@example.com\
\
Subscribe](https://www.financialmodellinghandbook.org/modelling-the-tax-computation-interest-deduction-thin-capitalisation#/portal/signup)
# What is deferred tax and how to model it

**Source:** https://www.financialmodellinghandbook.org/what-is-deffered-tax-and-how-to-model-it

---

Our tax calc is all working now, our balance sheet balances, and we have dealt with the circularity.

We have one more topic to cover, and that's Deferred tax.

Deferred tax liability is a line on the balance sheet that records taxes that are owed but are not due to be paid until a future date.

It's called a "deferred liability" because it relates to a difference in timing between when the tax was accrued and when it is due to be paid. We can think of it as an obligation to pay taxes in the future.

We have two items causing a difference between accounting profit and taxable profit. Those are

*   Tax depreciation
*   The maximum interest deduction for tax.

In the case of tax depreciation, this is only causing a timing difference between PBT and Taxable Profit. This is a Deferred Tax item.

In the case of the thin cap restriction on interest deductions, this is causing a permanent difference between PBT and Taxable profit and is therefore not usually a deferred tax item.

Let's look further at the tax depreciation issue.

In the first operating period, accounting depreciation equals $1m. In the same period, Tax depreciation is equal to $5m.

The difference is causing Taxable Profit to be $4m less than PBT. Multiplying this by the tax rate, we can see that the accelerated tax depreciation means that we are deferring $600k of tax payments. Another way of thinking about this is that if it were not for accelerated tax depreciation, we would have paid this $600m tax straight away, but now we will pay it sometime in the future.

This $600k deferred tax will be charged to the income statement, increasing our Deferred Tax liability on the balance sheet.

Later, accounting depreciation will be greater than tax depreciation, causing the situation to reverse and the Deferred Tax liability to reduce.

Deferred tax is a non-cash item that will only impact our income statement and balance sheet. However, failure to include it in our model could mean that our retained earnings are over or understated, leading to errors in the level of dividends distribution.

Let's walk this through.

Download the start file for this section:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Step 1: Calculate Deferred Tax charge
-------------------------------------

The Deferred tax in relation to depreciation is the difference between the accounting and tax depreciation multiplied by the tax rate.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/1-11.jpg)

  
Note that the row total adds to zero. This makes sense since we are dealing with tracking a timing difference.

If we chart our Deferred tax charge, it looks like this:

![](https://www.financialmodellinghandbook.org/content/images/2022/02/2-7.jpg)

  
If we overlay the Tax and Accounting depreciation lines, we can see that the Deferred tax change becomes negative when Tax Depreciation becomes smaller than Accounting Depreciation. We should, at this point, see the Deferred tax balance start to reduce. We'll check this shortly.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/3-6.jpg)

  
Step 2: Track Deferred tax liability balance
-----------------------------------------------

There are two ways we could do this.

The first maintains consistency with our practice to model balances in corkscrews.

We set up a simple corkscrew and flow the Deferred Tax charge out.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/4-4.jpg)

The second way, which is more common with tax advisors, is to calculate the difference between the Net book value of assets and the Asset value for tax and multiply that difference by the tax rate.

I've included this in our model for reference. It also serves as a good cross-check on the calculation.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/5-3.jpg)

Step 3: Next, let's wire this into our financial statements.
------------------------------------------------------------

  
We don't have placeholders for this, so it's an excellent opportunity to practice amending the financial statements.

Remember when you add new lines into the financial statements, always check:

*   Intermediate totals. In our case, we'll need to amend the calculation of Profit Before tax to include the new Deferred Tax line. I have seen SO many model errors caused by modellers forgetting this step.
*   Annual financial statements are adjusted to pick up the new line items.
*   Output summary sheet is adjusted to pick up the new line items.

Finally, let's check our deferred tax balance.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/6-1.jpg)

  
If we overlay the Deferred tax balance onto our previous chart, we can see that:

*   Deferred tax charge through the income statement (green line) goes negative when the Tax Depreciation (blue line) becomes smaller than the Accounting Depreciation (red line).
*   Previous to that, the Deferred tax balance (purple line) had been increasing. At that point, it starts to decrease, eventually reaching zero, at which point the timing difference has completely unwound.

All rather satisfying, actually.

Download the financial model complete to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--131.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/what-is-deffered-tax-and-how-to-model-it#/portal/signup)
# Modelling tax loss carry forward

**Source:** https://www.financialmodellinghandbook.org/modelling-tax-loss-carry-forward

---

However, most tax authorities will allow you to carry losses forward and offset them against taxable profit in the future.

Sometimes companies can carry these losses forward indefinitely. Sometimes they expire after a set number of years.

Our imaginary tax advisor has informed us that there is no limitation on the carry forward of tax losses in this jurisdiction.

So let's see how we can action this in the model.

Our steps will be as follows:

Step 1: Split out our Taxable Profit / (Tax losses arising) line into two separate lines. Each of these lines is going to drive further calculations.

Step 2: Tax losses arising will be the upward flow in a corkscrew we'll need to set up. The downward flow will be the utilisation of those tax losses.

Step 3: In any period, we'll compare Taxable profit and available tax losses brought forward from earlier periods. The tax losses utilised will be the lower of those two numbers.

Step 4: We'll deduct the utilised tax losses from the Taxable profit to give the "Taxable profit after tax losses utilised". Talk about a snappy label.

Step 5: Finally, we'll calculate the Tax paid by multiplying this line by the tax rate. We've been advised that taxes are paid quarterly. What do you mean by "isn't that a convenient simplification to make the modelling easy"? I mean, how long do you want me to drag out these tax chapters?

Let's go.

Download the start file for this section

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Step 1: Separate Taxable Profit from Tax losses arising.
--------------------------------------------------------

  
We're going to use two blocks for this:

![](https://www.financialmodellinghandbook.org/content/images/2022/02/1-3.jpg)

In the first block, we only want the positive values, so take the MAX of the value and zero. This only returns the positive values.

In the second block, we take a similar approach to isolate the negative values by taking the MIN of the value and zero. However, we want to process this line item as a positive item in our model to stick to our sign convention rules. We, therefore, sign switch this to give us positive values.

Step 2: Set up our corkscrew
----------------------------

We don't need an initial value injection, so we're using a four-line corkscrew structure. We immediately link tax losses into the corkscrew.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/2-2.jpg)

  
Step 3: Calculate tax losses utilised.
-----------------------------------------

  
We first link to taxable income. Then to the beginning balance of tax losses. The tax losses utilised is the minimum of those two. This then feeds back down into the corkscrew.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/3-2.jpg)

Step 4: Calculate tax losses after Tax-loss utilisation
-------------------------------------------------------

  
We now deduct the tax losses utilised from the taxable income to give the Taxable income after utilisation of tax losses.

![](https://www.financialmodellinghandbook.org/content/images/2022/02/4-2.jpg)

  
Step 5: Calculate Tax paid
-----------------------------

We now have the final Taxable Profit after tax losses that we can use to calculate the Tax payable line. To calculate the Tax paid, we multiple Taxable Profit by the tax rate,  in this case, 15%.  

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/02/5-2.jpg)

This line will be sign-switched (we'll need to add "POS" to the label, and will go to both the cash flow and income statements.

In our case, given the tax losses, tax payments do not begin until 2027.

Step 6: Wire into financial statements
--------------------------------------

Now that we have out Tax paid line, we can connect them to our financial statements. The Tax paid line will link to both the income statement and the cash flow statement.

Download the financial model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Circularity in our tax calculation
----------------------------------

When we do this, we immediately get a warning to tell us that the model is circular.

Why is the tax calculation circular?

Please take a moment to think through what might be causing us to get a circularity warning. This will help you when you find circularities in your own model later.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--79.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-tax-loss-carry-forward#/portal/signup)
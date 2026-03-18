# Sign convention in financial models

**Source:** https://www.financialmodellinghandbook.org/sign-convention

---

I started my financial modelling career at a large accounting practice. I learned my first modelling techniques by looking at my teammates' models. I absorbed what I thought was best practice by reverse engineering their models. From what I've learned since it seems my story is not an unusual one.

Unfortunately for me, many of the approaches were not best practices. It took me quite a few years to train myself out of the bad practice I learned.

One of the approaches was to use negative numbers for all outflows out the model. I adopted this approach in my modelling without much questioning. When I came across FAST a few years later, it was the first time I'd seen a logically argued convention for when numbers within the model should be positive and when they should be negative.

**What is the end goal?**
-------------------------

Users will expect to see outflows as negative numbers on the financial statements. Regardless of what we do elsewhere in the model, this is an expectation that we need to conform to.

![](https://www.financialmodellinghandbook.org/content/images/public/images/91b2f480-87b8-4563-b8f1-b2638e4dc35b_2554x1108.jpeg)

What happens on the financial statements then is not in question. The question is, what do we do in the rest of the model.

And for that, there are two options:

### Option 1: Make all the inputs for costs and outflows negative.

Let's say we had an Operating and Maintenance cost of $1.5m per annum. We would enter that as a negative number, and it would flow through the model as a negative number. We call this the "inflow/outflow" convention.

![](https://www.financialmodellinghandbook.org/content/images/public/images/c0b72f5b-9410-4beb-acb9-7c77f7606f04_1998x320.jpeg)

### 2 We keep everything positive inside the calculation engine of the model.

If we do this, at some point, before we get to the financial statements, we flip the sign. We're going to call this the "positive as normal convention."

![](https://www.financialmodellinghandbook.org/content/images/public/images/bdcfa7fd-d026-481e-9999-33f1496d785d_2216x378.jpeg)

Modellers are somewhat split about this. To a large degree, I expect preferences are driven by what you're used to.

My preferred approach is the "positive as normal" convention.

I'm going to set out my arguments for this below. You can then decide for yourself which you prefer.

We'll be using "positive as normal" throughout the rest of the book. There is no reason you can't adopt "inflow/outflow" for your models. Many people do with great success.

**Arguments for Positive as normal**
------------------------------------

### **Spotting errors**

If everything is positive by default in our model calculations, when a negative number does occur, it might indicate something we need to pay attention to.

It could be an error, or it could be that the number has correctly gone negative. Either way, we want to know about it. If all the numbers are positive, it is easier to spot when this happens.

**Experiment**

Is it easier to spot the positive numbers in image 1 below? Or is it easier to spot the negative numbers in image 2?

Image 1:

![](https://www.financialmodellinghandbook.org/content/images/public/images/d12abeea-d284-4f06-b540-f5770332236c_2394x610.jpeg)

Image 2:

![](https://www.financialmodellinghandbook.org/content/images/public/images/259a6eff-8b00-484c-bff9-5b1620124451_2394x600.jpeg)

It's easier to spot the negative numbers in image 2 than the positive number in image 1.

### **Visual Clutter**

This is also my personal opinion, but having thousands of numbers with brackets around them creates a sense of visual clutter in the model. You can see this in the images above.

**Arguments for inflow/outflow**
--------------------------------

### How do I know it's an outflow?

How do we know it's an outflow if the number is not negative?

I find it's easy to know from the context. We know that operating costs, debt interest and tax are outflows from the business. The numbers don't have to be negative for us to know this.

### "I can just add up the numbers."

Whenever we have a series of numbers, some that we are adding, some that we are subtracting, if we use the inflow/outflow convention, we can use the sum function and add them up.

However:

### **You have to switch the signs somewhere.**

Even if you use negative numbers throughout your model, you're going to have to get into the sign switching business somewhere.

Let's look at capex, depreciation and fixed asset balance.

Capex is an outflow, as is depreciation. Therefore, they would be negative numbers in our model if we used the inflow/outflow convention.

However, we'd expect to see a positive fixed asset balance. And that balance goes up with capex and comes down with depreciation. We would therefore have to get into the business of sign switching capex to make this work.

Let's look at an example:

![](https://www.financialmodellinghandbook.org/content/images/public/images/6c4b0e3b-30be-4c8d-84af-d1268fe93f6f_2602x730.jpeg)

Here, we are basing depreciation on the initial asset value. This asset value is rightly positive. To "make" depreciation be negative, we have to sign switch it within the calculation.

Then, when calculating the asset balance, we have to sign switch capex within the calculation to cause capex, a negative number, to increase the asset balance.

![](https://www.financialmodellinghandbook.org/content/images/public/images/ed7c39f0-f55e-44de-8c76-d4776c8cf97f_2674x1204.jpeg)

Therefore no matter which convention you choose, **you can't avoid sign switching**. With an inflow/outflow convention, we still have to do an amount of sign switching, but we have the downside of a sea of brackets in our model.

We use Column D to add "plus" and "less" labels to make it easier to see which line items the calculation is adding and which it is subtracting.

How we approach sign switching.
-------------------------------

I prefer to keep numbers positive inside the calculations of the model and then sign switch immediately before an outflow number goes to the financial statements.

If everything is positive within the model, we only have to sign switch for a few line items: outflows that go to the income statement or cash flow statement.

On the Template sheet, we keep a "sign switching" line that we can copy and drop below anything that needs to be sign switched before it goes to the financial statements.

![](https://www.financialmodellinghandbook.org/content/images/public/images/80768035-8256-4e87-a0a5-d467aaf54a27_2630x1074.jpeg)

Template Sign Switch line. Copy this below anything outflow that is going to the financial statements.

We change the label of the positive version by adding "POS" to the end. This is a lot like the label we add to opening balances. It's deliberately ugly so that it's tough to miss. We never want to link to the positive by mistake when we intend to link to the negative, and vice versa.

![](https://www.financialmodellinghandbook.org/content/images/public/images/e568a72d-04a0-4d25-828f-987536119e1d_2352x762.jpeg)

All sign switches in the model look the same.

The formula in column E looks at the row above and removes the "POS" That way, the two different line items, one positive, one negative, have different labels.

The sign switch is always red because it's always exported to the financial statements. This is because we only sign switch line items that are going to the financial statements.

We’re going to see sign switching used out our model build.

Here’s a summary of the steps.

How to switch signs - step by step
----------------------------------

In this example, we have just calculated depreciation, and we want to add it to our income statements.

Our starting position looks like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/a569a02c-818b-42c5-98ef-0d4f21f65a9e_2446x716.jpeg)

### Step 1: Add POS to the label.

This ensures that the positive and negative line items have unique labels. It also prevents us from linking to the wrong one in a future calculation.

![](https://www.financialmodellinghandbook.org/content/images/public/images/9b1e48ed-cb7d-42cc-938c-842fdc094136_2734x338.jpeg)

### **Step 2:** Copy the sign switcher from the Template sheet or somewhere else in the model.

The sign switch lines are all the same. So if you have used one somewhere nearby, you can easily copy it. Otherwise, grab the one from the Template sheet.

In our worked example file, we have used the sign switch on O&M costs, and so we can copy from there.

Shift spacebar then Control+c to copy the sign switcher.

![](https://www.financialmodellinghandbook.org/content/images/public/images/abf9e410-f621-47c7-b998-53453e978acb_2140x346.jpeg)

### **Step 3:** Drop the sign switch line item underneath the line to be sign switched.

Shift+spacebar, Enter

![](https://www.financialmodellinghandbook.org/content/images/public/images/beca47a7-e432-4615-8321-26d22df8177e_2444x616.jpeg)

Note: at first, it looks like we have taken the values from the O&M cost section. Don't panic at this stage. Remember, we are in manual calculation mode. We need the last step.

### Step 4: Local recalc to check results

Shift+F9

![](https://www.financialmodellinghandbook.org/content/images/public/images/688b8b30-1e4a-4819-9c9d-563b2a5b8573_2306x368.jpeg)

### **Step 5:** Link the negative line to the financial statements.

See [Core Modelling Skill 2](https://www.financialmodellinghandbook.org/how-to-create-a-link-in-a-financial-model/)
 on creating a link.

![](https://www.financialmodellinghandbook.org/content/images/public/images/024cf1c4-426c-44cd-864c-1ab6318ba476_2020x494.jpeg)

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--101.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/sign-convention#/portal/signup)
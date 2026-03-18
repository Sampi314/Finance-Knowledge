# Financial model section completion checklist

**Source:** https://www.financialmodellinghandbook.org/section-completion-checklist

---

Download the start file for this lesson

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

* * *

Whenever we complete a section of our model, it's helpful to spend a little time reviewing what we've built and tidying it up if necessary.

It's tempting to skip this and press on with the model build. I recommend getting into the habit of not skipping this. It's easier to review small sections of code as we go along rather than wait until the end to review everything.

The key to a good checklist is having the minimum number of essential items on the list. Too many items and people won't use the list. Too few, and we risk missing important steps.

I recommend running the following checklist at the end of each section of model build. It doesn't hurt to have this checklist somewhere in your model so that you can easily refer to it.

1.  Active error checks / alerts
2.  Spell check
3.  Analytical check
4.  Recheck inputs & relocate if necessary
5.  Tidy up input sheet
6.  Check heading capitalisation
7.  Check placeholders
8.  Tidy up grouping
9.  Check aggregated financial statements
10.  Check & resent output sheet

Let's see these steps in action, applied to the modelling we have just done of retained earnings and retained cash.

1\. Active error checks / alerts
--------------------------------

Error checks and alerts are visible throughout the model. If there are any active when you complete a section of modelling make sure you know why. If you don't know why, find out, and put it right if necessary.

2\. Spell check
---------------

The spell checker in Excel is not excellent. I've found that it does miss errors quite frequently. However, it's better than doing no spell checking at all. It's easy, and it's quick.

Access the spell check from the Review Menu:

![](https://www.financialmodellinghandbook.org/content/images/public/images/277f5190-cf35-420b-8aed-7da9b019f044_1304x786.jpeg)

The spell checker works on a sheet by sheet basis. We, therefore, don't have to spell check the entire model each time, just the sheet or sheets we've been working on.

In this case, the spell checker does not find any errors.

3\. Analytical check
--------------------

It's important to check that your calculation works when you change the inputs. It's better that you test this now than the recipients of your model change the inputs and find that the model breaks straight away.

As the model grows, it's unlikely that you will be able to test every possible combination of inputs; that quickly becomes an enormous number of possible combinations.

You should test each calculation as you go within a sensible range of inputs and check that the outputs make sense.

It's easy to forget to do this, which is why we use a checklist.

💡

The key question we're asking is, "Does the model react in the way I'd expect when I change the inputs".

To perform this test, we need to have a hypothesis about how the model will react.

We deliberately perform this step in the checklist before relocating inputs. It's easier to do the analytical review while the inputs are on the calculation sheet rather than paging back and forward to the input sheet.

If you are still not comfortable with inputs on your calculation sheet during the build, you'll have to make the changes on the input sheet. This, of course, is not a problem!

In the case of the retained cash and retained earnings balances that we have added, we only have two inputs - the opening balances for cash and retained earnings.

### Step 1: State your hypothesis about how the model should react when changing the inputs.

In the case of each of these opening balances, if I change them from zero, I expect to see:

*   An initial cash balance at financial close in the corkscrew
*   All of the period balances increase by that amount.
*   The same numbers flow through to the balance sheet.
*   If I have different initial balances for retained cash and retained earnings, the balance sheet will no longer balance. The balance sheet difference will be the difference between the initial cash balance and the initial retained earnings balance.
*   A balance sheet error to be reported in the model

### Step 2: Test your hypothesis in the model.

I'm going to enter an opening balance of 1,000 in Retained cash.

Note that initially, I'm just hitting Shift+F9. This causes Excel only to recalculate the active sheet. It can be helpful to control which parts of the model recalculate when doing an analytical review; I want to be looking at the section that's changing so I can see the impact myself.

![](https://www.financialmodellinghandbook.org/content/images/public/images/8966d45e-999c-412b-9d1f-c1ae90afcaf9_2404x632.jpeg)

I have confirmed that the corkscrew shows an initial cash balance at financial close. I've also confirmed that all projected balances have increased by that amount.

To check the balance sheet, I first go to the FS page. Because I have not yet calculated the whole model - there is no change to my balance sheet yet:

![](https://www.financialmodellinghandbook.org/content/images/public/images/c6a09c69-0df2-4885-9db3-98ca8e56f202_2256x1276.jpeg)

I hit Ctrl+Alt+F9 to fully recalculate the model while looking at the balance sheet. That way, I can see the changes happening in real-time. This gives me greater clarity and precision to my review.

![](https://www.financialmodellinghandbook.org/content/images/public/images/338f560f-16c6-4c01-966f-22f06611ef94_2224x1314.jpeg)

I have now confirmed that the same numbers flow through to the balance sheet. I can also see that model is flagging a balance sheet error. The balance sheet is out by the difference in the initial balances.

If I now enter 1,000 into retained cash and repeat the steps, as expected, the balance sheet now balances since the initial asset and initial liability balances are the same.

![](https://www.financialmodellinghandbook.org/content/images/public/images/8177317e-003e-4da5-b9a2-0545bc1e7abc_2240x1214.jpeg)

The first analytical review is simple as we only have two inputs. We'll see it again later with more complex and detailed inputs.

4\. Recheck inputs & relocate if necessary
------------------------------------------

This step deliberately occurs after the analytical review. We will likely have been messing around with our inputs to test our calculations. It's therefore essential to have this step happen afterwards, confirming that we have reset our inputs to our base-case assumptions. We can then relocate inputs to the input sheet.

### Step 1: Reset to base-case assumptions.

![](https://www.financialmodellinghandbook.org/content/images/public/images/896e1be4-415c-4fe7-a7d9-b5e545e6b484_2208x1122.jpeg)

Relocate inputs using Skill 10.

![](https://www.financialmodellinghandbook.org/content/images/public/images/f5a6741c-39a9-4cd4-b31e-e3139a33c205_2034x1028.jpeg)

5\. Tidy up input sheet
-----------------------

The input relocation macro will move your inputs to the bottom of the input sheet. It's worth keeping the input sheet tidy as we go along by moving these into a suitable position.

Don't worry too much about input structure now. The structure of the input sheet will emerge as the model build progresses. We can continue to restructure the sheet as we get a better sense of all the inputs we'll need.

The input relocation macro puts the inputs at the bottom of the page by default:

![](https://www.financialmodellinghandbook.org/content/images/public/images/66b52b8f-f025-472b-9e55-c84650632c9d_2466x1028.jpeg)

For now, I have created a section called "Opening balances". This heading may not be the final structure, but it works for now.

When moving the inputs, select the whole row (Shift+spacebar), then cut them (Ctrl+X). Don't use copy here.

![](https://www.financialmodellinghandbook.org/content/images/public/images/4d01b8ae-91dd-40fd-b2e3-e56e65816854_2724x1212.jpeg)

6\. Check heading capitalisation
--------------------------------

Checking and updating heading capitalisation is easy and quick to do and helps to maintain consistency as you go along.

Ctrl+Shift+6 to bring up the modelling utilities user form

![](https://www.financialmodellinghandbook.org/content/images/public/images/6a00e36f-73e7-4089-a382-b8d9c3aa3eab_2522x1736.jpeg)

Then hit 7 to run a quick check on heading and label capitalisation. In my case, no changes were required.

![](https://www.financialmodellinghandbook.org/content/images/public/images/80a1d3f8-2010-420a-9508-e25396500158_1804x916.jpeg)

7\. Check placeholders
----------------------

Here we are checking:

*   Are there any placeholders in the section I just created that I could already replace with links to actual calculations
*   Are placeholders well labelled and clear
*   Have I left a note with the placeholder to explain why it's there?

Leaving a note is helpful for other people who might review the model. It's also a valuable gift to your future self. When you open this model again in 6 weeks, these notes will make it easier for you to quickly remember what the placeholder is for and what you planned to do about it.

Shift+F2 adds a cell note

![](https://www.financialmodellinghandbook.org/content/images/public/images/e0bf7342-a962-4872-9b53-d6fa2ee25de6_1952x1206.jpeg)

8\. Tidy up grouping
--------------------

Again this is a quick one.

Control+Shift+6 to call up our modelling utilities.

Hit 3 to clean up the grouping.

This macro will apply two grouping levels, using the headings in Column A and Column B.

![](https://www.financialmodellinghandbook.org/content/images/public/images/f9ca3065-b6ef-400d-b144-b32201461812_2344x592.jpeg)

**9\. Check aggregated financial statements**
---------------------------------------------

Note: this check is only required if you have a "periodic financial statement" - e.g. quarterly, and an aggregated financial statement - e.g. annual.

If during your last session of modelling, you added line items to your periodic financial statement check to ensure that the Aggregated financial statements are correctly aligned and show the same line items. You may wish to include a check to confirm that the financial statements align.

You are checking:

*   Are the periodic and aggregated financial statements giving the same results? Checking the row totals on the income statement and cash flow will help.
*   If you have added line items to the periodic financial statements - are they replicated on the annual.

10\. Check & reset output sheet
-------------------------------

There are two parts to this check.

This check is similar to the aggregated financial statements. You are checking to see that there is still alignment between the financial statements and the output track sheet. Do row totals match? Are the income statement and cash flow statement items on the output sheet?

You can also check the change from the previous output track. Given the changes you have just made in the model, does this make sense?

Before moving on to the next modelling section, it's worth resetting the output sheet by adding a new stored track.

Resetting the output sheet will give you a valuable baseline to compare the impact of the next set of changes.

Ctrl+Shift+5 will store a new output track.

There’s very little on our output sheet at the moment, but this will start to change quite quickly.

Don't worry about the number of stored output tracks you have. You can always delete them later.

* * *

Download the file complete to this point.

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--93.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/section-completion-checklist#/portal/signup)
# Modeling dividends - solution

**Source:** https://www.financialmodellinghandbook.org/modelling-dividends-solution

---

What is the maximum amount of dividend that the model could pay?

Looking at the income statement, at present, there is $322.7m of Profit after tax being generated over the life of the project.

![](https://www.financialmodellinghandbook.org/content/images/public/images/3ec2b97c-4b62-474c-bc27-7f0c9e76d47e_2248x946.jpeg)

At present, those profits are not going anywhere. They are being retained in the business. If we look at the chart of Retained earnings, we can see that undistributed earnings are building up to the same amount - $322.7m.

![](https://www.financialmodellinghandbook.org/content/images/public/images/2dfdd24e-76e7-4e94-98b8-389b44ef3d2c_2414x1796.jpeg)

An F11 quick chart of the retained earnings balance - showing a build-up to $322.7m

Once we model dividends, all of this will be distributed. Therefore the total amount of the dividend will be $322.7m

Let's walk through the calculation.

We will work on the Equity tab.

Step 1: Add section headings.
-----------------------------

I like to signpost where I'm headed. If I know ahead of time, I'll add the section and sub-section headings that I need. I don't always know ahead of time!

![](https://www.financialmodellinghandbook.org/content/images/public/images/3e067c70-05b9-47d4-b463-943e07670d52_1934x1282.jpeg)

Step 2: Earnings available for dividend
---------------------------------------

We know that the earnings available will be the sum of the earnings at the beginning of the period and the Profit After Tax for the period.

Therefore we'll link to the beginning balance of Retained earnings using Skill 2.

![](https://www.financialmodellinghandbook.org/content/images/public/images/a4745d2a-e7a6-4264-87e4-61ba6eef3ed7_2230x1104.jpeg)

We'll then copy the existing link to Profit After Tax that's already in the Retained earnings corkscrew, using Skill 4

![](https://www.financialmodellinghandbook.org/content/images/public/images/0aedfc18-efbe-4b36-b630-db11ca91a13a_2378x1048.jpeg)

Set up the calculation for Earnings available for dividend.

Note that this amount is a balance. Conceptually, it’s the balance of earnings available at the end of the period, immediately prior to making a distribution. Because it’s a balance we don’t need to add a row total.

![](https://www.financialmodellinghandbook.org/content/images/public/images/417f71de-3b92-4fc6-8b6b-ab8ab677e558_2420x1060.jpeg)

Step 3: Repeat the same steps for cash.
---------------------------------------

![](https://www.financialmodellinghandbook.org/content/images/public/images/aab50fb0-3fe3-40b4-8a3b-3c8a707c0b79_2548x1434.jpeg)

Step 4: Calculate the minimum of earnings available and cash available.
-----------------------------------------------------------------------

We now need a new calculation block bringing in Earnings available and Cash available as new ingredients.

![](https://www.financialmodellinghandbook.org/content/images/public/images/fb202aea-0d3c-46fc-bda0-c0ccd1297c75_2048x998.jpeg)

The calculation we are writing needs to do two things:

1.  Calculate the minimum of retained cash and retained earnings
2.  Prevent the amount of distribution from being a negative number.

The MIN and MAX functions will be useful here.

(How long have we been working together - and I'm only now introducing new functions. Like I said at the start, this isn't a book about Excel functions).

Our formula will therefore be :

**MAX(0, MIN(Retained cash, Retained earnings).**

The formula will first calculate the lower of retained cash and retained earnings, and then take the maximum of that answer and 0. Therefore if the value is negative, the formula will always return 0.

![](https://www.financialmodellinghandbook.org/content/images/public/images/73c54aad-ca8b-4627-85f8-e5a8c8274a6b_2326x1150.jpeg)

Hopefully, a question should be jumping off the page at you:

Why is our calculation returning $22.9bn of dividends?

It's all down to the last step in the process.

Step 5: Add the dividend paid line into the retained earnings and retained cash corkscrews.
-------------------------------------------------------------------------------------------

Once the dividends have been paid, the earnings and the cash have been distributed and are no longer available to distribute again; we have to reduce each balance by the amount of the dividend.

Use Skill 2 to create a link to our new Dividends paid calculation in the retained cash corkscrew. Then use skill 4 to copy the link into the other corkscrew.

![](https://www.financialmodellinghandbook.org/content/images/public/images/8cd6f06a-cb3d-4ed1-b6f9-0684d329fdcd_2400x1130.jpeg)

Now we can see that the amount of dividend paid conforms to our hypothesis.

Step 6: Add dividends to the income and cash flow statements
------------------------------------------------------------

We have placeholders on the income statement and cash flow statement for the dividend line. Note that you’ll need to sign switch the dividend paid line before adding to the financial statements.

![](https://www.financialmodellinghandbook.org/content/images/public/images/aa8df31c-bb9c-43e0-a017-c0ee8379cdbd_1172x398.jpeg)

Dividends are an outflow and will need to be sign switched before being exported to the financial statements

![](https://www.financialmodellinghandbook.org/content/images/public/images/f22c291b-ccb5-4b97-b917-813341be5dd6_1346x570.jpeg)

Dividends added to the income statement

In the solution file, I changed the label on the income statement to read “Net income after dividends” as I think this is clearer. I made a similar change on the cash flow statement.

* * *

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

* * *

Before we move to depreciation, a slightly tricky analytical question:

**All the available cash being paid out, leaving a cash balance of zero in each period? However, not all the earnings are being paid out, leaving some retained earnings in the business in each period? Why is that?**

The answer is at the beginning of the next section. Try to develop a hypothesis for yourself before moving on.

![](https://www.financialmodellinghandbook.org/content/images/public/images/55840056-fb5b-4a0e-ba49-0ec4c1dc14a3_2388x1754.jpeg)

F11 quick chart of Retained earnings balance - what’s going on?

* * *

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--88.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-dividends-solution#/portal/signup)
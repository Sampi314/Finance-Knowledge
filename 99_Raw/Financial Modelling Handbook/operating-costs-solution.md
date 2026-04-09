# Modelling operating costs - solution

**Source:** https://www.financialmodellinghandbook.org/operating-costs-solution

---

* * *

Here's the step by step build-up of the operating costs block. I find it particularly satisfying that in preparing this calculation block, we use our Core Modelling Skills in order from 1 to 5.

Step 1: Add a heading
---------------------

I'm creating some space and adding a new Column A section header. It's helpful to keep the word END at the bottom of your calculation sheet so that if you navigate up and down in column A using Ctrl+up and down arrow, you will stop at the bottom of the calculation range.

![](https://www.financialmodellinghandbook.org/content/images/public/images/14960821-5ecc-43af-984c-b28ccda5c362_2104x1560.jpeg)

Now we're ready to gather ingredients:

Step 2: O&M cost input
----------------------

Use: Skill 1 - How to add an input

![](https://www.financialmodellinghandbook.org/content/images/public/images/ff42a863-f5b6-4a7e-9bf8-f614c8aeca6c_2024x1226.jpeg)

Note the label's specificity; we are clear that the O&M cost is annual, fixed and real. It may seem minor, but this helps model review later. I'm entering the amount in the default unit of the model so that I don't have to convert.

Step 3: Periods per year
------------------------

Use: Skill 2: How to create a link

I already have this ingredient on my input sheet, so I will link straight to that to avoid creating a duplicate.

![](https://www.financialmodellinghandbook.org/content/images/public/images/bc6766a2-d8d8-4668-bdc5-3c1c3779fc0d_2048x1350.jpeg)

Step 4: Indexation factor
-------------------------

Use Skill 3: How to create a placeholder

I've already decided that I'm not going to get diverted into modelling indexation at this stage. I'm therefore going to add a placeholder. I'm not going to worry about calculating the placeholder to match the specifications in the case. It's a placeholder. It's OK for it to be wrong. When we model indexation, I'll replace this placeholder with a link to the correct calculation. It's always worth adding a note to the placeholder to remind yourself in the future why you left it here.

![](https://www.financialmodellinghandbook.org/content/images/public/images/54bed753-918e-49d2-9322-d5e181daadf3_2264x832.jpeg)

Step 5: Operating period flag
-----------------------------

Skill 4: How to copy a link

I already have a link to the Operating period flag in row 37:

![](https://www.financialmodellinghandbook.org/content/images/public/images/b95558f8-45be-4689-84be-3661d19de0af_2058x1004.jpeg)

I'm therefore going to copy that link.

![](https://www.financialmodellinghandbook.org/content/images/public/images/b650a3e2-1b32-4fcd-b8b8-551f98ef4fa7_2232x952.jpeg)

Step 6: Write the calculation
-----------------------------

Skill 5: How to create a calculation

![](https://www.financialmodellinghandbook.org/content/images/public/images/55db6352-52c7-42a0-bf79-a6ab79ee45c4_2392x884.jpeg)

When writing the calculation, I'm paying particular attention to column anchoring the two constants.

I know that I'm going to sign switch the calculation before adding to the income statement, so I'm adding "POS" to the label straight away.

Step 7: Sign switch the calculation
-----------------------------------

As this is the first cost or outflow that we're modelling, I'm copying the sign switcher from the Tmp sheet. The more calculations that we sign switch, the more of these will be around our model, making it quicker to find one to copy.

![](https://www.financialmodellinghandbook.org/content/images/public/images/f420d911-170a-4085-86ac-3ec22f60c4e5_1778x772.jpeg)

e

Sign switching is a simple copy and paste operation. You'll need to refresh the page with Shift+F9 if you are in manual calculation model.

![](https://www.financialmodellinghandbook.org/content/images/public/images/bce1e97d-2b22-4835-9751-9638c038d8fd_2210x994.jpeg)

Step 8: Link to the financial statements.
-----------------------------------------

We're now ready to add O&M cost to our income statement.

We are again using Skill 2: How to create a link.

![](https://www.financialmodellinghandbook.org/content/images/public/images/94580041-1dae-4d97-8c4f-6695591beb46_2402x756.jpeg)

Once it's linked, you'll need to clear out the yellow placeholder shading. Select the row and use Productivity Pack keystroke Ctrl+Shift+c to clear the cell shading.

And that's Operating Costs complete.

A full recalculation of the model will show that we have new changes on the Output track (as expected) and that our balance sheet doesn't balance (also as expected).

![](https://www.financialmodellinghandbook.org/content/images/public/images/3de7040f-df10-40dc-96f6-7bc6981bf087_2078x1010.jpeg)

In the next chapter, we'll look at the working capital implication of our Operating costs and wire up the cash flow appropriately.

Before moving on, remember to go through the Section Completion Checklist.

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--142.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/operating-costs-solution#/portal/signup)
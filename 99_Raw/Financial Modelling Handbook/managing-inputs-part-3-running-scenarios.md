# Managing inputs - part 3: Running scenarios

**Source:** https://www.financialmodellinghandbook.org/managing-inputs-part-3-running-scenarios

---

In the last chapter, we defined a scenario as a "_variation on a case, based on changing a subset of the assumptions._"

Therefore, running a scenario involves changing some but not all the base case assumptions.

Ideally, when running a scenario, we'd like to:

*   avoid overwriting the base case assumptions themselves
*   only have to input the assumptions that are changing
*   have a clear picture of which assumptions are different in the scenario vs the base case.

We have set up the scenario input columns to achieve this.

It would be dangerous to change the underlying core base case data. If we change quite a few assumptions to run our scenario, we would have to remember to change all the numbers back. The risk of forgetting to change numbers back to their base case values is too significant.

Therefore, we can use the scenario columns to run variations without changing the underlying base case data. These scenario columns are currently O to R, although you can add as many as you need.

Let's see how this works in practice.

Each scenario has an underlying base case.

You choose the underlying base case for each scenario in row 6. We can have multiple scenarios with the same underlying base case.

![](https://www.financialmodellinghandbook.org/content/images/public/images/6cfd5c06-1581-4faf-b2bb-d34c452d14b7_1206x410.jpeg)

In our example, Scenario 4 refers to Base case 1. If any of the input cells under Scenario 4 is blank, the model will select the relevant Base case 1 input. Any inputs added to the Scenario 4 column will overwrite the Base case 1 assumptions.

At present, there are no specific inputs under Scenario 4. Therefore if we switch from Case 1 (Base case 1) to Case 4 (Scenario 1), nothing in our model changes. Since Scenario 4 has no inputs of its own, all the inputs are those for Base case 1.

Although we have switched to Scenario 1, the words “Base case” still appear under Base case 1; since this is the relevant base case for Scenario 1.

If we select Case 1 as our Comparison case, we can see in F7 that there are no differences between Scenario 4 and Base case 1.

![](https://www.financialmodellinghandbook.org/content/images/public/images/d18b9e9d-08bb-4ff0-949f-b47fb61b321c_1169x487.jpeg)

Let's say one of the changes we want to make in Scenario 4 is that we are running a 30 year PPA rather than a 25 year PPA. We enter this in row 21, under Scenario 4.

![](https://www.financialmodellinghandbook.org/content/images/public/images/457c36c9-7ce0-4862-9d8b-d7090aaf12ce_1162x553.jpeg)

We see three visual indicators to highlight the difference:

*   the scenario difference marker in row 21 shows that there is now a difference between Case 1 and Case 4
*   The cell formatting in Scenario 1 for PPA (row 21) has changed. The scenario input cells are set up with conditional formatting to only carry input formatting if they have a value in the cell. This makes it clear to see where the inputs are.
*   Cell F7 shows the number of differences between Base case 1 and Scenario 1.

Although this structure may seem like a lot, it gives us several essential abilities in our model. We can:

*   Change a subset of assumptions for a given scenario without having to remember what we've changed.
*   Revert to our base case without having to make any input changes. Whenever we want to go back to the base case, we select Case 1 again
*   Store the scenario assumptions separate from the base case assumptions for as long as we need them

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--98.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/managing-inputs-part-3-running-scenarios#/portal/signup)
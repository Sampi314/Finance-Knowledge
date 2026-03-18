# Managing inputs - part 2: Using and comparing cases

**Source:** https://www.financialmodellinghandbook.org/managing-inputs-part-2-using-and

---

We have set up the input sheet so that:

*   We add the actual input value in Columns K onwards.
*   The inputs are arranged into cases. Each column of inputs represents a case.
*   Column F selects the inputs based on the case we want to run.
*   The rest of the model links to Column F. Those are the numbers driving the calculations in our model.

We never input actual numbers into Column F itself. Column F only ever contains the formula to select the cases.

![](https://www.financialmodellinghandbook.org/content/images/public/images/a3a6a202-1cd9-473d-8cb5-aaed7bbe2978_1433x511.jpeg)

We select the active case by entering the case number into cell F4.

![](https://www.financialmodellinghandbook.org/content/images/public/images/006f091d-cc8a-455a-8e8f-1e63a7a1654c_1159x409.jpeg)

The number of the case corresponds to the case number in row 4. If we change to case 2, in this example the inputs from Column L will now be the ones driving the model. The “active case” marker arrow in row 2 moves, and the “Base case” identifier in row 7 changes also.

![](https://www.financialmodellinghandbook.org/content/images/public/images/14033ab9-9cfd-4feb-a0eb-cf08ccea2abb_1093x391.jpeg)

"So what's changed?": Using case comparison to track input changes.
-------------------------------------------------------------------

The time when financial modelling is required is usually a time of change or disruption for a business; it could be new investment, new financing, a new acquisition or a new bid for a project. These are times of high stakes and high pressure for the business and those relying on the modelling results.

**Assumptions will change quickly. Sometimes rather chaotically.** It will be up to you to keep track.

**At some point, you will be asked the question - "So what's changed here"?**

You will look like a rock star modeller if you can very quickly (ideally on the spot) go back to old previous base cases and articulate the differences. To make this possible, don't overwrite old input cases and don't get rid of them. Add another base case column for each new base case. Each time there is a significant change to the base case, add a new base case column.

When asked what's changed, you can quickly compare any two previous base cases and accurately describe what has changed.

How to compare input cases
--------------------------

Our input sheet is set up to allow us to track the differences between different sets of inputs. We use the "Comparison scenario" input in F5 for this.

Entering a scenario number into F5 allows us to compare any input case with the active case. In the set-up below, Scenario 1 is the active case, and we want to compare with Scenario 2.

![](https://www.financialmodellinghandbook.org/content/images/2022/03/4-2.png)

The model highlights the differences in two ways:

### The total number of input differences.

Cell F7 shows the total number of differences in the assumptions between the active case and the comparison case. We can see that there are three differences in the assumptions.

### Which particular inputs are different.

The marker in column I will "light up" to highlight that there is a difference between the active case and the comparison case in that particular row.

![](https://www.financialmodellinghandbook.org/content/images/2022/03/5-1.png)

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--99.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/managing-inputs-part-2-using-and#/portal/signup)
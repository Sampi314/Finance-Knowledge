# Managing inputs - part 1: Cases, scenarios & senstivities

**Source:** https://www.financialmodellinghandbook.org/managing-inputs-part-1-cases-scenarios

---

When designing the input sheet structure, we were aiming for the following outcomes:

1.  The ability to easily switch input scenarios;
2.  The ability to run alternative scenarios on base case data without changing the base case numbers themselves;
3.  The ability to have both constant and series based inputs;
4.  Clarity around which input scenario is active in the model;
5.  The ability to see quickly and accurately what has changed between different input sets;

The input sheet needs quite a lot of structure to fulfil the above objectives.

Over time, we have found it helpful to separate constant inputs from series (i.e. time-based) inputs. We will come back to series inputs in the next chapter.

This chapter will go through each element of the constants input sheet structure.

Although it seems like a lot of work to set up, we never build this from scratch. When starting a new model build assignment, we always start from a pre-existing "start file" with all the model infrastructure already set up. See Chapter X for more on the Start File.

Cases, base cases, scenarios and sensitivities.
-----------------------------------------------

Base case, sensitivities and scenarios are frequently used terms in financial modelling.

For this book, I'm defining them as follows:

*   **Case:** A set of inputs representing a particular view of the business or project.
*   **Base case:** A case that is the current "best view" of what will happen in the business or project. Note that it's possible to have multiple "base cases". For example, we might be looking at two different financing options and have a base case for each financing option.
*   **Scenario:** A variation on a case based on changing a subset of the assumptions.
*   **Sensitivity:** A variation on a case based on changing one assumption.

Applying these definitions in our model.
----------------------------------------

![](https://www.financialmodellinghandbook.org/content/images/public/images/cb02c9d5-f1c9-46e6-8bf2-e839e0e70122_2718x1106.jpeg)

*   Each of the columns from K to R in our example represents a **case.**
*   Columns K, L, and M are **base cases.**
*   Columns O through R are for **scenarios** based on a selected **base case.**

Spacer columns
--------------

We have set up this example input sheet to store seven cases: three base cases and four scenarios. There is nothing magic about these numbers. We need to be able to flexibly add base cases or additional scenario cases.

Columns J, N and S are spacer columns. They are narrow and formatted with grey shading. We should insert any new cases between those spacer columns; that way, the functions that make the case selection work will continue to operate.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--100.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/managing-inputs-part-1-cases-scenarios#/portal/signup)
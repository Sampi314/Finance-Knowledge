# Managing inputs - part 4: Input sheet mechanics

**Source:** https://www.financialmodellinghandbook.org/managing-inputs-part-4-input-sheet

---

How the formulas in column F work
---------------------------------

We have written the formula in column F using three index functions inside an IF statement.

![](https://www.financialmodellinghandbook.org/content/images/public/images/f95bb02e-dcdd-4c8e-8b7d-efda56b129b5_1305x492.jpeg)

If we were to translate the IF statement into English, it would read:

_If the cell in the selected scenario is blank, choose the value in the cell from the base case for that scenario; if it isn't blank, select the value from the chosen scenario._

The INDEX function in excel helps look across a range of options and pick an option based on user input.

As used here, the INDEX function has two arguments:

Array: This is the range of cells containing the possible options.

Row number: This is the number in that range of cells that the function should select. Although the function calls this argument "row number", the index function can work down a range of cells in a column (in which case row number would be correct) or across a range of cells in a row (in which case column number would be more appropriate).

The first INDEX function in F13 looks across the range from J13 to S13. It picks the value in the cell given by the number in cell I4.

This logic allows our scenarios to default to the selected base case if the scenario input is blank.

Non-changeable technical inputs
-------------------------------

There are always several "universal" constants in a model. We need to explicitly have these numbers as inputs to avoid hard coding them in formulas, but they never change. We usually, therefore, include a section of "Non-changeable technical inputs" at the bottom of the input sheet. These inputs are not connected to the input scenario structure as they never change.

Numbers like days in a year, months in a year etc., are stored here.

![](https://www.financialmodellinghandbook.org/content/images/public/images/53c6f9d0-c8f4-4d2e-baf3-7ed2a09420e1_905x437.jpeg)

Template input line
-------------------

We have a blank "template" input row at the bottom of the input sheet. This row is used by the Productivity Pack when running the input relocation macro. You can also use it as a template input row; you can copy this when you want to manually add a new input row.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--97.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/managing-inputs-part-4-input-sheet#/portal/signup)
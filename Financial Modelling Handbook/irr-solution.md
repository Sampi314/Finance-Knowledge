# Modelling IRR - solution

**Source:** https://www.financialmodellinghandbook.org/irr-solution

---

* * *

Let's go step by step through the IRR setup.

Download the solution case file for this lesson:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Step 1: New sheet
-----------------

I'm working on a new sheet called "Metrics".

Set up a sheet using Skill 9: How to create a new worksheet

Set up your section headings.

Step 2: Calculate Net cash flow to equity
-----------------------------------------

For the IRR calculation, we will have to model Net cash flow to equity on an inflow/outflow basis. This means that we should show outflows as negative and inflows as positive. Remember that we are showing this from the equity investors point of view. So the share capital they invest at the transaction date is an outflow, and the dividends are in inflow.

When calculating a line on an inflow/outflow basis is can be helpful to indicate this in the label. Therefore, an effective label can be "Net cash flow to / (from) equity". The (from) in brackets indicates that we expect some negative values, and we have indicated what those mean.

![](https://www.financialmodellinghandbook.org/content/images/public/images/dcf1b1a5-9c3d-462f-8282-ef44bf475a60_1323x378.jpeg)

Note that we are using a flag to place the $100m initial investment at the correct place on the timeline. The dividends are already placed correctly on the timeline.

Step 3: Calculate IRR using XIRR
--------------------------------

The block to calculate the IRR will have two ingredients:

*   the Net cashflow to / (from) equity line
*   the quarterly period end dates (linked from the time sheet)

Use Skill 2 to create both these links.

We will place our calculation of XIRR in the constants column.

We will format the IRR as a percentage using Ctrl+Shift+p.

![](https://www.financialmodellinghandbook.org/content/images/public/images/707d3bbe-4f06-41dc-9aae-1e9516be7dcb_1312x462.jpeg)

Step 4: Why are we getting an IRR of 0%?
----------------------------------------

A net cash flow of $222m should not give an IRR of 0%.

We see here a peculiarity of the XIRR function. The very first cash flow in the series must be a negative number. We will use a "very small" negative number in the first period to get around this.

We will amend the calculation as follows:

We have added a "small negative value for XIRR" input and, using the First column flag, have placed it on the timeline in the first time column. This allows XIRR to calculate without having any impact on its value.

![](https://www.financialmodellinghandbook.org/content/images/public/images/0972f71a-fc0a-4c5e-8d55-65609c5000a0_1308x501.jpeg)

Step 5: Add XIRR to the output sheet.
-------------------------------------

Select the IRR value in column F and use the Productivity Pack shortcut Ctrl+alt+o to add the output to the output sheet. Move the output from the bottom of the output sheet into the metrics section.

![](https://www.financialmodellinghandbook.org/content/images/public/images/997596c7-cbef-4331-ba0f-8ef9e039cc39_870x378.jpeg)

Step 6: Run the Section completion checklist.
---------------------------------------------

As usual, perform your section completion wrap up steps.

Now that we have IRR calculated, every time we make a change in the model, we will ask ourselves how it will impact IRR. And thanks to the Output sheet, we will be able to track and assess the movements.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--86.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/irr-solution#/portal/signup)
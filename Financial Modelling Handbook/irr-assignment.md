# Modelling IRR - assignment

**Source:** https://www.financialmodellinghandbook.org/irr-assignment

---

Every business has a metric or set of metrics that matter the most.

In a transaction like the one we are modelling here, IRR is typically one of those metrics. Lender coverage ratios also matter. We'll come on to those later.

The project investors will be particularly interested in this metric. Therefore, as a modeller, you have to be interested in it.

It's crucial to develop an intuitive understanding of how changes to your model will impact your most important metrics. We will focus on IRR, but I want you to remember that other metrics will be important in different contexts and behave differently from IRR.

We will begin by modelling the IRR based on the total project cashflows. We can think of this as the "total equity IRR". Since we will acquire a % of the project, we will adapt the calculation to give an IRR specific to the incoming investor. That will come later.

For now, our next job is to calculate the IRR based on total equity cashflows.

IRR is the discount rate that gives a net present value of zero. It is an "iterative" function. We can calculate it manually using a goal seek or the Excel IRR function, which is an embedded goal seek function.

Guidance notes for calculating IRR.
-----------------------------------

As usual, if you want to take a run at this unguided, skip these notes, have a go and check your results against the solution in the next chapter.

### Step 1: What are the ingredients to the calculation?

We will calculate IRR based on the "Net cash flow to equity" line.

The ingredients to calculate Net cash flow to equity are:

*   Equity investment (made at financial close / transaction date)
*   Dividends paid
*   Share capital redemption. In a concession based project like this one, the shareholder would typically be repaid at the end of the concession when the project ends, and the project company is wound up. We have not yet modelled this, so let's use a placeholder for now.

### Step 2: What function to use?

I generally prefer to use the XIRR function. The difference between the IRR and XIRR function is that XIRR uses the actual cash flow dates and returns an annual IRR. The IRR function assumes equal spacing of cash flows and returns an IRR on the same periodic basis as the cashflows. For example, if you feed the IRR function quarterly cashflows, you will get a quarterly IRR. You will then need to convert it to an annual IRR.

To convert a quarterly IRR to an annual IRR, you would use the following function:

Annual IRR = ((1 + Quarterly IRR) ^ 4) - 1

If you use the XIRR function, you will set up a block with both the Net cash flow to equity and the dates. You will "feed" both of these to the function.

Once we have our IRR, we will want to add it to the metrics section of our Output sheet.

Let's see what that looks like in practice.

Download the start file for this assignment:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._  

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--87.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/irr-assignment#/portal/signup)
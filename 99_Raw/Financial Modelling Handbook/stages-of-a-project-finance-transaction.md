# Stages of a Project Finance transaction

**Source:** https://www.financialmodellinghandbook.org/stages-of-a-project-finance-transaction

---

_This is a draft chapter from my forthcoming book - The Project Finance Modelling Handbook. I'm publishing drafts of every chapter online to get as much feedback and input from fellow professionals as possible. My goal is to publish the most useful book on Project Finance Modelling available._

* * *

Project Finance transactions using a competitive tendering process typically go through several distinct phases:

### Bid stage

During the bid stage of a transaction, project sponsors are pulling together multiple different parts of their bid. They are negotiating with EPC and O&M contractors, dealing with multiple lenders, testing different equipment options, etc. Pulling a bid together is a highly complex process. Sponsors are often working under extreme time pressure. The model is a core part of bid preparation and must be available early to perform one of its essential tasks: supporting project negotiations.

At this stage of the process, nothing is fixed. With every change in costs, debt structure and pricing, equipment performance, and multiple other variables, sponsors will want to understand the impact on the metric they care most about - the price or tariff they will bid.

At this stage, it's common to run the model with the sponsor IRR held constant and to evaluate the impact on tariff. At this stage, therefore, sponsor IRR is often an input, and bid tariff an output.

At the bid stage, sponsors will be evaluating debt offers from different lenders. These will include debt-sizing metrics from each lender. These are usually expressed as a target **Debt Service Coverage Ratio ("DSCR")**. Given these constraints, the model will need to calculate the amount of debt the project can support. Therefore, the DSCR is usually an input to the model at this stage, and the resulting leverage is an output.

### Post bid

After bids have been submitted, the preferred bidder will be appointed, and the process will continue with that bidder. Now that bids have been submitted, the tariff is fixed, apart from certain adjustments that are contractually pre-agreed. Any changes to project costs or operating parameters post-bid will result in a change in sponsors equity IRR. Post-bid, therefore, the model is no longer required to calculate the bid price to meet a target IRR. Instead, the IRR will move while the tariff is held constant.

Between the preferred bidder's appointment and the project's financial close, the debt package is being finalised with selected lenders. The leverage, therefore, remains an output of the model as project parameters change while the debt sizing requirements are held constant.

### Post financial close

At the project's financial close, the debt package is finalised. The drawdown profiles are fixed and written into the credit documentation. Often, at this stage, interest rate swaps are executed. With the debt now fixed, the project leverage becomes an input, and the resulting cover ratios become an output of the model.

The following table summarises how the model needs to perform at different transaction stages.

| Transaction stage | IRR | Tariff | DSCR | Leverage |
| --- | --- | --- | --- | --- |
| Pre-bid | Input | Output | Input | Output |
| Post-bid | Output | Input | Input | Output |
| Post-FC | Output | Input | Output | Input |

Our PF model needs to be set up so we can easily switch between these different "modes" of operation.

When running sensitivities in the model, it's essential to be clear whether we are discussing pre-bid, post-bid / pre-FC, or post-FC sensitivities.

This theme will come up at multiple points throughout the book.

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
Subscribe](https://www.financialmodellinghandbook.org/stages-of-a-project-finance-transaction#/portal/signup)
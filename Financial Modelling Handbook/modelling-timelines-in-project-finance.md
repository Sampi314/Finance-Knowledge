# Timelines in Project Finance models

**Source:** https://www.financialmodellinghandbook.org/modelling-timelines-in-project-finance

---

_This is a draft chapter from my forthcoming book - The Project Finance Modelling Handbook. I'm publishing drafts of every chapter online to get as much feedback and input from fellow professionals as possible. My goal is to publish the most useful book on Project Finance Modelling available. I'd welcome your views and feedback on this chapter._

* * *

How we model the timeline in a Project Finance transaction is crucial to the whole construction of the model.

The timeline of a Project Finance model has to have the flexibility to contend with several specific requirements:

*   The ability to model debt drawdowns monthly during the debt [**availability period**](https://www.financialmodellinghandbook.org/project-finance-glossary/)
     and to match the repayment schedule of the debt during the [**repayment period**](https://www.financialmodellinghandbook.org/project-finance-glossary/)
    .
*   The ability to deal with the specific set of cashflows that occur at Financial Close, particularly considering that Financial Close will not necessarily happen at the end of a modelling period. Our model must calculate interest and fees correctly during the first partial month.
*   The ability to deal with construction delays. Lenders will want to see specific sensitivities around construction delays. In particular, they will want to see if any **[Liquidated Damages](https://www.financialmodellinghandbook.org/project-finance-glossary/)
    ** agreed under the project documentation will be sufficient to keep the project whole in the event of construction delays. The model has to be able to run delay sensitivities as "Post FC sensitivities", i.e. the debt sizing or repayment calculations do not change, and the tariff is held constant.
*   The ability to correctly model contract extensions. Again, these will usually be "Post FC sensitivities".
*   Any procurer-specific requirements around financial statement presentation. It's usually easiest to model the operations period in "contract years" from **[COD](https://www.financialmodellinghandbook.org/project-finance-glossary/)
    **. However, procurers sometimes want financial statements presented in financial or calendar years. This can introduce considerable complexity into the timeline.

There are three approaches most often used to accommodate these requirements into a Project Finance model: the split timeline approach, the hybrid timeline approach, and the "whole model monthly" approach. All three approaches can work, and all three have advantages and disadvantages.

The split timeline approach
---------------------------

With this approach, we have two different classes of sheets in the model. Monthly sheets for the construction period and semi-annual or quarterly sheets for the operating period.

### Advantages of the split timeline approach

*   There is a clear separation between the construction period and the operating period calculations. For example, debt drawdown calculations only appear on the monthly sheets, and depreciation calculations only appear on the operating period calculation sheets.
*   The timeline calculations are simple since each sheet is either monthly or quarterly /semi-annual with no overlap.

### Disadvantages of the split timeline approach

*   There is complexity around passing values between sheets. For example, the debt sizing will done based on operating period CFADS, but is a value needed on the construction period debt drawdown sheets.
*   Financial statements will be presented quarterly or semi-annually. Therefore, every key monthly line item will have to be aggregated to match the periodicity of the financial statements.
*   Delay sensitivities calculations can be more complex since the delay has to affect both the construction period and operating period sheet.

The hybrid timeline approach
----------------------------

With a hybrid timeline model, every sheet has the same timeline, with a first set of columns representing the monthly construction periods, followed by columns set up to represent the quarterly or semi-annual operating periods.

### Advantages of the hybrid timeline approach

*   Every sheet has the same timeline
*   It's not necessary to pass values between sheets. For example, debt drawdowns and repayments can be accommodated within a single debt balance calculation.

### Disadvantages of the hybrid timeline approach

*   There is some additional "weight" to the timeline calculations since every column needs to have the flexibility to be a monthly column if it's during construction or a quarterly or semi-annual column if it's during operations.
*   Reduced visibility of operating calculations. Where a calculation does not have a monthly component, for example, depreciation, the calculation will be preceded by blank monthly columns and will require the user to scroll to the right to see the calculation.

The whole model monthly approach
--------------------------------

Back in the days of Excel 2003 and before, it wasn't possible to model a typical 25 to 30-year timeline on a monthly basis; there weren't enough columns in Excel. However, after Excel 2007, this constraint no longer applied. It became possible to model a PF transaction on a monthly basis throughout.

### Advantages of the whole model monthly approach

*   Maximum timeline flexibility. With a monthly model, we can accommodate quarterly or semi-annual timelines; the transition from construction to operations, from availability period to repayment and so on can be modelled with complete flexibility
*   Every sheet in the model has the same timeline.

### Disadvantages of the whole model monthly approach

*   Models become very large due to the number of columns being used. This can slow calculation time.
*   Many columns of the model are completely blank. With a semi-annual debt repayment, for example, five out of every six columns have no values. The user, therefore, has to spend a lot of time scrolling to the left and right to see values.

The approach used in this book
------------------------------

In my view, the hybrid timeline approach gives the best combination of flexibility and clarity. It allows every sheet to have the same timeline without encumbering the model with the file size and blank columns that a monthly model provides.

_In the next chapter, we'll look at how we set up the hybrid timeline in a Project Finance Model._  

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
Subscribe](https://www.financialmodellinghandbook.org/modelling-timelines-in-project-finance#/portal/signup)
# The critical last step: The Model Release Checklist

**Source:** https://www.financialmodellinghandbook.org/model-release-checklist

---

_This chapter is additional reading to accompany The Financial Modelling Handbook. To read the full handbook and obtain all the worked examples files, you can [buy the handbook here](https://buyfinancialmodellinghandbook.org/basket/?ref=financialmodellinghandbook.org)
._

* * *

Assuming you have been undertaking the [Section completion checklist](https://www.financialmodellinghandbook.org/section-completion-checklist/)
 regularly throughout the model build process,  you will have already picked up issues of spelling, label capitalisation and so on.

It's time to do a final review of the model.  

Checklist items
---------------

*   Input review
*   Software review
*   Check for placeholders
*   Set sheet zoom across all sheets
*   Reset focus to A1
*   Collapse all grouping
*   Check print settings
*   Check for duplicate row labels
*   Sense check units
*   Check Range Names for errors, unused names and hidden names.

Input review
------------

Often, while we are building our model, we can "play around" with inputs to test calculations. We also might not know certain inputs early in the model build process and put in temporary assumptions that we forgot to mark.

It's critical, then, to ensure that we review our model inputs before we release the model. **Ideally, you want a second pair of eyes for this job.** At this stage, you may be too close to the model, and it will be easier for you to miss critical inputs.

This happened to me when writing this book. I left some incorrect inputs in the model, which early readers of the book picked up. _I was too close to the model to notice, even though I did check._ It happens to us all.

A "second pair of eyes" review will help you pick up these silly but often costly mistakes.

Check for placeholders
----------------------

The point of placeholders is to be able to find temporary line items or hacks before we release a model. Therefore, it is critical that you check for placeholders before releasing the model.

See [this guide on how to create a list of placeholders.](https://www.financialmodellinghandbook.org/how-to-create-a-list-of-placeholders/)

Set sheet zoom across all sheets
--------------------------------

Very often, you end up with a variation of zoom settings as you work in different sheets.

Reset across all worksheets:

Ctrl+shift+6 to activate utilities, Alt+a to select all sheets, 1 to run zoom setting macro

You will be asked to enter the zoom setting you want across all sheets. Enter a number between 1 and 100 to set the zoom across all selected sheets.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/1-20.jpg)

Reset focus to cell A1
----------------------

Excel remembers where you were working on a sheet by sheet basis. You may not always want recipients of a model to know where you were last working in the model.

Ctrl+shift+6, Alt+a to select all sheets, then 2 to reset focus to cell A1

This will run through all selected sheets and set cell A1 as the active cells.

Collapse all grouping
---------------------

It can helpful for recipients to receive the model with all the grouping collapsed. This allows them to more easily grasp the big picture of what's in the model without being overwhelmed by the detail.

Ctrl+shift+6, Alt+a to select all sheets, then 6 to collapse all grouping

Check print settings
--------------------

People very rarely print excel workbooks, but if they do want to print a section you want to make sure that the print set-up doesn't have the name of an old project or client.

Ctrl+shift+6, Alt+a to select all sheets, then 8 to change print header settings

This will allow you to change any project or client name in the print header settings.

Check for duplicate row labels
------------------------------

See [this guide on how to check for duplicate row labels](https://www.financialmodellinghandbook.org/how-to-check-for-duplicate-row-labels-in-a-financial-model/)

Sense check model units
-----------------------

See [this guide on how to sense-check the units in your model](https://www.financialmodellinghandbook.org/how-to-sense-check-the-units-in-your-model/)

Check Range Names for errors or unused Names
--------------------------------------------

See t[his guide on how to check for Range Name errors, unused Names or hidden Names](https://www.financialmodellinghandbook.org/how-to-check-for-range-name-errors-unused-names-and-hidden-names/)
.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero-12.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/model-release-checklist#/portal/signup)
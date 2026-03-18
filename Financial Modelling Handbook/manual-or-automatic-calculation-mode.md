# The benefits of working in manual calculation mode

**Source:** https://www.financialmodellinghandbook.org/manual-or-automatic-calculation-mode

---

Throughout the book and my online courses, you'll notice that we operate in manual calculation mode.  

If you're used to operating in automatic calculation mode, this will probably irritate you for a while.

There are good reasons for it.

Usually, in models, inputs, calculations and outputs are separate. Therefore, we are not looking at outputs when we change inputs or calculations. We can't immediately see the impact of our changes since we are not looking at them when we change them.

I'm in charge of when the model calculates in manual calculation mode. Therefore, I can change inputs or calculations and then go and look at critical outputs like IRR or lender coverage ratios. If I calculate while I'm looking at these things, I have a much better sense of how the model reacts to my changes.

There are several keystrokes that you need to know related to model recalculation:

Shift+F9

This only recalculates the active sheet. This can be useful. You can, for example, see the impact of a change you just made on the calculations you are working on. Then later, go and look at the financial statements or output sheet, do a complete recalculation, and see the wider model impact.

F9

This calculates only the cells that have changed since you last recalculated and any cells that are dependent on those. Be careful with this one. Excel has been known not to recalculate everything that should be recalculated.

Ctrl+Alt+F9

This forces a complete recalculation of everything in the model. It is the safest calculations keystrokes.

Shift+Ctrl+Alt+F9

This forces a complete recalculation and rebuilds the dependency tree inside excel. This can be useful if you're finding that F9 on its own is not calculating the model correctly.

How calculation mode is set in Excel
------------------------------------

The calculation mode is a workbook level setting in Excel. Excel saves the setting with the workbook.

The first workbook you open in a session of Excel sets the calculation mode for that session. The calculation model will not change unless you manually change it in Excel's options.

For example, imagine that Excel is not running.

You double click on a workbook to open that file. Clicking on the workbook causes Excel to launch.

If the workbook you opened were set to manual calculation mode, Excel would be in manual calculation mode when it opens.

If the following file you open was saved in automatic calculation mode, Excel will ignore this and remain in manual calculation model.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--113.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/manual-or-automatic-calculation-mode#/portal/signup)
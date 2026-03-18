# Apple has done us dirty

**Source:** https://www.financialmodellinghandbook.org/apple-has-done-us-dirty

---

In [the most recent development sprint](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack/)
 on the Productivity Macros, we focused on getting all of the new and existing keystrokes working on Excel for Mac.

This turned out to be more challenging than expected.

Excel for Mac cannot "see" some of the modifier keys that we use in the macros - specifically the Command or Option key (Alt key on Windows). This much we knew. There used to be a [Python-based workaround](https://macexcel.com/examples/setupinfo/detectkeypress/?ref=financialmodellinghandbook.org)
.

However, Python is no longer built into Monterey, the latest macOS upgrade.

Patrick O'Beirne, one of the VBA developers who work on the macros, [has written about the issue in more detail on his blog](https://sysmod.wordpress.com/2022/03/23/excel-for-mac-vba-onkey-macros-and-macos-monterey/?ref=financialmodellinghandbook.org)
.

This left us with some tricky keystroke decisions. Many people have used the macros for many years, and the keystrokes are "baked in" to existing training materials. We wanted to avoid changing existing windows keystrokes as much as possible.

A number of our macros use the Ctrl+alt keyboard combination. These are the ones that caused us the problem.

Patrick has come up with a clever solution that does allow the Option key to be used, just not in the Ctrl+Option configuration. This has allowed us to leave the Windows shortcuts unchanged and create Mac-specific versions of the Ctrl+alt keystrokes.

These keystrokes are activated using Shift+Control+Option.

I know. It's a lot.

But in testing, I found that the position of those keys on the Mac means that they're not difficult to press together, and the replacement is consistent, meaning you can use the combination across all Ctrl+alt keystrokes.

I'll be updating all of the relevant sections of the handbook with the Mac-specific keystrokes.

In the meantime, I'd appreciate our Excel for Mac users [testing out the latest version](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack/)
.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--56.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/apple-has-done-us-dirty#/portal/signup)
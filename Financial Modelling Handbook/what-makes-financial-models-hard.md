# What makes financial models hard to read

**Source:** https://www.financialmodellinghandbook.org/what-makes-financial-models-hard

---

\=IF( AND( Assumptions!K4 = Workings!H10, Assumptions!F39 = Assumptions!L17), IF(OR( Workings!K2 = Output!J30, Workings!H9 = Data!G10), OFFSET(Workings!F8, Data!F2, Data!F3), IF( ROUNDUP( INDEX( Data!E17:E32,MATCH(Metrics!F10, Data!F9:F15, 0)), Assumptions!F35), Ops!F29, Metrics!F15)))

How often have you opened a model and come across a formula like this? You know that if you want to make sense of it, you will spend way more time than you'd like.

And this formula is by no means the worst you'll see.

So what makes formulas like this hard to read?

Firstly, it's just long. A lot is going on. Long formulas with lots of nested IFs are a disaster. They are impossible to understand and impossible to test. You'll see throughout the book that we keep formulas as short and straightforward as possible. The way we do this is to break up calculations into smaller steps. Long formulas are just formulas trying to do too much all at once.

Secondly, there are a lot of off-sheet references. This means that in trying to decode the formula, we also have to be trawling around the model trying to figure out what each of these numbers is, where it comes from and what it's doing in the formula.

These two things, long formulas and off-sheet references, often occur together.

A third thing is daisy chains. That's where we have links in our formulas that refer to other links, that refer to other links, and so on. We'll talk more about daisy chains later.

Most of us are self-taught modellers. When we start out in modelling, we all do these things. And we often don't think about them, which is the point. As soon we do think about them, we realise that they are a horrible idea.

#### More horrible formulas

If you want some more examples - check [this one](https://www.financialmodellinghandbook.org/p/another-horrible-excel-formula)
 out.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--15.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/what-makes-financial-models-hard#/portal/signup)
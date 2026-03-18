# The five types of flags

**Source:** https://www.financialmodellinghandbook.org/the-five-types-of-flag

---

I'm lazy. And so, I’m constantly on the lookout for hacks. I am a huge fan of reusing calculation blocks. I'm continually asking myself, "Have I built this before? Can I reuse a block?".

There are only five kinds of flags you will ever need in your model. In this section, we look at each one.

Download the worked example file to see each type of flag:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

There are numerous ways to get to the same answer using different formulas and approaches. That's one of the things that makes working in Excel so enjoyable.

You don't need to use my suggested approaches exactly. If you prefer a different approach, use that. The critical thing is to pick a system and stick to it.

Having a library of reference code that you use is a great way to avoid Stupid Unnecessary Thinking Time.

![](https://www.financialmodellinghandbook.org/content/images/public/images/1a8f0f2b-8cad-4121-9ebf-66a037955cbb_2084x976.jpeg)

The five types of timing flags

Flag Type 1: Period in which a specific event occurs
----------------------------------------------------

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/2-8.jpg)

### Typical uses

*   Transaction dates / financial close dates
*   "First dates" for anything - e.g. First operating date, First debt repayment date
*   "Last dates" for anything - e.g. Last construction period date, Last debt repayment date

### Modelling

The objective of the modelling is to find the period in which a single target-date occurs. If you are sure that the target date is a period end date, you can compare the target date to the model end period. If not, you can use the approach from the worked example file. This will highlight a target date if it occurs anytime within a given period.

Flag type 2: Periods before a specific event
--------------------------------------------

![](https://www.financialmodellinghandbook.org/content/images/2022/11/3-7.jpg)

### Typical uses

*   "Actuals" periods in rolling actuals vs forecast models
*   Pre-refinancing dates in models with refinancings

### Modelling

The objective of the modelling is to highlight all periods that occur before a particular date. It would usually be safer and cleaner to ensure that the target date is a period end date, but it doesn't have to be.

Flag type 3: Periods after a specific event
-------------------------------------------

![](https://www.financialmodellinghandbook.org/content/images/2022/11/4-7.jpg)

### Typical uses

*   "Forecast" periods in rolling actuals vs forecast models
*   Post-refinancing dates in models with refinancings
*   Post-contract dates

### Modelling

The objective of the modelling is to highlight all the periods that occur after a particular target date.

Flag type 4: Periods in between two events
------------------------------------------

![](https://www.financialmodellinghandbook.org/content/images/2022/11/5-7.jpg)

### Typical uses

*   Contract periods
*   Debt repayment periods
*   Construction periods

### Modelling

The objective is to highlight all the dates between a target start and end date. This flag will need both of these flags as ingredients. As you can see in the worked example, we are using an AND statement so that the calculation logic highlights periods where the model timeline date is in between the target dates.

With an AND statement, all the conditions within the function brackets must resolve to TRUE for the statement as a whole to return a TRUE. For example:

With the formula:

IF( AND( Condition1, Condition2, Condition3)), 1, 0)

All three conditions must be true for the IF statement to return a 1.

If any conditions are not true, the IF statement will return a 0.

Flag type 5: Recurring events
-----------------------------

![](https://www.financialmodellinghandbook.org/content/images/2022/11/6-5.jpg)

### Typical uses

*   Tax payment dates
*   Debt repayment dates
*   Ratio calculation dates

### Modelling

There are many possible ways of modelling recurring date flags. The approach shown in the worked example is only one possible method.

I have shown annual, semi-annual and quarterly flag approaches in the worked example file. Note that the worked example uses a monthly timeline. The approach would change if the timeline of your model were different.

The semi-annual and the quarterly flags use an OR statement.

With an OR statement, any of the conditions within the function brackets can resolve to TRUE for the statement as a whole to return a TRUE. For example:

With the formula:

IF( OR( Condition1, Condition2, Condition3)), 1, 0)

If any of the three conditions are true,  the IF statement will return a 1.

### Writing the formulas without using IF statements.

Some people prefer to avoid using IF statements when writing flag formulas. I have given examples of this in the "No IFs" sheet of the worked example file.

As I said - there are many ways to get the same result in Excel.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--119.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/the-five-types-of-flag#/portal/signup)
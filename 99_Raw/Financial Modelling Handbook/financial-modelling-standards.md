# Financial Modelling Standards

**Source:** https://www.financialmodellinghandbook.org/financial-modelling-standards

---

The system that I'm going to teach you in this book is based on the FAST Standard. It's one of a number of modelling standards that exist.

In this chapter, I'm going to give an overview of what's already out there so that you can learn from what other people have discovered about standardising models and developing a repeatable system.

In the previous chapters, I mentioned that there are two parts to an effective modelling system; the structure of the model, and the workflows that you use within it.

The modelling standards tend to talk more to the structure of the model and address the question - "what makes a well-structured model?"

### Error reduction

There are two broad categories of error in building financial models.

**Commercial / conceptual errors.** These kinds of errors come from not fully understanding what we're trying to model. We have perhaps modelled our understanding correctly, but it does not reflect the reality of the business.

For example, we might model debt interest using an act/365 day count convention when an act/360 should have been used. The calculation mechanics are all correct, but we're using an incorrect assumption leading to an incorrect result.

**Formula/calculation errors.** We may have understood how the business works and how we _should_ model it, but make formula or structural errors. There are many varieties of these kinds of mistakes. For example linking to the wrong ingredient in our calculation, hard coding incorrect values into formulas, formula inconsistencies etc.

**Standards do not reduce the incidence of modelling errors**. Human beings will continue to make errors at a consistent rate. To quote [Ray Panko](https://www.researchgate.net/publication/1912352_Spreadsheet_Errors_What_We_Know_What_We_Think_We_Can_Do?ref=financialmodellinghandbook.org)
:

> "Humans are incapable of doing complex cognitive tasks with great accuracy. Even for simple cognitive tasks, such as flipping switches, error rates are about one in 200. For more complex cognitive tasks, such as writing lines of computer code, error rates are about one in 50 to one in 20."

While standards do not change the error rate, they make it less likely that errors will go unnoticed.

They do this by reducing variability in the modelling approach. If the model is built to a common standard, the modeller knows what to expect from the structure. The easier a model is to review, the more likely errors will be detected.

Additionally, common to all standards is a focus on making models as simple as possible.

### Increased individual productivity

When we do things the same way, we get better at them. If the model is highly structured, macro tools can be introduced to do repetitive tasks and therefore cut down the model build time. Code can be easily reused. Model build mechanics can more easily become part of "muscle memory".

### Increased team productivity

Having everybody on a team model, in the same way, makes collaboration easier. One part of the model can be built by one person and continued by another. It's easier for modellers to review and share each's other work. Unnecessary thinking time is reduced.

How common is the use of modelling standards?
---------------------------------------------

According to the 2021 Financial Modelling Survey, **95% of modellers believe that standards are important**. 41% of modellers work in organisations where standards are applied rigorously. In professional services firms, this figure goes up to 64%. Of those who use a standard, the majority use an in-house code of best practice.

So while modellers believe that standards are important, and many are following a standard, outside professional services, most are not.

An overview of standards
------------------------

### ICAEW modelling code

The ICAEW Financial Modelling Code is a great place to start. It gives a series of recommendations for good spreadsheet practice. It's been compiled by a broad group of practitioners and so has wide applicability to different user requirements.

### FAST

The approach that I use and teach is based on FAST. FAST is highly prescriptive and certainly not everybody's cup of tea. Some people dislike (quite strongly!) the use of links or "call-ups" throughout the model and the fact that this increases the number of rows it takes to complete a calculation.

FAST stands for:

**Flexible:** To be effective, the structure and style of models require flexibility for both immediate usage and the long term.

**Appropriate:** Models must reflect key business assumptions directly and faithfully without being cluttered in unnecessary detail.

**Structured:** Rigorous consistency in layout and organisation is essential in retaining the model's logical integrity over time, particularly as a model's author may change.

**Transparent:** Effective models are founded upon simple, clear formulas that can be understood by other modellers and non-modellers alike.

FAST is "open-source" and maintained by a not-for-profit company called the FAST Standards Organisation. Unfortunately, not much development has gone into FAST over recent years which is somewhat of a missed opportunity.

### Smart / Mazars financial modelling standard.

SMART became the Mazars financial modelling standard after Mazars acquired Corality (who originated SMART).

They have a list of guiding philosophies that many professional modellers would agree with:

*   Use plain English, not Excel-speak
*   Meaningful calculations
*   Everything labelled with a title and units
*   Use headings to organise sections, like a report
*   From left to right, top to bottom
*   Format formulas for reading
*   Don't hide anything
*   Cover page and contents page
*   Consistent labelling structure
*   Professionally present every part of the model
*   Apply purposeful and consistent formatting
*   Graphs are worth a thousand numbers
*   Use simple grouping
*   Complementary colours
*   Logical hierarchy of labels that helps the user find what they are looking for quickly and easily
*   Separate inputs, calculations and outputs
*   Label, colour and group worksheets

### PwCs Global Financial Modelling Guide

A recent addition to this field is PwCs Global Financial Modelling Guidelines document published in January 2020. It's a well put together document with enough detail to be applicable in practical terms, and broad enough to apply to most time series modelling situations.

The document is made up of 5 core principles and 10 practical model design guidelines. The "Essence of spreadsheet evil section" is also well worth reading.

The five guiding principles include some useful thinking, clearly borne out of decades of collective modelling wisdom. These are:

*   Maximum simplicity consistency and transparency;
*   Minimise risk of errors, misinterpretations or incorrect use;
*   Minimize the scope for queries or issues from a model review or audit;
*   Provide universal applicability for any time series models
*   Provide a framework for building models that are user-friendly and fit for purpose

### Operis / "named range" approach

Operis and a number of other companies apply an approach that, on the surface, appears quite different but which has the same level of discipline and structure as the others, and adheres to a lot of the same principles.

Their system makes extensive use of "named ranges" in the model build. It's a highly systematic and well thought through process for modelling. Where FAST uses calculation blocks to ensure that the precedents to formulas are visible and easily read alongside the formula, by naming everything, the "Operis" approach means that formulas can be "read" like sentences.

Like the extensive use of call-ups in FAST, the extensive use of named ranges is not to everybody's taste.

### BPM

BPM was the first to systematically codify a modelling standard back in 2003. BPM is now under the Modano brand. There is an interesting tool on the Modano website which allows you to customise your own spreadsheet best practice guidelines.

Conclusion
----------

I recommend that you find what each of these has to offer and how it might develop your own thinking. Compare to what I'm teaching in this book and find an approach that works for you.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--7.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/financial-modelling-standards#/portal/signup)
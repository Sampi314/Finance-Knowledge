# An introduction to financial modelling standards

**Source:** https://www.fullstackmodeller.com/blog/an-introduction-to-financial-modelling-standards

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/An%20Introduction%20to%20Financial%20Modelling%20Standards.png)

An Introduction to Financial Modelling Standards
================================================

Published [by Kenny Whitelaw-Jones](https://www.fullstackmodeller.com/blog/author/kenny-whitelaw-jones)

Feb 10, 2022 8:59:12 AM

### The different modelling standards are more alike than they are different. They all emphasise similar elements of good practice. What’s important is to pick one and apply it consistently.

When I started in financial modelling, I worked for one of the Big 4.

As part of my induction week with other new joiners in the Corporate Finance team, we had several days of modelling training.

It wasn’t good.

Dull, irrelevant and delivered by a guy who hadn’t seen an actual transaction for decades.

What he told us about modelling was wholly detached from what was happening “on the shop floor”.

As this training was worse than useless, I had to learn on the job. I did this by reverse-engineering the deal models colleagues were using.

I tried to copy the approaches I saw as best I could.

Unfortunately, the models I was copying were also not very well built. And so, I just taught myself bad habits.

A few years later, I met the founders of FAST, John Richter and Morten Siersted. I was blown away by the thought that had gone into how to structure a model well, borne out of just the kind of experiences I’d also had.

It was the first time I became aware that there was such a thing as a modelling standard.

Why do modelling standards make a difference?
---------------------------------------------

### Error reduction

There are two broad categories of error in building financial models.

**Commercial / conceptual errors.** These kinds of errors come from not fully understanding what we’re trying to model. We have perhaps modelled our understanding correctly, but it does not reflect the reality of the business.

For example, we might model debt interest using an act/365 day count convention when an act/360 should have been used. The calculation mechanics are all correct, but we’re using an incorrect assumption leading to an incorrect result.

**Formula/calculation errors.** We may have understood how the business works and how we _should_ model it, but make formula or structural errors. There are many varieties of these kinds of mistakes. For example linking to the wrong ingredient in our calculation, hard coding incorrect values into formulas, formula inconsistencies etc.

**Standards do not reduce the incidence of modelling errors**. Human beings will continue to make errors at a consistent rate. To quote [Ray Panko](https://www.researchgate.net/publication/1912352_Spreadsheet_Errors_What_We_Know_What_We_Think_We_Can_Do)
:

> “Humans are incapable of doing complex cognitive tasks with great accuracy. Even for simple cognitive tasks, such as flipping switches, error rates are about one in 200. For more complex cognitive tasks, such as writing lines of computer code, error rates are about one in 50 to one in 20.”

While standards do not change the error rate, they make it less likely that errors will go unnoticed.

They do this by reducing variability in the modelling approach. If the model is built to a common standard, the modeller knows what to expect from the structure. The easier a model is to review, the more likely errors will be detected.

Additionally, common to all standards is a focus on making models as simple as possible.

### Increased individual productivity

When we do things the same way, we get better at them. If the model is highly structured, macro tools can be introduced to do repetitive tasks and therefore cut down model build time. Code can be easily reused. Model build mechanics can more easily become part of “muscle memory”.

### Increased team productivity

Having everybody on a team model in the same way makes collaboration easier. One part of the model can be built by one person and continued by another. It’s easier for modellers to review and share each’s other work. Unnecessary thinking time is reduced.

Who is using standards?
-----------------------

According to the [2021 Financial Modelling Survey](https://www.fullstackmodeller.com/resources/ebooks)
 **95% of modellers believe that standards are important**. 41% of modellers work in organisations where standards are applied rigorously. In professional services firms, this figure goes up to 64%.

Of those who use a standard, the majority use an in-house code of best practice:

![Image of bar chart from 2021 Financial Modelling survey ](https://www.fullstackmodeller.com/hubfs/Image%20of%20bar%20chart%20from%202021%20Financial%20Modelling%20survey%20.webp)

So while modellers believe that standards are important, and many are following a standard, outside professional services, most are not.

Modelling standardisation is hard to achieve.
---------------------------------------------

I’ve taught thousands of modellers from many of the world’s top companies over the years. And what I’ve seen is this: in all but a handful of dedicated modelling shops, it’s hard for companies to achieve standardisation across a team.

People have their own preferences. And these have often been built up over years of practice. It’s challenging and painful for them to change. And they may not be convinced that what they are switching to is better. And indeed it may not be.

**As software developer Paul Graham said, “programming languages are not merely technologies, but habits of mind as well, and nothing changes slower.”**

Just pick one.
--------------

There are several modelling standards. Overall, they are similar in more ways than they are different. They all emphasise similar elements of good practice; the separation of inputs, calculation and outputs; consistency of structure and layout; clarity of labelling etc.

What’s important is that you pick a standard and follow it. This is more important than the particular choice of standard that you use. I’ve provided links to find out more about each of the standards mentioned at the end of the article.

### ICAEW modelling code

The ICAEW Financial Modelling Code is a great place to start. It gives a series of recommendations for good spreadsheet practice. It’s been compiled by a broad group of practitioners and so has wide applicability to different user requirements.

### FAST

The approach that I use and teach is based on FAST. FAST is highly prescriptive and certainly not everybody’s cup of tea. Some people dislike (quite strongly!) the use of links or “call ups” throughout the model and the fact that this increases the number of rows it takes to complete a calculation.

FAST stands for:

**Flexible:** To be effective, the structure and style of models require flexibility for both immediate usage and the long term.

**Appropriate:** Models must reflect key business assumptions directly and faithfully without being cluttered in unnecessary detail.

**Structured:** Rigorous consistency in layout and organisation is essential in retaining the model’s logical integrity over time, particularly as a model’s author may change.

**Transparent:** Effective models are founded upon simple, clear formulas that can be understood by other modellers and non-modellers alike.

FAST is “open-source” and maintained by a not-for-profit company called the FAST Standards Organisation. Unfortunately, not much development has gone into FAST over recent years which is somewhat of a missed opportunity.

### Smart / Mazars financial modelling standard.

SMART became the Mazars financial modelling standard after Mazars acquired Corality (who originated SMART).

They have a list of guiding philosophies that most professional modellers would agree with:

*   Use plain English, not Excel-speak
*   Meaningful calculations
*   Everything labelled with a title and units
*   Use headings to organise sections, like a report
*   From left to right, top to bottom
*   Format formulas for reading
*   Don’t hide anything
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

### Operis / “named range” approach

Operis and many other companies apply an approach that, on the surface, appears quite different but which has the same level of discipline and structure as the others, and adheres to a lot of the same principles.

Their system makes extensive use of “named ranges” in the model build. It’s a highly systematic and well thought through process for modelling. Where FAST uses calculation blocks to ensure that the precedents to formulas are visible and easily read alongside the formula, by naming everything, the “Operis” approach means that formulas can be “read” like sentences.

Like the extensive use of call-ups in FAST, extensive use of named ranges is not to everybody’s taste.

### BPM

BPM was the first to systematically codify a modelling standard back in 2003. BPM is now under the Modano brand. There is an interesting tool on the Modano website which allows you to customise your own spreadsheet best practice guidelines.

Who cares in the end?
---------------------

Most of us don’t care what language an app is written in. We care about the user experience and whether the app does what we need. We rely on the software developer’s expertise to make sure that all the “behind the scenes” coding works.

Similarly, while modellers can get wound up about which approaches are best, in the end, many clients and users don’t care.

**They rightly rely on us to ensure that the model is well built and free of material errors, and critically, that it gives them the answers they need, quickly.**

Resources
---------

*   ICAEW: [Download the code](https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx)
     // Follow [David Lyford-Tilley](https://www.linkedin.com/in/davidlyfordsmith/)
    
*   FAST: [Download the code](https://www.fast-standard.org/wp-content/uploads/2019/10/FAST-Standard-02c-July-2019.pdf)
     // Follow [Andrew Berkley](https://www.linkedin.com/in/andrewberkley/)
    
*   Mazars: [Find out more](https://financialmodelling.mazars.com/)
     // Follow [Rickard Wärnelid](https://www.linkedin.com/in/warnelid/)
    
*   [Modano modelling guidelines](https://www.modano.com/guidelines)
    .
*   Gridlines [Essential Financial Modelling](https://academy.gridlines.com/p/essential-financial-modelling)
     is a free course on building a complete three statement financial model, based on FAST.
*   Download the Full Stack Modeller [2021 FINANCIAL MODELLING SURVEY REPORT](https://www.fullstackmodeller.com/resources/ebooks)
    

This post was originally published in the [Financial Modelling Handbook](https://www.financialmodellinghandbook.org/)

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fan-introduction-to-financial-modelling-standards)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fan-introduction-to-financial-modelling-standards)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fan-introduction-to-financial-modelling-standards)
    

![Award_Winning](https://www.fullstackmodeller.com/hubfs/badge.jpg)

Become a Modelling Pro
----------------------

Join us and we'll unlock your full potential.

Our award-winning training programme, and exclusive global community, will guide you on your way to Excel, Financial Modelling, data visualisation & analytics mastery.

[Join as an Individual](https://www.fullstackmodeller.com/full-stack-membership)
 [Register Your Team](https://www.fullstackmodeller.com/team-training)

Latest Blogs
------------

*   [New Year, New You?](https://www.fullstackmodeller.com/blog/full-stack-modeller-new-year-new-you)
    
*   [New Import Functions](https://www.fullstackmodeller.com/blog/excel-importtext-importcsv)
    
*   [Best Practice Confessions & Terminology Overload](https://www.fullstackmodeller.com/blog/unpivot-episode-40-full-stack-modeller)
    
*   [Excel Meetup Groups](https://www.fullstackmodeller.com/blog/excel-meetup-groups)
    
*   [New Features and Common Data Problems](https://www.fullstackmodeller.com/blog/unpviot-episode-39)
    
*   [More AI Hype and Traps to avoid when modelling](https://www.fullstackmodeller.com/blog/unpviot-episode-38)
    
*   [The Excel World Championship Song](https://www.fullstackmodeller.com/blog/excel-world-championship-song)
    
*   [The Advanced Financial Modeler Certificate from FMI](https://www.fullstackmodeller.com/blog/advanced-financial-modeler)
    
*   [The history of Microsoft Excel](https://www.fullstackmodeller.com/blog/history-of-excel)
    
*   [My main learning from the FMI AFM exam](https://www.fullstackmodeller.com/blog/financial-modeling-institute-fmi-afm-learnings)
    

#### Subscribe to our monthly modelling newsletter
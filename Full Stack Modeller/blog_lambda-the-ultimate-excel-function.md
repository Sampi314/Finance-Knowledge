# LAMBDA - The Ultimate Excel Function?

**Source:** https://www.fullstackmodeller.com/blog/lambda-the-ultimate-excel-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/LAMBDA%20%E2%80%93%20The%20Ultimate%20Excel%20Function.png)

LAMBDA – The Ultimate Excel Function?
=====================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Feb 16, 2022 10:18:21 AM

The release of LAMBDA has been celebrated as a seminal moment for Microsoft Excel – paralleled only by the Pivot Table back in 1994. And this comes hot on the heels of Data Types and Dynamic Array functionality. It’s an exciting time for us Excel geeks.

#### LAMBDA – The Great Promise

“With LAMBDA users can now create their own functions”. OK, this sounds exciting. I can see a spreadsheet full of =MYLES() functions spreading around the world.

“LAMBDAS can return LAMBDAS, so you can do currying. GREAT! I do love curry.

“You can define a fixed-point combinator using LAMBDA and hence write recursive functions”. Righty ho.

“With LAMBDA, Excel has become Turing-complete”. Say what now?

Let’s unpick what all this means. 

#### LAMBDA – Creating your own functions

We have always been able to build our own functions in Excel. Up until now, this was achieved using VBA to create “User-Defined Functions” (UDFs). 

The challenge with UDFs is that you need to know Excel’s VBA language to create them, and they are pretty much a mystery to 99% of Excel users. This can restrict the useability of a model to a small subset of users whose skills are way beyond the norm, and creates a challenge for model collaboration and audit.

LAMBDA brings this functionality to the masses.

But do the masses actually need to create their own functions?

I’m not convinced they do.

When I design a model my focus is on good structure and simplicity. By that, I mean laying out the data or calculations in clear, well-structured blocks where the calculation logic is easy to follow. I use the simplest possible set of functions.

And I really do mean simple, I rarely use more than SUM, IF, SUMIFS, INDEX, and XLOOKUP.

Now I’d be lying if I said that in the past I haven’t wished I could create my own functions. A few years ago I would certainly have used LAMBDA to create MYLESIFS(),  MYLESSUMIFS(), MYLESIFERROR(), and MYLESLOOKUP(). 

Luckily Microsoft stepped up and created these much-asked-for functions for us.

#### LAMBDA Curry anyone?

Where LAMBDA really does start getting interesting though is when we start using LAMBDAs as arguments in other LAMBDAs.

LAMBDA provides a way to convert a function that takes multiple arguments into a sequence of LAMBDA functions that each takes a single argument – currying. This then opens the door to creating recursive functions.

Quick shout out for the mathematician Haskell Curry, this is where currying comes from – not the food.

A recursive function works by referring to itself. It works through iteration, coming to the solution by working through multiple instances of the problem. 

Excel’s Goal Seek is a good example of this concept.

In the example below I am using Goal Seek to calculate the turnover needed for a business to break even.

![Excel tutorial gif - LAMBDA](https://www.fullstackmodeller.com/hs-fs/hubfs/Imported_Blog_Media/Final-GIF-3.gif?width=1800&height=1014&name=Final-GIF-3.gif)

We can now create a LAMBDA function to do this. Now that is useful! Some financial modelling applications come immediately to mind.

#### So, should you start adding LAMBDA to all of your models?

Well, put simply, no. Please don’t.

The release of LAMBDA reminds me of a younger version of myself that discovered VBA. Younger Myles, the “VBA aficionado”, added VBA to everything he could. 

VBA definitely had its place back then. I just got over-excited and didn’t use it appropriately.

And this is my concern with LAMBDA.

Used wisely, with structure and proper annotation LAMBDA is going to make a real difference for certain groups of Excel users.

If used badly, I can foresee a dystopian Excelverse of models littered with unnecessary and incomprehensible bespoke functions.

In the next article in this series, I’ll run through some useful applications of LAMBDAs, in particular for financial modelling, and how to make use of the new Advanced Formula Editor.

Read more about LAMBDA [here](https://techcommunity.microsoft.com/t5/excel-blog/announcing-lambdas-to-production-and-advanced-formula/ba-p/3073293)
.

Our Future of Excel series  

-----------------------------

This series of articles focuses on new features soon to be released on Excel. This is based on announcements by the [Microsoft Office Insider](https://insider.office.com/en-gb/)
 team.

See other articles in our Future of Excel series [here](https://www.fullstackmodeller.com/blog/future-of-excel)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Flambda-the-ultimate-excel-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Flambda-the-ultimate-excel-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Flambda-the-ultimate-excel-function)
    

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
# Financial Modeling Institute (FMI)

**Source:** https://www.fullstackmodeller.com/blog/fmi-afm-exam-6weeks

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/FSO%20introduces%20the%20certification%20for%20FAST%20Level%201.png)

6 weeks to go until the FMI AFM exam
====================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Jan 4, 2025 5:18:31 PM

Join me as I prepare for the Financial Modeling Institute's Advanced Financial Modeler (AFM) exam which next takes place in six week on 22nd February 2025.  

**Preparing for the February 2025 AFM exam  
**
-----------------------------------------------

I will be sitting the FMI Advanced Financial Modeler exam 20 22nd February 2025. In this series, I share my thoughts and learnings as I prepare for the exam.  

You can catch up on my previous posts using the links below:  

[12 weeks to go to the FMI AFM exam](https://www.fullstackmodeller.com/blog/fmi-afm-exam-12weeks)

[11 weeks to go to the FMI AFM exam](https://www.fullstackmodeller.com/blog/fmi-afm-exam-11weeks)

[10 weeks to go to the FMI AFM exam](https://www.fullstackmodeller.com/blog/fmi-afm-exam-10weeks)
[](https://www.fullstackmodeller.com/blog/fmi-afm-exam-11weeks)

[9 WEEKS TO GO TO THE FMI AFM EXAM](https://www.fullstackmodeller.com/blog/fmi-afm-exam-9weeks)

[7 WEEKS TO GO TO THE FMI AFM EXAM](https://www.fullstackmodeller.com/blog/fmi-afm-exam-7weeks)

Here is my latest weekly update with six weeks to go to the AFM exam.

What I covered last week
------------------------

Last week I worked through the three core elements of debt and interest, namely: Interest income;  Senior Debt; and the Revolver.

Let's take a look at each of these.

Interest Income  

------------------

Interest income is the interest received on the cash in the company's bank account. This is a s simple as balance  X  interest rate %.

The FMI allow you to choose either the average balance or the opening balance as the basis for the calculation. Very straightforward.

The interest value feeds into the income statement (for the AFM exam it is combined with debt interest on an "Interest Expense" line).

Senior Debt  

--------------

Senior debt is also pretty straightforward. There are two elements: The debt balance; and the debt interest.

The debt balance is a simple corkscrew where closing balance = opening balance  - debt repayment. The resulting debt balance feeds into the balance sheet and the repayment is reflected on the cash flow statement.

The debt interest is the interest balance  X  interest rate %. The FMI allow you to choose either the average balance or the opening balance as the basis for the calculation.

The debt interest value feeds into the income statement in the "Interest Expense" line.

The Revolver  

---------------

I've never modelled a revolver before so this part of the training took me a little longer to work through. The logic is also a little more involved.

A revolver is a "revolving credit line" that enables a company to borrow money when needed and repay it as cash becomes available.

To model a revolving loan facility we therefore need to consider the following logic flow:

![](https://www.fullstackmodeller.com/hs-fs/hubfs/image-png-Jan-04-2025-05-12-41-9087-PM.png?width=2523&height=2304&name=image-png-Jan-04-2025-05-12-41-9087-PM.png)

The free cash flow balance is Opening cash balance + operating cashflow + investing cashflow + senior debt repayment + common stock + dividend - basically everything on the cashflow apart from the revolver.

The revolver adjust calculation is MIN(Free cash flow balance , Revolver balance) \* -1

That is to say, return the lower of the free cash flow balance and the revolver balance. Multiply the resulting value by -1.

In scenario 1 there is a 100 positive cash balance and a 50 revolver balance to repay. The adjustment value uses 50 of the free cash balance to pay off the revolver.

In scenario 2 there is a 100 positive cash balance but no revolver balance to repay. No adjustment is required.

In scenario 3 there is a 50 negative cash balance. The revolver adjustment is therefore 50, which will bring the cash balance back up to 0.

Having a revolver in your AFM exam model means that the cash balance will never be negative.

Week 7 - 6 weeks to go
----------------------

Having now covered Debt and Interest, my focus for next week is the equity section.

My plan
-------

Below was my original plan by topic areas.

I am still running a little ahead with a week in-hand ahead of the AFM bootcamp.  

![](https://www.fullstackmodeller.com/hs-fs/hubfs/image-png-Nov-26-2024-03-47-48-1001-PM.png?width=1380&height=906&name=image-png-Nov-26-2024-03-47-48-1001-PM.png)

How we support FMI students at Full Stack
-----------------------------------------

Full Stack Modeller is an accredited training provider for the Financial Modeling Institute.

Our core training program covers all the Excel and financial modelling skills that you need to succeed in the FMI exams.

Our FMI [AFM exam Bootcamp](https://www.fullstackmodeller.com/fmi-afm-bootcamp)
, led by Giles Males, MVP and MFM has been designed specifically to support candidates taking the FMI AFM exam.

**Learn from a Master Financial Modeler**
-----------------------------------------

![IMG_2503](https://www.fullstackmodeller.com/hs-fs/hubfs/IMG_2503.jpg?width=612&height=816&name=IMG_2503.jpg)

Giles Male, our co-founder and CEO, has achieved the prestigious, highest level of accreditation from the FMI - The Master Financial Modeler (MFM).  

Learn from the best.

**What is the Financial Modeling Institute?**
---------------------------------------------

![FMI-1](https://www.fullstackmodeller.com/hs-fs/hubfs/FMI-1.png?width=774&height=585&name=FMI-1.png)

The Financial Modeling Institute (FMI) was founded in 2017 with the goal of “Promoting awareness, excellence and discipline in Financial Modeling through world-class accreditation programs”.

The Financial Modeling Institute (FMI) focuses on assessment, leaving the delivery of training to independent and proven partners like us at Full Stack Modeller.

**What are the FMI certification levels?**
------------------------------------------

The Financial Modeling Institute (FMI) has three certification levels. These are: Advanced Financial Modeler (AFM); Chartered Financial Modeler (CFM); and Master Financial Modeler (MFM).

![Advanced-Financial-Modeler-Podium-500x323](https://www.fullstackmodeller.com/hs-fs/hubfs/Advanced-Financial-Modeler-Podium-500x323.jpg?width=759&height=489&name=Advanced-Financial-Modeler-Podium-500x323.jpg)  ![Chartered-Financial-Modeler-Podium-500x323](https://www.fullstackmodeller.com/hs-fs/hubfs/Chartered-Financial-Modeler-Podium-500x323.jpg?width=759&height=489&name=Chartered-Financial-Modeler-Podium-500x323.jpg)  ![Master-Financial-Modeler-Podium-500x323](https://www.fullstackmodeller.com/hs-fs/hubfs/Master-Financial-Modeler-Podium-500x323.jpg?width=753&height=486&name=Master-Financial-Modeler-Podium-500x323.jpg)       

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ffmi-afm-exam-6weeks)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ffmi-afm-exam-6weeks)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Ffmi-afm-exam-6weeks)
    

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
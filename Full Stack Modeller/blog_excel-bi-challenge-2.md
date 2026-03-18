# Excel BI Challenge

**Source:** https://www.fullstackmodeller.com/blog/excel-bi-challenge-2

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTBEFORE%20Function.png)

Excel BI Challenge 2
====================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 16, 2024 11:42:26 PM

_Everything you need to master Excel BI Challenge 2  
_

The challenge
-------------

![Excel BI Challenge 2](https://www.fullstackmodeller.com/hs-fs/hubfs/image-png-3.png?width=2121&height=1242&name=image-png-3.png)

This is the second challenge in the Excel BI challenge series. We are asked to provide a formula to sum the last 3 non-zero values in the range A2:A10.  

The answer should be 44  

Here is the link to the base [Excel BI challenge file](https://lnkd.in/dcvT9VrA)
. You can view the Excel BI LinkedIn post for the challenge [HERE](https://www.linkedin.com/posts/excelbi_excel-advancedexcel-excelchallenge-activity-6966623632219336704-Fkr7/?utm_source=share&utm_medium=member_desktop)
.

Challenge walkthrough with Giles Male
-------------------------------------

Giles has recorded his attempt at this challenge live; no prep, no fluff, just opening the file and getting going. This means that you get to watch Giles' thought process and his journey, "warts and all".

You can watch Giles' walkthrough video on our [Excel on the Road Channel](https://youtu.be/M06onetzTfI?si=HpXYzU40s8kvw7Po)
.

Let's work through this challenge together  

---------------------------------------------

In this article, I am going to work through the core elements of the challenge. I recommend reading this article and then working through the video with the help of our supporting Excel file.

Please download the [supporting Excel file](https://docs.google.com/uc?export=download&id=1G4SNhrivvhs8Izih1e013FyQA68JlXQk)
. This file includes all of the formulas from Giles' walkthrough, complete with the full logic and workings with supporting guidance. It also covers alternative solutions including an Excel Tables-based version and a PowerQuery solution.

Before you get stuck into the video and supporting Excel file, let's step back and think about the logic behind this challenge.

The challenge: We need to sum the last 3 non-zeros values in the range A2:A10.

To sum up the last three non-zeros we are going to need to ignore or filter out any zeros in the data.

Once we have achieved that we need to find a way to identify the last three values in the range.

We then need to sum up those three numbers.

Ok, now that we have the logic in mind let's take a look at the two core elements of the logic flow:

Logic element 1 \- Filter out any zeros in the data  

We need to filter the data in the range A2:A10 to remove any zeros:

\=FILTER(A2:A10,A2:A10>0))

This uses the FILTER function to filter the data to return only values greater than 0

Logic element 2 \- Identify the last three values in the range  

If you aren't aware of the TAKE function then this part of the challenge would be very difficult.

Using the TAKE function it is nice and simple.

\=TAKE(C2#,-3)

Here we use the TAKE function over the range from element 1 to choose the rows to include. Using -3 takes the last three rows from the data.

Finally, let's bring it all together and sum it up:

Bringing the two elements from above together and wrapping it in a SUM gives us the following formula:

\=SUM(TAKE(FILTER(A2:A10,A2:A10>0),-3))

As long as you know the FILTER and TAKE functions this is a pretty simple challenge. To prove that point Giles solves it in just 2 minutes!

Don't worry though, in the [WALKTHROUGH VIDEO](https://www.youtube.com/watch?v=M06onetzTfI&t=303s)
 Giles then explores a number of other functions looking for other solutions and takes a look at a few other people's solutions to the challenge. The workings for this is all documented in the [supporting Excel file](https://docs.google.com/uc?export=download&id=1G4SNhrivvhs8Izih1e013FyQA68JlXQk)
.

I highly recommend that you work through the video alongside the Workings tab of the supporting Excel file and take your time to make sure that you understand each element.

My reflections on the challenge
-------------------------------

On the face of it, this seemed like a simple challenge, with relatively straightforward logic.

And,in fact, it was.

It is important to highlight that we are not saying this is the correct solution (or that focusing on single cell solutions is the right decision overall), it is just where Giles ended up in the live attempt.

Another neat solution, very similar to Giles' but using LET was the formula below from the elusive Victor Momoh:

\=LET(a,A2:A10,SUM(TAKE(FILTER(a,a<>0),-3)))

I explain how this formula works in the Victor Momoh tab of the supporting Excel file.

What is the Excel BI Challenge series?
--------------------------------------

The Excel BI Challenges series has been created by [Vijay A. Verma](https://www.linkedin.com/in/excelbi/)
. It is an (ever-growing) set of Excel-based challenges. Each challenge is designed to test your mastery of Excel-based modelling.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-2)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-2)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-2)
    

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
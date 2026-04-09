# Excel BI Challenge

**Source:** https://www.fullstackmodeller.com/blog/excel-bi-challenge-1

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTBEFORE%20Function.png)

Excel BI Challenge 1
====================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 10, 2024 7:21:59 PM

_Everything you need to master Excel BI Challenge 1  
_

The challenge
-------------

![](https://www.fullstackmodeller.com/hs-fs/hubfs/image-png-2.png?width=2547&height=1005&name=image-png-2.png)

This is the first challenge in the Excel BI challenge series. We are asked to provide a formula to count the number of cells having only 2 words in range A2:A20.

The answer should be 8

Here is the link to the base [Excel BI challenge file](https://onedrive.live.com/view.aspx?resid=E11B26EEAACB7947%217451&authkey=!AP-xFo3uF9DYxuU)
. You can view the Excel BI LinkedIn post for the challenge [here](https://www.linkedin.com/posts/excelbi_excel-excelchallenge-excelsolution-activity-6965972649277624320-yXe7/)
.

Challenge walkthrough with Giles Male
-------------------------------------

Giles has recorded his attempt at this challenge live; no prep, no fluff, just opening the file and getting going. This means that you get to watch Giles' thought process and his journey, "warts and all".

You can watch Giles' walkthrough video on our [Excel on the Road Channel](https://youtu.be/TehyPtX5CbQ?si=KEDN5c_-iMr5RJxk)
.

Let's work through this challenge together  

---------------------------------------------

In this article, I am going to work through the core elements of the challenge. I recommend reading this article and then working through the video with the help of our supporting Excel file.

Please download the [supporting Excel file](https://docs.google.com/spreadsheets/d/1pZXIj_sV7EZfwT-sYUWlPQaO_8EuBw9q/edit?usp=sharing&ouid=114101896430034884524&rtpof=true&sd=true)
. This file includes all of the formulas from Giles' walkthrough, complete with the full logic and workings with supporting guidance. It also covers alternative solutions including a simple, helper-column based version and a PowerQuery solution.

Before you get stuck into the video and supporting Excel file, let's step back and think about the logic behind this challenge.

The challenge: We need to determine how many cells contain two words. If a text string contains two words, it will contain exactly one space.

The first calculation will therefore need to determine which cells contain text with exactly one space. To do this we need to flag cells where the difference in text string length between the original text and the text with all blanks removed is equal to 1.

Once we have this list of cells containing 1 space we then need to count the number of these cells.

Ok, now that we have the logic in mind let's take a look at the two core elements of the logic flow:

Logic element 1 \- Does the text string contain exactly one space?

Giles covers this part of the challenge in the first five minutes of his [walkthough video](https://youtu.be/TehyPtX5CbQ?si=KEDN5c_-iMr5RJxk)
.

You can find all of the details for this step in the Workings tab of the [supporting Excel file](https://docs.google.com/spreadsheets/d/1pZXIj_sV7EZfwT-sYUWlPQaO_8EuBw9q/edit?usp=sharing&ouid=114101896430034884524&rtpof=true&sd=true)
.

Step 1 :

We need to find the length of the text in each cell:

\=LEN(A2:A20)

This uses the LEN function to find the length of the text string in the cell. It also leverages the dynamic array engine to calculate this with the formula entered in just one cell, which then spills down the range.

Step 2:

Next, we need to find the length of the text in each cell if you remove the blanks:

\=LEN(SUBSTITUTE(A2:A20, " ", ""))

This uses the SUBSTITUTE function to replace the blank (" ") with no blank (""). Then LEN is used as it was before.

Step 3:

Finally, we need to find the difference between the text string lengths from step 1 and step 2:

\=LEN(A2:A20)  -  LEN(SUBSTITUTE(A2:A20, " ", ""))

That is the first logical element of the challenge complete.

So now all we need to do is count the number of cells returning a 1.

Simple...

Or is it?

Logic element 2 \- Count the number of cells where the result is 1  

This seems like it really should be very simple. We all know how to count some cells where the value is 1 after all!

Well, it is super simple if you use helper-columns to solve the challenge. I have shown this in the "Simple Solution" tab in the [supporting Excel file](https://docs.google.com/spreadsheets/d/1pZXIj_sV7EZfwT-sYUWlPQaO_8EuBw9q/edit?usp=sharing&ouid=114101896430034884524&rtpof=true&sd=true)
.

The difficulty comes when you try to solve the whole thing in one cell. This is what you will see Giles work through in the rest of his [walkthrough video](https://youtu.be/TehyPtX5CbQ?si=KEDN5c_-iMr5RJxk)
.

Giles takes us on a journey through various possible solutions including COUNTIFS, SCAN, REDUCE, FILTER and LET.

I highly recommend that you work through the video alongside the Workings tab of the supporting Excel file and take your time to make sure that you understand each element.

My reflections on the challenge
-------------------------------

On the face of it, this seems like a simple challenge, with relatively straightforward logic.

It is pretty straight forward to solve using helper columns. The PowerQuery solution is also straightforward.

It becomes more difficult when you try to solve the challenge in one cell with one formula. This is because we are attempting to count the number of items in an array, which is not as simple as it first seems.

As you will see in Giles' live attempt, he looked at various approaches before settling on the solution using LET.

It is important to highlight that we are not saying this is the correct solution (or that focusing on single cell solutions is the right decision overall), it is just where Giles ended up in the live attempt.

The neatest solution that I found to this challenge was this formula from @babisflou87:

\=SUM(--((LEN(A2:A20)-LEN(SUBSTITUTE(A2:A20," ","")))=1))

I explain how this formula works in the babisflou87 Solution tab of the supporting Excel file.

What is the Excel BI Challenge series?
--------------------------------------

The Excel BI Challenges series has been created by [Vijay A. Verma](https://www.linkedin.com/in/excelbi/)
. It is an (ever-growing) set of Excel-based challenges. Each challenge is designed to test your mastery of Excel-based modelling.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-1)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-1)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-1)
    

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
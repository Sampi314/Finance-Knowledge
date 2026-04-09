# Excel BI Challenge

**Source:** https://www.fullstackmodeller.com/blog/excel-bi-challenge-5

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTBEFORE%20Function.png)

Excel BI Challenge 5
====================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Oct 21, 2024 1:54:20 PM

_Everything you need to master Excel BI Challenge 5  
_

![Excel BI challenge 5](https://www.fullstackmodeller.com/hs-fs/hubfs/C5%20image.jpg?width=2031&height=1248&name=C5%20image.jpg)

The challenge
-------------

This is the fifth challenge in the Excel BI challenge series. We are asked to provide a formula to know the name of the player(s) who have the highest Points on the basis of Round1+Round2+Round3.  

The answer should be "John, Shine".  

Here is the link to the base [Excel BI challenge file](https://onedrive.live.com/view.aspx?resid=E11B26EEAACB7947%217459&authkey=!AHi7g7vVdA4AkK0)
. You can view the Excel BI LinkedIn post for the challenge [HERE](https://www.linkedin.com/posts/excelbi_excel-advancedexcel-excelchallenge-activity-6968057882974064641-s4E0?utm_source=share&utm_medium=member_desktop)
.

Challenge walkthrough with Giles Male
-------------------------------------

Giles has recorded his attempt at this challenge live; no prep, no fluff, just opening the file and getting going. This means that you get to watch Giles' thought process and his journey, "warts and all".

You can watch Giles' walkthrough video on our [Excel on the Road Channel](https://www.youtube.com/watch?v=NY8i3g12DwA)
.

Let's work through this challenge together  

---------------------------------------------

In this article, I am going to work through the core elements of the challenge. I recommend reading this article and then working through the video with the help of our supporting Excel file.

Please download the [supporting Excel file](https://docs.google.com/uc?export=download&id=14iv0YgdTkSLs7j7-WTPufRFWT4x_NNS1)
. This file includes all of the formulas from Giles' walkthrough, complete with the full logic and workings with supporting guidance. It also covers alternative solutions including an Excel Tables-based version and a PowerQuery solution.

Before you get stuck into the video and supporting Excel file, let's step back and think about the logic behind this challenge.

The challenge:

We are asked to provide a formula to know the name of the player(s) who have the highest Points on the basis of Round1+Round2+Round3.  

To achieve this we will need to sum the values for the three rounds for each player, determine which sum values are the highest and who they belong to, and finally, join the players' names together.  

Step 1  

First, we need to sum the values for the three rounds for each player

\=BYROW(B2:D6, LAMBDA(x, SUM(x)))

Rather than using a simple SUM which returns a single result for a single row, we have used BYROW and LAMBDA to create a spilled result for all rows.

Step 2  

Next, we need to identify the player(s) with the highest score by ranking the result from step 1

\=RANK.EQ(J2#,J2#)

The RANK.EQ function returns the rank number for the row score within the range of scores.

Step 3

We now need to filter the list of player names to restrict it to those with the highest score (rank = 1 in step 2)

\=FILTER(A2:A6,L2#=1)

FILTER is a function that has been used regularly through these first five challenges.

Step 4  

The final step before bringing it all together is to join the names of the players with the highest combined scores together, separated by a comma

\=TEXTJOIN(", ",,N2#)

Step 5 - Finally, let's bring it all together

Giles wasn't able to bring everything together into a single-cell solution in his walk-through video. This was down to the fact that the RANK.EQ function needs a range not an array as its source.

I have created an alternative, single-cell solution using FILTER and MAX in the place of RANK.EQ. This is based on the logic in the solution from Byavya Gupta.

\=LET(  
     Players, A2:A6,  
     Scores, B2:D6,  
     SumScore, BYROW(Scores, LAMBDA(x, SUM(x))),  
     MaxScore, MAX(SumScore),  
     FilteredPlayers, FILTER(Players,SumScore = MaxScore),  
     Output, TEXTJOIN(" ,",,FilteredPlayers),  
     Output  
    )  

I highly recommend that you work through the video alongside the Workings tab of the [supporting Excel file](https://docs.google.com/uc?export=download&id=14iv0YgdTkSLs7j7-WTPufRFWT4x_NNS1)
. and take your time to make sure that you understand each element.

The PowerQuery Solution
-----------------------

For each of the challenges I am also providing an Excel Tables-based solution and a PowerQuery solution.

I am finding the challenge of solving these challenges with PowerQuery as rewarding as I am following the single cell-based solutions.

In this challenge it really struck me how similar the logic is between PowerQuery and the LET based solution that I ended up with. The steps being: aggregate; calculate the max value; filter the names by the max value & then combine the names.

My reflections on the challenge
-------------------------------

This was another really interesting challenge and I have come to love the structure that the LET function provides.

What really strikes me is just how much I am learning through working through these challenges and in-particular forcing myself to understand the single-cell solution.

Bring on challenge six!

What is the Excel BI Challenge series?
--------------------------------------

The Excel BI Challenges series has been created by [Vijay A. Verma](https://www.linkedin.com/in/excelbi/)
. It is an (ever-growing) set of Excel-based challenges. Each challenge is designed to test your mastery of Excel-based modelling.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-5)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-5)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-5)
    

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
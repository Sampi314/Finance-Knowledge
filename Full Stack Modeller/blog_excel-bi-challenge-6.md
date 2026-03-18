# Excel BI Challenge

**Source:** https://www.fullstackmodeller.com/blog/excel-bi-challenge-6

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTBEFORE%20Function.png)

Excel BI Challenge 6
====================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Dec 8, 2024 11:48:21 AM

_Everything you need to master Excel BI Challenge 6  
_

The challenge
-------------

![C6](https://www.fullstackmodeller.com/hs-fs/hubfs/C6.jpg?width=2043&height=1143&name=C6.jpg)

This is the sixth challenge in the Excel BI challenge series. We are asked to provide a formula to list numbers which appear more than once in Range A2:A20 and have both B and C in B2:B20.  

The answer should be "4,8".  

Here is the link to the base [Excel BI challenge file](https://onedrive.live.com/view.aspx?resid=E11B26EEAACB7947%217461&authkey=!APfs6bFjEsrJoZk)
. You can view the Excel BI LinkedIn post for the challenge [HERE](https://www.linkedin.com/posts/excelbi_excel-advancedexcel-excelchallenge-activity-6968788552088186880-a35K?utm_source=share&utm_medium=member_desktop)
.

Challenge walkthrough with Giles Male
-------------------------------------

Giles has recorded his attempt at this challenge live; no prep, no fluff, just opening the file and getting going. This means that you get to watch Giles' thought process and his journey, "warts and all".

You can watch Giles' walkthrough video on our [Excel on the Road Channel](https://www.youtube.com/watch?v=KJsNtgiBnxI)
.

Let's work through this challenge together  

---------------------------------------------

In this article, I am going to work through the core elements of the challenge. I recommend reading this article and then working through the video with the help of our supporting Excel file.

Please download the [supporting Excel file](https://docs.google.com/uc?export=download&id=1C5W8S8uY3EcvDReKcKXfTEuEg2rIZpdg)
. This file includes all of the formulas from Giles' walkthrough, complete with the full logic and workings with supporting guidance. It also covers alternative solutions including an Excel Tables-based version and a PowerQuery solution.

Before you get stuck into the video and supporting Excel file, let's step back and think about the logic behind this challenge.

The challenge:

We are asked to provide a formula to list numbers which appear more than once in the range A2:A20 and have both B and C in the range B2:B20.  

2,4 & 8 appear more than once. 2 has only C whereas 4 & 8 have both B & C. Hence the answer would be 4, 8.

Of the two logic tests laid out: "appear more than once"; and "have both B and C", only "have both B and C" actually needs to be tested for. If a number has both B and C, then by default, it must appear more than once.

The final logic flow is therefore as follows:

Aggregate the data column and combine the text together for each number then filter for numbers that contain both B and C.

Step 1  

First, we need to generate a unique list of the numbers in the Data column, sorted in ascending order

\=SORT(UNIQUE(A2:A20))

Here Giles used the UNIQUE function, with a SORT wrapped around it to sort the numbers in ascending order.

Step 2  

Next, we need to determine the letter(s) associated with each unique number from step 1, and concatenate them together.

\=CONCAT(FILTER($B$2:$B$20, $A$2:$A$20 = D2))

FILTER is a function that Giles has used regularly throughout the challenges.

Step 3

We now need to take a step back and create a formula that achieves the first two steps in a single cell that spills

\=MAP(D2#,LAMBDA(q,CONCAT(FILTER($B$2:$B$20,$A$2:$A$20=q))))

At this point Giles is leaning on LAMBDA with a MAP so that we have the whole formula in one cell that spills.

Step 4 and 5  

In the next two steps we need to identify whether the result of step 3 contains a "B" or "C".

These are initially calculated in two separate columns using the FIND function:

\=FIND("B",J2#)

\=FIND("C",J2#)

Step 6  

Next we bring the results of steps 4 and 5 together.

\=ISNUMBER(M2#) \* ISNUMBER(N2#)

Giles used ISNUMBER to convert the numbers in step 4 and step 5 into TRUE or FALSE so that we can then multiply the TRUE/FALSE results together.

Where the result is a 1 the number has both B and C in the range B2:B20.

Step 5 - Finally, let's bring it all together

Giles brought everything together into a single-cell solution in his walk-through video using the formula below:

\=LET(  
     Data, A2:A20,  
     Alpha, B2:B20,  
     UniqueData, SORT(UNIQUE(Data)),  
     DataCount,COUNTIFS(Data,UniqueData),  
     AlphaList, MAP(UniqueData,LAMBDA(q,CONCAT(FILTER(Alpha,Data=q)))),  
     FilteredData, TEXTJOIN(" ,",,FILTER(UniqueData, (DataCount > 1) \* (ISNUMBER(FIND("B",AlphaList))) \* (ISNUMBER(FIND("C",AlphaList))))),  
     FilteredData  
     )

My solution using GROUPBY

I used the new(ish) GROUPBY function to solve the challenge:

\=LET(  
     Data, A2:A20,  
     Alpha, B2:B20,  
     Aggregated, GROUPBY(Data,Alpha,CONCAT,0,0,1),  
     Column1, CHOOSECOLS(Aggregated, 1),  
     Column2, CHOOSECOLS(Aggregated, 2),  
     Filtered, FILTER(Column1,ISNUMBER(FIND("B", Column2)) \* ISNUMBER(FIND("C", Column2))),  
     Output, TEXTJOIN(" ,",,Filtered),  
     Output  
     )

I highly recommend that you work through the video alongside the Workings tab of the [supporting Excel file](https://docs.google.com/uc?export=download&id=1C5W8S8uY3EcvDReKcKXfTEuEg2rIZpdg)
. and take your time to make sure that you understand each element.

The PowerQuery Solution
-----------------------

For each of the challenges I am also providing an Excel Tables-based solution and a PowerQuery solution.

I am finding the challenge of solving these challenges with PowerQuery as rewarding as I am following the single cell-based solutions.

My reflections on the challenge
-------------------------------

This was another really interesting challenge and I have come to love the structure that the LET function provides.

What really strikes me is just how much I am learning through working through these challenges and in-particular forcing myself to understand the single-cell solution.

I was very pleased to be able to come up with my own solution using the GROUPBY function. As with previous challenges there were real similarities between my PowerQuery solution and the LET solution using GROUPBY.  

What is the Excel BI Challenge series?
--------------------------------------

The Excel BI Challenges series has been created by [Vijay A. Verma](https://www.linkedin.com/in/excelbi/)
. It is an (ever-growing) set of Excel-based challenges. Each challenge is designed to test your mastery of Excel-based modelling.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-6)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-6)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-6)
    

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
# Excel BI Challenge

**Source:** https://www.fullstackmodeller.com/blog/excel-bi-challenge-3

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTBEFORE%20Function.png)

Excel BI Challenge 3
====================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 24, 2024 10:16:16 PM

_Everything you need to master Excel BI Challenge 3  
_

The challenge
-------------

![Excel BI Challenge 3](https://www.fullstackmodeller.com/hs-fs/hubfs/image-png-4.png?width=1974&height=1338&name=image-png-4.png)

This is the third challenge in the Excel BI challenge series. We are asked to provide a formula to reverse a given number. Hence, if the number is 7834, then the answer would be 4387.  

The answer should be as provided in the Excel file.  

Here is the link to the base [Excel BI challenge file](https://onedrive.live.com/view.aspx?resid=E11B26EEAACB7947%217455&authkey=!AOzwss23wegX0rw)
. You can view the Excel BI LinkedIn post for the challenge [HERE](https://www.linkedin.com/posts/excelbi_excel-advancedexcel-excelchallenge-activity-6966996838612631552-Uver?utm_source=share&utm_medium=member_desktop)
.

Challenge walkthrough with Giles Male
-------------------------------------

Giles has recorded his attempt at this challenge live; no prep, no fluff, just opening the file and getting going. This means that you get to watch Giles' thought process and his journey, "warts and all".

You can watch Giles' walkthrough video on our [Excel on the Road Channel](https://www.youtube.com/watch?v=377OnqpJ0_U)
.

Let's work through this challenge together  

---------------------------------------------

In this article, I am going to work through the core elements of the challenge. I recommend reading this article and then working through the video with the help of our supporting Excel file.

Please download the [supporting Excel file](https://docs.google.com/uc?export=download&id=1sPJ5q58dmx15AWALc5j5VHszBzLcWcb3)
. This file includes all of the formulas from Giles' walkthrough, complete with the full logic and workings with supporting guidance. It also covers alternative solutions including an Excel Tables-based version and a PowerQuery solution.

Before you get stuck into the video and supporting Excel file, let's step back and think about the logic behind this challenge.

The challenge:

We are asked to provide a formula to reverse a given number.

The first thing I'm going to address here is that this is something that I have never needed to do in 25 years of modelling and probably never will need in the next 25 years.

But that's not really the point.

These challenges are designed to push us out of our Excel modelling comfort zone and try to use a variety of approached and functions to come up with a solution.

In order to reverse the order of the numbers we need to identify each number in the sequence and return them in an array rather than in a single cell.

We will then need to reverse the order that the numbers are placed in the sequence.

Finally, we will need to bring them back together from an array into a single cell. Ideally, this will all be delivered through a single formula that will SPILL for all of the rows in the data.

Ok, now that we have the logic in mind let's take a look at the two core elements of the logic flow.

I decided to pick the third row in the data for the walkthrough below as it is a better mix of numbers than row 2. The number we are trying to reverse is therefore 9032.

Step 1  

First, we need to determine how long the number string is as we need this for step 2.

\=LEN(A3)

This uses the LEN function which returns a value equal to the length of the number string. In this case, the result is 4 as the number string is 9032.

Step 2  

Next, we need to create a sequence of numbers from 1 to the number returned in step 1 (4).

\=SEQUENCE(D3, 1)

The result of this SEQUENCE function is a simple list of numbers from 1 to 4.

Step 3

We now need to replace the numbers in the array above with the numbers from the original number string: 9032.

\=MID(A3, F3#, 1)

The MID function is being used to cycle through the numbers in the number string, pulling the first item, then the second, then third etc etc based on the number coming from step 2

The first instance of the function returns 9, the second 0, the third 3 and the forth 2.

The combination of the three steps above converts the number string in one cell into an array of numbers.

Step 4 - Reversing the order

We need to reverse the order that the numbers are being pulled in Step 3.

\=SEQUENCE(D3, 1, D3, -1)

To do this we go back to step 2 and the SEQUENCE function using different elements of the function.

Let's take a closer look at this formula:

\=SEQUENCE(rows, \[columns\], \[start\], \[step\])

rows \- The length of the number string, in this case 4

columns \- Set to 1 as we need an array that is 1 column wide

start \- Start at the end of the number string, in this case in the 4th position (which is also the length of the number string)

step - We use -1 to step backwards

The combination of starting on the last character in the number string and taking 1 step backwards each time is how we reverse the order of the number string.

Step 5 - Finally, let's bring it all together

Bringing the elements from above together gives us the following formula:

\=CONCAT(MID(A2, SEQUENCE(LEN(A2), 1, LEN(A2), -1), 1))

In this case Giles' solution requires a formula for each row rather than being a true single-cell solution. Most people who attempted this solution also came up with a formula for each row.

I have shared a single cell solution from Anup Kumar in the [supporting Excel file](https://docs.google.com/uc?export=download&id=1sPJ5q58dmx15AWALc5j5VHszBzLcWcb3)
. This is what Anup's formula looks like:

\=MAP(A2:A6,  
LAMBDA(inputRange,  
LET(Nbr,inputRange,  
genSeq,SEQUENCE(LEN(Nbr),,1),  
NbrSplit,MID(Nbr,genSeq,1),  
0+CONCAT(SORTBY(NbrSplit,genSeq,-1))  
)  
)  
)

I highly recommend that you work through the video alongside the Workings tab of the supporting Excel file and take your time to make sure that you understand each element.

My reflections on the challenge
-------------------------------

I'll be honest, I was totally stumped by this challenge. I wouldn't have known where to start.  

And walking through the solution from Anup Kumar nearly melted my brain!

And that is what I love about these challenges. They are helping me learn new techniques and functions by forcing me to attempt things that I may not have ever faced in my normal modelling and training life.  

What is the Excel BI Challenge series?
--------------------------------------

The Excel BI Challenges series has been created by [Vijay A. Verma](https://www.linkedin.com/in/excelbi/)
. It is an (ever-growing) set of Excel-based challenges. Each challenge is designed to test your mastery of Excel-based modelling.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-3)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-3)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-3)
    

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
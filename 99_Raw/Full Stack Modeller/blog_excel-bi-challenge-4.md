# Excel BI Challenge

**Source:** https://www.fullstackmodeller.com/blog/excel-bi-challenge-4

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20TEXTBEFORE%20Function.png)

Excel BI Challenge 4
====================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Oct 7, 2024 2:08:08 PM

_Everything you need to master Excel BI Challenge 4  
_

The challenge
-------------

![](https://www.fullstackmodeller.com/hs-fs/hubfs/image-png-Sep-27-2024-08-18-06-6899-AM.png?width=2484&height=1695&name=image-png-Sep-27-2024-08-18-06-6899-AM.png)

This is the fourth challenge in the Excel BI challenge series. We are asked to extract the words which are all capitals (Uppercase).  

The answer should be as provided in the Excel file.  

Here is the link to the base [Excel BI challenge file](https://onedrive.live.com/view.aspx?resid=E11B26EEAACB7947%217458&authkey=!AMXp9C6FpYq4iBo)
. You can view the Excel BI LinkedIn post for the challenge [HERE](https://www.linkedin.com/posts/excelbi_excel-advancedexcel-excelchallenge-activity-6967713270291947520-RVuu?utm_source=share&utm_medium=member_desktop)
.

Challenge walkthrough with Giles Male
-------------------------------------

Giles has recorded his attempt at this challenge live; no prep, no fluff, just opening the file and getting going. This means that you get to watch Giles' thought process and his journey, "warts and all".

You can watch Giles' walkthrough video on our [Excel on the Road Channel](https://www.youtube.com/watch?v=heXFBMAPX0Y)
.

Let's work through this challenge together  

---------------------------------------------

In this article, I am going to work through the core elements of the challenge. I recommend reading this article and then working through the video with the help of our supporting Excel file.

Please download the [supporting Excel file](https://docs.google.com/uc?export=download&id=1vfnRcG1yvpBQqGZCFB3n_B8ubB7wNw_s)
. This file includes all of the formulas from Giles' walkthrough, complete with the full logic and workings with supporting guidance. It also covers alternative solutions including an Excel Tables-based version and a PowerQuery solution.

Before you get stuck into the video and supporting Excel file, let's step back and think about the logic behind this challenge.

The challenge:

We are asked to extract the words where every character is a capital (Uppercase).

To achieve this we will need to split the text into each separate word, then work out if every character in the word is a capital and, finally filter to only return words that are all in uppercase characters.

Step 1  

First, we need to split the text to separate out each word.

\=TEXTSPLIT(A2," ")

This uses the TEXTSPLIT function with a single space (" ") as a delimiter. TEXTSPLIT is a dynamic array function and therefore spills the results over the appropriate number of columns.

Step 2  

Next, we need to repeat the first step but, at the same time, convert the text to all uppercase.

\=UPPER(TEXTSPLIT(A2," "))

The UPPER function is used to convert text into all uppercase.

Step 3

We now need to compare the original text (step 1) to the uppercase version (step 2)

\=EXACT(D2,G2)

EXACT is a logical formula. It returns TRUE if the items match exactly and FALSE if not. EXACT is case-sensitive so can be used here to compare the results of step 1 and step 2.

Step 4  

The final step before bringing it all together is to filter out any words that include lowercase characters.

\=FILTER(G2#, J2:K2 = TRUE)

To do this we use the FILTER function to return only rows where the result of step 3 is equal to TRUE. That is to say that the original text and uppercase version of the text are exactly the same. ie the original text was already all uppercase.

Step 5 - Finally, let's bring it all together

Bringing the elements from above together within a LET function gives us the following formula:

\=LET(  
    Words, TEXTSPLIT(A2, " "),  
    UpperWords, UPPER(Words),  
    ExactMatch, EXACT(Words, UpperWords),  
    SplitOutput, FILTER(Words, ExactMatch = TRUE, ""),  
    Output, TEXTJOIN(" ", TRUE, SplitOutput),  
    Output  
    )

In this case, Giles' solution requires a formula for each row rather than being a true single-cell solution. Most people who attempted this solution also came up with a formula for each row.

I have shared a single-cell solution from Amardeep Singh in the [supporting Excel file](https://docs.google.com/uc?export=download&id=1vfnRcG1yvpBQqGZCFB3n_B8ubB7wNw_s)
. This is what Anup's formula looks like:

\=MAP(A2:A10,LAMBDA(x,  
    LET(  
       d,TEXTSPLIT(x," "),  
       r,IF(EXACT(d,UPPER(d)),d,""),  
       TEXTJOIN(" ",TRUE,r)  
       )  
       )  
       )

I then took this approach and applied it to Giles' row-based solution to provide a single cell version:

\=MAP(A2:A10, LAMBDA(x,  
    LET(  
    Words, TEXTSPLIT(x, " "),  
    UpperWords, UPPER(Words),  
    ExactMatch, EXACT(Words, UpperWords),  
    SplitOutput, FILTER(Words, ExactMatch = TRUE, ""),  
    Output, TEXTJOIN(" ", TRUE, SplitOutput),  
    Output  
    )

I highly recommend that you work through the video alongside the Workings tab of the supporting Excel file and take your time to make sure that you understand each element.

My reflections on the challenge
-------------------------------

I'll be honest, I was once again stumped by this challenge, mainly because I had never come across the EXACT function before.  

I am finding it incredibly useful to work through Giles' videos and build these articles and the accompanying workbook. Challenging myself to work in a way that is outside my normal, comfortable modelling style is a lot of fun. I am learning a lot.

I hope you are too.

What is the Excel BI Challenge series?
--------------------------------------

The Excel BI Challenges series has been created by [Vijay A. Verma](https://www.linkedin.com/in/excelbi/)
. It is an (ever-growing) set of Excel-based challenges. Each challenge is designed to test your mastery of Excel-based modelling.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-4)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-4)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fexcel-bi-challenge-4)
    

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
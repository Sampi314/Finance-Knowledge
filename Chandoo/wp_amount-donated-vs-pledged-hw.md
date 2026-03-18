# Amount Donated vs. Pledged [Excel Formula Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/amount-donated-vs-pledged-hw

---

Amount Donated vs. Pledged \[Excel Formula Homework\]
=====================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 26 comments

  

We have some home work folks! Today, lets test your Excel formula skills by giving some data related to a fund.

The problem:
------------

You manage a fund for a non-profit. You have donors who pledge certain amount at the start of the year. As you go thru the year, the donors donate money to your fund. At the end of the year, you have a table like this:

![Amount Donated vs. Pledged - Data](https://chandoo.org/img/hw/amount-donated-vs-pledged-data.png)

And you need to summarize the fund’s performance by calculating all these statistics.

![Amount Donated vs. Pledged - Summary Calculation Homework](https://chandoo.org/img/hw/donated-vs-pledged-homework.png)

Download the homework file:
---------------------------

**[Click here to download the homework file](https://img.chandoo.org/hw/formula-homework-donations-calculations.xls)
**. Write formulas in all blue boxes so that the values are calculated properly.

### The correct answers are shown below:

![Solution for Amount Donated vs. Pledged Excel Homework](https://chandoo.org/img/hw/donated-vs-pledged-homework-solution.png)

Post your Answers using Comments
--------------------------------

Once you finish calculating the summary values, please share your approach (and formulas) using comments. _**Go!**_

### Download the solution file:

There are several ways you can calculate the summary values. Here is my approach. [Click here to download the solution file](https://img.chandoo.org/hw/formula-homework-donations-calculations-sol.xlsx)
 \[[Excel 2003 version here](https://img.chandoo.org/hw/formula-homework-donations-calculations-sol.xls)\
\].

### More homework:

If you like to test your Excel skills then, checkout some of these homework problems:

1.  [Calculate sum of digits in a number using Array formulas](http://chandoo.org/wp/2011/03/18/calculating-sum-of-digits-in-a-number/)
    
2.  [Find average of closest 2 numbers](http://chandoo.org/wp/2011/01/19/average-of-closest-2-numbers/)
    
3.  [When does Thanksgiving day occur on same day again?](http://chandoo.org/wp/2010/11/26/when-does-thanksgiving-day-occur-on-same-date-again/)
    
4.  [Show zebra lines when value changes](http://chandoo.org/wp/2010/09/28/add-zebra-lines-when-value-changes/)
    
5.  _**… [More homework & Excel challenges](http://chandoo.org/wp/tag/homework/)
    **_

### Thanks David

Special thanks to _**David**_, who emailed me this problem a few weeks ago.

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Chandoo  <br>Tags: [array formulas](https://chandoo.org/wp/tag/array-formulas/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [sum()](https://chandoo.org/wp/tag/sum/)<br>, [sumproduct](https://chandoo.org/wp/tag/sumproduct/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 26 Responses to “Amount Donated vs. Pledged \[Excel Formula Homework\]”

1.  ![](https://secure.gravatar.com/avatar/3fe89f02ca57f9bfdd177d3eeef1e0cf93d5cd82e207932dee0670d039039bc7?s=64&d=mm&r=g) Bill says:
    
    [June 10, 2011 at 12:23 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204934)
    
    Great practice!
    
    First off, I made named ranges - Pledged (C7:C1206) and Given (D7:D1206).
    
    Then it was all about matching the constraints to 0 or 1 and multiplyng them as needed to get the proper sums.
    
    G7: {=SUM(IF(Pledged>0,1,0) \* IF(Given>Pledged,1,0))}  
    H7: {=SUM(IF(Pledged>0,1,0) \* IF(Given>Pledged,1,0) \*Pledged)}  
    I7: {=SUM(IF(Pledged>0,1,0) \* IF(Given>Pledged,1,0) \*Given)}
    
    most of the rest of the array formulas are simply changing the constraints (such as pledged=0 instead of pledged>0), but these other 2 are interesting as well since they need an extra term:
    
    G10: {=SUM(IF(Pledged>0,1,0) \* IF(Given0,1,0))}  
    H10: {=SUM(IF(Pledged>0,1,0) \* IF(Given0,1,0) \*Pledged)}
    
    I10 doesn't need the extra term because (IF(Given>0,1,0)) and Given are redundant.
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204934)
    
2.  ![](https://secure.gravatar.com/avatar/9e82e18c867f54c5812531149ebd674d22966e24b8401ccbda7a0652a4ad9e41?s=64&d=mm&r=g) Hurls says:
    
    [June 10, 2011 at 1:17 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204940)
    
    Nice challenge to start the morning! I'm so glad I found this site a few weeks back because it's great!
    
    I also named my ranges just as Bill did. However, I used a different approach than he and the solution did.
    
    Speaking of the solution - is it correct? Where you got 389, I got 294. Also, when you have 389, the two subtotals equal 1295, so that tells me something is wrong. Here's what I did:
    
    G7: =SUMPRODUCT((Pledged0))  
    H7: =SUMPRODUCT((Pledged0)\*(Pledged))  
    I7: =SUMPRODUCT((Pledged0)\*(Given))
    
    G8: =SUMPRODUCT((Pledged=Given)\*(Pledged>0))  
    G10: =SUMPRODUCT((Pledged>Given)\*(Pledged>0)\*(Given>0)\*1) // solution didn't have (given > 0) constraint  
    G11: =SUMPRODUCT((Pledged>Given)\*(Pledged>0)\*(Given=0)\*1)  
    G15: =SUMPRODUCT((Pledged=0)\*(Given>0)\*1)  
    G16: =SUMPRODUCT((Pledged=0)\*(Given=0)\*1)  
    So for the previous 5 rows, the equations in H and I were just multiplied by Pledged and Given, respectively, just like H7 and I7 were.
    
    I also used SUBTOTAL(9,...) for rows 12 and 17 and then SUBTOTAL(9,x7:x17) in row 19.
    
    Is my accusation correct?
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204940)
    
3.  ![](https://secure.gravatar.com/avatar/9e82e18c867f54c5812531149ebd674d22966e24b8401ccbda7a0652a4ad9e41?s=64&d=mm&r=g) Hurls says:
    
    [June 10, 2011 at 1:21 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204941)
    
    Ha! When I posted my solution, it interpreted some things as erroneous HTML tags. My attempt to correct that is replacing > with GT:  
    .  
    G7: =SUMPRODUCT((Pledged<Given)\*(Pledged GT 0))  
    H7: =SUMPRODUCT((Pledged<Given)\*(Pledged GT 0)\*(Pledged))  
    I7: =SUMPRODUCT((Pledged<Given)\*(Pledged GT 0)\*(Given))
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204941)
    
4.  ![](https://secure.gravatar.com/avatar/758cbbca7d5934cbb7e19edc5bc5d7cdd41f5bfd7bd8d7a5a1d41ccd2ba887c8?s=64&d=mm&r=g) Michael says:
    
    [June 10, 2011 at 1:55 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204943)
    
    I'm using SUMPRODUCT for this one:
    
    2 named range:  
    Amount\_Given =Sheet1!$D$7:$D$1206  
    Amount\_Pledged =Sheet1!$C$7:$C$1206
    
    For the first row, exceeded:
    
    COUNT  
    \=SUMPRODUCT(--(Amount\_Pledged>0),--(Amount\_Given>Amount\_Pledged))  
    PLEDGED =SUMPRODUCT(--(Amount\_Pledged>0),--(Amount\_Given>Amount\_Pledged),Amount\_Pledged)  
    GIVEN =SUMPRODUCT(--(Amount\_Pledged>0),--(Amount\_Given>Amount\_Pledged),Amount\_Given)
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204943)
    
5.  ![](https://secure.gravatar.com/avatar/44f55881d7f3d7a48700e9338c97ebee32fe7ebc6f2aaa34a4e72b7f334e02f7?s=64&d=mm&r=g) Doug says:
    
    [June 10, 2011 at 4:39 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204958)
    
    Where did the 18 names come from for those that did not pledge and did not give?
    
    By my estimate \[ Did not Pledge, Did not Give \] should be somewhere around 6.92 billion people.
    
    Good problem, I would have started with the sum(if()) approach and added columns for flags but didn't have the time to spare for more than a quick review after I saw the No Pledge No donation row.
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204958)
    
6.  ![](https://secure.gravatar.com/avatar/278ed91a3a617c2c6bf856541e1e874df8469ee8784cdb350c4d8eeaa461cbdb?s=64&d=mm&r=g) Fred says:
    
    [June 10, 2011 at 5:08 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204961)
    
    I have not started yet. but...
    
    pledged = 1168, did not pledge = 127 but total count is 1200? they don't add up?
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204961)
    
7.  ![](https://secure.gravatar.com/avatar/0efe9c04569caf74237e33a086d179983539da35e86dbeaa8163e8044f6ece2d?s=64&d=mm&r=g) Angi says:
    
    [June 10, 2011 at 5:17 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204963)
    
    First, I added a column next to given called Difference. I then named ranges as pledged, given and dif.
    
    Then I used COUNTIFS() and SUMIFS() formulas to summarize the data:  
    Row 7: =COUNTIFS(pledged,">0",dif,">0") =SUMIFS(pledged,pledged,">0",dif,">0") =SUMIFS(given,pledged,">0",dif,">0") =J7-I7  
    Row 8: =COUNTIFS(pledged,">0",dif,0) =SUMIFS(pledged,pledged,">0",dif,0) =SUMIFS(given,pledged,">0",dif,0) =J8-I8  
    Row 10: =COUNTIFS(pledged,">0",given,">0",dif,"0",given,">0",dif,"0",given,">0",dif,"0",given,0) =SUMIFS(pledged,pledged,">0",given,0) =SUMIFS(given,pledged,">0",given,0) =J11-I11  
    Row 12: (could have used sum instead, but I continued my formulas down to check my work.) =COUNTIF(pledged,">0") =SUMIFS(pledged,pledged,">0") =SUMIFS(given,pledged,">0") =J12-I12  
    Row 15 =COUNTIFS(pledged,0,dif,">0") =SUMIFS(pledged,pledged,0) =SUMIFS(given,pledged,0) =J15-I15  
    Row 16 =COUNTIFS(pledged,0,dif,0) =SUMIFS(pledged,pledged,0) 0 =J16-I16  
    Row 17 =SUM(H15:H16) =SUM(I15:I16) =SUM(J15:J16) =SUM(K15:K16)  
    Row 19 =SUM(H12,H17) =SUM(I12,I17) =SUM(J12,J17) =SUM(K12,K17)
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204963)
    
8.  ![](https://secure.gravatar.com/avatar/0efe9c04569caf74237e33a086d179983539da35e86dbeaa8163e8044f6ece2d?s=64&d=mm&r=g) Angi says:
    
    [June 10, 2011 at 5:22 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204964)
    
    Good eye Fred - you are right! Chandoo has a mistake in one of the count cell formulas.
    
    Those that did pledge and gave less than the pledge= 294 not 389. Subtotal for all those that pledged and underpaid is 1,073, which makes the total count = 1,200.
    
    Count column results:  
    Pledged Count  
    Exceeded 628  
    Met 56  
    Underpaid:  
    Did give 294  
    Did not give 95  
    Subtotal 1,073
    
    Did not Pledge  
    Gave 109  
    Did not give 18  
    Row 17 127
    
    Row 19 1,200
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204964)
    
9.  ![](https://secure.gravatar.com/avatar/a6a4b3d5c3fa8b186f392a059a16f0fb192a26fd4c4fe55e9f05644832f9f330?s=64&d=mm&r=g) diva says:
    
    [June 10, 2011 at 5:24 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204966)
    
    using single cell sumproduct formulas for correct conditions
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204966)
    
10.  ![](https://secure.gravatar.com/avatar/0efe9c04569caf74237e33a086d179983539da35e86dbeaa8163e8044f6ece2d?s=64&d=mm&r=g) Angi says:
    
    [June 10, 2011 at 5:25 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204967)
    
    Sorry, should have included this in my previous post. Chandoo's formula in his cell G10 can be corrected as:  
    \=SUM((lstPledged>lstGiven)\*(lstPledged>0)\*(lstGiven>0))  
    (He left off the last condition in the solution spreadsheet.)
    
    Thanks, Chandoo! This was fun work 🙂
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204967)
    
11.  ![](https://secure.gravatar.com/avatar/a6a4b3d5c3fa8b186f392a059a16f0fb192a26fd4c4fe55e9f05644832f9f330?s=64&d=mm&r=g) diva says:
    
    [June 10, 2011 at 5:29 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204969)
    
    okay,  
    for the explanations, since i cant upload the file  
    formula in  
    G7 =SUMPRODUCT(--($C$7:$C$1206>0),--($D$7:$D$1206>$C$7:$C$1206))  
    H7 =SUMPRODUCT(--($C$7:$C$1206>0),--($D$7:$D$1206>$C$7:$C$1206),C7:C1206)  
    I7 = =SUMPRODUCT(--($C$7:$C$1206>0),--($D$7:$D$1206>$C$7:$C$1206),D7:D1206)
    
    H10 =SUMPRODUCT(--($C$7:$C$1206>0),--($D$7:$D$12060),C$7:C$1206)
    
    other cells can be manipulated by proper conditions such as pledged > given, = given or < given etc
    
    can be made a bit more elegant by naming the ranges and making it trimmer
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204969)
    
12.  ![](https://secure.gravatar.com/avatar/278ed91a3a617c2c6bf856541e1e874df8469ee8784cdb350c4d8eeaa461cbdb?s=64&d=mm&r=g) Fred says:
    
    [June 10, 2011 at 5:46 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204971)
    
    My H10 is
    
    \={SUMPRODUCT(IF(PLEDGED>0,1,0),IF(GAVE0,1,0))}
    
    and I got 294
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204971)
    
13.  ![](https://secure.gravatar.com/avatar/2c377566914a9b79afc5f060e0336ca8210d64e539139fc828bbc45918a783c6?s=64&d=mm&r=g) SteveT says:
    
    [June 10, 2011 at 6:09 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204976)
    
    Were the 95 people in "Did not give" double counted? Total = 1295 as Fred said
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204976)
    
14.  ![](https://secure.gravatar.com/avatar/b9c0e2b1d3b3c4d5abf2cdba4955ed15b6b0f1ce901a202ac6a894ffe8c10aed?s=64&d=mm&r=g) Laksiri says:
    
    [June 10, 2011 at 6:10 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204977)
    
    First, "underpaid—did give" count is a miscalculation. it's simply double counted the 95 just below it (underpaid—did not give). Of course sub totals are not adding up to 1,200.
    
    I've done this with array formulas. Here is the link if any one interested.
    
    [http://cid-00557615ec1937ba.photos.live.com/self.aspx/Excel%20Public/ArrayFormula.JPG](http://cid-00557615ec1937ba.photos.live.com/self.aspx/Excel%20Public/ArrayFormula.JPG)
    
    Remember to press Ctrl+Shift+Enter. Happy Excel every one...!
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204977)
    
15.  ![](https://secure.gravatar.com/avatar/278ed91a3a617c2c6bf856541e1e874df8469ee8784cdb350c4d8eeaa461cbdb?s=64&d=mm&r=g) Fred says:
    
    [June 10, 2011 at 8:15 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204997)
    
    formula didn't post right...
    
    H10 should be
    
    { sumproduct ( if ( pledged > 0 , 1, 0 ), if (gave 0, 1 ,0 ) ) }
    
    and you get 294, then the toal would be correct at 1200
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204997)
    
16.  ![](https://secure.gravatar.com/avatar/278ed91a3a617c2c6bf856541e1e874df8469ee8784cdb350c4d8eeaa461cbdb?s=64&d=mm&r=g) Fred says:
    
    [June 10, 2011 at 8:18 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204998)
    
    god darn it didn't post right...
    
    { sumproduct ( if ( pledged GT 0, 1, 0), if (Gave LT pledged, 1, 0) times if (gave GT zero, one, zero ) ) }
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-204998)
    
17.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [June 11, 2011 at 12:40 am](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205009)
    
    @Fred... Thanks for pointing out the mistake. I fixed it and updated the solution files too. 🙂
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205009)
    
18.  ![](https://secure.gravatar.com/avatar/278ed91a3a617c2c6bf856541e1e874df8469ee8784cdb350c4d8eeaa461cbdb?s=64&d=mm&r=g) fred says:
    
    [June 11, 2011 at 5:10 am](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205019)
    
    Thanks for the donut! 😉
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205019)
    
19.  ![](https://secure.gravatar.com/avatar/892a728e01c28466e5c67cd51f882f5031799ef20b8874be859f595a8cd5735c?s=64&d=mm&r=g) Tom says:
    
    [June 11, 2011 at 9:53 am](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205038)
    
    Great task for a Saturday morning - enjoyed doing this a lot.  
    I started doing this with array formulae, but it got too tricky to debug, so I moved to using sumproduct for the sum columns. In the count columns I used an array formula with the right conditions.  
    I named the ranges as did most other people, Given and Pledged, then the formulae for the pledged totals (for example) become:  
    Pledged and Exceeded pledge: =SUMPRODUCT(Pledged, --((Pledged-Given)0))  
    Pledged and met pledge: =SUMPRODUCT(Pledged, --((Pledged-Given)=0), --(Pledged>0))  
    Pledged, underpaid but did give: =SUMPRODUCT(Pledged, --((Pledged-Given)>0), --(Pledged>0), --(Given>0))  
    I'd upload the file somewhere, but I don't have a website.
    
    Thanks for posting the challenge!
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205038)
    
20.  ![](https://secure.gravatar.com/avatar/4cdf8c8300564d8c2e85bc91d8d7912cf28f9e2946ab40558aa185f49e577404?s=64&d=mm&r=g) [Fowmy](http://coachexcel.webs.com/)
     says:
    
    [June 11, 2011 at 6:57 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205070)
    
    Interesting analysis.
    
    Please find my finished file:
    
    [http://cid-18c2ae6c7e70126a.office.live.com/self.aspx/.Documents/formula-homework-donations-calculations.xls](http://cid-18c2ae6c7e70126a.office.live.com/self.aspx/.Documents/formula-homework-donations-calculations.xls)
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205070)
    
21.  [Comparing Lists of Values in Excel using Array Formulas | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2011/06/14/compare-lists-array-formula/)
     says:
    
    [June 14, 2011 at 8:56 am](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205261)
    
    \[...\] week, we had a home work on Calculating Donation Summaries using Excel Formulas. This is a good case where array formulas can help us. So today, we will learn how we can use Array \[...\]
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205261)
    
22.  ![](https://secure.gravatar.com/avatar/fc01aafe7f74e0103e87c50efebde6424ae5e40c92661a1a3ca08a79990b3f53?s=64&d=mm&r=g) charles jackson says:
    
    [June 14, 2011 at 9:01 am](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205264)
    
    below is everything under the heading count  
    G7=SUM(($D$7:$D$1206>$C$7:$C$1206)\*($C$7:$C$1206>0))  
    G8=SUM(($D$7:$D$1206=$C$7:$C$1206)\*($C$7:$C$1206>0))
    
    G10=SUM(($C$7:$C$1206>$D$7:$D$1206)\*($D$7:$D$1206>0))  
    G11=COUNTIFS($D$7:$D$1206,0,$C$7:$C$1206,">0")  
    G12=SUM(G10:G11,G7:G8)
    
    G15=SUM(($C$7:$C$1206=0)\*(D$7:$D$1206>0))  
    G16=SUM(($C$7:$C$1206=0)\*($D$7:$D$1206=0))  
    G17=SUM(G15:G16)
    
    G19=SUM(G7:G8,G10:G11,G15:G16)
    
    Everything under pledged  
    H7=SUM(IF($D$7:$D$1206>$C$7:$C$1206,1,0)\*C7:C1206)  
    H8=SUM(($D$7:$D$1206=$C$7:$C$1206)\*($C$7:$C$1206>0)\*(C7:C1206))
    
    H10=SUM(($C$7:$C$1206>$D$7:$D$1206)\*($D$7:$D$1206>0)\*$C$7:$C$1206)  
    H11=SUMIFS($C$7:$C$1206,$D$7:$D$1206,0,$C$7:$C$1206,">0")  
    H12=SUM(H10:H11,H7:H8)
    
    H15=SUM(($C$7:$C$1206=0)\*($D$7:E$1206>0)\*C7:C1206)  
    H16=SUM(($C$7:$C$1206=0)\*($D$7:$D$1206=0)\*C7:C1206)  
    H17=SUM(H15:H16)
    
    H19=SUM(H7:H8,H10:H11,H15:H16)
    
    everything under Given  
    I7=SUM(($D$7:$D$1206>$C$7:$C$1206)\*(D7:D1206)\*(C7:C1206>0))  
    I8=SUM(($D$7:$D$1206=$C$7:$C$1206)\*($C$7:$C$1206>0)\*(D7:D1206))
    
    I10=SUM(($C$7:$C$1206>$D$7:$D$1206)\*($D$7:$D$1206>0)\*$D$7:$D$1206)  
    I11=SUMIFS($D$7:$D$1206,$D$7:$D$1206,0,$C$7:$C$1206,">0")  
    I12=SUM(I10:I11,I7:I8)
    
    I15=SUM(($C$7:$C$1206=0)\*($D$7:D$1206>0)\*($D$7:$D$1206))  
    I16=SUM(($C$7:$C$1206=0)\*($D$7:$D$1206=0)\*D7:D1206)  
    I17=SUM(I15:I16)
    
    I19=SUM(I7:I8,I10:I11,I15:I16)
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-205264)
    
23.  ![](https://secure.gravatar.com/avatar/7469b09b3ddcf213a9456f27ff4207d6a5fb181200cdc89ed7eaab0d21c9aec7?s=64&d=mm&r=g) cnestg8r says:
    
    [November 28, 2018 at 2:45 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-1596092)
    
    This is for pledged but did not give. The same structure is used in each cell. This makes it easy to read.
    
    \=SUM(--  
    (GIFT\[Amount Given\]0)\*  
    (GIFT\[Amount Given\]=0)\*  
    (GIFT\[Amount Pledged\]))
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-1596092)
    
24.  ![](https://secure.gravatar.com/avatar/7469b09b3ddcf213a9456f27ff4207d6a5fb181200cdc89ed7eaab0d21c9aec7?s=64&d=mm&r=g) cnestg8r says:
    
    [November 28, 2018 at 2:47 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-1596093)
    
    \=SUM(--  
    (GIFT\[Amount Given\]0)\*  
    (GIFT\[Amount Given\]=0)\*  
    (GIFT\[Amount Pledged\]))
    
    didn't post properly...
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-1596093)
    
25.  ![](https://secure.gravatar.com/avatar/7469b09b3ddcf213a9456f27ff4207d6a5fb181200cdc89ed7eaab0d21c9aec7?s=64&d=mm&r=g) cnestg8r says:
    
    [November 28, 2018 at 2:49 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-1596094)
    
    one more try:
    
    "{=SUM(--  
    (GIFT\[Amount Given\]0)\*  
    (GIFT\[Amount Given\]=0)\*  
    (GIFT\[Amount Pledged\]))}"
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-1596094)
    
26.  ![](https://secure.gravatar.com/avatar/7469b09b3ddcf213a9456f27ff4207d6a5fb181200cdc89ed7eaab0d21c9aec7?s=64&d=mm&r=g) cnestg8r says:
    
    [November 28, 2018 at 2:51 pm](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-1596095)
    
    {=SUM(--(GIFT\[Amount Given\]0)\*(GIFT\[Amount Given\]=0)\*(GIFT\[Amount Pledged\]))}
    
    [Reply](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#comment-1596095)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/amount-donated-vs-pledged-hw/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [How to create a Win-Loss Chart in Excel? \[Tutorial & Template\]](https://chandoo.org/wp/win-loss-chart/) | [Comparing Lists of Values in Excel using Array Formulas](https://chandoo.org/wp/compare-lists-array-formula/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
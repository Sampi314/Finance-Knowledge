# Formula forensics 17 - A Solution to Maljzm’s problem.

**Source:** https://chandoo.org/wp/formula-forensics-no-017

---

Formula Forensics No. 017 – A Solution to Maljzm’s problem.
===========================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Posts by Faseeh](https://chandoo.org/wp/category/posts-by-faseeh/)
 - 10 comments

  

Last week at the [Chandoo.org Forums](http://chandoo.org/forums/topic/formula-on-calculating-service-level-performance "Maljzm's Question")
 Malzjm, asked a question:

“_I need your help on calculating the service level if it passed or fail based on a requirement._

_So far, I have only managed to create this:_

_`=IF(O:O="","", IF(AND(D:D="SL 3",O:O<=TIME(12,0,0)),"Pass","Fail"))   `This works for one argument but if I do nested if, it does not._”

Faseeh, who joined the Forums in January this year, and has been a recent regular responder at the Forums responded with a nice:

`=IF((D2)<=(TIMEVALUE(INDEX($C$17:$C$20,MATCH(B2,$B$17:$B$20,0),0))),"PASS","FAIL")`

Malzjm, thanked Faseeh for the response and then asked could he explain how the above formula worked.

Being Shy, Not, I chipped in and asked Faseeh would he mind explaining the solution here as a Formula Forensic.

So today we are proud to present Faseeh’s first post at Chandoo.org, a Solution to Maljzm’s problem.

**Faseeh’s Formula:**
---------------------

As always at Formula Forensics you can follow along using real data from the example file: [Dowload Here](https://chandoo.org/wp/wp-content/uploads/2012/05/Faseeh01.xls "Example File")

### Define the problem:

_The formula should take a value from the Severity Column \[Column B\] and match the Time Resolved \[Column D\] against the same status value from a standard table. if the actual time is less than standard time then it should display “Pass” otherwise it should show “Fail”._

_The formula will take B2’s value (SL1), match it in second table, return the corresponding value from RESOLVED Time (02:00), then compare this value to the value in D2 (1:15) and will return Pass or Fail (Pass in this case)_

[![](https://chandoo.org/wp/wp-content/uploads/2012/05/FA_Master.png "FA_Master")](https://chandoo.org/wp/wp-content/uploads/2012/05/FA_Master.png)

Formula in **E2**:

\=IF((D2)<=(TIMEVALUE(INDEX($C$17:$C$20,MATCH(B2,$B$17:$B$20,0),0))),"Pass","Fail")

Lets break this formula down and work through it

  

### **Step No. 01**

\=IF((D2)<=(TIMEVALUE(INDEX($C$17:$C$20,MATCH(B2,$B$17:$B$20,0),0))),"Pass","Fail")

The Excel Match() function is used to match a value and give its position in an array.

The Match function takes following arguments,

_MATCH__(lookup\_value,lookup\_array,match\_type)_

For this situation it takes the following this form:

_MATCH(B2,$B$17:$B$20,0)_

Where:

Lookup\_Value = B2

Lookup\_array = _$B$17:$B$20_

_Match type: = 0 =_  ‘Exact match’

The result will be like this:

_MATCH(“SL3”,{”SL1”,”SL2”,”SL3”}, 0)_ 

_Excel will return the value **3**_

_This will be an input for the second function._

### Step No. 02

Our formula was…

_\=IF((D2)<=(TIMEVALUE(INDEX($C$17:$C$20,MATCH(B2,$B$17:$B$20,0),0))),"Pass","Fail")_

That take the following shape after evaluation of MATCH() function

\=IF((D2)<=(TIMEVALUE(INDEX($C$17:$C$20,3,0))),"Pass","Fail")

_So the next Function to be evaluated is INDEX ()._

_The Excel Index () function a few inputs_

_Index_(Array, Row\_num, Column\_num)

Note that we are using “Array Form” here \[The Index() function could be used in “Reference Form” as well\]

For our situation the formula takes this shape:

_INDEX($C$17:$C$20 ,3 ,0)_

_So the_

_**Array**: = $C$17:$C$20 is the range containing Resolves Time ,_

_**Row\_Num**: = 3 the value we get from MATCH()_

_**Column\_Num**: = 0  stands for we want to look in the Zeroth Column, i.e. the **Resolved Time** Column in itself so this will give us:_

_\=_INDEX ($C$17:$C$20, 3, 0)

\=INDEX ({“02:00″,”04:00″,”08:00″,”12:00”} ,3 ,0)

i.e. the Third element of the Zeroth column i.e. “_08:00″._

This will be the feed to the next formula.

### Step No. 03

After evaluating the INDEX () function our formula takes following shape:

_\=IF((D2)<=(TIMEVALUE(“08:00”)),”Pass”, “Fail”)_

_The Excel **Timevalue()** function returns the decimal number of the time represented by a text string._

_The decimal number is a value ranging from 0 (zero) to 0.99999999, representing the times from 0:00:00 (12:00:00 AM) to 23:59:59 (11:59:59 P.M.).  
_

_Thus for the values mentioned in “resolved time” the Timevalue() would give 0.083, 0.167, 0.333, 0.500 respectively._

_**Hint**: How will you get these values manually??… Timevalue = No. of Hours x 60 / Total Min in a Day_

so _08:00 Hrs x 60 / 1440 = 0.333_

_Similarly the others values in the Resolved Time can also be calculated_

_Note that this functions takes time as ‘text’. Hence by the end of this step the formula stood at:_

_\=IF((D2)<=0.333,”Pass”, “Fail”)_

### Step No. 04

The final step is an IF() statement that compares value of D2.

Since value in D2 (“1:15” = decimal 0.05208) is less than 0.333, the IF () statement will return “**Pass**” as the final result.

_\=IF((0.05208)<=0.333,”**Pass**”, “Fail”)_ 

You can check the values below this in E2 in the example file

**Download**
------------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/05/Faseeh01.xls "Example File")
.

**Formula Forensics “The Series”**
----------------------------------

**Congratulations Faseeh on your first published post at Chandoo.org**.

I hope Faseeh is able to continue with similar posts in the future!

You can learn more about how to pull Excel Formulas apart like Faseeh has just shown us in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics - The Series")

**We Need Your Help**
---------------------

I still need more ideas for future Formula Forensics posts and so I need your help!

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post just like Faseeh has done above or;

If you have a formula that you would like explained but don’t want to write a post also send it to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
 or [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
.

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
| Written by Hui...  <br>Tags: [if()](https://chandoo.org/wp/tag/if/)<br>, [INDEX()](https://chandoo.org/wp/tag/index/)<br>, [MATCH()](https://chandoo.org/wp/tag/match/)<br>, [Timevalue()](https://chandoo.org/wp/tag/timevalue/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 10 Responses to “Formula Forensics No. 017 – A Solution to Maljzm’s problem.”

1.  ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
    
    [April 5, 2012 at 12:12 pm](https://chandoo.org/wp/formula-forensics-no-017/#comment-222027)
    
    Excellent write-up Faseeh!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222027)
    
2.  ![](https://secure.gravatar.com/avatar/6722ef7faf9f58e3983354670465fbbe003d3ede4dc781da7cd862a7dde4d2ab?s=64&d=mm&r=g) Ksandra2901 says:
    
    [April 5, 2012 at 1:35 pm](https://chandoo.org/wp/formula-forensics-no-017/#comment-222030)
    
    That has got to be the best write up of a formula I have seen. Pulled apart, each section clearly explained and the result of each bit of the formula displayed, made this very clear for a "Beginner" like me!
    
    Good job xx
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222030)
    
3.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [April 5, 2012 at 3:32 pm](https://chandoo.org/wp/formula-forensics-no-017/#comment-222035)
    
    Very good explanation Faseeh... Thank you so much for writing & welcome.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222035)
    
4.  ![](https://secure.gravatar.com/avatar/1fa33c079ac43b49c628c843129e5b16881679da3a7832c63e7c937bca75daee?s=64&d=mm&r=g) oldchippy says:
    
    [April 5, 2012 at 4:33 pm](https://chandoo.org/wp/formula-forensics-no-017/#comment-222036)
    
    Nice one Faseeh, keep it going
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222036)
    
5.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [April 5, 2012 at 5:47 pm](https://chandoo.org/wp/formula-forensics-no-017/#comment-222041)
    
    Dear all! Luke M, Ksandara2901, Chandoo G, & oldchippy!!
    
    Thanks alot. I am just a humble fan of this site! 😀
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222041)
    
6.  ![](https://secure.gravatar.com/avatar/ce59b0d8e22bf577f01d4211907632b05b396bfcf8c32699db707da405274298?s=64&d=mm&r=g) Steve says:
    
    [April 5, 2012 at 6:29 pm](https://chandoo.org/wp/formula-forensics-no-017/#comment-222042)
    
    Thanks so much to Chandoo for the website--I have learned so much in a short time. Thanks to Faseeh for the formula and explanation. I have been trying to understand the various look up functions lately so this came at a very good time!
    
    May I ask if there is a better reason to use the Index andMatch instead of vlookup in this case? Could the formula also be:
    
    \=IF((D2)<=(TIMEVALUE(VLOOKUP(B2,$B$17:$C$20,2,FALSE))),"Pass","Fail")
    
    Thanks again!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222042)
    
7.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [April 6, 2012 at 12:08 am](https://chandoo.org/wp/formula-forensics-no-017/#comment-222050)
    
    \=IF(D2<INDEX(C$17:C$20,MATCH(B2,B$17:B$20))\*1,"Pass","Fail")
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222050)
    
    *   ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
        
        [April 6, 2012 at 2:43 am](https://chandoo.org/wp/formula-forensics-no-017/#comment-222056)
        
        No sam there is none, your formulas are equally correct and even compactor.. I just prefer Index(Match()) over vlookup() because vlookup can't look left to it, it reads only in the first column of the table ..It always go to it right so the first one is a more general one. But in this case you are right.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222056)
        
8.  ![](https://secure.gravatar.com/avatar/1f13342f9bc6347153cafc8c0b8f9634f576ccd415f5b92705895949fb2593ef?s=64&d=mm&r=g) Melzjm says:
    
    [April 10, 2012 at 8:27 am](https://chandoo.org/wp/formula-forensics-no-017/#comment-222193)
    
    Wow! This is impressive! It is like looking at an excel debugger! Thank you Faseeh for the helpful explanation. I learned a lot! Please keep up the good work! This formula made me keep my job! 🙂
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-222193)
    
9.  ![](https://secure.gravatar.com/avatar/e396b8922686d537e2b2452ff2a343b0fd32e877735909b52ce7c9dfacc90a1e?s=64&d=mm&r=g) Udit says:
    
    [September 17, 2012 at 9:59 am](https://chandoo.org/wp/formula-forensics-no-017/#comment-242216)
    
    Nice way... I just modified it to use vlookup though... I am more comfortable with that than INDEX...
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-017/#comment-242216)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-017/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Sign-up for my Excel Dashboard Masterclass in Australia](https://chandoo.org/wp/sign-up-for-my-excel-dashboard-masterclass-in-australia/) | [There are Easter eggs in this file!!!](https://chandoo.org/wp/easter-eggs-2012/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
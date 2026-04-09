# Calculate maximum change [homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/calculate-maximum-change-homework

---

Calculate maximum change \[homework\]
=====================================

[Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
 - 224 comments

  

Today, lets see how good your formula skills are.

### Calculate maximum change

Can you calculate what is the maximum change in product sales between 2 months for below data?

![Calculate maximum change - Excel formula homework](https://chandoo.org/wp/wp-content/uploads/2014/03/fc-calculate-max-change.png)

_**Bonus question:** Which product is responsible for this change?_

### Post your answers in comments

Just post your answers comments. If you are reading this in RSS or email, [then click here to post your answer](http://chandoo.org/wp/2014/03/21/calculate-maximum-change-homework#respond)
.

**Special note:** If your formula contains < or > symbols when posting it, use &lt; and &gt; instead. Our commenting system eats up < and > symbols.

**Want more Excel challenges?**

**[Try this](http://chandoo.org/wp/excel-problems-challenges/)
** – more than 25 challenges and problems in Excel.

PS: I got inspiration for this challenge from Mike Girvin’s excellent book – [Ctrl + Shift + Enter](http://www.amazon.com/gp/product/1615470077/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1615470077&linkCode=as2&tag=poinhairdilb-20)

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
| Written by Chandoo  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [array formulas](https://chandoo.org/wp/tag/array-formulas/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [max()](https://chandoo.org/wp/tag/max/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 224 Responses to “Calculate maximum change \[homework\]”

1.  ![](https://secure.gravatar.com/avatar/98b75c2c845381fea05d2c78636ffc32802faccee0ca20be4db9bf94522f60c9?s=64&d=mm&r=g) Amit says:
    
    [March 21, 2014 at 8:43 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474944)
    
    Answer to Question
    
    \={MAX(C1:C6/B1:B6)}
    
    Bonus Question  
    \={INDEX(A1:A6,D8,MATCH(MAX(C1:C6/B1:B6),C1:C6/B1:B6,0))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474944)
    
    *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [March 21, 2014 at 9:01 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474950)
        
        @Amit,  
        Did you mean: {=MAX(IFERROR(1-(C1:C6/B1:B6),))}
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474950)
        
    *   ![](https://secure.gravatar.com/avatar/349eb4ac45b0da94520e4a208eb096b9f0d3d5cccc39f923aca2d1fb07e87171?s=64&d=mm&r=g) Kerry says:
        
        [May 15, 2014 at 6:48 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-533199)
        
        Your solution return the maximum positive change not the maximum change. The maximum change occurs in Product 2 with a negative 33% change.
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-533199)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (micky) Avidan says:
            
            [May 16, 2014 at 12:34 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-533906)
            
            @Kerry,  
            Whom do you address with your reply ?  
            It is customary to specify the name.
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-533906)
            
2.  ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [March 21, 2014 at 8:50 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474946)
    
    For ???? MAX Positive Change:  
    \=MAX(C2:C7-B2:B7)  
    \=INDEX(A2:A7,MATCH(MAX(C2:C7-B2:B7),B2:B7-C2:C7))
    
    For MAX Absolute Change:  
    \=MAX((ABS(C2:C7-B2:B7)))  
    \=INDEX(A2:A7,MATCH(MAX(ABS(C2:C7-B2:B7)),ABS(B2:B7-C2:C7),0))
    
    \*\*\* ALL ARRAY FORMULAS !!!  
    Michael (Micky) Avidan
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474946)
    
    *   ![](https://secure.gravatar.com/avatar/6977d5b8fb31861470db30ff7e94956f9498b4c3f5acc101334453e5b41c660d?s=64&d=mm&r=g) [Bigger Don](http://bigdon-in-vbaland.blogspot.com/)
         says:
        
        [October 27, 2014 at 1:44 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-827312)
        
        Micky...I think you've transposed addresses in Max()'s ABS() functions.  
        {=INDEX(A2:A7,MATCH(MAX(ABS(C2:C7-B2:B7)),ABS(B2:B7-C2:C7),0)) } should be {=INDEX(A2:A7,MATCH(ABS(MAX(B2:B7-C2:C7)),ABS(B2:B7-C2:C7),0))}
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-827312)
        
        *   ![](https://secure.gravatar.com/avatar/c8ebee907f330e42b7adb97a239391f4fbe00696cda20131155b31ddfb3cb33d?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [October 27, 2014 at 3:05 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-827393)
            
            Not to my opinion...
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-827393)
            
            *   ![](https://secure.gravatar.com/avatar/6977d5b8fb31861470db30ff7e94956f9498b4c3f5acc101334453e5b41c660d?s=64&d=mm&r=g) [Bigger Don](http://bigdon-in-vbaland.blogspot.com/)
                 says:
                
                [October 27, 2014 at 6:41 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-827625)
                
                Ah! Now I see the difference! I assumed that as in real life situations, because of returns some of the "sales" for a month might be negative.
                
                When I tried your formula I got a different answer than what I would get running it almost by hand. Then I tested with just positives: Your formula gave the right answer, mine the minimum.
                
                The following works with all positives, all negatives, and mixed  
                {=INDEX(A22:A27,MATCH(ABS(MAX(ABS(B22:B27-C22:C27))),ABS(B22:B27-C22:C27),0))}
                
                [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-827625)
                
3.  ![](https://secure.gravatar.com/avatar/6b8bcdbab1b17d903bbb156aa0336a415d10c965945faecbf4c410742d47905a?s=64&d=mm&r=g) Eric Xu says:
    
    [March 21, 2014 at 8:56 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474948)
    
    Max change:{=max(abs(c3:c8-d3:d8))}
    
    Responsible product:{=index(b3:b8,match(max(abs(c3:c8-d3:d8)),abs(c3:c8-d3:d8),0))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474948)
    
4.  ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [March 21, 2014 at 8:59 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474949)
    
    According to the Picture (it is always wise to present a link for the workbook) the formulas should read:
    
    For MAX Positive Change Only:  
    \=MAX(C3:C8-B3:B8)  
    \=INDEX(A3:A8,MATCH(MAX(C3:C8-B3:B8),B3:B8-C3:C8))
    
    For MAX Absolute Change:  
    \=MAX((ABS(C3:C8-B3:B8)))  
    \=INDEX(A3:A8,MATCH(MAX(ABS(C3:C8-B3:B8)),ABS(B3:B8-C3:C8),0))
    
    \*\*\* ALL ARRAY FORMULAS !!!
    
    Michael (Micky) Avidan
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474949)
    
    *   ![](https://secure.gravatar.com/avatar/1b8dddc98a937302a578616384fc36373b3579f28be5476041d557af00400ecb?s=64&d=mm&r=g) Barnabas Path says:
        
        [March 30, 2014 at 7:45 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476548)
        
        When I try your formula, or any of these other formulii, all I can get as a response is either #Name or #Value. What am I missing?
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476548)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [March 30, 2014 at 8:23 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476552)
            
            Barnabas - Some of these formulas use the IFERROR function that was introduced in Excel 2007, and so won't work on earlier versions. Others are array formulas that need to be entered using Ctrl + Shift + Enter.
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476552)
            
            *   ![](https://secure.gravatar.com/avatar/1b8dddc98a937302a578616384fc36373b3579f28be5476041d557af00400ecb?s=64&d=mm&r=g) Barnabas Path says:
                
                [March 31, 2014 at 3:38 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476603)
                
                Thank you Jeff Weir. I'm somewhat of a newbie; researched applying array formulas and just now discovered how powerful that tool is. That was my problem.
                
                [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476603)
                
5.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [March 21, 2014 at 9:36 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474954)
    
    First: =MAX(ABS((C2:C7)-(D2:D7)))  
    Second: =INDEX(B2:B7,MATCH(C16,ABS((C2:C7)-(D2:D7)),0))
    
    Press Ctrl+Shift+Enter to execute..
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474954)
    
6.  ![](https://secure.gravatar.com/avatar/b4873ed7f148fdcb5565d2c4088a97919284dc89a4136ec30bb01da7ce856939?s=64&d=mm&r=g) jraju says:
    
    [March 21, 2014 at 9:46 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474957)
    
    the formula  
    \=MAX(ABS(c3:c87-d3:d87))  
    with control+shift+enter for array formula  
    abs to nullify + or -signs  
    The answer for the above formula is 40.  
    Bonus qu.an. Since the product reduces from 120 to 80
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474957)
    
7.  ![](https://secure.gravatar.com/avatar/b4873ed7f148fdcb5565d2c4088a97919284dc89a4136ec30bb01da7ce856939?s=64&d=mm&r=g) jraju says:
    
    [March 21, 2014 at 9:47 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474958)
    
    Hi, Please edit the formula to d3:d7 instead of d87 inadvertantly posted
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474958)
    
8.  ![](https://secure.gravatar.com/avatar/a2b299f085df47ac183b0ad59ad661022449b78179b80963aafd9fd7f87ef2e1?s=64&d=mm&r=g) Tigris says:
    
    [March 21, 2014 at 9:48 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474959)
    
    {=max(abs(c3:c8-d3:d8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474959)
    
9.  ![](https://secure.gravatar.com/avatar/b4873ed7f148fdcb5565d2c4088a97919284dc89a4136ec30bb01da7ce856939?s=64&d=mm&r=g) jraju says:
    
    [March 21, 2014 at 10:02 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474961)
    
    the difference in % for the product 2 is -33.3. hence the max change
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474961)
    
10.  ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) [Paramdeep Singh](http://www.edupristine.com/ca)
     says:
    
    [March 21, 2014 at 11:03 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474971)
    
    {=MAX(ABS(C3:C8-D3:D8))}  
    // Its an array function
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474971)
    
11.  ![](https://secure.gravatar.com/avatar/c22b75d5d78378b3395b2b104c1f254ea6c19acde0a26f211224d4ec541be2ba?s=64&d=mm&r=g) [Eamon](http://excelforofficeandhome/)
     says:
    
    [March 21, 2014 at 11:32 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474976)
    
    Hi Everyone,  
    Let's say you wanted to catch the biggest increase this month compared to last month. You would use MAX instead of ABS. However, if I use MAX in the array formula I just get #N/A? Why does ABS work and MAX doesn't?
    
    {=INDEX(B2:B7,MATCH(C16,MAX((C2:C7)-(D2:D7)),0))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474976)
    
12.  ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [March 21, 2014 at 11:44 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474978)
    
    @Eamon,  
    Would you be so kind to share with us the "bis secret" U R holding in cell C16 !?  
    Michael (Micky) Avidan
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474978)
    
    *   ![](https://secure.gravatar.com/avatar/c22b75d5d78378b3395b2b104c1f254ea6c19acde0a26f211224d4ec541be2ba?s=64&d=mm&r=g) [Eamon](http://excelforofficeandhome/)
         says:
        
        [March 21, 2014 at 11:46 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474979)
        
        Sorry,
        
        C16 is the returned value from {=MAX(C2:C7)-(B2:B7))}.
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474979)
        
        *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [March 21, 2014 at 12:03 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474984)
            
            @Eamon,  
            To my opinion you get it all wrong/mixed up.  
            In C6 try: =MAX((C2:C7)-(B2:B7)) and for the result try:  
            {=MATCH(C16,(C2:C7)-(B2:B7),0)} insted of: {=MATCH(C16,(C2:C7)-(D2:D7),0)}  
            Michael (Micky) Avidan
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474984)
            
            *   ![](https://secure.gravatar.com/avatar/c22b75d5d78378b3395b2b104c1f254ea6c19acde0a26f211224d4ec541be2ba?s=64&d=mm&r=g) Eamon says:
                
                [March 21, 2014 at 12:07 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474985)
                
                Thanks @Michael (Micky) Avidan.
                
                That worked.
                
                [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474985)
                
13.  ![](https://secure.gravatar.com/avatar/c22b75d5d78378b3395b2b104c1f254ea6c19acde0a26f211224d4ec541be2ba?s=64&d=mm&r=g) Eamon says:
    
    [March 21, 2014 at 11:55 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474980)
    
    Further to my comment I tried the formulas in Google Sheets using the MAX function and they work?
    
    [https://docs.google.com/spreadsheets/d/1uJI5knArPJWgnBZrKrbmo5RBnil59-UguKD423n-Hzk/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1uJI5knArPJWgnBZrKrbmo5RBnil59-UguKD423n-Hzk/edit?usp=sharing)
    
    Weird or bug or feature in Excel 2010?
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474980)
    
14.  ![](https://secure.gravatar.com/avatar/c22b75d5d78378b3395b2b104c1f254ea6c19acde0a26f211224d4ec541be2ba?s=64&d=mm&r=g) Eamon says:
    
    [March 21, 2014 at 11:57 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474981)
    
    Spoke too soon - it gives an answer - but the wrong answer!!!
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474981)
    
15.  ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
    
    [March 21, 2014 at 12:55 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474992)
    
    \=AGGREGATE(14,4,ABS((This.Month)-(Last.Month)),1)
    
    Not array entered
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474992)
    
    *   ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
        
        [March 21, 2014 at 1:03 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474993)
        
        or  
        \=AGGREGATE(14,4,ABS(MMULT(C3:D8,{-1;1})),1)  
        not array entered
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474993)
        
        *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
             says:
            
            [March 21, 2014 at 1:41 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474999)
            
            +1 for clever use of mmult()
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474999)
            
        *   ![](https://secure.gravatar.com/avatar/a79b823d464d67662958606b931ac50d6a0e30e3ad50f9e64085ef35c70c10ba?s=64&d=mm&r=g) Ezequiel says:
            
            [March 21, 2014 at 5:26 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475062)
            
            Hello everyone.  
            First of all sorry for my poor English.  
            Arrives a little late to the challenge and was originally my solution:  
            \= {MAX (ABS (C3: C8-D3: D8))}  
            \= {INDEX (B3: B8, MATCH (MAX (ABS (D3: D8-C3: C8)), ABS (D3: D8-C3: C8), 0), 1)}
            
            After reviewing some comments I see that Kyle's answer is very bright.  
            So my vote is for Kyle. I learn a lot with you.  
            \= AGGREGATE (14, 4, ABS (MMULT (C3: D8; {-1, 1})); 1)  
            \= { INDEX (B3: B8, MATCH (AGGREGATE (14, 4, ABS (MMULT (C3: D8; {-1, 1})); 1), ABS (C3: C8-D3: D8), 0) , 1)}
            
            Greetings.  
            Ezequiel.
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475062)
            
16.  ![](https://secure.gravatar.com/avatar/fa372ae2ae0b4063c593f2508015a4e433646256996cbc07aec12ea8d88e4a05?s=64&d=mm&r=g) Andrew Alexander says:
    
    [March 21, 2014 at 1:32 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474996)
    
    Just because I don't like array formulas (and LOVE Index!):
    
    Max Absolute change:  
    \=MAX(INDEX(ABS(B1:B6-A1:A6),0))
    
    Max Increase  
    \=MAX(INDEX(B1:B6-A1:A6,0))
    
    Max Decrease  
    \=MIN(INDEX(B1:B6-A1:A6,0))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-474996)
    
    *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [March 21, 2014 at 3:11 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475020)
        
        @Andrew,  
        I LOVE blondes but my wife says that coloring the hair harms.  
        If I'm not mistaken - INDEX (although being a very helpful function) is SEMI-VOLATILE and as such it is re-calculated every time the WB is re-opend.  
        On the other side - MAX is not volatile.  
        Michael (Micky) Avidan
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475020)
        
        *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
            
            [March 21, 2014 at 4:35 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475042)
            
            Michael,
            
            INDEX is re-calculated every time the WB is re-open ONLY when it is used to defined a dynamic range. Like =SUM(INDEX(A:A,1):INDEX(A:A,25))
            
            Regards
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475042)
            
    *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
        
        [March 21, 2014 at 4:28 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475037)
        
        Andrew,
        
        You don't like array formulas, but those are array formulas. You just don't confirm them with Ctrl+Shift+Enter
        
        Regards
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475037)
        
        *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [March 21, 2014 at 4:33 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475040)
            
            @Elias,  
            U R 100% correct.  
            The function: SUMPRODUCT works/calculates exactly(!) like {=sum...)} except the need to confirm with CSE - and this is only one example out of many.  
            Michael (Micky) Avidan
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475040)
            
        *   ![](https://secure.gravatar.com/avatar/fa372ae2ae0b4063c593f2508015a4e433646256996cbc07aec12ea8d88e4a05?s=64&d=mm&r=g) Andrew Alexander says:
            
            [March 23, 2014 at 12:57 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475401)
            
            In not too fond of the CSE ones as where I work not many people are aware of them and forget to use CSE when amending them.
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475401)
            
    *   ![](https://secure.gravatar.com/avatar/51d1b8be89259c0e51b298973f19dfe3e44adde58413d13e60241abee77acf6c?s=64&d=mm&r=g) vijay says:
        
        [March 28, 2014 at 9:21 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476100)
        
        you formula are incorrect
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476100)
        
17.  ![](https://secure.gravatar.com/avatar/88ab5418540b40815856128aa249ba6fd413df7fe36c80cd93a835c51a3c8bcb?s=64&d=mm&r=g) Cat2phat says:
    
    [March 21, 2014 at 3:10 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475018)
    
    I think there should be a secondary bonus, however, it would require changing the data a little.
    
    Change Product 1's This Month value from 120 to 140.
    
    The bonus challenge is to list the products that have the same max absolute change.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475018)
    
18.  ![](https://secure.gravatar.com/avatar/f0cab52a19d2bead4ab65a080028b3afd304efb1c966ea0c4f47b3a552a51a6b?s=64&d=mm&r=g) Michael Rivers says:
    
    [March 21, 2014 at 3:12 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475021)
    
    Steps  
    1 - Set Name Ranges for Readability  
    2 - Find Max Value | {=(MAX(Last\_Month-This\_Month))}  
    3 - Find Max Product | {=INDEX(Product,MATCH(MAX(Last\_Month-This\_Month),Last\_Month-This\_Month,0),1)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475021)
    
    *   ![](https://secure.gravatar.com/avatar/f0cab52a19d2bead4ab65a080028b3afd304efb1c966ea0c4f47b3a552a51a6b?s=64&d=mm&r=g) Michael Rivers says:
        
        [March 21, 2014 at 3:25 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475023)
        
        Left out the ABS...didn't fit the population of data but it fits the problem.
        
        1 – Set Name Ranges for Readability  
        2 – Find Max Value | {=(MAX(ABS(Last\_Month-This\_Month)))}  
        3 – Find Max Product | {=INDEX(Product,MATCH((MAX(ABS(Last\_Month-This\_Month))),ABS(Last\_Month-This\_Month),0),1)}
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475023)
        
19.  ![](https://secure.gravatar.com/avatar/cb714ec714d02c01a6371a81f094a8410fbb3046d6cc3d6a1f3273757cb09574?s=64&d=mm&r=g) Ulas says:
    
    [March 21, 2014 at 3:49 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475024)
    
    easy and usefull 🙂  
    {=MAX((B1:B6-A1:A6))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475024)
    
20.  ![](https://secure.gravatar.com/avatar/09e8a4afba66fe7e475348c19e68b61b897cc7e0baa840e1fc2a58b6d9612b6d?s=64&d=mm&r=g) Mani says:
    
    [March 21, 2014 at 3:58 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475026)
    
    {=MAX($B$2:$B$7-$C$2:$C$7)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475026)
    
21.  ![](https://secure.gravatar.com/avatar/7c89b5dac0367b0549376df1e142b1af6c5c08aa7f6797b96efe5d354207e9b0?s=64&d=mm&r=g) aissa says:
    
    [March 21, 2014 at 4:08 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475030)
    
    \={Max(Abs(\[this Month\]-\[lastMonth\]))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475030)
    
22.  ![](https://secure.gravatar.com/avatar/f7153b98a389b7c9a1681e9d8e4435390fe2295555a84039c61283b619773669?s=64&d=mm&r=g) Amey says:
    
    [March 21, 2014 at 4:08 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475031)
    
    Use  
    {=max (d3:d8-c3:c8)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475031)
    
23.  ![](https://secure.gravatar.com/avatar/3494bc4abb65576408bb4eae9d3e9ee988ca19bdc6e8b56cc82c89ee3a6890ad?s=64&d=mm&r=g) samtheman says:
    
    [March 21, 2014 at 4:19 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475034)
    
    {=MAX((C4:C8)-(C3:C7))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475034)
    
24.  ![](https://secure.gravatar.com/avatar/e50229b5d5f7765a07bd36f906a74f169a9b286a94c7dd09115337efe821a9bc?s=64&d=mm&r=g) Vinod says:
    
    [March 21, 2014 at 4:27 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475036)
    
    \={MAX(C1:C6/B1:B6)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475036)
    
25.  ![](https://secure.gravatar.com/avatar/9419442b98bf2bedd9a83327b4cfbe9f59716f7060500eccb105b9946b8a6a4e?s=64&d=mm&r=g) Kevin says:
    
    [March 21, 2014 at 4:31 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475038)
    
    \=(dmax(c3.c8)-dmax(d3.d8))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475038)
    
26.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [March 21, 2014 at 4:32 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475039)
    
    We can get as crazy as we want to get the max value but I think simple is better
    
    Array enter (Ctrl+Shift+Enter)  
    C11 =MAX(D3:D8-C3:C8)
    
    Just enter  
    D11 =LOOKUP(2,1/(D3:D8-C3:C8=C11),B3:B8)
    
    Regards
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475039)
    
27.  ![](https://secure.gravatar.com/avatar/96cf3e04b8344a9fc19149dfc282a7b78b9c646a8c2bbc74ef73a42c350f68d7?s=64&d=mm&r=g) Ari says:
    
    [March 21, 2014 at 4:33 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475041)
    
    The answer is 26.32%.
    
    You need to treat this as an array formula.
    
    {=MAX((THIS MONTH/LAST MONTH)-1)}
    
    OR
    
    Add an extra column and do the percent change and then subject that column through a MAX function...This is a good way to validate that the first formula is correct.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475041)
    
28.  ![](https://secure.gravatar.com/avatar/2cd527125f1dc006aee17492263399788dda5167174ee45861160c5d5da4c401?s=64&d=mm&r=g) Matthew Redman says:
    
    [March 21, 2014 at 4:38 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475043)
    
    \=MAX(ABS(C3:C8-D3:D8))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475043)
    
29.  ![](https://secure.gravatar.com/avatar/03a29183430628bb417c5485494e2e3c4d44a06bde37e084d29ae14eacf8f17a?s=64&d=mm&r=g) Gareth says:
    
    [March 21, 2014 at 4:40 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475044)
    
    \=MAX(($D$3:$D$8-$C$3:$C$8))
    
    and Product Name
    
    \=INDEX($B$3:$E$8,MATCH(MAX(($D$3:$D$8-$C$3:$C$8)),$E$3:$E$8,0),1)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475044)
    
30.  ![](https://secure.gravatar.com/avatar/db84584f4a220b770ff46776db28d79ad199b49c3bef223c39d94ab7e4029f66?s=64&d=mm&r=g) JMuskett says:
    
    [March 21, 2014 at 4:40 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475045)
    
    \=MAX(E2:E7) = 26.32
    
    Where e2 to e7 contain forumla for % ? eg =(D2/C2-1)\*100
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475045)
    
31.  ![](https://secure.gravatar.com/avatar/cf2403d1922a8d1f47b620f97bcea7844bd18f0d747f65a6b35a70f644538211?s=64&d=mm&r=g) Mrudula says:
    
    [March 21, 2014 at 4:41 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475046)
    
    Two solutions proposed:
    
    1)=(MAX(INDEX(ABS((B3:B8-C3:C8)/B3:B8),0))),where B3:B8 is the first column and C3:C8 is the second column as we want largest percentage change its important to consider the abs function. This returns the value 0.33
    
    2)Another variant,convert = MAX(ABS((C3:C8/B3:B8)-1)),convert it to an array formula by means of ctr+shift+enter and you get the same result
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475046)
    
32.  ![](https://secure.gravatar.com/avatar/ec205d2c33c8765a4e3036cf08a7ddfa79254a98764f8c226782eadc05f01dd6?s=64&d=mm&r=g) [remcos](http://n/a)
     says:
    
    [March 21, 2014 at 4:42 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475047)
    
    \={MAX(((C2:C7)-(B2:B7))/(B2:B7))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475047)
    
33.  ![](https://secure.gravatar.com/avatar/223551dad10bbae52f45999a89f5425a5283259507882705257390f41076122c?s=64&d=mm&r=g) Manoj Gupta says:
    
    [March 21, 2014 at 4:43 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475048)
    
    prod 1 100 120 20  
    prod 2 120 80 -40  
    prod 3 90 75 -15  
    prod 4 120 99 -21  
    prod 5 110 110 0  
    prod 6 95 120 25
    
    25
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475048)
    
34.  ![](https://secure.gravatar.com/avatar/95a6eeccbf092cd7d207fa5f0a33b38dc29f27215bf9ac79a9a8c77284ec64ba?s=64&d=mm&r=g) Jason H says:
    
    [March 21, 2014 at 4:44 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475049)
    
    I went with array formulas:
    
    Max change (in any direction):  
    {=MAX(ABS(D3:D8-C3:C8))}
    
    Note this form doesn't preserve the direction (sign) of the change.
    
    Identify product:  
    {=INDEX(B3:B8, MATCH(C11, ABS(D3:D8-C3:C8), 0))}
    
    Where C11 is the already determined max change value from previous formula.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475049)
    
35.  ![](https://secure.gravatar.com/avatar/8743d7035f8ee3dbc3aa76c55784a78e518a341cecdffa2296ea2352530fe17e?s=64&d=mm&r=g) [Tore Softing](http://www.excelkurs.com/)
     says:
    
    [March 21, 2014 at 4:46 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475050)
    
    Use an array formula like this:  
    \=MAX(D3:D8-C3:C8) - save with Control Shift Enter.
    
    To retrieve the product, you could use this array formula:  
    \=INDEX(B3:B8,MATCH(MAX(D3:D8-C3:C8),(D3:D8-C3:C8),0),1)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475050)
    
36.  ![](https://secure.gravatar.com/avatar/e54f4534722022ea1df4ad04f8071cfe460da3614d352f0f9ddecd76a4118791?s=64&d=mm&r=g) Jean-Eric says:
    
    [March 21, 2014 at 4:49 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475051)
    
    Hello,  
    {=MAX(D3:D8-C3:C8)}  
    Ctrl + Shift + Enter
    
    Jean-Eric from France
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475051)
    
37.  ![](https://secure.gravatar.com/avatar/d858a841268b3760404960a5ac4f472f9e920d8e10c5589a8eaebe561434b908?s=64&d=mm&r=g) Brett Hendley says:
    
    [March 21, 2014 at 4:51 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475052)
    
    \={SUM(MAX(ABS($D$3:$D$8-$E$3:$E$8)))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475052)
    
38.  ![](https://secure.gravatar.com/avatar/124691e7265e334c3ab29a996cadad8efa08d6624f6b6254510e814759717349?s=64&d=mm&r=g) Mike Park says:
    
    [March 21, 2014 at 5:04 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475053)
    
    \=MAX( ABS(C3:C8-D3:D8)) yields the correct answer of 40  
    \= INDEX(B3:B8, MATCH(MAX( ABS(C3:C8-D3:D8)), ABS(C3:C8-D3:D8),0 ), 1) correctly returns Product 2  
    both entered as array formulas
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475053)
    
39.  ![](https://secure.gravatar.com/avatar/ea60ced1b1c0dfb5fd0a6e0cc26ac56e771f7f0890af7b4067a59361a51669ab?s=64&d=mm&r=g) AKReeves says:
    
    [March 21, 2014 at 5:23 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475060)
    
    {=MAX(C2:C7-B2:B7)} - Array Formula
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475060)
    
40.  ![](https://secure.gravatar.com/avatar/a5fdd8b283d10fc0e93bd41964bbbf176462e98d114dcae529b22a3523293786?s=64&d=mm&r=g) Arindam says:
    
    [March 21, 2014 at 5:24 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475061)
    
    Me too went with Array...
    
    Situation A: if we are looking for absolute change from last month to this month -  
    Ans. 1) {=MAX(ABS((C3:C8)-(D3:D8)))} --- Returns: 40  
    Ans. Bonus Q.) {=INDEX($B$3:$B$8,MATCH(MAX(ABS($C$3:$C$8-$D$3:$D$8)),ABS($C$3:$C$8-$D$3:$D$8),0))} --- Returns: Product 2
    
    Situation B: If we are looking for absolute % change from last month to this month -
    
    Ans. 1) {=MAX(ABS((D3:D8)/(C3:C8)-1))} --- Returns:33% (with % Format)  
    Ans. Bonus Q.) {=INDEX($B$3:$B$8,MATCH(MAX(ABS(($D$3:$D$8)/($C$3:$C$8)-1)),ABS(($D$3:$D$8)/($C$3:$C$8)-1),0))} --- Returns: Product 2
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475061)
    
41.  ![](https://secure.gravatar.com/avatar/f337a02e3947e956f7e7e3a6af7e23913f8f69224b4f2eaec3caad74b8906c20?s=64&d=mm&r=g) Cauê Tavares says:
    
    [March 21, 2014 at 5:30 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475063)
    
    {=MAX(ABS(B2:B7-C2:C7))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475063)
    
42.  ![](https://secure.gravatar.com/avatar/d308cf41b14536cfe74edca744a5a2bcf5ffa28192aa82f2d0307e600dba27c0?s=64&d=mm&r=g) Char N. says:
    
    [March 21, 2014 at 5:31 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475064)
    
    \=MAX((C3-D3),(C4-D4),(C5-D5),(C6-D6),(C7-D7),(C8-D8))  
    Product 2
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475064)
    
43.  ![](https://secure.gravatar.com/avatar/e712445de79b68469708c0a37c61f16ac300116ecb826f117293b86847cf1508?s=64&d=mm&r=g) [xtbmlguy](http://n/a)
     says:
    
    [March 21, 2014 at 5:31 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475067)
    
    clearly, array formula good answer.
    
    \[Ctrl\]+\[Shift\]+\[Enter\] very nice book. Arrived a couple of days ago. Have been exchanging emails with Mike Girvin. Too bad Microsoft didn't produce manuals a tenth as good as his. Lots of great stuff in the book. And a real nice person. We need one on Data Tables. I just sped up an app which used VBA by using a Data Table as index to multicolumn sheet of data: decreased execution time by over 90%.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475067)
    
44.  ![](https://secure.gravatar.com/avatar/cf2403d1922a8d1f47b620f97bcea7844bd18f0d747f65a6b35a70f644538211?s=64&d=mm&r=g) Mrudula says:
    
    [March 21, 2014 at 5:32 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475068)
    
    Another solution  
    The premise is same as above,except that I am answering the bonus question now and with a different function. Here goes,
    
    \=IF(GCD(B3,C3)=C3,0,GCD(B3,C3))  
    This returns the following in column D,20,40,15,3,0,5 ,now apply max function and it returns 40
    
    Now apply the formula =INDEX(A3:A8,MATCH(E3,ABS(B3:B8-C3:C8),0))  
    ctrl+shft+enter to convert to array formula,it returns product 2
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475068)
    
45.  ![](https://secure.gravatar.com/avatar/9c523cc5975a959f9e750326b307f48881b9c01cd83c6652e3e1ab861017e215?s=64&d=mm&r=g) [Michael K](http://compaqee.com/)
     says:
    
    [March 21, 2014 at 5:37 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475069)
    
    With array formulas I used:
    
    Max (%) Change:  
    {=MAX((K4:K9-J4:J9)/(J4:J9))}
    
    Identify Product: (I created another column on (%) change in column L)  
    \=INDEX(I4:I9,MATCH(J11,L4:L9,0))
    
    Cheers,  
    Mike
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475069)
    
46.  ![](https://secure.gravatar.com/avatar/b2b8320cfaaafb197c0e1f518e7842802c2d4132741737354004a35edb3024c8?s=64&d=mm&r=g) Veiga says:
    
    [March 21, 2014 at 5:37 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475070)
    
    {=MÁXIMO(ABS(D3:D8-C3:C8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475070)
    
47.  ![](https://secure.gravatar.com/avatar/071b3b964530b6130f1bb6b593d1c2c0536ab3e381affc0bbf8fc4b6241b94fc?s=64&d=mm&r=g) JG says:
    
    [March 21, 2014 at 5:40 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475071)
    
    \=MAXA(B3:C3,B4:C4,B5:C5,B6:C6,B7:C7,B8:C8)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475071)
    
48.  ![](https://secure.gravatar.com/avatar/071b3b964530b6130f1bb6b593d1c2c0536ab3e381affc0bbf8fc4b6241b94fc?s=64&d=mm&r=g) JG says:
    
    [March 21, 2014 at 5:40 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475072)
    
    \=MAXA(B3:C3,B4:C4,B5:C5,B6:C6,B7:C7,B8:C8)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475072)
    
49.  ![](https://secure.gravatar.com/avatar/4b277541107d6ccc5ce448d1ae4cafabf83301e340e58b8ca480de4bd1948128?s=64&d=mm&r=g) Arnab says:
    
    [March 21, 2014 at 5:40 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475073)
    
    {=MAX(B2:B7-C2:C7)}  
    2 lesson of the book Ctrl + Shift + Enter
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475073)
    
50.  ![](https://secure.gravatar.com/avatar/201ac3f4b5f6796b84f873d385d6290ae9d8a650fc6ba7f3dd42c650b36fddf7?s=64&d=mm&r=g) Mike F. says:
    
    [March 21, 2014 at 5:45 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475075)
    
    \=MAX(ABS(C3:C8-D3:D8))
    
    Remember that since this is an array formula, instead of pressing the ENTER key, do .
    
    This will attach the array formula and the cell will look like this  
    {=MAX(ABS(C3:C8-D3:D8)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475075)
    
    *   ![](https://secure.gravatar.com/avatar/201ac3f4b5f6796b84f873d385d6290ae9d8a650fc6ba7f3dd42c650b36fddf7?s=64&d=mm&r=g) Mike F. says:
        
        [March 21, 2014 at 5:47 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475076)
        
        ...(ctrl alt enter) instead of enter -- sorry, this got cut off from my message above.
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475076)
        
        *   ![](https://secure.gravatar.com/avatar/201ac3f4b5f6796b84f873d385d6290ae9d8a650fc6ba7f3dd42c650b36fddf7?s=64&d=mm&r=g) Mike F. says:
            
            [March 21, 2014 at 5:49 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475078)
            
            ...sorry again, it is (ctrl shift enter)...how do you edit posts here?
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475078)
            
51.  ![](https://secure.gravatar.com/avatar/3634835f6131806698500bc26a0b020b97d2a7c6249d5be11db4920ba639ed2d?s=64&d=mm&r=g) Paul says:
    
    [March 21, 2014 at 5:48 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475077)
    
    I usually don't like array formulas either where you have to do Ctrl+Shift+Enter, but I decided to give it a try because I thought it was probably the only way to get the answer in one formula. I tried {=MAX(ABS(D3:D8-C3:C8))} and to my pleasure, it worked.
    
    Thanks, Chandoo. Fun little homwork assignment.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475077)
    
52.  ![](https://secure.gravatar.com/avatar/e9017b4068b576e5a01343cc570724a3c163a91b531b085bba0cf39f9ea35428?s=64&d=mm&r=g) BJ says:
    
    [March 21, 2014 at 5:59 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475079)
    
    {=INDEX(B3:B8,MATCH(MAX(ABS((C3:C8-D3:D8)/C3:C8)),ABS((C3:C8-D3:D8)/C3:C8),0))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475079)
    
53.  ![](https://secure.gravatar.com/avatar/da29a8a7d8d3421184371be340a07d90b0cc70ad981f45fc5338c2b9b9bd78ce?s=64&d=mm&r=g) Jim says:
    
    [March 21, 2014 at 6:14 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475082)
    
    {=MAX(ABS(B2:B7-C2:C7))}
    
    I think this formula answers the question as presented - it gives you the magnitude of the change, but not the direction of the change.
    
    {=MAX(C2:C7-B2:B7)}
    
    This formula would provide for the largest positive change, excluding all negative results.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475082)
    
54.  ![](https://secure.gravatar.com/avatar/caff65343f591f48ad5b333a97a393d09e8afcf351e9599a356d55f361aa3b6e?s=64&d=mm&r=g) Kieran says:
    
    [March 21, 2014 at 6:15 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475083)
    
    This will provide the max absolute change and preserve its direction, which seems more useful to me.
    
    \=INDEX((C3:C8-B3:B8), MATCH(MAX(INDEX(ABS(C3:C8-B3:B8),,0)), INDEX(ABS(C3:C8-B3:B8),), 0))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475083)
    
55.  ![](https://secure.gravatar.com/avatar/51c495207d66da32efc28a7a91fce2d9916dccf4b3959c6e87f906bf81672936?s=64&d=mm&r=g) Lewis Kohnle says:
    
    [March 21, 2014 at 6:21 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475084)
    
    {=max(abs(D3:D8-C3:C8))}
    
    Max change = product 2 at 40 units
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475084)
    
56.  ![](https://secure.gravatar.com/avatar/db23e7a1a9651dc9adf5c5a738594a9bec3438831a47b8cee67582822c762e49?s=64&d=mm&r=g) Tim says:
    
    [March 21, 2014 at 6:25 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475085)
    
    All these formulas are well and good to know (absolutely brilliant), but the most important question is, "How does the CUSTOMER (end user) want Max Change defined (positive, negative, ABS, percent change, etc).
    
    Once that is determined, then you can truly wow them with your Excel ninja skills (and save yourself a rewrite).
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475085)
    
57.  ![](https://secure.gravatar.com/avatar/9c59302462e723ce25906f8fc462bf8e98de294136d2f70888d0896edf025fb7?s=64&d=mm&r=g) Sudhakar R says:
    
    [March 21, 2014 at 6:43 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475088)
    
    {=MAX(B1:B6-A1:A6)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475088)
    
    *   ![](https://secure.gravatar.com/avatar/9c59302462e723ce25906f8fc462bf8e98de294136d2f70888d0896edf025fb7?s=64&d=mm&r=g) Sudhakar R says:
        
        [March 21, 2014 at 6:46 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475089)
        
        it is {=MAX(D1:D6-C1:C6)} where curly brackets comes automatically when we press CTRL+SHIFT+Enter
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475089)
        
58.  ![](https://secure.gravatar.com/avatar/c6991daf4d0fea04f5358a825892ce6087ca4a39ea68531348ef4608fe265dd1?s=64&d=mm&r=g) [Don](http://pistulka.com/)
     says:
    
    [March 21, 2014 at 7:27 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475096)
    
    {=IF(ABS(MIN(C3:C8-B3:B8))>MAX(C3:C8-B3:B8),MIN(C3:C8-B3:B8),MAX(C3:C8-B3:B8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475096)
    
59.  ![](https://secure.gravatar.com/avatar/c6991daf4d0fea04f5358a825892ce6087ca4a39ea68531348ef4608fe265dd1?s=64&d=mm&r=g) [Don](http://pistulka.com/)
     says:
    
    [March 21, 2014 at 7:31 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475097)
    
    Did not see the A Column was not used. Try:
    
    {=IF(ABS(MIN(D3:D8-C3:C8))>MAX(D3:D8-C3:C8),MIN(D3:D8-C3:C8),MAX(D3:D8-C3:C8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475097)
    
    *   ![](https://secure.gravatar.com/avatar/c6991daf4d0fea04f5358a825892ce6087ca4a39ea68531348ef4608fe265dd1?s=64&d=mm&r=g) [Don](http://pistulka.com/)
         says:
        
        [March 23, 2014 at 2:12 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475408)
        
        {=IF(ABS(MIN(D3:D8-C3:C8))&gtMAX(D3:D8-C3:C8),MIN(D3:D8-C3:C8),MAX(D3:D8-C3:C8))}
        
        Uses "&gt for >"
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475408)
        
        *   ![](https://secure.gravatar.com/avatar/c6991daf4d0fea04f5358a825892ce6087ca4a39ea68531348ef4608fe265dd1?s=64&d=mm&r=g) [Don](http://pistulka.com/)
             says:
            
            [March 23, 2014 at 2:38 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475414)
            
            Bonus:  
            {=INDEX($B$3:$B$8,MATCH(IF(ABS(MIN(D3:D8-C3:C8))&GTMAX(D3:D8-C3:C8),MIN(D3:D8-C3:C8),MAX(D3:D8-C3:C8)),D3:D8-C3:C8,0))}  
            Uses "&gt" for >
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475414)
            
60.  ![](https://secure.gravatar.com/avatar/fc39355a3428b4eb7c6288807902c0f1500f717a1ea6e3dd9a2150cd7dce51fb?s=64&d=mm&r=g) Ariel says:
    
    [March 21, 2014 at 7:49 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475098)
    
    \=MAX(B2:B7-C2:C7)
    
    then Ctrl + Shift + Enter in the cell
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475098)
    
61.  ![](https://secure.gravatar.com/avatar/a85e04c3e4ed26806a4cfefe8c34d882584254e79dfde9f1a21f747fb25696eb?s=64&d=mm&r=g) [Meni Porat](http://meniporat.blogspot.co.il/)
     says:
    
    [March 21, 2014 at 7:57 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475101)
    
    Array formula:
    
    \=MAX(($C$3:$C$8)-($D$3:$D$8))
    
    (Press: Ctrl+Shift+Enter instead of: Enter)
    
    result=40
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475101)
    
62.  ![](https://secure.gravatar.com/avatar/4422aa956171afc1ea8dd89a8f1c484ac3aeb805c2731f7e41f60986795d9fa4?s=64&d=mm&r=g) Gautham (Krish) says:
    
    [March 21, 2014 at 8:07 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475103)
    
    {=MAX(ABS(C3:C8-D3:D8))} = 40  
    {=INDEX(B3:B8,MATCH(MAX(ABS(C3:C8-D3:D8)),ABS(C3:C8-D3:D8),0))} = Product2  
    Simple:  
    \=120-80=40  
    which is maximum change when you chk individual product, then simply highlight 😉
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475103)
    
63.  ![](https://secure.gravatar.com/avatar/29a806c4ecffeeb3dbafb9eb66796f74f29e3e6e470f8626e909975264852986?s=64&d=mm&r=g) Rifkhan says:
    
    [March 21, 2014 at 8:12 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475104)
    
    {=MAX(C2:C7-D2:D7,D2:D7-C2:C7)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475104)
    
64.  ![](https://secure.gravatar.com/avatar/7c2845d0b0377fe4ee2c5dd4586540e9dbc7ab53b91dc2a0d30971065436a92c?s=64&d=mm&r=g) Rashmi says:
    
    [March 21, 2014 at 8:12 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475105)
    
    {=MAX(ABS(C3:C8-D3:D8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475105)
    
65.  ![](https://secure.gravatar.com/avatar/392a9ab0e12006e07a5d0177f45665e34f3d1f859f5f6ea9e1865e0cc121b36e?s=64&d=mm&r=g) vsieffer says:
    
    [March 21, 2014 at 8:20 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475107)
    
    This formula entered as an array formula calcs the max change  
    \=MAX(ABS(C3:C8-B3:B8))
    
    This formula entered as an array formula calcs the product name located in the first column associated with the max change  
    \=INDEX(A3:C8,MATCH(MAX(ABS(C3:C8-B3:B8)),ABS(C3:C8-B3:B8),0),1)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475107)
    
66.  ![](https://secure.gravatar.com/avatar/62db916e26db536df6c7b1ed431d27bf800d9688988c8b64c433b509030291db?s=64&d=mm&r=g) Mohamed Gaber says:
    
    [March 21, 2014 at 8:38 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475112)
    
    \=MAX(C4-D4,C5-D5,C6-D6,C7-D7,C8-D8,C9-D9)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475112)
    
67.  ![](https://secure.gravatar.com/avatar/96d0eca88eb30c7c94249bc37a42589af4a86fc4a993ae8b4b6a9a18abf6aa57?s=64&d=mm&r=g) [Orlando M](http://www.facebook.com/xltricks)
     says:
    
    [March 21, 2014 at 8:57 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475118)
    
    The question asks for maximum change regardless of the sign of the change so we need to take the magnitude and also think about the problem in terms of percentage. A change from 10 to 20 is greater a change from 100 to 150. In the former case the change is of 100% while in the latter the change is of 50%.
    
    Based on the previous statements one possible option would be:
    
    {=MAX(ABS(C3:C8-D3:D8)/C3:C8)}
    
    The bonus question would be solved as follows:
    
    {=INDEX(B3:B8,MATCH(MAX(ABS(C3:C8-D3:D8)/C3:C8),ABS(C3:C8-D3:D8)/C3:C8,0))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475118)
    
68.  ![](https://secure.gravatar.com/avatar/19ce6bef69a5a216fbac42e4308a8ef633e260226cee692bd65adb3435fb125e?s=64&d=mm&r=g) PavanSada says:
    
    [March 21, 2014 at 9:22 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475122)
    
    {=MAX(B2:B7-C2:C7)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475122)
    
69.  ![](https://secure.gravatar.com/avatar/f9c4b85a0a9b85beec57e34791e14440c631273eed007be1a3beb84d5b6fe0cc?s=64&d=mm&r=g) Uri Weiss says:
    
    [March 21, 2014 at 9:24 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475123)
    
    {=MAX(ABS((C3:C8-B3:B8)/B3:B8))}
    
    Note: Array Formula
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475123)
    
70.  ![](https://secure.gravatar.com/avatar/f9c4b85a0a9b85beec57e34791e14440c631273eed007be1a3beb84d5b6fe0cc?s=64&d=mm&r=g) Uri Weiss says:
    
    [March 21, 2014 at 9:25 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475124)
    
    {=MAX(ABS((C3:C8-B3:B8)/B3:B8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475124)
    
71.  ![](https://secure.gravatar.com/avatar/19ce6bef69a5a216fbac42e4308a8ef633e260226cee692bd65adb3435fb125e?s=64&d=mm&r=g) PavanSada says:
    
    [March 21, 2014 at 9:26 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475125)
    
    Confirmed by Cntrl Shit Entre
    
    {=MAX(ABS(C2:C8)-ABS(D2:D8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475125)
    
72.  ![](https://secure.gravatar.com/avatar/d69d547f5cb8248714b0485baf68554b96c96189471ac5522f28be34c36e9426?s=64&d=mm&r=g) Ronald says:
    
    [March 21, 2014 at 9:42 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475127)
    
    Its an array formula that calculates the max of the absolute value of the variance \[This month\] - \[Last month\]  
    \={MAX(ABS((D3:D8-C3:C8)))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475127)
    
73.  ![](https://secure.gravatar.com/avatar/06ead9563c7c74dc857d50a10382bd165f96ef275eb06920f7122ad75a5d0831?s=64&d=mm&r=g) Gianluca says:
    
    [March 21, 2014 at 10:14 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475134)
    
    Hi Chandoo,  
    I recommend the following 2 CSE-solutions:
    
    max absolute change  
    {=max((D3:D8)-(C3:C8))}  
    max relative change  
    {=max((D3:D8)/(C3:C8)-1)}
    
    Kind regards, Gianluca
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475134)
    
74.  ![](https://secure.gravatar.com/avatar/2d67b79c508903f9080daef445bb404bc75c43158360f30bd503c99ebe5af472?s=64&d=mm&r=g) Alok Joshi says:
    
    [March 21, 2014 at 10:30 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475137)
    
    \=Max(C3:C8-D3:D8)  
    entered as an array formula
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475137)
    
75.  ![](https://secure.gravatar.com/avatar/dad69a6f4960233855a18d0a15eda9ab4edaf16c6218c90775b96fce837e81d6?s=64&d=mm&r=g) Alex Ashin says:
    
    [March 21, 2014 at 11:08 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475141)
    
    {=INDEX(J3:L8,MATCH(MAX(K3:K8-L3:L8),K3:K8-L3:L8,0),1)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475141)
    
76.  ![](https://secure.gravatar.com/avatar/3a3d85e2906c58e36e484dfdc005bce2f49e8839341d29fe7487060ec8eac3e7?s=64&d=mm&r=g) Roger Spire says:
    
    [March 22, 2014 at 12:16 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475146)
    
    Bem a resposta é
    
    {=MÁXIMO(ABS((D3:D8-C3:C8)/C3:C8))}  
    resultado é 33%
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475146)
    
77.  ![](https://secure.gravatar.com/avatar/00c1082b6df2068cab91b7e5197b5e60cf35658109704717b6d73dbc1736cd3d?s=64&d=mm&r=g) Donna Swoope says:
    
    [March 22, 2014 at 12:41 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475148)
    
    \=(d2-c2)/c2  
    copy the formula for rows 3 thru 8  
    then highlight the column with the changes in it, and use conditional formatting to highlight the highest number.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475148)
    
78.  ![](https://secure.gravatar.com/avatar/c1d23f0e63dc68840cb79990e337a7ea800d27fb9712322fe9166c0e2089271b?s=64&d=mm&r=g) Mark Wiley says:
    
    [March 22, 2014 at 1:32 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475153)
    
    {=MAX(ABS(I5:I10-J5:J10))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475153)
    
79.  ![](https://secure.gravatar.com/avatar/c1d23f0e63dc68840cb79990e337a7ea800d27fb9712322fe9166c0e2089271b?s=64&d=mm&r=g) Mark Wiley says:
    
    [March 22, 2014 at 1:36 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475154)
    
    Sorry, I put data in rows I & J instead of C & D.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475154)
    
80.  ![](https://secure.gravatar.com/avatar/8c3d9894b3153ca11a0daf26cde20da71adba5c39e115154cd8cd335eeede1eb?s=64&d=mm&r=g) [Rajesh Chawda](http://nowebsiteofmyown/)
     says:
    
    [March 22, 2014 at 2:05 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475156)
    
    Hi Chandoo,
    
    Here is my solution ..
    
    \=MAX(C3:C8-B3:B8) CTRL+SHIF+ENTER
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475156)
    
81.  ![](https://secure.gravatar.com/avatar/0f272fbef52d877bdb4099e4e342cf43852df46f0db40b53784578ae54342ffa?s=64&d=mm&r=g) Mukesh says:
    
    [March 22, 2014 at 3:56 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475165)
    
    I think this formula will find out max change
    
    \=sum(max(cell reference of this month-cell reference of last month))
    
    and press control shift enter
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475165)
    
82.  ![](https://secure.gravatar.com/avatar/2316df589f6aae48ebb74b0787222a1c9d5baee2db3b2f536fe0861f1c5c60cd?s=64&d=mm&r=g) DavidRaj says:
    
    [March 22, 2014 at 4:49 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475170)
    
    {=MAX(C3:C8-D3:D8)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475170)
    
83.  ![](https://secure.gravatar.com/avatar/c5ab19439d1c64b7b913f24b490d5a3489f343035239d3f744dad783c4ff1daf?s=64&d=mm&r=g) Mamith V says:
    
    [March 22, 2014 at 4:50 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475171)
    
    {=MAX(ABS(C3:C8-D3:D8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475171)
    
84.  ![](https://secure.gravatar.com/avatar/7c9b7c1904bb3bd479c1c941c702a268fe4c82a4acb44d4abb3095c9001ae50e?s=64&d=mm&r=g) [ravi](http://chandoo/)
     says:
    
    [March 22, 2014 at 5:07 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475174)
    
    \=(max(c3:c8)-min(c3:c8))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475174)
    
85.  ![](https://secure.gravatar.com/avatar/5c5419d6800bd683f30e336a53fa672fbb2363bfd716e30ad10e1a70df4a295b?s=64&d=mm&r=g) Sapan Dighe says:
    
    [March 22, 2014 at 5:14 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475178)
    
    I used the following formula with Ctrl+Shift+Enter  
    \=MAX(ABS(C2:C6-B2:B6), ABS(B2:B6-C2:C6))
    
    This will give me max difference irrespective of numerical value in these cells.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475178)
    
    *   ![](https://secure.gravatar.com/avatar/5c5419d6800bd683f30e336a53fa672fbb2363bfd716e30ad10e1a70df4a295b?s=64&d=mm&r=g) Sapan Dighe says:
        
        [March 22, 2014 at 5:20 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475180)
        
        Sorry for the mistaken row numbers. The formula with corrected row numbers is as follows:-(to be used with Ctrl+Shift+Enter)  
        \=MAX(ABS(C3:C8-B3:B8), ABS(B3:B8-C3:C8))
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475180)
        
    *   ![](https://secure.gravatar.com/avatar/e53bafc4c704a81080ce0a89ff242c6052e9db4f70895a7136349221da55ae22?s=64&d=mm&r=g) Sapan S Dighe says:
        
        [March 22, 2014 at 5:22 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475182)
        
        Pardon me for the mistaken row numbers. The formula with corrected row numbers is as follows:-
        
        \=MAX(ABS(C3:C8-B3:B8), ABS(B3:B8-C3:C8))
        
        (to be used with Ctrl+Shift+Enter)
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475182)
        
86.  ![](https://secure.gravatar.com/avatar/dc65f037697aae13238369ab8d110667a93792e34c08ed469b7ca35d01436eac?s=64&d=mm&r=g) NK Jaketia says:
    
    [March 22, 2014 at 5:33 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475184)
    
    {=Max(d3:d8-c3:c8)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475184)
    
87.  ![](https://secure.gravatar.com/avatar/d3cdff2193f19c12f4612ee18748d1f16464d18b8900818bece045b9ea5006ec?s=64&d=mm&r=g) KM Zachariah says:
    
    [March 22, 2014 at 6:13 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475190)
    
    {=MAX(C3:C8-D3:D8)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475190)
    
88.  ![](https://secure.gravatar.com/avatar/6c44e1a50e656a86f7eccb57355c8fb1d499ee334313bca73ca390656dfce7dc?s=64&d=mm&r=g) parisa says:
    
    [March 22, 2014 at 6:20 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475191)
    
    \=max(C1:c8-d1:d8)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475191)
    
    *   ![](https://secure.gravatar.com/avatar/6c44e1a50e656a86f7eccb57355c8fb1d499ee334313bca73ca390656dfce7dc?s=64&d=mm&r=g) parisa says:
        
        [March 22, 2014 at 6:22 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475192)
        
        cntrl+shift+enter
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475192)
        
89.  ![](https://secure.gravatar.com/avatar/02b7aa329c9b6023e967b428a9984cc41b1e3caa22aad710defed358c1bf9dee?s=64&d=mm&r=g) mahesh says:
    
    [March 22, 2014 at 7:04 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475198)
    
    no
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475198)
    
90.  ![](https://secure.gravatar.com/avatar/8b516a0666f5144a824512b14b3d97a3a8729cce8fbc10769ec7390c5342e1e3?s=64&d=mm&r=g) Mukundan says:
    
    [March 22, 2014 at 7:37 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475205)
    
    \=max(large($C$2:$C$8,1),large($d$2:$d$8,1))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475205)
    
91.  ![](https://secure.gravatar.com/avatar/628ea4bc19ad5abeb70f343e2dab3b99207258f4b4d4955e399fdf0be5e03fac?s=64&d=mm&r=g) Vijay says:
    
    [March 22, 2014 at 7:39 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475206)
    
    \=INDEX($A$2:$A$7,MATCH(MAX(($C$2:$C$7)-$B$2:$B$7),(($C$2:$C$7)-($B$2:$B$7)),0),0)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475206)
    
    *   ![](https://secure.gravatar.com/avatar/628ea4bc19ad5abeb70f343e2dab3b99207258f4b4d4955e399fdf0be5e03fac?s=64&d=mm&r=g) Vijay says:
        
        [March 22, 2014 at 7:41 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475207)
        
        \=INDEX($A$2:$A$7,MATCH(MAX(($C$2:$C$7)-$B$2:$B$7),(($C$2:$C$7)-($B$2:$B$7)),0),0) with CSE
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475207)
        
        *   ![](https://secure.gravatar.com/avatar/628ea4bc19ad5abeb70f343e2dab3b99207258f4b4d4955e399fdf0be5e03fac?s=64&d=mm&r=g) Vijay says:
            
            [March 22, 2014 at 7:43 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475208)
            
            \=INDEX($A$2:$A$7,MATCH(MAX(ABS(($C$2:$C$7)-$B$2:$B$7)),ABS((($C$2:$C$7)-($B$2:$B$7))),0),0) with CSE
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475208)
            
92.  ![](https://secure.gravatar.com/avatar/befbddb2b6cc257252cb86b07e7078f4531d9287bcd17f59072d816697a2aaef?s=64&d=mm&r=g) Johnson Mathias says:
    
    [March 22, 2014 at 7:44 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475209)
    
    Highest Value Change (HVC)  
    HVC Product Name  
    \=INDEX(B3:B8,MATCH(MAX(ABS(C3:C8-D3:D8)),ABS(C3:C8-D3:D8),0),1)
    
    HVC Sales Diff Value  
    \=MAX(ABS(B3:B8-C3:C8))
    
    HVC % Diff (first identify the HVC value & derive %)  
    \=MAX(ABS(C3:C8-D3:D8))/INDEX(C3:C8,MATCH(MAX(ABS(C3:C8-D3:D8)),ABS(C3:C8-D3:D8),0),1)
    
    Highest Percentage Change (HPC)  
    HPC Product Name  
    \=INDEX(B3:B8,MATCH(MAX(ABS(C3:C8-D3:D8)/C3:C8),ABS(C3:C8-D3:D8)/C3:C8,0),1)
    
    HPC Sales Diff Value (first identify the HPC Percentage & derive Value)  
    \=ABS(INDEX(C3:C8,MATCH(MAX(ABS(C3:C8-D3:D8)/C3:C8),ABS(C3:C8-D3:D8)/C3:C8,0),1)-INDEX(D3:D8,MATCH(MAX(ABS(C3:C8-D3:D8)/C3:C8),ABS(C3:C8-D3:D8)/C3:C8,0),1))
    
    HPC % Diff  
    \=MAX(ABS(B3:B8-C3:C8)/B3:B8)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475209)
    
93.  ![](https://secure.gravatar.com/avatar/b3c3b91880158dc85c4a32a0cae0e738b2edc9d2f2828493aa5bf6e30475b909?s=64&d=mm&r=g) Tamal Ghosh says:
    
    [March 22, 2014 at 8:03 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475215)
    
    Max %Change :  
    \=INDEX(A3:A19,MATCH(MAX(E3:E19),E3:E19,0))&" : "&ROUND(LARGE(E3:E19,1),0)&"%"
    
    Max Change (Absolute) :  
    \=INDEX(A3:A19,MATCH(MAX(D3:D19),D3:D19,0))&" : "&ROUND(LARGE(D3:D19,1),0)
    
    i've create another two column to calculate absolute change in "D" column & %change in "E" column.  
    answer of 'Bonus Question' included in above formula.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475215)
    
94.  ![](https://secure.gravatar.com/avatar/512bd5c9fc30ff75651701c30c6c5fa3314516a348484d3a90edc44c4968e0c4?s=64&d=mm&r=g) Punet says:
    
    [March 22, 2014 at 8:27 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475220)
    
    \=Max(d3:d8-c3:c8) - array formula
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475220)
    
95.  ![](https://secure.gravatar.com/avatar/befbddb2b6cc257252cb86b07e7078f4531d9287bcd17f59072d816697a2aaef?s=64&d=mm&r=g) Johnson Mathias says:
    
    [March 22, 2014 at 8:30 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475221)
    
    all above formulas are entered by Ctrl Shift Enter
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475221)
    
96.  ![](https://secure.gravatar.com/avatar/af8fbc19fd7b53fed4fe06b8a91462459707b9e69a5e7171e9d138f6286d2688?s=64&d=mm&r=g) Seth Strandin says:
    
    [March 22, 2014 at 9:07 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475226)
    
    Hi everyone.  
    Being on a Power Pivot trip I did it this way:  
    Months on columns, Products on rows  
    Calculated field:  
    (\[ThisMonthSales\]-\[LastMonthSales\])/\[ThisMonthSales\]  
    Sorted Largest to Smallest, and based on the greatest change positive or negative was -33,3% for Product 2.  
    I know this was not a Data Model, but I tested it on Snacks 'R Us.  
    Power Pivot is awesome, and thanks Chandoo for the Power Pivot University on line. From now on I will probably use PP for most of my analysis tasks.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475226)
    
97.  ![](https://secure.gravatar.com/avatar/07dab345e431173036ac7b57a2726c40f56f8968343ce3265f3d1a5326cf9b98?s=64&d=mm&r=g) Yatin says:
    
    [March 22, 2014 at 9:14 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475229)
    
    \=MAX(ABS(F4:F9-E4:E9))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475229)
    
98.  ![](https://secure.gravatar.com/avatar/613715ad3bf6f4fdfa71974b6f3c865209391f063a7564e0e642e0e40af5b07c?s=64&d=mm&r=g) SAMBIT KUMAR MOHAPATRA says:
    
    [March 22, 2014 at 10:33 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475239)
    
    \=MAX(ABS(C5:C10-B5:B10))
    
    Press (CTRL+SHIFT+ENTER) KEY instead of ENTER KEY
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475239)
    
99.  ![](https://secure.gravatar.com/avatar/1e705db54235250fac2896974176dfa6e0d011a3dd36070f515f3bfea0434cd6?s=64&d=mm&r=g) [Eric (France)](http://no/)
     says:
    
    [March 22, 2014 at 11:47 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475249)
    
    maximum change in product sales :  
    {=MAX(D3:D8-C3:C8)}  
    result : 25
    
    Which product is responsible for this change?  
    {=INDEX(B3:B8;EQUIV(MAX(D3:D8-C3:C8);D3:D8-C3:C8;0))}  
    result : product 6
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475249)
    
100.  ![](https://secure.gravatar.com/avatar/ae278de2b0495343c72d7cc07ab0c1573c9df539ed1bc5c6c9c7062d27eb1e74?s=64&d=mm&r=g) RobertThi says:
    
    [March 22, 2014 at 1:30 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475265)
    
    \=MAX(C2:D8)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475265)
    
101.  ![](https://secure.gravatar.com/avatar/29bf64bdb4b6feecb54ff3c2442137bb22e518b9dcf4cff41fc12267bdae13c5?s=64&d=mm&r=g) javhkhlantugs says:
    
    [March 22, 2014 at 2:33 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475273)
    
    \=LARGE(ABS(D3:D8-C3:C8),1)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475273)
    
102.  ![](https://secure.gravatar.com/avatar/fa775a70782e59dc8a39f0a45c4dd8b5bd8817cc81002bfc218401d8edb09bd1?s=64&d=mm&r=g) Mrunal Meher says:
    
    [March 22, 2014 at 2:45 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475275)
    
    Used as an array formula:
    
    \=INDEX(B4:B9,MATCH(MAX(ABS(D4:D9/C4:C9-1)),ABS(D4:D9/C4:C9-1),0))&" is responsible for the change with "&TEXT(MAX(ABS(D4:D9/C4:C9-1)),"##.0%")&" change"
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475275)
    
103.  ![](https://secure.gravatar.com/avatar/4f8762e51993304d8931628a1f8dcbd6a51f39e065f117b08f24658595970949?s=64&d=mm&r=g) John Kragh says:
    
    [March 22, 2014 at 3:15 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475279)
    
    \=MAKSV(ABS(B3-C3);ABS(B4-C4);ABS(B5-C5);ABS(B6-C6);ABS(B7-C7);ABS(B8-C8)) = 40
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475279)
    
104.  ![](https://secure.gravatar.com/avatar/cc949bb818cf2acd5fe3158e7bc80e579eef8bf7ed9ce3895ce85f03ca3e9afe?s=64&d=mm&r=g) Khalid says:
    
    [March 22, 2014 at 3:19 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475280)
    
    for max positive change  
    {=MAX(B2:B7-C2:C7)} with Ctrl+Shift and Enter  
    For bonus question  
    {=INDEX(A2:A7,MATCH(C8,B2:B7-C2:C7,0),)} Again an array formula will go with ctrl+sshift+enter
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475280)
    
105.  ![](https://secure.gravatar.com/avatar/513fbc0b4817abd85275836dfa2068aeafd09ecbcd2d366c984025837cf67996?s=64&d=mm&r=g) Naveen BP says:
    
    [March 22, 2014 at 3:24 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475281)
    
    {=MAX(ABS(E9:E14-F9:F14))}  
    retursns 40
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475281)
    
106.  ![](https://secure.gravatar.com/avatar/1c014ba1e9af62e49c1441dde572e009b0151afdc228d586ece92ab7f01ff6b7?s=64&d=mm&r=g) Thor says:
    
    [March 22, 2014 at 4:20 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475292)
    
    I found the easiest way to do this was to use an array formula to get the biggest difference:
    
    \=MAX((D2:D7-C2:C7))
    
    And in order to get the product, I'd first use the match function to find out which difference was the largest and then use the index function to find the equivalent position in the product string. This formula is also entered as an array formula using ctrl+shift+enter. I live in Denmark so in the formulas I use ";" instead of "," as argument separator.
    
    \=INDEX(B2:B7;MATCH(B11;D2:D7-C2:C7))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475292)
    
107.  ![](https://secure.gravatar.com/avatar/c8b1ff358c5b4cb67c5a7d8bef74e12745ba5437cd0b344320f5ae7aa59c0f08?s=64&d=mm&r=g) hassan says:
    
    [March 22, 2014 at 5:33 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475298)
    
    {=MAX(B1:B6-C1:C6)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475298)
    
108.  ![](https://secure.gravatar.com/avatar/861026334c934827c2c84c93b5a0c5038909e9de9ec224113196ae54e8b00d7a?s=64&d=mm&r=g) Alexis says:
    
    [March 22, 2014 at 6:45 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475305)
    
    \=MAX(ABS($D-$C)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475305)
    
109.  ![](https://secure.gravatar.com/avatar/e273ce22767ba4286f0cd3f05e2be3e7ff3626cc5d5aa4d0c7f4a1a5aca1c86c?s=64&d=mm&r=g) Ankit Chopra says:
    
    [March 22, 2014 at 7:18 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475308)
    
    \=MAX(K3:K8-J3:J8)
    
    K3:K8 = This Month Column  
    J3:J8 = Last Month Column
    
    Answer is 25
    
    Instead of pressing enter, press Ctrl + Shft + Enter ( Array Formula)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475308)
    
110.  ![](https://secure.gravatar.com/avatar/eb3ffbc8e7fd679e486ab23d13b536485fcaf535405dd8bdca8fd274ed8ee540?s=64&d=mm&r=g) Jake says:
    
    [March 22, 2014 at 9:22 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475320)
    
    Knowing the absolute change alone is not terribly meaningful, imo, if you don't know the sign of the change also, so I went this route:
    
    Calculating Maximum Change:  
    {=IF(MAX(C2:C7-B2:B7)>=MAX(ABS(C2:C7-B2:B7)),MAX(C2:C7-B2:B7),MIN(C2:C7-B2:B7))}
    
    \- I first check whether the max of the difference is at least the max of the absolute difference. If it is, then I know that the largest difference is positive, so I return the value of the difference. If it isn't then I know that the largest difference is negative, so I return the value of the smallest difference, i.e., the most negative number.
    
    Bonus Question:  
    \=INDEX(A2:A7,MATCH(IF(MAX(C2:C7-B2:B7)>=MAX(ABS(C2:C7-B2:B7)),MAX(C2:C7-B2:B7),MIN(C2:C7-B2:B7)),C2:C7-B2:B7,0),1)
    
    \- This is just the classic INDEX + MATCH reverse VLOOKUP. The index range is just the list of product names, the second argument is just the answer to the max change question, the third is just 1 since my index range has only one column.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475320)
    
    *   ![](https://secure.gravatar.com/avatar/eb3ffbc8e7fd679e486ab23d13b536485fcaf535405dd8bdca8fd274ed8ee540?s=64&d=mm&r=g) Jake says:
        
        [March 22, 2014 at 9:23 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475321)
        
        Sorry, the bonus question answer should also be an array formula. Here's a corrected version:
        
        Bonus Question:  
        {=INDEX(A2:A7,MATCH(IF(MAX(C2:C7-B2:B7)>=MAX(ABS(C2:C7-B2:B7)),MAX(C2:C7-B2:B7),MIN(C2:C7-B2:B7)),C2:C7-B2:B7,0),1)}
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475321)
        
111.  ![](https://secure.gravatar.com/avatar/857a7032113e1b7ab915c70f00ec6324acd204b1b932ec1963395393ccdd4f6f?s=64&d=mm&r=g) Yogesh says:
    
    [March 23, 2014 at 1:25 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475351)
    
    First: =MAX(ABS((C2:C7)-(D2:D7)))Second:=INDEX(B2:B7,MATCH(C16,ABS((C2:C7)-(D2:D7)),0))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475351)
    
112.  ![](https://secure.gravatar.com/avatar/1cceb2d65227cef923eff7c553e57b3462295de995e90172d148294712660fe5?s=64&d=mm&r=g) Rupesh Kumar says:
    
    [March 23, 2014 at 4:15 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475367)
    
    We can calculate maximum change by using the array formula.  
    {=Max(C3:C8-D3:D8)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475367)
    
113.  ![](https://secure.gravatar.com/avatar/bb109f427be2a172f0a87ad5c448b09831ed883b25ecbf64561ff03b640c6f34?s=64&d=mm&r=g) Frank Bernard says:
    
    [March 23, 2014 at 7:16 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475383)
    
    With your help (how to enter a matrix formula)  
    {=MAX(ABS(D3:D8-C3:C8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475383)
    
114.  ![](https://secure.gravatar.com/avatar/3bbaa9a9d58abbb29ed8a5a873d3d3a1cf7009f2d89acaa1d9b77f6891b49ae3?s=64&d=mm&r=g) Jude Shyju says:
    
    [March 23, 2014 at 10:45 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475394)
    
    Assuming data in A1:C7,
    
    Max Change : {=MAX(ABS(B2:B7-C2:C7))}  
    Product Name : {=INDEX(A2:C7,MATCH(C9,(ABS(B2:B7-C2:C7)),0),1)}
    
    Thanks,  
    Jude Shyju
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475394)
    
115.  ![](https://secure.gravatar.com/avatar/e5b63e805734a79bbe1d476d44d6cbf0880238af765a92a4784a064072c22f39?s=64&d=mm&r=g) Emil Lascau says:
    
    [March 23, 2014 at 11:08 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475398)
    
    \=MAX(D2-C2,D3-C3,D4-C4,D5-C5,D6-C6,D7-C7)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475398)
    
116.  ![](https://secure.gravatar.com/avatar/4bc95f84e1ae0f607a5aed5d470dfd4bf70212828868b4ea35c1dfd062ea4036?s=64&d=mm&r=g) Viraj Chachad says:
    
    [March 23, 2014 at 4:01 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475422)
    
    Hi Chando
    
    I used this formula:
    
    \=MAX(C3:C8-D3:D8) then hit \[CTRL\] + \[SHIFT\] + \[Enter\] for array
    
    Thanks
    
    Viraj
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475422)
    
117.  ![](https://secure.gravatar.com/avatar/f1b558f49b2be9258ba01b30fd11270b4aa0d3bf365a0d0c89d3ce6eaabf4e0e?s=64&d=mm&r=g) Alok Kumar Jena says:
    
    [March 23, 2014 at 6:47 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475436)
    
    \=MAX((ABS(D2:D7-C2:C7)))
    
    Enter Ctrl+Shift+Enter
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475436)
    
118.  ![](https://secure.gravatar.com/avatar/1287eae29018ca83c35452c17bc0ddda8d7d317dd07b868b3de0714aea4fbc59?s=64&d=mm&r=g) Sheela A.M says:
    
    [March 24, 2014 at 2:03 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475469)
    
    \=Max()
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475469)
    
119.  ![](https://secure.gravatar.com/avatar/ed3550eff0acd063de1e923a57ef4b7eb4e8dc3c970f0fc6778182e3ddd27e8e?s=64&d=mm&r=g) Ron Wallace says:
    
    [March 24, 2014 at 3:05 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475474)
    
    Calculate Maximum Change Homework  
    Prod in col B, last month col C, this month col D  
    For max difference =LARGE(D4:D9-C4:C9,1), use S-C-E  
    For product producing max =INDEX($B$4:$B$9,MATCH(MAX($D$4:$D$9-$C$4:$C$9),$D$4:$D$9-$C$4:$C$9,0)), use S-C-E
    
    Arrays are neat. \[Yes, I know I could have used the MAX() in an array to find the max difference, but wanted to show an alternate method\]
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475474)
    
120.  ![](https://secure.gravatar.com/avatar/80565a4d7390e05990a3bfbbf0959227a9c8f48218dfeb19e9c53eefc205ec4a?s=64&d=mm&r=g) hooroy says:
    
    [March 24, 2014 at 3:58 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475477)
    
    Challenge #1 solution:  
    {=MAX(ABS(C3:C8-D3:D8))}  
    Array entered
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475477)
    
    *   ![](https://secure.gravatar.com/avatar/ce03385c69428bac11f48906ef58f91a8fcf38840e808b61df56ed8cc5cff280?s=64&d=mm&r=g) Juda Phali says:
        
        [March 24, 2014 at 5:55 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475482)
        
        Product 6
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475482)
        
121.  ![](https://secure.gravatar.com/avatar/48f0002d2b01875a1a54167465c5193e2d6b62b3e4976c9a43a474aa7dcfc1cf?s=64&d=mm&r=g) Anil Arora says:
    
    [March 24, 2014 at 4:45 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475479)
    
    {=MAX(ABS((C2:C7-B2:B7)/B2:B7))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475479)
    
122.  ![](https://secure.gravatar.com/avatar/2dc3d2ad237d30ebc60423191c35e190c9c239219e4d834b1e5f6088a8fddc08?s=64&d=mm&r=g) Rishab says:
    
    [March 24, 2014 at 6:50 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475489)
    
    25  
    Product 6
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475489)
    
    *   ![](https://secure.gravatar.com/avatar/0234c622c186a415ac23503f7ac398765807b035bbd8d4d937094c4f1c323fc7?s=64&d=mm&r=g) Nik says:
        
        [March 24, 2014 at 11:35 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475531)
        
        Correct answer is 40. product 2
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475531)
        
123.  ![](https://secure.gravatar.com/avatar/0234c622c186a415ac23503f7ac398765807b035bbd8d4d937094c4f1c323fc7?s=64&d=mm&r=g) Nik says:
    
    [March 24, 2014 at 8:31 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475495)
    
    \=max(abs(c3-d3),abs(c4-d4),abs(c5-d5),abs(c6-d6),abs(c7-d7),abs(c8-d8))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475495)
    
124.  ![](https://secure.gravatar.com/avatar/4cccf578eba9d6a0c6f0819006f08b1120ad7ceea3950b93c3a705a04ec49d75?s=64&d=mm&r=g) John Michaloudis says:
    
    [March 24, 2014 at 8:46 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475497)
    
    \={LARGE(ABS((D3:D8)-(C3:C8)),1)}
    
    \={INDEX((B3:B8),MATCH(LARGE((C3:C8)-(D3:D8),1),(C3:C8)-(D3:D8),0))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475497)
    
125.  ![](https://secure.gravatar.com/avatar/164291cfc92a59344169a61fea96ba454ddcd0c76404f50a92ca1b1ccdbecd9f?s=64&d=mm&r=g) Chus says:
    
    [March 24, 2014 at 8:49 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475498)
    
    \={MAX((C2:C5)/(B2:B5)-1)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475498)
    
126.  ![](https://secure.gravatar.com/avatar/8a722d0e52e31a9ccee213886abc40c8599c04e5c5464df3c82a89d064e3f47f?s=64&d=mm&r=g) Henk Stander says:
    
    [March 24, 2014 at 9:03 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475499)
    
    '{=MAX(ABS((D3:D8)-(C3:C8)))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475499)
    
127.  ![](https://secure.gravatar.com/avatar/0e0e59d831f93ddc24665b9a50be43de0c516f0e91d332023f195fc30f790fc3?s=64&d=mm&r=g) waqar says:
    
    [March 24, 2014 at 10:04 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475506)
    
    Max Change 25 {=LARGE(($E$3:$E$8)-($D$3:$D$8),1)}
    
    Max Change 25 { =MAX(($E$3:$E$8)-($D$3:$D$8))}
    
    Product Max Change Product6 { =INDEX($B$3:$E$8,MATCH(MAX(($E$3:$E$8)-($D$3:$D$8)),($E$3:$E$8)-($D$3:$D$8),0),1)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475506)
    
128.  ![](https://secure.gravatar.com/avatar/99244896b5979ad6359d7873b6f16d1913351c2ed426b2c0da3d8a91eb88768b?s=64&d=mm&r=g) RACH says:
    
    [March 24, 2014 at 10:59 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475524)
    
    {=MAX((B3:B8)/(A3:A8)-1)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475524)
    
    *   ![](https://secure.gravatar.com/avatar/99244896b5979ad6359d7873b6f16d1913351c2ed426b2c0da3d8a91eb88768b?s=64&d=mm&r=g) RACH says:
        
        [March 24, 2014 at 11:03 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475525)
        
        Sorry - the last result was based on my own workbook.  
        based on Chandoo's version, below the result  
        {=MAX((D3:D8)/(C3:C8)-1)}
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475525)
        
        *   ![](https://secure.gravatar.com/avatar/99244896b5979ad6359d7873b6f16d1913351c2ed426b2c0da3d8a91eb88768b?s=64&d=mm&r=g) RACH says:
            
            [March 24, 2014 at 11:15 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475529)
            
            in case of cosidering all upward/downward trend, following will work:
            
            {=MAX(ABS(MAX(($D$3:$D$8)-($C$3:$C$8))),ABS(MIN(($D$3:$D$8)-($C$3:$C$8))))}
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475529)
            
129.  ![](https://secure.gravatar.com/avatar/73fbd4fd77ec65084ac130b4c93cba1806115fad2389509b6712034d6e76ba8d?s=64&d=mm&r=g) Olav says:
    
    [March 24, 2014 at 11:55 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475537)
    
    \=MAX(MAX(D2:D7-C2:C7),MAX(C2:C7-D2:D7))  
    entered as an array formula will find the max difference whichever column has the high and low number.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475537)
    
130.  ![](https://secure.gravatar.com/avatar/bfcd0a61098d8da1cab9fa91ad51d63aeba1a73712a079f05d5b595df0c49289?s=64&d=mm&r=g) C.Treffner says:
    
    [March 24, 2014 at 11:56 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475539)
    
    {=MAX(ABS(C3:C8-D3:D8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475539)
    
131.  ![](https://secure.gravatar.com/avatar/1a29326bc228d96d5683d7a05a4b07b61037cef76193090539f18eea0f108a10?s=64&d=mm&r=g) Marco Magalhães says:
    
    [March 24, 2014 at 12:03 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475540)
    
    Consider the following Arrays  
    ProductName=A2:A7  
    lm=B2:B7  
    tm=C2:C7
    
    \=INDEX(ProductName;MATCH(MAX(tm-lm);(tm-lm);0);1) & " with " & MAX(tm-lm)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475540)
    
132.  ![](https://secure.gravatar.com/avatar/b487f330ec96ac52da4745d9d04f3be6dbd590fde4835750467dc4df8d1a0300?s=64&d=mm&r=g) Pablo says:
    
    [March 24, 2014 at 1:52 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475551)
    
    Hello  
    An array formula will do the trick:
    
    {=MAX(C3:C8-B3:B8)}
    
    showing 25, which is the right answer
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475551)
    
133.  ![](https://secure.gravatar.com/avatar/e2d38a7b61ed6b0bfe101e75235fb5469be1b8bee4003bbace72eac2d4cb740e?s=64&d=mm&r=g) canapone says:
    
    [March 24, 2014 at 2:50 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475557)
    
    Hi,
    
    in B10 absolute max difference
    
    \=MAX(INDEX(ABS(B3:B8-C3:C8),0))
    
    in B11 related product name
    
    \=INDEX(A3:A8,MATCH(B10,INDEX(ABS(B3:B8-C3:C8),0),0))
    
    Regards  
    Regards
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475557)
    
134.  ![](https://secure.gravatar.com/avatar/3dd83aa8a6c923d6ad3234a0980fcf693eb2c5f784cd820e4bdbabd7460bf04d?s=64&d=mm&r=g) Chris says:
    
    [March 24, 2014 at 4:19 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475567)
    
    My formula entered as an array  
    \=LARGE(D2:D7-C2:C7,1)
    
    Regards
    
    Chris
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475567)
    
135.  ![](https://secure.gravatar.com/avatar/a16f2b0a2435901c192e86e85ff05faca6640f03b23bab8736010ea99716c1f3?s=64&d=mm&r=g) Kevin says:
    
    [March 24, 2014 at 5:25 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475578)
    
    For the max (input into cell B9):  
    {=(MAX(ABS(B2:B7-C2:C7)))}
    
    For the bonus question:  
    {=INDIRECT(CONCATENATE("A",MATCH(B9,ABS(B1:B7-C1:C7),0)))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475578)
    
136.  ![](https://secure.gravatar.com/avatar/3bffe80d82fb74fb61bd0a0f55b292f031d281407c51edc6f747234161c375ba?s=64&d=mm&r=g) Hanlie Croeser says:
    
    [March 24, 2014 at 6:49 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475590)
    
    {=MAX(C2:C7/B2:B7-1)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475590)
    
137.  ![](https://secure.gravatar.com/avatar/32a7638d648755272776a3c8929bce57e0765cfe30cde07e17d1338eb1ebfe55?s=64&d=mm&r=g) JanWim says:
    
    [March 24, 2014 at 7:24 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475598)
    
    \= max(c3..c8)-min(c3..c8)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475598)
    
138.  ![](https://secure.gravatar.com/avatar/d5d17ceb48d57081e529bd12408ffc66cc96f2abbcbe34de763f07fa4fea2ff9?s=64&d=mm&r=g) [Jerry Giles](http://google/)
     says:
    
    [March 24, 2014 at 10:01 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475614)
    
    \=max(c3-d3,c4-d4,c5-d5,c6-d6,c7-d7,c8-d8)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475614)
    
139.  ![](https://secure.gravatar.com/avatar/e3dd6c3f398ec19109491deeb679941acb8c3ffc60a9da71cba7d4b26731b6cc?s=64&d=mm&r=g) young-Mi Yoo says:
    
    [March 25, 2014 at 5:12 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475644)
    
    {=MAX(ABS(B2:B7-C2:C7))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475644)
    
    *   ![](https://secure.gravatar.com/avatar/a5b6637336a8dc00b1238c70eab4abc9936b4e77e1849756b25f279f8ce5f3a2?s=64&d=mm&r=g) Luigi Neri says:
        
        [March 25, 2014 at 2:02 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475680)
        
        The formula of young-Mi Yoo works.
        
        For the bonus question the answer is :
        
        {=INDEX($B$2:$B$7,MATCH(MAX(ABS(C2:C7-D2:D7)),ABS(C2:C7-D2:D7),0))}
        
        Tested and it works. Thanks for having taught me this nice trick.
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475680)
        
140.  ![](https://secure.gravatar.com/avatar/ed490bcd9059e62de5d8a3fb65e1e6875582b4ba5013026dc3ff10a10fd33312?s=64&d=mm&r=g) Peter Lang says:
    
    [March 25, 2014 at 6:48 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475646)
    
    \=max(D3:D8-C3:c8) and Press Ctrl-Shit-Enter and the formula will be change to this: {=max(D3:D8-C3:c8)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475646)
    
141.  ![](https://secure.gravatar.com/avatar/aa0a5cdf3b08c9d10abdbf3ee21d367439e167d5e79f0f33cf4d1d74ecb0db88?s=64&d=mm&r=g) [Prafull Jadhav](http://-/)
     says:
    
    [March 25, 2014 at 2:46 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475684)
    
    Hi Sir,  
    Please find the below formula ..it is working perfect.  
    Please let me know is it correct ...way ..  
    Please also provide us better way.  
    \={LARGE($D$2:$D$6-$C$2:$C$6,ROW(A1))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475684)
    
142.  ![](https://secure.gravatar.com/avatar/aa0a5cdf3b08c9d10abdbf3ee21d367439e167d5e79f0f33cf4d1d74ecb0db88?s=64&d=mm&r=g) [Prafull Jadhav](http://-/)
     says:
    
    [March 25, 2014 at 2:48 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475685)
    
    \={LARGE($D$2:$D$6-$C$2:$C$6,ROW(A1))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475685)
    
143.  ![](https://secure.gravatar.com/avatar/e6f0c2b5d2e99ac726df1bb9d2d1fa606b9c99bddfd8cacd8a338afb2c4f8d52?s=64&d=mm&r=g) [Adeniyi Ajani](http://www.turningpointdata.net/)
     says:
    
    [March 25, 2014 at 11:28 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475735)
    
    \={MAX(D3:D8-C3:C8)} The {} is entered by excel because it is an array function
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475735)
    
144.  ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra Sharma says:
    
    [March 26, 2014 at 7:31 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475788)
    
    Sorry for responding late...  
    My formula is  
    \=MAX((D2:D7)-(C2:C7))  
    this is an array formula.
    
    With Regards  
    Rudra
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475788)
    
145.  [Calculating Maximum Change \[solutions & discussion\] | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2014/03/26/maximum-change-solutions/)
     says:
    
    [March 26, 2014 at 8:16 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475795)
    
    \[…\] Friday, we had a fun little Excel challenge – Calculate Maximum Change. More than 170 people commented and shared their solutions to this \[…\]
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475795)
    
146.  ![](https://secure.gravatar.com/avatar/0dfa5bb8e7c42438efb81c36194be62fb9227741707c113d7837328cb84f70f3?s=64&d=mm&r=g) aditya says:
    
    [March 26, 2014 at 11:55 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475829)
    
    just find the difference of c and d in e and use max formula in c11.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475829)
    
147.  ![](https://secure.gravatar.com/avatar/66d45a7bceb41fb65cb091cb81dad7817fc2ba6f0203a2120ccbadf998c3fb51?s=64&d=mm&r=g) Abhi says:
    
    [March 26, 2014 at 7:12 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475890)
    
    {=MAX(IF($K$3:$K$8-$J$3:$J$8<0,($K$3:$K$8-$J$3:$J$8)\*-1,$K$3:$K$8-$J$3:$J$8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475890)
    
148.  ![](https://secure.gravatar.com/avatar/28f9f8add1263fe9a7eb17e14ab54367d3703cf84f39a678f6631e26373b0b53?s=64&d=mm&r=g) [Vivek](http://www.vim.ac.in/)
     says:
    
    [March 27, 2014 at 8:35 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475958)
    
    \={INDEX(A2:A7,MATCH(MAX(ABS(C2:C7-B2:B7)),ABS(C2:C7-B2:B7)),0)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-475958)
    
149.  ![](https://secure.gravatar.com/avatar/750ecbcfd44348a6300efb948a0b894ffb5e4c56d288aac541e8152166eab4bb?s=64&d=mm&r=g) Ben Mosbeh Mohamed Slim says:
    
    [March 28, 2014 at 8:25 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476184)
    
    {=Max(ABS(C3-D3))} in absolute terme  
    \=MAX(ABS(C3:C8-D3:D8)/C3:C8) Max rate of change
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476184)
    
150.  ![](https://secure.gravatar.com/avatar/834ca42fa121a1fb75319f053433bcdb16448d25263c59f99a55fddfe554962d?s=64&d=mm&r=g) [Mark Blackburn](http://www.exceler8/co.za)
     says:
    
    [April 2, 2014 at 11:25 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476997)
    
    \=MAX($C$2:$C$7-$B$2:$B$7)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476997)
    
    *   ![](https://secure.gravatar.com/avatar/834ca42fa121a1fb75319f053433bcdb16448d25263c59f99a55fddfe554962d?s=64&d=mm&r=g) [Mark Blackburn](http://www.exceler8/co.za)
         says:
        
        [April 2, 2014 at 11:26 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476998)
        
        That is for the Max positive change
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-476998)
        
151.  ![](https://secure.gravatar.com/avatar/51ae33943eba48f67d13146af3c083a3fa3eea8f64c939273bf3e0d5ebb30a05?s=64&d=mm&r=g) PSG says:
    
    [April 4, 2014 at 5:23 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477267)
    
    \=MAX(ABS((B3:B8)-(C3:C8)))
    
    Press C+S+E (Array Function)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477267)
    
152.  ![](https://secure.gravatar.com/avatar/44dd43efcd84591b09c75e4571d178d7f9aee52a20f77846b0264c2ea9b3ba9b?s=64&d=mm&r=g) Daffy says:
    
    [April 4, 2014 at 5:23 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477268)
    
    Max change {=MAX(ABS(C3:C8-D3:D8))}  
    Max change product {=INDEX(B:B,MATCH(C11,ABS(C:C-D:D),0),)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477268)
    
153.  ![](https://secure.gravatar.com/avatar/266f3f67d3fd200718e02f1863b65ca1fde0088504bb58a771150aacc0c58873?s=64&d=mm&r=g) Mark says:
    
    [April 4, 2014 at 7:24 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477276)
    
    Create table & use array formulas
    
    Absolute Max Change  
    {=MAX(ABS(MyProducts\[This Month\] - MyProducts\[Last Month\]))}
    
    Product Responsible  
    {=INDEX(MyProducts\[Product\],MATCH(MAX(ABS(MyProducts\[Last Month\] - MyProducts\[This Month\])),ABS(MyProducts\[Last Month\]-MyProducts\[This Month\]),0))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477276)
    
154.  ![](https://secure.gravatar.com/avatar/f907534c8010f5652c25fb6c3b2555e5678589bd3adb7eb2306032a06d9b41e4?s=64&d=mm&r=g) Mustafa says:
    
    [April 4, 2014 at 7:37 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477278)
    
    {max(D3:D8-C3:C8)} Its an array formula, and we do that with pressing Ctrl+Shift+Enter
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477278)
    
155.  ![](https://secure.gravatar.com/avatar/b9c0e2b1d3b3c4d5abf2cdba4955ed15b6b0f1ce901a202ac6a894ffe8c10aed?s=64&d=mm&r=g) Laksiri says:
    
    [April 4, 2014 at 11:03 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477294)
    
    Max Change \[on C11\] : =MAX(D3:D8-C3:C8)  
    Product \[on C12\] : =OFFSET(B1,SUM(IF(D3:D8-C3:C8=C11,ROW(D3:D8),0)),0)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477294)
    
156.  ![](https://secure.gravatar.com/avatar/c69ddd921c1a869320e813f9c234190498b96d6e4cdf98634be29071cc926ac4?s=64&d=mm&r=g) Ashok says:
    
    [April 6, 2014 at 5:06 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477414)
    
    CSE formula =MAX(D3:D8-C3:C8)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477414)
    
157.  ![](https://secure.gravatar.com/avatar/614549173491068e224a10fdaa6bed0de9ebe2ffb51f49138f96d1e8be3c4a89?s=64&d=mm&r=g) [Prerit](http://www.prerit.in/)
     says:
    
    [April 7, 2014 at 6:16 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477521)
    
    Max change value =MAX(C2:C7-B2:B7)  
    Max change product = =INDEX(A2:A7,MATCH(MAX(C2:C7-B2:B7),C2:C7-B2:B7,0),1)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477521)
    
158.  ![](https://secure.gravatar.com/avatar/d3217a0779f86ec47db7c25649f906208c68021360b6df58e0b58fb008764a8c?s=64&d=mm&r=g) marvin says:
    
    [April 7, 2014 at 9:14 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477539)
    
    CSE=MAX(ABS(C3:C8-D3:D8))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477539)
    
159.  ![](https://secure.gravatar.com/avatar/22ed94d9bcbfa55f94d9fd1fc2c5934b24ac60cf120d929f3f9b7603e75decc7?s=64&d=mm&r=g) [Vivek S](http://aol/)
     says:
    
    [April 7, 2014 at 9:54 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477546)
    
    \={INDEX(B3:B8,MATCH(MAX(C3:C8-D3:D8),C3:C8-D3:D8,0))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477546)
    
160.  ![](https://secure.gravatar.com/avatar/748c1cf4bbbedb2cfb5e18c07ce86bd4f750b3f805c05d5b0101b8b857a8909e?s=64&d=mm&r=g) Matt Healy says:
    
    [April 8, 2014 at 4:01 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477652)
    
    All very clever, but I want something simple enough that when I open the file six months from now, I can understand what I did. Kernigan and Plauger warned against being too clever at the expense of clarity. So I would just add an auxiliary column with a formula for the change. Then I can use a simple Max formula to get its max, and find which it s using Max and Offset.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-477652)
    
161.  ![](https://secure.gravatar.com/avatar/c27ff3e18ae1788809b98e77f4b4698e0681f6e1753c23861bdb8457a623aa53?s=64&d=mm&r=g) Md. Nazmul Muneer says:
    
    [April 14, 2014 at 4:00 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-478649)
    
    \=INDEX(B3:B8,MATCH(MAX(ABS((C3:C8-D3:D8))),ABS(C3:C8-D3:D8),0))  
    Ctrl+Shift+Enter
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-478649)
    
162.  ![](https://secure.gravatar.com/avatar/5af79bfbd387bf849c0850ca1d1a017f4569a8f8b42580660b42cbe7dc244cb8?s=64&d=mm&r=g) Fay says:
    
    [April 16, 2014 at 12:38 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-479039)
    
    Ans 1: =MAX(ABS(D3:D8-C3:C8))(Ctrl+Shift+Enter)  
    Ans 2: =INDEX(B3:B8,MATCH(MAX(ABS(D3:D8-C3:C8)),ABS(D3:D8-C3:C8),0)) (Ctrl+Shift+Enter)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-479039)
    
163.  ![](https://secure.gravatar.com/avatar/7538a6c411ce17580208b003b65b314d77773545daaeaa6d2676b65033f0c35d?s=64&d=mm&r=g) Maria says:
    
    [April 28, 2014 at 12:12 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-496025)
    
    \=MAX((C3-D3),(C4-D4),(C5-D5),(C6-D6),(C7-D7),(C8-D8))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-496025)
    
164.  ![](https://secure.gravatar.com/avatar/c99c2ff020421a3df29d09d5a09a1eb6f77039f8cb8c29b15e989dbec9c8af9e?s=64&d=mm&r=g) Preeti says:
    
    [April 29, 2014 at 7:12 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-499490)
    
    ans 1. =MAX((ABS(C3:C8-B3:B8))/B3:B8)\*100
    
    ans 2.=INDEX(A3:A8,MATCH(MAX(((ABS(C3:C8-B3:B8))/B3:B8)\*100),(((ABS(C3:C8-B3:B8))/B3:B8)\*100),0))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-499490)
    
165.  ![](https://secure.gravatar.com/avatar/d54e389d993518067566e58ea03ad45491e5d068bca76f5c6a2a42c9f5450af0?s=64&d=mm&r=g) BVGPitt says:
    
    [April 29, 2014 at 6:15 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-500746)
    
    I still can't get rid of the #VALUE! for any of these answers above.  
    It's reading the formula as an error. I am using Excel 2010. I have tried everything.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-500746)
    
    *   ![](https://secure.gravatar.com/avatar/c99c2ff020421a3df29d09d5a09a1eb6f77039f8cb8c29b15e989dbec9c8af9e?s=64&d=mm&r=g) Preeti says:
        
        [April 30, 2014 at 3:03 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-501697)
        
        hi, are you using ctr+shift+enter ? these are array formuale so you can't simply enter !
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-501697)
        
        *   ![](https://secure.gravatar.com/avatar/d54e389d993518067566e58ea03ad45491e5d068bca76f5c6a2a42c9f5450af0?s=64&d=mm&r=g) BVGPitt says:
            
            [April 30, 2014 at 1:05 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-502847)
            
            I tried that before but now realize now you have to do that while the window is still open --- thank you very much! I was doing it after I created the formula!
            
            [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-502847)
            
166.  ![](https://secure.gravatar.com/avatar/0b336d8a83126201d753c43a50ccf9ea4ae8c3573b56c5f51510fdc9d38a1d5b?s=64&d=mm&r=g) Koel Ray says:
    
    [May 7, 2014 at 6:44 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-522497)
    
    \=MAX( ABS(B2:B7-C2:C7))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-522497)
    
    *   ![](https://secure.gravatar.com/avatar/0b336d8a83126201d753c43a50ccf9ea4ae8c3573b56c5f51510fdc9d38a1d5b?s=64&d=mm&r=g) Koel Ray says:
        
        [May 7, 2014 at 6:46 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-522503)
        
        make it an array calculation with ctrl + shift +enter
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-522503)
        
167.  ![](https://secure.gravatar.com/avatar/9e2a35f3db21b763b464279bb7a1b15e7bd4b6174b5f57acde3e2ee52d027646?s=64&d=mm&r=g) Damien says:
    
    [May 21, 2014 at 12:49 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-537972)
    
    \=IF(MAX(D74:D76-C74:C76)&GT=ABS(MIN(D74:D76-C74:C76)),MAX(D74:D76-C74:C76),MIN(D74:D76-C74:C76))
    
    Will tell you the max positive or negative difference I think.
    
    Damien 🙂
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-537972)
    
168.  ![](https://secure.gravatar.com/avatar/b4addf67bd0e8786e80296babfae64fa186fb5028c353389a27a7894e572f45a?s=64&d=mm&r=g) Thiago Cardoso says:
    
    [June 3, 2014 at 2:07 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-547940)
    
    I used:
    
    #1:  
    {=MAX((Tabela1\[This month\]-Tabela1\[Last month\])\*-1)}
    
    #2:  
    {=INDEX(Tabela1\[Product\];MATCH(MAX((Tabela1\[This month\]-Tabela1\[Last month\])\*-1);(Tabela1\[This month\]-Tabela1\[Last month\])\*-1);0)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-547940)
    
169.  ![](https://secure.gravatar.com/avatar/a73f634c34098988cdf039389a3799544e690d885e1e635dad70b7a75280f509?s=64&d=mm&r=g) Ajay Rajguru says:
    
    [June 3, 2014 at 8:36 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-548116)
    
    Question: Which product is responsible for this change?  
    Answer: write the following formula;
    
    \=INDEX(B3:B8,MATCH(B12,INDEX(C3:C8-D3:D8,0),0),1)
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-548116)
    
170.  ![](https://secure.gravatar.com/avatar/bae7297daf02ccda9230b828bbe4b26001f531f420f6d6258ca751c2d9e9db45?s=64&d=mm&r=g) Johne305 says:
    
    [June 25, 2014 at 7:08 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-562670)
    
    Its actually a nice and helpful piece of information. Im glad that you shared this useful information with us. Please keep us up to date like this. Thanks for sharing. cabegfabeekg
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-562670)
    
171.  ![](https://secure.gravatar.com/avatar/31d33cde6dd807e8b3f04bee22071e7eec977029e1e42bea0f98157289b470bd?s=64&d=mm&r=g) John Fuller says:
    
    [July 2, 2014 at 3:24 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-566419)
    
    {=MAX(ABS(C2:C7-D2:D7))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-566419)
    
172.  ![](https://secure.gravatar.com/avatar/09cb124ad5262b455774aed5da89f0b00902502ce224093ca8cf8375c154e522?s=64&d=mm&r=g) Suresh TNVB says:
    
    [July 9, 2014 at 11:28 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-570200)
    
    {=MAX(B2:B7-C2:C7)}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-570200)
    
173.  ![](https://secure.gravatar.com/avatar/0ff1d032f4fa26334e37e7057aec71b07575d6065924ca8e826cc760033a6673?s=64&d=mm&r=g) Jo says:
    
    [July 23, 2014 at 5:52 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-578783)
    
    \={C1:C6-B1:B6} I think this is the simplest formula
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-578783)
    
    *   ![](https://secure.gravatar.com/avatar/7b6b7fab871ac1e2b2dd3b8f5f3502c80cd7034875988482f38d0a2f24ecf46d?s=64&d=mm&r=g) Amanda says:
        
        [August 8, 2014 at 4:52 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-593287)
        
        {=MAX((L11:L16)-(M11:M16))}
        
        [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-593287)
        
174.  ![](https://secure.gravatar.com/avatar/3810fe7ff29db9a59e59050302a8c7cdefe8999ba0206a003684a95f45566d7d?s=64&d=mm&r=g) candychung says:
    
    [August 11, 2014 at 3:17 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-601979)
    
    \={max(abs(c3:C8-D3:D8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-601979)
    
175.  ![](https://secure.gravatar.com/avatar/6977d5b8fb31861470db30ff7e94956f9498b4c3f5acc101334453e5b41c660d?s=64&d=mm&r=g) [Bigger Don](http://bigdon-in-vbaland.blogspot.com/)
     says:
    
    [October 9, 2014 at 9:33 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-804122)
    
    {=MAX(ABS(B2:B7-C2:C7))}  
    IOW 40...
    
    First I tried to wrap my head around array functions from a theoretical standpoint but since I was a Business major and not a math or engineering person, I figured it was beyond me, some sort of esoterica discussed over rabidly by people too nerdy to be gamers. (ahem! If someone doesn't see I'm kidding, I'm sorry)
    
    Then I saw the vlookup array function. OK. That's cool. I do a lot of vlookups and it could save me some headaches and time.
    
    But this challenge made all my doubts go away that I might someday understand a little bit what's going on with array formulas! Thanks for an easy one to get me started!
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-804122)
    
176.  ![](https://secure.gravatar.com/avatar/8e551b9cfe9f81bc780ee2f3f0b8ae5f33aed43809d255b79fc9c26ea17317e8?s=64&d=mm&r=g) Demid says:
    
    [October 25, 2014 at 10:37 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-823780)
    
    {=INDEX($A$2:$A$7,MATCH(MAX(ABS((C2:C7)/(B2:B7)-1)),ABS((C2:C7)/(B2:B7)-1),0))&" ("&ROUND(MAX(ABS((C2:C7)/(B2:B7)-1)),2)&"%)"}
    
    Gives "Product 2 (33%)"
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-823780)
    
177.  ![](https://secure.gravatar.com/avatar/63131c198775bfd9640096a34c42409060cd6b801d633b6c03669b307be5c40f?s=64&d=mm&r=g) jay sharma says:
    
    [January 22, 2015 at 10:06 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-898260)
    
    pklz send me tric
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-898260)
    
178.  ![](https://secure.gravatar.com/avatar/6e9f0101770cde527305c1df0c4715d7bea5d923edbd2cc84908ea885643b6f0?s=64&d=mm&r=g) karan says:
    
    [February 24, 2015 at 6:25 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-919139)
    
    \=MAX(ABS(c3:c87-d3:d87))
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-919139)
    
179.  ![](https://secure.gravatar.com/avatar/843a4b770d05ea44bc6e382c51168b2a391df7829c347b0f0608e4f83220c32f?s=64&d=mm&r=g) Gurminder Singh Puri says:
    
    [June 24, 2015 at 6:59 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-999228)
    
    Step 1. A new Column will be created in Cell D1 , named " Difference Multiplied by (-)1 and the following formula will be entered in Cell D2 :=IF((C2-B2)/B2%<0,((C2-B2)/B2%)\*-1,(C2-B2)/B2%)  
    Step 2. The following Formula will be entered in Cell C11 to find the Maximum Change Value : =MAX(D2:D7)  
    Step 3. Now to find the Product responsible for this change, the following formula will be entered in Cell C13 :=INDEX(A2:D7,MATCH(C11,D2:D7,FALSE),1)  
    Explanation : When we have ascertained that Max. Change ( Either Positive or Negative in the provided data is 50, we have to find out the Row # which contains value 50. This is done by use of the formula =MATCH(C11,D2:D7,FALSE) , which returns the Row # as 2, from range D2:D7 and when we incorporate this Match Formula in the above written Index formula, it returns the value in Col 1 of the range A2:D7.
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-999228)
    
180.  ![](https://secure.gravatar.com/avatar/fb281e6e5c09e08c2f0c0563f1590b2d752f8c79b798b776e212faac85f328da?s=64&d=mm&r=g) [PeterEruteya](http://www.infowavesng.info/)
     says:
    
    [November 1, 2015 at 6:27 am](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-1074519)
    
    The answer is solved using Array Ctrl+Shift+Enter
    
    {=MAX(B2:B8-A2:A8)}
    
    Thanks
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-1074519)
    
181.  ![](https://secure.gravatar.com/avatar/0ee87ce4e36d337838dd1a00dc1d93fb92c6cc4bbd4a94fba23769495103fcb6?s=64&d=mm&r=g) Abhijit Mandal says:
    
    [January 30, 2016 at 12:48 pm](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-1128710)
    
    {=MAX(ABS(B2:B8-C2:C8))}
    
    [Reply](https://chandoo.org/wp/calculate-maximum-change-homework/#comment-1128710)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/calculate-maximum-change-homework/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Free Invoice Template using Excel – Download](https://chandoo.org/wp/free-invoice-template/) | [Why you should close down Excel completely](https://chandoo.org/wp/why-you-should-close-down-excel-completely/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
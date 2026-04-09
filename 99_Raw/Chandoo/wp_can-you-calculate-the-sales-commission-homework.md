# Can you calculate the sales commission? [homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework

---

Can you calculate the sales commission? \[homework\]
====================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 86 comments

  

Imagine you run a cute little pastry in Rome (Italy). To boost the sales you have a 2 person sales team. Caterina & Antonio. Caterina is the manager & Antonio, her assistant.

Apart from basic salary, they will also receive sales commission. This comes from a portion of net profit allocated to “incentive pool”. The sales commission is decided as below:

*   First €25,000 goes to Caterina
*   Any amount between €25,000 and €60,000 is split in 70:30 in favor of Caterina
*   Any amount beyond €60,000 is split 50:50 between Caterina & Antonio

**Your job: Write a formula to calculate the sales commission:**

Assuming,

*   Cell A1 ( named _incentive_ ) contains total amount in incentive pool
*   Cell A2 ( named _first.split_ ) contains €25,000
*   Cell A3 ( named _second.split_ ) contains €60,000
*   Cell B2 ( named _first.ratio_ ) contains 70%
*   Cell B3 ( named _second.ratio_ ) contains 50%

**What formula gives Caterina’s commission?**

And what formula gives Antonio’s commission?

### Post your answers in comments section

Go ahead and share your answers.

PS: This homework problem inspired from [a question in our forum posted by _Robbie._](http://forum.chandoo.org/threads/confused-and-need-help-putting-salary-formulas-together.20389/)

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
| Written by Chandoo  <br>Tags: [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 86 Responses to “Can you calculate the sales commission? \[homework\]”

1.  ![](https://secure.gravatar.com/avatar/f9f2322fec9fe18f2f44865f7ad91b22f5cc4240996930c34751b55d679db5c7?s=64&d=mm&r=g) Vad says:
    
    [November 21, 2014 at 8:22 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-854968)
    
    \=max(second.split-first.split-incentive,0)\*(1-first.ratio)+max(incentive-second.split, 0)\*(1-second.ratio)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-854968)
    
2.  ![](https://secure.gravatar.com/avatar/2ce0b6860ea486b9f91f5ba8422b861e6ce4439b6e01aa261df22a30301fec8f?s=64&d=mm&r=g) juanito says:
    
    [November 21, 2014 at 8:46 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-854982)
    
    Vad's is certainly shorter that what I came up with, but I can't get it to work. Here's mine:  
    (some users may need to change semi-colons to commas)  
    \- juanito
    
    \=MIN(first.split;incentive)+first.ratio\*MIN(second.split-first.split;incentive-first.split)\*(incentive>first.split)+second.ratio\*(incentive-second.split)\*(incentive>second.split)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-854982)
    
3.  ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
    
    [November 21, 2014 at 9:11 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855003)
    
    Here is the answer.
    
    \=IF(incentive>second.split,(incentive-second.split)\*(1-second.ratio)+(second.split-first.split)\*(1-first.ratio),IF(incentive>first.split,(incentive-first.split)\*(1-first.ratio),0))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855003)
    
    *   ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
        
        [November 21, 2014 at 9:31 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855025)
        
        The above formula is for Antonio. Below formula is for Caterina
        
        \=incentive-IF(incentive>second.split,(incentive-second.split)\*(1-second.ratio)+(second.split-first.split)\*(1-first.ratio),IF(incentive>first.split,(incentive-first.split)\*(1-first.ratio),0))
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855025)
        
4.  ![](https://secure.gravatar.com/avatar/5af2cf5ea39d6b77269224dbdbd7796a932368c799654ea3b1de959d5f0dae15?s=64&d=mm&r=g) Robert says:
    
    [November 21, 2014 at 9:16 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855008)
    
    Antonio:  
    \=IF(incentive>second.split,(incentive-second.split)\*second.ratio,)+IF(incentive>=first.split,(MIN(incentive,second.split)-first.split)\*(1-first.ratio),)
    
    Caterina:  
    \=IF(incentivesecond.split,(incentive-second.split)\*second.ratio,)+IF(incentive>=first.split,(MIN(incentive,second.split)-first.split)\*first.ratio,)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855008)
    
5.  ![](https://secure.gravatar.com/avatar/5af2cf5ea39d6b77269224dbdbd7796a932368c799654ea3b1de959d5f0dae15?s=64&d=mm&r=g) Robert says:
    
    [November 21, 2014 at 9:52 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855036)
    
    Oops  
    For Caterina it should read  
    \=if(incentive < = second.split.....
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855036)
    
6.  ![](https://secure.gravatar.com/avatar/c41e028f8bf633779a67a38ab57a5c44cec6506430d6715b4f07583f2e821418?s=64&d=mm&r=g) Ben says:
    
    [November 21, 2014 at 9:56 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855038)
    
    Caterina:  
    \=IF(incentivesecond.split,first.split+((second.split-first.split)\*first.ratio)+(incentive-second.split)\*second.ratio,first.split+(incentive-first.split)\*first.ratio))
    
    Antonio:  
    \=IF(incentivesecond.split,(second.split-first.split)\*(1-first.ratio)+(incentive-second.split)\*second.ratio,(incentive-first.split)\*(1-first.ratio)))
    
    I'm sure there's a better way than nested IFs but this works.
    
    Ben.
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855038)
    
    *   ![](https://secure.gravatar.com/avatar/c41e028f8bf633779a67a38ab57a5c44cec6506430d6715b4f07583f2e821418?s=64&d=mm&r=g) Ben says:
        
        [November 24, 2014 at 9:09 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857266)
        
        VB solution with Caterina's commission in C7 and Antonio's in C9:
        
        Private Sub Worksheet\_SelectionChange(ByVal Target As Range)
        
        Dim cIn As Currency  
        Dim cIn1 As Currency  
        Dim cIn2 As Currency  
        Dim cIn3 As Currency  
        Dim cIn4 As Currency
        
        cIn = Cells(1, 1).Value
        
        If cIn 25000 And cIn 60000 Then  
        cIn1 = 35000 \* 0.7  
        cIn2 = 35000 \* 0.3  
        cIn3 = cIn - 60000  
        cIn4 = cIn3 \* 0.5
        
        Cells(7, 3).Value = 25000 + cIn1 + cIn4  
        Cells(9, 3).Value = cIn2 + cIn4
        
        End If
        
        End Sub
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857266)
        
7.  ![](https://secure.gravatar.com/avatar/4dc639faaf6e67531cbb830d58ec2858c1e27bb6551e34c6234661e1b7165a57?s=64&d=mm&r=g) QL says:
    
    [November 21, 2014 at 9:57 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855044)
    
    Caterina:  
    \=MIN(incentive,first.split) + MAX(MIN(incentive,second.split)-first.split,0)\*first.ratio + MAX(incentive-second.split,0)\*second.ratio
    
    Antonio:  
    \=MAX(MIN(incentive,second.split)-first.split,0)\*(100%-first.ratio) + MAX(incentive-second.split,0)\*(100%-second.ratio)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855044)
    
    *   ![](https://secure.gravatar.com/avatar/37e517c24e67a5520edd2cfaf60a9ed7ea444ce32b01d20114d275197c61540f?s=64&d=mm&r=g) Matt Johnson says:
        
        [November 21, 2014 at 9:54 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855362)
        
        This is exactly how I did it as well.
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855362)
        
    *   ![](https://secure.gravatar.com/avatar/9fb887ece635839a0cf77b3d9d918e84ffa505300d49c898feca71b95ede6bae?s=64&d=mm&r=g) Mark says:
        
        [December 14, 2014 at 4:02 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874614)
        
        My formula for Caterina's was the same.
        
        For Antonio, I had: =incentive - caterina
        
        Where caterina was the cell containing the Caterina formula.
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874614)
        
8.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [November 21, 2014 at 10:02 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855051)
    
    Hi Chandoo.
    
    \=MIN(incentive,first.split)+first.ratio\*MIN(MAX(0,incentive-first.split),second.split-first.split)+second.ratio\*(MAX(0,incentive-second.split))
    
    Regards
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855051)
    
9.  ![](https://secure.gravatar.com/avatar/e21535477ff59298ae74624c20201c0c8f61f86e0e15d39926b62b14182776c4?s=64&d=mm&r=g) K Murugesan says:
    
    [November 21, 2014 at 10:44 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855082)
    
    Caterina:  
    \=IF(Incentive>Second.Split,first.split+((Incentive-first.split)\*Second.ratio),IF(Incentive>first.split,first.split+((Incentive-first.split)\*First.ratio),Incentive))
    
    Antonio:  
    \=IF(Incentive>Second.Split,((Incentive-first.split)\*Second.ratio),IF(Incentive>first.split,((Incentive-first.split)\*(1-First.ratio)),""))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855082)
    
10.  ![](https://secure.gravatar.com/avatar/bf45b53b7627a57311df8c9c64b7d03ee10cc1110f7b6713cf35e10b79eb5bb3?s=64&d=mm&r=g) John long says:
    
    [November 21, 2014 at 3:48 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855193)
    
    \=IF(incentive<=first.split,incentive,IF(incentivesecond.split,((incentive-second.split)\*second.ratio)+((second.split-first.split)\*first.ratio)+first.split,"F")))
    
    So for 25000 she would get 25000  
    for 60000 she would get 49500  
    for 85000 she would get 62000  
    i added figures just to see if i understood the question right lol ... so if anyone matches these ill be happy
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855193)
    
    *   ![](https://secure.gravatar.com/avatar/bf45b53b7627a57311df8c9c64b7d03ee10cc1110f7b6713cf35e10b79eb5bb3?s=64&d=mm&r=g) John long says:
        
        [November 21, 2014 at 3:51 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855195)
        
        \=IF(incentive<=first.split,incentive,IF(incentivesecond.split,((incentive-second.split)\*second.ratio)+((second.split-first.split)\*first.ratio)+first.split,"F")))
        
        looked at my formula in post and it didnt paste properly (missing pieces ???) so will try posting it again
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855195)
        
        *   ![](https://secure.gravatar.com/avatar/bf45b53b7627a57311df8c9c64b7d03ee10cc1110f7b6713cf35e10b79eb5bb3?s=64&d=mm&r=g) John long says:
            
            [November 21, 2014 at 3:53 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855198)
            
            ok its still not pasting in the formula properly so probably best not to allow this post through as it would confuse others if they try it out
            
            [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855198)
            
11.  ![](https://secure.gravatar.com/avatar/6977d5b8fb31861470db30ff7e94956f9498b4c3f5acc101334453e5b41c660d?s=64&d=mm&r=g) [Bigger Don](http://bigdon-in-vbaland.blogspot.com/)
     says:
    
    [November 21, 2014 at 4:33 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855216)
    
    For the Boss (Named incentive.manager )  
    \=MIN(first.split,incentive)  
    +first.ratio\*IF(incentive<first.split,0,MIN(incentive-first.split,first.split))  
    +second.ratio\*IF(incentive<second.split,0,incentive-second.split)
    
    Now, the underling's is easy  
    \= incentive - incentive.manager
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855216)
    
12.  ![](https://secure.gravatar.com/avatar/85bf103b9c66b8a22bf9467a537acdb28cb17fc10140116b29b0bbd4bb1497fc?s=64&d=mm&r=g) Wanderlei Santos says:
    
    [November 21, 2014 at 4:59 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855229)
    
    Caterina: =MIN(incentive,first.split)+(first.ratio\*MIN(MAX(incentive-first.split,0),second.split-first.split))+(second.ratio\*MAX(incentive-second.split,0))  
    Antonio: =((1-first.ratio)\*MIN(MAX(incentive-first.split,0),second.split-first.split))+((1-second.ratio)\*MAX(incentive-second.split,0))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855229)
    
13.  ![](https://secure.gravatar.com/avatar/034312106d10933d12c084f3860bf3f5eabfad9eebcf46e584054137e6bfdd8d?s=64&d=mm&r=g) joão says:
    
    [November 21, 2014 at 6:13 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855250)
    
    I couldn't make it shorter...
    
    \=MIN(incentive,first.split)+first.ratio\*MIN(MAX(0,incentive-first.split),second.split-first.split)+second.ratio\*MAX(0,incentive-second.split)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855250)
    
14.  ![](https://secure.gravatar.com/avatar/9a40b108e2eb818213ac23dd4df4b5d0b3576ff6489b0292885ff8d796aea835?s=64&d=mm&r=g) Todd Peskin says:
    
    [November 21, 2014 at 6:24 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855257)
    
    Here is an option without using IF. I wrote this before seeing Bigger Don's answer, but mine is very similar. I agree with Bigger Don's answer for the underling being the easiest, but I wasn't sure if that was the homework:
    
    Caterina: =MIN(incentve,first.split)+(MAX(first.split,(MIN(incentve,second.split)))-first.split)\*first.ratio+(MAX(incentve,second.split)-second.split)\*second.ratio
    
    Antonio: =(MAX(first.split,(MIN(incentve,second.split)))-first.split)\*(1-first.ratio)+(MAX(incentve,second.split)-second.split)\*(1-second.ratio)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855257)
    
15.  ![](https://secure.gravatar.com/avatar/21e77d3f95933bd1e47cec2c7ce1fb787e57f167f518160616ed5b7622533a88?s=64&d=mm&r=g) Matías says:
    
    [November 21, 2014 at 6:32 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855261)
    
    I know some people hate VLOOKUP, but is nice to resolve this...
    
    Caterina:  
    \=if.error(VLOOKUP(incentive;$A$2:$B$3;2;TRUE)\*incentive;incentive)
    
    for Antonio  
    \=if.error((1-VLOOKUP(incentive;$A$2:$B$3;2;TRUE))\*incentive;0)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855261)
    
16.  ![](https://secure.gravatar.com/avatar/16d9241f7e303d64dd940fc32d3cf13fc84bbafa4f76777f245cdfd7df578730?s=64&d=mm&r=g) Tim Parham says:
    
    [November 21, 2014 at 6:32 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855262)
    
    For Manager  
    \=IF(Incentivefirst.spilt,Incentivesecond.spilt,first.spilt+(second.spilt-first.spilt)\*first.ratio+(Incentive-second.spilt)\*second.ratio)))
    
    For Assistant  
    \=IF(Incentivefirst.spilt,Incentivesecond.spilt,(second.spilt-first.spilt)\*(1-first.ratio)+(Incentive-second.spilt)\*(1-second.ratio))))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855262)
    
17.  ![](https://secure.gravatar.com/avatar/4c6e9aa07c15fbce41a4462c348aef327f4cb0bd069cb43236bd5b11b02fa6d9?s=64&d=mm&r=g) guitarthrower says:
    
    [November 21, 2014 at 6:34 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855263)
    
    Mine is slightly different, but same results
    
    \=MIN(incentive,first.split)  
    +(MIN(MAX(0,incentive-first.split),second.split-first.split)\*first.ratio)  
    +(MAX(incentive-second.split,0)\*second.ratio)
    
    Second formula is simply =incentive-caterina
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855263)
    
18.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [November 21, 2014 at 6:42 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855270)
    
    Hi Chandoo,
    
    If you can post the exact output for some given data, that will resolve the case...
    
    Regards,  
    Faseeh
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855270)
    
19.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [November 21, 2014 at 6:50 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855276)
    
    For 26000, The commision should be 1000\*0.3 =300 ...
    
    \=IF(incentive>=25000,incentive-25000,incentive)\*LOOKUP(incentive,{0,25000,60000},B1:B3)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855276)
    
    *   ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
        
        [November 21, 2014 at 6:53 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855278)
        
        Sorry, 1000 \* 0.7 = 700, but formula still works... for first question
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855278)
        
20.  ![](https://secure.gravatar.com/avatar/21e77d3f95933bd1e47cec2c7ce1fb787e57f167f518160616ed5b7622533a88?s=64&d=mm&r=g) Matías says:
    
    [November 21, 2014 at 6:52 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855277)
    
    There goes another one:
    
    I think than we can simplify this a bit more, but this is around MEDIAN.
    
    for Caterina.  
    \=IF(incentive<first.split;incentive;if(incentive=MEDIAN(A1:A3);first.ratio\*incentive;second.ratio\*incentive))
    
    for Antonio  
    \=IF(incentive<first.split;0;IF(incentive=MEDIAN(A1:A3);(1-first.ratio)\*incentive;(1-second.ratio)\*incentive))
    
    NOTE:  
    In this solution if the incentive is 60000, then still splits 70-30.
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855277)
    
21.  ![](https://secure.gravatar.com/avatar/1987061b30a0a8ee0a72a591a0c58912313f5c5069e4ad6c1901082e0ce375f9?s=64&d=mm&r=g) Nagaraj says:
    
    [November 21, 2014 at 7:09 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855286)
    
    \=MIN(first.split,Incentive)+first.ratio\*MAX(MIN(Incentive-first.split,second.split-first.split),0)+second.ratio\*MAX(Incentive-second.split,0)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855286)
    
22.  ![](https://secure.gravatar.com/avatar/b5e5763f7454eef8b8f600b2cb211178a9eece08d183380e42145a9854ecc4eb?s=64&d=mm&r=g) GGraham says:
    
    [November 21, 2014 at 7:35 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855305)
    
    \=IF(AND((Incentive>first.split),(Incentivesecond.split,Incentive\*second.ratio))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855305)
    
23.  ![](https://secure.gravatar.com/avatar/d41d3a55cf967f57c041f24102a4adb536d3bdae723419a77ff6fd85165979d3?s=64&d=mm&r=g) Rich says:
    
    [November 21, 2014 at 7:41 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855311)
    
    For Antonio=SUMPRODUCT(--(Incentive>first.split), MIN(Incentive-first.split, second.split-first.split), 1-first.ratio)+SUMPRODUCT(--(Incentive>second.split), Incentive-60000, 1-second.ratio)  
    For Caterina = Incentive-Antonio.commission
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855311)
    
24.  ![](https://secure.gravatar.com/avatar/95f9852c3d1a12fb6dbccd3afe0eeff0c9bb9729be943d7c64c3baa06e1dabbe?s=64&d=mm&r=g) [Gregory Mathiesen](http://none/)
     says:
    
    [November 21, 2014 at 9:20 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855350)
    
    for Caterina  
    \=MIN(incentive,first.split) + (incentive>=first.split)\*((incentive-first.split)\*first.ratio) - MAX(incentive-second.split, 0)\*(first.ratio-second.ratio)
    
    for Antonio  
    \=incentive-caterina
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855350)
    
25.  ![](https://secure.gravatar.com/avatar/614549173491068e224a10fdaa6bed0de9ebe2ffb51f49138f96d1e8be3c4a89?s=64&d=mm&r=g) prerit says:
    
    [November 21, 2014 at 9:30 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855354)
    
    Caterina  
    \=MIN(first.split,incentive)+first.ratio\*MIN(incentive-first.split,second.split-first.split)+second.ratio\*MAX(0,incentive-second.split)
    
    Antonio  
    \=(1-first.ratio)\*MIN(incentive-first.split,second.split-first.split)+(1-second.ratio)\*MAX(0,incentive-second.split)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855354)
    
26.  ![](https://secure.gravatar.com/avatar/f6fb631cb5af8ef896c056c59eee762e3c8aebb9b7f99c46044a735449aaa449?s=64&d=mm&r=g) Jeanbar says:
    
    [November 21, 2014 at 11:14 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855383)
    
    Hi,
    
    I prefer to set my variables outside the worksheet just to have them in one place, like this:
    
    With  
    C.Rates ={1,0.7,0.5}  
    A.Rates = 1-C.Rates  
    C.Levels ={0,7.5,12}  
    A.Levels =-C.Levels  
    End
    
    Commission(C) =SUM(((Incentive-C.Levels)>0)\*C.Levels)+Incentive\*INDEX(C.Rates;SUM(N((Incentive-C.Levels)>0))) +CSE  
    Commission(A) =SUM(((Incentive-A.Levels)>0)\*A.Levels)+Incentive\*INDEX(A.Rates;SUM(N((Incentive-A.Levels)>0))) +CSE
    
    The commission formula is symmetrical.
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855383)
    
27.  ![](https://secure.gravatar.com/avatar/88f0d77b590516b222c26dbf08e5c28b743ca6d19235d13770a59612d4617918?s=64&d=mm&r=g) Tom Nijsten says:
    
    [November 21, 2014 at 11:22 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855389)
    
    Caterina=MIN(incentive,first.split)+first.ratio\*MAX(0,MIN(incentive,second.split)-first.split)+second.ratio\*MAX(0,incentive-second.split)
    
    Antonio= incentive - Caterina
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855389)
    
28.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [November 22, 2014 at 2:41 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855548)
    
    Here is a pic Micky Avidan shared about this problem.
    
    ![Formula logic for Sales Commission calculation - Micky Avidan](https://img.chandoo.org/f/sales-comission-calc-micky-1.png)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855548)
    
    *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [November 22, 2014 at 9:17 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855799)
        
        Hi, Chandoo, and all,  
        1) Thanks for posting in my behalf.  
        2) To my opinion - the huge advantage in my approach is the flexibility.  
        The formula stays "simple" also in cases of a large amount of splits.  
        I mainly, use such a formula for IRS progressive calculations.  
        PS: Wouldn't it be a great benefit, for this site, if we could present a picture, by ourselves, without bothering you ?  
        Michael (Micky) Avidan  
        “Microsoft® Answers" - Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855799)
        
        *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
             says:
            
            [November 22, 2014 at 11:13 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855888)
            
            You are welcome Michael. I would love to allow users to post pictures. I just don't know how to with our WordPress native comments. It doesn't allow such thing. I suggest upload the pictures to a free hosting site like flickr and pasting the link here in comments.
            
            [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855888)
            
            *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [November 22, 2014 at 12:25 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855926)
                
                NP.  
                Testing...
                
                ![](https://i60.tinypic.com/2zjbbxz.png)
                
                Michael (Micky) Avidan  
                “Microsoft® Answers” – Wiki author & Forums Moderator  
                “Microsoft®” MVP – Excel (2009-2015)  
                ISRAEL
                
                [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855926)
                
                *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                     says:
                    
                    [November 22, 2014 at 2:55 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855987)
                    
                    Edit by Hui...  
                    I wrapped your URL in an \[Img SRC=" URL"/\] wrapper  
                    But use < > brackets instead  
                    Refer: [http://chandoo.org/wp/2011/11/04/fancy-posts-using-html-display-codes/](http://chandoo.org/wp/2011/11/04/fancy-posts-using-html-display-codes/)
                    
                *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                    
                    [November 22, 2014 at 5:05 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856048)
                    
                    TEST #2:
                    
                *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                    
                    [November 22, 2014 at 5:08 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856050)
                    
                    TEST #3:
                    
                *   ![](https://secure.gravatar.com/avatar/4dc639faaf6e67531cbb830d58ec2858c1e27bb6551e34c6234661e1b7165a57?s=64&d=mm&r=g) QL says:
                    
                    [November 26, 2014 at 10:01 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-858864)
                    
                    Here is a similar approach, which seems easier to understand.
                    
                    Data Setup:  
                    \---------------------------  
                    A B  
                    1 75000  
                    2 0 100%  
                    3 25000 70%  
                    4 60000 50%  
                    \---------------------------  
                    where CELL A1 contains total incentive amount
                    
                    Formula:  
                    \=SUMPRODUCT(--(A1>A2:A4), A1-A2:A4, B2:B4-B1:B3)
                    
29.  ![](https://secure.gravatar.com/avatar/84ba46f1f80bd9f39b5a9ba1c8b02a84860226ab5d77c639eb6c93b1f4dac8b4?s=64&d=mm&r=g) [MF](http://wmfexcel.wordpress.com/)
     says:
    
    [November 22, 2014 at 5:45 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855675)
    
    I do it with a little tweak...  
    A6 = Incentive Pool  
    A1 = 0  
    A2 = 25001  
    A3 = 60001  
    B1 = 100%
    
    For Caterina:  
    \=SUM(LOOKUP(ROW(INDIRECT(("1:"&A6))),A1:B3))  
    Control Shift Enter
    
    For Antonia  
    \=Incentive Pool - Incentive for Caterina
    
    Limitations:  
    Incentive must be a whole number and <= 1048576
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855675)
    
30.  ![](https://secure.gravatar.com/avatar/3c73d030680815be0f341cba1df8023465b3a51dae77656a4e0ab295117c69fb?s=64&d=mm&r=g) Chandra Mohan Singh says:
    
    [November 22, 2014 at 9:35 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855805)
    
    Caterina’s commission=IF(A125000,A160000,(25000+(60000-25000)\*0.7+(A1-60000)\*0.5))))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855805)
    
31.  ![](https://secure.gravatar.com/avatar/3c73d030680815be0f341cba1df8023465b3a51dae77656a4e0ab295117c69fb?s=64&d=mm&r=g) Chandra Mohan Singh says:
    
    [November 22, 2014 at 9:49 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855818)
    
    Caterina's Com."=IF(A125000,A160000,(25000+(60000-25000)\*0.7+(A1-60000)\*0.5))))"
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855818)
    
    *   ![](https://secure.gravatar.com/avatar/3c73d030680815be0f341cba1df8023465b3a51dae77656a4e0ab295117c69fb?s=64&d=mm&r=g) Chandra Mohan Singh says:
        
        [November 22, 2014 at 9:49 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855820)
        
        Caterina's Com."=IF(A125000,A160000,(25000+(60000-25000)\*0.7+(A1-60000)\*0.5))))"
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855820)
        
        *   ![](https://secure.gravatar.com/avatar/3c73d030680815be0f341cba1df8023465b3a51dae77656a4e0ab295117c69fb?s=64&d=mm&r=g) Chandra Mohan Singh says:
            
            [November 22, 2014 at 9:51 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855821)
            
            Sorry Chandoo!! Trying to paste the formula but showing after submitting the comment it is not showing correctly.....
            
            [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855821)
            
            *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [November 22, 2014 at 10:54 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855872)
                
                ...and this is a good reason for allowing to embed(!) a picture into the post.  
                Michael (Micky) Avidan
                
                [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855872)
                
                *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                     says:
                    
                    [November 22, 2014 at 2:37 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855979)
                    
                    @Micky  
                    Also have a read of:  
                    [http://chandoo.org/wp/2011/11/04/fancy-posts-using-html-display-codes/](http://chandoo.org/wp/2011/11/04/fancy-posts-using-html-display-codes/)
                    
32.  ![](https://secure.gravatar.com/avatar/d3cdff2193f19c12f4612ee18748d1f16464d18b8900818bece045b9ea5006ec?s=64&d=mm&r=g) KM Zachariah says:
    
    [November 22, 2014 at 10:24 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855855)
    
    Caterina's commission:
    
    \=IF(incentive=60000,first\_split+first\_ratio\*(second\_split-first\_split)+second\_ratio\*(incentive-second\_split),first\_split+first\_ratio\*(incentive-first\_split)))
    
    Antonio's commission:
    
    \=incentive-IF(incentive=60000,first\_split+first\_ratio\*(second\_split-first\_split)+second\_ratio\*(incentive-second\_split),first\_split+first\_ratio\*(incentive-first\_split)))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-855855)
    
33.  ![](https://secure.gravatar.com/avatar/139ca1f3a51aafe84d2b71104b711e5af04aa8f764a72dea4e4f7595ada3460a?s=64&d=mm&r=g) tenzing says:
    
    [November 22, 2014 at 3:48 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856011)
    
    Mine's not elegant.
    
    For Caterina: IF(incentivefirst.split,incentivesecond.split,first.split+second.ratio\*(incentive-first.split))))
    
    For Antonio: Incentive - Caterina 🙂
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856011)
    
34.  ![](https://secure.gravatar.com/avatar/139ca1f3a51aafe84d2b71104b711e5af04aa8f764a72dea4e4f7595ada3460a?s=64&d=mm&r=g) tenzing says:
    
    [November 22, 2014 at 3:50 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856014)
    
    Mine's not elegant.
    
    IF(incentivefirst.split,incentivesecond.split,first.split+second.ratio\*(incentive-first.split))))
    
    For Antonio: Incentive – Caterina 🙂
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856014)
    
35.  ![](https://secure.gravatar.com/avatar/6eb97a7fc45a22ec93ab2848a971e769d2af5c5a93f4b915137cd460c9ad1c81?s=64&d=mm&r=g) Rich Halecki says:
    
    [November 22, 2014 at 5:28 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856058)
    
    caterina: =CHOOSE(RANK(incentive,$A$1:$C$1),  
    ((incentive-second.split)\*second.ratio)+((second.split-first.split)\*first.ratio)+first.split,  
    ((incentive-first.split)\*first.ratio)+first.split,  
    incentive)
    
    antonio: =CHOOSE(RANK(incentive,$A$1:$C$1),  
    ((incentive-second.split)\*second.ratio)+((second.split-first.split)\*first.ratio)+first.split,  
    ((incentive-first.split)\*first.ratio)+first.split,  
    incentive)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856058)
    
    *   ![](https://secure.gravatar.com/avatar/95f9852c3d1a12fb6dbccd3afe0eeff0c9bb9729be943d7c64c3baa06e1dabbe?s=64&d=mm&r=g) [Gregory Mathiesen](http://none/)
         says:
        
        [November 24, 2014 at 2:48 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857425)
        
        Cool solution using RANK, new to me.
        
        Does not work for me. Chandoo defined incentive and splits as A1:A3.  
        I believe that you put incentive and splits in row A.
        
        I Replaced ...RANK(incentive,$A$1:$C$1)...  
        with ...RANK(incentive,$A$1:$A$3)...  
        and it works perfectly.
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857425)
        
36.  ![](https://secure.gravatar.com/avatar/d4eb401143b7857d8366d729fddf69e94135f5c8ac6faa5b0dcb07cea9cc805d?s=64&d=mm&r=g) Ardraaken says:
    
    [November 22, 2014 at 10:01 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856200)
    
    Mine is totally long winded lol!!!
    
    Caterina = =IF(incentive>=first.split,first.split+IF(AND(incentive>first.split,incentivesecond.split,incentive>first.split),(second.split-first.split)\*first.ratio,0)+IF(incentive>second.split,(incentive-second.split)\*second.ratio,0)),incentive)
    
    Antonio = =IF(incentivefirst.split,incentivesecond.split,incentive>first.split),(second.split-first.split)\*(1-first.ratio),0)+IF(incentive>second.split,(incentive-second.split)\*second.ratio,0)))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856200)
    
37.  ![](https://secure.gravatar.com/avatar/5b754bd84001d2d1e48b44e143cbc82932156783bad93267f3d82ff9572a342f?s=64&d=mm&r=g) James says:
    
    [November 23, 2014 at 5:50 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856421)
    
    Caterina.Commission cell calculated as follows:  
    \=IF(Incentive<First.Split,Incentive,IF(Incentive<Second.Split,First.Split+(Incentive-First.Split)\*First.Ratio,First.Split+(Second.Split-First.Split)\*First.Ratio+(Incentive-Second.Split)\*Second.Ratio))
    
    Antonio.Commission easy as : =Incentive-Caterina.Commission
    
    (but note that this means there is no cross-check)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856421)
    
38.  ![](https://secure.gravatar.com/avatar/dcf5c6d6fdafd91a7523c941e9dabab697786ccb2a1ca0449607e78879939033?s=64&d=mm&r=g) [Santosh](http://na/)
     says:
    
    [November 23, 2014 at 10:32 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856557)
    
    Caterina's Commission  
    \=IF(Incentive<Second.split,(Incentive-First.split)\*First.ratio+First.split,(Incentive-Second.split)\*Second.ratio+(Second.split-First.split)\*First.ratio+First.split)
    
    Antonio's commisson  
    \=IF(Incentive<Second.split,((Incentive-First.split)\*(1-First.ratio)),(Incentive-Second.split)\*Second.ratio+(Second.split-First.split)\*(1-First.ratio))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856557)
    
39.  ![](https://secure.gravatar.com/avatar/9ade1fed55dfa24178ef89ddda5f8c0c421c41dafdfac549727162c2b2f631f9?s=64&d=mm&r=g) Hubert says:
    
    [November 24, 2014 at 2:09 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856971)
    
    For Caterina:  
    \=IF(incentive<first.split,incentive,IF(incentive<second.split,first.split+(incentive-first.split)\*first.ratio,first.split+(second.split-first.split)\*first.ratio+(incentive-second.split)\*second.ratio))
    
    For Antonio:  
    \=IF(incentive<first.split,0,IF(incentive<second.split,(incentive-first.split)\*(1-first.ratio),(second.split-first.split)\*(1-first.ratio)+(incentive-second.split)\*(1-second.ratio)))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-856971)
    
40.  ![](https://secure.gravatar.com/avatar/f94b51469a1fc97cfe870651152b02e1ea0fda5ed99bba10bb018ea8edcb823b?s=64&d=mm&r=g) Medha says:
    
    [November 24, 2014 at 9:01 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857260)
    
    Caterina's commission =  
    IF(incentive>second.split,(incentive-second.split)\*0.5+49500,IF(incentive>first.split,(incentive-first.split)\*0.7+first.split,incentive))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857260)
    
    *   ![](https://secure.gravatar.com/avatar/f94b51469a1fc97cfe870651152b02e1ea0fda5ed99bba10bb018ea8edcb823b?s=64&d=mm&r=g) Medha says:
        
        [November 24, 2014 at 9:02 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857262)
        
        Antonio's commission:
        
        \=incentive-Caterina’s commission
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857262)
        
41.  ![](https://secure.gravatar.com/avatar/460be5157a8ff55b9ffdf755dce4658a7d42130b5bda58c43f07368eb6088d00?s=64&d=mm&r=g) Daniel says:
    
    [November 24, 2014 at 11:07 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857324)
    
    An old trick using differential rates
    
    Brackets = {0,25000,60000}
    
    For Caterina:
    
    Ratios = {100%,70%,50%}  
    Dif\_ratios\_Cat = {100%,-30%,-20%}  
    Caterina =SUMPRODUCT(--(Incentive>Brackets),Incentive-Brackets,Dif\_ratios\_Cat)
    
    For Caterina:
    
    Ratios = {0%,30%,20%}  
    Dif\_ratios\_Ant = {0%,30%,20%}  
    Antonio =SUMPRODUCT(--(Incentive>Brackets),Incentive-Brackets,Dif\_ratios\_Ant)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857324)
    
    *   ![](https://secure.gravatar.com/avatar/460be5157a8ff55b9ffdf755dce4658a7d42130b5bda58c43f07368eb6088d00?s=64&d=mm&r=g) Daniel says:
        
        [November 24, 2014 at 11:51 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857340)
        
        My mistake:
        
        For Antonio:
        
        Ratios = {0%,30%,20%}  
        Dif\_ratios\_Ant = {0%,30%,20%}  
        Antonio =SUMPRODUCT(–(Incentive>Brackets),Incentive-Brackets,Dif\_ratios\_Ant)
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857340)
        
        *   ![](https://secure.gravatar.com/avatar/460be5157a8ff55b9ffdf755dce4658a7d42130b5bda58c43f07368eb6088d00?s=64&d=mm&r=g) Daniel says:
            
            [November 24, 2014 at 1:09 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857371)
            
            Another one, in both formulas use "--" not "-"
            
            Caterina =SUMPRODUCT(--(Incentive>Brackets),Incentive-Brackets,Dif\_ratios\_Cat
            
            Antonio =SUMPRODUCT(--(Incentive>Brackets),Incentive-Brackets,Dif\_ratios\_Ant)
            
            [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857371)
            
42.  ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra says:
    
    [November 24, 2014 at 12:25 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857351)
    
    Assuming that incentive is 100000, first 25 k goes to the Caterina .Next 35 K is shared in the ratio of 7:3 and finally remaining about in the ratio of 50:50. My Formula to Calculate;
    
    Caterina's Share : =25000+(0.7\*35000)+((Incentive-second.split)\*0.5)  
    Antonio's Share : =Incentive- Caterina's Share
    
    Regards  
    Rudra
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857351)
    
43.  ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra says:
    
    [November 24, 2014 at 12:28 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857352)
    
    Bit of Correction
    
    Assuming that incentive is 100000, first 25 k goes to the Caterina .Next 35 K is shared in the ratio of 7:3 and finally remaining about in the ratio of 50:50. My Formula to Calculate;
    
    Caterina’s Share : ==first.split+(0.7\*(second.split-first.split))+((Incentive-second.split)\*0.5)  
    Antonio’s Share : =Incentive- Caterina’s Share
    
    Regards  
    Rudra
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857352)
    
44.  ![](https://secure.gravatar.com/avatar/bfcd0a61098d8da1cab9fa91ad51d63aeba1a73712a079f05d5b595df0c49289?s=64&d=mm&r=g) Cristof says:
    
    [November 24, 2014 at 3:31 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857446)
    
    Here is my solution:  
    Caterina:  
    \=MIN(A2;B2)+MIN(MAX(A2-B2;0);C2-B2)\*D2+MAX(A2-C2;0)\*E2
    
    Antonio:  
    \=MIN(MAX(A2-B2;0);C2-B2)\*(1-D2)+MAX(A2-C2;0)\*(1-E2)
    
    When..  
    A2 = Incentive  
    B2 = First.Split  
    C2 = Second.Split  
    D2 = First.Ratio  
    E2 = Second.Ratio
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857446)
    
45.  ![](https://secure.gravatar.com/avatar/ecb738242617857cad5dc9cdae85037999ca39251c939048828204b4119442f0?s=64&d=mm&r=g) Richy says:
    
    [November 24, 2014 at 3:38 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857448)
    
    Formula in C6
    
    Antonio =IF(A1>=A3,IF(A1>A2,(A3-A2)\*(1-A4))+IF(A1>=A3,(A1-A3)\*A5),IF(AND(A1>=A2,A1<=A3),(A1-A2)\*(1-A4),0))
    
    Caterina =A1-C6
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857448)
    
46.  ![](https://secure.gravatar.com/avatar/75c334365ff4885a44651a26505d1dad31307eafc37667131ab9089d8594d1ff?s=64&d=mm&r=g) Haz says:
    
    [November 24, 2014 at 6:59 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857503)
    
    Caterina's  
    \=MIN(A1;A2)+MIN(A1-MIN(A1;A2);A3-A2)\*A4+MAX(A1-A3;0)\*A5
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-857503)
    
47.  ![](https://secure.gravatar.com/avatar/bf0a2f4e213b4acccef3339e03520f6ec02a81cc6ca8cd47aec1af3495a0dbf2?s=64&d=mm&r=g) John Jairo V says:
    
    [November 25, 2014 at 7:04 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-858300)
    
    Here is my aproach:
    
    For Catherina:  
    \=MIN(A1:A2)+A4\*(MEDIAN(A1:A3)-A2)+A5\*MAX(0,A1-A3)  
    For Antonio:  
    \=(1-A4)\*(MEDIAN(A1:A3)-A2)+(1-A5)\*MAX(0,A1-A3)
    
    Blessings!
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-858300)
    
48.  ![](https://secure.gravatar.com/avatar/fd9af4acce1439d437e4e11131e7ec072beda281b7e1b28fef9899c498ae9cbc?s=64&d=mm&r=g) Alex says:
    
    [November 25, 2014 at 8:23 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-858333)
    
    Yet another formula, with Frequency  
    Need to have cell B1 filled with 100%
    
    For Caterina:  
    \=SUMPRODUCT(SMALL(A1:A3,ROW(A1:A3))\*(B1:B3-OFFSET(B1:B3,1,)\*(ROW(A1:A3)<INDEX(FREQUENCY(A1:A3,A1),1)))\*(ROW(A1:A3)<=INDEX(FREQUENCY(A1:A3,A1),1)))
    
    Antonio = A1- Caterina
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-858333)
    
49.  ![](https://secure.gravatar.com/avatar/4874014916579d097ade58bc0d93ad65933b3c412b641891ccfa9941d1ccaab5?s=64&d=mm&r=g) Mark says:
    
    [November 26, 2014 at 3:53 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-859085)
    
    Hi Chandoo,
    
    i've used this plugin in the past, which works with the native wordpress comments system and allows commenters to upload images as part of their comment.
    
    [https://wordpress.org/plugins/comment-images/](https://wordpress.org/plugins/comment-images/)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-859085)
    
50.  ![](https://secure.gravatar.com/avatar/8c5f4db9c554db6032672e5edf80981a34e34cb9f852c088d38bc12f116ff667?s=64&d=mm&r=g) Jeremy says:
    
    [December 2, 2014 at 5:08 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-863179)
    
    Caterina = IF(incentive<first.split,incentive,first.split+MIN(incentive-first.split,second.split-first.split)\*first.ratio+(incentive-first.split-MIN(incentive-first.split,second.split-first.split))\*second.ratio)
    
    Antonio = IF(incentive<first.split,0,incentive-Caterina)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-863179)
    
51.  ![](https://secure.gravatar.com/avatar/5dfb9f33ef06e000ac1aa5c24be44fe1810b004ce9dfcae529e871fc0741e984?s=64&d=mm&r=g) Gerhard says:
    
    [December 2, 2014 at 7:00 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-863705)
    
    Hi Chandoo and friends of chandoo.org,  
    I'm from germany and here are my versions of the formulas. I wrote it firstly in the german excel language. So I hope it's right in english.  
    Sorry, that are long formulas, but I like it.
    
    Caterina:  
    \=first.split+If((incentive-first.split)>60,(second.split-first.split)\*first.ratio,"")+(incentive-first.split-If((incentive-first.split)>60,(second.split-first.split)\*first.ratio,"")-If((incentive-first.split)>60,(second.split-first.split)\*(1-first.ratio),""))\*second.ratio
    
    Antonio:  
    \=incentive-Cateriana's commission or
    
    \=If((incentive-first.split)>60,(second.split-first.split)\*(1-first.ratio),"")+(incentive-first.split-If((incentive-first.split)>60,(second.split-first.split)\*first.ratio,"")-If((incentive-first.split)>60,(second.split-first.split)\*(1-first.ratio),""))\*second.ratio
    
    Thank you and Bye-bye!  
    Gerhard
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-863705)
    
52.  ![](https://secure.gravatar.com/avatar/f8f55e598a930ee2169d0a2d0ab178c8c8b79ad855dba54f8b2917896a59e4e3?s=64&d=mm&r=g) Pedro says:
    
    [December 3, 2014 at 2:38 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-864524)
    
    For Antonio commission:  
    IF(incentive>second.split;(incentive-second.split)\*second.ratio+35.000\*30%;IF(incentive>first.split;(incentive-first.split)\*30%;0))
    
    For Caterina commission:  
    incentive-Antonio commission
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-864524)
    
53.  ![](https://secure.gravatar.com/avatar/171c33099a641e0c3261fdc05659b37070af5b69454662a966c4f384152cfd4a?s=64&d=mm&r=g) Scott F says:
    
    [December 3, 2014 at 3:42 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-864559)
    
    If the incentive pool is $100,000, is Caterina's commission $69,500 and Antonio's $30,500? Those are the answers my equations listed below spit out.
    
    Caterina's commission  
    \=A2+(B2\*(A3-A2))+IF(A1>A3,((A1-A3)\*0.5), (0))
    
    Antonio's commission  
    \=0.3\*(A3-A2)+IF(A1>A3, ((A1-A3)\*0.5), (0))
    
    Not sure how to name cells yet so I just used the standard reference. Think these equations are right but I welcome anyone who may be willing to advise. Thanks!
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-864559)
    
54.  ![](https://secure.gravatar.com/avatar/a2ce73364d19179c6ea9c2faafdbc068646d29946dc41fd2fa77a0efe48ea2c6?s=64&d=mm&r=g) frank mccraw says:
    
    [December 13, 2014 at 6:05 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-873976)
    
    Catarina in cell B5
    
    \=IF(A1<A2,A1,IF(A1<A3,A2+(A1-A2)\*B2,A2+B2\*(A3-A2)+(A1-A3)\*B3))
    
    Antonia in cell B6
    
    A1-B5
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-873976)
    
55.  ![](https://secure.gravatar.com/avatar/42c276d9dfcb5e5d4bdbde6a59cdac00b29d191b108066a1c8b0166c85b25e9f?s=64&d=mm&r=g) [Yogesh Gupta](http://www.yogeshguptaonline.com/)
     says:
    
    [December 14, 2014 at 4:32 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874273)
    
    I will Calculate Antonio's commision and then remaining amount will be Catarina's commission
    
    Antonio's commision without use of If formula's is
    
    \=MAX(MIN(second.split-first.split,incentive-first.split),0)\*(1-first.ratio)+MAX(incentive-second.split,0)\*second.ratio
    
    Catarina's Commission is = incentive - Antonio's commision
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874273)
    
56.  ![](https://secure.gravatar.com/avatar/e7a8e1d407a55e75181a40d245fc96bdf1f5976c9da2c5695d188c438c8da0bd?s=64&d=mm&r=g) Khurrum Iqbal says:
    
    [December 14, 2014 at 9:24 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874441)
    
    € 25,001.00  
    € 25,000 70%  
    € 60,000 50%
    
    Caterina  
    Cathrine =IF(incentive=first.split,incentivesecond.split,(((incentive-first.split)\*second.ratio)+first.split),0)))
    
    Antonio  
    \=IF(AND(incentive>=first.split,incentivesecond.split,(incentive-first.split)\*(1-second.ratio),0))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874441)
    
57.  ![](https://secure.gravatar.com/avatar/bd7581ba9f9e519c807be040fc699b70ffbc7497e7d169b5a13ab0e2664fc164?s=64&d=mm&r=g) Abdul Rehman says:
    
    [December 14, 2014 at 10:13 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874470)
    
    \=IF(A1A2,A1<A3),A2+(A1-A2)\*A4,A2+(A3-A2)\*A4+(A1-A3)\*A5))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874470)
    
    *   ![](https://secure.gravatar.com/avatar/bd7581ba9f9e519c807be040fc699b70ffbc7497e7d169b5a13ab0e2664fc164?s=64&d=mm&r=g) Abdul Rehman says:
        
        [December 14, 2014 at 4:48 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874631)
        
        The above formula is for Catarina's commission
        
        [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874631)
        
58.  ![](https://secure.gravatar.com/avatar/e7a8e1d407a55e75181a40d245fc96bdf1f5976c9da2c5695d188c438c8da0bd?s=64&d=mm&r=g) Khurrum Iqbal says:
    
    [December 14, 2014 at 10:21 am](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874474)
    
    Cathrine:  
    \=IF(incentive=first.split,incentivesecond.split,(((incentive-first.split)\*second.ratio)+first.split),0)))
    
    Antonio:  
    \=IF(AND(incentive>=first.split,incentivesecond.split,(incentive-first.split)\*(1-second.ratio),0))
    
    Ignore first not displayed properly.
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874474)
    
59.  ![](https://secure.gravatar.com/avatar/de67e10d2152b8e3b2bec26e3aa9758030de4305d63efc36e6f7068e5dea7086?s=64&d=mm&r=g) Dale says:
    
    [December 14, 2014 at 9:34 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874753)
    
    By my calcs, If the Incentive pool was €70000  
    Catarina should receive €54500, Antonio should receive €15500  
    Catarina's formula is  
    \=IF(Incentive>second.split,  
    first.split+(((Incentive-first.split)-(Incentive-second.split))\*first.ratio)+((Incentive-second.split)\*second.ratio),  
    IF(Incentive>first.split,first.split+(((Incentive-first.split))\*first.ratio),  
    Incentive))  
    Antonio's formula is  
    \=IF(Incentive>second.split,  
    ((Incentive-first.split)-(Incentive-second.split))\*(1-first.ratio)+((Incentive-second.split)\*second.ratio),  
    IF(Incentive>first.split, ((Incentive-first.split))\*(1-first.ratio),  
    0))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-874753)
    
60.  ![](https://secure.gravatar.com/avatar/25a6186b0285531cf6acb99557cfd7fb69c8acc373aae8045ef2673b5dd0d719?s=64&d=mm&r=g) Julian G says:
    
    [December 15, 2014 at 6:39 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-875393)
    
    \=MAX((commission-second.amount)\*second.split,0)+MAX((MIN(commission,second.amount)-first.amount)\*(1-first.split),0)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-875393)
    
61.  ![](https://secure.gravatar.com/avatar/823723a288fb99f69a7f51d38a48b2b60ed896ce7d4fa75af1edbdb980546c4a?s=64&d=mm&r=g) Tadeus says:
    
    [January 9, 2015 at 7:58 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-891331)
    
    Here my answers:  
    for Catherine:  
    \=IF(Incentive>85000,(Incentive-85000)\*Second.Ratio+67000,IF(Incentive>25000,(Incentive-25000)\*First.Ratio+25000,Incentive))
    
    For Antonio:  
    \=IF(Incentive>85000,(Incentive-85000)\*Second.Ratio+18000,IF(Incentive>25000,(Incentive-25000)\*(100%-First.Ratio)+25000,Incentive))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-891331)
    
62.  ![](https://secure.gravatar.com/avatar/823723a288fb99f69a7f51d38a48b2b60ed896ce7d4fa75af1edbdb980546c4a?s=64&d=mm&r=g) Tadeus says:
    
    [January 9, 2015 at 8:05 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-891336)
    
    sorry I forget to change the formula for Antonio  
    here you are again:  
    \=IF(Incentive>85000,(Incentive-85000)\*Second.Ratio+18000,IF(Incentive>25000,(Incentive-25000)\*(100%-First.Ratio),0))
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-891336)
    
63.  ![](https://secure.gravatar.com/avatar/15733ff427445e709ce7d0187312c79e6b4132da1dd33528bc9c24f9598aeb9b?s=64&d=mm&r=g) Avnish Tiwari says:
    
    [November 9, 2016 at 4:41 pm](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-1335108)
    
    Hi Chandoo  
    \=IF(Incentive LTE 25000,Incentive,25000) +  
    \=IF(Incentive GT 60000, 35000\*70%, IF((Incentive-25000) GT 0,(A7-25000)\*70%,0)) +  
    \=IF(Incentive GT 60000,(A7-60000)\*50%,0)
    
    [Reply](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#comment-1335108)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/can-you-calculate-the-sales-commission-homework/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Open & Save files faster in Excel 2013 \[quick tip\]](https://chandoo.org/wp/open-save-files-faster-in-excel-2013/) | [Calculate Pi by throwing Frozen Hotdogs !](https://chandoo.org/wp/calculate-pi-by-throwing-frozen-hotdogs/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
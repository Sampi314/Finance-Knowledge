# Can you find that pattern? [Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/find-text-pattern

---

Can you find that pattern? \[Homework\]
=======================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 240 comments

  

Hi folks…

Are you ready for an Excel challenge?

Today, your job is very simple. Just find a pattern in a text and return corresponding value.

**Your Homework:**

In a range we have some resource types & their billing rates.

In another range, we have some descriptions. Each description contains a resource type somewhere inside it. We need to retrieve billing rate for each description by looking up which resource type is mentioned in it.

See this diagram:

![Can you find that pattern? - Excel formula homework](https://img.chandoo.org/hw/can-you-find-that-pattern-excel-homework.png)

**Download the data**

[Click here to download the data](https://img.chandoo.org/hw/can-you-find-the-pattern.xlsx)
 to write your formulas.

Notes:

*   The file contains 3 named ranges – resIDs, resTypes, resRates for resource IDs, types & rates in that order. You can use these to shorten your formulas.

**Post your answers:**

Go ahead and solve this. Then come back and post your formulas in comments. **[Click here to post your answer](http://chandoo.org/wp/2012/12/14/find-text-pattern/#respond)
.**

**Need clues?**

Read [wildcards in COUNTIF formula](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)
 page to get some clues.

So go ahead and post your answers. I am waiting…

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
| Written by Chandoo  <br>Tags: [array formulas](https://chandoo.org/wp/tag/array-formulas/)<br>, [challenge](https://chandoo.org/wp/tag/challenge/)<br>, [countif()](https://chandoo.org/wp/tag/countif/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [INDEX()](https://chandoo.org/wp/tag/index/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [patterns](https://chandoo.org/wp/tag/patterns/)<br>, [text processing](https://chandoo.org/wp/tag/text-processing/)<br>, [wildcards in excel](https://chandoo.org/wp/tag/wildcards-in-excel/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 240 Responses to “Can you find that pattern? \[Homework\]”

1.  ![](https://secure.gravatar.com/avatar/b8604c6f79c8db3f79e17c562e6f7cd888a268d59501100720b70a6c3046ee1f?s=64&d=mm&r=g) Vijay Sharma says:
    
    [December 14, 2012 at 8:23 am](https://chandoo.org/wp/find-text-pattern/#comment-345783)
    
    Not my formula but this will do the trick...
    
    \=LOOKUP(2^15,SEARCH(resTypes,B4),resRates)
    
    ~VijaySharma
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-345783)
    
    *   ![](https://secure.gravatar.com/avatar/ee5bcebe16818c3ce98a2bbc568e03997ee7cb900a65b28eeaa07b2adcc69c91?s=64&d=mm&r=g) Peter van Klinken says:
        
        [December 14, 2012 at 9:57 am](https://chandoo.org/wp/find-text-pattern/#comment-345919)
        
        Great solution! Trying to figure out how it works. Could you explain? especially the 2^15 part.
        
        Peter
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-345919)
        
        *   ![](https://secure.gravatar.com/avatar/ac1f0aa7233483e25901587bda7abe67c2b5131c710b421f87f92c788512f5e9?s=64&d=mm&r=g) Dmitry says:
            
            [December 14, 2012 at 10:17 am](https://chandoo.org/wp/find-text-pattern/#comment-345948)
            
            Seems like here might be an answer:  
            [http://www.youtube.com/watch?v=huDPpuOucF0](http://www.youtube.com/watch?v=huDPpuOucF0%C2%A0)
             
            
            [Reply](https://chandoo.org/wp/find-text-pattern/#comment-345948)
            
        *   ![](https://secure.gravatar.com/avatar/ca001eeabcda092dabada99dcebc945563a21c24797ad9e1c70ab25f4b3cd16a?s=64&d=mm&r=g) Irvine R says:
            
            [December 14, 2012 at 11:18 am](https://chandoo.org/wp/find-text-pattern/#comment-346016)
            
            The 2^15 is the lookup value and needs to be large enough to be greater then the length of the text in B4, since the search function will return #VALUE! for the search terms not matched and the position of the matched search term.
            
            Effectively, the lookup becomes =LOOKUP(2^15,{#VALUE!;#VALUE!;#VALUE!;9;#VALUE!;#VALUE!},resRates)
            
            [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346016)
            
            *   ![](https://secure.gravatar.com/avatar/333687c5a56dffddd1c9e392a2bc1c4a66efefccd216169f32cad58276a993df?s=64&d=mm&r=g) Greg says:
                
                [December 14, 2012 at 7:25 pm](https://chandoo.org/wp/find-text-pattern/#comment-346846)
                
                2^15 is an arbitrary number for this example.  The largest position that SEARCH returns in this example is 16, which can be used in the example.
                
                [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346846)
                
        *   ![](https://secure.gravatar.com/avatar/eb925eedebecb06f67116a479230bda5b270c59abafb40b8ca2f665e3f469920?s=64&d=mm&r=g) Bryan says:
            
            [December 14, 2012 at 6:49 pm](https://chandoo.org/wp/find-text-pattern/#comment-346805)
            
            This formula works unless you have a Resource Description of "FM Radio Station AM xxxxx2324" or anything combination before the resource type that matches a different resource type.  So in my example there is FM which is not the type in this description but the formula will still pick it up as the type and bring back a 75 instead of a 50.
            
            [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346805)
            
    *   ![](https://secure.gravatar.com/avatar/cde7529b28558dce2057f1ba5a0ca5f41c59d99c9ea4bf33d8b6b68f3d51693e?s=64&d=mm&r=g) Jon says:
        
        [December 14, 2012 at 10:11 am](https://chandoo.org/wp/find-text-pattern/#comment-345943)
        
        I love this one however it fails if some string appears in a word  
        I would add a trailing space (and leading ?).  
        \=LOOKUP(2^15;SEARCH( esTypes & " ";B4);resRates)  
         
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-345943)
        
        *   ![](https://secure.gravatar.com/avatar/180579deb2af12f557da480f315608d3b45a1190f72e595ed5600da6ce839fee?s=64&d=mm&r=g) Matt says:
            
            [December 14, 2012 at 12:20 pm](https://chandoo.org/wp/find-text-pattern/#comment-346077)
            
            Then you can use this one...  
            \=LOOKUP(2^15,SEARCH(resTypes & " xxx", B4 & " xxx"), resRates)
            
            [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346077)
            
            *   ![](https://secure.gravatar.com/avatar/6a34ec2dc66cc4288b3dc55c10b22905e2c3de672edf4b5e04da7969630cf41b?s=64&d=mm&r=g) Eric says:
                
                [December 14, 2012 at 12:54 pm](https://chandoo.org/wp/find-text-pattern/#comment-346116)
                
                That's close, I think.  But if there is a couple of research types like PM and PPM then you'd still get the wrong answer. 
                
                <code>=LOOKUP(2^15, SEARCH(" " & resTypes & " ", B4), resRates)</code>
                
                I think this'd take care of it.
                
                [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346116)
                
                *   ![](https://secure.gravatar.com/avatar/180579deb2af12f557da480f315608d3b45a1190f72e595ed5600da6ce839fee?s=64&d=mm&r=g) Matt says:
                    
                    [December 14, 2012 at 1:07 pm](https://chandoo.org/wp/find-text-pattern/#comment-346135)
                    
                    Almost 🙂  
                    \=LOOKUP(2^15,SEARCH(” ” & resTypes & ” xxx”, ” ” & B4 & ” xxx”), resRates)  
                     
                    
                *   ![](https://secure.gravatar.com/avatar/180579deb2af12f557da480f315608d3b45a1190f72e595ed5600da6ce839fee?s=64&d=mm&r=g) Matt says:
                    
                    [December 14, 2012 at 1:10 pm](https://chandoo.org/wp/find-text-pattern/#comment-346139)
                    
                    Uuups, no you are right...
                    
    *   ![](https://secure.gravatar.com/avatar/9fce29f130e9609327b1f50936c6ac121ace3cb073961079adda2ca9dbb9777d?s=64&d=mm&r=g) Shakeel says:
        
        [December 15, 2012 at 6:48 am](https://chandoo.org/wp/find-text-pattern/#comment-347632)
        
        in fact the best & right answer
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347632)
        
    *   ![](https://secure.gravatar.com/avatar/03a29183430628bb417c5485494e2e3c4d44a06bde37e084d29ae14eacf8f17a?s=64&d=mm&r=g) GB says:
        
        [December 17, 2012 at 10:22 am](https://chandoo.org/wp/find-text-pattern/#comment-350840)
        
        array formula
        
        \=VLOOKUP(INDEX($H$4:$H$9,MAX(IF(ISERROR(FIND($H$4:$H$9,B4)),-1,1)\*(ROW($H$4:$H$9)-ROW($H$4)+1))),$H$4:$I$9,2,FALSE)
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-350840)
        
    *   ![](https://secure.gravatar.com/avatar/53c1e9a2880bb5fabfc2adb55e1ba7be442aa03a06736e20dc28a5be1631981b?s=64&d=mm&r=g) Emanuel Clark says:
        
        [March 27, 2018 at 4:20 am](https://chandoo.org/wp/find-text-pattern/#comment-1541772)
        
        Love this formula, agree with Irvine, 2^15 can be replaced with any number as long as it is similar or has greater length than the text on column B.
        
        with addition of index and match it can help you find the correct billing rate.
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1541772)
        
    *   ![](https://secure.gravatar.com/avatar/c53550c434a2f457e608346f9a43d17909cdf2ac44f60f85f0b7351b65314309?s=64&d=mm&r=g) Sushma says:
        
        [December 6, 2023 at 5:41 am](https://chandoo.org/wp/find-text-pattern/#comment-2155601)
        
        It is working for LOOKUP, But if I am trying with VLOOKUP it is not working. Any idea why?
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2155601)
        
    *   ![](https://secure.gravatar.com/avatar/9871ebda2f155975df09a0e3859ab97316645ef20decfb2282509cb17526a014?s=64&d=mm&r=g) Ali says:
        
        [March 17, 2024 at 9:47 am](https://chandoo.org/wp/find-text-pattern/#comment-2195923)
        
        This works too:  
        \=LOOKUP(1000,SEARCH(resTypes,B4),resRates)
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2195923)
        
    *   ![](https://secure.gravatar.com/avatar/34e2a070604e87f1abe0fa34265ea41707bc2edd4ff6b5839efc66ebaa1936bb?s=64&d=mm&r=g) Hasan says:
        
        [November 10, 2024 at 6:39 pm](https://chandoo.org/wp/find-text-pattern/#comment-2306457)
        
        First I used replace function to free resource type with not required text and value, then used v look formula to get the billing rate Resource Description Billing Rate Correct Answers  
        Nothing CM xxxx4607 CM 120 120  
        Few things CXO xxxx5633 CXO 250 250  
        Lots of things RM xxxxxx6378 RM 150 150  
        Something AM xxxx9132 AM 50 50  
        One thing AM xxx5299 AM 50 50  
        Few things PM xxxxx5502 PM 60 60  
        Nothing AM xxxx6096 AM 50 50  
        Another thing RM xxx7837 RM 150 150  
        Something AM xxxxx6719 AM 50 50  
        One thing FM xxx1817 FM 75 75  
        One thing CXO xxxxx2823 CXO 250 250  
        Nothing AM xxx5155 AM 50 50  
        Another thing FM xxxx3012 FM 75 75  
        Something AM xxx2124 AM 50 50  
        Nothing CM xxxx9363 CM 120 120  
        One thing CM xxxx2104 CM 120 120  
        Nothing FM xxxxx1386 FM 75 75  
        Another thing PM xxx9637 PM 60 60  
        Few things PM xxxx8157 PM 60 60  
        One thing PM xxxxxx9699 PM 60 60  
        Few things RM xxxxxx8637 RM 150 150  
        Lots of things RM xxxxxx3863 RM 150 150  
        Something CM xxxxx4671 CM 120 120  
        One thing CXO xxxx2450 CXO 250 250  
        Nothing PM xxxx1759 PM 60 60  
        Something RM xxxx8382 RM 150 150  
        Something PM xxxxxx8054 PM 60 60  
        Another thing CXO xxxx1293 CXO 250 250  
        Something RM xxx4545 RM 150 150  
        Something RM xxxxxx7317 RM 150 150
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2306457)
        
    *   ![](https://secure.gravatar.com/avatar/6fab70ce6d08fb077b9b9dfcbf7ac75ca1ee43e28fe900808584b18a8d544cfa?s=64&d=mm&r=g) Gabe says:
        
        [February 24, 2025 at 4:44 pm](https://chandoo.org/wp/find-text-pattern/#comment-2366600)
        
        \=XLOOKUP(TRUE, ISNUMBER(SEARCH(resTypes, B4)), resRates, "Not Found")
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2366600)
        
2.  ![](https://secure.gravatar.com/avatar/71ffaabf1033276a0b99660eb228c2de7e920926aa959ce3ea97e550d66531d8?s=64&d=mm&r=g) GFC says:
    
    [December 14, 2012 at 9:35 am](https://chandoo.org/wp/find-text-pattern/#comment-345881)
    
    \=RECHERCHEV(SUPPRESPACE(DROITE(GAUCHE(B4;TROUVE("xx";B4)-2);3));$H$4:$I$9;2;0)  
    
    \=Vlookup(trim(right(left(b4;find("xx";b4)-2);3));$h$4:$i$9;2;0)    
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-345881)
    
    *   ![](https://secure.gravatar.com/avatar/4ba3c5350e3131b6f74c701e8ae38eb93903f4eddcf9ef3afbb7eb3988288efa?s=64&d=mm&r=g) Bitoubi says:
        
        [June 19, 2014 at 3:46 pm](https://chandoo.org/wp/find-text-pattern/#comment-558790)
        
        cant replace right(left()) with a stxt()
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-558790)
        
3.  ![](https://secure.gravatar.com/avatar/0d7263112584639382213490bb53b2872e51f44757da9a23c695421f48971b45?s=64&d=mm&r=g) James lilg says:
    
    [December 14, 2012 at 9:52 am](https://chandoo.org/wp/find-text-pattern/#comment-345908)
    
     Formula is too long but it works  
    \=VLOOKUP(MID(B4,IF(ISERROR(FIND("ngs",B4)),FIND("ng",B4)+3,FIND("ngs",B4)+4),2)&"\*",$H$4:$I$9,2,0)
    
    ~lilg  
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-345908)
    
4.  ![](https://secure.gravatar.com/avatar/ac1f0aa7233483e25901587bda7abe67c2b5131c710b421f87f92c788512f5e9?s=64&d=mm&r=g) Dmitry says:
    
    [December 14, 2012 at 10:16 am](https://chandoo.org/wp/find-text-pattern/#comment-345947)
    
    What i've figured out is:  
     {=INDEX(resRates;SUM(NOT(ISERROR(SEARCH(resTypes;B4;1)))\*ROW(resTypes))-3)}
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-345947)
    
5.  ![](https://secure.gravatar.com/avatar/8539757ca3a7f5fff54c20a4db4439797329408035caf3d035623e2bccfb2122?s=64&d=mm&r=g) Sebastien says:
    
    [December 14, 2012 at 10:31 am](https://chandoo.org/wp/find-text-pattern/#comment-345962)
    
    Here is my solution (array formula):  
    INDEX(resRates,MATCH(0,FIND(resTypes,B4,1)\*($J$4:$J$9),0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-345962)
    
6.  ![](https://secure.gravatar.com/avatar/3d8474ea2081f8d11f211ae103f3da747eca65ee6b1c306f28147e8de6b2fbe4?s=64&d=mm&r=g) Chantty says:
    
    [December 14, 2012 at 11:53 am](https://chandoo.org/wp/find-text-pattern/#comment-346047)
    
    Hi,
    
    I have used countif & If conditions, Please do let me know if we have any other better way...
    
    IF(COUNTIF(B4,"\*"&$H$4&"\*")<>0,$I$4,IF(COUNTIF(B4,"\*"&$H$5&"\*")<>0,$I$5,IF(COUNTIF(B4,"\*"&$H$6&"\*")<>0,$I$6,IF(COUNTIF(B4,"\*"&$H$7&"\*")<>0,$I$7,IF(COUNTIF(B4,"\*"&$H$8&"\*")<>0,$I$8,IF(COUNTIF(B4,"\*"&$H$9&"\*")<>0,$I$9,"Check"))))))
    
    Looking forward to learn a lot from here.....
    
    Cheers...
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346047)
    
    *   ![](https://secure.gravatar.com/avatar/0a7e7527cc17f66e66c71e3d4be572deed308c07a0d64467e164176b65261014?s=64&d=mm&r=g) Ramanan says:
        
        [December 14, 2012 at 1:03 pm](https://chandoo.org/wp/find-text-pattern/#comment-346130)
        
        1\. INDEX(resRates,MATCH(1,--(ISNUMBER(FIND(resTypes,B4))),0))  
        2. INDEX(resRates,SMALL(IF(1\*(ISNUMBER(FIND(resTypes,B4))),ROW(resTypes)-ROW($H$4)+1),1))
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346130)
        
        *   ![](https://secure.gravatar.com/avatar/0a7e7527cc17f66e66c71e3d4be572deed308c07a0d64467e164176b65261014?s=64&d=mm&r=g) Ramanan says:
            
            [December 14, 2012 at 1:03 pm](https://chandoo.org/wp/find-text-pattern/#comment-346132)
            
            Both required Ctrl+shift+Enter
            
            [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346132)
            
7.  ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
    
    [December 14, 2012 at 1:25 pm](https://chandoo.org/wp/find-text-pattern/#comment-346165)
    
    I like Vijay's best so far, but this is what I first came up with. Maybe I just love using SUMPRODUCT too much....
    
    \=SUMPRODUCT(ISNUMBER(SEARCH(resTypes,B4))\*(resRates))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346165)
    
    *   ![](https://secure.gravatar.com/avatar/38bfd714e0878c4c77c2836b8fd2ee41b72c25d1fbb100eb810d15192a39505d?s=64&d=mm&r=g) Kuldeep says:
        
        [December 14, 2012 at 4:37 pm](https://chandoo.org/wp/find-text-pattern/#comment-346542)
        
        Yes Luke You Do Love Very much of Sumproduct
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346542)
        
        *   ![](https://secure.gravatar.com/avatar/c443a69573a9ceef6d77ac4e33843313d2daa7ec6735d2750a0591e54ecd8cef?s=64&d=mm&r=g) Harish says:
            
            [December 14, 2012 at 6:37 pm](https://chandoo.org/wp/find-text-pattern/#comment-346792)
            
            sumproduct is useful function which was developed by excel user like us...and idea apply by MS in excel 2007 as sumifs......:D
            
            [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346792)
            
8.  ![](https://secure.gravatar.com/avatar/bcfe3a3636829e0913ae564f77467378affe1e80e300d172e248f979f516b48d?s=64&d=mm&r=g) Till Kta says:
    
    [December 14, 2012 at 2:47 pm](https://chandoo.org/wp/find-text-pattern/#comment-346286)
    
    GFC variation : 
    
    \=RECHERCHEV(SUBSTITUE(DROITE(GAUCHE(B4;CHERCHE("xx";B4)-2);3);" ";"");$H$3:$I$9;2;0)  
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346286)
    
9.  ![](https://secure.gravatar.com/avatar/c3c6e737e9f32941c47496250e22c873613e1726aa8882d33524b019c3d4971e?s=64&d=mm&r=g) Fernando says:
    
    [December 14, 2012 at 2:56 pm](https://chandoo.org/wp/find-text-pattern/#comment-346293)
    
    array formula  
    \=SUM((IFERROR(SEARCH(resTypes,b4),0)<>0)\*resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346293)
    
10.  ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) [Sajan](http://chandoo.org/forums/profile/sthomas)
     says:
    
    [December 14, 2012 at 3:53 pm](https://chandoo.org/wp/find-text-pattern/#comment-346388)
    
    I too like Vijay's LOOKUP formula since it very short and to the point!  
    (I would wrap the restypes in a space on either side to avoid any false positives.)
    
    Here is what I came up with:  
    \=INDEX(resRates, MATCH(99,FIND(" " & resTypes  & " ", B4)))  
    Ctrl + Shift + Enter
    
    The idea is similar to a few of the formulas already posted.
    
    Cheers,  
    Sajan.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346388)
    
11.  ![](https://secure.gravatar.com/avatar/18bebb259a5e0b8dfbdfe8e49715e6846819865c3d39b4f2229e0eddfec87fc7?s=64&d=mm&r=g) Nick M. says:
    
    [December 14, 2012 at 5:09 pm](https://chandoo.org/wp/find-text-pattern/#comment-346639)
    
    Looks like I'm the only one that went the vba route with this one.  I think I got a good handle on formulas since been using them since forever, so always look for ways to improve my vba skills.  Well anyways, here it is.   
    [https://www.dropbox.com/s/qipm1hoczmvrxgv/can-you-find-the-pattern%20NMone.xlsm](https://www.dropbox.com/s/qipm1hoczmvrxgv/can-you-find-the-pattern%20NMone.xlsm)
      
       
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346639)
    
12.  ![](https://secure.gravatar.com/avatar/5c75174189bf4c1b6d768e247cd2ba6e4cd3aafc8848f31f3cdf2e21257d7496?s=64&d=mm&r=g) Matthieu says:
    
    [December 14, 2012 at 6:09 pm](https://chandoo.org/wp/find-text-pattern/#comment-346752)
    
    \=OFFSET(resRates,MAX((IFERROR(FIND(resTypes,B4,1),0)>1)\*resIDs)-1,0,1,1)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346752)
    
13.  ![](https://secure.gravatar.com/avatar/5c75174189bf4c1b6d768e247cd2ba6e4cd3aafc8848f31f3cdf2e21257d7496?s=64&d=mm&r=g) Matthieu says:
    
    [December 14, 2012 at 6:14 pm](https://chandoo.org/wp/find-text-pattern/#comment-346761)
    
    \=OFFSET(resRates,MAX((IFERROR(FIND(resTypes,B4,1),0)>1)\*resIDs)-1,0,1,1)  
    Ctrl+Shift+Enter of course.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346761)
    
14.  ![](https://secure.gravatar.com/avatar/c443a69573a9ceef6d77ac4e33843313d2daa7ec6735d2750a0591e54ecd8cef?s=64&d=mm&r=g) Harish says:
    
    [December 14, 2012 at 6:30 pm](https://chandoo.org/wp/find-text-pattern/#comment-346784)
    
    \=VLOOKUP(TRIM(CLEAN(RIGHT(MID(B4,1,FIND("x",B4)-1),4))),$H$3:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346784)
    
15.  ![](https://secure.gravatar.com/avatar/dfa49a470826f91c1f8655192a5e503003326ffe7444d31ba90c7a5216217b20?s=64&d=mm&r=g) L Maddy says:
    
    [December 14, 2012 at 6:45 pm](https://chandoo.org/wp/find-text-pattern/#comment-346799)
    
    \=IF(NOT(ISERROR(SEARCH($H$4,B4))),$I$4,IF(NOT(ISERROR(SEARCH($H$5,B4))),$I$5,IF(NOT(ISERROR(SEARCH($H$6,B4))),$I$6,IF(NOT(ISERROR(SEARCH($H$7,B4))),$I$7,IF(NOT(ISERROR(SEARCH($H$8,B4))),$I$8,IF(NOT(ISERROR(SEARCH($H$9,B4))),$I$9))))))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346799)
    
16.  ![](https://secure.gravatar.com/avatar/86ede4a858c33a9e947b20cc95f910d0ab43316206ccc60dcd88843abe0532fa?s=64&d=mm&r=g) Colin says:
    
    [December 14, 2012 at 7:04 pm](https://chandoo.org/wp/find-text-pattern/#comment-346826)
    
    \=INDEX(resRates,MATCH(TRIM(LEFT(RIGHT(B4,LEN(B4)-FIND(" x",B4)+4),3)),resTypes,0),1)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346826)
    
17.  ![](https://secure.gravatar.com/avatar/6e4efb56494c2f9e9465ce07f96ec4810c8ec7f537a4a716a51ba905e20c03b9?s=64&d=mm&r=g) Harlan says:
    
    [December 14, 2012 at 7:11 pm](https://chandoo.org/wp/find-text-pattern/#comment-346830)
    
    \=SUMPRODUCT(COUNTIF(B4,"\*"&resTypes&"\*")\*resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346830)
    
18.  ![](https://secure.gravatar.com/avatar/4e52b05d900178940f118b887ac2300c8bd1de1024e2d024ce14db7558ecc7ff?s=64&d=mm&r=g) shaji says:
    
    [December 14, 2012 at 7:17 pm](https://chandoo.org/wp/find-text-pattern/#comment-346837)
    
       
    Assign a code relevant to match with resource type in column A by filtering text contain resource type......then use simple forlmula.... =VLOOKUP(A4,$H$4:$I$9,2,FALSE) ...  
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346837)
    
19.  ![](https://secure.gravatar.com/avatar/1105fcdac5175213f64b458be36b70fa751dfc4ee2e2c94f2c4c5685930359cf?s=64&d=mm&r=g) Ananya Jena says:
    
    [December 14, 2012 at 7:25 pm](https://chandoo.org/wp/find-text-pattern/#comment-346845)
    
    \=VLOOKUP(SUBSTITUTE(MID(B4,FIND("x",B4,1)-4,3)," ",""),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346845)
    
    *   ![](https://secure.gravatar.com/avatar/3494bc4abb65576408bb4eae9d3e9ee988ca19bdc6e8b56cc82c89ee3a6890ad?s=64&d=mm&r=g) Samtheman says:
        
        [December 14, 2012 at 9:53 pm](https://chandoo.org/wp/find-text-pattern/#comment-347107)
        
        Awesome nonfancy formula
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347107)
        
20.  ![](https://secure.gravatar.com/avatar/c04f90b2bd3fd8547eb66c3c08fb8a27264b7e2f36df7caf7401767ddfd4cab5?s=64&d=mm&r=g) Detlef says:
    
    [December 14, 2012 at 7:33 pm](https://chandoo.org/wp/find-text-pattern/#comment-346860)
    
    Two solutions.
    
    \=LOOKUP(2,1/COUNTIF(B4,"\*"&resTypes&"\*"),resRates)  
    \=LOOKUP(9^9,SEARCH(resTypes,B4),resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346860)
    
    *   ![](https://secure.gravatar.com/avatar/df6cb0e6ac22c2f18e1d98866f6d870aeecbb9567a9386e337f5e4273e1d56d6?s=64&d=mm&r=g) cypher says:
        
        [June 17, 2017 at 6:47 pm](https://chandoo.org/wp/find-text-pattern/#comment-1463596)
        
        \=VLOOKUP(TRIM(MID(B4,FIND("x",B4,1)-4,3)),$H$4:$I$9,2,FALSE)
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1463596)
        
21.  ![](https://secure.gravatar.com/avatar/b03ce1ef57cbfc8c985f6f281c63e97d5c9e5bdb12f80933d6084be48c6ccb14?s=64&d=mm&r=g) Squiggler says:
    
    [December 14, 2012 at 7:43 pm](https://chandoo.org/wp/find-text-pattern/#comment-346885)
    
    \=SUMPRODUCT(1-ISERROR(FIND(resTypes,B4)),resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346885)
    
    *   ![](https://secure.gravatar.com/avatar/96c39114d12a5d6ac91e307c7abbbbb61afa200033ad1457dfae5cedb20f50e0?s=64&d=mm&r=g) James says:
        
        [December 14, 2012 at 9:22 pm](https://chandoo.org/wp/find-text-pattern/#comment-347076)
        
        Good answer..elegant solution. So, by using the Sumproduct function, the Find function can handle an array of values that it normally could not do  outside of the Sumproduct function???  Thanks for the post.
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347076)
        
22.  ![](https://secure.gravatar.com/avatar/da5df737f6337d5256ec10c126b5859dd5d67de2337128f859b3de89b57e1edc?s=64&d=mm&r=g) Nicholas says:
    
    [December 14, 2012 at 7:57 pm](https://chandoo.org/wp/find-text-pattern/#comment-346896)
    
    I couldn't figure out how to do it without a "helper" column, (I kept running into errors when I tried to nest VLOOKUP. So I just created a nested IF formula in the E column to tell me the resource's ID:  
    \=IF(ISNUMBER(FIND("AM",B4)),1,IF(ISNUMBER(FIND("PM",B4)),2,IF . . . etc.  
    Then, I just used a simple VLOOKUP with a reference to the ID in column E:  
    \=VLOOKUP(E4,$G$4:$I$9,3)  
    Not the most elegant solution. I'm looking forward reading the awesome that all of you used to solve this.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346896)
    
23.  ![](https://secure.gravatar.com/avatar/26d3c2c67e3447e9de73b775e243a6d98ea96237587a8d9044ba50874639721f?s=64&d=mm&r=g) Matt says:
    
    [December 14, 2012 at 8:18 pm](https://chandoo.org/wp/find-text-pattern/#comment-346922)
    
    \=SUMPRODUCT(--(TRIM(MID(B4,FIND("x",B4)-4,3))=(resTypes)),resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346922)
    
24.  ![](https://secure.gravatar.com/avatar/4051d77e302e5b9bef5f646a88044a7df166d8b768b34a3e3928547d36785f72?s=64&d=mm&r=g) D Blakewood says:
    
    [December 14, 2012 at 8:34 pm](https://chandoo.org/wp/find-text-pattern/#comment-346981)
    
    Similar to others looking left of x's     
    \=VLOOKUP((TRIM(MID(B4,TRIM(FIND("x",B4,1)-4),3))),$h$4:$i$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-346981)
    
25.  ![](https://secure.gravatar.com/avatar/d349aca6f51a0592fc347ff2908f63d627697c751ea7651c3c3f8103ac0bf050?s=64&d=mm&r=g) Tony Strong says:
    
    [December 14, 2012 at 9:07 pm](https://chandoo.org/wp/find-text-pattern/#comment-347044)
    
    \=IF(COUNTIF(B4,"\*CM\*")=1,VLOOKUP(4,RANGE1,3,FALSE),(IF(COUNTIF(B4,"\*CXO\*")=1,VLOOKUP(6,RANGE1,3,FALSE),(IF(COUNTIF(B4,"\*RM\*")=1,VLOOKUP(5,RANGE1,3,FALSE),(IF(COUNTIF(B4,"\*AM\*")=1,VLOOKUP(1,RANGE1,3,FALSE),(IF(COUNTIF(B4,"\*PM\*")=1,VLOOKUP(2,RANGE1,3,FALSE),(IF(COUNTIF(B4,"\*FM\*")=1,VLOOKUP(3,RANGE1,3,FALSE))))))))))))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347044)
    
26.  ![](https://secure.gravatar.com/avatar/8b3482ca548117c8d7dd182ba621a2152d8fb0a1afc638e95778a35f9e5ef369?s=64&d=mm&r=g) peejay says:
    
    [December 14, 2012 at 9:22 pm](https://chandoo.org/wp/find-text-pattern/#comment-347079)
    
    very elegant!
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347079)
    
27.  ![](https://secure.gravatar.com/avatar/23cc68b9d63a8e9f8e5bd0f2373f24af91830cd2d2844c4b6ba01f5294aa218b?s=64&d=mm&r=g) Steve says:
    
    [December 14, 2012 at 9:41 pm](https://chandoo.org/wp/find-text-pattern/#comment-347094)
    
    Haha, far from pretty, far from elegant, and FAR from dynamic, but it works:  
    \=IF(NOT(ISERROR(FIND($H$4,$B4,1))),$I$4,IF(NOT(ISERROR(FIND($H$5,$B4,1))),$I$5,IF(NOT(ISERROR(FIND($H$6,$B4,1))),$I$6,IF(NOT(ISERROR(FIND($H$7,$B4,1))),$I$7,IF(NOT(ISERROR(FIND($H$8,$B4,1))),$I$8,IF(NOT(ISERROR(FIND($H$9,$B4,1))),$I$9,"N/A"))))))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347094)
    
28.  ![](https://secure.gravatar.com/avatar/252cc9a88bef15d679051c27c0b94dbb0220c9685868d87144e12edaafe553d7?s=64&d=mm&r=g) Brian says:
    
    [December 14, 2012 at 10:05 pm](https://chandoo.org/wp/find-text-pattern/#comment-347118)
    
    Man, all of you guys' other answers are quite impressive.  Mine I thought was pretty simple, yet works perfectly.  Let me know what you think...
    
    \=IFERROR( INDEX( resRates, MATCH( MID( B4, (FIND( "M", B4) -1), 2), resTypes, 0), 1), 250) 
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347118)
    
29.  ![](https://secure.gravatar.com/avatar/1f81d59df75bc9669e59d0009a23b1d290806ca68868e56e42e6b07b48821043?s=64&d=mm&r=g) Walter says:
    
    [December 14, 2012 at 11:11 pm](https://chandoo.org/wp/find-text-pattern/#comment-347183)
    
    Took two approaches  
    1\. created a separate table setting the "Resource Type" than using that table for VLOOKUP reference
    
    TRIM(CLEAN(MID(B4,FIND("x",B4)-4,3)))
    
            followed by
    
    IFERROR(VLOOKUP(L4,rate,2,FALSE),"")
    
       
    OR....  
    2\. A singular VLOOKUP combining efforts:
    
    \=IFERROR(VLOOKUP((TRIM(CLEAN(MID(B4,FIND("x",B4)-4,3)))),rate,2,FALSE),"")  
       
    Thank you that was fun.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347183)
    
30.  ![](https://secure.gravatar.com/avatar/8dbfc4f4953cd6797f28e6403c70dc7c2ca14973f47bcc53c9d3118bc44e5663?s=64&d=mm&r=g) Michael Pennington says:
    
    [December 14, 2012 at 11:31 pm](https://chandoo.org/wp/find-text-pattern/#comment-347205)
    
    \=SUM(resRates\*COUNTIF(B4,"\*"&resTypes&"\*"))
    
    Array entered 
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347205)
    
    *   ![](https://secure.gravatar.com/avatar/d719865c251ecd8c04d9ca78714934c0b5cbdefcf68951311ae64cd0ca18db9d?s=64&d=mm&r=g) Somak Roy Choudhury says:
        
        [December 15, 2012 at 1:01 am](https://chandoo.org/wp/find-text-pattern/#comment-347299)
        
        WOOOOW!!!!
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347299)
        
    *   ![](https://secure.gravatar.com/avatar/1673083cef631283046773d4a61e0cd938f020e2cba6a0fdd0aa7004604c560d?s=64&d=mm&r=g) AJ says:
        
        [December 16, 2012 at 9:05 am](https://chandoo.org/wp/find-text-pattern/#comment-349362)
        
        Mike,
        
        LOVE IT, LOVE IT,,simplicity
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-349362)
        
    *   ![](https://secure.gravatar.com/avatar/d349aca6f51a0592fc347ff2908f63d627697c751ea7651c3c3f8103ac0bf050?s=64&d=mm&r=g) Tony Strong says:
        
        [December 17, 2012 at 1:25 pm](https://chandoo.org/wp/find-text-pattern/#comment-351004)
        
        Looks simples, but I get zero for value when I plug the formula into cell C4 and down. Anyone else has that problem?
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-351004)
        
    *   ![](https://secure.gravatar.com/avatar/5a2752a18062d8735f1f7ae2b72982d0a4202574727eca9e4dc1308c001c0279?s=64&d=mm&r=g) Mayur Naik says:
        
        [December 19, 2012 at 12:11 pm](https://chandoo.org/wp/find-text-pattern/#comment-353722)
        
        Even I am getting Zero when i plug the same formula in C4.  
        Can you assist? 
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-353722)
        
    *   ![](https://secure.gravatar.com/avatar/db7ede23c655f2ba4dd63b04879d87bc5352c8ea247ef7db9a21b438e14ae31b?s=64&d=mm&r=g) subburaj says:
        
        [August 1, 2014 at 6:11 pm](https://chandoo.org/wp/find-text-pattern/#comment-585028)
        
        Please explain this formula...mainly about array
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-585028)
        
31.  ![](https://secure.gravatar.com/avatar/d719865c251ecd8c04d9ca78714934c0b5cbdefcf68951311ae64cd0ca18db9d?s=64&d=mm&r=g) Somak Roy Choudhury says:
    
    [December 15, 2012 at 12:55 am](https://chandoo.org/wp/find-text-pattern/#comment-347290)
    
    I exploited the commonality of the resource desc field values, and then did a little bit trial and error... with "things" and "thing" there are some offshoot of number of characters, fortunately you have spacebar in between thing/things and xxx... thus trim worked.
    
      =VLOOKUP(TRIM(MID(B4,FIND("thing",B4,1)+LEN("thing")+1,FIND("x",B4,1)-FIND("thing",B4,1)-LEN("thing")-2)),$H$3:$I$9,2,FALSE)
    
    Thanks, Somak  
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347290)
    
32.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [December 15, 2012 at 1:21 am](https://chandoo.org/wp/find-text-pattern/#comment-347312)
    
    Excellent answers everyone... Here is my solution.
    
    {=INDEX(resRates,MAX(COUNTIF(B4,"\*"&resTypes&"\*")\*(resIDs)))}
    
    [Solution file](http://img.chandoo.org/hw/can-you-find-the-pattern-sol.xlsx)
    .
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347312)
    
    *   ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
         says:
        
        [December 15, 2012 at 6:20 am](https://chandoo.org/wp/find-text-pattern/#comment-347600)
        
        Why not just this array-entered formula **without** the INDEX part?
        
        \=MAX(COUNTIF(B4,"\*"&resTypes&"\*")\*resRates)
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347600)
        
        *   ![](https://secure.gravatar.com/avatar/61a1f728f50c2d3cc2c41cc61bd6955d5d8694ab70b5994ec696e4271948c127?s=64&d=mm&r=g) Wainers says:
            
            [December 21, 2012 at 5:40 pm](https://chandoo.org/wp/find-text-pattern/#comment-356896)
            
            Really good suggestion, Rick, but I think it only works if all array elements are numeric. If result is non-numeric then INDEX or something similar will be needed.
            
            [Reply](https://chandoo.org/wp/find-text-pattern/#comment-356896)
            
    *   ![](https://secure.gravatar.com/avatar/f102f4b56ae94646daa1ecd043f488815131c0f1d31df5f9473df5a62fdf0c58?s=64&d=mm&r=g) vinoth david says:
        
        [January 7, 2013 at 10:15 am](https://chandoo.org/wp/find-text-pattern/#comment-382250)
        
        I got answer...  
           
        {=VLOOKUP("\*CM\*",H4:I9,2,0)}
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-382250)
        
    *   ![](https://secure.gravatar.com/avatar/b926e2c9a7bc01e2e4f795cb6a7c6e646a8a11e118a6232d25b757c2fc1b32c7?s=64&d=mm&r=g) Gabriel says:
        
        [January 30, 2013 at 9:53 am](https://chandoo.org/wp/find-text-pattern/#comment-410009)
        
        If there is no match the result is wrong (for example: Description "Few things xxxx5633", gives the answer: 50  
        There is no AF In this description.  
        That because we get a zero vector to maximize.
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-410009)
        
33.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) Afzal S says:
    
    [December 15, 2012 at 5:16 am](https://chandoo.org/wp/find-text-pattern/#comment-347520)
    
    \=IF(COUNTIF(B4,"\*M\*"),VLOOKUP(MID(B4,FIND("M",B4)-1,2),$H$4:$I$8,2,0),$I$9)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347520)
    
34.  ![](https://secure.gravatar.com/avatar/be0942581ecf6840ea793380b8ea9cc3b0c55d1890674298d87ad1ac87d70b0c?s=64&d=mm&r=g) shrivallabha says:
    
    [December 15, 2012 at 5:42 am](https://chandoo.org/wp/find-text-pattern/#comment-347557)
    
    There was a similar case on Chandoo forum.  
       
    Here it is:  
    [http://chandoo.org/forums/topic/search-for-a-word-string-and-return-that-string-if-found](http://chandoo.org/forums/topic/search-for-a-word-string-and-return-that-string-if-found)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347557)
    
35.  ![](https://secure.gravatar.com/avatar/01c2cda8d6a968500797a59ca7f186d10dab5bbff529058e976af82579c1cf7b?s=64&d=mm&r=g) [Ravinder Negi](http://yahoo.com/)
     says:
    
    [December 15, 2012 at 6:50 am](https://chandoo.org/wp/find-text-pattern/#comment-347635)
    
    \=INDEX($H$4:$I$9,MATCH(MID(SUBSTITUTE(B5," ","@",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))-1),SEARCH("@",SUBSTITUTE(B5," ","@",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))-1))+1,SEARCH(" ",SUBSTITUTE(B5," ","@",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))-1),SEARCH("@",SUBSTITUTE(B5," ","@",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))-1)))-SEARCH("@",SUBSTITUTE(B5," ","@",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))-1))-1),resTypes,0),2)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347635)
    
36.  ![](https://secure.gravatar.com/avatar/64f3ca9031d8d6d04048ec2f41499646f58129752d4e1e3646103e8684042a97?s=64&d=mm&r=g) zur says:
    
    [December 15, 2012 at 7:07 am](https://chandoo.org/wp/find-text-pattern/#comment-347655)
    
    SUMP RODUCT IS SIMPLEST
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347655)
    
37.  ![](https://secure.gravatar.com/avatar/9bea90e2b3088a5cb40cd361c320790b5feff298a66b4736806902213bdd12c1?s=64&d=mm&r=g) GPCHV Dutt says:
    
    [December 15, 2012 at 7:19 am](https://chandoo.org/wp/find-text-pattern/#comment-347669)
    
    HI  
    I have taken Combination of Left, Right,Find & Trim with VLookup  
       
    \=VLOOKUP(TRIM(RIGHT(LEFT(B4,FIND(" x",B4)-1),3)),$H$4:$I$9,2,0)  
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347669)
    
38.  ![](https://secure.gravatar.com/avatar/9fce29f130e9609327b1f50936c6ac121ace3cb073961079adda2ca9dbb9777d?s=64&d=mm&r=g) Shakeel says:
    
    [December 15, 2012 at 7:25 am](https://chandoo.org/wp/find-text-pattern/#comment-347674)
    
    i am totally agree with Vijay Shrama solution. Here is i am explaining the trick
    
    \=LOOKUP(16,SEARCH(resTypes,B4),resRates)
    
    The text length of starting CM,AM etc is maximum 16, so this formula works also by putting 16. Any how if you not now the length than the best maximum digit should be enter.
    
    Dear Chandoo
    
    you are working really awesome, i am in very initial stage. i like your tricks. I started Excel about 8 months ago. From your blog and Mr, Excel is fun i have learned a lot.
    
    also i request you if you will guide me how can i improve my self.  
    Thanks & Regards  
    Muhammad Shakeel
    
    is the simple and best.......
    
    **Description**  
    **LEN**
    
    Nothing C  
    9
    
    Few things P  
    12
    
    Lots of things A  
    16
    
    Something P  
    11
    
    One thing A  
    11
    
    Another thing C  
    15
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347674)
    
    *   ![](https://secure.gravatar.com/avatar/9fce29f130e9609327b1f50936c6ac121ace3cb073961079adda2ca9dbb9777d?s=64&d=mm&r=g) Shakeel says:
        
        [December 15, 2012 at 7:27 am](https://chandoo.org/wp/find-text-pattern/#comment-347679)
        
        correction
        
        **Description**                   **LEN**  
        Nothing C                         9  
        Few things P                  12  
        Lots of things A              16  
        Something P                   11  
        One thing A                    11  
        Another thing C             15 
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347679)
        
39.  ![](https://secure.gravatar.com/avatar/8b875c9820cb7b0be4f327283b40e70cf5d3cfcb0e612d17996ef90694e81067?s=64&d=mm&r=g) JP DAVY says:
    
    [December 15, 2012 at 8:09 am](https://chandoo.org/wp/find-text-pattern/#comment-347755)
    
    Hi everyone,  
    May I suggest the following array formula :  
    **{=INDEX(resRates,MAX(ISNUMBER(IFERROR(FIND(" " & resTypes & " ",B4),""))\*resIDs))}**  
    As you could notice :  
    I did not use any wild card.  
    I supposed the 'codes' were had no blank space in front and/or behind (e.g. CM, not \[ CM\], \[ CM \] or \[CM \]  
    I wanted to avoid that any code could be found inside another word (in col B)  
    I finally could find the trick to get it work whatever the length of the code  
    Congratulations and Thanks to you all  
    Have a great week end  
    _A Frenchie_
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347755)
    
40.  ![](https://secure.gravatar.com/avatar/9d50a3d9e3840ac36fd3c596db89594344e58775b2570336a7e6137b1a480091?s=64&d=mm&r=g) Sanjeev Gupta says:
    
    [December 15, 2012 at 8:56 am](https://chandoo.org/wp/find-text-pattern/#comment-347816)
    
    \=VLOOKUP("\*"&H4&"\*",$B$3:$D$33,3,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347816)
    
41.  ![](https://secure.gravatar.com/avatar/01c2cda8d6a968500797a59ca7f186d10dab5bbff529058e976af82579c1cf7b?s=64&d=mm&r=g) [Ravinder Negi](http://yahoo.com/)
     says:
    
    [December 15, 2012 at 9:05 am](https://chandoo.org/wp/find-text-pattern/#comment-347832)
    
    \=MAX(IFERROR((SEARCH("\*"&resTypes&"\*",B4))\*1\*(resRates),0))  
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347832)
    
42.  ![](https://secure.gravatar.com/avatar/411924af70342c1fc95adbec47db199d98220c6fffc1d272a7db1387c7c03d31?s=64&d=mm&r=g) pmsocho says:
    
    [December 15, 2012 at 9:22 am](https://chandoo.org/wp/find-text-pattern/#comment-347849)
    
    \=VLOOKUP(TRIM(MID(B4,LARGE(IF(MID(B4,ROW($A$1:$A$50),1)=" ",ROW($A$1:$A$50),0),2)+1,3)),$H$4:$I$9,2,0)  
    Array-entered. 
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347849)
    
43.  ![](https://secure.gravatar.com/avatar/f9c4b85a0a9b85beec57e34791e14440c631273eed007be1a3beb84d5b6fe0cc?s=64&d=mm&r=g) Uri says:
    
    [December 15, 2012 at 9:56 am](https://chandoo.org/wp/find-text-pattern/#comment-347884)
    
    Meanwhile Waiting
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347884)
    
44.  ![](https://secure.gravatar.com/avatar/8b875c9820cb7b0be4f327283b40e70cf5d3cfcb0e612d17996ef90694e81067?s=64&d=mm&r=g) JP DAVY says:
    
    [December 15, 2012 at 10:47 am](https://chandoo.org/wp/find-text-pattern/#comment-347947)
    
    Hi again,  
    Here's another suggestion  
    \=INDEX(resRates,SUM(--ISNUMERIC(FIND(" " & resTypes & " ",B4))\*resIDs))  
    As an array formula (CTRL+SHIFT+Enter)  
    Seems to work well ...
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-347947)
    
45.  ![](https://secure.gravatar.com/avatar/1f39af04164236ece3ed823f30f330f69a2de3c016b10204af752941a386b15b?s=64&d=mm&r=g) Quotenjunkie says:
    
    [December 15, 2012 at 1:14 pm](https://chandoo.org/wp/find-text-pattern/#comment-348072)
    
    \=MAX(IFERROR((SEARCH(resTypes;B4)/SEARCH(resTypes;B4))\*resRates;0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-348072)
    
46.  ![](https://secure.gravatar.com/avatar/19c7fc15c019a58b3188a9d9a8b5919d39aa9b4feebd4935f5b35f32408bd844?s=64&d=mm&r=g) Patnaik says:
    
    [December 15, 2012 at 1:48 pm](https://chandoo.org/wp/find-text-pattern/#comment-348131)
    
    Hi  
       
    using with array formula  
       
    \=MAX(IFERROR(SEARCH(resTypes,B4)/SEARCH(resTypes,B4)\*(resRates),0))  
       
    CTR+SHFT+ENTER
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-348131)
    
    *   ![](https://secure.gravatar.com/avatar/c443a69573a9ceef6d77ac4e33843313d2daa7ec6735d2750a0591e54ecd8cef?s=64&d=mm&r=g) Harish says:
        
        [December 18, 2012 at 12:38 pm](https://chandoo.org/wp/find-text-pattern/#comment-352366)
        
        Not working
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-352366)
        
47.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [December 15, 2012 at 3:09 pm](https://chandoo.org/wp/find-text-pattern/#comment-348230)
    
    This one as well:  
       
    \=INDEX(resRates,SUM(IF(IFERROR((SEARCH(resTypes,B4)\*ROW($A$1:$A$6))>0,0),ROW($A$1:$A$6))),0)  
       
    Ctrl+Shift+Enter  
       
    Regards,  
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-348230)
    
48.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [December 15, 2012 at 3:12 pm](https://chandoo.org/wp/find-text-pattern/#comment-348237)
    
    Hi All,  
       
    This one as well:  
       
    \=INDEX(resRates,SUM(IF(IFERROR((SEARCH(resTypes,B4)\*ROW($A$1:$A$6))>0,0),ROW($A$1:$A$6))),0)  
       
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-348237)
    
49.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [December 15, 2012 at 3:17 pm](https://chandoo.org/wp/find-text-pattern/#comment-348267)
    
    Hi  
       
    This one as well  
       
    \=INDEX(resRates,SUM(IF(IFERROR((SEARCH(resTypes,B4)\*ROW($A$1:$A$6))>0,0),ROW($A$1:$A$6))),0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-348267)
    
50.  ![](https://secure.gravatar.com/avatar/3fecba9a1eb61b3aafb9cd0fc6b88618d18f5bdd541ab5bd183da168de01d9cc?s=64&d=mm&r=g) Senthilkumar\_RM says:
    
    [December 16, 2012 at 3:36 am](https://chandoo.org/wp/find-text-pattern/#comment-348995)
    
    \=VLOOKUP(TRIM(MID(B4,FIND("x",B4)-4,3)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-348995)
    
51.  ![](https://secure.gravatar.com/avatar/5f9d2aa0d43d4f1e23dcc70a6334d770adea37a57a4a74258fdfec9016cd12e4?s=64&d=mm&r=g) oranus says:
    
    [December 16, 2012 at 8:20 am](https://chandoo.org/wp/find-text-pattern/#comment-349296)
    
    {=SUMPRODUCT(IF(IFERROR(FIND($H$4:$H$9;B4);0)>0;1;0);$I$4:$I$9)}
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-349296)
    
52.  ![](https://secure.gravatar.com/avatar/b1dda0b7163008c0bac2ae3592716af66f9eab5b942826460491d61678c6d9fa?s=64&d=mm&r=g) daniil says:
    
    [December 16, 2012 at 10:46 pm](https://chandoo.org/wp/find-text-pattern/#comment-350194)
    
    \=VLOOKUP(TRIM(MID(B4,FIND(" x",B4,1)-3,3)),$H$4:$I$9,2,FALSE)
    
    Came up with this in a couple min. It works but it's not as generic as I'd like.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-350194)
    
53.  ![](https://secure.gravatar.com/avatar/d3307dabaea7b5b83f6156b46f51ac11df32342f4c34708174932b57b9844c68?s=64&d=mm&r=g) jp says:
    
    [December 17, 2012 at 12:38 am](https://chandoo.org/wp/find-text-pattern/#comment-350286)
    
    I ended up with the following array formula
    
    \=SUMPRODUCT(IF(ISNUMBER(FIND(resTypes,B28))=TRUE,1,0),resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-350286)
    
54.  ![](https://secure.gravatar.com/avatar/80fd8539a2fd6d32a0c46df03b0248d7bf4e6bc9215673cd71668de0d63f718c?s=64&d=mm&r=g) delvillardennis says:
    
    [December 17, 2012 at 6:29 am](https://chandoo.org/wp/find-text-pattern/#comment-350571)
    
    This will work:
    
    \=LOOKUP(2^10,SEARCH(resTypes,B4),resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-350571)
    
    *   ![](https://secure.gravatar.com/avatar/db7ede23c655f2ba4dd63b04879d87bc5352c8ea247ef7db9a21b438e14ae31b?s=64&d=mm&r=g) subburaj says:
        
        [August 1, 2014 at 6:06 pm](https://chandoo.org/wp/find-text-pattern/#comment-585020)
        
        Request you to explain about 2^10
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-585020)
        
55.  ![](https://secure.gravatar.com/avatar/e396b8922686d537e2b2452ff2a343b0fd32e877735909b52ce7c9dfacc90a1e?s=64&d=mm&r=g) Udit says:
    
    [December 17, 2012 at 6:45 am](https://chandoo.org/wp/find-text-pattern/#comment-350591)
    
    I came up with this... I see many have similar entries
    
    \=SUMPRODUCT(IF(IFERROR(FIND(resTypes,B4),0)=0,0,1)\*resRates)
    
    One thing I would suggest to people who have used SEARCH in their formula. SEARCH isnt case-sensitive so in a case like this, it would be better to use FIND.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-350591)
    
56.  ![](https://secure.gravatar.com/avatar/1dfb3e2ea93d60aec6e3957128cc751768b47fd313041cec998b998ac24a822c?s=64&d=mm&r=g) MOHAMMED A. WASEEM says:
    
    [December 17, 2012 at 11:28 am](https://chandoo.org/wp/find-text-pattern/#comment-350907)
    
    I have got the correct results, the following is the formula :
    
    VLOOKUP(TRIM(IF(ISERROR(IF(ISERROR(MID(B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1)-FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1))=TRUE),MID(B4,L4+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)-FIND(" ",B4,FIND(" ",B4,1)+1)),MID(B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1)-FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)))=TRUE),MID(B4,FIND(" ",B4,1)+1,FIND(" ",B4,FIND(" ",B4,1)+1)-FIND(" ",B4,1)),IF(ISERROR(MID(B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1)-FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1))=TRUE),MID(B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)-FIND(" ",B4,FIND(" ",B4,1)+1)),MID(B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1)-FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1))))),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-350907)
    
57.  ![](https://secure.gravatar.com/avatar/1dfb3e2ea93d60aec6e3957128cc751768b47fd313041cec998b998ac24a822c?s=64&d=mm&r=g) MOHAMMED A. WASEEM says:
    
    [December 17, 2012 at 11:49 am](https://chandoo.org/wp/find-text-pattern/#comment-350917)
    
    I got it, following is the formula :
    
    \=VLOOKUP(TRIM(IF(ISERROR(IF(ISERROR(MID(B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1)-FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1))=TRUE),MID(B4,L4+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)-FIND(" ",B4,FIND(" ",B4,1)+1)),MID(B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1)-FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)))=TRUE),MID(B4,FIND(" ",B4,1)+1,FIND(" ",B4,FIND(" ",B4,1)+1)-FIND(" ",B4,1)),IF(ISERROR(MID(B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1)-FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1))=TRUE),MID(B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)-FIND(" ",B4,FIND(" ",B4,1)+1)),MID(B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1)+1)-FIND(" ",B4,FIND(" ",B4,FIND(" ",B4,1)+1)+1))))),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-350917)
    
58.  ![](https://secure.gravatar.com/avatar/3f58be5a37323864904629ef04a9faf99b3f6ac9f8042daceb61d931dc75f3e8?s=64&d=mm&r=g) prince says:
    
    [December 18, 2012 at 5:47 am](https://chandoo.org/wp/find-text-pattern/#comment-351955)
    
    **\=TRIM(MID(B4,IFERROR(IFERROR(IFERROR(SEARCH(("ing ?? xx"),B4)+5,SEARCH(("ings ?? xx"),B4)+5),SEARCH(("ing ??? xx"),B4)+5),SEARCH(("ings ??? xx"),B4)+5)-1,SEARCH("xx",B4)-IFERROR(IFERROR(IFERROR(SEARCH(("ing ?? xx"),B4)+5,SEARCH(("ings ?? xx"),B4)+5),SEARCH(("ing ??? xx"),B4)+5),SEARCH(("ings ??? xx"),B4)+5)))**
    
    **my solution is also long 🙁**
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-351955)
    
59.  ![](https://secure.gravatar.com/avatar/3a2006732793487b4195c2d6bd9d8cf504e41a35191688c69ffb58d1ee025e9d?s=64&d=mm&r=g) [Jaydeep Moulik](http://na/)
     says:
    
    [December 18, 2012 at 7:43 am](https://chandoo.org/wp/find-text-pattern/#comment-352083)
    
    \=VLOOKUP(IF(MID(B4,FIND("x",B4)-1-3,1)=" ",MID(B4,FIND("x",B4)-1-2,2),MID(B4,FIND("x",B4)-1-3,3)),$H$3:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-352083)
    
60.  ![](https://secure.gravatar.com/avatar/d6c30d6cc8ee36edb79f8f67e8a54c3a8c43826a2f4b9f798902d7aff9a85a77?s=64&d=mm&r=g) Amritansh says:
    
    [December 18, 2012 at 8:59 am](https://chandoo.org/wp/find-text-pattern/#comment-352168)
    
    \=INDEX(resRates,MATCH(TRUE,IFERROR(FIND(resTypes,B5),0)<>0,0))
    
    Ctrl+Shift+Enter for array formula
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-352168)
    
61.  ![](https://secure.gravatar.com/avatar/8831a54b3547afd593350025198bccb32fc03ddbf2e9fd377ce0667820b17286?s=64&d=mm&r=g) Gaurav says:
    
    [December 18, 2012 at 10:03 am](https://chandoo.org/wp/find-text-pattern/#comment-352228)
    
    Hi chandoo,
    
    although i havent use countif function, but i have found an alternative to this problem. my only concern is that it took me 15-20 mins atleast for arriving at this solution which to too much. if u cud sugest a shorter or more simpler solution to it, i shall be grateful. 
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-352228)
    
62.  ![](https://secure.gravatar.com/avatar/8831a54b3547afd593350025198bccb32fc03ddbf2e9fd377ce0667820b17286?s=64&d=mm&r=g) Gaurav says:
    
    [December 18, 2012 at 10:04 am](https://chandoo.org/wp/find-text-pattern/#comment-352229)
    
    \=VLOOKUP(IF(MID(B8,FIND("x",B8)-4,1)=" ",MID(B8,FIND("x",B8)-3,2),MID(B8,FIND("x",B8)-4,3)),$H$3:$I$9,2,0)
    
    Hi chandoo,  
    although i havent use countif function, but i have found an alternative to this problem. my only concern is that it took me 15-20 mins atleast for arriving at this solution which to too much. if u cud sugest a shorter or more simpler solution to it, i shall be grateful.  
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-352229)
    
63.  ![](https://secure.gravatar.com/avatar/ba96e5980f8b87d2ad519e755fb475b0d70c5ef03199191704c6f868a71bbffe?s=64&d=mm&r=g) Oli says:
    
    [December 18, 2012 at 3:08 pm](https://chandoo.org/wp/find-text-pattern/#comment-352505)
    
    Late to the party but here is what I came up with  
    \=MAX(IFERROR(MATCH("\*"&$H$4:$H$9&"\*",B4,0),0)\*resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-352505)
    
64.  ![](https://secure.gravatar.com/avatar/ca3ce845372f436651795c659508263af9ce248438f332dbe89fe6d88ab416a2?s=64&d=mm&r=g) Ryan says:
    
    [December 18, 2012 at 4:46 pm](https://chandoo.org/wp/find-text-pattern/#comment-352642)
    
    Entered as an array:
    
    \=VLOOKUP(MATCH(1,COUNTIF(B4,"\*"&resTypes&"\*"),0),$G$4:$I$9,3,0)
    
    Not as elegant/straightforward as some of the others, but does not rely on the entry of an arbitrarily large value like 2^15. 
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-352642)
    
65.  ![](https://secure.gravatar.com/avatar/5a2752a18062d8735f1f7ae2b72982d0a4202574727eca9e4dc1308c001c0279?s=64&d=mm&r=g) Mayur Naik says:
    
    [December 19, 2012 at 11:55 am](https://chandoo.org/wp/find-text-pattern/#comment-353715)
    
    Quite late though , This formula gave me desired result :
    
    \=VLOOKUP(TRIM(IF(FIND("ing",B4,1),MID(B4,IFERROR(FIND("ings",B4,1),FIND("ing",B4,1))+4,FIND(" x",B4)-(IFERROR(FIND("ings",B4,1),FIND("ing",B4,1))+4)),IF(FIND("ings",B4,1),MID(B4,IFERROR(FIND("ings",B4,1),FIND("ing",B4,1))+5,FIND(" x",B4)-(IFERROR(FIND("ings",B4,1),FIND("ing",B4,1))+5))))),$H$4:$I$9,2,0) 
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-353715)
    
66.  ![](https://secure.gravatar.com/avatar/b7ecde76e797e6aea0e9407bb8cce1cff427ca1654db1ae3202377181f3e87b9?s=64&d=mm&r=g) Yogesh says:
    
    [December 20, 2012 at 9:04 am](https://chandoo.org/wp/find-text-pattern/#comment-354957)
    
    \=VLOOKUP(TRIM(RIGHT(LEFT(B4,FIND(" xxx",B4,1)),4)),$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-354957)
    
67.  ![](https://secure.gravatar.com/avatar/264475311ad5a4e3fd8d67bd93e44458e316c365b07c19d322f266f10f300663?s=64&d=mm&r=g) [Istiyak](http://istiyak.shaikh@hpage.com/)
     says:
    
    [December 25, 2012 at 3:00 pm](https://chandoo.org/wp/find-text-pattern/#comment-362340)
    
    hi,
    
    TO Vijay:
    
    Is it mendatory to put 2^15.
    
    if i want to try with another string.  
    i.e. 
    
    PJEAL-S-JY13551-12A1
    
    In that string i want 12a1.
    
    no doubt with your formula i m getting result. but i want to understand the fundamental about "2^15".
    
    Hope you will understand.
    
    Regards  
    Istiyak 
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-362340)
    
68.  ![](https://secure.gravatar.com/avatar/e29a29adbfa011345fc203af35ef248bfbc368ad44593815e0afecef04aa4599?s=64&d=mm&r=g) Antonio says:
    
    [December 26, 2012 at 12:54 am](https://chandoo.org/wp/find-text-pattern/#comment-362852)
    
    You don't need to use 2^15. You just need to use a number that is bigger than the size (number of characters) of your largest string. If your strings are always less than 30 characters, you can use 30 instead of 2^15. If you don't know the size of your strings or you want to use a number that fits all situations, use the max number of characters a cell can hold (which is 32768 = 2^15).
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-362852)
    
69.  ![](https://secure.gravatar.com/avatar/13d43e3fe330177abb076eeb8ed2c9b4468e33e7fed7ee363a0948e2df2655ab?s=64&d=mm&r=g) Tom Dorsey says:
    
    [December 27, 2012 at 12:11 am](https://chandoo.org/wp/find-text-pattern/#comment-364351)
    
    \=VLOOKUP(TRIM(MID(B4,FIND("x",B4)-4,4)),$G$4:$H$9,2,FALSE)
    
    where B4 is the search string, and $G$4:$H$9 is the vlookup range. 
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-364351)
    
70.  ![](https://secure.gravatar.com/avatar/addd6ae4ded132bfde6d5e7e8d51fec93a050e7738ac178845373a56efa76ee1?s=64&d=mm&r=g) Sachin says:
    
    [December 27, 2012 at 3:30 pm](https://chandoo.org/wp/find-text-pattern/#comment-365347)
    
    Hey I tried this long formula and it worked VLOOKUP(IF(COUNTIF(B4,"\*"&$H$4&"\*")<>0,$H$4,IF(COUNTIF(B4,"\*"&$H$5&"\*")<>0,$H$5,IF(COUNTIF(B4,"\*"&$H$6&"\*")<>0,$H$6,IF(COUNTIF(B4,"\*"&$H$7&"\*")<>0,$H$7,IF(COUNTI....................
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-365347)
    
71.  ![](https://secure.gravatar.com/avatar/33682e84ff8f98f270e5cdf85eafff518545266ed1d0a14a9e92caf8f176477c?s=64&d=mm&r=g) [Vikas Chauhan](http://vikask008.hpage.com/)
     says:
    
    [December 28, 2012 at 9:33 am](https://chandoo.org/wp/find-text-pattern/#comment-366364)
    
    my answer is 
    
    \=VLOOKUP((TRIM(RIGHT((LEFT(B4,FIND(" x",B4))),4))),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-366364)
    
72.  ![](https://secure.gravatar.com/avatar/e5ce96064939126adb19813ef9e7872561e9ce32c13c51b3faf71fdd10d7d263?s=64&d=mm&r=g) Bill Tong says:
    
    [January 2, 2013 at 4:08 pm](https://chandoo.org/wp/find-text-pattern/#comment-374794)
    
    \=IF(ISERROR(FIND(H$4,B4)),IF(ISERROR(FIND(H$5,B4)),IF(ISERROR(FIND(H$6,B4)),IF(ISERROR(FIND(H$7,B4)),IF(ISERROR(FIND(H$8,B4)),IF(ISERROR(FIND(H$9,B4)),0,250),150),120),75),60),50)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-374794)
    
    *   ![](https://secure.gravatar.com/avatar/64f3ca9031d8d6d04048ec2f41499646f58129752d4e1e3646103e8684042a97?s=64&d=mm&r=g) zur says:
        
        [January 3, 2013 at 9:20 am](https://chandoo.org/wp/find-text-pattern/#comment-376059)
        
        Please display the full formula
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-376059)
        
73.  ![](https://secure.gravatar.com/avatar/d3fe07e573358c852c1bb91cabb87ee1e3639becf8aa4b630cf006fa61b3e7e0?s=64&d=mm&r=g) [Grant](http://www.effex.co.za/)
     says:
    
    [January 10, 2013 at 6:48 am](https://chandoo.org/wp/find-text-pattern/#comment-386987)
    
    Hi Chandoo  
    Loved this post!  
    I find these days, I immediately default to using Boolean logic when dealing with array formulas - especially as the COUNTIF first argument "range" doesn't accept arrays - BUT I did not know that the second argument can!  
       
    So here is my formula:  
    \=INDEX(resRates,MATCH(1,COUNTIF(B4,"\*"&resTypes&"\*"),0))  
       
    Thanks for the great content
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-386987)
    
74.  ![](https://secure.gravatar.com/avatar/864bc03c0d303d01fee370b4f8d7869525c15c8862db8ddda339c4761bc0ffd7?s=64&d=mm&r=g) Raj Kumar Kothari says:
    
    [January 12, 2013 at 11:00 am](https://chandoo.org/wp/find-text-pattern/#comment-390005)
    
    \=LOOKUP(9.99999999999999E+307,SEARCH(resTypes,B4),resRates)  
    Being in the E-Commerce Industry, I use this awesome trick all the time to get the color of the products form there names from a list of colors.  
    Having said that the problem with this formula is that it would look up the keywords inside a word or any where in the text also for example the keyword "AM" would be looked up in the following sentence "No**AM**ing CM xxxx4607" (just for eg.) but the correct answer should be CM instead of AM. To avoid this what I do is add a space before and after the keyword, which reduces the chances of this kind of errors.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-390005)
    
75.  ![](https://secure.gravatar.com/avatar/b626aa17679406a39f76227ac647397cb0d0fe227d9053253aeb5ec97630c940?s=64&d=mm&r=g) Jitendra Jain says:
    
    [January 12, 2013 at 11:16 am](https://chandoo.org/wp/find-text-pattern/#comment-390032)
    
    Hi,  
    i used below formula & got the answers  
    \=VLOOKUP(TRIM(RIGHT(LEFT(B4,FIND("xxx",B4,1)-2),3)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-390032)
    
76.  ![](https://secure.gravatar.com/avatar/b926e2c9a7bc01e2e4f795cb6a7c6e646a8a11e118a6232d25b757c2fc1b32c7?s=64&d=mm&r=g) Gabriel says:
    
    [January 28, 2013 at 1:19 pm](https://chandoo.org/wp/find-text-pattern/#comment-409524)
    
    Building the 2 char code:  
    \=RIGHT(LEFT(B4,FIND("x",B4)-2),2)  
    find the wildcard code via vlookup:  
    \=VLOOKUP("\*"&E4&"\*",$H$4:$I$9,2,0)  
    of course you can join them together. ( but it harder to understand )
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-409524)
    
77.  ![](https://secure.gravatar.com/avatar/b926e2c9a7bc01e2e4f795cb6a7c6e646a8a11e118a6232d25b757c2fc1b32c7?s=64&d=mm&r=g) Gabriel says:
    
    [January 28, 2013 at 1:21 pm](https://chandoo.org/wp/find-text-pattern/#comment-409525)
    
    E4 IN the previous is the 2 char code.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-409525)
    
78.  ![](https://secure.gravatar.com/avatar/e2cda6bb869114f1dc685c4e3ac122530a01cd08b5ecce786b213a259374dec9?s=64&d=mm&r=g) [Andreas](http://schuderer.net/)
     says:
    
    [February 4, 2013 at 1:58 pm](https://chandoo.org/wp/find-text-pattern/#comment-411357)
    
    Haven't seen my solution here yet:  
    {=SUM(IF(ISERROR(FIND(resTypes,B2)),0,resRates))}  
    This is an array formula. Enter it without the curly braces and hit Ctrl+Shift+Enter instead of Enter.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-411357)
    
79.  ![](https://secure.gravatar.com/avatar/0a8cf4d0ff38419149ae34d9d63e63af9992b157706d9ad7806778712e139182?s=64&d=mm&r=g) Usman says:
    
    [March 2, 2013 at 10:37 am](https://chandoo.org/wp/find-text-pattern/#comment-417087)
    
    can some body explain me, =SEARCH(resTypes,B4) as it returns # VALUE! in my excel sheet   
       
       
       
     
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-417087)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [March 3, 2013 at 4:09 am](https://chandoo.org/wp/find-text-pattern/#comment-417246)
        
        @Usman  
        It's because the value in B4 can't be found in the Range resTypes  
        This is either because B4 isn't in the range or that the range isn't where you think it is  
        You may also want to check that either B4 or the values in the range don't have leading or trailing spaces
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-417246)
        
80.  ![](https://secure.gravatar.com/avatar/0a8cf4d0ff38419149ae34d9d63e63af9992b157706d9ad7806778712e139182?s=64&d=mm&r=g) Usman says:
    
    [March 3, 2013 at 11:28 am](https://chandoo.org/wp/find-text-pattern/#comment-417303)
    
    @Hui thanks, I guess u have answers to my questions 🙂  
    the thing is vijay posted this formula (above) =LOOKUP(16,SEARCH(resTypes,B4),resRates)  
       
    what I am trying is to understand is that how this formula works so I took out the SEARCH(resTypes,B4) part out to understand in pieces but it returns #VALUE! so I m confused, and one more thing is it necessary for the search formula refer to a named range or I can give simple range like H4:H9 ???  
    please help and thanks alot 🙂
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-417303)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) Hui says:
        
        [March 3, 2013 at 12:22 pm](https://chandoo.org/wp/find-text-pattern/#comment-417308)
        
        @Usman  
        It depends on where the name ResTypes is referring to are you sure it's where you expect?  
        Can you post the file?
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-417308)
        
81.  ![](https://secure.gravatar.com/avatar/0a8cf4d0ff38419149ae34d9d63e63af9992b157706d9ad7806778712e139182?s=64&d=mm&r=g) Usman says:
    
    [March 3, 2013 at 3:33 pm](https://chandoo.org/wp/find-text-pattern/#comment-417336)
    
    I dont no how to post file ? as there is isnt any link for uploading file can i email u or some thing.....as I also want to send u the file for the Question on sum product that we have been discussing on another page.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-417336)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [March 4, 2013 at 9:19 am](https://chandoo.org/wp/find-text-pattern/#comment-417508)
        
        @Usman  
        You can email me click on Hui... above or  
        [http://chandoo.org/forums/topic/posting-a-sample-workbook](http://chandoo.org/forums/topic/posting-a-sample-workbook)
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-417508)
        
82.  ![](https://secure.gravatar.com/avatar/41d70259d728e6b2ea6005a682eb53e7379ab6565cde42f7dffc0823e49c7765?s=64&d=mm&r=g) richard says:
    
    [March 22, 2013 at 10:40 am](https://chandoo.org/wp/find-text-pattern/#comment-420740)
    
    Well, here is my solution:  
    \=SUMPRODUCT(COUNTIF(B4,"\* "&resTypes&" \*"),resRates)  
    by entering an array in COUNTIF function I get back an array of same size as resType consisting of 1s and 0s. So, I used that array to multiply the billing rate array using SUMPRODUCT. Brilliant website, makes the complicated understandable.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-420740)
    
83.  ![](https://secure.gravatar.com/avatar/1457a0ec4520b4b6c091fef4c2a3e4e6093e0b261baab0a202675b78d9c8de48?s=64&d=mm&r=g) Aniket Thombare says:
    
    [April 6, 2013 at 9:40 am](https://chandoo.org/wp/find-text-pattern/#comment-422550)
    
    **\=VLOOKUP(TRIM(RIGHT(MID(B4,1,FIND(" x",B4,1)),4)),$G$4:$H$9,2,FALSE)**
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-422550)
    
84.  ![](https://secure.gravatar.com/avatar/0e916f8e897a63112b894e8f5d7c78b47f5846cc20a50c761d956c8b95e2ae8d?s=64&d=mm&r=g) Mehul says:
    
    [April 24, 2013 at 7:53 am](https://chandoo.org/wp/find-text-pattern/#comment-426282)
    
    \=IF(ISNUMBER(FIND("CM",B5)),$I$7,IF(ISNUMBER(FIND("PM",B5)),$I$5,IF(ISNUMBER(FIND("FM",B5)),$I$6,IF(ISNUMBER(FIND("AM",B5)),$I$4,IF(ISNUMBER(FIND("RM",B5)),$I$8,IF(ISNUMBER(FIND("CXO",B5)),$I$9,))))))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-426282)
    
85.  ![](https://secure.gravatar.com/avatar/4181e6738f248b9f679035b344640b9ec16d0ef821c11976d3f8bde4eb9a2cc5?s=64&d=mm&r=g) Brent says:
    
    [May 1, 2013 at 10:53 pm](https://chandoo.org/wp/find-text-pattern/#comment-428366)
    
    I'm partial to SUMIFS
    
    Here is what I used:
    
    \=SUMIFS(resRates,resTypes,TRIM(RIGHT(LEFT(B4,FIND(" x",B4)),4)))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-428366)
    
86.  ![](https://secure.gravatar.com/avatar/1580baf6c8ba15b185b15e9044912cc66e47bf62c8a315521903e6fb94f2782e?s=64&d=mm&r=g) Rakesh Patel says:
    
    [May 14, 2013 at 10:56 am](https://chandoo.org/wp/find-text-pattern/#comment-430375)
    
    \=LOOKUP((IF(ISNUMBER(FIND("CM",B4,1)),"CM",IF(ISNUMBER(FIND("AM",B4,1)),"AM",IF(ISNUMBER(FIND("CXO",B4,1)),"CXO",IF(ISNUMBER(FIND("RM",B4,1)),"RM",IF(ISNUMBER(FIND("PM",B4,1)),"PM",IF(ISNUMBER(FIND("FM",B4,1)),"FM","XX"))))))),resTypes,resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-430375)
    
87.  ![](https://secure.gravatar.com/avatar/b926e2c9a7bc01e2e4f795cb6a7c6e646a8a11e118a6232d25b757c2fc1b32c7?s=64&d=mm&r=g) Gabriel says:
    
    [June 16, 2013 at 4:31 am](https://chandoo.org/wp/find-text-pattern/#comment-436647)
    
    Can someone summerise the good answres such as the shortes one ( minimum functions) or the simple one to understand or most dynamic model ? ( it is quiet a lot of time to check all the answers)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-436647)
    
88.  ![](https://secure.gravatar.com/avatar/5c81df4333ee153363932b44aee464f5214038b5956993fbdb753d26aaeb429a?s=64&d=mm&r=g) El\_Terrible says:
    
    [August 5, 2013 at 6:15 pm](https://chandoo.org/wp/find-text-pattern/#comment-442257)
    
    \=IF(NOT(ISERROR(FIND("AM",B4))),VLOOKUP("AM",RES,2,FALSE),IF(NOT(ISERROR(FIND("PM",B4))),VLOOKUP("PM",RES,2,FALSE),IF(NOT(ISERROR(FIND("FM",B4))),VLOOKUP("FM",RES,2,FALSE),IF(NOT(ISERROR(FIND("CM",B4))),VLOOKUP("CM",RES,2,FALSE),IF(NOT(ISERROR(FIND("RM",B4))),VLOOKUP("RM",RES,2,FALSE),IF(NOT(ISERROR(FIND("CXO",B4))),VLOOKUP("CXO",RES,2,FALSE),"NOTHING FOUND"))))))
    
    This one took me awhile, but I finally came up with a solution. It's pretty lengthy, so I do apologize for that ;\\.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-442257)
    
89.  ![](https://secure.gravatar.com/avatar/d5ed012b3ece34e5368a362dbe78aa5b563541ee93732085091ea430106d2db3?s=64&d=mm&r=g) Delson says:
    
    [August 6, 2013 at 5:23 am](https://chandoo.org/wp/find-text-pattern/#comment-442312)
    
    \=IF(RIGHT(MID(B4,1,FIND(" x",B4,1)-1),2)="XO",RIGHT(MID(B4,1,FIND(" x",B4,1)-1),3),RIGHT(MID(B4,1,FIND(" x",B4,1)-1),2))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-442312)
    
90.  ![](https://secure.gravatar.com/avatar/9c208ad6a2fc14905e196966102ffb12d615c0709c83db7e08a4e7a3c1c4f5bf?s=64&d=mm&r=g) Faisal Ali says:
    
    [August 26, 2013 at 7:55 am](https://chandoo.org/wp/find-text-pattern/#comment-444220)
    
    \=SUMIF($H$4:$H$9,TRIM(MID(B4,FIND("xx",B4,1)-4,3)),$I$4:$I$9)
    
    Maybe got lucky with the names !
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-444220)
    
91.  ![](https://secure.gravatar.com/avatar/c5a321b550161678a67ecd0e93413a0655e776089592a7321674064674a5e23e?s=64&d=mm&r=g) Meeran ekkeri says:
    
    [September 1, 2013 at 1:25 pm](https://chandoo.org/wp/find-text-pattern/#comment-444815)
    
    \=VLOOKUP(TRIM(MID(B4,FIND("xx",B4)-4,3)),$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-444815)
    
92.  ![](https://secure.gravatar.com/avatar/715054bc966ddba98e69811dc96c191c61b48fa809dc5c1754ea4bcf55b63518?s=64&d=mm&r=g) Alexis David says:
    
    [October 3, 2013 at 12:10 pm](https://chandoo.org/wp/find-text-pattern/#comment-447913)
    
    Hi guys,
    
    Here is what I just came up with (and I'm sure there is a way to get rid of the IFERROR)
    
    \=SUM((IFERROR(IF(FIND(resTypes;B4)0;1);0)\*resRates))  
    and Ctrl + Alt + Enter
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-447913)
    
93.  ![](https://secure.gravatar.com/avatar/c9492c612a17092ecf8824e9c34a3881402a6a0b9ba88d1c24faadecedb38b62?s=64&d=mm&r=g) Roger says:
    
    [January 14, 2014 at 3:20 am](https://chandoo.org/wp/find-text-pattern/#comment-465239)
    
    Hello everybody.
    
    To solve this problem I used this formula for every cell in Billing Rate column.
    
    \=VLOOKUP(  
    IF(COUNTIF(B4,"\*"&$H$4&"\*"),1,  
    IF(COUNTIF(B4,"\*"&$H$5&"\*"),2,  
    IF(COUNTIF(B4,"\*"&$H$6&"\*"),3,  
    IF(COUNTIF(B4,"\*"&$H$7&"\*"),4,  
    IF(COUNTIF(B4,"\*"&$H$8&"\*"),5,  
    IF(COUNTIF(B4,"\*"&$H$9&"\*"),6,0)))))),  
    $G$4:$I$9,3)
    
    I worked for me.
    
    Thanks.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-465239)
    
94.  ![](https://secure.gravatar.com/avatar/c9492c612a17092ecf8824e9c34a3881402a6a0b9ba88d1c24faadecedb38b62?s=64&d=mm&r=g) Roger says:
    
    [January 14, 2014 at 3:42 am](https://chandoo.org/wp/find-text-pattern/#comment-465241)
    
    Hello everybody.
    
    To solve this problem I used this formula for every cell in Billing Rate column.
    
    \=VLOOKUP(MATCH(1,COUNTIF(B4,"\*"&resTypes&"\*"),0),$G$4:$I$9,3)
    
    Take care to enter the formula in cell C4 and finish with Shift+Ctrl+Enter because is a formula array. Then copy it to range C5:C33.
    
    Thanks.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-465241)
    
95.  ![](https://secure.gravatar.com/avatar/24f62fdfdb5d7142ba2a3cde41a75bb3c0ef3fc53211b0da8c2503c4fa4f1a56?s=64&d=mm&r=g) ALPESH says:
    
    [February 5, 2014 at 12:47 pm](https://chandoo.org/wp/find-text-pattern/#comment-468564)
    
    G H  
    particular amt  
    NOTHING CM 120  
    FEW MC 50
    
    answer :  
    partricular amt  
    CM( J9) (?) 120  
    formula : =VLOOKUP("\*"&J9&"\*",$G$9:$H$10,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-468564)
    
96.  ![](https://secure.gravatar.com/avatar/e83e0d6ac5fff697f66ed2cc0941e8196b6b8c65ebf7bb35ea4d3083c70061a0?s=64&d=mm&r=g) David M. says:
    
    [February 21, 2014 at 9:07 pm](https://chandoo.org/wp/find-text-pattern/#comment-470909)
    
    \=SUMPRODUCT(--(COUNTIF($B4,"\*"&resTypes&"\*")=1),resRates)
    
    memory efficient array without ctrl+shift+enter.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-470909)
    
97.  ![](https://secure.gravatar.com/avatar/3634835f6131806698500bc26a0b020b97d2a7c6249d5be11db4920ba639ed2d?s=64&d=mm&r=g) Paul S. says:
    
    [March 21, 2014 at 7:00 pm](https://chandoo.org/wp/find-text-pattern/#comment-475091)
    
    Assuming the data in this table will have the following consistencies based on the data already there.  
    1\. Assume that the last segment starts with at least 2 x's.  
    2\. Assume there will be a space before the lookup code we want to use.  
    3\. Assume code will always be 2 or 3 characters long.  
    For those of us not as proficient with concise formulas, I built the following formula step by step in cheater cells first (much easier to build it and follow it along), and then put them all together into the one cell. The formula I use is longer than many, but building it piece by piece, it may be easier for those of use who are not as "awesome" in Excel. It is all based on the 3 assumptions above and searching for key characters to find the lengths of the different segments we want to know so that we can use the mid formula.  
    The following is to get the Code to look up.  
    \=MID(B4,SEARCH(" ",B4,SEARCH(" xx",B4,1)-6)+1,SEARCH(" xx",B4,1)-(SEARCH(" ",B4,SEARCH(" xx",B4,1)-6)+1))
    
    Explanation:  
    \=MID(B4, --- Want to take the middle portion of B4 for the code.
    
    SEARCH(" ",B4,SEARCH(" xx",B4,1)-6)+1 -- Since the " xx" seems the easiest to find, the later portion looks for the " xx", and backs up 6 characters as our starting point to find the space before the 2 or 3 character code. Once you find the space before the code, you need to add one space to get the first character of the code.
    
    SEARCH(" xx",B4,1)-(SEARCH(" ",B4,SEARCH(" xx",B4,1)-6)+1))  
    \-- The first part of this gets the length of where the " xx" begins or where the code ends. The later part gets the length of where the code begins as explained in the item above. Subtracting the two, you get the length you want for the length of the Mid function.
    
    The above gets the code value. You then add it to the vlookup to get the final formula which should be placed into cell C4 and copied down.  
    \=VLOOKUP(MID(B4,SEARCH(" ",B4,SEARCH(" xx",B4,1)-6)+1,SEARCH(" xx",B4,1)-(SEARCH(" ",B4,SEARCH(" xx",B4,1)-6)+1)),$H$4:$I$9,2,FALSE)
    
    I hope people can follow this. Trying to explain something like this in a post is a little difficult without the use of color coding, etc. I know this seems long, but building it step by step, it isn't too bad. The main thing is that it is using more "normal" functions for those of us who are not as "awesome" in Excel.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475091)
    
98.  ![](https://secure.gravatar.com/avatar/0f272fbef52d877bdb4099e4e342cf43852df46f0db40b53784578ae54342ffa?s=64&d=mm&r=g) Mukesh says:
    
    [March 22, 2014 at 5:24 am](https://chandoo.org/wp/find-text-pattern/#comment-475183)
    
    i have no idea about this...  
    kindly explain me how to do this......
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475183)
    
99.  ![](https://secure.gravatar.com/avatar/1dfb3e2ea93d60aec6e3957128cc751768b47fd313041cec998b998ac24a822c?s=64&d=mm&r=g) [M. A. Waseem](http://nowebsite/)
     says:
    
    [March 22, 2014 at 5:44 am](https://chandoo.org/wp/find-text-pattern/#comment-475186)
    
    \=VLOOKUP(TRIM(CONCATENATE(MID(B4,FIND("x",B4,1)-1-3,1),MID(B4,FIND("x",B4,1)-1-2,1),MID(B4,FIND("x",B4,1)-1-1,1))),$H$4:$I$9,2,0)
    
    This is my second response to this and this is far smaller compared to my earlier formula
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475186)
    
100.  ![](https://secure.gravatar.com/avatar/29c4031b33771756cc318e4fe0ac162c7a52743d4018691abf8d13e22122b355?s=64&d=mm&r=g) Bibek Saha says:
    
    [March 24, 2014 at 9:49 am](https://chandoo.org/wp/find-text-pattern/#comment-475502)
    
    Try this formula, It is working on my side:  
    \=INDEX($J$32:$K$37,MATCH(TRIM(MID(B32,FIND("xx",B32)-4,3)),$J$32:$J$37,0),2)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475502)
    
101.  ![](https://secure.gravatar.com/avatar/164291cfc92a59344169a61fea96ba454ddcd0c76404f50a92ca1b1ccdbecd9f?s=64&d=mm&r=g) Chus says:
    
    [March 24, 2014 at 10:24 am](https://chandoo.org/wp/find-text-pattern/#comment-475512)
    
    I guess the easier approach woul be sumproduct
    
    \=SUMPRODUCT(COUNT.IF(A1,"\*"&resTypes&"\*")\*resRates)
    
    But this one is easy aswell
    
    \=INDEX(resRates,MATCH(MID(A1,FIND("x",A1)-2,2),resTypes,0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475512)
    
102.  ![](https://secure.gravatar.com/avatar/55a44e8c79dd3a76f211cb40ac5f01ec0736906f5efff3bd9bcb47066f87099c?s=64&d=mm&r=g) Danail says:
    
    [March 24, 2014 at 12:08 pm](https://chandoo.org/wp/find-text-pattern/#comment-475541)
    
    I'm getting on this bit late but my solution for getting the billing rate is:  
    \=INDEX(resRates,MATCH(B4,"\*"&resTypes&"\*",1),1)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475541)
    
    *   ![](https://secure.gravatar.com/avatar/55a44e8c79dd3a76f211cb40ac5f01ec0736906f5efff3bd9bcb47066f87099c?s=64&d=mm&r=g) Danail says:
        
        [March 24, 2014 at 12:11 pm](https://chandoo.org/wp/find-text-pattern/#comment-475543)
        
        woops, sorry - this was a mistake
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475543)
        
103.  ![](https://secure.gravatar.com/avatar/55a44e8c79dd3a76f211cb40ac5f01ec0736906f5efff3bd9bcb47066f87099c?s=64&d=mm&r=g) Danail says:
    
    [March 24, 2014 at 12:20 pm](https://chandoo.org/wp/find-text-pattern/#comment-475545)
    
    This is my solution:  
    \=INDEX(resRates,MATCH(50,FIND(resTypes,B4),1),1)
    
    The constant "50" here depends on the length of the strings - here it is short and that's why 50.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475545)
    
104.  ![](https://secure.gravatar.com/avatar/dd97b9ae0c829aa82d232f8028ba0cb85e150191e1ca2a24c7f5a737170859b0?s=64&d=mm&r=g) Dylan says:
    
    [March 24, 2014 at 5:35 pm](https://chandoo.org/wp/find-text-pattern/#comment-475585)
    
    \=VLOOKUP(IFERROR(MID(B4,FIND("M",B4)-1,2),"CXO"),$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-475585)
    
105.  ![](https://secure.gravatar.com/avatar/65b25818d2458f5a81305637c7b9db8d8686735de512697df0339040756d14ec?s=64&d=mm&r=g) vidushi says:
    
    [March 30, 2014 at 5:20 pm](https://chandoo.org/wp/find-text-pattern/#comment-476538)
    
    Why we have used max function in this formula :
    
    \=INDEX(resRates,MAX(COUNTIF(B4,"\*"&resTypes&"\*")\*(resIDs)))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-476538)
    
106.  ![](https://secure.gravatar.com/avatar/9db0ba26c73be599e26d365e5775c8b253b3b330eafff9ef2dc4089ece6daf73?s=64&d=mm&r=g) Francis says:
    
    [April 1, 2014 at 10:59 am](https://chandoo.org/wp/find-text-pattern/#comment-476861)
    
    \=VLOOKUP(TRIM(MID(B4,FIND("x",B4)-4,4)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-476861)
    
107.  ![](https://secure.gravatar.com/avatar/a7dac39a691fce4c367686737569328c87ace55328ad33e3f97c3c62343b4d90?s=64&d=mm&r=g) Ashok Sindkar says:
    
    [April 5, 2014 at 4:08 am](https://chandoo.org/wp/find-text-pattern/#comment-477313)
    
    I am using Excel-2013 and it is very simple with it. I copied this all to new sheet. Then inserted one column after B column. Using flash fill CM,CXO,RM can be easily extracted in new column. After that required output can get easily using simple Vlookup formula.  
    \=VLOOKUP(C4,$I$4:$J$9,2,FALSE).  
    Thanks.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-477313)
    
108.  ![](https://secure.gravatar.com/avatar/739cfdb5ea30edb21f11f556a7d6e2bbeeb70a73e879852930da9403469d6d53?s=64&d=mm&r=g) faresar says:
    
    [April 6, 2014 at 10:46 am](https://chandoo.org/wp/find-text-pattern/#comment-477437)
    
    Well i used the functions that i know and came up with nested if conditions. It's long i know but it works
    
    \=VLOOKUP(IF(ISNUMBER(SEARCH($H$4,B4)),MID(B4,SEARCH($H$4,B4),LEN($H$4)),IF(ISNUMBER(SEARCH($H$5,B4)),MID(B4,SEARCH($H$5,B4),LEN($H$5)),IF(ISNUMBER(SEARCH($H$6,B4)),MID(B4,SEARCH($H$6,B4),LEN($H$6)),IF(ISNUMBER(SEARCH($H$7,B4)),MID(B4,SEARCH($H$7,B4),LEN($H$7)),IF(ISNUMBER(SEARCH($H$8,B4)),MID(B4,SEARCH($H$8,B4),LEN($H$8)),IF(ISNUMBER(SEARCH($H$9,B4)),MID(B4,SEARCH($H$9,B4),LEN($H$9)),0)))))),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-477437)
    
109.  ![](https://secure.gravatar.com/avatar/db08bfe318fa21d025916eff867b3377439d8eda7ab526a46b8c5aa94e16865f?s=64&d=mm&r=g) Elkhan says:
    
    [April 9, 2014 at 6:59 pm](https://chandoo.org/wp/find-text-pattern/#comment-477852)
    
    formula below, or any analogue of it quoted here, is ok unless you have a reference character (like "x" in this case). otherwise any repetition of ResTypes characters will return wrong answer. interestingly different formulas gives wrong answers in different cases depending on where and what kind of repetition occurs in Res Desc text string.
    
    \=VLOOKUP(TRIM(LEFT(RIGHT(B4,(LEN(B4)-FIND("x",B4)+5)),4)),$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-477852)
    
110.  ![](https://secure.gravatar.com/avatar/db08bfe318fa21d025916eff867b3377439d8eda7ab526a46b8c5aa94e16865f?s=64&d=mm&r=g) Elkhan says:
    
    [April 9, 2014 at 8:51 pm](https://chandoo.org/wp/find-text-pattern/#comment-477864)
    
    In my previous post it should be "until you have a reference character", of course. Sorry for my bad English
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-477864)
    
111.  ![](https://secure.gravatar.com/avatar/1005e345a590e6eef6dc1111616c33b8cb6849918ba7ef71a2b307eb66f0975d?s=64&d=mm&r=g) lokesh says:
    
    [April 13, 2014 at 4:43 am](https://chandoo.org/wp/find-text-pattern/#comment-478408)
    
    \=VLOOKUP(IFERROR(MID(B4,SEARCH(" ?M",B4)+1,2),"CXO"),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-478408)
    
112.  ![](https://secure.gravatar.com/avatar/5256bb5c95df85654a1a5e0def2ba2935c71416610bd8713394930142245ecf0?s=64&d=mm&r=g) Sam says:
    
    [April 23, 2014 at 10:31 pm](https://chandoo.org/wp/find-text-pattern/#comment-486198)
    
    \=VLOOKUP(INDEX(resTypes,MATCH(1,COUNTIF(B4,"\*"&resTypes&"\*"),0)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-486198)
    
    *   ![](https://secure.gravatar.com/avatar/5256bb5c95df85654a1a5e0def2ba2935c71416610bd8713394930142245ecf0?s=64&d=mm&r=g) Sam says:
        
        [April 23, 2014 at 10:33 pm](https://chandoo.org/wp/find-text-pattern/#comment-486200)
        
        Forgot to mention: use ctrl + shift + enter
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-486200)
        
113.  ![](https://secure.gravatar.com/avatar/4ba3c5350e3131b6f74c701e8ae38eb93903f4eddcf9ef3afbb7eb3988288efa?s=64&d=mm&r=g) Bitoubi says:
    
    [June 19, 2014 at 3:40 pm](https://chandoo.org/wp/find-text-pattern/#comment-558786)
    
    \=VLOOKUP(TRIM(MID(B4,SEARCH("xxx",B4)-4,4)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-558786)
    
114.  ![](https://secure.gravatar.com/avatar/75c334365ff4885a44651a26505d1dad31307eafc37667131ab9089d8594d1ff?s=64&d=mm&r=g) Haz says:
    
    [June 27, 2014 at 5:30 pm](https://chandoo.org/wp/find-text-pattern/#comment-563762)
    
    {=INDEX(resRates,MATCH(1,MATCH("\* "&resTypes&" x\*",B4,0),0))}
    
    The " x\*" part is there to find the correct resource, so having "FM Radio" in the description doesn't bring the wrong result.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-563762)
    
115.  ![](https://secure.gravatar.com/avatar/aab3931bd50946503798f193ef86d53c0cd68d7e2857566c5510b52b5d888430?s=64&d=mm&r=g) Max says:
    
    [July 17, 2014 at 1:54 pm](https://chandoo.org/wp/find-text-pattern/#comment-574478)
    
    I split the text of that one column into several ones (seperating by spaces). Then I wrote this formula:
    
    \=IF(A2=$P$2;50;IF(A2=$P$3;60;IF(A2=$P$4;75;IF(A2=$P$5;120;IF(A2=$P$6;150;IF(A2=$P$7;250;0))))))
    
    And pulled it over 5 columns to the right and all the way down. Last thing was taking the sums of of those 5 columns with the formula.
    
    The P column has the legend.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-574478)
    
116.  ![](https://secure.gravatar.com/avatar/0a48c794ac4905db66f4151cc000e1a2d810fa6c8d205d15e066eb5e98d847fd?s=64&d=mm&r=g) Shibu Alex says:
    
    [July 30, 2014 at 4:36 am](https://chandoo.org/wp/find-text-pattern/#comment-582990)
    
    Hi All,
    
    This is formula which is giving correct answer for me 🙂
    
    \=COUNTIF(B4,CONCATENATE("\*",$H$4,"\*"))\*$I$4+COUNTIF(B4,CONCATENATE("\*",$H$5,"\*"))\*$I$5+COUNTIF(B4,CONCATENATE("\*",$H$6,"\*"))\*$I$6+COUNTIF(B4,CONCATENATE("\*",$H$7,"\*"))\*$I$7+COUNTIF(B4,CONCATENATE("\*",$H$8,"\*"))\*$I$8+COUNTIF(B4,CONCATENATE("\*",$H$9,"\*"))\*$I$9
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-582990)
    
117.  ![](https://secure.gravatar.com/avatar/db7ede23c655f2ba4dd63b04879d87bc5352c8ea247ef7db9a21b438e14ae31b?s=64&d=mm&r=g) subburaj says:
    
    [August 1, 2014 at 5:44 pm](https://chandoo.org/wp/find-text-pattern/#comment-584999)
    
    \=IFERROR(VLOOKUP(MID(B4,FIND($H$4,B4),2),$H$3:$I$9,2,0),IFERROR(VLOOKUP(MID(B4,FIND($H$5,B4),2),$H$3:$I$9,2,0),IFERROR(VLOOKUP(MID(B4,FIND($H$6,B4),2),$H$3:$I$9,2,0),IFERROR(VLOOKUP(MID(B4,FIND($H$7,B4),2),$H$3:$I$9,2,0),IFERROR(VLOOKUP(MID(B4,FIND($H$8,B4),2),$H$3:$I$9,2,0),IFERROR(VLOOKUP(MID(B4,FIND($H$9,B4),3),$H$3:$I$9,2,0),0))))))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-584999)
    
118.  ![](https://secure.gravatar.com/avatar/e768900f95173568b30c158deccb58d5974d7b9628cc9cec24ca1f8bb3fd3c94?s=64&d=mm&r=g) Dan says:
    
    [August 1, 2014 at 6:19 pm](https://chandoo.org/wp/find-text-pattern/#comment-585036)
    
    \=SUM(COUNTIF(B4,"=\*"&$H$4&"\*")\*$I$4,COUNTIF(B4,"=\*"&$H$5&"\*")\*$I$5,COUNTIF(B4,"=\*"&$H$6&"\*")\*$I$6,COUNTIF(B4,"=\*"&$H$7&"\*")\*$I$7,COUNTIF(B4,"=\*"&$H$8&"\*")\*$I$8,COUNTIF(B4,"=\*"&$H$9&"\*")\*$I$9)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-585036)
    
119.  ![](https://secure.gravatar.com/avatar/a6c3b738f052fada25b4d955ba54264648382a7713de2de1eb86dc4d8adbe05e?s=64&d=mm&r=g) Sumit says:
    
    [August 8, 2014 at 11:00 am](https://chandoo.org/wp/find-text-pattern/#comment-593116)
    
    Below is my solution
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-593116)
    
120.  ![](https://secure.gravatar.com/avatar/a6c3b738f052fada25b4d955ba54264648382a7713de2de1eb86dc4d8adbe05e?s=64&d=mm&r=g) Sumit says:
    
    [August 8, 2014 at 11:01 am](https://chandoo.org/wp/find-text-pattern/#comment-593117)
    
    Below is my solution:
    
    VLOOKUP(TRIM(MID(B4,(FIND(" xx",B4)-3), 3)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-593117)
    
    *   ![](https://secure.gravatar.com/avatar/d2eea2f0168a29526a3811e2c4de538d738b4924d658a57b196fab4ec288d80b?s=64&d=mm&r=g) Tim says:
        
        [September 18, 2014 at 11:41 am](https://chandoo.org/wp/find-text-pattern/#comment-748040)
        
        The formula works. check mine below
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-748040)
        
121.  ![](https://secure.gravatar.com/avatar/d2eea2f0168a29526a3811e2c4de538d738b4924d658a57b196fab4ec288d80b?s=64&d=mm&r=g) Tim says:
    
    [September 18, 2014 at 11:38 am](https://chandoo.org/wp/find-text-pattern/#comment-748028)
    
    Write the following formula in cell C4 and copy to the rest of the cells
    
    \=VLOOKUP(TRIM(RIGHT(LEFT(B4,FIND("xx",B4)-2),3)),$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-748028)
    
122.  ![](https://secure.gravatar.com/avatar/4796e5e6f652fb42ec9ca9daa901b467c7e2b178ca4dbd12ca02baeb03d5a4bd?s=64&d=mm&r=g) Umang says:
    
    [February 2, 2015 at 8:56 am](https://chandoo.org/wp/find-text-pattern/#comment-905368)
    
    Using simple excel functions-
    
    \=VLOOKUP(TRIM(RIGHT(TRIM(MID(B3,1,FIND(" x",B3)-1)),3)),$H$3:$I$8,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-905368)
    
123.  ![](https://secure.gravatar.com/avatar/1819fac522f7e1fbf7609f3cc99a36d01f50f6570b9339f1c4118e96380e9049?s=64&d=mm&r=g) Agung Karjono says:
    
    [March 26, 2015 at 8:20 am](https://chandoo.org/wp/find-text-pattern/#comment-939671)
    
    This is my solution
    
    \=LOOKUP(LEN(B4);FIND($H$4:$H$9;B4;1);$I$4:$I$9)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-939671)
    
124.  ![](https://secure.gravatar.com/avatar/a8c0b632912be8e36ee09ec6a321275928167549b2ade7f20e4852efc9d812da?s=64&d=mm&r=g) VândaloIT says:
    
    [May 11, 2015 at 3:09 pm](https://chandoo.org/wp/find-text-pattern/#comment-970998)
    
    Hi all,
    
    First of all I want you know this is the first time I see these challenges, so answering in 2015 a 2012 question !?!?!?! "Where you have been, you ask".
    
    Never mind, straight to my solution:
    
    \=sum(if(isnumber(find(restype,b8));resrates)) ending with ctrl+shif+enter as it is an array formula.
    
    Vândalo.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-970998)
    
125.  ![](https://secure.gravatar.com/avatar/d3f4b370241446fd1be092b2a9fa1a0800f29b2965955f3e5e30c7b32eb821d5?s=64&d=mm&r=g) Philip Stevenson says:
    
    [May 14, 2015 at 11:20 am](https://chandoo.org/wp/find-text-pattern/#comment-973468)
    
    My answer (a little bit long)
    
    \=VLOOKUP(IFERROR(IF(FIND($H$4,B4,1)>0,1,0),IFERROR(IF(FIND($H$5,B4,1)>0,2,0),IFERROR(IF(FIND($H$6,B4,1)>0,3,0),IFERROR(IF(FIND($H$7,B4,1)>0,4,0),IFERROR(IF(FIND($H$8,B4,1)>0,5,0),IFERROR(IF(FIND($H$9,B4,1)>0,6,0),"")))))),$G$4:$I$9,3,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-973468)
    
126.  ![](https://secure.gravatar.com/avatar/c63cf4efd6ef7a5ba8207631f361e6e63440519398ff666bb8508da76756c36d?s=64&d=mm&r=g) Abhay says:
    
    [August 3, 2015 at 9:14 am](https://chandoo.org/wp/find-text-pattern/#comment-1017844)
    
    use this formula
    
    \=VLOOKUP("\*"&MID(B4,FIND("x",B4)-3,2)&"\*",$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1017844)
    
127.  ![](https://secure.gravatar.com/avatar/a8c0b632912be8e36ee09ec6a321275928167549b2ade7f20e4852efc9d812da?s=64&d=mm&r=g) Vândalo says:
    
    [August 3, 2015 at 3:47 pm](https://chandoo.org/wp/find-text-pattern/#comment-1017967)
    
    It could seem silly among you excel gurus, but this was the first approach that crossed my mind.
    
    CTRL+SHIFT+ENTER
    
    \=INDEX(resRates;MAX(--ISNUMBER(FIND(resTypes;B4))\*{1;2;3;4;5;6}))
    
    Vândalo
    
    P.S. - I didn't red all the posts so I'm not aware if someone already posted an answer like this one.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1017967)
    
128.  ![](https://secure.gravatar.com/avatar/9902dbc38069592a4ec9a6cee357b2281210e772c3aa2fcdace199d02e925aa9?s=64&d=mm&r=g) surya prakash says:
    
    [August 26, 2015 at 7:29 am](https://chandoo.org/wp/find-text-pattern/#comment-1031460)
    
    \=VLOOKUP((TRIM(RIGHT(LEFT($B4,FIND(" xxx",$B4)-1),3))),H:I,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1031460)
    
129.  ![](https://secure.gravatar.com/avatar/a6283f70ef51d8165a85f38a1bfe7393bf05189163ad786f71269263e8f00a62?s=64&d=mm&r=g) Amit says:
    
    [October 23, 2015 at 1:25 pm](https://chandoo.org/wp/find-text-pattern/#comment-1067828)
    
    \=VLOOKUP(TRIM(MID(B4,FIND("x",B4)-4,3)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1067828)
    
130.  ![](https://secure.gravatar.com/avatar/42c63173b45cccd941f9d99714c7081d0346e4554129223c6b7f6dc614a7efa6?s=64&d=mm&r=g) Ata says:
    
    [November 6, 2015 at 4:40 am](https://chandoo.org/wp/find-text-pattern/#comment-1076574)
    
    \=INDEX(resRates,SUMPRODUCT(resIDs,COUNTIF(B4,"\*"&resTypes&"\*")))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1076574)
    
131.  ![](https://secure.gravatar.com/avatar/e341a3c99aa802bcdfb2b4584bbef9e367d603c8c17120e66d9abac97b44ebd6?s=64&d=mm&r=g) Vinay says:
    
    [February 16, 2016 at 6:58 am](https://chandoo.org/wp/find-text-pattern/#comment-1133414)
    
    Hi ,
    
    I was using formula --> =VLOOKUP("\*"&B4&"\*",H4:I9,2,0) but this does not work and gives error.
    
    Could someone please explain why it does not return the required output.
    
    Thanks,
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1133414)
    
132.  ![](https://secure.gravatar.com/avatar/ed9f42b96f89c87b5f2bd2a7f4022e9e58aed8044febe885935b816f32b1348e?s=64&d=mm&r=g) mukesh says:
    
    [April 12, 2016 at 5:17 pm](https://chandoo.org/wp/find-text-pattern/#comment-1167951)
    
    \=INDEX(resRates,MATCH(TRIM(LEFT(TRIM(SUBSTITUTE(B4,LEFT(B4,FIND(" x",B4,1)-4),"")),3)),$H$4:$H$9,0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1167951)
    
133.  ![](https://secure.gravatar.com/avatar/ed9f42b96f89c87b5f2bd2a7f4022e9e58aed8044febe885935b816f32b1348e?s=64&d=mm&r=g) mukesh says:
    
    [April 12, 2016 at 5:42 pm](https://chandoo.org/wp/find-text-pattern/#comment-1167956)
    
    \=INDEX($I$4:$I$9,MATCH(TRIM(MID(B4,IFERROR(FIND("gs",B4,1)+3,FIND("g ",B4,1)+2),3)),$H$4:$H$9,0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1167956)
    
134.  ![](https://secure.gravatar.com/avatar/ed9f42b96f89c87b5f2bd2a7f4022e9e58aed8044febe885935b816f32b1348e?s=64&d=mm&r=g) mukesh says:
    
    [April 12, 2016 at 5:59 pm](https://chandoo.org/wp/find-text-pattern/#comment-1167959)
    
    \=INDEX($I$4:$I$9,MATCH(TRIM(MID(B4,FIND(" x",B4,1)-3,3)),$H$4:$H$9,0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1167959)
    
135.  ![](https://secure.gravatar.com/avatar/ed9f42b96f89c87b5f2bd2a7f4022e9e58aed8044febe885935b816f32b1348e?s=64&d=mm&r=g) mukesh says:
    
    [April 12, 2016 at 6:10 pm](https://chandoo.org/wp/find-text-pattern/#comment-1167962)
    
    IFERROR(VLOOKUP(MID(B4,IFERROR(FIND(CHAR(77),B4,1),250)-1,2),$H$4:$I$9,2,FALSE),250)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1167962)
    
136.  ![](https://secure.gravatar.com/avatar/ed9f42b96f89c87b5f2bd2a7f4022e9e58aed8044febe885935b816f32b1348e?s=64&d=mm&r=g) mukesh says:
    
    [April 13, 2016 at 2:47 pm](https://chandoo.org/wp/find-text-pattern/#comment-1168247)
    
    \=VLOOKUP(TRIM(RIGHT(TRIM(SUBSTITUTE(SUBSTITUTE(B4,"x",""),RIGHT(SUBSTITUTE(B4,"x",""),5),"")),3)),$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1168247)
    
137.  ![](https://secure.gravatar.com/avatar/750c4fbed9366ef0816b04f3ff1cd200530ec54b9269bfd0640179200dd2b372?s=64&d=mm&r=g) Mohammed says:
    
    [August 1, 2016 at 5:58 am](https://chandoo.org/wp/find-text-pattern/#comment-1243631)
    
    \=IFERROR(VLOOKUP(MID(B4,SEARCH("xx",B4)-3,2),H$3:I$9,2,0),VLOOKUP(MID(B4,SEARCH("xx",B4)-4,3),H$3:I$9,2,0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1243631)
    
138.  ![](https://secure.gravatar.com/avatar/b6558ca3f0ae02c8196db2a4d5a24b7be4f25e8638080a64e878683ee9ee3835?s=64&d=mm&r=g) Nitya Nand Singh says:
    
    [August 5, 2016 at 1:11 pm](https://chandoo.org/wp/find-text-pattern/#comment-1246566)
    
    \=VLOOKUP(TRIM(MID(B4,FIND("xxx",B4)-4,3)),$H$4:$I$10,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1246566)
    
139.  ![](https://secure.gravatar.com/avatar/d60d47e5fc580862287a32bf364704aeb25aabf6b4d3fd6fd16c1954d8dada50?s=64&d=mm&r=g) tushar says:
    
    [August 9, 2016 at 11:44 am](https://chandoo.org/wp/find-text-pattern/#comment-1250559)
    
    \=INDEX($H$4:$I$9,MATCH(TRIM(MID(SUBSTITUTE(B4,"things","thing"),SEARCH("g",SUBSTITUTE(B4,"things","thing"))+1,4)),resTypes,0),2)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1250559)
    
140.  ![](https://secure.gravatar.com/avatar/2feb43842406f2bfa8f650913572a7ecbd7d80ba44483b82b00f54c1c8e7531f?s=64&d=mm&r=g) Ajay Kumar says:
    
    [November 23, 2016 at 12:20 pm](https://chandoo.org/wp/find-text-pattern/#comment-1348846)
    
    \=IFERROR(INDEX(resRates,MATCH(TRIM(RIGHT(LEFT(B4,SEARCH(" xx",B4)),4)),resTypes,0)),"Something went wrong !")
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1348846)
    
141.  ![](https://secure.gravatar.com/avatar/22eb483a2e0cfe6363342a7dcd1a471bf947d5dfe2b9440e3b883479f2c4366e?s=64&d=mm&r=g) Rojo Loco says:
    
    [February 26, 2017 at 7:27 pm](https://chandoo.org/wp/find-text-pattern/#comment-1413839)
    
    I like to use isnumber(search(indirect(....... to enable dynamic changing of the search results and then return a defined dynamic result (such as the cell being searched or the term searched for). This enables changing of the search term without changing the formula. In this case the search term is then used for a simple index match.
    
    1 row of formulas:  
    Resource Description am pm fm cm rm cxo Billing Code Billing Rate Correct Answers  
    Nothing CM xxxx4607 =IF(ISNUMBER(SEARCH(INDIRECT("$C$3"),$B4)),$C$3,"") =IF(ISNUMBER(SEARCH(INDIRECT("$d$3"),$B4)),$D$3,"") =IF(ISNUMBER(SEARCH(INDIRECT("$e$3"),$B4)),$E$3,"") =IF(ISNUMBER(SEARCH(INDIRECT("$f$3"),$B4)),$F$3,"") =IF(ISNUMBER(SEARCH(INDIRECT("$g$3"),$B4)),$G$3,"") =IF(ISNUMBER(SEARCH(INDIRECT("$h$3"),$B4)),$H$3,"") =CONCATENATE(C4,D4,E4,F4,G4,H4) =INDEX(resRates,MATCH(J4,resTypes,0)) 120
    
    Results appear as:  
    Resource Description am pm fm cm rm cxo Billing Code Billing Rate Correct Answers  
    Nothing CM xxxx4607 cm cm 120 120
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1413839)
    
142.  ![](https://secure.gravatar.com/avatar/822de47c867c9cdebab29d80c8627031e77f6b5c7dd2e201683d19e985f7e7dd?s=64&d=mm&r=g) Jayant says:
    
    [June 14, 2017 at 5:01 pm](https://chandoo.org/wp/find-text-pattern/#comment-1461602)
    
    \=VLOOKUP(IF(ISERR(FIND($H$4,B4)),1,1)\*IF(ISERR(FIND($H$5,B4)),1,2)\*IF(ISERR(FIND($H$6,B4)),1,3)\*IF(ISERR(FIND($H$7,B4)),1,4)\*IF(ISERR(FIND($H$8,B4)),1,5)\*IF(ISERR(FIND($H$9,B4)),1,6),$G$4:$I$9,3,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1461602)
    
143.  ![](https://secure.gravatar.com/avatar/a90331faa9c2ded50dc828864e7cdf0fed6be06a3a56e4bcb58b823d59acfdf0?s=64&d=mm&r=g) kapil goyal says:
    
    [July 27, 2017 at 2:09 pm](https://chandoo.org/wp/find-text-pattern/#comment-1486594)
    
    \=IF(COUNTIF(B4,"\*CXO\*")=0,VLOOKUP(MID(B4,FIND("x",B4)-3,2),$H$3:I9,2,0),VLOOKUP(MID(B4,FIND("x",B4)-4,3),$H$3:I9,2,0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1486594)
    
144.  ![](https://secure.gravatar.com/avatar/c1ddcf19801d8521d68d75289603ba1b9e820901b048d361bdef49e3e65aacff?s=64&d=mm&r=g) Barman says:
    
    [August 4, 2017 at 7:40 am](https://chandoo.org/wp/find-text-pattern/#comment-1492053)
    
    nested if:  
    \=IF(ISNUMBER(SEARCH($H$4,B4)),$I$4,IF(ISNUMBER(SEARCH($H$5,B4)),$I$5,IF(ISNUMBER(SEARCH($H$6,B4)),$I$6,IF(ISNUMBER(SEARCH($H$7,B4)),$I$7,IF(ISNUMBER(SEARCH($H$8,B4)),$I$8,IF(ISNUMBER(SEARCH($H$9,B4)),$I$9,NA))))))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1492053)
    
145.  ![](https://secure.gravatar.com/avatar/f928fa471c4cadd2bbc1f1c3d714e84afd4cabbb2beaa30fe74e26a846b66ce3?s=64&d=mm&r=g) Umakanth Kokkula says:
    
    [August 7, 2017 at 7:41 am](https://chandoo.org/wp/find-text-pattern/#comment-1493568)
    
    This worked for me:  
    \=VLOOKUP(TRIM(RIGHT(TRIM(LEFT(B4,FIND("xxx",B4)-1)),3)),$H$4:$I$9,2,0)
    
    Please correct me if i am wrong. 🙂
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1493568)
    
146.  ![](https://secure.gravatar.com/avatar/9f816465d55273694c479d19e71b70b51b4bac692551d61a1c5ea7d68b59e2da?s=64&d=mm&r=g) PRATEEK KHEMKA says:
    
    [November 16, 2017 at 5:35 pm](https://chandoo.org/wp/find-text-pattern/#comment-1522880)
    
    This worked for me
    
    \=VLOOKUP(MID(B4,FIND("x",B4)-3,2),$H$4:$I$9,2)
    
    Thank You
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1522880)
    
147.  ![](https://secure.gravatar.com/avatar/9dc7ff6ddbdfa23a5304c6b278e705fe3636ed03071e5fba15db335a91bf4da8?s=64&d=mm&r=g) Yves S says:
    
    [November 30, 2017 at 4:03 am](https://chandoo.org/wp/find-text-pattern/#comment-1525340)
    
    I like these:  
    VLOOKUP:  
    \={VLOOKUP(MATCH(TRUE,IFERROR(FIND(resTypes,B4,1)0,0),0),$G$4:$I$9,3,0)}
    
    or with INDEX(MATCH):  
    \={INDEX(resRates,MATCH(TRUE,IFERROR(FIND(resTypes,B4,1)0,0),0),1)}
    
    I used the FIND function in the resTypes array to return:{#VALUE!;#VALUE!;#VALUE!;TRUE;#VALUE!;#VALUE!}  
    then IFERROR to eliminate #VALUE! error:  
    {0;0;0;TRUE;0;0}  
    then MATCH to locate ID:  
    4
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1525340)
    
148.  ![](https://secure.gravatar.com/avatar/87556b114acd3c44143b37a1b7047379bd9faf96337c7829b3a1adbcb8001670?s=64&d=mm&r=g) Prem says:
    
    [January 17, 2018 at 5:03 pm](https://chandoo.org/wp/find-text-pattern/#comment-1532376)
    
    this syntax give you value, but changing value by manually  
    like CM to AM, PM, FM etc.
    
    \=VLOOKUP(SUBSTITUTE(MID($B4,SEARCH("CM",$B4),3)," ",""),$H$4:$I$9,2,0)  
    this syntax works 100%
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1532376)
    
149.  ![](https://secure.gravatar.com/avatar/c4c4eba68eaa00c4c46a85549c134a75ccd356aa8d7b54d41ddf090be0fda4c2?s=64&d=mm&r=g) Madhur says:
    
    [February 19, 2018 at 12:00 pm](https://chandoo.org/wp/find-text-pattern/#comment-1537127)
    
    \=VLOOKUP(SUBSTITUTE(RIGHT(SUBSTITUTE(LEFT(B4,FIND("xx",B4)-1)," ",REPT(" ",LEN(B4))),LEN(B4)\*2)," ",""),$H$4:$I$9,2,0)
    
    This formula works 100% . Just copy the same formula in to your excel sheet
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1537127)
    
150.  ![](https://secure.gravatar.com/avatar/5a885f56e0a46e5d619e7251bd48f043a2973759181cce613e36e26527173abb?s=64&d=mm&r=g) Paul says:
    
    [April 30, 2018 at 1:57 am](https://chandoo.org/wp/find-text-pattern/#comment-1545387)
    
    \=VLOOKUP(MID(B33,AGGREGATE(14,3,SEARCH(resTypes,B33),1),FIND(" x",B33)-AGGREGATE(14,3,SEARCH(resTypes,B33),1)),$H$4:$I$9,2,0)
    
    Not all that elegant, but it works. Use Ctrl+Shift+Enter.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1545387)
    
151.  ![](https://secure.gravatar.com/avatar/b58f660d8fbf6dba9c536b1fda39c88cf9aa3dd0c8e84ba298f0dea21cae2414?s=64&d=mm&r=g) Prem Singh says:
    
    [June 6, 2018 at 4:57 am](https://chandoo.org/wp/find-text-pattern/#comment-1551694)
    
    \=VLOOKUP(LOOKUP(2^15,SEARCH(resTypes,B4),resTypes),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1551694)
    
152.  ![](https://secure.gravatar.com/avatar/9f9d43b2126b5584362ec40e9811ca4cabfcae8332c86eb4f8d17e632d9a458b?s=64&d=mm&r=g) Ashton Morgan says:
    
    [June 24, 2018 at 8:51 pm](https://chandoo.org/wp/find-text-pattern/#comment-1555042)
    
    array formula
    
    {=INDEX(resRates,MATCH(TRUE,(ISNUMBER(FIND(resTypes,B4))),0))}
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1555042)
    
153.  ![](https://secure.gravatar.com/avatar/c4bcf9ed94af3a788fa140a2f0c44f191bf27b65a4206562272a7caaa61a919e?s=64&d=mm&r=g) Rahul saha says:
    
    [July 22, 2018 at 6:00 pm](https://chandoo.org/wp/find-text-pattern/#comment-1566050)
    
    \=VLOOKUP(TRIM(MID(B4,FIND("x",B4,1)-4,4)),$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1566050)
    
154.  ![](https://secure.gravatar.com/avatar/f56c24594692b67bbfc192667b687c477fb91a9d494aea324c50fa072be1803e?s=64&d=mm&r=g) Naz says:
    
    [August 21, 2018 at 2:03 pm](https://chandoo.org/wp/find-text-pattern/#comment-1569686)
    
    \=VLOOKUP(IF(COUNTIF(B4,"\*AM\*"),1,IF(COUNTIF(B4,"\*PM\*"),2,IF(COUNTIF(B4,"\*FM\*"),3,IF(COUNTIF(B4,"\*CM\*"),4,IF(COUNTIF(B4,"\*RM\*"),5,IF(COUNTIF(B4,"\*CXO\*"),6,"")))))),$G$4:$I$9,3)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1569686)
    
155.  ![](https://secure.gravatar.com/avatar/c83cc6fa9fe070eb7d51277ecd40997f87743fa211e39ce50bd1648ae7264325?s=64&d=mm&r=g) BHAGWAN DAS says:
    
    [September 15, 2018 at 8:00 am](https://chandoo.org/wp/find-text-pattern/#comment-1575389)
    
    \=VLOOKUP(TRIM(RIGHT(LEFT(B4,FIND("x",B4)-1),4)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1575389)
    
156.  ![](https://secure.gravatar.com/avatar/99270fa0a3c23898bba5e2b497c07847e6540515d16f4f5f2bddc0ef2b888d13?s=64&d=mm&r=g) Abhishek says:
    
    [November 27, 2018 at 7:08 am](https://chandoo.org/wp/find-text-pattern/#comment-1595500)
    
    formula
    
    \=VLOOKUP(TRIM(MID(B4,FIND("xx",B4,1)-4,3)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1595500)
    
157.  ![](https://secure.gravatar.com/avatar/7469b09b3ddcf213a9456f27ff4207d6a5fb181200cdc89ed7eaab0d21c9aec7?s=64&d=mm&r=g) cnestg8r says:
    
    [November 27, 2018 at 6:40 pm](https://chandoo.org/wp/find-text-pattern/#comment-1595801)
    
    \=INDEX(resRates,MATCH(TRIM(MID(B4,FIND(" xx",B4)-3,3)),resTypes,0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1595801)
    
158.  ![](https://secure.gravatar.com/avatar/ab727266093bdf84361e84250648539fcd97d842d7074ab581589fa666d1f346?s=64&d=mm&r=g) abhishek says:
    
    [January 27, 2019 at 12:53 pm](https://chandoo.org/wp/find-text-pattern/#comment-1617473)
    
    1\. Add new column(E): =MID(B4,SEARCH(" x",B4)-3,3)  
    2\. second column(F): =IF(LEFT(E4,1) = " ",RIGHT(E4,2),RIGHT(E4,3))  
    3.billing rate(C) : =INDEX(resRates,MATCH(F4,resTypes,FALSE))
    
    INDEX (H:J)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1617473)
    
159.  ![](https://secure.gravatar.com/avatar/aa86b2612d50a9260c093fb0ef04305fa8f973171ef55ce28c6ee8c611da87ab?s=64&d=mm&r=g) Sushil Kumar says:
    
    [April 11, 2019 at 7:05 am](https://chandoo.org/wp/find-text-pattern/#comment-1636928)
    
    \=VLOOKUP(INDEX($H$4:$H$9,MATCH(TRUE,ISNUMBER(SEARCH($H$4:$H$9,B4)),0)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1636928)
    
160.  ![](https://secure.gravatar.com/avatar/99bbf3795f205cda3ffa9bdff91782a7cac1cf30e97552440f7f36638d3ea68c?s=64&d=mm&r=g) AMIT KATHAR says:
    
    [May 10, 2019 at 4:26 pm](https://chandoo.org/wp/find-text-pattern/#comment-1646191)
    
    I liked the =LOOKUP(20000,SEARCH(resTypes,B4),resRates) solution the most. please see below my conventional formula  
    \=VLOOKUP(TRIM(RIGHT(MID(B4,1,FIND("^",SUBSTITUTE(B4," ","^^",LEN(B4)-LEN(SUBSTITUTE(B4," ",""))))-1),3)),$H$4:$I$9,2,FALSE)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1646191)
    
161.  ![](https://secure.gravatar.com/avatar/07128921eedc846ed82cf9141a1604a6c9f8d5997e851624df1f1f1ca6a36feb?s=64&d=mm&r=g) SUJAY says:
    
    [June 3, 2019 at 11:59 am](https://chandoo.org/wp/find-text-pattern/#comment-1652890)
    
    \=VLOOKUP(TRIM(MID($B4,IFERROR(FIND($K$4,$B4,1),1)\*IFERROR(FIND($K$5,$B4,1),1)\*IFERROR(FIND($K$6,$B4,1),1)\*IFERROR(FIND($K$7,$B4,1),1)\*IFERROR(FIND($K$8,$B4,1),1)\*IFERROR(FIND($K$9,$B4,1),1),3)),$K$4:$L$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1652890)
    
162.  ![](https://secure.gravatar.com/avatar/c7c2c5108e6faa90132f5ae546af21f7d704b9378cc72b8dd22803c808e42b0b?s=64&d=mm&r=g) Jagdish Nathumal Utwani says:
    
    [October 21, 2019 at 6:03 pm](https://chandoo.org/wp/find-text-pattern/#comment-1699520)
    
    \=IF(COUNTIF(B4,"\*CM\*"),120,IF(COUNTIF(B4,"\*PM\*"),60,IF(COUNTIF(B4,"\*FM\*"),75,IF(COUNTIF(B4,"\*RM\*"),150,IF(COUNTIF(B4,"\*CXO\*"),250,IF(COUNTIF(B4,"\*AM\*"),50,""))))))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1699520)
    
    *   ![](https://secure.gravatar.com/avatar/c7c2c5108e6faa90132f5ae546af21f7d704b9378cc72b8dd22803c808e42b0b?s=64&d=mm&r=g) Jagdish Nathumal Utwani says:
        
        [October 21, 2019 at 6:04 pm](https://chandoo.org/wp/find-text-pattern/#comment-1699521)
        
        \=IF(COUNTIF(B4,"\*CM\*"),120,IF(COUNTIF(B4,"\*PM\*"),60,IF(COUNTIF(B4,"\*FM\*"),75,IF(COUNTIF(B4,"\*RM\*"),150,IF(COUNTIF(B4,"\*CXO\*"),250,IF(COUNTIF(B4,"\*AM\*"),50,""))))))
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1699521)
        
163.  ![](https://secure.gravatar.com/avatar/a8a26b9486724a8b8e1b58f4c580db09507d0e29ebd03e213f4b7cb68d3cd3e6?s=64&d=mm&r=g) [HARISH KUMAR](http://n/A)
     says:
    
    [October 22, 2019 at 10:57 am](https://chandoo.org/wp/find-text-pattern/#comment-1699765)
    
    HI ,  
    IS THAT THE PERFECT SOLUTION OF THIS , I HAVE SOME SOLUTION OF THAT PROBLEM
    
    \=VLOOKUP(TRIM(MID(B4,FIND("x",B4)-4,3)),rate,2,0)
    
    TRIM()= REMOVE THE WHITE SPACES.  
    MID=FIND X CHAR IN STRING.  
    RATE=THIS IS THE NAME OF RANGE WHICH HAVE RATE AND TYPE.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1699765)
    
164.  ![](https://secure.gravatar.com/avatar/dcd1ed50f4424f1c4334c5e21701a4248b44d881383f58110def116d5c9b3c56?s=64&d=mm&r=g) Rafal says:
    
    [December 20, 2019 at 7:56 am](https://chandoo.org/wp/find-text-pattern/#comment-1722715)
    
    Hi,
    
    I have come up with this:  
    \=INDEX($D$4:$D$33;MATCH("\*" & H4 & "\*";$B$4:$B$33;0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1722715)
    
165.  ![](https://secure.gravatar.com/avatar/2e6012c305f442cd730c8c1ce23d64785ede19aaebc2865485c59bacad94f975?s=64&d=mm&r=g) Sushmita Bhar says:
    
    [January 21, 2020 at 6:41 am](https://chandoo.org/wp/find-text-pattern/#comment-1731418)
    
    \=INDEX(resRates,MATCH(TRIM(RIGHT(SUBSTITUTE(LEFT(B4,FIND("x",B4)-2)," ",REPT(" ",100)),100)),resTypes,0))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1731418)
    
166.  ![](https://secure.gravatar.com/avatar/5926e170559d480a0e690501f82eb781747af722de284d3a53840bd7e7797e7f?s=64&d=mm&r=g) adam says:
    
    [April 3, 2020 at 4:53 am](https://chandoo.org/wp/find-text-pattern/#comment-1770859)
    
    \=Vlookup(mid(original text,find(" ",original text,find(" ",original text)+1)-find(" ",original text)-1),Range To look in,2,False)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1770859)
    
167.  ![](https://secure.gravatar.com/avatar/659bfc24a6d447f88c9b8e921ca0cb6b680c189bba05d938077987cce316af4c?s=64&d=mm&r=g) Christian M says:
    
    [December 5, 2020 at 8:36 pm](https://chandoo.org/wp/find-text-pattern/#comment-1940753)
    
    Here is my formula.  
    \=XLOOKUP(TRIM(MID(B4,FIND("x",B4) -4,3)),resTypes,resRates,0,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1940753)
    
168.  ![](https://secure.gravatar.com/avatar/5560dd2d38a90a77e37656a72bb929972921176601a1851b5018de1dc62c6c3b?s=64&d=mm&r=g) Anonymous Coward says:
    
    [December 29, 2020 at 1:48 am](https://chandoo.org/wp/find-text-pattern/#comment-1952334)
    
    \=MMULT(--ISNUMBER(SEARCH(TRANSPOSE(resTypes),B4:B33)),resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1952334)
    
169.  ![](https://secure.gravatar.com/avatar/5563b25096da8bddf8d1d8666341c49704b7e539f6ddf9d5a708ac215fe813d8?s=64&d=mm&r=g) Pushpendra Saini says:
    
    [February 5, 2021 at 1:28 pm](https://chandoo.org/wp/find-text-pattern/#comment-1973544)
    
    1\. used text to columns to separate each text given in 'Resource Description' column.  
    2\. Now in each separated columns used vlookup function to see if there is a resource code in a cell, otherwise it will show #N/A error.  
    3\. removed all n/a errors with a alphabet(lets consider "y") that is not in resource code.  
    4\. concatenated all cells form separated columns and used substitute function to remove that "y" and we got pure codes  
    5\. used again vlookup function to get the billing rate
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1973544)
    
170.  ![](https://secure.gravatar.com/avatar/96c0ea67eeb845c38f20f52a5c80cc4293be86cda20cd5d2a1e54775a44dd64d?s=64&d=mm&r=g) zack9400 says:
    
    [April 11, 2021 at 11:04 am](https://chandoo.org/wp/find-text-pattern/#comment-1992451)
    
    I have two solutions :
    
    first one : =LOOKUP(SUM(IFERROR(FIND(resTypes;B4);0));SEARCH(resTypes;B4);resRates)
    
    second one :  
    \=INDEX($I$4:$J$9;MATCH(TRIM(INDEX(MID(B4;SUM(IFERROR(SEARCH(resTypes;B4;LEN(resTypes));0));LEN(resTypes));ROWS(resTypes)));resTypes;0);2)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-1992451)
    
171.  ![](https://secure.gravatar.com/avatar/db364b2b353295561c79fcdef4df1130425dd332344fa295f774dad7da012caf?s=64&d=mm&r=g) Lego says:
    
    [May 19, 2021 at 4:44 pm](https://chandoo.org/wp/find-text-pattern/#comment-2000870)
    
    \=INDEX(resRates,AGGREGATE(15,6,(ROW(resTypes)-ROW($H$3))/ISNUMBER(SEARCH(resTypes,B4)),1))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2000870)
    
172.  ![](https://secure.gravatar.com/avatar/f13760716d1aa1db6ef6b9240d362443365f6c0832ea30aa9e9eb45400a21489?s=64&d=mm&r=g) Rolan Reynacido says:
    
    [June 21, 2021 at 8:05 am](https://chandoo.org/wp/find-text-pattern/#comment-2007647)
    
    \=VLOOKUP(TRIM(MID($B4,FIND("xx",$B4)-4,3)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2007647)
    
    *   ![](https://secure.gravatar.com/avatar/75e5fd0859f1ebc73658e65bbe18cdb2782cef8f58926cb8c8079149f5cba139?s=64&d=mm&r=g) Adhy says:
        
        [June 5, 2023 at 5:47 am](https://chandoo.org/wp/find-text-pattern/#comment-2129072)
        
        This one works really well.
        
        [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2129072)
        
173.  ![](https://secure.gravatar.com/avatar/9b9c80afdf5a99b09b59cd5ab24d546370ff3212798353d4b90eb9e9ad34e7e4?s=64&d=mm&r=g) Bhu says:
    
    [May 15, 2022 at 10:50 am](https://chandoo.org/wp/find-text-pattern/#comment-2077464)
    
    \=VLOOKUP(TRIM(TEXTJOIN("",TRUE,IFERROR(MID(B4,SEARCH(resTypes,B4,1),3),""))),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2077464)
    
174.  ![](https://secure.gravatar.com/avatar/6cf7f6c25026e963fc67b581817c92a0d275e723c7f89a1503c8ac1938bea924?s=64&d=mm&r=g) Jaime says:
    
    [December 20, 2022 at 12:05 am](https://chandoo.org/wp/find-text-pattern/#comment-2112381)
    
    BUSCARV(ESPACIOS(EXTRAE(B4,ESPACIOS(HALLAR("xx",B4)-4),3)),idbilling,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2112381)
    
175.  ![](https://secure.gravatar.com/avatar/db364b2b353295561c79fcdef4df1130425dd332344fa295f774dad7da012caf?s=64&d=mm&r=g) Rob says:
    
    [April 12, 2023 at 10:10 pm](https://chandoo.org/wp/find-text-pattern/#comment-2125002)
    
    Using the new functions.
    
    \=XLOOKUP(REDUCE(TEXTSPLIT(B4,," "),{-2,1},LAMBDA(s,c,TAKE(s,c))),resTypes,resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2125002)
    
176.  ![](https://secure.gravatar.com/avatar/9d56bc4320b1ad5959c2ba34d331ec276153018da1df0c5fd87c2622825ca055?s=64&d=mm&r=g) [Sohan Advani](http://sohanadvani.com/)
     says:
    
    [April 29, 2023 at 8:18 am](https://chandoo.org/wp/find-text-pattern/#comment-2126362)
    
    \=VLOOKUP(TRIM(MID(B4,FIND("x",B4,1)-4,4)),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2126362)
    
177.  ![](https://secure.gravatar.com/avatar/75e5fd0859f1ebc73658e65bbe18cdb2782cef8f58926cb8c8079149f5cba139?s=64&d=mm&r=g) Adhy says:
    
    [June 5, 2023 at 5:39 am](https://chandoo.org/wp/find-text-pattern/#comment-2129070)
    
    I got it right, but it's silly long.
    
    \=VLOOKUP(IF(MID(B4;SEARCH("xx";B4;1)-3;2)="XO";"CXO";MID(B4;SEARCH("xx";B4;1)-3;2));$H$4:$I$9;2;0)
    
    I first started with a SEARCH function for "xx" and then -3 to get the 2-digit code (CM, AM, etc). And then encapsulated like within an IF if the result was XO. If it was XO, then I'd change it to "CXO".
    
    From there, you put that entire thing inside a VLOOKUP function to get your billing amount.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2129070)
    
178.  ![](https://secure.gravatar.com/avatar/0c57ffda5ecac01d95a21fe37d3ffea96c7192c1584f12846763bf7ba5a943c0?s=64&d=mm&r=g) Mahmoud says:
    
    [July 22, 2023 at 11:31 pm](https://chandoo.org/wp/find-text-pattern/#comment-2134402)
    
    \=VLOOKUP(TRIM(CLEAN(MID(B4 FIND("x" B4)-4,3)\]),$H$4:$1$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2134402)
    
179.  ![](https://secure.gravatar.com/avatar/2eb59413ebfdcc25f95bdeff01e1b0f6952d9b7fe1332dd7628a058a20ca8a00?s=64&d=mm&r=g) Pranav Dave says:
    
    [September 14, 2023 at 10:43 am](https://chandoo.org/wp/find-text-pattern/#comment-2142931)
    
    \=VLOOKUP(TRIM(CLEAN(MID(B4,FIND("x",B4)-4,3))),$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2142931)
    
180.  ![](https://secure.gravatar.com/avatar/168201139c9b97e9f63b58f1e1da8ac2f99ab2e18e9ad5af3874110d4c281fe1?s=64&d=mm&r=g) [Paul Behanna](http://www.pnmtabsllc.com/)
     says:
    
    [November 22, 2023 at 7:47 pm](https://chandoo.org/wp/find-text-pattern/#comment-2153662)
    
    \=XLOOKUP(TRIM(MID(B4,(FIND(" x",B4)-3),3)),resTypes,resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2153662)
    
181.  ![](https://secure.gravatar.com/avatar/2501c61332e71f8032cf3edb8eb80a39d029f7cf67d35f81029036d4a26484d3?s=64&d=mm&r=g) APC says:
    
    [December 16, 2023 at 11:54 pm](https://chandoo.org/wp/find-text-pattern/#comment-2157569)
    
    This works  
    \=SUM(IF(IF(ISNUMBER(SEARCH(resTypes,B4)),1,0),resRates,""))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2157569)
    
182.  ![](https://secure.gravatar.com/avatar/8792f74b62f4fa11944c36dbc7e1c9b9388e94cf90e707925d3df9c082cc7a48?s=64&d=mm&r=g) Rahul Bhadrecha says:
    
    [January 29, 2024 at 9:23 am](https://chandoo.org/wp/find-text-pattern/#comment-2168718)
    
    \=VLOOKUP(TRIM(MID(B3,TEXTJOIN("",TRUE, IFERROR(FIND($H$2:$H$8,B3),"")),3)),$H$2:$I$8,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2168718)
    
183.  ![](https://secure.gravatar.com/avatar/bb079c867fb0a6eaac6001225fbff79d0fbb8c5c41965b3e4192868c3023f9dc?s=64&d=mm&r=g) Hemant Suresh Kamane says:
    
    [February 10, 2024 at 2:50 am](https://chandoo.org/wp/find-text-pattern/#comment-2172114)
    
    \=VLOOKUP(IFERROR(RIGHT(LEFT(B4,FIND("M",B4)),2),RIGHT(LEFT(B4,FIND("XO",B4)+1),3)),$H$3:$I$9,2,0)
    
    Simple !!!
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2172114)
    
184.  ![](https://secure.gravatar.com/avatar/893202bcf726f72aa0db072df3743f1eebdf25658042ca28b57a37f3c7e882d1?s=64&d=mm&r=g) Avishek says:
    
    [February 17, 2024 at 4:50 pm](https://chandoo.org/wp/find-text-pattern/#comment-2175919)
    
    The formula is-  
    \=IF(COUNTIF(B4,"\*AM\*"),50,IF(COUNTIF(B4,"\*PM\*"),60,IF(COUNTIF(B4,"\*FM\*"),75,IF(COUNTIF(B4,"\*CM\*"),120,IF(COUNTIF(B4,"\*RM\*"),150,IF(COUNTIF(B4,"\*CXO\*"),250,""))))))
    
    Just drag it and see the magic.
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2175919)
    
185.  ![](https://secure.gravatar.com/avatar/9871ebda2f155975df09a0e3859ab97316645ef20decfb2282509cb17526a014?s=64&d=mm&r=g) Ali says:
    
    [March 17, 2024 at 9:16 am](https://chandoo.org/wp/find-text-pattern/#comment-2195872)
    
    \=XLOOKUP(LOOKUP(1000,SEARCH(resTypes,B4),resTypes),resTypes,resRates,"",0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2195872)
    
186.  ![](https://secure.gravatar.com/avatar/4073419b589deabbe067d75225f0a5c04081e48088bf1619e44b526f1aee436f?s=64&d=mm&r=g) [suresh sethi](https://suresh95564.blogspot.com/)
     says:
    
    [May 23, 2024 at 6:19 am](https://chandoo.org/wp/find-text-pattern/#comment-2214016)
    
    Answer is tricky i found a simple solution is  
    " =VLOOKUP(TRIM(MID(Description, FIND("x", Description)-4,3)),restable,2,0) "
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2214016)
    
187.  ![](https://secure.gravatar.com/avatar/03775abe4108c91f0f21dd25efc680c277a73298bab9a1a6cb1fec1b2a6ff9b0?s=64&d=mm&r=g) Rampally Vishal Kumar says:
    
    [June 16, 2024 at 5:53 pm](https://chandoo.org/wp/find-text-pattern/#comment-2224018)
    
    i separated the values by flash fill then applied VLOOKUP formula
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2224018)
    
188.  ![](https://secure.gravatar.com/avatar/02bc2c98aa2555b437ff475502785d2d3da68b9a620352c9a8751ce7fa138687?s=64&d=mm&r=g) Amirdha says:
    
    [August 27, 2024 at 12:01 am](https://chandoo.org/wp/find-text-pattern/#comment-2275264)
    
    I used a "Nested If" and "Search" function to solve this problem. Here is my solution:
    
    \=IF(ISNUMBER(SEARCH($H$4, B4)), $I$4, IF(ISNUMBER(SEARCH($H$5, B4)), $I$5, IF(ISNUMBER(SEARCH($H$6, B4)), $I$6, IF(ISNUMBER(SEARCH($H$7, B4)), $I$7, IF(ISNUMBER(SEARCH($H$8, B4)), $I$8, IF(ISNUMBER(SEARCH($H$9, B4)), $I$9, 0))))))
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2275264)
    
189.  ![](https://secure.gravatar.com/avatar/f59977c27d9b6439c54eac40fbf0a67db3ba2148679484ec88755f3eb1e5b48e?s=64&d=mm&r=g) [Gehad Mohammed Hassan](https://youtube.com/@gehadmohammed?si=AYJmBe_Q2u4I69Be)
     says:
    
    [January 4, 2025 at 8:42 pm](https://chandoo.org/wp/find-text-pattern/#comment-2338680)
    
    I have two approaches:  
    \[1\]  
    with three helper columns,  
    the first of them  
    \=FIND("xxx",B4)  
    the second  
    \=FIND(" ",B4,K4-5)  
    the third  
    \=MID(B4,L4,K4-L4)  
    those will give me the types only  
    then I used  
    \=VLOOKUP(TRIM(M4),$H$4:$I$9,2,0)  
    in billing rate column to get the answers  
    \================  
    \[2\] with array formulas  
    I copied the restypes and trasposed them as column headers  
    then copied the range from b4:b33 and paste it as rows of the array  
    then I developed the matrix by this formula  
    {=IFERROR(SEARCH($U$3:$Z$3,$T$4:$T$33),0)}  
    after that I used this formula next to each row of the developed matrix  
    \=SUM(U4:Z4)  
    thus I get the index of the start of each restype in each record and used  
    \=TRIM(MID(T4,AA4,3))  
    to extract only the restypes letters in front of correponding record of the table  
    and used vlookup to get the rate  
    \=VLOOKUP(AB4,$H$4:$I$9,2,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2338680)
    
190.  ![](https://secure.gravatar.com/avatar/a50908e1c2525d668d697415bbde3e5fd58b477a6ffb3b7607211c5be767278e?s=64&d=mm&r=g) Tek Lentine says:
    
    [January 8, 2025 at 6:55 pm](https://chandoo.org/wp/find-text-pattern/#comment-2340280)
    
    \=XLOOKUP("\*"&MID(B4,FIND(" x",B4)-2,2),resTypes,resRates,0,2,1)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2340280)
    
191.  ![](https://secure.gravatar.com/avatar/3741c796e0ddc7a3b044d8639c162b2bd2f1fbe87166ba2642194f2a8d94cdbd?s=64&d=mm&r=g) DK Kim says:
    
    [January 11, 2025 at 1:59 am](https://chandoo.org/wp/find-text-pattern/#comment-2341077)
    
    Here is my answer using the latest excel functions.
    
    \=XLOOKUP(REGEXEXTRACT(B4:B33,TEXTJOIN("|",TRUE,resTypes)),resTypes,resRates)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2341077)
    
192.  ![](https://secure.gravatar.com/avatar/8ac27015ead7f55f7902f0d2391a73b70d5bdb244d9259bdaa498ccb20f11f6f?s=64&d=mm&r=g) Brennen says:
    
    [February 15, 2025 at 4:06 am](https://chandoo.org/wp/find-text-pattern/#comment-2363351)
    
    \=IFERROR(IF(INDEX(resRates,MATCH(TRUE, ISNUMBER(SEARCH(resTypes,$B4)),0))=0, "",INDEX(resRates,MATCH(TRUE, ISNUMBER(SEARCH(resTypes,$B4)),0))),"")
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2363351)
    
193.  ![](https://secure.gravatar.com/avatar/399364aca33fc87cef74fb801e5338856aaa67b14b5fbe79592a04d8a18f3817?s=64&d=mm&r=g) ghaith says:
    
    [April 2, 2025 at 4:51 am](https://chandoo.org/wp/find-text-pattern/#comment-2377988)
    
    \=XLOOKUP(TRUE, ISNUMBER(SEARCH($H$4:$H$9, B4)), $I$4:$I$9)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2377988)
    
194.  ![](https://secure.gravatar.com/avatar/ce0316aaf901183689c493429a627928ee280c4daa1e533183924675f5511fe6?s=64&d=mm&r=g) shahrukh says:
    
    [April 23, 2025 at 1:54 pm](https://chandoo.org/wp/find-text-pattern/#comment-2384493)
    
    \=XLOOKUP(TEXTBEFORE(TEXTAFTER(B4," ",-2)," ",1),$H$4:$H$9,$I$4:$I$9,,0)
    
    [Reply](https://chandoo.org/wp/find-text-pattern/#comment-2384493)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/find-text-pattern/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Highlight best week & month in a trend chart \[tutorials\]](https://chandoo.org/wp/highlight-best-week-month-in-charts/) | [Show hide list boxes using VBA](https://chandoo.org/wp/show-hide-list-boxes-using-vba/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
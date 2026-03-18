# Count unique values in a range?

**Source:** https://chandoo.org/wp/formula-forensics-025

---

Formula Forensics 025. Count Unique Values in a Range
=====================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 , [wonder why](https://chandoo.org/wp/category/wonder-why/)
 - 25 comments

  

This week at the [Chandoo.org Forums](http://chandoo.org/forums/topic/what-is-the-count-of-unique-parties "Unique post")
, Ajinka asked a question about counting unique values in a range.

Faseeh answered with a neat Sumproduct() based formula and quoting a post that Chandoo had written at [Chandoo.org](http://chandoo.org/wp/2009/08/06/count-number-of-unique-cells/)
 answering the question in 2009.

A few people asked how it worked and Luke M gave a good response which I will be plagiarising in part here.

Faseeh’s formula was \=SUMPRODUCT(1/COUNTIF(B2:B8,B2:B8))

As always at Formula Forensics you can follow along using a Worked Example which you can download here: [Excel 97-2013](https://chandoo.org/wp/wp-content/uploads/2012/07/Unique.xls "Unique Sample file")
.

Count Unique Values
-------------------

Faseeh’s formula was \=SUMPRODUCT(1/COUNTIF(B2:B8,B2:B8))

So lets look at how that works

\=SUMPRODUCT(1/COUNTIF(B2:B8,B2:B8))

The formula is a Sumproduct() based formula which tells us that the Sumproduct() function is being used to multiply and addup the component arrays. As there is only 1 array component in our formula, Sumproduct simply adds up the values. You can learn more about the Excel Sumproduct function here: [Formula Forensics 007](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/ "FF007")

The components of the Sumproduct() function are:

1/COUNTIF(B2:B8,B2:B8)

Lets start with the COUNTIF(B2:B8,B2:B8) part

In a blank cell F12 put \=COUNTIF(B2:B8,B2:B8), press F9 instead of Enter  
Excel will respond with \={3;1;2;3;3;2;1}

### What is Countif() doing ?

The Syntax of Countif() is:  
[![](https://chandoo.org/wp/wp-content/uploads/2012/07/FF251.png "FF251")](https://chandoo.org/wp/wp-content/uploads/2012/07/FF251.png)

In our example COUNTIF(B2:B8,B2:B8) the Range and the Criteria are the same Range B2:B8  
So Countif will Look at the Range (B2:B8) and see what matches the criteria in each cell in the Criteria Range (B2:B8), 1 cell at a time.

Lets look at the first few cells in the Criteria and work through them.

The first cell in the Criteria is B2 which contains “ABC”  
We can see that the Range contains the first value in the criteria “ABC”, 3 times  
This is the first 3 in the Array shown above ={**3**;1;2;3;3;2;1}  
[![](https://chandoo.org/wp/wp-content/uploads/2012/07/FF252.png "FF252")](https://chandoo.org/wp/wp-content/uploads/2012/07/FF252.png)

The second cell in the Criteria is B3 which contains “XYZ”  
We can see that the Range contains the second value in the criteria “XYZ”, 1 times  
This is the second element in the Array shown above ={3;**1**;2;3;3;2;1}  
[![](https://chandoo.org/wp/wp-content/uploads/2012/07/FF253.png "FF253")](https://chandoo.org/wp/wp-content/uploads/2012/07/FF253.png)

The third cell in the Criteria is B4 which contains “HML”  
We can see that the Range contains the third value in the criteria “HML”, 2 times  
This is the third element in the Array shown above ={3;1;**2**;3;3;2;1}  
[![](https://chandoo.org/wp/wp-content/uploads/2012/07/FF254.png "FF254")](https://chandoo.org/wp/wp-content/uploads/2012/07/FF254.png)

Stepping through the range and comparing each value in the criteria results in: ={3;1;2;3;3;2;1}

### Reciprocal

The next part of the formula is the  
1/COUNTIF(B2:B8,B2:B8)

This takes the reciprocal of our Array {3;1;2;3;3;2;1}

In a Blank cell **F14** enter \=1/COUNTIF(B2:B8,B2:B8) press **F9** not Enter  
Excel returns: \={0.333;1;0.5;0.333;0.333;0.5;1}  (I have truncated the 0.33333333333 values to save space)  
Which is the same as {1/3; 1/1; 1/2; 1/3; 1/3; 1/2; 1/1}

The Sumproduct() function now steps in and adds up the values of the array returning the answer **4**.

### Summary

So generically if a value occurs T times in the range, it will occur T times in the criteria.

This will return the value T, T times. The smart bit here is taking the reciprocal of the Count.  
So this means it will return the value T, 1/T times.

So ultimately T x (1/T) = 1.

You can see from the above it doesn’t matter how many times a value occurs, every unique value will be seen as 1 and then added up by Sumproduct

Download
--------

You can download a copy of the above file and follow along, [Download Here Excel 97-2013](https://chandoo.org/wp/wp-content/uploads/2012/07/Unique.xls "Unique Sample file")
.

Formula Forensics “The Series”
------------------------------

This is the 25th or Silver Anniversary Post in the Formula Forensics series and was the first Formula Forensics completely developed in the new Office 2013.  
You can learn more about how to pull Excel Formulas apart in the following posts  
[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics Series")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.  
If you have a neat formula that you would like to share as Jong has done above, try putting pen to paper and draft up a Post like above or;  
If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "Contact Chandoo")
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
| Written by Hui...  <br>Tags: [countif()](https://chandoo.org/wp/tag/countif/)<br>, [sumproduct](https://chandoo.org/wp/tag/sumproduct/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 25 Responses to “Formula Forensics 025. Count Unique Values in a Range”

1.  ![](https://secure.gravatar.com/avatar/b83256a20df2a732aa8fdfd5607ba34d5be6a67bee307659c24322371330b736?s=64&d=mm&r=g) Dohsan says:
    
    [July 26, 2012 at 9:57 am](https://chandoo.org/wp/formula-forensics-025/#comment-227731)
    
    I saw this in the original thread and thought it was very cheeky little formula! One thing I did notice though was that it will return #DIV/0! error if any blanks are present in the list.
    
    I played around and managed to get the following to work
    
    {=SUMPRODUCT(IF(A1:A10<>"",1/COUNTIF(A1:A10,A1:A10),0)) }
    
    Only issue is that it then becomes an array formula.
    
    I then stumbled across this on another forum, which doesn't need to be entered as an array
    
    \=SUMPRODUCT((A1:A10<>"")/COUNTIF(A1:A10,A1:A10&""))
    
    Interesting behaviour of COUNTIF, where a blank will return 1 if you were to use COUNTIF(A1,A1&"")
    
    Original thread was here, explains it far better than I could attempt:
    
    [http://www.mrexcel.com/forum/showthread.php?70835-Count-distinct-function](http://www.mrexcel.com/forum/showthread.php?70835-Count-distinct-function)
      
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227731)
    
    *   ![](https://secure.gravatar.com/avatar/e1f3759531553673c134f5d49ed8dbe431ce8be5af6dd4931314fc13e214b19e?s=64&d=mm&r=g) [Oscar](http://www.get-digital-help.com/)
         says:
        
        [July 27, 2012 at 8:29 am](https://chandoo.org/wp/formula-forensics-025/#comment-227788)
        
        The formula =SUMPRODUCT((A1:A10<>”")/COUNTIF(A1:A10,A1:A10&”")) is really interesting!
        
        You can use the same technique to extract unique distinct values if blanks are present in the list!  
        **Array formula in cell B2:**  
        \=INDEX($A$1:$A$10, MATCH(0, COUNTIF($B$1:B1,  $A$1:$A$10&""),0))  
        Copy cell B2 and paste down as far as needed.
        
        [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227788)
        
2.  ![](https://secure.gravatar.com/avatar/a8f247e2cbe20bb3f03aa959b837b5ed676ea1c5bb8998c92a24233c043cf422?s=64&d=mm&r=g) Jon says:
    
    [July 26, 2012 at 10:39 am](https://chandoo.org/wp/formula-forensics-025/#comment-227732)
    
    That just blew my mind!!!!!
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227732)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 26, 2012 at 10:46 am](https://chandoo.org/wp/formula-forensics-025/#comment-227733)
        
        @Jon  
        I hope you enjoy the rest of the [Formula Forensics Series](http://chandoo.org/wp/category/formula-forensics/ "FF Series")
        
        🙂
        
        [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227733)
        
3.  ![](https://secure.gravatar.com/avatar/1738041b93739c94f8ef89076615ff4e4b16fa9af6352d48020835f0c01229a1?s=64&d=mm&r=g) Kevin says:
    
    [July 26, 2012 at 11:12 am](https://chandoo.org/wp/formula-forensics-025/#comment-227734)
    
    Why do people hate the DCOUNT function.
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227734)
    
    *   ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
        
        [July 26, 2012 at 12:29 pm](https://chandoo.org/wp/formula-forensics-025/#comment-227740)
        
        What makes you say that Kevin? DCOUNT is for use with a database (which requires headers) and is also limited to just counting numbers (not text). This article is about counting unique values. 
        
        [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227740)
        
        *   ![](https://secure.gravatar.com/avatar/1738041b93739c94f8ef89076615ff4e4b16fa9af6352d48020835f0c01229a1?s=64&d=mm&r=g) Kevin says:
            
            [July 26, 2012 at 5:49 pm](https://chandoo.org/wp/formula-forensics-025/#comment-227755)
            
            DCOUNTA counts text. Isn't Cells A1. C8 a database.
            
            [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227755)
            
            *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
                
                [July 26, 2012 at 9:42 pm](https://chandoo.org/wp/formula-forensics-025/#comment-227766)
                
                There's more than one way to skin a cat, as the saying goes. Each with advantages and disadvandages.  
                The 'D' functions are definately underused, but because they need to reference a criteria range stored in the spreadsheet somewhere, you can't easily pop in a D function somewhere and then fill down in the same way as you can with other functions. The reason is because each D function occupies one row, but the criteria they reference must occupy at least 2 rows. Hard to visualise, harder still to explain. And while there are workarounds to this, they require quite a bit of trickery.  
                   
                 So D functions tend to be more helpful if you're only interested in answering one question based on just one criteria as in this case. If you need lots of formulas to answer questions based on a whole heap of criteria, they are not so helpful.  
                   
                I'm going to quote from my clever pal Sam:  
                _The "D" Functions (DSUM, DCOUNT etc) in Excel are often underused._  
                _A common complaint among users is that you cant drag it down.... Well you can ...but it's tricky._   
                   
                _D function advantages_  
                _1.Speed - Faster than SP (but slower than SUMIF/s and CountIF/s)_
                
                _2.Can handle both AND and OR like SP_
                
                _3.Can handle Wild cards \*,? directly_  
                _4\. Can be dragged down like SP when used along with the SUM function as DSUM-SUM_  
                _5\. Can handle multiple OR criteria in a much better way than SP_  
                   
                _Disadvantages_  
                _1\. The default operator is String\* and not Equals (Like in Advance Filter)_  
                _2\. If you want to use the Equals operator - it has to be explicitly specified like '=String_  
                _3\. Cant handle row and column criteria_  
                _4\. Not as Flexible as SP_  
                _5\. Cant Replicate COUNTIF(s)(Rng,Rng)_
                
                [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227766)
                
4.  ![](https://secure.gravatar.com/avatar/ff8548dffe18eb441ca20b0b8641da8417ed968470565511fb69e0dca4377c4d?s=64&d=mm&r=g) David K says:
    
    [July 26, 2012 at 1:46 pm](https://chandoo.org/wp/formula-forensics-025/#comment-227745)
    
    \=IF(SUMPRODUCT(($A$2:$A2=A2)\*($C$2:$C2=C2))>1,0,1)  
    _Drag down to expand the Range_  
    I use this formula for 2 variables uniqueness.  
    Col A has is a Company and Col C is who is assigned to company.  
    This allows me to quickly Sum up the number of Unique Reps assigned to a Company.  
       
    _\*I forgot the source where I got this from but I'll attach it later if I find it._  
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227745)
    
5.  ![](https://secure.gravatar.com/avatar/be0942581ecf6840ea793380b8ea9cc3b0c55d1890674298d87ad1ac87d70b0c?s=64&d=mm&r=g) shrivallabha says:
    
    [July 26, 2012 at 5:19 pm](https://chandoo.org/wp/formula-forensics-025/#comment-227752)
    
    You can also use:  
    \=SUM((FREQUENCY(B2:B8,B2:B8)>0)+0)  
    for numerical data  
    and  
    \=SUM((FREQUENCY(MATCH(B2:B8,B2:B8,0),MATCH(B2:B8,B2:B8,0))>0)+0)  
    for non-numerical data!  
    MATCH needs to be added to non-numerical cases due to the fact that FREQUENCY works with numbers only.
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227752)
    
6.  ![](https://secure.gravatar.com/avatar/7008f4f444a2e70ffb5f5b2287371948c6bbe97fdc31baab12a9bab083088199?s=64&d=mm&r=g) Noah Helenihi says:
    
    [July 26, 2012 at 6:24 pm](https://chandoo.org/wp/formula-forensics-025/#comment-227757)
    
    Awsesome, as usual! But, what if you want to then _list_ the values? Say, you want to identify all of the unique values so you can display counts by unique values or percentage of transactions to unique values . . . Is there a simple formula you can use to pull these unique values out of the range and then list them on the side (likely an array formula)?
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227757)
    
    *   ![](https://secure.gravatar.com/avatar/b83256a20df2a732aa8fdfd5607ba34d5be6a67bee307659c24322371330b736?s=64&d=mm&r=g) Dohsan says:
        
        [July 27, 2012 at 7:28 am](https://chandoo.org/wp/formula-forensics-025/#comment-227781)
        
        Hi Noah,
        
        If you want a distinct list (i.e. show all the values in a list once)
        
        then you can use the following:
        
        \=IFERROR(INDEX(List,MATCH(0,IF(ISBLANK(List),"",COUNTIF($B$1:B1,List)),0)),"")
        
        Assuming your data is in column A setup a named ranged called List and then enter this in B2, enter as an array and drag down. 
        
        If you want a unique list (Only list the values that appear once in the list) then you can use:
        
        \=IFERROR(INDEX(List, MATCH(0, COUNTIF($C$1:C1, List)+(COUNTIF(List, List)<>1), 0)),"")
        
        Put that in C2 as an array and drag down 
        
        [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227781)
        
7.  ![](https://secure.gravatar.com/avatar/7008f4f444a2e70ffb5f5b2287371948c6bbe97fdc31baab12a9bab083088199?s=64&d=mm&r=g) Noah Helenihi says:
    
    [July 26, 2012 at 6:29 pm](https://chandoo.org/wp/formula-forensics-025/#comment-227759)
    
    One more question . . . what are the pros/cons of using the "Countif" formulation versus a "Sum/Frequency" formulation to do the same thing? And, why don't they just create a "CountUnique" formula?
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227759)
    
8.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
    
    [July 26, 2012 at 9:44 pm](https://chandoo.org/wp/formula-forensics-025/#comment-227767)
    
    Great formula, great explanation. Well done, Hui.
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227767)
    
9.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [July 28, 2012 at 5:32 am](https://chandoo.org/wp/formula-forensics-025/#comment-227837)
    
    @Jeff.
    
    6\. The D Functions handle Formulas in the Criteria (just like Adv Filter)  
    The Rules for Formula criteria remain the same as Advanced Filters.
    
    1\. The Headings of the Criteria should be different from the Data  
    2\. Some where in the formula you must refer to the first cell in the Column you want to SUM/COUNT etc. That reference should be relative. All other range references should be absolute.
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227837)
    
10.  ![](https://secure.gravatar.com/avatar/d68368c2758a908cbaafd82cea650abd38422d92a8afad2fe51913c321ede50f?s=64&d=mm&r=g) ahamed says:
    
    [July 28, 2012 at 5:38 am](https://chandoo.org/wp/formula-forensics-025/#comment-227838)
    
    First I would like to take this opportunity to thank Chandoo.org for bringing up this post.   
    Another issue that I have always been facing for long time is to find a simple formula to extract those unique items (parties) into different cells.   
    Now we know according to the given formula we have 4 unique parties, how can we extract these unique parties into different cells from the list. (Ex: ABC,XYZ,HML,NKY)  
    During the course of developing a dash boards I frequently face these kinds of issues where I have a huge set of data of which certain items repeat.  
    Now I want to find and list out in separate cells these unique items and their totals, from which the "items and values" are again taken into the dash board on rank basis (ex- top 5 etc)  
    Pls advice me
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227838)
    
11.  ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David Hager says:
    
    [July 29, 2012 at 4:08 am](https://chandoo.org/wp/formula-forensics-025/#comment-227896)
    
    For those who might be interested in what was written on this subject 13 years ago see:[](http://www.j-walk.com/ss/excel/eee/eee004.txt)
    
    [](http://www.j-walk.com/ss/excel/eee/eee004.txt)
    
      [](http://www.j-walk.com/ss/excel/eee/eee004.txt)
    [http://www.j-walk.com/ss/excel/eee/eee004.txt](http://www.j-walk.com/ss/excel/eee/eee004.txt)
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-227896)
    
    *   ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) Sajan says:
        
        [August 2, 2012 at 10:08 pm](https://chandoo.org/wp/formula-forensics-025/#comment-228236)
        
        Thanks David.  That site is a treasure trove of Excel gems!
        
        \-Sajan.
        
        [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-228236)
        
12.  ![](https://secure.gravatar.com/avatar/e05d1bb8e50d63dbe9b9d76135b15ee596a185ba885cfb486b592196cbca8c30?s=64&d=mm&r=g) Jordan says:
    
    [August 6, 2012 at 2:40 pm](https://chandoo.org/wp/formula-forensics-025/#comment-228435)
    
    Hi, I have been able to make this formula work, but! i have an added twist that i'm having difficulty with. In my case, i would like to find the unique value whether a certain criteria is found in 2 different columns. I think of it instead of look at column 1 and 2 to see if there are unique volumes in column 3, i would like it two say column 1 or 2 meets a criteria make sure column 3 is unique.
    
    I hope this explains properly.
    
    One more try, Im looking up unique values for 2 whether found in column B or C. Therefore the count should come back only 1:
    
    Jan  2  3  
    Jan 3   2  
    Jan  2  3
    
    Thanks!  
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-228435)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [August 7, 2012 at 2:09 am](https://chandoo.org/wp/formula-forensics-025/#comment-228445)
        
        I am not sure I understand this. Can you explain your problem again or send me your workbook? My email address is here: [http://chandoo.org/wp/contact/](http://chandoo.org/wp/contact/)
        
        [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-228445)
        
        *   ![](https://secure.gravatar.com/avatar/e05d1bb8e50d63dbe9b9d76135b15ee596a185ba885cfb486b592196cbca8c30?s=64&d=mm&r=g) Jordan says:
            
            [August 7, 2012 at 4:04 pm](https://chandoo.org/wp/formula-forensics-025/#comment-228486)
            
            Yes sorry, difficult for me to explain. And now that i notice this posting wasnt really on counting uniques based on multiple criteria. I first found the formula here: [http://www.get-digital-help.com/2011/07/12/count-unique-distinct-values-that-meet-multiple-criteria-in-excel/](http://www.get-digital-help.com/2011/07/12/count-unique-distinct-values-that-meet-multiple-criteria-in-excel/)
            
            But then i found this post and went with stream of thought and blurted out the question. I would like to find the unique values whether a criteria is met in column b or c, while the formula mentioned in the link is if something is found in both.
            
            Apologies for hi-jacking thread.
            
            [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-228486)
            
13.  ![](https://secure.gravatar.com/avatar/c39e0361722fb9e859326748bd0abba004ee9ab925b6017f84a7bf82918081de?s=64&d=mm&r=g) Alfredo says:
    
    [December 9, 2014 at 7:24 pm](https://chandoo.org/wp/formula-forensics-025/#comment-870517)
    
    I have to process a list every day, it does not have blank values but instead its length changes every time; the staff wants to see that list on top of the report and then the summary so I have a fixed amount of rows at top and then just hide what any blank rows after pasting the data from an external DB.
    
    I am using another formula to count unique values (I will use range A1:A200) as an example:
    
    {=SUM(IF(FREQUENCY(IF(LEN(A2:A200)>0,MATCH(A2:A200,A2:A200,0),""),IF(LEN(A2:A200)>0,MATCH(A2:A200,A2:A200,0),""))>0,1))}
    
    I like the formula posted here as it's simpler but it will not take the blank rows at the bottom without throwing an error, so what I did is to use the dynamic range approach (that I also learned here at chandoo.org) and it looks like this:
    
    \=SUMPRODUCT(1/COUNTIF(INDIRECT("A2:A"&COUNTA(A2:A200)),INDIRECT("A2:A"&COUNTA(A2:A200))))
    
    Next I will like filter the list to count (unique values that meet certain criteria in other columns) I will appreciate any ideas 🙂
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-870517)
    
14.  ![](https://secure.gravatar.com/avatar/ab7ea4d7341d1b30cd8eb344d521df9d9b90c01f2db82e6792cffc2df94de0b1?s=64&d=mm&r=g) Shaji Nathan Panchali says:
    
    [August 17, 2017 at 3:56 am](https://chandoo.org/wp/formula-forensics-025/#comment-1497932)
    
    If M=1, Y=2, S=3, O=4, R=5 and E=6..
    
    Then,  
    In cell A1 if i enter "M", in cell A2 i should get "1"  
    In cell A1 if i enter "MS", in cell A2 i should get "13"  
    In cell A1 if i enter "OEY", in cell A2 i should get "462"
    
    I NEED A FORMULA IN CELL A2 TO GET THESE VALUE AS I ENTER DATA IN CELL A1
    
    [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-1497932)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 17, 2017 at 8:29 am](https://chandoo.org/wp/formula-forensics-025/#comment-1498013)
        
        @Shaji
        
        Please ask this question in the Chandoo.org Forums  
        [http://forum.chandoo.org/](http://forum.chandoo.org/)
        
        Also attach a sample file
        
        [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-1498013)
        
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 17, 2017 at 8:40 am](https://chandoo.org/wp/formula-forensics-025/#comment-1498019)
        
        try:  
        \=TEXTJOIN(,,MATCH(MID(D9,ROW(INDIRECT("1:"&LEN(D9))),1),A2:A7,0)) Ctrl+Shift+Enter
        
        Where:  
        Column A2:A7 have the Letters  
        Column B2:B7 have the Numbers  
        D9 has the letters
        
        This requires Excel 2016/365 or above
        
        [Reply](https://chandoo.org/wp/formula-forensics-025/#comment-1498019)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-025/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Show only few rows & columns in Excel \[Quick tip\]](https://chandoo.org/wp/show-only-few-rows-columns-in-excel/) | [Welcome to Chandoo.org – A short introduction to our site](https://chandoo.org/wp/welcome-to-chandoo-org/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
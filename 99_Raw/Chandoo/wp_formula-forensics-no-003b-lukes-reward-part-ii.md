# Extract data from a list that match multiple criteria

**Source:** https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii

---

Formula Forensics No. 003b – Lukes Reward – Part II
===================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 64 comments

  

One of the more commonly asked questions on the Chandoo.org Forums is “_How Do I extract data from a list that matches a criteria_“.

There are a number of ways to achieve this including use of Tables and Filtering, Pivot Table and Filtering, Advanced Filters and Formula based solutions.

Chandoo.org Ninja, Luke wrote his initial Chandoo.org post in which he described a formula based approach in the Formula Forensic post [http://chandoo.org/wp/2011/11/18/formula-forensics-003/](http://chandoo.org/wp/2011/11/18/formula-forensics-003/ "FF003")

Of recent times though there has been a large number of questions at the forums “_How Do I extract data from a list that matches a **number** of criteria_”

One such post was [http://chandoo.org/forum/threads/find-data-through-vlookup-condition-data-between-two-value.19995/#post-120549](http://chandoo.org/forum/threads/find-data-through-vlookup-condition-data-between-two-value.19995/#post-120549)

This problem required the extraction of records that were within a range +/- a value from the base value. This requires two criteria **Records >= Base – Value** and **Records <= Base + Value**.

This post will look at a small modification to Lukes original Formula that allows such a solution to any number of criteria.

Recap of Lukes Formula
----------------------

This post isn’t going to explain how Luke’s formula works and if you are interested I recommend that you revisit Luke’s discussion at: [http://chandoo.org/wp/2011/11/18/formula-forensics-003/](http://chandoo.org/wp/2011/11/18/formula-forensics-003/ "FF003")

Firstly, lets recap Luke’s original formula

\=IF(COUNTIF(A:A,$D$2) < ROWS($E$2:E2), “”,  INDEX(B:B,  SMALL( IF($A$2:$A$10 =$D$2, ROW( $A$2:$A$10)), ROW(A1))))

The logic which allows the selection of the records is based inside the inner If() function as shown below

\=IF(COUNTIF(A:A,$D$2) < ROWS($E$2:E2), “”,  INDEX(B:B,  SMALL( IF($A$2:$A$10 =$D$2, ROW( $A$2:$A$10)), ROW(A1))))

In addition the formula also checks that the number of records matching the criteria hasn’t been exceeded which results in an error. This occurs in the outer If() function.

\=IF(COUNTIF(A:A,$D$2) < ROWS($E$2:E2), “”,  INDEX(B:B,  SMALL( IF($A$2:$A$10 =$D$2, ROW( $A$2:$A$10)), ROW(A1))))

To allow for multiple criteria we need to adjust both these sections.

As always with formula Forensics posts you can follow along using the attached [Sample File (Excel 2007+ Only)](https://chandoo.org/wp/wp-content/uploads/2014/11/Formula-Forensics-3b.xlsx "FF003b Sample File (2007+ only)")

If you see an error on trying to open the sample file, accept it and proceed.

Adding Multiple Criteria
------------------------

Firstly, lets add some extra data to Lukes data including a Month and Shop fields as well as a further reporting field Quantity

[![FF003b1](https://chandoo.org/wp/wp-content/uploads/2014/11/FF003b1.png)](https://chandoo.org/wp/wp-content/uploads/2014/11/FF003b1.png)

By adding multiple criteria we complicate the problem

[![FF003b2](https://chandoo.org/wp/wp-content/uploads/2014/11/FF003b2.png)](https://chandoo.org/wp/wp-content/uploads/2014/11/FF003b2.png)

So we need to search for records that match the **Type**, **Month** and **Shop** fields

Luke’s original formula was

\=IF(COUNTIF(A:A,$D$2) < ROWS($E$2:E2), “”,  INDEX(B:B,  SMALL( IF($A$2:$A$10 =$D$2, ROW( $A$2:$A$10)), ROW(A1))))

The two areas which look after the logic of choosing records are shown in Pink and Red above

We can adjust this logic to suit our expanded data set and criteria using

\=IF(COUNTIFS($A:$A,$G$6,$B:$B,$G$9,$C:$C,$G$3)<ROWS($I$2:I2),””,INDEX(D:D,SMALL(IF(($A$2:$A$25=$G$6)+($B$2:$B$25=$G$9)+($C$2:$C$25=$G$3)=3,ROW($C$2:$C$25)),ROW(C1))))

Lets look at each section

COUNTIFS($A:$A,$G$6,$B:$B,$G$9,$C:$C,$G$3)<ROWS($I$2:I2)

This checks that the current record being reported ROWS($I$2:I2) is less than the number of records matching the criteria COUNTIFS($A:$A,$G$6,$B:$B,$G$9,$C:$C,$G$3).  

It stops the #NUM! error from occurring if the formula tries to extract more records than those match the criteria

In our sample we can see that in the sixth row of the report, which is blank, the ROWS($I$2:I7) = 6 is greater than the number of records matching the criteria (**5**) and so a Blank cell is returned

The second change from Luke’s formula is ($A$2:$A$25=$G$6)+($B$2:$B$25=$G$9)+($C$2:$C$25=$G$3)=3

This is a simple addition of 3 Arrays, one for each criteria

If we go to cell **I2** Edit the formula with F2, Then select the first criteria from the formula ($A$2:$A$25=$G$6) then press F9

Excel returns: {TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;FALSE}

If we repeat this for each criteria

Criteria 2: Select ($B$2:$B$25=$G$9) then press F9

Excel returns: {FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}

Criteria 3: Select ($C$2:$C$25=$G$3) then press F9  

Excel returns: {FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}

The great things is that by combining the 3 criteria with simple Additions allows Excel converts the results to numbers, corresponding to how many criteria each record match

Combined criteria: Select ($A$2:$A$25=$G$6)+($B$2:$B$25=$G$9)+($C$2:$C$25=$G$3) then press F9

Excel returns: {1;1;2;2;1;2;0;0;1;1;0;1;2;2;**3**;**3**;2;**3**;1;1;**3**;**3**;1;2}

We can see that there are 5 values of 3, these correspond to the 5 Records that match all 3 Criteria

Finally comparing this array to the number of criteria we end up with an array of True/False which correspond to our records

Combined criteria: Select ($A$2:$A$25=$G$6)+($B$2:$B$25=$G$9)+($C$2:$C$25=$G$3) = 3 then press F9

Excel returns: {FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;**TRUE**;**TRUE**;FALSE;**TRUE**;FALSE;FALSE;**TRUE**;**TRUE**;FALSE;FALSE}

Note the 5 True values, that correspond to the 5 records that match the 3 criteria.

As an array Formula accept the formula with Ctrl+Shift+Enter

We can now see that there are 5 records that match the 3 criteria.

[![FF003b3](https://chandoo.org/wp/wp-content/uploads/2014/11/FF003b3.png)](https://chandoo.org/wp/wp-content/uploads/2014/11/FF003b3.png)

This is used inside the Index() function to return Row number of the record that is required.

The function can then be copied across to return other fields as in the quantity using the same logic.

Final Discussion
----------------

Although there are a number of methods that can be used to solve this including Tables and Filtering, Pivot Table and Filtering and Advanced Filters, the use of a formula based approach allows the extraction of these records without any user intervention or VBA code.

Download
--------

You can download a copy of the above file and follow along: [Download Here](https://chandoo.org/wp/wp-content/uploads/2014/11/Formula-Forensics-3b.xlsx "Luke Example File")
.

[Formula Forensics “The Series”](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")

-----------------------------------------------------------------------------------------------------------------

This is the 31st post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts: [Formula Forensic Series](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share like above, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
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
| Written by Hui...  <br>Tags: [Formula Forensic](https://chandoo.org/wp/tag/formula-forensic/)<br>, [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 64 Responses to “Formula Forensics No. 003b – Lukes Reward – Part II”

1.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [November 10, 2014 at 8:22 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844028)
    
    You can also exploit a technique used by VIkas Gautam to achieve the same results as the array:
    
    IF(($A$2:$A$25=$G$6)+($B$2:$B$25=$G$9)+($C$2:$C$25=$G$3)=3
    
    by using an identical COUNTIFS construction to that here, though with a "reversal" of the criteria and criteria\_ranges (and here using entire column references would certainly not be advisable!), i.e.:
    
    IF(COUNTIFS($G$6,$A$2:$A$25,$G$9,$B$2:$B$25,$G$3,$C$2:$C$25)
    
    Although I have not performed tests as to which of these two constructions is the more efficient (in terms of worksheet performance), I would imagine that the latter may well be.
    
    Also, a minor point, but the use of ROW(C1) for SMALL's k parameter leaves the construction susceptible to error upon row insertions. More rigorous is to use e.g. ROWS($I$2:I2) here also.
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844028)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [November 10, 2014 at 5:40 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844449)
        
        For the latter approach - may I suggest:  
        IF((A$2:A$25=G$6)\*(B$2:B$25=G$9)\*(C$2:C$25=G$3),...  
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844449)
        
2.  ![](https://secure.gravatar.com/avatar/7c8f20e6f1dd88975957ff3a5ed86f72b72134ed8c4c11117f0ccbcc83a7eaa9?s=64&d=mm&r=g) bob hoskins says:
    
    [November 10, 2014 at 12:11 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844220)
    
    I'm an absolute array formula n00blet, and this might be a dumb question but I have to ask:
    
    Why do you need the 'small' function in this formula? Could you have a formula with the same functionality but without the 'small' function?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844220)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [November 10, 2014 at 3:16 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844326)
        
        @Bob  
        Did you read Luke's original post, where this is described  
        [http://chandoo.org/wp/2011/11/18/formula-forensics-003/](http://chandoo.org/wp/2011/11/18/formula-forensics-003/)
        
        The small function returns the Nth row that matches the criteria  
        Initially it returns the 1st row that matches the criteria, then the 2nd , 3rd etc  
        The 1st match may be the 5th row of the source table etc  
        The Nth row is the last parameter in the Small function
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844326)
        
3.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [November 10, 2014 at 5:16 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844427)
    
    After a short glance - it seems to me that the complete formula can be shorten as follows (in "Excel 2007" and above):  
    \=IFERROR(INDEX(E:E,SMALL(IF((A$2:A$25=G$6)\*(B$2:B$25=G$9)\*(C$2:C$25=G$3),ROW(C$2:C$25)),ROW(D1))),"")  
    Michael (Micky) Avidan  
    “Microsoft® Answers" - Wiki author & Forums Moderator  
    “Microsoft®” MVP – Excel (2009-2015)  
    ISRAEL
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844427)
    
4.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [November 10, 2014 at 5:28 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844436)
    
    This type of formula can almost always be shortened using an equivalent IFERROR set-up. However, what most people don't realise is that, if the dataset in question is relatively large (e.g. several thousand rows), the IFERROR version is generally vastly inferior - in terms of workbook performance - than the version which uses an initial IF clause, as given here by Luke.
    
    There's an explanation as to why here:
    
    [http://superuser.com/questions/812727/look-up-a-value-in-a-list-and-return-all-multiple-corresponding-values/812848#812848](http://superuser.com/questions/812727/look-up-a-value-in-a-list-and-return-all-multiple-corresponding-values/812848#812848)
    
    Of course, if this is a "shortest" formula challenge then I too would go with the IFERROR set-up! But if and only if!
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844436)
    
5.  ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
    
    [November 10, 2014 at 6:58 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844499)
    
    Excellent add-on Hui. Thanks for explaining this concept. 🙂
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-844499)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [November 12, 2014 at 8:30 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-846575)
        
        He he,  
        I answered about 5 posts in a 2 week period and figured I'd be better to do this once and then refer people to it.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-846575)
        
6.  ![](https://secure.gravatar.com/avatar/53b324ee3aa8827253790f7d0302a693ada75ec8a1b3bda84e34ced1d765f846?s=64&d=mm&r=g) Jared says:
    
    [November 11, 2014 at 6:11 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-845790)
    
    How would you create the formula to leave out a certain criteria?
    
    If you wanted to search for both Type and Month but not include Shop as a filter as an example.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-845790)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [November 12, 2014 at 7:58 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-846549)
        
        Leave out the part: \*(B$2:B$25=G$9)  
        Meaning - the formula will look like this:  
        \=IFERROR(INDEX(E:E,SMALL(IF((A$2:A$25=G$6)\*(C$2:C$25=G$3),ROW(C$2:C$25)),ROW(D1))),””)  
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-846549)
        
        *   ![](https://secure.gravatar.com/avatar/53b324ee3aa8827253790f7d0302a693ada75ec8a1b3bda84e34ced1d765f846?s=64&d=mm&r=g) Jared says:
            
            [November 12, 2014 at 10:32 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-847185)
            
            Micky,
            
            Thanks but not exactly what I was looking for. Is there a way to make this dynamic so that you could have blank field in the drop down which would include ALL SHOP entries.
            
            So in this example you would get  
            Type: Vegetable  
            Month: January  
            Shop: No Selection or Blank cell (Leaving blank would return both Shops in the North and South that fit the other criteria)
            
            Does that make sense?
            
            Thanks!
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-847185)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                 says:
                
                [November 13, 2014 at 5:35 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-847526)
                
                @Jared  
                As Micky suggested  
                Change the \*(B$2:B$25=G$9)  
                to \*if(G$9="",1,(B$2:B$25=G$9))
                
                for each section
                
                \=IFERROR(INDEX(E:E,SMALL(IF(If(G$6="",1,(A$2:A$25=G$6))\*If(G$(="",1,(B$2:B$25=G$9))\*if(G$3="",1,(C$2:C$25=G$3)),ROW(C$2:C$25)),ROW(D1))),””)
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-847526)
                
                *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                    
                    [November 13, 2014 at 2:41 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-847929)
                    
                    @Hui,  
                    1\. You missed the G$9 (typed: "G$(" instead).  
                    2\. Your formula "suffers" from a "few" extra brackets.  
                    \=IFERROR(INDEX(E:E,SMALL(IF(IF(G$6="",1,A$2:A$25=G$6)\*IF(G$9="",1,B$2:B$25=G$9)\*IF(G$3="",1,C$2:C$25=G$3),ROW(C$2:C$25)),ROW(D1))),"")  
                    Michael (Micky) Avidan  
                    “Microsoft® Answers” – Wiki author & Forums Moderator  
                    “Microsoft®” MVP – Excel (2009-2015)  
                    ISRAEL
                    
7.  ![](https://secure.gravatar.com/avatar/ad53cd10d27b3732545a6a559862d8f3303459a945a7014fd11e62cceed515f6?s=64&d=mm&r=g) Temma says:
    
    [November 13, 2014 at 4:43 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-848007)
    
    This may seem like a silly question, but is there anyway to have the internal if statement search an array rather than a single cell reference. So search an array with an array of criteria?
    
    Basically, I am attempting to extract information based on user selected criteria. This means I might only have 1 item for "Line Item" but I could have 3 items for "WeekEnding", and I need to be able to pull all of the rows that have that "Line Item" for WeekEnding1, WeekEnding2, Weekending3, etc.. I have tried using an OR() but the formula just got angry.
    
    Thanks,  
    Temma
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-848007)
    
8.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [November 14, 2014 at 8:16 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-848707)
    
    @Temma
    
    For what you require, the OR function is not the appropriate choice within this type of array formula. Your construction for the WeekEnding criterion would be of the form:
    
    IF(ISNUMBER(MATCH(WeekEndingRange,A1:A3,0))
    
    where I'm assuming that WeekEndingRange is the range reference pertaining to that data, e.g. C1:C1000, and that you have your values corresponding to WeekEnding1, WeekEnding2 and WeekEnding3 in A1:A3.
    
    This basically means that an entry in WeekEndingRange which matches ANY of WeekEnding1, WeekEnding2 and WeekEnding3 will be considered.
    
    If you don't want to use actual cells within the worksheet to hold your WeekEnding1, WeekEnding2 and WeekEnding3 values, you can hard-code them in the above construction itself. In that case, however, the syntax would be a little different, and to be sure of getting it right it would be useful to know the precise form that these values take (e.g. dates?).
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-848707)
    
    *   ![](https://secure.gravatar.com/avatar/49f904e0d5f1c70658fc81dee5a9c34d60d96ecb6f132159b6b6b255719c941a?s=64&d=mm&r=g) Emily says:
        
        [December 30, 2014 at 5:09 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-885968)
        
        I am having the same question that I believe Temma asked, but am a bit confused on the response (or what "WeekEndRanges" refers to).
        
        Essentially my question is as follows: I have sets of account codes that are categorized (e.g. Salary, Tuition, supplies, etc), and I would like to pull values (Amt Paid and Description) from each of the codes but have them remain grouped under the categories I have delineated for each (E.g. Salary has acct codes 1051, 1052, 1054, 1771, etc). I would like to create a summary report based on all of the entries per account code but remain grouped still within the 'salary category'. Regarding the output, I don't need to know which account code it came from, but simply that the line item of 'Bob Smith $100.00' falls under the Salary categories.
        
        Hopefully this makes sense. Thank you for your help!  
        Emily
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-885968)
        
        *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
             says:
            
            [January 1, 2015 at 3:54 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-886846)
            
            @Emily  
            Can you please ask your question in the Forums  
            [http://chandoo.org/forum/](http://chandoo.org/forum/)
              
            Please attach a sample file for a more specific answer
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-886846)
            
9.  ![](https://secure.gravatar.com/avatar/ad53cd10d27b3732545a6a559862d8f3303459a945a7014fd11e62cceed515f6?s=64&d=mm&r=g) Temma says:
    
    [November 14, 2014 at 1:36 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-848901)
    
    @XOR LX
    
    THANK YOU!!!! I knew I was missing something really simple and also knew that I had been staring at this spreadsheet for way too long to see it.
    
    This is perfect. Since I have all my ranges named and they are dynamic, this is the PERFECT solution!!!!
    
    Thank you again,  
    Temma
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-848901)
    
10.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [November 16, 2014 at 8:16 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-850518)
    
    @Temma You're welcome! Glad to help!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-850518)
    
11.  ![](https://secure.gravatar.com/avatar/f90a016f1cecd4e649c642ffa0adef47c811dbd01e20fb7c96b464aa61b53329?s=64&d=mm&r=g) IainG says:
    
    [January 21, 2015 at 3:10 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-897545)
    
    Afternoon,
    
    I've tried this formula out today. I work with FOI requests, which are time limited, and want to produce a "to do" list of requests that are due a 10, 15, 17, 19 day reminder or are on day 20 and a response is due.  
    I'm not as bothered about the error hiding bit, so have transposed the formula above to the following:  
    {=INDEX(RequestLog!$C$8:$C$1008,SMALL(IF((RequestLog!$AA$8:$AA$1008="")+(RequestLog!$V$8:$V$1008="")+(RequestLog!$AX$8:$AX$10085)=4,ROW(RequestLog!$C$8:$C$1008)),ROW(RequestLog!C7)))}
    
    To explain - My data is in a massive table on tab 2 (RequestLog), V is the column that gets a tick (P in wingding2) if the 10 day reminder has been sent, C is the column containing the reference number, AX is a running count of days remaining until deadline, AA is the column recording whether a final response has been sent.
    
    I've evaluated the steps, and everything is fine up until the last bit, rows 404 and 407 are returned, but the final production is #num (fyi - i did try the original with the error removing, but suspect i got the same answer as i couldn't see anything!)
    
    I know these kind of work, as i managed to formulate the following, which will show only the first instance of a reminder being due (but when copied down just shows the same!):  
    {=INDEX(RequestLog!$A$8:$AX$1008,MATCH(1,(RequestLog!$AA$8:$AA$1008="")\*(RequestLog!$V$8:$V$1008="")\*(RequestLog!$AX$8:$AX$10085),0),2)}
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-897545)
    
    *   ![](https://secure.gravatar.com/avatar/f90a016f1cecd4e649c642ffa0adef47c811dbd01e20fb7c96b464aa61b53329?s=64&d=mm&r=g) IainG says:
        
        [January 21, 2015 at 3:11 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-897546)
        
        Apologies, the formula displays wrong...
        
        \=INDEX(RequestLog!$C$8:$C$1008,SMALL(IF((RequestLog!$AA$8:$AA$1008="")+(RequestLog!$V$8:$V$1008="")+(RequestLog!$AX$8:$AX$1008 LESS THAN 11)+(RequestLog!$AX$8:$AX$1008 GREATER THAN 5)=4,ROW(RequestLog!$C$8:$C$1008)),ROW(RequestLog!C7)))
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-897546)
        
12.  ![](https://secure.gravatar.com/avatar/69ce39426bc4f6908c069572855f3f9214e82944f00ecd7422a0c45c350b662d?s=64&d=mm&r=g) Alan says:
    
    [April 16, 2015 at 2:39 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-953508)
    
    Thanks very much for this, been looking for ages for something like this!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-953508)
    
13.  ![](https://secure.gravatar.com/avatar/ae4037117fb9a78afc21622485ecd96c5421d356966ff86b0efc8c7d28ef9636?s=64&d=mm&r=g) DLOVE says:
    
    [May 19, 2015 at 7:02 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-977089)
    
    i am looking to match 2 fields to pull back 1 record for the field if unique. otherwise imore than 1 if multiple matches for criteria( in the same cell)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-977089)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [May 20, 2015 at 12:56 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-977185)
        
        @DLove
        
        Can you ask the question at the Chandoo.org Forum  
        [http://chandoo.org/forum/](http://chandoo.org/forum/)
        
        Attach a sample file to simplify a solution
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-977185)
        
14.  ![](https://secure.gravatar.com/avatar/24409a67b963df06da223105e7d0acf25ca7c4cf566beafbd379858735df1be7?s=64&d=mm&r=g) arthur says:
    
    [June 8, 2015 at 11:02 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-989309)
    
    How can i make it work to where if i only wanted to select 2 out of the 3 criteria, and still show a result. Example: if I only selected the "month" and the "shop" can it show me all that match the month and shop even if the type is fruit of vegetable. OR select the all the items sold in January in the south shop, displaying all vegetables and fruits that meet the two criteria.
    
    In other words how can i make it so if i OPT to not choose one or more of the criteria, it still shows me data matching the criteria selected
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-989309)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 9, 2015 at 12:28 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-989345)
        
        @Arthur
        
        Yes, this can be done by simply changing the selection logic  
        I have done this and you can download a file from:  
        [https://www.dropbox.com/s/78phxaej9ui3k7z/Formula-Forensics-3b\_Mod2.xlsx?dl=0](https://www.dropbox.com/s/78phxaej9ui3k7z/Formula-Forensics-3b_Mod2.xlsx?dl=0)
        
        In fact it is setup to work with 1, 2 or 3 criteria
        
        Let me know what you think?
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-989345)
        
        *   ![](https://secure.gravatar.com/avatar/f1de1a6b40b904e69e3cbf613f3061bcfeb83542c4ac385171e7df462fd2110f?s=64&d=mm&r=g) Chris says:
            
            [June 27, 2015 at 1:52 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1000797)
            
            What if you have North, South, East and West in your data and you add a field to select multiple locations (i.e. South and West)? I'm assuming you need to use the OR formula at some point, but having a few issues inserting that into the formula in the dropbox file. Thanks!
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1000797)
            
15.  ![](https://secure.gravatar.com/avatar/c38555a2df581aab550e36bad2223b73260bb8646b044e752d19a495a579165a?s=64&d=mm&r=g) Granpa says:
    
    [June 14, 2015 at 7:00 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-993072)
    
    How do you handle blanks in your data? Suppose some of the lines in the sample were not region specific. You could enter the line twice, once with "south" and again with "north", but in my application I have several lines that have blanks so that is not practical. Is there something that I can put in the blank that will act like a wildcard?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-993072)
    
16.  ![](https://secure.gravatar.com/avatar/2a90ac99e43d116e0aa0692556ba629f9e64415f6e2011be0114a5c67d6eb226?s=64&d=mm&r=g) Priya K says:
    
    [June 17, 2015 at 11:03 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-995536)
    
    I’ve tried this formula out today.  
    \=IF(COUNTIFS($A:$A,$G$6,$B:$B,$G$9,$C:$C,$G$3)<ROWS($I$2:I2),"",INDEX(D:D,SMALL(IF(($A$2:$A$25=$G$6)+($B$2:$B$25=$G$9)+($C$2:$C$25=$G$3)=3,ROW($C$2:$C$25)),ROW(C1))))
    
    it works good but as soon as i am increasing cell range(in $A$2:$A$25) from 25 to 2500 it displays error. please help, i am really stuck here.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-995536)
    
17.  ![](https://secure.gravatar.com/avatar/ef40bf426380d26563f3b3963fc048c6fbdbb7233dde0b6cc983eaeeb616b9ab?s=64&d=mm&r=g) Abhijeet says:
    
    [September 26, 2015 at 2:18 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1051898)
    
    Hi Luke
    
    Thanks for this excellent technique
    
    But i want to know if Multiple criteria & data is huge then how do we copy paste result in next sheet with help of macro.please give some VBA tips also
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1051898)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [September 26, 2015 at 5:58 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1052099)
        
        @Abhijeet
        
        This technique works quite well even on large data sets
        
        If you want to copy or move data to other sheets  
        I'd read about the techniques here:
        
        Move Data to other Sheets  
        [http://chandoo.org/wp/2012/05/14/vba-move-data-from-one-sheet-to-multiple-sheets/](http://chandoo.org/wp/2012/05/14/vba-move-data-from-one-sheet-to-multiple-sheets/)
          
        Advanced Filter Move Data to other Files  
        [http://chandoo.org/wp/2011/10/19/split-excel-file-into-many/](http://chandoo.org/wp/2011/10/19/split-excel-file-into-many/)
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1052099)
        
18.  ![](https://secure.gravatar.com/avatar/88f8c491415c0ab40c0985b436859863365abe482a86dbe818ecdc332ed14a10?s=64&d=mm&r=g) rrk says:
    
    [December 2, 2015 at 4:30 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1094970)
    
    I want to extract data from different files from 1 folder:  
    e.g all files will be saved in 1 location : \\\\c\\files\\
    
    I have desiged a summary but in the same format as indvidual files with a micro button. I want to write a code which extract information from indvidual files :\\\\c\\files\\ to the summary fromat that i have designed using the button
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1094970)
    
19.  ![](https://secure.gravatar.com/avatar/28e3f273a004f114fb5f8b86ed83be6ac89c392e25735e9ed74f00fb6df34eff?s=64&d=mm&r=g) pvdv says:
    
    [April 26, 2016 at 1:31 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1175468)
    
    Hello,
    
    I am working based on your sheet, but for my solution i want to get the output in an dropdown menu. For this reason, the formula needs to be placed in the data-validation menu.  
    But when I do, i get only the first possible value as a return. How do I transform the formula to generate a comma seperated list (as the data validation requires)?  
    Any help would be greatly appreciated.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1175468)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [April 26, 2016 at 3:13 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1175505)
        
        @Pvdv
        
        Have you read about Dynamic Data Validation  
        [http://chandoo.org/wp/2014/02/13/dynamic-cascading-dropdowns-that-reset/](http://chandoo.org/wp/2014/02/13/dynamic-cascading-dropdowns-that-reset/)
        
        Jeff Weir is a gun on this and worth chasing him up
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1175505)
        
        *   ![](https://secure.gravatar.com/avatar/28e3f273a004f114fb5f8b86ed83be6ac89c392e25735e9ed74f00fb6df34eff?s=64&d=mm&r=g) pvdv says:
            
            [April 29, 2016 at 9:56 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1176535)
            
            Thanks for the reply, but I am still not quite able to build what I want. I have one sheet consiting of 80 rows, each one with one driver. Name, drivers licence 1 (YN), drivers licence 2(YN), ... monday (YN), tuesday (YN) and finally a location from where the person is working from.
            
            Based on this data, i want to get the people able to ride routes in some sort of drop down list. There are around 70 routes to be driven, 7 days a week, with differences in required drivers licences, distribution centra and departure times. For maintainabillity i want to avoid listing options for each day a route is scheduled.
            
            It feels like i am almost there with your formula but I can't get the drop-down bit to work.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1176535)
            
20.  ![](https://secure.gravatar.com/avatar/08d3a997e85c79d06d29a82ac383a755a3167eefeba8bfe52c33104e1d11e55a?s=64&d=mm&r=g) sami says:
    
    [May 8, 2016 at 7:48 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1182695)
    
    i am extracting student data of a particular class having session "2015-16", and class "ONE" as CRITERIA from table wherein a particular record has 42 columns (i.e. class PG to 10)  
    columns are: roll no, student name, father name, acadmic year, class, fee (last three columns are repeated)  
    countifs is fetching no. of records but fail to fetch roll no wise record in my case. pls advise
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1182695)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [May 8, 2016 at 3:00 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1183113)
        
        @Sami
        
        I'd suggest asking the question at the Chandoo.org Forums  
        [http://forum.chandoo.org/](http://forum.chandoo.org/)
          
        Attach a sample file will allow us to give a specific answer
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1183113)
        
21.  ![](https://secure.gravatar.com/avatar/08d3a997e85c79d06d29a82ac383a755a3167eefeba8bfe52c33104e1d11e55a?s=64&d=mm&r=g) sami says:
    
    [May 12, 2016 at 6:18 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1187044)
    
    below mentioned data used as source:  
    ADMISSION NO, STUDENT NAME, FATHER NAME, ACADEMIC YEAR, CLASS, MONTHLY FEE, ACADEMIC YEAR, CLASS, MONTHLY FEE, ACADEMIC YEAR, CLASS, MONTHLY FEE  
    1, Saifullah, Samiullah, 2013-14, KG, 2400, 2014-15, ONE, 2500, 2015-16, TWO, 2500,  
    2, EMAAN FATMAH, Roohullah, 2013-14, NURSERY, 1500, 2014-15, KG, 1500, 2015-16, ONE, 1500,  
    3, muhammad aaqib, Samiullah, 2014-15, KG, 1800, 2015-16, ONE, 1900, 2016-17, TWO, 1900,  
    4, Zareen Roohullah, Roohullah, 2010-11, NURSERY, 1700, 2011-12, KG, 1700, 2012-13, ONE, 1700,  
    5, KALEEM, LATE VUSKA, 2013-14, KG, 2400, 2014-15, ONE, 2500, 2015-16, TWO, 2500,  
    6, ZEESHAN TARIQ, 2013-14, NURSERY, 1500, 2014-15, KG, 1600, 2015-16, ONE, 1500,  
    7, ABDULLAH, ASAD, 2014-15, KG, 1800, 2015-16, ONE, 1800, 2016-17, TWO, 1900,  
    8, KASHIF, MUKHTAR, 2010-11, NURSERY, 1700, 2011-12, KG, 1700, 2012-13, ONE, 1700,
    
    ADMISSION NO 1  
    ADMISSION NO 4  
    ACADMIC YEAR 2013-14 (used as criteria)  
    CLASS KG (used as criteria)  
    FEE PERIOD FROM MAY YEAR 2016  
    FEE PERIOD TO MAY YEAR 2016  
    LATE-CHG 100  
    SLIP ISSUE DATE 28-04-2016  
    FEE DUE DATE 11.05.2016  
    SLIP VALIDITY DATE 20-05-2016  
    SECTION A
    
    what i want is to display roll nos matching the criteria?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1187044)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [May 13, 2016 at 1:09 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1187133)
        
        @Sami
        
        I'd suggest asking the question at the Chandoo.org Forums  
        [http://forum.chandoo.org/](http://forum.chandoo.org/)
          
        Please attach a sample file will allow us to give a specific answer
        
        The problem with the data you supplied is that there is no way to be sure that when I import it, that I get the columns/fields correct
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1187133)
        
22.  ![](https://secure.gravatar.com/avatar/2198506928402a1c5d207728686de38dd38fe25d45d2d62bb94e5c9c91284e3f?s=64&d=mm&r=g) James says:
    
    [May 20, 2016 at 5:13 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1193880)
    
    Can you use less than or greater than? I have a formula that I'm trying to use dates and show data that fall within a certain time period.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1193880)
    
    *   ![](https://secure.gravatar.com/avatar/ef40bf426380d26563f3b3963fc048c6fbdbb7233dde0b6cc983eaeeb616b9ab?s=64&d=mm&r=g) Abhijeet says:
        
        [May 22, 2016 at 1:24 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1194843)
        
        Hi James
        
        what u want from 2 dates u want to identify which dates are falls or what can u pls upload data with expected result
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1194843)
        
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 22, 2016 at 2:09 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1218803)
        
        @James
        
        something like:
        
        \=IF(COUNTIFS($A:$A,">"&$G$6,$A:$A,"<="&$G$9,$C:$C,$G$3)<ROWS($I$2:I2),"",INDEX(D:D,SMALL(IF(($A$2:$A$25>$G$6)+($A$2:$A$25<=$G$9)+($C$2:$C$25=$G$3)=3,ROW($C$2:$C$25)),ROW(C1))))
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1218803)
        
23.  ![](https://secure.gravatar.com/avatar/c7988236ef553f12a27c95a237baa7e5fdc72934e9bfac0895493994b8066845?s=64&d=mm&r=g) Glenn says:
    
    [June 20, 2016 at 7:52 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1217279)
    
    This is great. I have been searching for this solution. I am curious however, I am trying to use this with three criteria, two of which are dates. So essentially one criteria would be greater than or equal to one date and then less than or equal to another date (basically between two dates). How would I incorporate that into this? Thanks.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1217279)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 22, 2016 at 2:07 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1218801)
        
        @Glenn  
        Something like:
        
        \=IF(COUNTIFS($A:$A,">"&$G$6,$A:$A,"<="&$G$9,$C:$C,$G$3)<ROWS($I$2:I2),"",INDEX(D:D,SMALL(IF(($A$2:$A$25>$G$6)+($A$2:$A$25<=$G$9)+($C$2:$C$25=$G$3)=3,ROW($C$2:$C$25)),ROW(C1))))
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1218801)
        
24.  ![](https://secure.gravatar.com/avatar/bc6f2502dc8e5247b5404e89cebe71f1c4b4bf74d2474ec329741dcf50400c0f?s=64&d=mm&r=g) AALLeeXX says:
    
    [June 22, 2016 at 9:36 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1218625)
    
    Hi,
    
    Thanks for this interesting tutorial. It's almost what I was looking for, with a minor difference that is for the criteria I need to consider the capitalization, ie make "North" and "north" discriminated.  
    I'm thinking of using FIND but I still fails using it with arrays.  
    Is it possible ?
    
    Thanks.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1218625)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 22, 2016 at 1:49 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1218792)
        
        @Alex
        
        To use case sensitivity in the sample file for this tutorial
        
        I2: =IF((($A$2:$A$25=$G$6)+EXACT($B$2:$B$25,$G$9)+($C$2:$C$25=$G$3)) < ROWS($I$2:I2),"",INDEX(D:D,SMALL(IF(($A$2:$A$25=$G$6)+EXACT($B$2:$B$25,$G$9)+($C$2:$C$25=$G$3)=3,ROW($C$2:$C$25)),ROW(C1))))
        
        J2: =IF((($A$2:$A$25=$G$6)+EXACT($B$2:$B$25,$G$9)+($C$2:$C$25=$G$3)) < ROWS($I$2:J2),"",INDEX(E:E,SMALL(IF(($A$2:$A$25=$G$6)+EXACT($B$2:$B$25,$G$9)+($C$2:$C$25=$G$3)=3,ROW($C$2:$C$25)),ROW(D1))))
        
        You will also need to adjust the Data validation in G9
        
        You can download a copy of the modified file here:  
        [http://chandoo.org/wp/wp-content/uploads/2014/11/Formula-Forensics-3b\_Case\_Sensitivity.xlsx](http://chandoo.org/wp/wp-content/uploads/2014/11/Formula-Forensics-3b_Case_Sensitivity.xlsx)
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1218792)
        
        *   ![](https://secure.gravatar.com/avatar/bc6f2502dc8e5247b5404e89cebe71f1c4b4bf74d2474ec329741dcf50400c0f?s=64&d=mm&r=g) AALLeeXX says:
            
            [June 23, 2016 at 6:47 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1219406)
            
            Hi Hui,
            
            Thank you for this great update, appreciated a lot.
            
            My case is however a bit more challenging 😉  
            One of the criterias is rather "contains this string or substring" with case sensitivity. In our example above, the shops could contain 1 to 4 directions lise N, S, W, E, N-E, S-W but also n-e, s-W, etc.... then the criteria becomes "contains n" (like n, n-e, w-n... but not N, N-e...).  
            This is why I was thinking of FIND which does that well in basic formulas, but with array, I'm stuck... Thaks for any other hint 😉
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1219406)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                 says:
                
                [June 24, 2016 at 1:08 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1220080)
                
                @Alex
                
                I'm thinking a purpose built User Defined Function may be a better solution
                
                Ask the question in the forums [http://forum.chandoo.org/](http://forum.chandoo.org/)
                  
                and attach a sample file with sample answers
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1220080)
                
25.  ![](https://secure.gravatar.com/avatar/29964f4dc68462686abe68ee54733867c27a25604b6307c90c676c660429b012?s=64&d=mm&r=g) Farhat says:
    
    [September 18, 2016 at 1:26 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1290624)
    
    Hi,  
    Can we get unique(no duplicates) without blanks and alphabetically sorted list?
    
    In my case, i have a hierarchy with which i want to design a dashboard with dynamic charts for the staff reporting to a particular manager, for a particular month. It works fine, when we select a particular month. But, we also have "Quarters" on a different column, and when we select quarter, we get duplicated results.
    
    Any help shall be highly appreciated.  
    Thanks
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1290624)
    
26.  ![](https://secure.gravatar.com/avatar/110eadd27db435c23790ba8b5012d457fa84ccdf71fde6f44aa8c41634adabb4?s=64&d=mm&r=g) sridhar says:
    
    [September 24, 2016 at 1:48 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1296149)
    
    For Multiple Criteria, we are getting all the data based on the selections that we have selected for Type, Month and Shop. Can you please help me to top n values with output shown as below
    
    Output Quantity  
    Spinach 39  
    Spinach 33  
    Potato 29  
    Broccoli 21
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1296149)
    
27.  ![](https://secure.gravatar.com/avatar/834dc30fa342f6528aa79807b92b7ea908c352db9139260bb52eef4b97057d17?s=64&d=mm&r=g) HeyInKy says:
    
    [March 22, 2017 at 3:03 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1422133)
    
    Hi! great post ...so I tried to take this down to only 2 criteria instead 3, and substitute table ranges, and ended up with this:
    
    \=IF(COUNTIFS(Table1\[Region\],$H$2,Table1\[Level\],$H$5)<ROWS($K$2:K2),"",INDEX(Table1\[Employee\],SMALL(IF((Table\[Region\]=$H$1)+(Table\[Level\]=$H$5)=2,ROW(Table1\[Level\])),ROW(E1))))
    
    ...where my array formula will be in column K, and my \[Level\] column is column E, but it returns #NUM! error in K@ before even copying down. The last portion, ROW(Table1\[Level\])),ROW(E1)))) seems to be the cause...
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1422133)
    
28.  ![](https://secure.gravatar.com/avatar/5287389369c78209b007d47d7498c566032be4a2f1bf973efac9b6bbae7064b1?s=64&d=mm&r=g) Thiru says:
    
    [April 4, 2017 at 3:01 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1431309)
    
    I need to Extract The Records From Master data By using Multiple drop down Condition.  
    Let me know.What Function i can Use?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1431309)
    
29.  ![](https://secure.gravatar.com/avatar/a1fb04bc3c0006b44f18a2af031604e148e5b38949e42159c23d9026123294ca?s=64&d=mm&r=g) Greg says:
    
    [April 7, 2017 at 3:57 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1433402)
    
    I finally got it implemented and it works great so long as the changes to the criteria are TYPED into the cells. I have 3 criteria. Month, Year , and JV#. I would like JV# to be dynamic. But every time I use an index/match to determine the JV# of the data coming in, the data disappears I typically can't use the lookup again unless go back in excel to before I did the lookup . I can type a JV in and it will work. Further I can type more JV's in and they will work.
    
    Somehow data presented by a function will not trigger a lookup.
    
    Any ideas on how to fix this.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1433402)
    
30.  ![](https://secure.gravatar.com/avatar/6eae138df0a4afddcf312f3c3a5a5efb3fd0f2127b1e3c43d78332135ac4b411?s=64&d=mm&r=g) Callao2908 says:
    
    [June 5, 2017 at 2:20 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1456624)
    
    Good morning, thanks for such a good example.  
    What I want to know is that formula should be used,  
    so instead of seeing the list that includes vegetables  
    that are repeated, only the accumulated. Example:
    
    Output Quantity  
    Potato 29  
    Spinach 72  
    Peas 19  
    Broccoli 21
    
    Spinach It is the sum of 39 plus 33, the two that are  
    repeated, and so for all cases that repeat  
    Thanks for the attention  
    Jorge from Peru
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1456624)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 6, 2017 at 2:17 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1456769)
        
        @Callao2908
        
        You can use the technique shown here to get the list of Vegetables  
        Then use a Sumifs() function to sum the Column where the vegetable is equal to eg: Potato
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1456769)
        
        *   ![](https://secure.gravatar.com/avatar/6eae138df0a4afddcf312f3c3a5a5efb3fd0f2127b1e3c43d78332135ac4b411?s=64&d=mm&r=g) Callao2908 says:
            
            [June 6, 2017 at 4:29 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1456951)
            
            Thank you Hui  
            Regards
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1456951)
            
31.  ![](https://secure.gravatar.com/avatar/67ef9553cf8fd75768348bd3cf0e9d9f8c9ec8b5e5df7177cde4e427cf5dfab1?s=64&d=mm&r=g) Sajeesh says:
    
    [June 7, 2017 at 8:52 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1457162)
    
    Sir,
    
    Consider, if we are having multiple products for Example Peas two times - how we will calculate.
    
    Regards,
    
    SAJEESH P
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1457162)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 7, 2017 at 1:11 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1457210)
        
        @Sajeesh
        
        Please ask the question in the Forums and attach a sample file as it is unclear what you are asking ?  
        [http://forum.chandoo.org/](http://forum.chandoo.org/)
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1457210)
        
32.  ![](https://secure.gravatar.com/avatar/ae0e0640dde456bbe4bb07f065709e00fa7bde2871a1baeba3e04890352604e7?s=64&d=mm&r=g) effefirn says:
    
    [July 16, 2017 at 2:10 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1481209)
    
    I am looking ways to extract data by single formula (copy-pasteable all the way down) for this case:  
    Suppose the data is:
    
    Apple  
    Orange  
    Broccoli  
    Spinach  
    Pear  
    Peas  
    Apple  
    Orange  
    Broccoli  
    Spinach  
    Pear  
    Peas  
    Apple  
    Mango  
    Potato  
    Spinach  
    Pear  
    Peas  
    Apple  
    Orange  
    Broccoli  
    Spinach  
    Pear  
    Peas
    
    Now, we know there are 4 Apples. and 3 Orange. So I want to extract the data into
    
    Apple  
    Apple  
    Apple  
    Apple  
    Orange  
    Orange  
    Orange
    
    Anyone has idea?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1481209)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [July 19, 2017 at 11:55 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1482352)
        
        Sorting the data?
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1482352)
        
        *   ![](https://secure.gravatar.com/avatar/3bd9345d4324d3cc01e769163e5dad5f426b42ef833b59f9137dacc1b23c8d1f?s=64&d=mm&r=g) ron maltase says:
            
            [August 24, 2017 at 7:58 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1502453)
            
            Chandoo, cand you help me, please! I'm using this formula {IF(COUNTIFS(MS4download!$C$2:$C$19999,$B$1,MS4download!$E$2:$E$19999,DAILYREPORT332!$A$15)<ROWS($B15:B$15),"",INDEX(MS4download!$F$2:$F$19999,SMALL(IF((MS4download!$C$2:$C$19999=$B$1)+(MS4download!$E$2:$E$19999=DAILYREPORT332!$A$15)=2,ROW(MS4download!$F$2:$F$19999)),ROW(F1))))} to retrieve values from a long table. It using two criteria to qualify the data, one is $b$1, and the second is $A$15. Its close, but I need help, PLEASE! The formula is using the two criteria correctly, but it’s pulling back repeating values from the list? There are only 9 unique values that meet the criteria, yet it pulling back all 110 lines that meet the criteria. I only want it to pull back each value that meets the criteria, ONCE. –Thanks, Ron M.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1502453)
            
33.  ![](https://secure.gravatar.com/avatar/b6d62702fe6a1eeb64713997f559813c7fd0148d977f10dd549f2f60d4ffee88?s=64&d=mm&r=g) Nisar Ahmad says:
    
    [February 14, 2019 at 12:50 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1622259)
    
    Wonderful tutorial. Learned a lot.
    
    But I seem to fail at modifying it to my problem which is, list all those names ( in column A), whose salaries ( in column B) are BETWEEN a number in D1 and D2. Your help would be greatly appreciated.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1622259)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [February 14, 2019 at 2:17 pm](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1622273)
        
        @Nisar
        
        Try:  
        \=IF(COUNTIFS($B:$B,">"&$D$1,$B:$B,"<"&$D$2)$D$1)+($B$2:$B$500<$D$29)=2,ROW($C$2:$C$500)),ROW(C1)))) If that doesn't work, please post the question in the Forums [https://chandoo.org/forum/](https://chandoo.org/forum/)
          
        and attach a sample file so we can check the solution
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1622273)
        
34.  ![](https://secure.gravatar.com/avatar/02337b27e93117a68e29453db006dee172e29745800008e1ba7e386273cb1010?s=64&d=mm&r=g) faecal says:
    
    [September 5, 2019 at 2:18 am](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1684470)
    
    One problem i have is if you have blanks cells it will return a zero. Is there a way to return a blank if its a true blank cell or some other code (#N/A) if it finds a true blank cell? The data could also have legitimate 0's as well as blank cells.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#comment-1684470)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-003b-lukes-reward-part-ii/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [CP025: Sexy on spreadsheet, Ugly on Printout](https://chandoo.org/wp/cp025-sexy-on-spreadsheet-ugly-on-printout/) | [Looking up when data won’t play nice – few more alternatives](https://chandoo.org/wp/looking-up-when-data-wont-play-nice-few-more-alternatives/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
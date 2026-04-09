# Sumerian Voter Problem [IF formula homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/sumerian-voter-problem

---

Sumerian Voter Problem \[IF formula homework\]
==============================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 136 comments

  

Here is a simple IF formula challenge for you. Go ahead and post your answers in the comments section.

### Can this person vote in Sumeria?

Imagine you are the chief election officer in the great country of Sumeria. You have introduced a new eligibility criteria for voters just before the grand presidential elections of 2016. In order to vote,

*   Male citizens must be 21 years or older
*   Female citizens must be 18 years or older
*   Non-citizens can vote if they are 24 years or older and have been living in Sumeria since 1st of Jan 2006.
*   Age should be calculated as of TODAY. For the purpose of age calculation, one year = 365 days.

So on one snowy April morning (it snows every month in Sumeria!), you find yourself staring at the Sumerian voter list. You need to find out if each person on that list can actually vote.

![sumerian-voters](https://chandoo.org/wp/wp-content/uploads/2016/04/sumerian-voters.png)

What formula would you write in the **can vote?** column.

Feel free to use below structural names or cell references in your answer.

*   \[@Gender\] or C4
*   \[@\[Date of Birth\]\] or D4
*   \[@Citizen\] or E4
*   \[@\[Resident Since\]\] or F4

**Go ahead and figure out the formula**

And share your answers in the comments section.

**[Download the Sumerian voter list](https://chandoo.org/wp/wp-content/uploads/2016/04/sumerian-voter-list.xlsx)
** if you want practice data.

**NOTE:** When posting >= or > symbols in the formula, replace them with GTE or GT. Otherwise, wordpress (my blogging software) will eat up your > symbols.

Related: [An IF formula challenge for you](http://chandoo.org/wp/2012/04/25/if-formula-challenge-for-you/)
 and [How to write business logic in Excel formulas](http://chandoo.org/wp/2015/01/22/cp028-how-to-tell-business-logic-rules-to-excel/)

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
| Written by Chandoo  <br>Tags: [and()](https://chandoo.org/wp/tag/and/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [Excel 101](https://chandoo.org/wp/tag/excel-101/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [OR() excel formula](https://chandoo.org/wp/tag/or-excel-formula/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 136 Responses to “Sumerian Voter Problem \[IF formula homework\]”

1.  ![](https://secure.gravatar.com/avatar/bc8a0dbcbe57940f0690670a6505cd90834803f6849fc3fde948c478b058caae?s=64&d=mm&r=g) Jake says:
    
    [April 22, 2016 at 9:15 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173111)
    
    I've gone for this:
    
    \=IF(E4="no",IF(AND(D4=DATEVALUE("01/01/2006")),"yes","no"),IF(OR(AND(C4="male",(D4<=(DATE(YEAR(TODAY()),MONTH(TODAY()),DAY(TODAY()))-(21\*365)))),AND(C4="female",(D4<=(DATE(YEAR(TODAY()),MONTH(TODAY()),DAY(TODAY()))-(18\*365))))),"yes","no"))
    
    Seems to work, although I'm sure someone can work out something that’s less complicated!
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173111)
    
    *   ![](https://secure.gravatar.com/avatar/bc8a0dbcbe57940f0690670a6505cd90834803f6849fc3fde948c478b058caae?s=64&d=mm&r=g) Jake says:
        
        [April 22, 2016 at 9:48 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173126)
        
        Correction, should be:
        
        \=IF(E4="no",IF(D4=DATEVALUE("01/01/2006"),"yes","no"),IF(OR(AND(C4="male",(D4<=(DATE(YEAR(TODAY()),MONTH(TODAY()),DAY(TODAY()))-(21\*365)))),AND(C4="female",(D4<=(DATE(YEAR(TODAY()),MONTH(TODAY()),DAY(TODAY()))-(18\*365))))),"yes","no"))
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173126)
        
        *   ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
            
            [April 22, 2016 at 2:42 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173354)
            
            @Jake your formula doesn't take account of when non-citizens took up residence in the country. To fix that, you'd need to change the first part of your formula as follows:
            
            \=IF(E4="no",IF(F4<=DATEVALUE("01/01/2006"),...
            
            However, even with this, I think your formula is still wrong. You need to ask if the non-citizen is over 24, which you haven't done. In other words, someone who entered the country on or before 1/1/2006 can vote, even if they're only 10 years of age!
            
            [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173354)
            
2.  ![](https://secure.gravatar.com/avatar/e4e88fc595be4712b0ea0049fbc8481fc5e4f691b80ae96307b3c42d709df2d1?s=64&d=mm&r=g) [gsvirdi](http://virdigs.blogspot.com/)
     says:
    
    [April 22, 2016 at 9:27 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173115)
    
    most raw formula which I can come up with is:  
    \=IF(\[@Citizen\]="Yes",IF(OR(AND(\[@Gender\]="Male",TEXT(TEXT(TODAY()-\[@\[Date of Birth\]\],0)/365,0)>="21"),AND(\[@Gender\]="Female",TEXT(TEXT(TODAY()-\[@\[Date of Birth\]\],0)/365,0)>="18")),"Yes","No"),IF(TEXT(TEXT(TODAY()-\[@\[Resident Since\]\], 0)/365, 0)>="24","Yes.","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173115)
    
    *   ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
        
        [April 22, 2016 at 2:46 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173361)
        
        @gsvidri This formula doesn't work correctly. If someone is not a citizen, your formula only checks if they have been in the country more than 24 years. However it should check if they've been here since 1/1/2006 and if their date of birth is more than 24 years ago.
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173361)
        
    *   ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
        
        [April 22, 2016 at 2:47 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173362)
        
        @gsvirdi I got your name wrong in the previous comment. Apologies.
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173362)
        
3.  ![](https://secure.gravatar.com/avatar/490869133f1e07e3932af39e8bab01a8f5e84e658d99b8fe940666269ffbad7a?s=64&d=mm&r=g) James says:
    
    [April 22, 2016 at 9:28 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173117)
    
    \=SUMPRODUCT(  
    (--(\[@Citizen\]="Yes")\*--(\[@Gender\]="Male")\*--(DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y")>=21))+  
    (--(\[@Citizen\]="Yes")\*--(\[@Gender\]="Female")\*--(DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y")>=18))+  
    (--(\[@Citizen\]="No")\*--(DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y")>=24)\*--(\[@\[Resident Since\]\]<=DATEVALUE("01/01/2006"))))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173117)
    
    *   ![](https://secure.gravatar.com/avatar/270b84cfd152229a12ad59e1d5bd7a3b7c3f8e1f7b2fc7e45468bb38d37697fc?s=64&d=mm&r=g) Rob T says:
        
        [April 22, 2016 at 3:53 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173408)
        
        I went the SUMPRODUCT route too, and started off with (effectively) the same as James.  
        Then I reduced it down, eliminating duplication by moving the resident check and gender check to the DOB section, and the citizen check also to the Resident Since section (ensuring this section always returns TRUE for citizens).  
        The resulting formula is:  
        \=IF(SUMPRODUCT(  
        ((\[@\[Date of Birth\]\]<=(TODAY()-(  
        IF(\[@Citizen\]="No",24,  
        IF(\[@Gender\]="Male",21,18))\*365))))  
        \*(\[@\[Resident Since\]\]<=  
        IF(\[@Citizen\]="Yes",\[@\[Resident Since\]\],DATE(2006,1,1)))  
        )=0,"No","Yes")
        
        If 1 or 0 are sufficient, can omit the outer IF(...=0,"No","Yes").
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173408)
        
4.  ![](https://secure.gravatar.com/avatar/f7885cb882908ebe04e09fdb8a30c692938eb21650bd72f6c9d19c1a87efb412?s=64&d=mm&r=g) [Amit Goyal](http://www.akgoyal.com/)
     says:
    
    [April 22, 2016 at 9:44 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173122)
    
    \=IF(\[@Citizen\]="Yes",OR(AND(\[@Gender\]="Male",((TODAY()-\[@\[Date of Birth\]\])/365) GTE 21),AND(\[@Gender\]="Female",((TODAY()-\[@\[Date of Birth\]\])/365) GTE 18)),(AND((TODAY()-\[@\[Date of Birth\]\])/365 GTE 24,\[@\[Resident Since\]\] GTE DATE(2006,1,1))))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173122)
    
5.  ![](https://secure.gravatar.com/avatar/f7885cb882908ebe04e09fdb8a30c692938eb21650bd72f6c9d19c1a87efb412?s=64&d=mm&r=g) [Amit Goyal](http://www.akgoyal.com/)
     says:
    
    [April 22, 2016 at 9:45 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173124)
    
    Somehow the GTE did not convert to >=
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173124)
    
    *   ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
        
        [April 22, 2016 at 2:54 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173371)
        
        @Amit Goyal I think your formula is almost correct, apart from at the very end, it should check if the \[@\[Resident Since\]\] is LTE Date(2006,1,1), i.e., before or on that date.
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173371)
        
6.  ![](https://secure.gravatar.com/avatar/19943016a87ec8d519e7b22345040aaff34f7c4f5eb5307f94f956ae584404d8?s=64&d=mm&r=g) Grondmaster says:
    
    [April 22, 2016 at 10:50 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173147)
    
    \=IF(\[@Citizen\]="Yes",IF(\[@Gender\]="Male",IF(((TODAY()-\[@\[Date of Birth\]\])/365)>20,"Yes","No"),IF(((TODAY()-\[@\[Date of Birth\]\])/365)>17,"Yes","No")),IF(\[@\[Resident Since\]\]<NUMBERVALUE(DATE(2006,1,1)), IF(((TODAY()-\[@\[Date of Birth\]\])/365)>23,"Yes","No"),"No"))
    
    using > & < instead of GT & GTE et al.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173147)
    
7.  ![](https://secure.gravatar.com/avatar/2e6abaf5ac49344b95f76181c0d2c52d1cb33bf95c3606caec5af112482bfc3d?s=64&d=mm&r=g) [MF](http://wmfexcel.com/)
     says:
    
    [April 22, 2016 at 11:02 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173161)
    
    \=(DATEDIF(\[@\[Date of Birth\]\],TODAY(),"Y")>=IF(\[@Gender\]="Male",21,18))\*(\[@Citizen\]="Yes")+(\[@Citizen\]="No")\*(\[@\[Resident Since\]\]=24
    
    I did put an IF in my formula 🙂
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173161)
    
    *   ![](https://secure.gravatar.com/avatar/2e6abaf5ac49344b95f76181c0d2c52d1cb33bf95c3606caec5af112482bfc3d?s=64&d=mm&r=g) [MF](http://wmfexcel.com/)
         says:
        
        [April 22, 2016 at 11:03 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173164)
        
        Hey, wordpress did not eat up the ">="...
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173164)
        
        *   ![](https://secure.gravatar.com/avatar/2e6abaf5ac49344b95f76181c0d2c52d1cb33bf95c3606caec5af112482bfc3d?s=64&d=mm&r=g) [MF](http://wmfexcel.com/)
             says:
            
            [April 22, 2016 at 12:47 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173259)
            
            but it ate every thing in between .....  
            my formula should be  
            \=(DATEDIF(\[@\[Date of Birth\]\],TODAY(),"Y")GTE.IF(\[@Gender\]="Male",21,18))\*(\[@Citizen\]="Yes")+(\[@Citizen\]="No")\*(\[@\[Resident Since\]\]LTE.(DATE(2006,1,1)))\*DATEDIF(\[@\[Date of Birth\]\],TODAY(),"Y")GTE.24
            
            where GTE. >=  
            LTE. <=
            
            [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173259)
            
8.  ![](https://secure.gravatar.com/avatar/7761facc828b80c3190413802e562e69de95de62a617564461662ccb4ff35ce7?s=64&d=mm&r=g) MikeB says:
    
    [April 22, 2016 at 11:12 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173167)
    
    \=IF(AND(\[@Citizen\]="YES",OR(AND(\[@Gender\]="MALE",\[@\[Date of Birth\]\]<=TODAY()-(365\*21)),AND(\[@Gender\]="Female",\[@\[Date of Birth\]\]<=TODAY()-(365\*18)))),1,IF(OR(\[@\[Date of Birth\]\]<=TODAY()-(365\*24),\[@\[Resident Since\]\]<=1/1/2006),1,0))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173167)
    
9.  ![](https://secure.gravatar.com/avatar/0a8cf4d0ff38419149ae34d9d63e63af9992b157706d9ad7806778712e139182?s=64&d=mm&r=g) UG says:
    
    [April 22, 2016 at 11:25 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173170)
    
    \=IF(\[@Citizen\]="No",IF(AND(((TODAY()-\[@\[Date of Birth\]\])/365>24),\[@\[Resident Since\]\]21)),"Yes",IF(AND(\[@Gender\]="Female",((TODAY()-\[@\[Date of Birth\]\])/36Usman5>18)),"Yes","No")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173170)
    
10.  ![](https://secure.gravatar.com/avatar/0a8cf4d0ff38419149ae34d9d63e63af9992b157706d9ad7806778712e139182?s=64&d=mm&r=g) UG says:
    
    [April 22, 2016 at 11:25 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173171)
    
    \=IF(\[@Citizen\]="No",IF(AND(((TODAY()-\[@\[Date of Birth\]\])/365>24),\[@\[Resident Since\]\]21)),"Yes",IF(AND(\[@Gender\]="Female",((TODAY()-\[@\[Date of Birth\]\])/365>18)),"Yes","No")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173171)
    
11.  ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
    
    [April 22, 2016 at 12:23 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173214)
    
    \=IF(INT((TODAY()-\[@\[Date of Birth\]\])/365) .GTE. 18,IF(\[@Citizen\]="Yes",IF(\[@Gender\]="female","VOTE",IF(INT((TODAY()-\[@\[Date of Birth\]\])/365) .GTE. 21,"VOTE","")),IF(INT((TODAY()-\[@\[Date of Birth\]\])/365) .GTE. 24,IF(\[@\[Resident Since\]\]=18
    
    Next, are you a citizen? If yes, are you female? is so, you can VOTE.  
    IF(\[@Citizen\]="Yes",IF(\[@Gender\]="female","VOTE"
    
    If not female, then you're Male, but are you over 21? If so, you can VOTE, if not, No Vote.  
    IF(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=21,"VOTE",""))
    
    For those who aren't citizens, are you over 24?  
    IF(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=24  
    If not, No Vote.
    
    If you are over 24, have you lived here since 1/1/2006?  
    IF(\[@\[Resident Since\]\]<=DATE(2006,1,1)  
    If so, you can VOTE.
    
    Otherwise, No Vote.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173214)
    
    *   ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
        
        [April 22, 2016 at 12:25 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173223)
        
        Sorry, messed up on inserting that formula. Here it is again:
        
        \=IF(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=18,IF(\[@Citizen\]="Yes",IF(\[@Gender\]="female","VOTE",IF(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=21,"VOTE","")),IF(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=24,IF(\[@\[Resident Since\]\]=18
        
        Next, are you a citizen? If yes, are you female? is so, you can VOTE.  
        IF(\[@Citizen\]="Yes",IF(\[@Gender\]="female","VOTE"
        
        If not female, then you're Male, but are you over 21? If so, you can VOTE, if not, No Vote.  
        IF(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=21,"VOTE",""))
        
        For those who aren't citizens, are you over 24?  
        IF(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=24  
        If not, No Vote.
        
        If you are over 24, have you lived here since 1/1/2006?  
        IF(\[@\[Resident Since\]\]<=DATE(2006,1,1)  
        If so, you can VOTE.
        
        Otherwise, No Vote.
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173223)
        
12.  ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
    
    [April 22, 2016 at 12:26 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173226)
    
    Third time lucky, I don't know what's happening here, but if this doesn't work, I'm giving up:
    
    \=IF(INT((TODAY()-\[@\[Date of Birth\]\])/365) .GTE. =18,IF(\[@Citizen\]="Yes",IF(\[@Gender\]="female","VOTE",IF(INT((TODAY()-\[@\[Date of Birth\]\])/365) .GTE. 21,"VOTE","")),IF(INT((TODAY()-\[@\[Date of Birth\]\])/365) .GTE. 24,IF(\[@\[Resident Since\]\]<=DATE(2006,1,1),"VOTE",""),"")),"")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173226)
    
13.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [April 22, 2016 at 12:50 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173263)
    
    My suggested formula resides within the linked picture.
    
    [http://s31.postimg.org/jbbfr9juj/NONAME.png](http://s31.postimg.org/jbbfr9juj/NONAME.png)
    
    \=IF(OR((E4="No")\*(TODAY()-D4 GTE 24\*365)\*(F4 STE --"1/1/2006"),((C4="Male")\*(TODAY()-D4 GTE 21\*365))+((C4 NOT EQUAL "Male")\*TODAY()-D4>=18\*365)),"Yes","No")
    
    Michael Avidan  
    ISRAEL
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173263)
    
    *   ![](https://secure.gravatar.com/avatar/036392219fa42f7d54e74786f1e7bc769c17f67a3361e3ddb8a77d92c3db9647?s=64&d=mm&r=g) SunnyKow says:
        
        [April 23, 2016 at 4:18 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173670)
        
        Hi Michael  
        Your formula does not seems to work properly for non-citizen. I suspect it is the RESIDENT SINCE date calculation where you put the double negative to force the text date 1/1/2006 to a value for comparison.  
        Eg.  
        Voter ID Citizen Resident Since Can vote?  
        SV-000.041 No 4 Apr / 2006 Yes  
        SV-000.086 No 17 Apr / 2008 Yes  
        SV-000.106 No 12 Oct / 2010 Yes  
        SV-000.126 No 29 Jul / 2007 Yes  
        The answers should be No instead of Yes.
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173670)
        
14.  ![](https://secure.gravatar.com/avatar/d1c5834140d6e6cb54eddbf0d261c8e1d6c1a6d2da686158c3f97de7c66e5aa5?s=64&d=mm&r=g) [Kapil Marwaha](https://www.truedata.in/)
     says:
    
    [April 22, 2016 at 1:50 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173320)
    
    This looks good and works on the demo excel sheet.. Please check & confirm.. Thank you for this Home work, Chandoo 🙂
    
    \=IF(\[@Citizen\]="Yes",IF(OR(AND(\[@Gender\]="Male",(TODAY()-\[@\[Date of Birth\]\])/365 >= 21),(AND(\[@Gender\]="Female",(TODAY()-\[@\[Date of Birth\]\])/365 >= 18))),"Yes","No"),IF(AND((TODAY()-\[@\[Date of Birth\]\])/365 >= 24, (\[@\[Resident Since\]\]<= DATE(2006,1,1))),"Yes","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173320)
    
15.  ![](https://secure.gravatar.com/avatar/7251e975cc6743cce4a9a5fb86e52b75cafd08d701852d054f4b2133fb0436ef?s=64&d=mm&r=g) Steve Stafford says:
    
    [April 22, 2016 at 1:55 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173325)
    
    Used the R1C1 cell reference to create a Formula > Name “ageyears”. “Ageyears” referred to:  
    \=DATEDIF(data!RC\[-3\],TODAY(),"y").
    
    In the “Can Vote?” column, then used this formula: =IF(OR(AND(\[@Citizen\]="yes",\[@Gender\]="male",ageyears>=21),AND(\[@Citizen\]="yes",\[@Gender\]="female",ageyears>=18),AND(\[@Citizen\]="no",\[@\[Resident Since\]\]=24)),"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173325)
    
    *   ![](https://secure.gravatar.com/avatar/7251e975cc6743cce4a9a5fb86e52b75cafd08d701852d054f4b2133fb0436ef?s=64&d=mm&r=g) Steven Stafford says:
        
        [April 22, 2016 at 4:52 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173423)
        
        Not sure why but when formula was copied and pasted a key element was left out. Here is revised formula;
        
        Used the R1C1 cell reference to create a Formula > Name “ageyears”. “Ageyears” referred to:  
        \=DATEDIF(data!RC\[-3\],TODAY(),"y").
        
        In the “Can Vote?” column, then used this formula: =IF(OR(AND(\[@Citizen\]="yes",\[@Gender\]="male",ageyears>=21),AND(\[@Citizen\]="yes",\[@Gender\]="female",ageyears>=18),AND(\[@Citizen\]="no",\[@\[Resident Since\]\]=24)),"Yes","No"
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173423)
        
        *   ![](https://secure.gravatar.com/avatar/7251e975cc6743cce4a9a5fb86e52b75cafd08d701852d054f4b2133fb0436ef?s=64&d=mm&r=g) Steven Stafford says:
            
            [April 22, 2016 at 5:01 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173426)
            
            Unsure why but when I post, even though it appears correct in the message area, there is a piece of the final "AND" clause that is left out. This clause looks to see if the resident was there prior to 1/1/06 (I assumed that it was inclusive of 1/1/06).
            
            The final "AND" clause should read;
            
            "AND(\[@Citizen\]="no",\[@\[Resident Since\]\]=24)"
            
            Ok this looks right in the message window, Now I'll submit.
            
            [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173426)
            
            *   ![](https://secure.gravatar.com/avatar/7251e975cc6743cce4a9a5fb86e52b75cafd08d701852d054f4b2133fb0436ef?s=64&d=mm&r=g) Steven Stafford says:
                
                [April 22, 2016 at 5:02 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173427)
                
                Didn't work again, but think you get idea.
                
                [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173427)
                
                *   ![](https://secure.gravatar.com/avatar/616e79633c417a50d356e09298f5f31106f0a916c43eb33ed73360cd52b9f636?s=64&d=mm&r=g) hbillions says:
                    
                    [April 22, 2016 at 5:19 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173436)
                    
                    Now i understand Steve. Happened to me too; twice!
                    
16.  ![](https://secure.gravatar.com/avatar/7251e975cc6743cce4a9a5fb86e52b75cafd08d701852d054f4b2133fb0436ef?s=64&d=mm&r=g) Steven Stafford says:
    
    [April 22, 2016 at 2:16 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173342)
    
    Used the R1C1 cell reference to create a Formula > Name “ageyears”. “Ageyears” referred to:  
    \=DATEDIF(data!RC\[-3\],TODAY(),"y").
    
    In the “Can Vote?” column, then used this formula: =IF(OR(AND(\[@Citizen\]="yes",\[@Gender\]="male",ageyears>=21),AND(\[@Citizen\]="yes",\[@Gender\]="female",ageyears>=18),AND(\[@Citizen\]="no",\[@\[Resident Since\]\]=24)),"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173342)
    
17.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [April 22, 2016 at 2:21 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173346)
    
    D2 = TODAY()  
    F2 = 1/1/2016  
    G2 = Male
    
    \=IF(E4="No",F4>$F$2,($D$2-D4)/365>IF(C4=$G$2,20,17))
    
    Regards
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173346)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [April 22, 2016 at 2:33 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173350)
        
        @Elias,  
        Assuming you meant 1/1/2006 in cell F2 (not 1/1/2016) please check voter ID. SV-000.001  
        He is a MALE, a CITIZEN and "only" 20.15 Years old.  
        Your suggested formula returns TRUE for him.
        
        Voter ID: SV-000.011 in NOT a Citizen but she is "only" 12.31 Years old.  
        Your suggested formula returns TRUE for her.  
        \--------------------------------------  
        Michael Avidan  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173350)
        
        *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
            
            [April 22, 2016 at 7:20 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173472)
            
            Fixed
            
            \=IF(E4="No",AND(F4+1>$F$2,($D$2-D4)/365 GTE 24),($D$2-D4)/365 GTE IF(C4=$G$2,21,18))
            
            Elias
            
            [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173472)
            
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [April 22, 2016 at 7:31 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173476)
                
                @Elias,  
                Your current formula also returns TRUE for the voter ID. SV-000.001 who did not reach the age of 21 yet.  
                Assuming my suggested formula returns the expected results - please check/compare at leat 200 Voters to be sure your formula returns the same.  
                \--------------------------------------  
                Michael Avidan  
                ISRAEL
                
                [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173476)
                
                *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
                    
                    [April 23, 2016 at 5:09 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173886)
                    
                    @Michael
                    
                    For that particular voter and all the Citizens my formula is returning the correct results. However, it needs a little change to work correctly with No citizens.
                    
                    \=IF(E44="No",AND(F44 LTE $F$2,($D$2-D44)/365 GTE 24),($D$2-D44)/365 GTE IF(C44=$G$2,21,18))
                    
                    Also, you may want to review your formula because it is returning wrong results for No citizens
                    
                    Regards
                    
18.  ![](https://secure.gravatar.com/avatar/85bf103b9c66b8a22bf9467a537acdb28cb17fc10140116b29b0bbd4bb1497fc?s=64&d=mm&r=g) Wanderlei Santos says:
    
    [April 22, 2016 at 2:55 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173375)
    
    \=AND(((TODAY()-\[@\[Date of Birth\]\])/365) GTE IF(\[@Citizen\]="Yes",IF(\[@Gender\]="Male",21,18),24),OR(\[@Citizen\]="Yes",AND(\[@\[Resident Since\]\] NE "",\[@\[Resident Since\]\] LTE DATE(2006,1,1))))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173375)
    
19.  ![](https://secure.gravatar.com/avatar/85bf103b9c66b8a22bf9467a537acdb28cb17fc10140116b29b0bbd4bb1497fc?s=64&d=mm&r=g) Wanderlei Santos says:
    
    [April 22, 2016 at 3:11 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173389)
    
    new simpler formula:  
    \=AND(((TODAY()-\[@\[Date of Birth\]\])/365)>=IF(\[@Citizen\]="Yes",IF(\[@Gender\]="Male",21,18),24),OR(\[@Citizen\]="Yes",\[@\[Resident Since\]\]<=DATE(2006,1,1)))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173389)
    
20.  ![](https://secure.gravatar.com/avatar/5be12b64a28ff934f6930846fbcf3175ec8e29a5db26bd1eb730d4825458be7a?s=64&d=mm&r=g) Mike Marshall says:
    
    [April 22, 2016 at 4:38 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173420)
    
    \=IF(OR(  
    AND(\[@Citizen\]="No",(TODAY()-\[@\[Date of Birth\]\])/365 GTE 24,\[@\[Resident Since\]\] GTE DATE(2006,1,1)),  
    AND(\[@Citizen\]="Yes",\[@Gender\]="Male",(TODAY()-\[@\[Date of Birth\]\])/365 GTE 21),  
    AND(\[@Citizen\]="Yes",\[@Gender\]="Female",(TODAY()-\[@\[Date of Birth\]\])/365 GTE 18)),  
    "Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173420)
    
21.  ![](https://secure.gravatar.com/avatar/3dac65172e74763ba0552527162e677c628b03e661d3ce917a91b6725f6dec22?s=64&d=mm&r=g) Mia Munn says:
    
    [April 22, 2016 at 5:03 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173428)
    
    With reason if can't vote (MC<18, FC<18, NC21\*365,"Y","MC18\*365,"Y","FC24\*365,"Y","NC<24"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173428)
    
    *   ![](https://secure.gravatar.com/avatar/3dac65172e74763ba0552527162e677c628b03e661d3ce917a91b6725f6dec22?s=64&d=mm&r=g) Mia Munn says:
        
        [April 22, 2016 at 5:21 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173437)
        
        Forgot the Non Citizen resident clause (and forgot to convert > to GT:
        
        \=IF(Citizen="Yes",IF(Gender="Male",IF(TODAY()-\[@\[Date of Birth\]\] GT 21\*365,"Y","MC<21"),IF(TODAY()-\[@\[Date of Birth\]\] GT 18\*365,"Y","FC<18")),IF(TODAY()-\[@\[Date of Birth\]\] GT 24\*365,IF(\[@\[Resident Since\]\]-42370 GTE 0,"Y","NCNR"),"NC<24"))
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173437)
        
22.  ![](https://secure.gravatar.com/avatar/02522cffb869fc88bc67d4218fbb8b28c0dd42e24a97bde69b68bf14bd201d37?s=64&d=mm&r=g) Ellaysee says:
    
    [April 22, 2016 at 5:04 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173429)
    
    So many ways to get there! Here's mine...
    
    \=IF(OR(AND(\[@Citizen\]="yes",\[@Gender\]="male",(TODAY()-\[@\[Date of Birth\]\])/365 GTE 21),AND(\[@Citizen\]="yes",\[@Gender\]="female",(TODAY()-\[@\[Date of Birth\]\])/365 GTE 18),AND(\[@Citizen\]="no",(TODAY()-\[@\[Date of Birth\]\])/365 GTE 24,\[@\[Resident Since\]\] LTE DATE(2006,1,1))),"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173429)
    
23.  ![](https://secure.gravatar.com/avatar/a49db62c450d92ee3555e3d457441297cb40b7cf6c822daaf4e847d477a303e6?s=64&d=mm&r=g) Ashish Dabral says:
    
    [April 22, 2016 at 5:05 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173430)
    
    \=IF(AND(voters\[\[#This Row\],\[Gender\]\]="Male",DATEDIF(voters\[\[#This Row\],\[Date of Birth\]\],TODAY(),"Y")>=21,voters\[\[#This Row\],\[Citizen\]\]="Yes"),"Yes",IF(AND(voters\[\[#This Row\],\[Gender\]\]="Female",DATEDIF(voters\[\[#This Row\],\[Date of Birth\]\],TODAY(),"Y")>=18,voters\[\[#This Row\],\[Citizen\]\]="Yes"),"Yes",IF(AND(voters\[\[#This Row\],\[Resident Since\]\]<=DATE(2006,1,1),voters\[\[#This Row\],\[Resident Since\]\]"",DATEDIF(voters\[\[#This Row\],\[Date of Birth\]\],TODAY(),"Y")>=24),"Yes","No")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173430)
    
24.  ![](https://secure.gravatar.com/avatar/616e79633c417a50d356e09298f5f31106f0a916c43eb33ed73360cd52b9f636?s=64&d=mm&r=g) hbillions says:
    
    [April 22, 2016 at 5:09 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173431)
    
    Here's my first attempt below.
    
    \=IF(AND(Gender&Citizen="MaleYes",DATEDIF(Date\_of\_Birth,TODAY(),"y")>=21),"YES",IF(AND(Gender&Citizen="FemaleYes",DATEDIF(Date\_of\_Birth,TODAY(),"y")>=18),"YES",IF(AND(Citizen="No",Resident\_Since=24),"YES","NO")))
    
    Too bad shorter and simpler formulas already proposed? Working to shorten it.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173431)
    
25.  ![](https://secure.gravatar.com/avatar/1987061b30a0a8ee0a72a591a0c58912313f5c5069e4ad6c1901082e0ce375f9?s=64&d=mm&r=g) [Nagaraj](http://www.thesmarttrader.net/)
     says:
    
    [April 22, 2016 at 5:10 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173432)
    
    \=OR(AND(\[@Gender\]="Male",\[@Citizen\]="Yes",INT(TODAY()-\[@\[Date of Birth\]\])/365>=21),AND(\[@Gender\]="Female",\[@Citizen\]="Yes",INT(TODAY()-\[@\[Date of Birth\]\])/365>=18),AND(\[@Citizen\]="No",\[@\[Resident Since\]\]=24))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173432)
    
26.  ![](https://secure.gravatar.com/avatar/616e79633c417a50d356e09298f5f31106f0a916c43eb33ed73360cd52b9f636?s=64&d=mm&r=g) hbillions says:
    
    [April 22, 2016 at 5:14 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173434)
    
    A portion of the last IF statement was cut-off for some reasons. Here's the full portion of the last IF statement:
    
    ...IF(AND(Citizen="No",Resident\_Since=24),"YES","NO")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173434)
    
27.  ![](https://secure.gravatar.com/avatar/1987061b30a0a8ee0a72a591a0c58912313f5c5069e4ad6c1901082e0ce375f9?s=64&d=mm&r=g) [Nagaraj](http://www.thesmarttrader.net/)
     says:
    
    [April 22, 2016 at 5:15 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173435)
    
    Previous one was an error.
    
    \=OR(AND(\[@Gender\]="Male",\[@Citizen\]="Yes",INT(TODAY()-\[@\[Date of Birth\]\])/365>=21),AND(\[@Gender\]="Female",\[@Citizen\]="Yes",INT(TODAY()-\[@\[Date of Birth\]\])/365>=18),AND(\[@Citizen\]="No",\[@\[Resident Since\]\]=24))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173435)
    
28.  ![](https://secure.gravatar.com/avatar/a8c3882878b5ea21765137806ef35c3c2a964df60b4532429cd2dfb83211ded0?s=64&d=mm&r=g) Steve says:
    
    [April 22, 2016 at 5:39 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173442)
    
    \=IF(SUMPRODUCT((IF(\[@Citizen\]="Yes",1,IF(\[@\[Resident Since\]\]>=38718,1,0)))\*(IF(AND(\[@Gender\]="Female",((TODAY()-\[@\[Date of Birth\]\])/365)>18),1,IF( (TODAY()-\[@\[Date of Birth\]\])/365>21,1,0)))),"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173442)
    
29.  ![](https://secure.gravatar.com/avatar/743a885fe3cb7ca2dbd023ad5e6ee456019017618cd54e3176ede1a9ebbd2368?s=64&d=mm&r=g) Maciej says:
    
    [April 22, 2016 at 6:04 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173448)
    
    The simplest approach is with nested IFs:  
    \=IF(\[@Citizen\]="Yes";IF(\[@Gender\]="Male";DATEDIF(\[@\[Date of Birth\]\];TODAY();"y") GT 20;DATEDIF(\[@\[Date of Birth\]\];TODAY();"y") GT 17);AND(DATEDIF(\[@\[Date of Birth\]\];TODAY();"y") GT 23;\[@\[Resident Since\]\] LE DATE(2016;1;1)))
    
    Here is formula without IFs:  
    \=CHOOSE(LEN(\[@Citizen\]);;AND(DATEDIF(\[@\[Date of Birth\]\];TODAY();"y") GT 23;\[@\[Resident Since\]\] LE DATE(2016;1;1));CHOOSE(LEN(\[@Gender\])/2;;DATEDIF(\[@\[Date of Birth\]\];TODAY();"y") GT 20;DATEDIF(\[@\[Date of Birth\]\];TODAY();"y") GT 17))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173448)
    
30.  ![](https://secure.gravatar.com/avatar/0057d919f5d1c57c0f42994fa8572d1308869bfe5e68cfbb49542c57d3dece0d?s=64&d=mm&r=g) Amjad mahmood says:
    
    [April 22, 2016 at 6:12 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173453)
    
    My solution is user-defined excel function as follows:  
    \=CanVote(B4,C4,D4,E4,F4)
    
    where CanVote is bolean type private funtion
    
    Private Function CanVote (x as bolean)  
    .  
    .  
    .  
    End Function
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173453)
    
31.  ![](https://secure.gravatar.com/avatar/ff138ee081e2c11ccaf682bd91e41bd5fe0ac4de7d722608f36db39b334f538f?s=64&d=mm&r=g) Ted says:
    
    [April 22, 2016 at 8:13 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173490)
    
    This answer tells the reason why (or why not) the person can vote, rather than just yes/no. It could be used for statistics. 🙂
    
    \=IF(\[@Citizen\]="Yes", IF(\[@Gender\]="Male", IF((TODAY()-\[@\[Date of Birth\]\])/365 GTE 21,"Yes- male citizen can vote","No- male citizen too
    
    young"), IF(\[@Gender\]="Female", IF((TODAY()-\[@\[Date of Birth\]\])/365 GTE 18, "Yes- woman citizen ok to vote","No- woman citizen too
    
    young"))), IF(\[@Citizen\]="No", IF((TODAY()-\[@\[Date of Birth\]\])/365 LTE 24, "No- non-citizen too young", IF(\[@\[Resident Since\]\] LT DATE
    
    (2006,1,1), "Yes- non-citizen meets requirements to vote", "No- non-citizen hasn't been resident long enough"))))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173490)
    
32.  ![](https://secure.gravatar.com/avatar/ff138ee081e2c11ccaf682bd91e41bd5fe0ac4de7d722608f36db39b334f538f?s=64&d=mm&r=g) Ted says:
    
    [April 22, 2016 at 8:30 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173496)
    
    Those crazy Sumerians. In the sample data file, 25 had Residency before they were born.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173496)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [April 23, 2016 at 3:28 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173649)
        
        Good find. I blame the Excel's random data generators 😉
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173649)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [April 23, 2016 at 6:50 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173711)
            
            @Chandoo,  
            For my bad English knowledge (and it has onlt to do with GTE or STE) - a NON Citizen will be allowed to vote if he/she are 24 years or older and have been living in Sumeria since 1st. of Jan, 2006.  
            Does this mean that if one is 26 years old and was living in Sumeria on the 25th, Dec. 2005 he/she will not be allowed - or one should have been living since 1st. Jan, 2006 up to Today BUT NOT BEFORE the 1st. Jan, 2006 ?  
            Thanks,  
            Michael Avidan  
            ISRAEL
            
            [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173711)
            
            *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
                 says:
                
                [April 25, 2016 at 4:38 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174443)
                
                In this case, the non citizen can vote.
                
                [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174443)
                
                *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                    
                    [April 26, 2016 at 12:03 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175428)
                    
                    Sorry but I still don't fully understand.  
                    Please refer to the voters in rows: 44, 49 snd 52.  
                    Which one, of them, can vote and who cannot ?  
                    Thanks,  
                    Michael Avidan  
                    ISRAEL
                    
        *   ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
            
            [April 23, 2016 at 12:51 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173817)
            
            Chandoo,
            
            please do not blame the RNG. You could use a formula something like,
            
            RANDBETWEEN(\[@\[Date of Birth\]\],TODAY())
            
            [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173817)
            
            *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
                 says:
                
                [April 25, 2016 at 4:38 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174444)
                
                Of course, the blame is with me. Excel simply produced data based on the formulas I wrote 🙂
                
                [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174444)
                
33.  ![](https://secure.gravatar.com/avatar/12428bcff2de17e39a3d11487abfb732656f76e125fd4f6c3fb658d01af52ba0?s=64&d=mm&r=g) sagar malik says:
    
    [April 22, 2016 at 9:51 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173518)
    
    OR(AND(\[@Citizen\]="Yes",OR(AND(\[@Gender\]="Male",TODAY()-\[@\[Date of Birth\]\] GTE 21\*365),AND(\[@Gender\]="Female",TODAY()-\[@\[Date of Birth\]\] GTE 18\*365))),AND(\[@Citizen\]="No",TODAY()-\[@\[Date of Birth\]\] GTE 24\*365,NOT(ISBLANK(\[@\[Resident Since\]\])),\[@\[Resident Since\]\] LTE DATE(2006,1,1)))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173518)
    
34.  ![](https://secure.gravatar.com/avatar/773cc5ffff20f8c42eff3fb2fc547a46393010f383b3ebb50abba33817febcc4?s=64&d=mm&r=g) martinjust says:
    
    [April 23, 2016 at 12:08 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173560)
    
    \=IF(SUM(SUMPRODUCT((\[@Citizen\]="Yes")\*(\[@Gender\]="Male")\*(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=21)),SUMPRODUCT((\[@Citizen\]="Yes")\*(\[@Gender\]="Female")\*(INT((TODAY()-\[@\[Date of Birth\]\])/365)>=18)),SUMPRODUCT((\[@Citizen\]="No")\*(\[@\[Resident Since\]\]>=DATE(2006,1,1)))\*(\[@age\]>=24)),"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173560)
    
35.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [April 23, 2016 at 2:59 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173640)
    
    \=IF(E4="Yes",IF(C4="Male",21,18),IF(F4<=DATE(2006,1,1),24,999))<=(TODAY()-D4)/365
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173640)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [April 23, 2016 at 5:26 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173892)
        
        @David N,  
        From the few voters on whom I checked your suggested formula I can only say: "Chapeau bas vous !!!"  
        Michael Avidan  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173892)
        
    *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
        
        [April 23, 2016 at 6:49 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173918)
        
        @ David,
        
        I like this one!
        
        Regards
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173918)
        
36.  ![](https://secure.gravatar.com/avatar/87dc4750fec5d41070eb52cc91911c7a933dccd6f4e72859c747bdc8a422179c?s=64&d=mm&r=g) RAC says:
    
    [April 23, 2016 at 5:04 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173685)
    
    \=IF(AND((voters\[\[#This Row\],\[Gender\]\]="Male"),(H4>=21),(voters\[\[#This Row\],\[Citizen\]\]="Yes")),"Yes",IF(AND((voters\[\[#This Row\],\[Gender\]\]="Female"),(H4>=18),(voters\[\[#This Row\],\[Citizen\]\]="Yes")),"Yes",IF(AND((H4>=24),(voters\[\[#This Row\],\[Citizen\]\]="No"),(I4>=3765)),"Yes","No")))
    
    H4 : =DATEDIF(voters\[\[#This Row\],\[Date of Birth\]\],TODAY(),"y")
    
    I4: =IFERROR(DATEDIF(voters\[\[#This Row\],\[Resident Since\]\],TODAY(),"d"),0)
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173685)
    
37.  ![](https://secure.gravatar.com/avatar/73ae4d4b4c74cb80e037083a485b16d5e543b2602fb033199fd56d77f1276c23?s=64&d=mm&r=g) Suryakant Kulkarni says:
    
    [April 23, 2016 at 6:40 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173708)
    
    \=IF(\[@Citizen\]="Yes",IF(AND(\[@Gender\]="Male",YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\])>21),"Yes",IF(AND(\[@Gender\]="Female",YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\])>18),"Yes","No")),IF(AND(YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\])>21,\[@\[Resident Since\]\]<DATE(2006,1,1)),"Yes","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173708)
    
38.  ![](https://secure.gravatar.com/avatar/73ae4d4b4c74cb80e037083a485b16d5e543b2602fb033199fd56d77f1276c23?s=64&d=mm&r=g) Suryakant Kulkarni says:
    
    [April 23, 2016 at 6:55 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173712)
    
    Hi  
    Chandoo,
    
    Just small change in formula,  
    \=IF(\[@Citizen\]="Yes",IF(AND(\[@Gender\]="Male",((TODAY()-\[@\[Date of Birth\]\])/365)>21),"Yes",IF(AND(\[@Gender\]="Female",((TODAY()-\[@\[Date of Birth\]\])/365)>18),"Yes","No")),IF(AND(((TODAY()-\[@\[Date of Birth\]\])/365)>21,\[@\[Resident Since\]\]<DATE(2006,1,1)),"Yes","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173712)
    
39.  ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
    
    [April 23, 2016 at 7:42 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173729)
    
    \=OR(AND((\[@Gender\]="Male"),(TODAY()-\[@\[Date of Birth\]\] GT 365\*21),\[@Citizen\]="Yes"),AND((\[@Gender\]="Female"),(TODAY()-\[@\[Date of Birth\]\] GT 365\*18),\[@Citizen\]="Yes"),AND((TODAY()-\[@\[Date of Birth\]\] GT 365\*24),\[@Citizen\]="No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173729)
    
    *   ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
        
        [April 23, 2016 at 9:01 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173755)
        
        Hi Chandoo,  
        Please accept my modified version.
        
        \=OR(AND((\[@Gender\]="Male"),(TODAY()-\[@\[Date of Birth\]\] GT 365\*21),\[@Citizen\]="Yes"),AND((\[@Gender\]="Female"),(TODAY()-\[@\[Date of Birth\]\] GT 365\*18),\[@Citizen\]="Yes"),AND((TODAY()-\[@\[Date of Birth\]\] GT 365\*24),\[Resident Since\] LT 38718))
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173755)
        
40.  ![](https://secure.gravatar.com/avatar/3c73d030680815be0f341cba1df8023465b3a51dae77656a4e0ab295117c69fb?s=64&d=mm&r=g) Chandra Mohan Singh says:
    
    [April 23, 2016 at 10:11 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173775)
    
    IF(AND(D12="No",VALUE((TODAY()-C12)/365)>=24,E12>=1/1/2006),"Yes",IF(AND(D12="Yes",B12="Male",VALUE((TODAY()-C12)/365)>=21),"Yes",IF(AND(D12="Yes",B12="Female",VALUE((TODAY()-C12)/365)>=18),"Yes","No")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173775)
    
41.  ![](https://secure.gravatar.com/avatar/843a4b770d05ea44bc6e382c51168b2a391df7829c347b0f0608e4f83220c32f?s=64&d=mm&r=g) Gurminder Singh Puri says:
    
    [April 23, 2016 at 12:14 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173806)
    
    The formula to solve the problem is as under :
    
    \=IF(OR(AND(@Gender="M",(TODAY()-@Date Of Birth)/365 GTE 21),AND(@Gender="F",(TODAY()-@Date Of Birth)/365 GTE 18),AND(@Resident Since GTE "01-01-2006",(TODAY()-@Date Of Birth)/365 GTE 24)),"Yes","No")
    
    I am not a big expert, but I have tried to solve the problem. GTE is used for Greater than or equal to and GT is used for Greater Than as advised by you
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173806)
    
42.  ![](https://secure.gravatar.com/avatar/843a4b770d05ea44bc6e382c51168b2a391df7829c347b0f0608e4f83220c32f?s=64&d=mm&r=g) Gurminder Singh Puri says:
    
    [April 23, 2016 at 1:24 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173832)
    
    I have noticed an error in the formula sent by me. Am working on it and will resend after correction. Kindly Excuse.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173832)
    
43.  ![](https://secure.gravatar.com/avatar/35c28f77de45edd59bd2c60771581a44066cbb3a7a818c86eb2149c54033e616?s=64&d=mm&r=g) [Phil](http://excelblog.net/excel-spreadsheet-formulas/)
     says:
    
    [April 23, 2016 at 1:49 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173840)
    
    Hi Chandoo,
    
    nice challenge which very much reminded me of Daniel Ferry's amazing post about I HEART IF.
    
    I wanted to avoid nested IFs by any mean so I chose his approach by applying the numerical values of 0 and 1 for FALSE and TRUE and simply add up all three preconditional stages (male citizen, female citizen, non-citizen)
    
    Here are the steps I took:
    
    To apply readability to the formulas used I first created a few names. First set was the "variables" for the ages.
    
    1\. sumeria.age18 has been defined as =18\*365  
    2\. sumeria.age21 has been defined as =21\*365  
    3\. sumeria.age24 has been defined as =24\*365
    
    I could have used the absolute numbers as well but this helps the future use of this file a little more, because these definitions (CTRL+F3 for the name manager) help better understand what I was doing
    
    Then I placed the cursor in the first row (4) and again hit CTRL+F3 to define another variable for "todays age in days":
    
    4\. age.in.days has been defined as =TODAY()-$D4
    
    Now that I have these "readability issues" solved, it's time to create the formula itself. Here's how I approached it:
    
    As several conditions need to be matched I applied AND - as my fellow Excel buddies did - for each of the three condition sets and added them up. I first checked for male citizens, then female citizens and then non-citizens
    
    \=AND(\[@Gender\]="Male",age.in.days GTE sumeria.age21,\[@Citizen\]="Yes")+AND(\[@Gender\]="Female",age.in.days GTE sumeria.age18,\[@Citizen\]="Yes")+AND(\[@Citizen\]="no",age.in.days>=sumeria.age24,\[@\[Resident Since\]\]=sumeria.age24,\[@\[Resident Since\]\]<="01.01.2006")
    
    Remarks: One could expand the naming part even further by applying names for the other checks - such as defining is.male as =\[@Gender\]="Male" - as well but that was a little "over the top" for me 😉
    
    Hope you like my solution 🙂
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173840)
    
    *   ![](https://secure.gravatar.com/avatar/35c28f77de45edd59bd2c60771581a44066cbb3a7a818c86eb2149c54033e616?s=64&d=mm&r=g) [Phil](http://excelblog.net/excel-spreadsheet-formulas/)
         says:
        
        [April 23, 2016 at 1:52 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173841)
        
        Looks like WOrdpress has cut down some of my content, because I also added a breakdown of the evaluation for each condition set, so here's that missing part 😉
        
        Here are the three parts broken down for each condition set:
        
        MALE CITIZENS (first part, initiated by the = sign):
        
        \=AND(\[@Gender\]="Male",age.in.days GTE sumeria.age21,\[@Citizen\]="Yes")
        
        FEMALE CITIZENS (second part, initiated by the + sign):  
        +AND(\[@Gender\]="Female",age.in.days GTE sumeria.age18,\[@Citizen\]="Yes")
        
        NON-CITIZENS (third part, initiated by another + sign):
        
        AND(\[@Citizen\]="no",age.in.days>=sumeria.age24,\[@\[Resident Since\]\] LTE "01.01.2006")
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173841)
        
44.  ![](https://secure.gravatar.com/avatar/2cfd89a5f664f0bcc55d97031c27c3816a5b5a95d5069df82a1303a7b7dd207c?s=64&d=mm&r=g) Stewart says:
    
    [April 23, 2016 at 2:55 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173857)
    
    I went with a few bits to say WHY they couldn't vote...
    
    IF(\[@\[Resident Since\]\]="",  
    IF(\[@Gender\]="male",  
    IF(DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y") GTE 21,"Yes","No (male, too young)"),  
    IF(\[@Gender\]="Female",IF(DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y") GTE 18,"Yes","No (female, too young)"))),  
    IF(\[@Citizen\]="No",  
    IF(\[@\[Resident Since\]\]<="1/1/2006",  
    IF(DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y") GTE 24,"Yes","No (non-citizen, too young)"),  
    "No (non-citizen, residency too short)"),  
    "No (not citizen and/or failed other rules)"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173857)
    
45.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [April 23, 2016 at 5:42 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173897)
    
    One more without IFs  
    D2 = TODAY()  
    F2 = 1/1/2006  
    G2 = Male
    
    \=AND(($D$2-D4)/365 GTE MAX(24\*(E4="No"),21\*(E4="Yes")\*(C4=$G$2),18\*(E4="Yes")\*(C4$G$2)),(E4="Yes")+(F4 LTE $F$2))
    
    Regards
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173897)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [April 23, 2016 at 6:28 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173907)
        
        @Elias,  
        1) I know my formula is not perfect and in fact I gave up and stopped altering it after I saw David,s formula.  
        2) Please check your last formula for (line 46) voter:  
        \-----------------------------------------------------  
        SV-000.043 Female 01/09/2001 Yes  
        \-----------------------------------------------------  
        She is only 14.65 years old, therefore the result should read: FALSE.
        
        Michael Avidan  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173907)
        
        *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
            
            [April 23, 2016 at 6:44 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173914)
            
            @Michael
            
            I don't know how you are applying my formulas because my last formula and the one I replied to you in a previous comments return FALSE for that voter.
            
            Regards
            
            [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173914)
            
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [April 23, 2016 at 7:34 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173924)
                
                @Elias,  
                As there is a limit of replies in each post - with your permission after this reply, of mine, I will rest my case.  
                I do hope I didn't made any mistake in copying your formula nor changing the GTE respectively.  
                Here is a picture of row 46 voter + your formula + result (shoud be FALSE).  
                \---------------------------------------------------------  
                [http://s31.postimg.org/facmsw123/NONAME.png](http://s31.postimg.org/facmsw123/NONAME.png)
                  
                \---------------------------------------------------------  
                Michael Avidan  
                ISRAEL
                
                [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173924)
                
                *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                    
                    [April 23, 2016 at 7:38 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173925)
                    
                    @Elias,  
                    Please forget about my 7:34 PM reply.  
                    Check out the linked picture - where in row 7589 the result should be FALSE because the voter residency started on: 02/07/2001 which is prior to: 1/1/2006.  
                    \------------------------------------------------------  
                    [http://s31.postimg.org/cjht2qgwr/NONAME.png](http://s31.postimg.org/cjht2qgwr/NONAME.png)
                      
                    \------------------------------------------------------  
                    Thanks for your patience,  
                    Michael Avidan  
                    ISRAEL
                    
46.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [April 24, 2016 at 1:10 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173989)
    
    @Michael,
    
    Sorry you were right. My last formula without IF was not correct. Here is the new version without IF, OR & AND.
    
    ((E4="No")\*24+(E4="Yes")\*(21\*(C4=$G$2)+18\*(C4$G$2)))\*365<=($D$2-D4)\*((E4="Yes")+(E4="No")\*(F4<=$F$2))
    
    Regards
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1173989)
    
47.  ![](https://secure.gravatar.com/avatar/0fcd44cc98f65e936dd28b3edcfc92fcd45bfe98e14237b6b18b95688468748d?s=64&d=mm&r=g) Praveen Bharadwaj K R says:
    
    [April 24, 2016 at 2:55 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174013)
    
    Formula will be as follows
    
    IF(\[@Gender\]="Male",IF(AND(\[@Citizen\]="Yes",\[@Age\]GTE21),"Yes",IF(AND(\[@Citizen\]="No",\[@Age\]GTE24,\[@\[Resident Since\]\]LTEDATE(2006,1,1)),"Yes","No")),IF(AND(\[@Citizen\]="Yes",\[@Age\]GTE18),"Yes",IF(AND(\[@Citizen\]="No",\[@Age\]GTE24,\[@\[Resident Since\]\]GTEDATE(2006,1,1)),"Yes","No")))
    
    Note: GTE Greater Than or Equal to & LTE Less Than or Equal to
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174013)
    
    *   ![](https://secure.gravatar.com/avatar/0fcd44cc98f65e936dd28b3edcfc92fcd45bfe98e14237b6b18b95688468748d?s=64&d=mm&r=g) Praveen Bharadwaj K R says:
        
        [April 24, 2016 at 2:58 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174015)
        
        For Age Calculation I have used following Formula:
        
        INT(YEARFRAC(\[@\[Date of Birth\]\],TODAY()))
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174015)
        
48.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [April 24, 2016 at 7:09 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174087)
    
    @Elias,  
    With all due respect this is my last check/response as for your formula(s).  
    I hope Chandoo will check all the suggestions and reply accordingly.  
    Your last formula returns FALSE for Voter: SV-000.004 although he is a Male & a Citizen & Older than 24 years.  
    To my opinion - an Equal sign (=) is missing within the: C4$G$2 section.  
    I have added it in order for the formula to work.  
    Kind regards,  
    Michael Avidan  
    ISRAEL
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174087)
    
    *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
        
        [April 24, 2016 at 7:39 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174274)
        
        @Michael, I didn't notice the missing sign. It is a different than . Also, my formula returns exactly the same results as David N formula for all the records.
        
        Regards
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174274)
        
49.  ![](https://secure.gravatar.com/avatar/3bbaa9a9d58abbb29ed8a5a873d3d3a1cf7009f2d89acaa1d9b77f6891b49ae3?s=64&d=mm&r=g) Jude Shyju says:
    
    [April 24, 2016 at 9:57 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174142)
    
    OPTION 1
    
    \=IF(E11="Sumeria",IF(OR(AND(C11="Male",TODAY()-D11 GT 365\*21),AND(C11="Female",TODAY()-D11 GT 365\*18)),"Eligible","Not Eligible"),IF(AND(TODAY()-D11 GT 365\*24,F11 LT DATE(2006,1,1)),"Eligible","Not Eligible"))
    
    OPTION 2 (Using SUMPRODUCT)
    
    \=IF(OR(SUMPRODUCT((C10="Male")\*(E10="Sumeria")\*(TODAY()-D10 GT 365\*21)),SUMPRODUCT((C10="Female")\*(E10="Sumeria")\*(TODAY()-D7 GT 365\*18)),SUMPRODUCT(((E10LTGT"Sumeria")\*(TODAY()-D10 GT 365\*24)\*(F10LTDATE(2006,1,1))))),"Eligible","Not Eligible")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174142)
    
50.  ![](https://secure.gravatar.com/avatar/05fd3d0730b041e096ef1221c9479da79f471e508934ba34853fb22553cceb9b?s=64&d=mm&r=g) Jayant says:
    
    [April 24, 2016 at 3:26 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174222)
    
    \=(IF(AND(C4="Male",DATEDIF(D4,TODAY(),"Y")>=21),"Y",(IF(AND(C4="Female",DATEDIF(D4,TODAY(),"Y")>=18),"Y",IF(E4="No",IF((DATEDIF(D4,TODAY(),"Y")>=24),"Y","N"),"N")))))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174222)
    
51.  ![](https://secure.gravatar.com/avatar/2103815b1fda49c963f32f3f61782e0a9b13d11d99537986177d93c90167dc7b?s=64&d=mm&r=g) Jason Morin says:
    
    [April 24, 2016 at 8:42 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174293)
    
    \=(((TODAY()-D4)/365GTE21)\*(C4="Male")+((TODAY()-D4)/365GTE18)\*(C4="Female"))\*(E4="Yes")+((TODAY()-D4)/365GTE24)\*(F4<=DATE(2006,1,1))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174293)
    
52.  ![](https://secure.gravatar.com/avatar/036392219fa42f7d54e74786f1e7bc769c17f67a3361e3ddb8a77d92c3db9647?s=64&d=mm&r=g) SunnyKow says:
    
    [April 25, 2016 at 1:08 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174374)
    
    \=IF(F4="",IF(OR(AND(C4="Male",(TODAY()-D4)/365GE21),AND(C4="Female",(TODAY()-D4)/365GE18)),"Yes","No"),IF(AND(F4LE38718,(TODAY()-D4)/365GE24),"Yes","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174374)
    
53.  ![](https://secure.gravatar.com/avatar/73507e4c059a473735274f3c0b4c3ce2aefae22686b79d972cc4d262e46839bb?s=64&d=mm&r=g) Ashish says:
    
    [April 25, 2016 at 3:58 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174431)
    
    My suggested solution:  
    \=+IF(OR(AND(\[@Citizen\]="Yes",\[@Gender\]="Male",DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y")GTE21),AND(\[@Citizen\]="yes",\[@Gender\]="Female",DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y")GTE18),AND(\[@Citizen\]="No",DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y")GTE24,\[@\[Resident Since\]\]LTEDATE(2006,1,1))),"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174431)
    
54.  ![](https://secure.gravatar.com/avatar/c6516f88ab7c446cc754933f60412a3842ed5a2da5f9277306965698d8f2acc7?s=64&d=mm&r=g) Kapil says:
    
    [April 25, 2016 at 6:24 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174470)
    
    \=IF((--(voters\[@Citizen\]="Yes")\*(--(OR(AND(voters\[@Gender\]="male",((TODAY()-voters\[@\[Date of Birth\]\])/365) GT21),AND(voters\[@Gender\]="Female",((TODAY()-voters\[@\[Date of Birth\]\])/365) GT24)))))+(--(voters\[@Citizen\]="No")\*(--(AND("01-01-2006"GTvoters\[@\[Resident Since\]\],((TODAY()-voters\[@\[Date of Birth\]\])/365)>21))))=1,"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174470)
    
55.  ![](https://secure.gravatar.com/avatar/caa8928e587871d1b40b936c64e48950749f8a31d6d0fd7fa4a43314831c83b9?s=64&d=mm&r=g) Basan0187 says:
    
    [April 25, 2016 at 7:07 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174479)
    
    IF(AND(E4="Yes",C4="Male",((TODAY()-D4)/365)>=21),"Y",IF(AND(E4="Yes",C4="feMale",((TODAY()-D4)/365)>=18),"Y",IF(AND(E4="No",((TODAY()-D4)/365)>=24,F4>=1/1/2006),"Y","N")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174479)
    
56.  ![](https://secure.gravatar.com/avatar/b3dba70d28eb85376897d3f433d1cb164ed9ee4ff7911975ca160a021ef50f10?s=64&d=mm&r=g) Cyril says:
    
    [April 25, 2016 at 7:31 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174485)
    
    Suggested solution:  
    \=IF(\[@Citizen\]="Yes",IF(\[@Gender\]="Male",IF((TODAY()-\[@\[Date of Birth\]\])/365GTE21,"Yes","No"),IF((TODAY()-\[@\[Date of Birth\]\])/365GTE18,"Yes","No")),IF(\[@\[Resident Since\]\]GTE38718,"No",IF((TODAY()-\[@\[Date of Birth\]\])/365GTE24,"Yes","No")))  
    or:  
    \=IF(OR(AND(\[@Citizen\]="Yes",\[@Gender\]="Male",(TODAY()-\[@\[Date of Birth\]\])/365GTE21),AND(\[@Citizen\]="Yes",\[@Gender\]="Female",(TODAY()-\[@\[Date of Birth\]\])/365GTE18),AND(\[@Citizen\]="No",\[@\[Resident Since\]\]<=38718,(TODAY()-\[@\[Date of Birth\]\])/365GTE24)),"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174485)
    
57.  ![](https://secure.gravatar.com/avatar/47c0fbfebeb688973d53d7a76d8034db1d81913d41bf71d3d2bd06a2c3187a85?s=64&d=mm&r=g) Eumelode says:
    
    [April 25, 2016 at 8:52 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174500)
    
    \=IF(@Citizen="No",  
    IF(@Residentsince>DATE(2006,1,1),"No Foreign Young",IF(TODAY()-@0,"Yes","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174500)
    
58.  ![](https://secure.gravatar.com/avatar/633a94145407dd3707bd10363a125d4583873df340cd9b619d4c53b212e60203?s=64&d=mm&r=g) ANKUSH says:
    
    [April 25, 2016 at 10:38 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174520)
    
    \=IF(voters\[\[#This Row\],\[Citizen\]\]="Yes",OR(AND(voters\[\[#This Row\],\[Gender\]\]="Male",((TODAY()-voters\[\[#This Row\],\[Date of Birth\]\])/365)>21),AND(voters\[\[#This Row\],\[Gender\]\]="Female",((TODAY()-voters\[\[#This Row\],\[Date of Birth\]\])/365)>18)),OR(((TODAY()-voters\[\[#This Row\],\[Date of Birth\]\])/365)>=24,voters\[\[#This Row\],\[Resident Since\]\]<DATE(2006,1,1)))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174520)
    
59.  ![](https://secure.gravatar.com/avatar/2f4e95a68e884deb9d0a72c72c2805aa72bbf22247d7cfaf544ebb3bdcae4402?s=64&d=mm&r=g) Alex Groberman says:
    
    [April 25, 2016 at 3:47 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174892)
    
    \=AND(OR(\[@Citizen\]="Yes",\[@\[Resident Since\]\]<=DATE(2006,1,1)),YEARFRAC(\[@\[Date of Birth\]\],TODAY(),3)>=IF(\[@Citizen\]="No",24,IF(\[@Gender\]="Male",21,18)))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1174892)
    
60.  ![](https://secure.gravatar.com/avatar/c3ae645db7d213585cc57b18ec42d0f0a23a6432cbe09e8fd6ca4a98828219fd?s=64&d=mm&r=g) Ben Oshyer says:
    
    [April 25, 2016 at 11:36 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175046)
    
    \=IF(((E4="yes")\*((C4="Male")\*(((TODAY()-D4)/365)>21))+((C4="Female")\*(((TODAY()-D4)/365)>18)))+((E4="No")\*(((TODAY()-D4)/365)>24)\*(AND(F4"",F4>DATE(2006,1,1))))>0,"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175046)
    
61.  ![](https://secure.gravatar.com/avatar/894a5841d14d0373996076ea210c2543530d084c5c815af5a11c63bda41be68e?s=64&d=mm&r=g) Marydas says:
    
    [April 26, 2016 at 5:25 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175131)
    
    \=IF(AND(data!$E4="Yes",data!$C4="Male",YEARFRAC(data!$D4,TODAY(),3)>=21),"Can Vote",IF(AND(data!$E4="Yes",data!$C4="Female",YEARFRAC(data!$D4,TODAY(),3)>=18),"Can Vote",IF(AND(E4="No",YEARFRAC(D4,TODAY(),3)>=24,F4<38718),"Can Vote",0)))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175131)
    
62.  ![](https://secure.gravatar.com/avatar/a65291a8f3f8d7b22c74d24665042e68392ca996aba4fec8158ffad2c7255e3e?s=64&d=mm&r=g) Ash says:
    
    [April 26, 2016 at 6:19 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175153)
    
    Hi Chandoo,
    
    Here's the formula I came up with:
    
    \=IF(\[@Citizen\]="Yes",IF(AND(\[@Gender\]="Male",((TODAY()-\[@\[Date of Birth\]\])/365)>=21),"Yes",IF(AND(\[@Gender\]="Female",((TODAY()-\[@\[Date of Birth\]\])/365)>=18),"Yes","No")),IF(AND((TODAY()-\[@\[Date of Birth\]\])/365>=24,\[@\[Resident Since\]\]<=DATE(2006,1,1)),"Yes","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175153)
    
63.  ![](https://secure.gravatar.com/avatar/460be5157a8ff55b9ffdf755dce4658a7d42130b5bda58c43f07368eb6088d00?s=64&d=mm&r=g) Daniel H says:
    
    [April 26, 2016 at 11:50 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175425)
    
    \=OR(AND(\[@\[Resident Since\]\]>DATE(2015,12,31),DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y")>23),AND(\[@\[Resident Since\]\]="",DATEDIF(\[@\[Date of Birth\]\],TODAY(),"y")>17+N(\[@Gender\]="Male")\*3))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175425)
    
64.  ![](https://secure.gravatar.com/avatar/b8b93be3161caa7e8cc65a3ddb76c8cb8522cf1b99a3ea04af26af60bc08b88a?s=64&d=mm&r=g) Miguel Cubeles says:
    
    [April 27, 2016 at 11:48 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175958)
    
    I did it, took me a while, I liked this one, 🙂
    
    \=IF(AND(voters\[@Gender\]="male",INT(TEXT(TODAY()-voters\[@\[Date of Birth\]\],"yy"))>21,voters\[@Citizen\]="Yes"),"YES",IF(AND(voters\[@Gender\]="Female",INT(TEXT(TODAY()-voters\[@\[Date of Birth\]\],"yy"))>18,voters\[@Citizen\]="Yes"),"YES",IF(AND(voters\[@Citizen\]="No",voters\[@\[Resident Since\]\]>DATE(2006,1,1)),"YES","NO")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175958)
    
65.  ![](https://secure.gravatar.com/avatar/b8b93be3161caa7e8cc65a3ddb76c8cb8522cf1b99a3ea04af26af60bc08b88a?s=64&d=mm&r=g) Miguel Cubeles says:
    
    [April 28, 2016 at 1:49 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175988)
    
    forgot to put =  
    there it is  
    \=IF(AND(\[@Gender\]="male",INT(TEXT(TODAY()-\[@\[Date of Birth\]\],"yy"))>=21,\[@Citizen\]="Yes"),"YES",IF(AND(\[@Gender\]="Female",INT(TEXT(TODAY()-\[@\[Date of Birth\]\],"yy"))>=18,\[@Citizen\]="Yes"),"YES",IF(AND(\[@Citizen\]="No",\[@\[Resident Since\]\]>=DATE(2006,1,1)),"YES","NO")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175988)
    
66.  ![](https://secure.gravatar.com/avatar/b8b93be3161caa7e8cc65a3ddb76c8cb8522cf1b99a3ea04af26af60bc08b88a?s=64&d=mm&r=g) Miguel Cubeles says:
    
    [April 28, 2016 at 2:45 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175998)
    
    \=IF(AND(\[@Gender\]="male",INT(TEXT(TODAY()-\[@\[Date of Birth\]\],"yy"))>=21,\[@Citizen\]="Yes"),"CAN VOTE",IF(AND(\[@Gender\]="Female",INT(TEXT(TODAY()-\[@\[Date of Birth\]\],"yy"))>=18,\[@Citizen\]="Yes"),"CAN VOTE",IF(AND(\[@Citizen\]="No",INT(TEXT(TODAY()-\[@\[Date of Birth\]\],"yy"))>=24,\[@\[Resident Since\]\]>=DATE(2006,1,1)),"CAN'T VOTE","CAN'T VOTE")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1175998)
    
67.  ![](https://secure.gravatar.com/avatar/7951ed9129b695df383f11a8e799a70cded039b33715f45bd71d2bc8d875d31d?s=64&d=mm&r=g) Chirayu says:
    
    [April 28, 2016 at 9:02 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176069)
    
    \=IF(AND(C88="Male",E88="Yes",((TODAY()-D88)/365)>=21),"Yes",IF(AND(C88="Female",E88="Yes",((TODAY()-D88)/365)>=18),"Yes",IF(AND(E88="No",((TODAY()-D88)/365)>=24,F88>=DATE(2006,1,1)),"Yes","No")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176069)
    
    *   ![](https://secure.gravatar.com/avatar/7951ed9129b695df383f11a8e799a70cded039b33715f45bd71d2bc8d875d31d?s=64&d=mm&r=g) Chirayu says:
        
        [April 28, 2016 at 9:02 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176070)
        
        I accidentally took the formula from row 88 lol
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176070)
        
68.  ![](https://secure.gravatar.com/avatar/4307667ded9be53fe4dd78e734cecdeb839b08918c4a63f5e96b99746e00d367?s=64&d=mm&r=g) Mike B says:
    
    [April 28, 2016 at 5:44 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176191)
    
    \=IF(OR(AND(((TODAY()-TEXT(\[@\[Date of Birth\]\],"mm/dd/yyyy"))/365)>=21,\[@Gender\]="Male",\[@Citizen\]="Yes"),(AND(((TODAY()-TEXT(\[@\[Date of Birth\]\],"mm/dd/yyyy"))/365)>=18,\[@Gender\]="Female",\[@Citizen\]="Yes"))),"Yes",IF(AND(\[@Citizen\]="No",TEXT(\[@\[Resident Since\]\],"mm/dd/YYYY")>1/1/2006,((TODAY()-TEXT(\[@\[Date of Birth\]\],"mm/dd/yyyy"))/365)>=24),"Yes","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176191)
    
    *   ![](https://secure.gravatar.com/avatar/4307667ded9be53fe4dd78e734cecdeb839b08918c4a63f5e96b99746e00d367?s=64&d=mm&r=g) Mike B says:
        
        [April 28, 2016 at 6:27 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176201)
        
        114 Female and 127 Male Non-Citizens Cannot vote  
        361 Female and 657 Male Citizens Cannot vote  
        227 Female and 255 Male Non-Citizens CAN vote  
        3050 Female and 2746 Male Citizens CAN vote
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176201)
        
69.  ![](https://secure.gravatar.com/avatar/4307667ded9be53fe4dd78e734cecdeb839b08918c4a63f5e96b99746e00d367?s=64&d=mm&r=g) Mike B says:
    
    [April 28, 2016 at 7:55 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176218)
    
    Update-Did not handle DOB correctly for Citizenry  
    \=IF(OR(AND(((TODAY()-TEXT(\[@\[Date of Birth\]\],"mm/dd/yyyy"))/365)>=21,\[@Gender\]="Male",\[@Citizen\]="Yes"),(AND(((TODAY()-TEXT(\[@\[Date of Birth\]\],"mm/dd/yyyy"))/365)>=18,\[@Gender\]="Female",\[@Citizen\]="Yes"))),"Yes",IF(AND((TODAY()-(TEXT(\[@\[Date of Birth\]\],"mm/dd/yyyy")))/365>24,DATE(2006,1,1)>=\[@\[Resident Since\]\]FALSE),"Yes","No"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176218)
    
70.  ![](https://secure.gravatar.com/avatar/8fb38723217fa1c369b0660ef7f8b46367e9d7f4e7fcdd4d852a900cd691fbf3?s=64&d=mm&r=g) Jacques L says:
    
    [April 29, 2016 at 10:17 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176542)
    
    \=IF(OR(AND(\[@Gender\]="Male",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)GTE21,\[@Citizen\]="Yes"),AND(\[@Gender\]="Female",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)GTE18,\[@Citizen\]="Yes"),AND(\[@Citizen\]="No",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)GTE24,38718GTE\[@\[Resident Since\]\]))=TRUE,"YES","No")
    
    I see most of the post did not include the "GTE", so I'm wondering if I did well to include it.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1176542)
    
71.  ![](https://secure.gravatar.com/avatar/fe45cbf7dec33aa2e76011af0114fdceab215494100fe33cbcb6d353bb7cdb25?s=64&d=mm&r=g) Matt L. says:
    
    [May 3, 2016 at 5:20 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1178570)
    
    \=IF(\[@Citizen\]="No",IF(AND((TODAY()-\[@DOB\])/365>=24,\[@\[Resident Since\]\]=21),"Yes",IF(AND(\[@Gender\]="Female",(TODAY()-\[@DOB\])/365>=18),"Yes","No")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1178570)
    
    *   ![](https://secure.gravatar.com/avatar/fe45cbf7dec33aa2e76011af0114fdceab215494100fe33cbcb6d353bb7cdb25?s=64&d=mm&r=g) Matt L. says:
        
        [May 3, 2016 at 5:29 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1178572)
        
        Wow! That is definitely not what I pasted into my comment!
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1178572)
        
    *   ![](https://secure.gravatar.com/avatar/fe45cbf7dec33aa2e76011af0114fdceab215494100fe33cbcb6d353bb7cdb25?s=64&d=mm&r=g) Matt L. says:
        
        [May 3, 2016 at 5:38 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1178578)
        
        Here is what I meant to post, with GTE and LTE instead of the symbols.
        
        \=IF(\[@Citizen\]="No",IF(AND((TODAY()-\[@DOB\])/365 GTE 24,\[@\[Resident Since\]\] LTE DATE(2006,1,1)),"Yes","No"),IF(AND(\[@Gender\]="Male",(TODAY()-\[@DOB\])/365 GTE 21),"Yes",IF(AND(\[@Gender\]="Female",(TODAY()-\[@DOB\])/365 GTE 18),"Yes","No")))
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1178578)
        
72.  ![](https://secure.gravatar.com/avatar/e0ac4fb3c46afb0d9932905cd78d00c7b0e31d0d58c2155724b0067852bf3e15?s=64&d=mm&r=g) Emerson says:
    
    [May 4, 2016 at 3:00 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179019)
    
    \=IF(OR(AND(C4="Female";E4="Yes";YEAR(TODAY())-YEAR(D4)>=18);AND(C4="Male";E4="Yes";YEAR(TODAY())-YEAR(D4)>=21);AND(E4="No";YEAR(TODAY())-YEAR(D4)>=24;TEXT(F4;"dd/mm/aaaa")>="01/01/2006"));"Can Vote";"Cannot")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179019)
    
73.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [May 5, 2016 at 5:29 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179675)
    
    \=IF(E4="No",AND(E4&F4 LTE "No38718",(TODAY()-D4)/365.25 GTE 24),(TODAY()-D4)/365.25 GTE LOOKUP(E4&C4,{"N","YesF","YesM"},{24,18,21}))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179675)
    
74.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [May 5, 2016 at 7:12 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179752)
    
    A little modification
    
    \=(NOW()-C4)/365 GTE IF(D4="No",IF(E4 LE 38719,24),IF(B4="Male",21,18))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179752)
    
75.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [May 5, 2016 at 7:14 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179755)
    
    By the way, credit to that last one should go to my friend and colleague Debraj. I just took out a few characters from his formula. 😀
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179755)
    
76.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [May 5, 2016 at 7:33 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179769)
    
    Here's my final version with 60 characters, but not with IF
    
    \=(NOW()-C4)/365 GTE LOOKUP(D4&B4,{"N","YesF","YesM"},{24,18,21})
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179769)
    
77.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [May 5, 2016 at 7:54 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179780)
    
    On further analysis, realized that my last formula is flawed. But good challenge Chandoo
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1179780)
    
78.  ![](https://secure.gravatar.com/avatar/99a9cbc70a6d2685406b902abedada926be9504f8371e9553d7bfc37021cf9e5?s=64&d=mm&r=g) Boris says:
    
    [May 10, 2016 at 3:39 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1185009)
    
    \=IF(E3="No",IF(AND((TODAY()-D3)>8760,F3>1/1/2006),"Yes","No"),IF(C3="Male",IF((TODAY()-D3)>7665,"Yes","No"),IF((TODAY()-D3)>6570,"Yes","No")))
    
    C3 = Male/Female Column  
    D3 = DOB  
    E3 = Citizen  
    F3 = Resident Date
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1185009)
    
79.  ![](https://secure.gravatar.com/avatar/c961e192f5634a1907c21e8c9be0d74b1bfded78648acc570cc5f3999932afd8?s=64&d=mm&r=g) Bill says:
    
    [May 18, 2016 at 11:18 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1192174)
    
    No Ifs used
    
    \=CHOOSE(1+((\[@Citizen\]="yes")\*(\[@Gender\]="Male")\*(TODAY()-\[@\[Date of Birth\]\] GT 21\*365))+((\[@Citizen\]="yes")\*(\[@Gender\]="Female")\*(TODAY()-\[@\[Date of Birth\]\] GT 18\*365))+((\[@Citizen\]="No")\*(TODAY()-\[@\[Date of Birth\]\] GT 24\*365)\*(\[@\[Resident Since\]\] LTE DATEVALUE("01/01/2006"))),"No","Yes")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1192174)
    
80.  ![](https://secure.gravatar.com/avatar/68f32385061284e6c3ca68f1b318f709c6cc91a06221cad443c7476c7193360a?s=64&d=mm&r=g) [aylyn](http://n/a)
     says:
    
    [June 8, 2016 at 6:48 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1209444)
    
    \=IF(E4="no",IF(YEARFRAC(D4,TODAY())>=24,"yes","no"),IF(C4="male",IF(YEARFRAC(D4,TODAY())>=21,"yes","no"),IF(C4="female",IF(YEARFRAC(D4,TODAY())>=18,"yes","no"))))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1209444)
    
    *   ![](https://secure.gravatar.com/avatar/68f32385061284e6c3ca68f1b318f709c6cc91a06221cad443c7476c7193360a?s=64&d=mm&r=g) [aylyn](http://n/a)
         says:
        
        [June 8, 2016 at 6:58 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1209448)
        
        C4 = Gender  
        D4 = Date  
        E4 = Citizen
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1209448)
        
81.  ![](https://secure.gravatar.com/avatar/68f32385061284e6c3ca68f1b318f709c6cc91a06221cad443c7476c7193360a?s=64&d=mm&r=g) [aylyn](http://n/a)
     says:
    
    [June 8, 2016 at 9:56 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1209498)
    
    Revised:
    
    \=IF(E4="no",IF(AND(YEARFRAC(D4,TODAY())>=24,(F4=21,"yes","no"),IF(C4="female",IF(YEARFRAC(D4,TODAY())>=18,"yes","no"))))
    
    C4 = Gender  
    D4 = Date of Birth  
    E4 = Citizen  
    F4 = Resident Since
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1209498)
    
82.  ![](https://secure.gravatar.com/avatar/427af7ff50f55af9ad5cb51fb948a0abf20dc1ce5d56a28e976df0d076b712cb?s=64&d=mm&r=g) Rakesh says:
    
    [July 7, 2016 at 6:23 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228464)
    
    hi  
    What is the formula to add "/" symbol between date month and year automatically?
    
    e.g 04072016 (4th July 2016) automatically converted to 04/07/2016 ??
    
    pls help
    
    thanks in advance
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228464)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 7, 2016 at 6:42 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228468)
        
        @Rakesh
        
        If the cell contains a true date you can use a Custom Number Format such as dd/mm/yyyy
        
        If the cell contains text, which i suspect it does  
        Use a helper column and put =DATE(RIGHT(A2,4),MID(A2,3,2),LEFT(A2,2))  
        Then apply a Custom Number Format such as dd/mm/yyyy  
        Then copy/paste as values
        
        or you can use Text To Columns  
        Select the text  
        Goto the data Tab, select Text to Columns  
        Select Delimitered  
        Next  
        Next  
        Select date, then select DMY  
        apply
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228468)
        
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [July 7, 2016 at 7:10 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228479)
        
        @Rakesh,  
        If all you need is for displaying the dates but NOT for calculations and you want to see: 04/07/2016 upon hitting 'Enter' after typing: 04072016 – try to 'Custom Format' those cells with the following pattern:  
        00\\/00\\/0000  
        \*\*\* The symbols, between the 'Zeros', are not the character V but one 'Back slash' & one 'Forward slash'.
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228479)
        
83.  ![](https://secure.gravatar.com/avatar/427af7ff50f55af9ad5cb51fb948a0abf20dc1ce5d56a28e976df0d076b712cb?s=64&d=mm&r=g) Rakesh says:
    
    [July 7, 2016 at 6:55 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228472)
    
    Thanks a ton Hui..
    
    really I was looking for this type of formula for the last 5-6 Months.  
    during this I got some related formulas but problem was not solved according to my requirements (dd/mm/yyyy) format.  
    But with this one I am fully satisfied and my long-standing problem is resolved now.  
    Thanks a lot again dear Hui..  
    I would also like to thanks candoo.org
    
    Thanks.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228472)
    
84.  ![](https://secure.gravatar.com/avatar/427af7ff50f55af9ad5cb51fb948a0abf20dc1ce5d56a28e976df0d076b712cb?s=64&d=mm&r=g) Rakesh says:
    
    [July 7, 2016 at 6:57 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228474)
    
    sorry
    
    its chandoo.org not candoo.org
    
    sorry
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228474)
    
85.  ![](https://secure.gravatar.com/avatar/427af7ff50f55af9ad5cb51fb948a0abf20dc1ce5d56a28e976df0d076b712cb?s=64&d=mm&r=g) Rakesh says:
    
    [July 7, 2016 at 2:44 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228594)
    
    Thank you very much dear Micky for your helpful tips. This is wonderful  
    when it is only for displaying and not for calculating.
    
    Thanks again
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228594)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [July 7, 2016 at 2:53 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228597)
        
        @Rakesh,  
        You are more than welcome.  
        If you need to perform calculations use a helper-column and type: =TEXT(A1,"00\\/00\\/0000") (Same pattern as above)
        
        [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1228597)
        
86.  ![](https://secure.gravatar.com/avatar/749b79c2ec7afe93f7443be290b9caf9ee41bdf733f0b5b087a68999d92f3f49?s=64&d=mm&r=g) Rushabh Gala says:
    
    [September 29, 2016 at 4:19 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1299613)
    
    \=IF(OR(AND(\[@Gender\]="Male",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)>=21,\[@Citizen\]="Yes"),AND(\[@Gender\]="Female",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)>=18,\[@Citizen\]="Yes"),AND(\[@Citizen\]="No",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)>=24,\[@\[Resident Since\]\]>38718))=TRUE,"Can Vote","Can not Vote")
    
    I don't know if this formula is perfect, but it gave me satisfactory answer.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1299613)
    
87.  ![](https://secure.gravatar.com/avatar/749b79c2ec7afe93f7443be290b9caf9ee41bdf733f0b5b087a68999d92f3f49?s=64&d=mm&r=g) Rushabh Gala says:
    
    [September 29, 2016 at 4:43 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1299635)
    
    \=IF(OR(AND(\[@Gender\]="Male",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)>=21,\[@Citizen\]="Yes"),AND(\[@Gender\]="Female",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)>=18,\[@Citizen\]="Yes"),AND(\[@Citizen\]="No",ROUNDDOWN((TODAY()-\[@\[Date of Birth\]\])/365,0)>=24,\[@\[Resident Since\]\]<38718))=TRUE,"Can Vote","Can not Vote")
    
    the earlier formula had a minor mistake, kindly comment if this formula is correct.
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1299635)
    
88.  ![](https://secure.gravatar.com/avatar/15733ff427445e709ce7d0187312c79e6b4132da1dd33528bc9c24f9598aeb9b?s=64&d=mm&r=g) Avnish Tiwari says:
    
    [November 9, 2016 at 4:00 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-1335041)
    
    Hello friends  
    I am a bit new on this forum still I have used my very tiny brain to solve this challenge for The great Chandoo, think it works fine for the problem  
    \=IF(OR(AND(C2="MALE",DATEDIF(D2,TODAY(),"Y")GTE21,E2="YES"),AND(C2="FEMALE",DATEDIF(D2,TODAY(),"Y")GTE18,E2="YES"))),"YES",IF(AND(E2="NO",DATEDIF(D2,TODAY(),"Y")GTE24,DATEDIF(F2,TODAY(),"Y")GTE10,)"YES","NO"))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1335041)
    
89.  ![](https://secure.gravatar.com/avatar/9f676795ef65aeea1222181706ce86c62e218539fbc699478d2aa51fc09c6068?s=64&d=mm&r=g) MVF says:
    
    [March 13, 2017 at 9:21 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-1419478)
    
    \=IF(OR(AND(\[@Citizen\]="yes",\[@Gender\]="Male",(TODAY()-\[@\[Date of Birth\]\])>=7665),AND(\[@Citizen\]="yes",\[@Gender\]="Female",(TODAY()-\[@\[Date of Birth\]\])>=6570),AND(\[@Citizen\]="No",(TODAY()-\[@\[Date of Birth\]\])>=8760,(TODAY()-IF(\[@\[Resident Since\]\]="",0,\[@\[Resident Since\]\]))>=4089)),"Yes","No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-1419478)
    
90.  ![](https://secure.gravatar.com/avatar/24e318f1db61852e5ab188ce1283e334963387999ef5f79c0085e4ea9ed664a7?s=64&d=mm&r=g) Chanchal Sahu says:
    
    [September 25, 2022 at 3:41 pm](https://chandoo.org/wp/sumerian-voter-problem/#comment-2099439)
    
    \=IF(OR(AND(voters\[@Citizen\]="Yes",voters\[@Gender\]="Male",DATEDIF(voters\[@\[Date of Birth\]\],TODAY(),"Y")>=21),AND(voters\[@Citizen\]="Yes",voters\[@Gender\]="Female",DATEDIF(voters\[@\[Date of Birth\]\],TODAY(),"Y")>=18),AND(voters\[@Citizen\]="No",DATEDIF(voters\[@\[Date of Birth\]\],TODAY(),"Y")>=24,voters\[@\[Resident Since\]\]>DATE(2006,1,1))),"Can Vote","Can't Vote")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-2099439)
    
91.  ![](https://secure.gravatar.com/avatar/655f2c011ea39ba13bab2490442aafe88092a05f58406f6cd00077cfa3b4b8f2?s=64&d=mm&r=g) cutegal says:
    
    [December 7, 2023 at 4:07 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-2155735)
    
    \=IF(AND(\[@Gender\]="Male",YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\]) GTE 21,\[@Citizen\]="Yes"),"Yes",IF(AND(\[@Gender\]="Female",YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\]) GTE 18,\[@Citizen\]="Yes"),"Yes",IF(AND(YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\]) GTE 24,\[@Citizen\]="No",\[@\[Resident Since\]\]<=DATE(2006,1,1)),"Yes","No")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-2155735)
    
92.  ![](https://secure.gravatar.com/avatar/655f2c011ea39ba13bab2490442aafe88092a05f58406f6cd00077cfa3b4b8f2?s=64&d=mm&r=g) cutegal says:
    
    [December 7, 2023 at 4:08 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-2155736)
    
    \=IF(AND(\[@Gender\]="Male",YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\])>=21,\[@Citizen\]="Yes"),"Yes",IF(AND(\[@Gender\]="Female",YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\])>=18,\[@Citizen\]="Yes"),"Yes",IF(AND(YEAR(TODAY())-YEAR(\[@\[Date of Birth\]\])>=24,\[@Citizen\]="No",\[@\[Resident Since\]\]<=DATE(2006,1,1)),"Yes","No")))
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-2155736)
    
93.  ![](https://secure.gravatar.com/avatar/6ddb4aad4bd3f636e7895c6048287a211130412f56657b48b579d056f1db6e5a?s=64&d=mm&r=g) Cad says:
    
    [November 6, 2025 at 11:47 am](https://chandoo.org/wp/sumerian-voter-problem/#comment-2497405)
    
    \=IFS(AND(\[@Citizen\]="Yes",\[@Gender\]="Male",(TODAY()-\[@\[Date of Birth\]\])/365 GTE 21),"Yes", AND(\[@Citizen\]="Yes",\[@Gender\]="Female",(TODAY()-\[@\[Date of Birth\]\])/365 GTE 18),"Yes", AND(\[@Citizen\] = "No", (TODAY()-\[@\[Date of Birth\]\])/365 GTE 24, \[@\[Resident Since\]\] LTE DATE(2006,1,1)), "Yes", TRUE, "No")
    
    [Reply](https://chandoo.org/wp/sumerian-voter-problem/#comment-2497405)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sumerian-voter-problem/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Excel Tips, Tricks, Cheats & Hacks – Microsoft MVP Edition](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/) | [Earth Venus cosmic dance – Animated chart in Excel](https://chandoo.org/wp/earth-venus-cosmic-dance-animated-chart-in-excel/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
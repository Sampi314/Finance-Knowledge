# Strip leading zeroes from strings with this array formula

**Source:** https://chandoo.org/wp/formula-forensics-no-027

---

Formula Forensics No. 027 – Remove Leading Zeroes
=================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 42 comments

  

A few weeks ago Chandoo received an email from a reader, **Chandu**:

_“I am in search of a formula for the below scenario, please suggest:_

 _I am trying to delete the zeros before the numbers._

_Eg:_

_002459J_

_0002459R_

_02459O_

_I need one unique formula in case of huge data, please suggest.”_

Chandoo responded with two solutions:

If you want to get rid of all 0’s:

\=Substitute(B2, “0”, “”)

If you want to get rid of all leading 0’s:

\=Mid(B2, Min(Iferror(Find({1,2,3,4,5,6,7,8,9}, B2), “”)), LEN(B2)) CTRL+Shift+Enter

So today we will look at these two formulas and see what makes them tick.

As always at Formula Forensics you can follow along using a Worked Example which you can download here: [Excel 97-2013](https://chandoo.org/wp/wp-content/uploads/2012/08/Remove-Zeroes.xls "Remove Leading Zeroes")
.

Substitute(… )
--------------

Chandoo’s first formula uses the Excel Substitute() function to replace all the 0’s with a Null character. The Null character is what is between the two quotation marks “” (Nothing).

The syntax of the Excel Substitute Function is:

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/FF261.png "FF261")](https://chandoo.org/wp/wp-content/uploads/2012/08/FF261.png)

In Chandoo’s formula \=Substitute(B2,”0″,””) we see that

**Text**: = B2

**Old\_Text**: “0”

**New Text**: “” Null Character

So this formula says: Replace all the 0 characters in the text in Cell B2 with “”

**Advantages**: Simple formula if the text only has leading zeroes eg: _002459J_ _will correctly return_ _2459J_

**Disadvantages**: Doesn’t work if the text has internal or trailing zeroes eg: _0024509J_ _will incorrectly return 2459J_

Mid( … )
--------

Chandoo’s second formula was the array formula:

\=MID(B2,MIN(IFERROR(FIND({1,2,3,4,5,6,7,8,9},B2),””)),LEN(B2)) **Ctrl**+**Shift**+**Enter**

This formula is based on the Excel Mid() function which returns a Sub-String from within the source String

The string is the text that starts at the position of the first non zero number in the string

Let’s start in the middle and work our way out to see what is happening here:

\=MID(B2,MIN(IFERROR(FIND({1, 2, 3, 4, 5, 6, 7, 8, 9}, B2),””)),LEN(B2))

In the middle of the formula we see the Excel Find() function.

The syntax of Find() is:

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/FF271.png "FF271")](https://chandoo.org/wp/wp-content/uploads/2012/08/FF271.png)

In Chandoo’s Formula

**Find\_text**: {1,2,3,4,5,6,7,8,9,}

**Within\_text**: B2

**Start\_num**: 1 (Default)

So the Find() function will look for the values 1 to 9 in the cell B2

Lets see that in an example

In **C26** put one of the values **0024059J**

In a blank cell **D28** put \=FIND({1, 2, 3, 4, 5, 6, 7, 8, 9}, C26) then press **F9**, not Enter

Excel responds with: \={#VALUE!,3,#VALUE!,4,6,#VALUE!,#VALUE!,#VALUE!,7}

Looking at this we can see that the formula has returned 4 values of 3, 4 6 & 7 with some #VALUE! Errors in between.

The values 3, 4, 6 & 7 are the positions in cell C26 of the values 1, 2, 3, 4, 5, 6, 7, 8 & 9

We can see that C26 contains: 0024059J and that in positions 3, 4, 6 & 7 we have values from the array 1, 2, 3, 4, 5, 6, 7, 8 & 9

Stepping out of the original formula a little bit \=MID(B2,MIN(IFERROR(FIND({1,2,3,4,5,6,7,8,9},B2),””)),LEN(B2))

We can see that the above Find() formula is surrounded by an Iferror() function.

This will take the results of the Find() function and where there is an error insert a “”

In a blank cell **D30** put \=IFERROR(FIND({1,2,3,4,5,6,7,8,9},C26),””) then press **F9**, not Enter

Excel responds with: \={“”,3,””,4,6,””,””,””,7}

The #VALUE! Errors have been converted to “”

Stepping out a bit more in our original formula we encounter a Min() function next.

\=MID(B2,MIN(IFERROR(FIND({1,2,3,4,5,6,7,8,9},B2),””)),LEN(B2))

The Min() function will return the Minimum value from the Iferror() function

So Min(IFERROR(FIND({1,2,3,4,5,6,7,8,9},B2),””)) is the same as Min({“”,3,””,4,6,””,””,””,7})

Which we can see is **3**

But lets check that:

In a blank cell **D32** type: \=MIN(IFERROR(FIND({1,2,3,4,5,6,7,8,9},C26),””)) then press **F9**, not Enter

Excel responds with: **3** as we deduced above,

Finally we arrive at our original formula: \=MID(B2,MIN(IFERROR(FIND({1,2,3,4,5,6,7,8,9},B2),””)),LEN(B2))

Which can now be simplified to

\=MID(0024059J, 3, LEN(0024059J))

The length of 0024059J is **8** characters long and so the formula becomes

\=MID(0024059J, 3, 8)

What this is asking is return the Middle 8 characters of the text 00245059J starting at position **3**

Which is **24059J**

This has effectively stripped of the left or leading zeroes as Chandu required.

**Download**
------------

You can download a copy of the above file and follow along, [Download Here – Excel 97-2013](https://chandoo.org/wp/wp-content/uploads/2012/08/Remove-Zeroes.xls "Remove Leading Zeroes")
.

Formula Forensics “The Series”
------------------------------

This is the 27th post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics Series")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/)
 or [Chandoo](http://chandoo.org/wp/contact/)
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
| Written by Hui...  <br>Tags: [find](https://chandoo.org/wp/tag/find/)<br>, [iferror](https://chandoo.org/wp/tag/iferror/)<br>, [len()](https://chandoo.org/wp/tag/len/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [MIN()](https://chandoo.org/wp/tag/min/)<br>, [substitute()](https://chandoo.org/wp/tag/substitute/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 42 Responses to “Formula Forensics No. 027 – Remove Leading Zeroes”

1.  ![](https://secure.gravatar.com/avatar/d309cae04fc971e84a19db159ccc2dfa78b7a1949564de62d999cbebc5e7cf62?s=64&d=mm&r=g) Vishwa says:
    
    [August 23, 2012 at 8:19 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229178)
    
    Hi Chandoo,
    
    This fails when it starts with any charcter after the Zeros... like 00FG345L. Any solution for this ?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229178)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 23, 2012 at 8:39 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229180)
        
        @Vishwa  
        It only fails when the first non 0 character isn't a number  
        However, the following formula fixes that:  
        `=MID(C26, MIN(IF(CODE(MID(C26, ROW(OFFSET($A$1,,,LEN(C26))),1))>48, ROW(OFFSET($A$1,,,LEN(C26))))), LEN(C26))`
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229180)
        
    *   ![](https://secure.gravatar.com/avatar/e67fdb07e5d0fcd8bb421d6325b953279ecfc0a6fcbb63ea2665d598a3c0c3d8?s=64&d=mm&r=g) Debraj Roy says:
        
        [August 23, 2012 at 8:51 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229181)
        
        @Vishwa,  
        If you can afford a UDF, then you may go for below function..  
        Excel >> VBA (Alt + F11) >> Insert New Module >> Paste the below code  
        \`  
        Function RemoveLeadingZeros(strInput)  
          RemoveLeadingZeros = strInput  
          Do While Left(RemoveLeadingZeros, 1) = "0"  
            RemoveLeadingZeros = Mid(RemoveLeadingZeros, 2)  
          Loop  
        End Function  
        \`  
        and in Excel write Formula as  
        \`=RemoveLeadingZeros(A2)\`  
        Regards,  
        Deb
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229181)
        
        *   ![](https://secure.gravatar.com/avatar/618675e7bd85c38fe2760f75054a37f2b4ee4eec867774ad218f85e83fcb2126?s=64&d=mm&r=g) [Novicetech1](http://none/)
             says:
            
            [August 23, 2012 at 8:04 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229222)
            
            Thanks Deb. This is the way I prefer to do this kind of thing. Sweet function. 🙂
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229222)
            
        *   ![](https://secure.gravatar.com/avatar/d85e47e84ed3dd6a332dd407199befaf3210153ab3b5155d6ac8868206aca836?s=64&d=mm&r=g) George says:
            
            [August 24, 2012 at 10:01 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229247)
            
            Would you not be better served with:  
            RemoveLeadingZeros = Mid(RemoveLeadingZeros, 2)   
            being replaced by  
            RemoveLeadingZeros = Right(RemoveLeadingZeros, len(RemoveLeadingZeros)-1)    
            Or am I missing something? 
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229247)
            
        *   ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
             says:
            
            [August 26, 2012 at 6:46 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229514)
            
            @Deb,
            
            The VBA function can be done without using a loop...
            
            <code>  
            Function RemoveLeadingZeros(S As String) As String  
              RemoveLeadingZeros = Replace(LTrim(Replace(S, "0", " ")), " ", "0")  
            End Function  
            </code>
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229514)
            
    *   ![](https://secure.gravatar.com/avatar/d309cae04fc971e84a19db159ccc2dfa78b7a1949564de62d999cbebc5e7cf62?s=64&d=mm&r=g) Vishwa says:
        
        [August 23, 2012 at 10:16 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229185)
        
        Thanks all.... meanwhile i tried one more method to solve this issue
        
        \=MID(B2,MATCH(TRUE,(MID(B2,ROW(INDIRECT("1:"&LEN(B2))),1)<>"0"),0),LEN(B2))
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229185)
        
        *   ![](https://secure.gravatar.com/avatar/618675e7bd85c38fe2760f75054a37f2b4ee4eec867774ad218f85e83fcb2126?s=64&d=mm&r=g) [Novicetech1](http://none/)
             says:
            
            [August 23, 2012 at 8:07 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229223)
            
            It would be nice if we had some forensics on this one. Thanks.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229223)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                 says:
                
                [August 26, 2012 at 7:56 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229527)
                
                @Novicetech1  
                Why don't you try using some of the techniques I discuss in Formula Forensics to look at he formula  
                Start in the middle and select an entire function, evaluate it with F9  
                Work out what it's doing and why  
                Then step out a function 
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229527)
                
    *   ![](https://secure.gravatar.com/avatar/e76b71de9bafba0a82ae54f211ac398ce3f653de25606471effdcc722da0858b?s=64&d=mm&r=g) BruceW says:
        
        [August 23, 2012 at 4:38 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229207)
        
        Hi Vishwa
        
        Try  
        \=MID(A1,SUM(IFERROR(FIND(REPT(CHAR(48),ROW(INDIRECT("1:"&LEN(A1)))),A1),0))+1,256)
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229207)
        
        *   ![](https://secure.gravatar.com/avatar/f6fb631cb5af8ef896c056c59eee762e3c8aebb9b7f99c46044a735449aaa449?s=64&d=mm&r=g) Jeanbar says:
            
            [October 21, 2012 at 2:35 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-273520)
            
            Vishwa,  
            Nice formula to find out the first "non-leading zero" character.  
            BruceW,  
            For those wo can't use the IFERROR() function (Yes I'am using the 2003 version :()  
            \=MID(B2,SUM(N(MID(B2,1,LEN(T\_00))=T\_00)),256) + CSE  
            where T\_00 is defined as =REPT("0",ROW(INDIRECT("1:10"))
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-273520)
            
2.  ![](https://secure.gravatar.com/avatar/e9977c0323779337d6216e89141068d273328cc36e564ca80ef0ba361b832dcf?s=64&d=mm&r=g) Kevin says:
    
    [August 23, 2012 at 3:42 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229201)
    
    To get 001234 to 1234 all you have to do is =TEXT(VALUE(001234),"0000")
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229201)
    
3.  ![](https://secure.gravatar.com/avatar/b877a8c6350bbbc9b49ff3500eb6a61d77d25e898bf55b8b57f62197f3808c08?s=64&d=mm&r=g) Rosco says:
    
    [August 23, 2012 at 3:47 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229202)
    
    This one seems to cover all bases and doesn't require Ctrl+Shift+Enter
    
     =RIGHT(B2,LEN(B2)-MATCH(TRUE,MID(B2,{1,2,3,4,5,6,7,8,9},1)<>"0",0)+1) 
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229202)
    
4.  ![](https://secure.gravatar.com/avatar/d3bea61ec8cc84a1172a897182e688eb70a966fb2a7cb65c918d78082728117c?s=64&d=mm&r=g) James Blair says:
    
    [August 23, 2012 at 4:25 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229204)
    
    If you modify the substitut formula into a RIGHT formula then you can do it for any character after the 0s and not have to use an array:
    
    assuming the target cell is C11
    
    \=RIGHT(C11,LEN(C11)-SEARCH(LEFT(SUBSTITUTE(C11,"0",""),1),C11)+1)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229204)
    
5.  ![](https://secure.gravatar.com/avatar/6f35b5f4259a9ffe30d69fc2bfcbd4279d67a24974f466485ffe245fc95bd4ce?s=64&d=mm&r=g) Stephen says:
    
    [August 23, 2012 at 4:30 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229205)
    
    \=RIGHT(A1,LEN(A1)-IF(LEFT(A1)="0",IF(MID(A1,1,1)="0",IF(MID(A1,2,1)="0",IF(MID(A1,3,1)="0",IF(MID(A1,4,1)="0",IF(MID(A1,5,1)="0",5,4),3),2),1),0),0))
    
    A little longer, but more intuitive, for me anyway; it will strip up to 5 0's from the beginning.  More if statements could be used if more zeros are present. 
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229205)
    
6.  ![](https://secure.gravatar.com/avatar/6f35b5f4259a9ffe30d69fc2bfcbd4279d67a24974f466485ffe245fc95bd4ce?s=64&d=mm&r=g) Stephen says:
    
    [August 23, 2012 at 4:31 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229206)
    
    Sorry, the line was too long.
    
    \=RIGHT(A1,LEN(A1)-IF(LEFT(A1)="0",IF(MID(A1,1,1)="0", IF(MID(A1,2,1)="0",IF(MID(A1,3,1)="0",IF(MID(A1,4,1)="0", IF(MID(A1,5,1)="0",5,4),3),2),1),0),0))
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229206)
    
7.  ![](https://secure.gravatar.com/avatar/be0942581ecf6840ea793380b8ea9cc3b0c55d1890674298d87ad1ac87d70b0c?s=64&d=mm&r=g) shrivallabha says:
    
    [August 23, 2012 at 4:52 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229209)
    
    Only for the sample data posted.  
    \=--LEFT(A3,LEN(A3)-1)&RIGHT(A3)  
    will also work.  
    And following approach should work generally without CSE:  
    \=REPLACE(A1,1,MATCH(TRUE,MID(A1,{1,2,3,4,5,6,7,8,9},1)<>"0",0)-1,"")
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229209)
    
    *   ![](https://secure.gravatar.com/avatar/be0942581ecf6840ea793380b8ea9cc3b0c55d1890674298d87ad1ac87d70b0c?s=64&d=mm&r=g) shrivallabha says:
        
        [August 23, 2012 at 4:57 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229210)
        
        Or to make it handle any number of zeroes (NEED CSE):  
        \=REPLACE(A1,1,MATCH(TRUE,MID(A1,ROW(INDEX(A:A,1):INDEX(A:A,LEN(A1))),1)<>"0",0)-1,"")
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229210)
        
8.  ![](https://secure.gravatar.com/avatar/2957373d23f7c0c89d8dc4cedef211937c6b9b7a21d4c5c0c00ada3e7dbf3d46?s=64&d=mm&r=g) Squiggler says:
    
    [August 23, 2012 at 5:16 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229212)
    
    Or simpler, not using array formulas:
    
    \=IFERROR(MID(B2,FIND(LEFT(SUBSTITUTE(B2,"0",""),1),B2),65535),"")
    
    Will handle any number of leading zeros, and doesn't care if the string is numeric or alphabetic or both!  
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229212)
    
    *   ![](https://secure.gravatar.com/avatar/2957373d23f7c0c89d8dc4cedef211937c6b9b7a21d4c5c0c00ada3e7dbf3d46?s=64&d=mm&r=g) Squiggler says:
        
        [August 23, 2012 at 5:18 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229213)
        
        Just remove all zero's find the first character that isn't zero and search for it in the string, Strip off everything before this character.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229213)
        
        *   ![](https://secure.gravatar.com/avatar/2957373d23f7c0c89d8dc4cedef211937c6b9b7a21d4c5c0c00ada3e7dbf3d46?s=64&d=mm&r=g) Squiggler says:
            
            [August 23, 2012 at 6:12 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229216)
            
            In-fact, =MID(B2,FIND(LEFT(SUBSTITUTE(B2,"0","")),B2),65535)
            
            will suffice, I put the error in for the blank string but it's not needed, the only case it is needed is if B2 already contains an error!  
             
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229216)
            
9.  ![](https://secure.gravatar.com/avatar/37126bca5b2d642974940c98f7a8241b321d0f5c21e32fb204d414d88c874564?s=64&d=mm&r=g) Leonid K. says:
    
    [August 23, 2012 at 6:06 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229214)
    
    My non-array version is:  
    \=REPLACE(A1,1,FIND(LEFT(TRIM(SUBSTITUTE(A1,"0"," ")),1),A1),"")
    
    where LEFT(TRIM(SUBSTITUTE(A1,"0"," ")),1) gives us the first non zero character,  
    FIND(LEFT(TRIM(SUBSTITUTE(A1,"0"," ")),1) finds its position and then REPLACE chops everything to the left up to that position.
    
    It would be practical to have in Excel a worksheet function LTRIM. Then the formula could be shorter like SUBSTITUTE(LTRIM(SUBSTITUTE(A1,"0"," "))," ","0")
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229214)
    
10.  ![](https://secure.gravatar.com/avatar/cd02b423ed5968e79b79b81e20a79f8922cf37688a37212ffb9fc960f1302123?s=64&d=mm&r=g) Jeremy says:
    
    [August 23, 2012 at 7:09 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229218)
    
    Love the site!  Lot's of awesome content here, and I'm a regular reader. 
    
    This probably defeats the purpose of the 'Formula Forensics' topic, but a far easier method which requires no formula is to use the 'multiply' functionality from the paste special menu.  Type the number '1' in an empty cell and copy it.  Highlight the cells containing the values with leading zeros and do paste special.  From that menu, select 'values' and then select 'multiply'.  All leading zeros are eliminated and no formula is required!  It's fast too.       
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229218)
    
    *   ![](https://secure.gravatar.com/avatar/08eff0d2d07c6903594ab7dea4efc9c312dda7b2f88bdeab9782d76167c30505?s=64&d=mm&r=g) harold says:
        
        [August 24, 2012 at 2:17 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229229)
        
        jeremy.. this can only possible if "0" will lead after a number. All values that have letters after zero's cannot be cleaned. 
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229229)
        
11.  ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
     says:
    
    [August 23, 2012 at 7:58 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229220)
    
    Assuming there are no spaces in the data (as shown), you can use this simple formula...
    
    \=SUBSTITUTE(TRIM(SUBSTITUTE(A1,0," "))," ",0)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229220)
    
    *   ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
         says:
        
        [August 23, 2012 at 8:02 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229221)
        
        Never mind... that formula will not work correctly if the text ends with zeroes.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229221)
        
    *   ![](https://secure.gravatar.com/avatar/08eff0d2d07c6903594ab7dea4efc9c312dda7b2f88bdeab9782d76167c30505?s=64&d=mm&r=g) harold says:
        
        [August 24, 2012 at 2:20 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229230)
        
        This will remove all the zero's. not just in the beginning but also at the mid and end
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229230)
        
12.  ![](https://secure.gravatar.com/avatar/b4f59fe7b45001d3377636d5014b41c3fcf5c2fe4e48ade6b5459a2f26fb7dd0?s=64&d=mm&r=g) Sanika says:
    
    [August 24, 2012 at 3:59 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229232)
    
    I guess this works in excel 2003 only...
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229232)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 24, 2012 at 4:02 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229233)
        
        @Sanika  
        No, The formulas don't use any 2007, 2010 or 2013 specific functions  
        Which formula is specifically not working ?
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229233)
        
        *   ![](https://secure.gravatar.com/avatar/b4f59fe7b45001d3377636d5014b41c3fcf5c2fe4e48ade6b5459a2f26fb7dd0?s=64&d=mm&r=g) Sanika says:
            
            [August 24, 2012 at 5:32 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229236)
            
            The substitue formula is not working..
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229236)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui](http://chandoo.org/wp/about-hui/)
                 says:
                
                [August 24, 2012 at 7:29 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229241)
                
                @Sanika  
                   
                Substitute has been in Excel since day 0 and so it is something wrong at your end  
                   
                What version of Excel do you use?  
                Can you email me the file, click on Hui, email at bottom of page
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229241)
                
            *   ![](https://secure.gravatar.com/avatar/2957373d23f7c0c89d8dc4cedef211937c6b9b7a21d4c5c0c00ada3e7dbf3d46?s=64&d=mm&r=g) Squiggler says:
                
                [August 24, 2012 at 8:03 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229242)
                
                @Sanika, if you cut and pasted the formula watch out for the quotation marks, you may need to overtype them, as the web page uses different ones to the standard ones excel understands. Also some versions of Excel use ; rather than , in the formulas.
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229242)
                
        *   ![](https://secure.gravatar.com/avatar/5d417581d9fee4641b55a36bfd0123c7da24f07ff7299dfa1a9824f9389e7ab4?s=64&d=mm&r=g) Jim Watson says:
            
            [August 28, 2012 at 3:23 pm](https://chandoo.org/wp/formula-forensics-no-027/#comment-229889)
            
            Hui,
            
            The IFERROR function in your formula was not introduced until Excel 2007. Also, in your last paragraph, you inadvertently added an additional "5" in the example text (00245059J). It should be 0024059J. Great article!
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229889)
            
13.  ![](https://secure.gravatar.com/avatar/a0050e6f7d4b70a9a4395440e325873188c78881aa5ee4a460a07aae78bce011?s=64&d=mm&r=g) Ajit Roy says:
    
    [August 24, 2012 at 4:41 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229234)
    
    Hi all  
    i think the formula is fine but in this world we all are living in a short cut to do the same job.  
       
    go for it  
    Ctrl+F ---> type 0 ---> replace with none ----> here you go 🙂 all zero went vanish 😉
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229234)
    
    *   ![](https://secure.gravatar.com/avatar/2957373d23f7c0c89d8dc4cedef211937c6b9b7a21d4c5c0c00ada3e7dbf3d46?s=64&d=mm&r=g) Squiggler says:
        
        [August 24, 2012 at 8:07 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229243)
        
        @Ajit
        
        Except if you try that on 00010230100R you get 1231R rather than 10340100R......
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229243)
        
14.  ![](https://secure.gravatar.com/avatar/d85e47e84ed3dd6a332dd407199befaf3210153ab3b5155d6ac8868206aca836?s=64&d=mm&r=g) George says:
    
    [August 24, 2012 at 11:25 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229258)
    
    Since the input is in a string format, wouldn't it make sense if the output was too (if you run it on a number, eg 00001234 you end up with 1234 **as a numbe**r)?
    
    I thought CSTR() would work for the VBA solutions, but Excel helpfully converts these strings back to numbers.
    
    Any help?  Right now I'm using the solution posted by Debraj Roy because I think it's awesome.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229258)
    
15.  ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
    
    [August 25, 2012 at 3:48 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229321)
    
    Vishwa posted something similar already but here is my take:  
    \=MID(A1,MATCH(FALSE,INDEX(--MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)=0,),0),LEN(A1))
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229321)
    
16.  ![](https://secure.gravatar.com/avatar/5c2ab69197c1092615a2e2e684d36b8382a7c65404808b3dcf844d2cdcc65dc3?s=64&d=mm&r=g) Faez says:
    
    [August 25, 2012 at 11:27 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229339)
    
    \=IF(ABS(MID(B2,1,3))=0,ABS(MID(B2,1,4)),ABS(MID(B2,1,3)))&IF(ABS(MID(B2,1,3))=0,(MID(B2,5,LEN(B2))),MID(B2,4,LEN(B2)))
    
    This formula works with min. 3 digitals before adding letters
    
    try it
    
    Thanks  
    Faez
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229339)
    
17.  ![](https://secure.gravatar.com/avatar/212e6583e3d726ca184caf4ef47410e87e5f74d4f09a579059c6371725807e50?s=64&d=mm&r=g) Olav says:
    
    [August 27, 2012 at 4:56 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-229733)
    
    Thanks so much for your website...Downloaded your interaction file.  Brilliant.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-229733)
    
18.  ![](https://secure.gravatar.com/avatar/e90e27df607cf7ee7326405d2950b97a14a5842eae5e4e119cc53bb643594fa3?s=64&d=mm&r=g) Ansi says:
    
    [September 11, 2012 at 4:16 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-237477)
    
    \=value()
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-237477)
    
19.  ![](https://secure.gravatar.com/avatar/e90e27df607cf7ee7326405d2950b97a14a5842eae5e4e119cc53bb643594fa3?s=64&d=mm&r=g) Ansi says:
    
    [September 11, 2012 at 4:18 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-237479)
    
    Please ignore what I just said. I didn't read the question clearly.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-237479)
    
20.  ![](https://secure.gravatar.com/avatar/406508a7b110afdb100af0b5f9fa7d412add74b10827cd5a37a6aae62ea96a17?s=64&d=mm&r=g) Suril Mehta says:
    
    [October 5, 2016 at 7:12 am](https://chandoo.org/wp/formula-forensics-no-027/#comment-1304338)
    
    A different solution - this works with any leading character. Have used the concept from Formula Forensic No. 021 – Find the 4th Slash !
    
    Here B1 represents the leading character to be replaced.  
    \=MID(A1,MATCH(0,(VALUE(MID(A1,ROW(INDIRECT("1:200")),1))=$B$1)\*ROW(INDIRECT("1:200")),0),LEN(A1))
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-027/#comment-1304338)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-027/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Growing a Money Mustache using Excel \[for fun\]](https://chandoo.org/wp/growing-a-money-mustache-using-excel/) | [Excel Salary Survey Dashboard Contest Winners](https://chandoo.org/wp/salary-survey-contest-winners/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
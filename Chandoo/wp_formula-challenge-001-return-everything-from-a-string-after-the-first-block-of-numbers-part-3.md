# Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 3.)

**Source:** https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3

---

Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 3.)
==================================================================================================

[Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
 , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
 - 42 comments

  

Welcome back to yet another gripping episode of “When good formulas go _GREAT_”.

We’re working up the singles charts to the number one hit “[Formula Challenge 001 – Return everything in string after first block of numbers](http://chandoo.org/forums/topic/return-everything-in-string-after-first-block-of-numbers)
”

By way of a quick refresher, this formula challenge calls for a formula to return a substring from a longer string.

Those strings look something like this:

|     |     |
| --- | --- |
| **String:** | **Required Substring:** |
| Monaco7190**Australia1484** | Australia1484 |
| Liechtenstein42**Austria128590** | Austria128590 |
| Malta6**Belarus78** | Belarus78 |

   
   
So far we’ve heard from these crooners:

Jeff: [Formula Challenge 001 – Part 1](http://chandoo.org/wp/2013/07/16/formula-challenge-001-1/ "Formula Challenge 001 - Part 1")

Sajan: [Formula Challenge 001 – Part 2](http://chandoo.org/wp/2013/07/17/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/ "Formula Challenge 001 - Part 2")

You can download the challenge and full dataset here: [Formula Challenge 1.3](https://chandoo.org/wp/wp-content/uploads/2013/07/Formula-Challenge-1.3.xlsx)

Specifically, we need a formula to return only the second country and associated number …in the case of Monaco7190**Australia1484** it’s that bit in bold i.e. **Australia1484**

Part 3
------

Yesterday, Sajan and his band performed this hot Latin-infused number:

\=MID(A1,MODE(MMULT((N(ISNUMBER(-MID(A1,ROW(INDIRECT(“1:”&LEN(A1))),1)))={1,0})\*(ROW(INDIRECT(“1:”&LEN(A1)))-{0,1}),{1;1}))+1,LEN(A1))

Today, **Haseeb** shakes his groove thing in return, to the tune of this hard-rock anthem:

\=MID(A1,MIN(IFERROR(SEARCH(CHAR(ROW($65:$90)),A1,MIN(IFERROR(FIND(ROW($1:$10)-1,A1),””))+1),””)),LEN(A1))

_Rock and roll, baby!_

Haseeb’s orchestration is really clever:

### 1\. Find the position where every number in the string occurs:

Here’s how he does that:

\=FIND(ROW($1:$10)-1,A1)

\=FIND({1;2;3;4;5;6;7;8;9;10} -1,A1)

\=FIND({0;1;2;3;4;5;6;7;8;9} , A1)

\={10;8;#VALUE!;#VALUE!;21;#VALUE!;#VALUE!;7;22;9}

### 2\. Remove the errors…

\=IFERROR({10;8;#VALUE!;#VALUE!;21;#VALUE!;#VALUE!;7;22;9},””)

\={10;8;””;””;21;””;””;7;22;9}

### 3\. …so that we can work out which of these numbers occurs first in the string:

He does this by taking the MIN of them. Just like the judges on X-Factor, MIN doesn’t handle errors. Which is why he removed them in the last verse.

\=MIN({10;8;””;””;21;””;””;7;22;9})

\=8

So he’s already worked out where that first block of numbers begins – position 8 – meaning he can completely ignore any text that occurs before this position.

### 4\. Get the start of the second block:

Now he can search from position 8 for the _very next letter_. That letter will be the start of the text block we’re after. Ingenious.

\=SEARCH(CHAR(ROW($65:$90)),A1,8)

\=SEARCH({“A”;”B”;”C”;”D”;”E”;”F”;”G”;”H”;”I”;”J”;”K”;”L”;”M”;”N”;”O”;”P”;”Q”;”R”;”S”;”T”;”U”;”V”;”W”;”X”;”Y”;”Z”},A1,8)

\={11; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!; 18; #VALUE!; #VALUE!; 17; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!; 15; 13; 14; 12; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!}

###  5. Get rid of those errors with IFERROR:

\=IFERROR({11; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!; 18; #VALUE!; #VALUE!; 17; #VALUE!; #VALUE!;#VALUE!; #VALUE!; #VALUE!; 15; 13; 14; 12; #VALUE!; #VALUE!; #VALUE!; #VALUE!; #VALUE!},””)

\={11;””;””;””;””;””;””;””;18;””;””;17;””;””;””;””;””;15;13;14;12;””;””;””;””;””}

### 6\. Work out which of these letters occurs first in the string:

Again, he does this by taking the MIN of them:

\=MIN({11;””;””;””;””;””;””;””;18;””;””;17;””;””;””;””;””;15;13;14;12;C”;””;””;””;””})

\=11

### 7\. Split the string from that point forward:

\=MID(A1,11,LEN(A1))

\=Australia1484

Ahh, Australia again. ACDC, anyone?

[![IMG_0656RS - Copy](https://chandoo.org/wp/wp-content/uploads/2013/07/IMG_0656RS-Copy.jpg "Hui at AC/DC Perth 2010")](https://chandoo.org/wp/wp-content/uploads/2013/07/IMG_0656RS-Copy.jpg)

TNT, He’s dynamite

TNT and his formulas are tight

TNT, He’s an Excel nerd

TNT, A shorter formula would be absurd!

_…or **would** it ?_

Tune in same time on Monday and find out. And bring your air guitar this time.

About the Author.
-----------------

Jeff Weir – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure #VALUE!

Find out more at [http:www.heavydutydecisions.co.nz](http://www.heavydutydecisions.co.nz/ "http:www.heavydutydecisions.co.nz")

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
| Written by Hui...  <br>Tags: [char()](https://chandoo.org/wp/tag/char/)<br>, [iferror](https://chandoo.org/wp/tag/iferror/)<br>, [len()](https://chandoo.org/wp/tag/len/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [MIN()](https://chandoo.org/wp/tag/min/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [search](https://chandoo.org/wp/tag/search/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 42 Responses to “Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 3.)”

1.  ![](https://secure.gravatar.com/avatar/8d66fff8a8809045872e44f9c58af0cc8149a66c1b09fc2742eafc9b92c09727?s=64&d=mm&r=g) [ExcelStrategy](http://www.youtube.com/user/ExcelStrategy)
     says:
    
    [July 19, 2013 at 7:13 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440404)
    
    Time for my crazy formula !!!
    
    This one works for every number pattern and every string lenght !
    
    \=MID(B4;AGGREGATE(14;6;FIND(CHAR(ROW($65:$90));B4);1);255)
    
    And it does not need to be entered as an array 🙂
    
    Regards.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440404)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 19, 2013 at 7:41 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440412)
        
        Close, but unfortunately it fails on some of the challenge data. E.g. Norway734EuropeanUnion3206
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440412)
        
        *   ![](https://secure.gravatar.com/avatar/8d66fff8a8809045872e44f9c58af0cc8149a66c1b09fc2742eafc9b92c09727?s=64&d=mm&r=g) [ExcelStrategy](http://www.youtube.com/user/ExcelStrategy)
             says:
            
            [July 19, 2013 at 8:10 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440418)
            
            Yep i just noticed it falis on 9,75% of the sample data :\\
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440418)
            
2.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [July 19, 2013 at 7:44 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440414)
    
    Many thanks for Hui who put together the accompanying download file, and also entered this post and the last two into WordPress for me. Not to mention that he also attended an actual ACDC concert and took the photo above in anticipation of this blog post. Hui, you're a time-travelling mind reader.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440414)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 19, 2013 at 10:16 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440432)
        
        Why else would I attend the concert and take the photo ?
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440432)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [July 19, 2013 at 11:25 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440442)
            
            Isn't attending ACDC concerts like voting in your country, Hui?
            
            Over here, we're not legally compelled to do either. Although I'd much rather not vote...it just encourages the buggers.
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440442)
            
3.  ![](https://secure.gravatar.com/avatar/fa372ae2ae0b4063c593f2508015a4e433646256996cbc07aec12ea8d88e4a05?s=64&d=mm&r=g) Andrew Alexander says:
    
    [July 19, 2013 at 8:57 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440423)
    
    Here's a slight variation on this formula that makes use of FIND's case sensitive nature by searching for the second capital letter and taking the rest of the string from there (PROPER makes sure there's only two capital letters):
    
    \=RIGHT(A4,LEN(A4)-MAX(IFERROR(FIND(CHAR(ROW($65:$90)),PROPER(A4),1),0))+1)
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440423)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 19, 2013 at 11:22 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440441)
        
        Good approach, Andrew. Unfortunately it fails on the full sample dataset that I originally made available for the challenge, given some countries (mine included) have two capital letters. Try your formula out on Netherlands2684NewZealand6907 and you'll see what I mean.
        
        Granted, the cut-down dataset that is available from the link above doesn't have such countries...my bad. The original dataset is at [http://chandoo.org/forums/topic/return-everything-in-string-after-first-block-of-numbers](http://chandoo.org/forums/topic/return-everything-in-string-after-first-block-of-numbers)
         if you're interested.
        
        But well done, regardless.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440441)
        
        *   ![](https://secure.gravatar.com/avatar/fa372ae2ae0b4063c593f2508015a4e433646256996cbc07aec12ea8d88e4a05?s=64&d=mm&r=g) Andrew Alexander says:
            
            [July 19, 2013 at 12:46 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440460)
            
            Ah good spot, thanks! Although it wasn't that there were two capitals in the NewZealand part (proper would have lowered the Z anyway), it was that both countries began with N so MAX found the first one! I've amended the FIND part of the formula to start from the 2nd character of the string and it should now work:
            
            \=RIGHT(A1,LEN(A1)-MAX(IFERROR(FIND(CHAR(ROW($65:$90)),PROPER(A1),2),0))+1)
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440460)
            
4.  ![](https://secure.gravatar.com/avatar/0c71373bc01a0a1dc58d2ac7d3f84a0006fa472544e1c2ea12749672db247c6e?s=64&d=mm&r=g) ianamck says:
    
    [July 19, 2013 at 12:53 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440464)
    
    @Jeff
    
    Your just messing with my head now aren't you? Keeping it coming though I am still learning something.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440464)
    
5.  ![](https://secure.gravatar.com/avatar/0c71373bc01a0a1dc58d2ac7d3f84a0006fa472544e1c2ea12749672db247c6e?s=64&d=mm&r=g) ianamck says:
    
    [July 19, 2013 at 1:11 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440475)
    
    I do have one query. After reading the solution and doing some testing to better understand what is written I then start trying different data. So if I try using Peru1350France1485 for example Sajan's example gives me France1485 which is what you would expect.
    
    However Haseeb's gives me rance1485. Did I break something??????
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440475)
    
6.  ![](https://secure.gravatar.com/avatar/2f453e74af5b89fc30ab301b58a751d147f6366ba7b74ad1e857b5097346242b?s=64&d=mm&r=g) Greg G says:
    
    [July 19, 2013 at 3:04 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440487)
    
    "He does this by taking the MIN of them. Just like the judges on X-Factor, MIN doesn’t handle errors. Which is why he removed them in the last verse.
    
    \=MIN({10;8;”";”";21;”";”";7;22;9})
    
    \=8"
    
    I get 7, not 8.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440487)
    
    *   ![](https://secure.gravatar.com/avatar/2f453e74af5b89fc30ab301b58a751d147f6366ba7b74ad1e857b5097346242b?s=64&d=mm&r=g) Greg G says:
        
        [July 19, 2013 at 3:24 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440488)
        
        With the +1 in it (which isn't mentioned in that breakdown) then it becomes 8.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440488)
        
7.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [July 19, 2013 at 3:42 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440491)
    
    I already posted this but look like it was unseen. This one can handle any character after the numbers and not only letters A-Z.
    
    \=MID(A4,MATCH(TRUE,(MID(A4,ROW(A:A),1)\*ISERR(-MID(A4,ROW(A:A)+1,1)))>0,)+1,9^9)
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440491)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 19, 2013 at 5:22 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440501)
        
        @Elias  
        Chandoo.org is a moderated forum and so your post doesn't appear until approved
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440501)
        
8.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [July 19, 2013 at 5:11 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440497)
    
    I can reduce it to 76 characters length. It also does not get mess if users insert/delete a row/column.
    
    \=MID(A4,MATCH(TRUE,MID(A4,ROW(A:A),1)\*ISERR(-MID(A4,ROW(A:A)+1,1))>0,)+1,9^9)
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440497)
    
    *   ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) [Sajan](http://chandoo.org/wp/category/posts-by-sajan/)
         says:
        
        [July 19, 2013 at 8:00 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440513)
        
        Hi Elias,  
        Please check your formula against a string such as "Check1230Result1234".
        
        i.e. when the digit preceding the alphabet is 0.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440513)
        
        *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
            
            [July 19, 2013 at 8:20 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440515)
            
            I have to add 4 characters to avoid that issue.
            
            \=MID(A4,MATCH(TRUE,(1+MID(A4,ROW(A:A),1))\*ISERR(-MID(A4,ROW(A:A)+1,1))>0,)+1,9^9)
            
            Regards
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440515)
            
            *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
                 says:
                
                [July 19, 2013 at 10:33 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440518)
                
                Elias, that formula is intriguing. Will definitely write this up when I get a moment, along with your earlier pandigital approach. Thanks for the new tricks...gone straight into my toolkit.
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440518)
                
                *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
                     says:
                    
                    [July 19, 2013 at 11:28 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440523)
                    
                    Interesting. I never knew until just now when I checked out Elias' formula that if the third argument of MATCH is a comma followed by nothing else, Excel interprets this the same as if that third argument was FALSE or Zero. Guess that makes sense...INDEX works the same way. But I never new MATCH did. So that's a handy way to shorten a formula if you're answering a challenge (although I'd leave it in in a real-world situation).
                    
                    So with a blank comma as the 3rd agrument, all these are equivalent:  
                    \=MATCH(3,{1,2,4,5},)  
                    \=MATCH(3,{1,2,4,5},FALSE)  
                    \=MATCH(3,{1,2,4,5},0)  
                    \= #N/A
                    
                    And _without_ the comma, these are equivalent:  
                    \=MATCH(3,{1,2,4,5})  
                    \= MATCH(3,{1,2,4,5},TRUE)  
                    \= MATCH(3,{1,2,4,5},1)  
                    \= 2
                    
                    Also, it's interesting to note that MATCH can handle errors, so Elias doesn't have to add more code to strip them out.
                    
                    If you're interested in walking through Elias' formula, you might want to use this longer version that doesn't use whole row references, because a) it will calculate faster and b) you will be able to evaluate it bit by bit using either F9 or the Evaluate Formula functionality:  
                    \=MID(A1,MATCH(TRUE,(1+MID(A1,ROW(OFFSET(A$1,,,LEN(A1))),1))\*ISERR(-MID(A1,ROW(OFFSET(A$1,,,LEN(A1)))+1,1))>0,)+1,9^9)
                    
                *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
                     says:
                    
                    [July 19, 2013 at 11:44 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440525)
                    
                    If you're interested in walking through Elias' formula, you might want to use this longer version that doesn't use whole row references, because a) it will calculate faster and b) you will be able to evaluate it bit by bit using either F9 or the Evaluate Formula functionality:  
                    \=MID(A1,MATCH(TRUE,(1+MID(A1,ROW(OFFSET(A$1,,,LEN(A1))),1))\*ISERR( -MID(A1,ROW(OFFSET(A$1,,,LEN(A1)))+1,1))>0,)+1,9^9)
                    
                    Interesting. Very clever how he checks for numbers with this bit as well as offsets the array by one all in one clever move:  
                    1+MID(A1,ROW(OFFSET(A$1,,,LEN(A1))),1)
                    
                    ...and then checks for text with this bit without offsetting the array:  
                    ISERR( -MID(A1,ROW(OFFSET(A$1,,,LEN(A1)))+1,1))
                    
                    ...and then multiplies these arrays together, to find the first position where there is a number:  
                    MATCH(TRUE,{array}>0,)
                    
                    Genius!
                    
                *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
                    
                    [July 20, 2013 at 4:33 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440546)
                    
                    Jeff, we can reduce 2 characters your adapted formula by changing the second offset and deleting the +1.
                    
                    \=MID(A1,MATCH(TRUE,(1+MID(A1,ROW(OFFSET(A$1,,,LEN(A1))),1))\*ISERR(-MID(A1,ROW(OFFSET(A$2,,,LEN(A1))),1))>0,)+1,9^9)
                    
                    Or the following one if we don’t want to use a Volatile option.
                    
                    \=MID(A1,MATCH(TRUE,(1+MID(A1,ROW(A$1:INDEX(A:A,LEN(A1))),1))\*ISERR(-MID(A1,ROW(A$2:INDEX(A:A,LEN(A1))),1))>0,)+1,8^5)
                    
                    Regards
                    
9.  ![](https://secure.gravatar.com/avatar/d9ec70fe666db9ef710d63e625eee47a6cb1c396d6f1f6f5fb133ae7fff9bb1a?s=64&d=mm&r=g) Shrivallabha says:
    
    [July 19, 2013 at 5:31 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440502)
    
    Otta say that you have way wid words Jeff
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440502)
    
10.  ![](https://secure.gravatar.com/avatar/4cdf8c8300564d8c2e85bc91d8d7912cf28f9e2946ab40558aa185f49e577404?s=64&d=mm&r=g) Fowmy says:
    
    [July 21, 2013 at 1:56 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440674)
    
    Here go my solution . . . , its an array formula, confirm it with CTRL+SHIFT+ENTER keys.
    
    Text is in B4:
    
    \=MID(B4,MATCH(TRUE,--ISNUMBER(--MID(B4,ROW(INDIRECT("1:"&LEN(B4))),1))>--ISNUMBER(--MID(B4,ROW(INDIRECT("2:"&LEN(B4)+1)),1)),)+1,255)
    
    Any suggest/comments to improve my attempt will be appreciated.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440674)
    
11.  ![](https://secure.gravatar.com/avatar/0575c24503f5a5efd20ec37b052153619dcc24b875902c087beceaf478d97340?s=64&d=mm&r=g) [Christos Samaras](http://www.myengineeringworld.net/)
     says:
    
    [July 21, 2013 at 10:11 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440710)
    
    I hope it's not too late!  
    Assuming that Monaco7190Australia1484 is in A2, then in B2 we can write:
    
    \=MID(A2;MIN(IFERROR(SEARCH(CHAR(ROW($65:$90));A2;MIN(IFERROR(FIND(CHAR(ROW(48:56));A2);""))+1);""));LEN(A2))
    
    Of course it's an array formula, so CTRL + SHIFT + ENTER is required...
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440710)
    
    *   ![](https://secure.gravatar.com/avatar/0575c24503f5a5efd20ec37b052153619dcc24b875902c087beceaf478d97340?s=64&d=mm&r=g) [Christos Samaras](http://www.myengineeringworld.net/)
         says:
        
        [July 21, 2013 at 10:16 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440711)
        
        A small mistake:
        
        \=MID(A2;MIN(IFERROR(SEARCH(CHAR(ROW($65:$90));A2;MIN(IFERROR(FIND(CHAR(ROW($48:$57));A2);”"))+1);”"));LEN(A2))
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440711)
        
12.  ![](https://secure.gravatar.com/avatar/0575c24503f5a5efd20ec37b052153619dcc24b875902c087beceaf478d97340?s=64&d=mm&r=g) [Christos Samaras](http://www.myengineeringworld.net/)
     says:
    
    [July 22, 2013 at 7:28 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440773)
    
    Assuming that Monaco7190Australia1484 is in A2, then in B2 we can write:
    
    \=MID(A2,MIN(IFERROR(SEARCH(CHAR(ROW($65:$90)),A2,MIN(IFERROR(FIND(CHAR(ROW($48:$57)),A2),””))+1),””)),LEN(A2))
    
    Of course it’s an array formula, so CTRL + SHIFT + ENTER is required…
    
    CHAR(48) to CHAR(57) returns the numbers 0 to 9.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-440773)
    
13.  ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
    
    [July 25, 2013 at 3:40 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441172)
    
    \=MID(A2,LOOKUP(,-MID(9&LEFT(A2,LEN(A2)-(LEN(LOOKUP(,-RIGHT(A2&9,COLUMN(2:2))))-2)), COLUMN(2:2), 1), COLUMN(2:2)), 99)
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441172)
    
14.  ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
    
    [July 25, 2013 at 3:43 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441173)
    
    \=MID(A2;LOOKUP(;-MID(9&LEFT(A2;LEN(A2)-(LEN(LOOKUP(;-RIGHT(A2&9;COLUMN(2:2))))-2)); COLUMN(2:2); 1); COLUMN(2:2)); 99)
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441173)
    
15.  ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
    
    [July 25, 2013 at 3:44 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441175)
    
    AND  
    {=MID(A1;MATCH(2;1/(CODE(MID(9&A1;COLUMN(A1:Z1);1))64);1); 99)}
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441175)
    
16.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [July 25, 2013 at 6:54 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441201)
    
    Stef@n, that last formula doesn't work for me. Can you check it? Still looking at the previous formula.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441201)
    
    *   ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
        
        [July 26, 2013 at 7:53 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441252)
        
        Hi Jeff  
        oh - a ">" is missing ;O  
        this is the German formular  
        {=TEIL(A1;VERGLEICH(2;1/(CODE(TEIL(9&A1;SPALTE(A1:Z1);1))64);1); 99)}  
        i have probl to translate into an engl formular  
        perhaps - you can help  
        {=MID(A1;MATCH(2;1/(CODE(MID(9&A1;COLUMN(A1:Z1);1))64);1); 99)}
        
        Regards  
        Stef@n
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441252)
        
        *   ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
            
            [July 26, 2013 at 8:44 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441255)
            
            mmmh  
            the >< are already missing  
            \=TEIL(A1;VERGLEICH(2;1/(CODE(TEIL(9&A1;SPALTE(A1:Z1);1)) 64);1); 99)
            
            a before 64
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441255)
            
            *   ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
                
                [July 26, 2013 at 8:48 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441256)
                
                sorry - it does not work  
                i split it into different lines ..
                
                \=TEIL  
                (A1;VERGLEICH  
                (2;1/  
                (CODE  
                (TEIL  
                (9&A1;SPALTE  
                (A1:Z1);1))  
                64 'is bigger than sixtyfour  
                );1); 99)
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441256)
                
                *   ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
                    
                    [July 26, 2013 at 8:50 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441257)
                    
                    sorry, i can't publish it ... sorry  
                    the "is smaller than" an "is bigger than"  
                    will not be shown in the thread
                    
                *   ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
                    
                    [July 26, 2013 at 10:34 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441264)
                    
                    my last try 😉  
                    \=TEIL(A1;VERGLEICH(2;1/(CODE(TEIL(9&A1;SPALTE(A1:Z1);1))"is smaller than"58)/(CODE(TEIL(A1;SPALTE(A1:Z1);1))"is bigger than"64);1); 99)
                    
                    perhaps i can send an email / upload a picture
                    
                *   ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
                    
                    [July 28, 2013 at 9:17 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441466)
                    
                    Hi Jeff  
                    please "send" me your email-adress  
                    i will send you an email  
                    perhaps you can publish the formular :O  
                    ... the formular works 😉 ... is short AND interessing 😉  
                    Regards  
                    Stef@n
                    
17.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [July 25, 2013 at 7:10 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441204)
    
    Stef@n - that first formula you posted is a very clever approach indeed. I love it how you split the string into progressively longer bits from the right hand side so you can find the start of that last batch of numbers, and then truncate the string from the left so that those numbers are excluded.
    
    I've changed it so it doesn't use whole column references, in case anyone wants to evaluate it bit by bit:  
    \=MID(A1,LOOKUP(,-MID(9&LEFT(A1,LEN(A1)-(LEN(LOOKUP(,-RIGHT(A1&9,COLUMN(OFFSET(A1,,,,LEN(A1))))))-2)),COLUMN(OFFSET(A1,,,,LEN(A1))),1),COLUMN(OFFSET(A1,,,,LEN(A1)))),9^9)
    
    Looking forward to seeing your last formula, once you've reposted a version that works. I presume the wordpress parser ate some of it.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441204)
    
    *   ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
        
        [July 28, 2013 at 9:20 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441468)
        
        Hi Jeff  
        i will send you the formula via mail  
        because i can not publish it here on chandoo 🙁  
        Regards  
        Stef@n
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441468)
        
18.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [July 28, 2013 at 9:38 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441471)
    
    Stef@n: here it is in English:  
    \=MID(A1,MATCH(2,1/(CODE(MID(9&A1,COLUMN(A1:Z1),1)) is less than 58)/(CODE(MID(A1,COLUMN(A1:Z1),1)) is greater than 64),1),99)
    
    Very clever how you add a character to the start of one string in order to get an array that is one element out of alignment with the other array, so that when you convert them to true/false and divide one by the other, you can find the position you need.
    
    Will definitely include this in my next article in this series.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441471)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 28, 2013 at 10:21 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441474)
        
        This can be simplified further to:  
        \=MID(A1,1+MATCH(0,MID(A1,ROW(OFFSET(A1,,,LEN(A1),)),1)-MID(" "&A1,ROW(OFFSET(A1,,,LEN(A1),)),1),),9^9)
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-441474)
        
19.  ![](https://secure.gravatar.com/avatar/3a3c2b315b00e9a57768579f1d58fe00186f95bd11cc3bdebfa68fe7ba8c1a02?s=64&d=mm&r=g) Kundepuu says:
    
    [December 15, 2015 at 2:53 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-1103703)
    
    How handle scandinavian letters Ä,Ö,Å in formulas?
    
    String: Required Substring:  
    Monttu123Äänekoski Äänekoski34567
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#comment-1103703)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Are you interested in learning Power Pivot?](https://chandoo.org/wp/are-you-interested-in-learning-power-pivot/) | [Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 4.)](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
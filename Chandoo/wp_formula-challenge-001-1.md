# Formula Challenge 001 - Return everything from a string after the first block of numbers (Part 1)

**Source:** https://chandoo.org/wp/formula-challenge-001-1

---

Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 1.)
==================================================================================================

[Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
 , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
 - 43 comments

  

**The Formula Challenge Series: Where good formulas go GREAT:**

**Formula Challenge 001 – Return everything from a string after first block of numbers**

Introduction to the Formula Challenge series:
---------------------------------------------

Formulas are like the DNA of Excel…you can solve some very complicated evolutionary challenges by stringing together a few simple base-pairs in the right order.

Over at [http://chandoo.org/forums/forum/excel-challenges](http://chandoo.org/forums/forum/excel-challenges "http://chandoo.org/forums/forum/excel-challenges")
 you’ll find a whole bunch of tricky formula challenges posted by a group of excel nerds (me included) trying to out-nerd each other with formula nerdiness.

Consequently, these formula challenges are designed to get participants thinking creatively about how to solve a tricky problem using formulas only.

(Oh, and they might be designed to get a whole bunch of nerds to do my tricky work assignments for me too.)

\[Psst….so as to not hurt any feelings, I’m obliged to point out under the UN’s declaration of Super-Human Rights that one person who posted a response at this challenge is not an Excel Nerd, thus allowing everybody who posted to assume it was them.\]

\[Psst (again)…of course, in actual fact that lone non-nerd was in fact moi – but don’t tell them that…it will spoil their delusions of normality 😉 \]

Putting together a formula to tackle these challenges shows you have a great mastery of excel. Putting together a formula that tackles the challenge and is also shorter than anyone else’s is something more akin to standing on the gold podium at the Olympics and shouting “In yer face, LOSERS” down to the silver and bronze teams while you strut your best Jagger strut to the Windows 95 launch song. [http://www.youtube.com/watch?v=5VPFKnBYOSI](http://www.youtube.com/watch?v=5VPFKnBYOSI "http://www.youtube.com/watch?v=5VPFKnBYOSI")

(Yes, it’s actually that satisfying to a true Excel nerd. Or so I’m told.)

Anyway….I’ve learned a lot from looking at how different people tackle these, and my formula toolkit is much bigger as a result.

To help you increase your toolkit, today we’re going to take a look at the first challenge in this series:

Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 1).
--------------------------------------------------------------------------------------------------

Without further ado, here’s the details of the first challenge:

*   Split the strings in Column A with a formula that only returns the substring that you see in column B. So for instance, if the string is Monaco7190Australia1484 then we want everything to the right of that first block of numbers i.e. Australia1484.
*   Your formula should handle any length of string, and any length of numbers – not just the lengths shown below
*   You should not use any helper cells, intermediate formulas or named ranges, or VBA

Those strings look something like this:

|     |     |
| --- | --- |
| **String:** | **Required Substring:** |
| Monaco7190**Australia1484** | Australia1484 |
| Liechtenstein42**Austria128590** | Austria128590 |
| Malta6**Belarus757812** | Belarus757812 |

You can download the challenge and full dataset here: [Formula Challenge 1.1](https://chandoo.org/wp/wp-content/uploads/2013/07/Formula-Challenge-1.1.xls)

The bit that’s required to be returned is the Blue **Bold** bit i.e. the block of text and numbers after the first block of text and numbers, which in the case of Monaco7190Australia1484 is Australia1484.

What’s tricky about this challenge is that we have a block of text, followed by a block of numbers, followed by the block of text/number that we actually want to extract. So it’s hard to pinpoint the location of that 2nd block of text/numbers given there’s a preceding block of text/numbers.

Despite having a head start of several weeks on this challenge (I first conceived of the approach when answering a post a weeks before posting the problem as a challenge) and despite (or perhaps because of) taking copies amounts of performance-enhancing drugs, I didn’t even make it onto that Olympic podium. Instead, I arrived huffing and puffing at the finish line with this unwieldy beast:

\=MID(A1,1+MATCH(1,(CODE(MID(A1,ROW(A$1:INDEX(A:A,LEN(A1))),1))<58)\*(CODE(MID(A1&”a”,ROW(A$2:INDEX(A:A,LEN(A1)+1)),1))>57),0),LEN(A1))

The approach I took was to try to find the point at which we have a number immediately followed by a letter.

For instance, the zero and letter A from Monaco7190Australia1484. To do this:

### 1\. I dynamically break the string apart into one-digit bites with this:

\= (MID(A1,ROW(A$1:INDEX(A:A,LEN(A1))),1)

Excel returns: \={“M”;”o”;”n”;”a”;”c”;”o”;”7″;”1″;”9″;”0″;”A”;”u”;”s”;”t”;”r”;”a”;”l”;”i”;”a”;”1″;”4″;”8″;”4″}

### 2\. Wrap a code function around that which converts these to the specific number that Excel uses to represent each number/letter:

\=CODE({“M”;”o”;”n”;”a”;”c”;”o”;”7″;”1″;”9″;”0″;”A”;”u”;”s”;”t”;”r”;”a”;”l”;”i”;”a”;”1″;”4″;”8″;”4″})

Excel returns: \={77;111;110;97;99;111;55;49;57;48;65;117;115;116;114;97;108;105;97;49;52;56;52}

### 3\. Work out which of those codes represents numbers.

ie: All numbers fall before character code 58

\={77;111;110;97;99;111;55;49;57;48;65;117;115;116;114;97;108;105;97;49;52;56;52}<58

Excel returns: \={FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE}

### 4\. Repeat steps 1 to 3 but this time I check for the occurrence of letters.

Furthermore I make a change so that the resulting array is offset by one position, by changing the ROW(A$1… bit in 1 to ROW(A$2… :

\=CODE(MID(A1&”a”,ROW(A$2:INDEX(A:A,LEN(A1)+1)),1))>57

Excel returns: ={TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE}

### 5\. Multiply these two arrays together

This converts these TRUE and FALSE numbers to Ones and Zeros.

Furthermore, because that 2nd array is offset by one, this gives me the position where a letter and a number coincide. (Which – given that 2nd array has been offset – is equivalent to identifying the occurrence of where a number is immediately followed by a letter:

\={FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE} \* {TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE}

Excel returns: \={0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;1}

### 6\. All I need to do then is to identify where that first 1 falls in this array:

\=MATCH(1,{0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;1},0)

Excel returns: =10

### 7\. …and then return all of the original string to the right of that position:

\=MID(A1,1+10,LEN(A1))

Excel returns: =Australia1484

Summary
-------

Neat, eh?

Well, I thought so.

In fact, I thought that would be a sure-fire winner of the challenge.

But that didn’t even get me the Bronze. Rather, that honour belongs to **Sajan**, who scooped up the consolation prize with this little beauty:

\=MID(A1,MODE(MMULT((N(ISNUMBER(-MID(A1,ROW(INDIRECT(“1:”&LEN(A1))),1)))={1,0})\*(ROW(INDIRECT(“1:”&LEN(A1)))-{0,1}),{1;1}))+1,LEN(A1))

…which requires you to pre-emptively take a whole bottle aspirin AND get a good nights’ sleep before trying to wrap your head around it.

So go take that aspirin, take your pens out of your pocket, and hit the pillow, and I’ll see you back here this time tomorrow for some Einsteinium formula relativity as we tackle this gem of an approach in Part 2.

About the Author.
-----------------

**Jeff Weir** – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure #VALUE!

Find out more at [http://www.heavydutydecisions.co.nz](http://www.heavydutydecisions.co.nz/ "http://www.heavydutydecisions.co.nz")

### Comments from Hui:

Jeff has been a valuable contributor at Excel Hero Academy during the past two years and recently started posting at the [Chandoo.org Forums](http://chandoo.org/forums/profile/jeffreyweir "Chandoo.org Forums")

This is Jeff’s First post at Chandoo.org and I am sure you will welcome his verbose narrative to these interesting Formula Challenges

Please leave comments and feedback and alternative solutions in the comments below.

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
| Written by Hui...  <br>Tags: [code](https://chandoo.org/wp/tag/code/)<br>, [INDEX()](https://chandoo.org/wp/tag/index/)<br>, [len()](https://chandoo.org/wp/tag/len/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 43 Responses to “Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 1.)”

1.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [July 16, 2013 at 8:15 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-439976)
    
    Thanks Hui. This was actually my 2nd post. First is at [http://chandoo.org/wp/2009/07/24/medicare-chart-critique/](http://chandoo.org/wp/2009/07/24/medicare-chart-critique/)
    
    Looking forward to doing more.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-439976)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 16, 2013 at 8:38 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-439978)
        
        Wow that was the day before my first visit and the day the forums started.  
        I hope the third doesn't take as long as the second did.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-439978)
        
2.  ![](https://secure.gravatar.com/avatar/29bbca105e236cdc542ea85079cfe1464fb7a0cf9edec0f9dde1a9c2f03af0e0?s=64&d=mm&r=g) Chris Byham says:
    
    [July 16, 2013 at 9:30 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-439985)
    
    Hi Jeff,
    
    Nice post - I looked at the problem first and then looked through your solution, and I'm afraid to say mine was almost the same as yours, apart from using ISNUMBER instead of CODE as per formula below:
    
    \=MID(A1,MATCH(1,ISNUMBER(1\*MID(A1,ROW(A$1:INDEX(A:A,LEN(A1))),1))=TRUE)\*ISNUMBER(1\*MID(A1,ROW(A$1:INDEX(A:A,LEN(A1)))+1,1))=FALSE),0)+1,LEN(A1))
    
    which, whilst a little longer in length than the code version, can be read more easily than the 'Code' option.
    
    Look forward to more posts. And thanks for highlighting the Challenges forum too - whilst being a long-time reader of Chandoo's blog, I seem to have somehow overlooked this - but know where I'm going to be spending a lot of time now!!
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-439985)
    
3.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [July 16, 2013 at 10:52 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-439996)
    
    Good skills, Chris. I'm the same as you...long time reader of this blog but somehow have not managed to spend much time on the Forum. But I tell ya what...I've learned as much from the Forum in the last month as I've learned in the last year on my own.
    
    There's three more posts to come on this challenge alone, so stay tuned.
    
    Regards
    
    Jeff
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-439996)
    
4.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [July 16, 2013 at 1:54 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440006)
    
    Excellent write up Jeff.... Welcome back to the guest author spot. I am eager to read remaining parts of this and other challenges. I found the questions in forum really interesting and quite challenging.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440006)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 16, 2013 at 7:09 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440038)
        
        Thanks Chandoo. It's a bit overdue...I promised you a few guest posts back when your twins were born!
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440038)
        
    *   ![](https://secure.gravatar.com/avatar/08cc1ad470c52d479f2a8b76dbaf25746e968ea92f698313549c202e59abca9e?s=64&d=mm&r=g) Kutty says:
        
        [August 15, 2013 at 8:45 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-443316)
        
        Hai Chandoo,I have an error in my formula during the sixth steps doing..  
        I have a formula  
        \=CODE(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1))>57  
        \*CODE(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1))<58
        
        but i got All are True ..
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-443316)
        
5.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [July 16, 2013 at 3:09 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440016)
    
    One more option.
    
    \=MID(A4,MATCH(1,(CODE(MID(A4,ROW($1:$255),1))>57)\*(ROW($1:$255)>MIN(FIND(ROW($1:$10)-1,A4&57321^2))),0),255)
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440016)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 16, 2013 at 7:12 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440040)
        
        Hi Elias. Unfortuntanely it fails on the _Your formula should handle any length of string, and any length of numbers – not just the lengths shown above/below_ count.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440040)
        
        *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
            
            [July 16, 2013 at 9:39 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440047)
            
            Hi Jeff, the formula can handles any length of numbers and 255 characters string, but if we change the 255 for 32,767 it will handle the max number of characters that a cell can contain.
            
            \=MID(A4,MATCH(1,(CODE(MID(A4,ROW($1:$32767),1))>57)\*(ROW($1:$32767)>MIN(FIND(ROW($1:$10)-1,A4&57321^2))),0),32767)
            
            Regards
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440047)
            
            *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
                 says:
                
                [July 16, 2013 at 10:28 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440051)
                
                Good stuff, Elias. Your formula can be made even shorter:  
                \=MID(A1,MATCH(1,(CODE(MID(A1,ROW(A:A),1))>57)\*(ROW(A:A)>MIN(FIND(ROW($1:$10)-1,A1&57321^2))),0),32767)
                
                ...although those whole-column references make it really really resource intensive!
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440051)
                
                *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
                     says:
                    
                    [July 16, 2013 at 10:42 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440052)
                    
                    And shorter again with this:  
                    \=MID(A1,MATCH(1,(CODE(MID(A1,ROW(A:A),1))>57)\*(ROW(A:A)>MIN(FIND(ROW(A:A)-1,A1&57321^2))),0),8^5)
                    
                    ...and could go shorter still if you can find a shorter way to write a similar digit to 57321^2 that includes all digits from 0 to 9.
                    
                    That is a masterstroke, by the way...what a great way to ensure you will always get a match for each number. How did you come up with that concept? It's not one I've seen before.
                    
                *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
                     says:
                    
                    [July 16, 2013 at 10:50 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440054)
                    
                    Ahh, I see they are called pandigital numbers. Freakin' awesome.
                    
                *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
                     says:
                    
                    [July 16, 2013 at 11:25 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440058)
                    
                    Here's a shorter way to write a pandigital number than 57321^2  
                    7^18
                    
                    ...which means we can tighten that puppy up even more:  
                    \=MID(A1,MATCH(1,(CODE(MID(A1,ROW(A:A),1))>57)\*(ROW(A:A)>MIN(FIND(ROW($1:$10)-1,A1&7^18))),0),9^9)
                    
                *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
                    
                    [July 17, 2013 at 1:53 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440142)
                    
                    Hi Jeff, I’m glad you liked the formula. I used to use A1&1234567890 to avoid the error when finding/searching for numbers from 0 to 9, but I learned the pandigital way from Roberto Mensa in the ExcelHero LinkedIn group.
                    
                    Regards
                    
6.  ![](https://secure.gravatar.com/avatar/3a6f8f9173c7fc770b7cebd2a9a5b94b833c505427f24dd0f5b276f710599fd9?s=64&d=mm&r=g) Sammy.Adade says:
    
    [July 16, 2013 at 4:17 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440024)
    
    Realized both blocks of numbers are four-digit. Hence came up with this:  
    \=MID(A6,MATCH(TRUE,ISNUMBER(--MID(A6,ROW(INDIRECT("1:"&LEN(A6))),1)),0)+4,LEN(A6)-MATCH(TRUE,ISNUMBER(--MID(A6,ROW(INDIRECT("1:"&LEN(A6))),1)),0)+3)
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440024)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 16, 2013 at 4:40 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440027)
        
        @Sammy  
        Both blocks don't have to be 4 characters long  
        It's one of the criteria
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440027)
        
7.  [Formula Challenge 001 - Return everything from a string after the first block of numbers (Part 2.) | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2013/07/17/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/)
     says:
    
    [July 17, 2013 at 7:00 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-440101)
    
    \[...\] you’ll keenly recall from yesterday’s gripping episode of “When good formulas go GREAT”, Sajan claimed Bronze in our inaugural formula challenge at Formula Challenge 001 – Return \[...\]
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440101)
    
8.  ![](https://secure.gravatar.com/avatar/2ce0b6860ea486b9f91f5ba8422b861e6ce4439b6e01aa261df22a30301fec8f?s=64&d=mm&r=g) juanito says:
    
    [July 17, 2013 at 8:53 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-440112)
    
    Thanks for the interesting challenge, Jeff - coffee was a little more fun this morning!  
    Well, I came up with a solution very similar to Chris's. In a sense all solutions will be directionally similar, I believe, in that we must test for position n where n is the first ocurrence of \*n is digit\* and \*n+1 is text\* - this (I think inevitably) requires multiplying two boolean arrays
    
    \=MID(A1;MATCH(1;ISNUMBER(MID(A1;ROW(A1:INDEX(A:A;LEN(A1)));1)+0)\*NOT(ISNUMBER(MID(A1;ROW(A1:INDEX(A:A;LEN(A1)))+1;1)+0));0)+1;LEN(A1)) (array-entered)
    
    \- Juanito
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440112)
    
9.  ![](https://secure.gravatar.com/avatar/748c1cf4bbbedb2cfb5e18c07ce86bd4f750b3f805c05d5b0101b8b857a8909e?s=64&d=mm&r=g) Matt Healy says:
    
    [July 18, 2013 at 2:45 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-440224)
    
    For this sort of task, I run my data through Perl so I can use its powerful one-liners. Sometimes as I am slicing and dicing my data, I'll make multiple round trips between Excel and Perl.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440224)
    
10.  ![](https://secure.gravatar.com/avatar/a4b2f07b9fd4e56ff4b5bef3158f7acefb90822374e9d320c40c7675201e0be4?s=64&d=mm&r=g) Chris Rowley says:
    
    [July 18, 2013 at 7:01 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440326)
    
    Hi All,
    
    This is my attempt........It needs entering via ctrl + shift + enter and change A1 for whatever cell the data is in
    
    \=RIGHT(A1,LEN(A1)-MIN(IFERROR(SEARCH({“A”,”B”,”C”,”D”,”E”,”F”,”G”,”H”,”I”,”J”,”K”,”L”,”M”,”N”,”O”,”P”,”Q”,”R”,”S”,”T”,”U”,”V”,”W”,”X”,”Y”,”Z”},A1,MIN(IFERROR((SEARCH({1,2,3,4,5,6,7,8,9},A1,1)),”")))-1,”")))
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440326)
    
11.  ![](https://secure.gravatar.com/avatar/c06367652c10e62a49c0a7c1772fd2900c5d378d5a7dbe5fe55244230eb8d10e?s=64&d=mm&r=g) Sartori says:
    
    [July 18, 2013 at 9:04 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440337)
    
    This is my try. It assumes the second text block will always start with a capital letter:
    
    {=RIGHT(A1,1+LEN(A1)-SMALL(FIND(CHAR(ROW(INDIRECT("65:90"))),A1&"ABCDEFGHIJKLMNOPQRSTUVWXYZ",2),1))}
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440337)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 18, 2013 at 10:41 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440345)
        
        Sartori - the problem with this is that it fails when the first country has two capital letters e.g. NewZealand.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440345)
        
12.  ![](https://secure.gravatar.com/avatar/0c71373bc01a0a1dc58d2ac7d3f84a0006fa472544e1c2ea12749672db247c6e?s=64&d=mm&r=g) ianamck says:
    
    [July 18, 2013 at 10:30 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440343)
    
    To be perfectly honest I am way out of my depth here. But I follow the blog and learn. I read the forum responses (even helping if I can) and learn. I ask questions and get great responses and learn. I am reading this article and although like I said I am out of my depth I still continue to learn.
    
    pandigital numbers........... cmon guys give me a chance here that's something new to start reading about. My head hurts but looking forward to your next episode Jeff
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440343)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 18, 2013 at 10:37 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440344)
        
        Given the complexity of explaining some of these approaches, my next episode is likely to be a psychotic one 🙂
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440344)
        
13.  ![](https://secure.gravatar.com/avatar/a4b2f07b9fd4e56ff4b5bef3158f7acefb90822374e9d320c40c7675201e0be4?s=64&d=mm&r=g) Chris R says:
    
    [July 19, 2013 at 5:41 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-440394)
    
    Jeff,
    
    Can you let me know if mine worked ok or if I missed a trick? I was unable to test it on the actual file so had to simulate date, do was just curious.
    
    Thanks  
    Chris
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440394)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 19, 2013 at 11:16 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-440440)
        
        Works fine, Chris. Good skills. In fact, that's pretty much the approach that I cover in the next post at [http://chandoo.org/wp/2013/07/19/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/](http://chandoo.org/wp/2013/07/19/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/)
         albeit with a shorter version of the formula.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440440)
        
        *   ![](https://secure.gravatar.com/avatar/a4b2f07b9fd4e56ff4b5bef3158f7acefb90822374e9d320c40c7675201e0be4?s=64&d=mm&r=g) Chris Rowley says:
            
            [July 19, 2013 at 12:39 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440454)
            
            Cheers Jeff, thanks for letting me know.
            
            I look forward to reading the post.
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440454)
            
14.  [Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 3.) | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2013/07/19/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/)
     says:
    
    [July 19, 2013 at 7:03 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-440402)
    
    \[...\] Jeff: Formula Challenge 001 – Part 1 \[...\]
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440402)
    
15.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [July 19, 2013 at 3:41 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440489)
    
    I already posted this but look like it was unseen. This one can handle any character after the numbers and not only letters A-Z.
    
    \=MID(A4,MATCH(TRUE,(MID(A4,ROW(A:A),1)\*ISERR(-MID(A4,ROW(A:A)+1,1)))>0,)+1,9^9)
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440489)
    
16.  ![](https://secure.gravatar.com/avatar/3b23ba31bc239880246ac989b02bab3dfbc6a87a3333c86eedeed98db64bfb91?s=64&d=mm&r=g) WWCII says:
    
    [July 19, 2013 at 4:18 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440492)
    
    A5 contents: Liechtenstein4352Austria8590
    
    Formula:  
    \=SUBSTITUTE(TRIM(CLEAN(MID(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A5,1,8),2,8),3,8),4,8),5,8),6,8),7,8),8,8),9,8),0,8),FIND(8888,SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A5,1,8),2,8),3,8),4,8),5,8),6,8),7,8),8,8),9,8),0,8),1)+4,88))),8888,"")&TRIM(CLEAN(RIGHT(A5,4)))
    
    Formula Output: Austria8590
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440492)
    
17.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [July 19, 2013 at 5:12 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440500)
    
    I can reduce it to 76 characters length. It also does not get mess if users insert/delete a row/column.
    
    \=MID(A4,MATCH(TRUE,MID(A4,ROW(A:A),1)\*ISERR(-MID(A4,ROW(A:A)+1,1))>0,)+1,9^9)
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440500)
    
18.  ![](https://secure.gravatar.com/avatar/8519d721021b48b1ef577ec6ffed552c1334562b1fd29529b702123ed2270776?s=64&d=mm&r=g) JP Ronse says:
    
    [July 19, 2013 at 6:01 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440503)
    
    Hi All,
    
    I've developed my own functions to do this by using regular expression. My formula looks as:
    
    \=RegExp\_Extract(A1,"(\[0-9\]+)(\[A-Z\].\*$)","$2")
    
    It would lead much to far to explain the use of RE's (regular expressions) but is common use.
    
    Just as an example: =RegExp\_Extract(A1;"(\[0-9\]+)(\[A-Z\]+)(\[0-9\]+$)";"$2")
    
    extracts "Australia". The functions have even the option to use case sensitive comparisons.
    
    Wkr,
    
    JP Ronse
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440503)
    
19.  ![](https://secure.gravatar.com/avatar/5671034704d280c4a557ef7ac78e92a0ae9df0246d7eb707283548ec2c7af157?s=64&d=mm&r=g) GJ says:
    
    [July 21, 2013 at 1:20 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440670)
    
    Nice post Jeff! Looking forward to reading more from you 🙂
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440670)
    
20.  [Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 4.) | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2013/07/22/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/)
     says:
    
    [July 22, 2013 at 7:15 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-440770)
    
    \[...\] Jeff: Formula Challenge 001 – Part 1 \[...\]
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440770)
    
21.  ![](https://secure.gravatar.com/avatar/1be8ea2727b99e8b08d715d6cf7e8b7b0079f0ed1c69e9beb0d92b4cf5fa1a2c?s=64&d=mm&r=g) [Shangz(like Shance)](http://www.shangbaby.net/)
     says:
    
    [July 23, 2013 at 5:40 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-440898)
    
    Hello everyone. I am new to the forum and wanted to see if I could at least think my way through the challenge to a solution I would hope could work for me. I would like some feedback on my solution. Where should I post my solution to the substring challenge?
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440898)
    
22.  [Blog Posts of the Week (14th - 20th July 2013) - The South Asia MVP Blog - Site Home - TechNet Blogs](http://blogs.technet.com/b/southasiamvp/archive/2013/07/23/blog-posts-of-the-week-14th-20th-july-2013.aspx)
     says:
    
    [July 23, 2013 at 1:37 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-440944)
    
    \[...\] Return everything from a string after the first block of numbers \[...\]
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-440944)
    
23.  ![](https://secure.gravatar.com/avatar/63e48b04a65705729faa16c4209c29b041516c90bd69c2d2fd62bb323c48e8ad?s=64&d=mm&r=g) [Carl](http://chandoo.org/)
     says:
    
    [July 25, 2013 at 8:00 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-441211)
    
    Dear Chandoo, I am new to this post and I really like the responses every gave. I know I'm not that smart about excel but I think I can get around this. Please forgive me for rambling along. I'm retired and disabled and I thought I knew something about Excel but I don't. I look froward to your help in the future too.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-441211)
    
24.  [Some Power Query/M Examples | Chris Webb's BI Blog](http://cwebbbi.wordpress.com/2013/08/16/some-power-querym-examples/)
     says:
    
    [August 16, 2013 at 10:31 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-443372)
    
    \[...\] [http://chandoo.org/wp/2013/07/16/formula-challenge-001-1/](http://chandoo.org/wp/2013/07/16/formula-challenge-001-1/)
     \[...\]
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-443372)
    
25.  ![](https://secure.gravatar.com/avatar/75c334365ff4885a44651a26505d1dad31307eafc37667131ab9089d8594d1ff?s=64&d=mm&r=g) Haz says:
    
    [July 16, 2014 at 6:45 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-574020)
    
    {=MID(A4,MAX(IFERROR(FIND(ROW(A$1:A$10)-1&(CODE(COL($A1:$Z1)+96)),A4),),1)+1,LEN(A4))}
    
    Since the string is always broken with a number followed by a letter, that's what I seached for.  
    The ROW(A$1:A$10)-1&(CODE(COL($A1:$Z1)+96)) part will create a matrix with all (260!) combinations from "0a" to "9z", then you just have to look for it in the initial string and return the second part.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-574020)
    
26.  ![](https://secure.gravatar.com/avatar/d1e3ed89fd6869c8137c499376d02ac83cef7a36940f84dbe8f1a87f5c166dde?s=64&d=mm&r=g) [argent sur le web](http://argentenligne.net/)
     says:
    
    [July 16, 2016 at 4:55 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-1233897)
    
    Undeniably believe that which you said. Your favorite  
    justification appeared to be on the net the simplest thing to be aware of.
    
    I say to you, I certainly get annoyed while people think about worries that  
    they just don't know about. You managed to hit the nail upon the top as well as defined out the whole thing without having side effect ,  
    people can take a signal. Will likely be back to  
    get more. Thanks
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-1233897)
    
27.  ![](https://secure.gravatar.com/avatar/024dc51a744bb34fde7f5170198ec1e4f80dcd274aca53531839adba0d1218ee?s=64&d=mm&r=g) Steve Jobs says:
    
    [August 13, 2016 at 7:35 am](https://chandoo.org/wp/formula-challenge-001-1/#comment-1254451)
    
    Nice post. I learn something new and challenging on websites I stumbleupon every day.  
    It will always be exciting to read through articles from  
    other authors and practice something from thesir websites.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-1254451)
    
28.  ![](https://secure.gravatar.com/avatar/e7f2fe71d82b4ff511ca412fb10ebccb2cf0be8ccbc9551e1becda1699e9343b?s=64&d=mm&r=g) Calvin says:
    
    [December 22, 2016 at 1:05 pm](https://chandoo.org/wp/formula-challenge-001-1/#comment-1374627)
    
    \=MID(A1,SMALL(IFERROR(IF(LEN(IFERROR(VALUE(MID(A1,ROW(INDIRECT("2:"&LEN(A1)+1)),1)),"")&IFERROR(VALUE(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)),""))=1,ROW($1:$10000),""),""),2)+1,1000)
    
    Pasted this in B2. An array formula. Great examples above...
    
    \-Calvin
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-1/#comment-1374627)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-challenge-001-1/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Never use simple numbers in your dashboards (bonus tip: how to fix default conditional formatting)](https://chandoo.org/wp/never-use-simple-numbers-in-your-dashboards/) | [Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 2.)](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
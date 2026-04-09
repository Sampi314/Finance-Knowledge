# Formula Challenge 001 - Return everything from a string after the first block of numbers (Part 2.)

**Source:** https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2

---

Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 2.)
==================================================================================================

[Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
 , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
 - 46 comments

  

Welcome back. Get a good night’s sleep? Great.

Hopefully you had freshly-picked brain-function-enhancing blueberries for breakfast, and a red bull or five, because you’re gonna need it. Why? Because today, my friends, we peek inside the multi-dimensional mind of Sajan the Excel Magician.

As you’ll keenly recall from yesterday’s gripping episode of “[When good formulas go GREAT](http://chandoo.org/wp/2013/07/16/formula-challenge-001-1/ "When Good Formulas go GREAT")
”, Sajan claimed Bronze in our inaugural formula challenge at Formula Challenge 001 – Return everything in string after first block of numbers

By way of a quick refresher, this formula challenge calls for a formula to return a substring from a longer string. Those strings look something like this:

|     |     |
| --- | --- |
| **String:** | **Required Substring:** |
| Monaco7190**Australia1484** | Australia1484 |
| Liechtenstein42**Austria128590** | Austria128590 |
| Malta130612**Belarus8** | Belarus8 |

You can download the challenge and full dataset here: [Formula Challenge 1.2](https://chandoo.org/wp/wp-content/uploads/2013/07/Formula-Challenge-1.2.xlsx)
 (Excel 2007+ only, because the formulas have too many nested formulas for earlier Excel versions to handle)

Specifically, we need a formula to return only the second country and associated number …in the case of Monaco7190**Australia1484** it’s that bit in bold i.e. Australia1484

Sajan the Magician split those strings with this award-winning beauty:

\=MID(A1,MODE(MMULT((N(ISNUMBER(-MID(A1,ROW(INDIRECT(“1:”&LEN(A1))),1)))={1,0})\*(ROW(INDIRECT(“1:”&LEN(A1)))-{0,1}),{1;1}))+1,LEN(A1))

How does this wizardly wonder work? Let’s find out…

### 1\. Sajan splits apart the source string into it’s characters

This is as I did in the last post, albeit using a slightly different formula than I did:

\=MID(A1,ROW(INDIRECT(“1:”&LEN(A1))),1)

\=MID(A1,{1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23},1)

\={“M”;”o”;”n”;”a”;”c”;”o”;”7″;”1″;”9″;”0″;”A”;”u”;”s”;”t”;”r”;”a”;”l”;”i”;”a”;”1″;”4″;”8″;”4″}

### 2\. Then he adds zero to the array

This coerces any numbers stored as text into numbers, while causing the text bits to throw errors

\={“M”;”o”;”n”;”a”;”c”;”o”;”7″;”1″;”9″;”0″;”A”;”u”;”s”;”t”;”r”;”a”;”l”;”i”;”a”;”1″;”4″;”8″;”4″} +0

\={#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;7;1;9;0; #VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;1;4;8;4}

### 3\. Wrap an ISNUMBER around this unsightly spawn of Satan,

This turns numbers to True, and turns those hideously unnatural errors of nature to better-behaved booleans: \=ISNUMBER({#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;7;1;9;0;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;1;4;8;4})

\={FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE}

### 4\. Turn this array into Ones and Zeros, and checks if it equals either One or Zero.

I know…me too. But let’s give him the benefit of the doubt for now, and see what rabbit hole he’s leading us down…we might yet pop out of a magicians’ hat:

\=N({FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE})={1,0}

\={0;0;0;0;0;0;1;1;1;1;0;0;0;0;0;0;0;0;0;1;1;1;1}={1,0}

\={FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;TRUE,FALSE;TRUE,FALSE;TRUE,FALSE;TRUE,FALSE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;TRUE,FALSE;TRUE,FALSE;TRUE,FALSE;TRUE,FALSE}

What this has done in effect is create a 2D array – with one column of the array being the inverse of the other. So one column records whether something is a number, and the other records whether something isn’t a number. I know…me too. But maybe it would help if we saw what this would look like if entered over an Excel range, with our original string down the side so we can try and work out what spell this Wizard is whipping together:

[![FC021](https://chandoo.org/wp/wp-content/uploads/2013/07/FC021.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/FC021.png)

###  5. He then creates a second 2d array with this bit:

\=(ROW(INDIRECT(“1:”&LEN(A16)))-{0,1})

\={1,0;2,1;3,2;4,3;5,4;6,5;7,6;8,7;9,8;10,9;11,10;12,11;13,12;14,13;15,14;16,15;17,16;18,17;19,18;20,19;21,20;22,21;23,22}

…which if we were to enter over an Excel range would look like this:

[![FC022](https://chandoo.org/wp/wp-content/uploads/2013/07/FC022.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/FC022.png)

### 6\. He then throws this array into his wizard’s cauldron together with the array in 5 – along with generous portions of Eye of newt, toe of frog, wool of bat and tongue of dog. (This simply means Multiply the two previous Arrays)

This gives us the following:

\={FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;TRUE,FALSE;TRUE,FALSE;TRUE,FALSE;TRUE,FALSE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;FALSE,TRUE;TRUE,FALSE;TRUE,FALSE;TRUE,FALSE;TRUE,FALSE}\*{1,0;2,1;3,2;4,3;5,4;6,5;7,6;8,7;9,8;10,9;11,10;12,11;13,12;14,13;15,14;16,15;17,16;18,17;19,18;20,19;21,20;22,21;23,22}

\={0,0;0,1;0,2;0,3;0,4;0,5;7,0;8,0;9,0;10,0;0,10;0,11;0,12;0,13;0,14;0,15;0,16;0,17;0,18;20,0;21,0;22,0;23,0}

…which again would look like this if entered over an Excel range (with our original string down the side by way of reference):

[![FC023](https://chandoo.org/wp/wp-content/uploads/2013/07/FC023.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/FC023.png)

Well mess up my hair, and call me Einstein. Because now I see what all that was about. The only time that the same number in that first array also appears in that second array is that magical place where the first block of numbers ends, and the second block of letters begins. That is some serious sorcery!

### 7\. Multiply the arrays

Next he conjures this 2D array into 1D, with the help of MMULT.

Microsoft tells us that MMULT _“…returns the matrix product of two arrays. The result is an array with the same number of rows as array1 and the same number of columns as array2.”_

If that’s got you scratching your head, then try this alternate explanation: The **M** in **M**MULT stands for **_Magic_**.  😉

The way Sajan is using MMULT is to basically add across each row to find out what the total is for each row. Or another way of thinking about it is that because there’s ether a zero or a number in each row, he’s zipping up these two lists into one to just get the numbers and to ignore the zeros:  
\=MMULT({0,0;0,1;0,2;0,3;0,4;0,5;7,0;8,0;9,0;10,0;0,10;0,11;0,12;0,13;0,14;0,15;0,16;0,17;0,18;20,0;21,0;22,0;23,0},{1;1})

\= {0;1;2;3;4;5;7;8;9;10;10;11;12;13;14;15;16;17;18;20;21;22;23}

### 8\. Work out the most common number in that array and add one to it

Now he’s got the start position of our desired substring.

\=MODE({0;1;2;3;4;5;7;8;9;10;10;11;12;13;14;15;16;17;18;20;21;22;23})+1

\=11

### 9\. Lastly, he uses this trickery to tease out our answer string

\=MID(A16,MODE({0;1;2;3;4;5;7;8;9;10;10;11;12;13;14;15;16;17;18;20;21;22;23})+1,LEN(A16))

\=MID(A16,11,LEN(A16))

\=Australia1484

Austrailia1484. Crikey dick. Strewth, mate!

That bonza beaut has more bounce than a Boomer! Makes me feel a couple of tinnies short of a slab.

And that’s the formula that got the lowly Bronze! Tune in tomorrow, and we’ll see what the Silver-medal winner, **Haseeb,** has to offer. If you dare…..

About the Author.
-----------------

Jeff Weir – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure **#VALUE!**

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
| Written by Hui...  <br>Tags: [INDIRECT()](https://chandoo.org/wp/tag/indirect/)<br>, [isnumber](https://chandoo.org/wp/tag/isnumber/)<br>, [len()](https://chandoo.org/wp/tag/len/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [MMult()](https://chandoo.org/wp/tag/mmult/)<br>, [mode()](https://chandoo.org/wp/tag/mode/)<br>, [N()](https://chandoo.org/wp/tag/n/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 46 Responses to “Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 2.)”

1.  ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David Hager says:
    
    [July 17, 2013 at 9:46 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440121)
    
    How about? Am I too late to win 🙁
    
    \=MID(A1,MAX(IFERROR(FIND((ROW(1:10)-1)&CHAR(COLUMN(BM:CL)),UPPER(A1)),0))+1,255)
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440121)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 17, 2013 at 10:56 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440127)
        
        Also note that you don't need the UPPER, although you do need to change ROW(1:10) to absolute references in order to copy the formula down. And you could replace that hard-coded 255 with say 9^9 to handle any length of string (although we only need a number of no more than 32767 on the end, so 9^9 is slightly overkill, albeit with no ill effect).
        
        By my account that makes it 76 characters. Well done.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440127)
        
    *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
        
        [July 17, 2013 at 4:13 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440161)
        
        What if the next character after the first numbers is not between A-Z? Like Monaco7190@Australia1484
        
        Regards
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440161)
        
        *   ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David Hager says:
            
            [July 17, 2013 at 4:22 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440164)
            
            In retrospect, the formula can be further simplified by making the CHAR array more comprehensive (i.e.  
            CHAR(COLUMN(BF:DS))). Then, there would be no reason to convert A1 to UPPER(A1).
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440164)
            
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [July 17, 2013 at 7:36 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440182)
            
            Elias - that's another challenge entirely. In this one - based on some question I answered in a forum somewhere recently - the sample data always has the letter A-Z after a number.
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440182)
            
            *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
                
                [July 17, 2013 at 8:33 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440185)
                
                I think this one handles the scenario I’m talking about, and still short.
                
                \=MID(A4,MATCH(TRUE,(MID(A4,ROW(A:A),1)\*ISERR(-MID(A4,ROW(A:A)+1,1)))>0,)+1,9^9)
                
                Regards
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440185)
                
        *   ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David hager says:
            
            [July 17, 2013 at 10:03 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440195)
            
            \=MID(A1,MAX(IFERROR(FIND(CHAR(COLUMN(BF:DR))&(ROW(1:10)-1),A1),0))+1,255)
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440195)
            
            *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
                 says:
                
                [July 17, 2013 at 10:14 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440196)
                
                David...you've got to have the numbers first. Plus I changed 255 for 9^9 to handle strings longer than 255 characters:  
                \=MID(A1,MAX(IFERROR(FIND((ROW(1:10)-1)&CHAR(COLUMN(BF:DR)),A1),0))+1,9^9)
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440196)
                
            *   ![](https://secure.gravatar.com/avatar/165a6ecd6d73f369da17f0b925d050377d49f1507e936a2aaf6c8aa0d33843a4?s=64&d=mm&r=g) Rajesh says:
                
                [October 25, 2017 at 5:59 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-1518530)
                
                Hii @David,, I'm unable to understand,,
                
                Column(BF:DR),,
                
                Plz reply to me also @ [sinha14raj@gmail.com](mailto:sinha14raj@gmail.com)
                 ?
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-1518530)
                
                *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                     says:
                    
                    [October 26, 2017 at 1:39 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-1518582)
                    
                    @Rajesh  
                    CHAR(COLUMN(BF:DR))  
                    is the same as =CHAR(COLUMN(58:122))  
                    So it is just extracting an array of the Characters between Char 58 and 122  
                    ie: between characters : and z
                    
        *   ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David Hager says:
            
            [July 17, 2013 at 10:17 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440197)
            
            \=MID(A1,MAX(IFERROR(FIND((ROW(1:10)-1)&CHAR(COLUMN(BF:DR)),A1),0))+1,255)
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440197)
            
2.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [July 17, 2013 at 10:37 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440126)
    
    Ha...you spoiled my punch line, David. At the end of this series (a couple of posts of which are still to come) I was going to challenge readers to find a shorter solution than the respondents had so far posted, with a slightly longer version of yours in mind. Specifically =MID(A1,MIN(IFERROR(FIND(CHAR(COLUMN($AW:$BF))&CHAR(ROW($65:$90)),A1),""))+1,LEN(A1))
    
    Great skills. Be sure to check out the other challenges, and still check in to see the other innovative solutions that I'll be covering re this challenge.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440126)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 17, 2013 at 11:03 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440128)
        
        Whoops, the above comments are out of order. Also, with my slight revision it runs at 79 characters, not 76 as I said below. But that's still a winner!
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440128)
        
3.  ![](https://secure.gravatar.com/avatar/8d66fff8a8809045872e44f9c58af0cc8149a66c1b09fc2742eafc9b92c09727?s=64&d=mm&r=g) [ExcelStrategy](http://www.youtube.com/user/ExcelStrategy)
     says:
    
    [July 17, 2013 at 3:06 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440149)
    
    Man your formula is insane ! All those Matrix operations !!
    
    Here my very simple solution
    
    \={MID(B12;MATCH(TRUE;ISNUMBER(--MID(B12;ROW(INDIRECT("1:"&LEN(B12)));1));0)+4;100)}
    
    Regards.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440149)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 17, 2013 at 7:32 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440181)
        
        Hi ExcelStrategy. The formula challenge sets out that _your formula should handle any length of string, and any length of numbers – not just the lengths shown above/below_.
        
        Your formula is hard-coded to 4 digits, but as per the challenge we can't rely on the numbers always being four digits.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440181)
        
        *   ![](https://secure.gravatar.com/avatar/8d66fff8a8809045872e44f9c58af0cc8149a66c1b09fc2742eafc9b92c09727?s=64&d=mm&r=g) [ExcelStrategy](http://www.youtube.com/user/ExcelStrategy)
             says:
            
            [July 18, 2013 at 9:41 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440263)
            
            Now I understand why you have isolated the only sequence of FALSE;TRUE (0;1) in the initial array! it signals the change between the numbers and text in the two blocks of strings !
            
            I have based my formula on the data wich was inside the example workbook that has a pattern of 4 numbers every time 🙂
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440263)
            
            *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
                 says:
                
                [July 18, 2013 at 9:43 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440264)
                
                Yeah, i was a little lazy when whipping up the sample data. Cheers, ExcelStrategy.
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440264)
                
    *   ![](https://secure.gravatar.com/avatar/c205bccefb49c2cec3c8c92a76ccc97e3c3bac0ffdada902876961b1bb4b97bd?s=64&d=mm&r=g) Kevin says:
        
        [July 22, 2013 at 9:48 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440853)
        
        this does not work for me.Can you please advise?
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440853)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [July 22, 2013 at 9:59 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440856)
            
            Kevin - you've got to array enter that formula. So instead of just pushing ENTER you've got to push CTRL + SHIFT + ENTER.
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440856)
            
4.  ![](https://secure.gravatar.com/avatar/f254cc498658237b0a8497db218d506e3f38aed9dabe88a80818f503a61b99c8?s=64&d=mm&r=g) [simon](http://uk.linkedin.com/in/simonlavender)
     says:
    
    [July 17, 2013 at 5:31 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440173)
    
    Can't you use the CODE function to get ASCII number greater than 64 related to second sequential number greater than 64 via vlookup or nested if or search or find functions?
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440173)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 18, 2013 at 12:51 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440206)
        
        Simon: here's what CODE returns on the whole string:  
        \={77;111;110;97;99;111;55;49;57;48;65;117;115;116;114;97;108;105;97;49;52;56;52}  
        ...and here's the ones that are greater than 64:  
        \={TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE}  
        How does that help?
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440206)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [July 18, 2013 at 1:08 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440208)
            
            Sorry, I should elaborate further. You can use this:  
            \=CODE(MID(A1,ROW(A$1:INDEX(A:A,LEN(A1))),1))>64  
            …to return this:  
            \={TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE}
            
            And then we can search that array for the first FALSE with this:  
            \=MATCH(FALSE,CODE(MID(A1,ROW(A$1:INDEX(A:A,LEN(A1))),1))>64,0)  
            …but then we’d need to find where the next TRUE falls relative to the length of the original string, so that we could split that original string. And that requires quite a bit more manipulation, which really blows out the length of our formula.
            
            The next post discusses a formula that does something similar to your suggested approach. But there’s not a MATCH or VLOOKUP in sight. Stay tuned ?
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440208)
            
            *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
                 says:
                
                [July 18, 2013 at 1:09 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440210)
                
                Weird...I posted a smiley face at the end of Stay Tuned, but WordPress turned it into a question mark.
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440210)
                
5.  ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David Hager says:
    
    [July 18, 2013 at 1:15 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440211)
    
    Pair of parentheses not needed, final formula.
    
    \=MID(A1,MAX(IFERROR(FIND(ROW(1:10)-1&CHAR(COLUMN(BF:DR)),A1),0))+1,9^9)
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440211)
    
    *   ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) [Sajan](http://chandoo.org/wp/category/posts-by-sajan/)
         says:
        
        [July 18, 2013 at 1:36 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440214)
        
        David,  
        Very clever technique! I love its simplicity! Sheer genius!
        
        By the way, I recently discovered your old EEE posts. Amazing stuff! I hope you resurrect those posts since there are very few posts out there of such quality!
        
        Regards,  
        Sajan.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440214)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [July 18, 2013 at 1:43 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440219)
            
            Sajan...don't tease me...what's the link.
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440219)
            
            *   ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) [Sajan](http://chandoo.org/wp/category/posts-by-sajan/)
                 says:
                
                [July 18, 2013 at 2:05 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440221)
                
                Hi Jeff,  
                You can find the old EEE posts at:  
                [http://www.j-walk.com/ss/excel/eee/](http://www.j-walk.com/ss/excel/eee/)
                
                Regards,  
                Sajan.
                
                [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440221)
                
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 18, 2013 at 1:42 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440217)
        
        Still need those $ in the Row, though.  
        \=MID(A1,MAX(IFERROR(FIND(ROW($1:$10)-1&CHAR(COLUMN(BF:DR)),A1),0))+1,9^9)  
        Otherwise you have to array-enter your formula individually for each item in our data list.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440217)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [July 18, 2013 at 2:54 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440227)
            
            David, you can shave another character off like this:  
            \=MID(A1,MAX(IFERROR(FIND(COLUMN(A:J)-1&CHAR(ROW($65:$90)),A1),0))+1,9^9)
            
            THis works, because (A:J) is shorter than (1:10)
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440227)
            
6.  ![](https://secure.gravatar.com/avatar/cccfe9f54c4f0adf5321020bff45fb7b971ee5303f6a5d0ff04652bcda85e41c?s=64&d=mm&r=g) Nikki says:
    
    [July 18, 2013 at 7:29 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440249)
    
    Way too complicated for this little brain but love how your mind works, Chandoo - the wit!! 🙂
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440249)
    
7.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [July 18, 2013 at 8:37 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440253)
    
    @David - Brilliant...Sheer Genius....  
    @Jeff Reminds me of the gem to search a exact word in a string from the academy from you and Craig.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440253)
    
8.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [July 18, 2013 at 8:54 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440256)
    
    @Sam...yeah, I remember you were _standing and clapping_ A phase that I've now trademarked, so use it and I'll sue your ass 😉
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440256)
    
9.  ![](https://secure.gravatar.com/avatar/2911ac319625b7c32be416fb9d3da71b2126e5215ac3762a38a71c2998e90ee8?s=64&d=mm&r=g) Valli! says:
    
    [July 18, 2013 at 11:57 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440282)
    
    Am new to the Site. Spending hours together to understand the work - breaking my head.
    
    Could somebody help me to understand why we use "-" in formula (before 2nd MID formula and "-{0,1}) and what {1;1} does.
    
    MID(A6,MODE(MMULT((N(ISNUMBER(-MID(A6,ROW(INDIRECT("1:"&LEN(A6))),1)))={1,0})\*(ROW(INDIRECT("1:"&LEN(A6)))-{0,1}),{1;1}))+1,LEN(A6))
    
    Thanks!  
    Valli
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440282)
    
10.  ![](https://secure.gravatar.com/avatar/a4b2f07b9fd4e56ff4b5bef3158f7acefb90822374e9d320c40c7675201e0be4?s=64&d=mm&r=g) Chris Rowley says:
    
    [July 18, 2013 at 6:59 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440325)
    
    Hi All,
    
    Just came across this.........Thought I'd have a crack at it before reading anyone else's responses, just to see what method my brain would come up with!
    
    This entered as an array formula (Ctrl + Shift +Enter) would do the trick, changing A1 for whatever cell needed
    
    \=RIGHT(A1,LEN(A1)-MIN(IFERROR(SEARCH({"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"},A1,MIN(IFERROR((SEARCH({1,2,3,4,5,6,7,8,9},A1,1)),"")))-1,"")))
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440325)
    
11.  ![](https://secure.gravatar.com/avatar/0c71373bc01a0a1dc58d2ac7d3f84a0006fa472544e1c2ea12749672db247c6e?s=64&d=mm&r=g) ianamck says:
    
    [July 19, 2013 at 12:15 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440353)
    
    @Jeff
    
    Woah psychotic is most probably an understatement. Let me say this english is my first language and I have read and understood your brilliant explanation. I have even taken the time to test bits of your explanation of see what some of the functions are doing.
    
    What still befuddles me is how a number of you even start to approach this type of problem right from the beginning. Which functions to use and in what order to get to the solutions you are all showing.
    
    I used to just write very simple formulas that did one or two things and with this site I have come on leaps and bounds by studying the answers and explanations from lots of contributors. A few names always rise to the top (that includes your forum posts Jeff and those of the Forum Ninjas) I just want to get to the point where I can begin to approach a problem like this by understanding which of those functions I should use and how to nest them. Rather than just copying an answer and moving on. I know that will take time, practice and lots more learning and I am sure it will slowly come. Keep up the great explanations and remember us less gifted lovers of excel.
    
    Bring on episode three Jeff....................... I can take it 😉
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440353)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 19, 2013 at 12:37 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440354)
        
        Thanks for your kind words. You raise a good point...how to even start formulating approaches such as this. I'll probably write something up in due course along those lines. I can certainly say that there's no way I'd ever have put together the approaches that some of the other respondents put together. That's the beauty of a challenge like this...you get to see many expert cat-skinners in action.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440354)
        
        *   ![](https://secure.gravatar.com/avatar/0c71373bc01a0a1dc58d2ac7d3f84a0006fa472544e1c2ea12749672db247c6e?s=64&d=mm&r=g) ianamck says:
            
            [July 19, 2013 at 12:42 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440355)
            
            Jeff a great idea
            
            ".....you raise a good point…how to even start formulating approaches such as this. I’ll probably write something up in due course along those lines........."
            
            Looking forward to that. Book me a front row seat.
            
            Maybe a series of posts from your good self and some of the Ninjas to start with????????????????
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440355)
            
12.  [Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 3.) | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2013/07/19/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/)
     says:
    
    [July 19, 2013 at 7:01 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440401)
    
    \[...\] Sajan: Formula Challenge 001 – Part 2 \[...\]
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440401)
    
13.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [July 19, 2013 at 3:41 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440490)
    
    I already posted this but look like it was unseen. This one can handle any character after the numbers and not only letters A-Z.
    
    \=MID(A4,MATCH(TRUE,(MID(A4,ROW(A:A),1)\*ISERR(-MID(A4,ROW(A:A)+1,1)))>0,)+1,9^9)
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440490)
    
14.  ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
    
    [July 19, 2013 at 5:11 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440498)
    
    I can reduce it to 76 characters length. It also does not get mess if users insert/delete a row/column.
    
    \=MID(A4,MATCH(TRUE,MID(A4,ROW(A:A),1)\*ISERR(-MID(A4,ROW(A:A)+1,1))>0,)+1,9^9)
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440498)
    
15.  ![](https://secure.gravatar.com/avatar/f6fb631cb5af8ef896c056c59eee762e3c8aebb9b7f99c46044a735449aaa449?s=64&d=mm&r=g) Jeanbar says:
    
    [July 22, 2013 at 11:08 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440796)
    
    Hi,
    
    My 2 cents (76 chars), Excel 2003:  
    \=MID(A2;MATCH(2;MMULT(N(ISERR(-MID(A2;ROW($1:$99)+{0\\1};1)));{1;2});0)+1;99)
    
    (French conventions:  
    formula separator ";"  
    {0\\1}=column vector 0,1  
    {1;2}=row vector 1,2)
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440796)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 22, 2013 at 6:58 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440840)
        
        Great stuff. Sajan also came up with this one, which I've written up at [http://chandoo.org/wp/2013/07/22/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/](http://chandoo.org/wp/2013/07/22/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/)
        
        His version has some added stuff to ensure any length of string is covered.  
        \=MID(A1,MATCH(1,MMULT(-ISERR(-MID(A1,ROW(OFFSET(A$1,,,LEN(A1))),{1,2})),{1;-1}),)+1,6^6)
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440840)
        
16.  ![](https://secure.gravatar.com/avatar/f6fb631cb5af8ef896c056c59eee762e3c8aebb9b7f99c46044a735449aaa449?s=64&d=mm&r=g) Jeanbar says:
    
    [July 22, 2013 at 1:12 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440801)
    
    It is strange to see how complex data manipulation is with Excel when it is so simple with Word:
    
    1°) Copy the herebelow lines in Word:
    
    Monaco7190Australia1484  
    Denver11222Chicago4257  
    Beijin42Sofia666877  
    London11998Paris75006
    
    2°) FIND & REPLACE  
    Find what : (\*\[0-9\]{1;10})(\*)(^13)  
    Options : Use wildcards  
    Replace with : \\2\\3  
    (REPLACE ALL)
    
    3°) That's it!
    
    I wish Excel have these wildcard capabilities!
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440801)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 22, 2013 at 6:55 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440839)
        
        I agree. What you can do with Word's Find and Replace is very cool.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-440839)
        
17.  ![](https://secure.gravatar.com/avatar/57cd9b94a67870e52a69e148df05ff13bf11887101196bd50aa605969d08f2cd?s=64&d=mm&r=g) Sam says:
    
    [August 16, 2013 at 6:52 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-443422)
    
    \=MID(A1,MODE(MMULT((N(ISNUMBER(-MID(A1,ROW(INDIRECT(“1:”&LEN(A1))),1)))={1,0})\*(ROW(INDIRECT(“1:”&LEN(A1)))-{0,1}),{1;1}))+1,LEN(A1))
    
    I can't get this to work on A1= Monaco7190Australia1484
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-443422)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 17, 2013 at 5:49 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-443450)
        
        @Sam
        
        It works fine for me?
        
        You have to retype the " characters, as the characters above look like " but aren't
        
        It doesn't need Array Entering, just a simple Enter will suffice
        
        Have a look at my file here: [https://www.dropbox.com/s/rtpbpvlyvynvlwl/For%20Sam.xlsx](https://www.dropbox.com/s/rtpbpvlyvynvlwl/For%20Sam.xlsx)
        
        If that doesn't help what version of excel are you using ?
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#comment-443450)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 1.)](https://chandoo.org/wp/formula-challenge-001-1/) | [Are you interested in learning Power Pivot?](https://chandoo.org/wp/are-you-interested-in-learning-power-pivot/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
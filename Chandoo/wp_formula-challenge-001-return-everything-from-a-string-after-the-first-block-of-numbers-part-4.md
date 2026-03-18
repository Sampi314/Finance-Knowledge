# Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 4.)  » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4

---

Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 4.)
==================================================================================================

[Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
 , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
 - 20 comments

  

[![FC001-4Head](https://chandoo.org/wp/wp-content/uploads/2013/07/FC001-4Head.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/FC001-4Head.png)
Welcome back to another gripping episode of “When good formulas go _GREAT_”.  Just like the immortal combatants in the classic 1986 movie _Highlander_, over the last three posts in this series our Excel nerds have been locked in an ages-old battle to decapitate. A text-string, that is. Not each other.

So far we have seen some formidable formulas from these fearsome foes:

Jeff: [Formula Challenge 001 – Part 1](http://chandoo.org/wp/2013/07/16/formula-challenge-001-1/ "Formula Challenge 001 - Part 1")

Sajan: [Formula Challenge 001 – Part 2](http://chandoo.org/wp/2013/07/17/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-2/ "Formula Challenge 001 - Part 2")

Haseeb: [Formula Challenge 001 – Part 3](http://chandoo.org/wp/2013/07/19/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/ "Formula Challenge 001 - Part 3")

But while we’ve witnessed a few intriguing battles, none of our defeated warriors ultimately had what it took to win _the prize_. So steel your nerves, grab a seat near the edge of the arena, and find out what brute force another contender can bring to bear on the problem in…

…Part 4: The Sorcerer Samurai
-----------------------------

By way of a quick refresher, our formula challenge calls for a mighty Excel hero to slay a fearsome dragon – err, t_ext string_ – and return triumphantly back to Court with its tail – err, _substring_ – in time for the cook (that would be me) to serve it up to the King (that would be Chandoo) at the Feast of St. Christopher.

Those dragons and associated tails look a little something like this:

|     |     |
| --- | --- | 
| **Dragon:** | **Tail:** |
| NewZealand99**Australia41** | Australia41 |
| France12**NewZealand41** | NewZealand41 |
| Australia23**France17** | France17 |
| England53**France37** | France37 |
| England7**NewZealand27** | NewZealand27 |
| Australia16**England24** | England24 |
| SouthAfrica21**France11** | France11 |
| SouthAfrica42**Australia33** | Australia33 |
| NewZealand48**SouthAfrica34** | SouthAfrica34 |
| England12**SouthAfrica22** | SouthAfrica22 |

(Bonus Question: Who can tell me what these numbers represent?)

You can download the challenge and full dataset here: [Formula Challenge 1.4](https://chandoo.org/wp/wp-content/uploads/2013/07/Formula-Challenge-1.4.xlsx)

So our brave Knights must wield their mighty sword – **Excel**ibur – and lop off the bit in bold at the end. The winner of the challenge is the combatant who can do that slicing with as short a sword – err, _formula –_ as possible.

That winner receives his or her weight in gold. Fool’s gold.  And as a wise Highlander one said about the winner of battles involving mass decapitations: **_“There can be only one”_**.

But this will be harder than it looks. Those numbers are of variable length (and getting longer each year), and the fact that we are searching for a block of text and numbers that occurs after _another_ block of text and numbers makes it very tricky indeed. Mwah ha ha.

Well, the next contender for _the prize_ is….SAJAN! Again!!

You might remember Sajan the Magician’s vaguely coherent incantation of a formula from a few posts ago:

\=MID(A1,MODE(MMULT((N(ISNUMBER(-MID(A1,ROW(INDIRECT(“1:”&LEN(A1))),1)))={1,0})\*(ROW(INDIRECT(“1:”&LEN(A1)))-{0,1}),{1;1}))+1,LEN(A1))

Discontent with the mere Bronze that his wizardry brought him, Sajan’s kicked over his magic cauldron, drawn his trusty pen-knife of a formula from its dusty scabbard, and stabbed our string right through the heart. Dead. With this:

\=MID(A1,MATCH(1,MMULT(-ISERR(-MID(A1,ROW(OFFSET(A$1,,,LEN(A1))),{1,2})),{1;-1}),)+1,6^6)

[![Jeff](https://chandoo.org/wp/wp-content/uploads/2013/07/Jeff.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/Jeff.png)
Wow! From 133 characters down to 88! I can still hear the chants of “_Long Live Sajan the Samurai”_ ringing in my ears from when he dragged that severed substring into the Chandoo.org forum and dumped it victoriously at the formula challenge thread’s  feet . Err, footer.

But you weren’t there to see it, were you? So let’s have our Court Jester (me) don his silly face, and re-enact the fight blow by blow, so to speak. _**En Garde!**_

### 1\. Samurai Sajan sneaks up on the string and slices it into slender slivers:

He carves the string into one-character off-cuts, and casts them into a couple of columns with his crescent-shaped cutlass:

\=MID(A1,ROW(OFFSET(A$1,,,LEN(A1))),{1,2})

{ “N”, “Ne”; “e”, “ew”; “w”, “wZ”; “Z”, “Ze”; “e”, “ea”; “a”, “al”; “l”, “la”; “a”, “an”; “n”, “nd”; “d”, “d9”; “9”, “99”; “9”, “9A”; “A”, “Au”; “u”, “us”; “s”, “st”; “t”, “tr”; “r”, “ra”; “a”, “al”; “l”, “li”; “i”, “ia”; “a”, “a4”; “4”, “41”; “1”, “1”}

So he’s taken the original **1D** string,and split it apart into a **2D** (i.e. two column) array with the help of the {1,2} bit. Both columns of the new array are almost the same, except all the elements in one of them is _one_ character long, and all the elements in the other are _two_ characters long.

If entered over a range, here’s what that looks like:  
[![Part 4 Array 1](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-1.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-1.png)

### 3\. He displays any of dem digits dat _looks_ like a digit _as_ a digit, using a dash:

Currently Excel thinks that this array is just text – even the numbers in it. Putting a minus sign in the front of the array – or in fact doing _any_ kind of mathematical operation on it – will force any numbers to wake up and _act_ like numbers. (Unfortunately, it also freaks any actual _text_ out…to the point that any bits of text whinges _“I’m not a number, there’s been some kind of error”_. Hence the #VALUE! errors below, along with the numbers.)  
\= -{ “N”, “Ne”; “e”, “ew”; “w”, “wZ”; “Z”, “Ze”; “e”, “ea”; “a”, “al”; “l”, “la”; “a”, “an”; “n”, “nd”; “d”, “d9”; “9”, “99”; “9”, “9A”; “A”, “Au”; “u”, “us”; “s”, “st”; “t”, “tr”; “r”, “ra”; “a”, “al”; “l”, “li”; “i”, “ia”; “a”, “a4”; “4”, “41”; “1”, “1”}

\={ #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; -9, -99; -9, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; -4, -41; -1, -1}

Again, here’s how that looks if entered over an Excel range (with our original string split apart down the side by way of reference):  
[![Part 4 Array 2](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-2.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-2.png)

### 4\. He hacked away at the resulting horrible herrors (err.._errors_) that happened due to this harsh handling:

He turns any of those errors to TRUE and anything else to FALSE with this:  
\=ISERR({ #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; -9, -99; -9, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; #VALUE!, #VALUE!; -4, -41; -1, -1}

\={ TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; FALSE, FALSE; FALSE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; FALSE, FALSE; FALSE, FALSE}

So now we have TRUE where there was text, and FALSE where there was numbers. Which looks like this:  
[![Part 4 Array 3](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-3.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-3.png)

### 5\. He butchered those Boolean values into bite-sized bits, by binding a brutal minus sign on at the beginning:

Just as putting a minus sign in the front in formula 3 above forced any numbers stored as text to _act_ like numbers, putting a minus sign in front of an array of TRUE and FALSE values (otherwise known as _Boolean_ values) or doing any other kind of mathematical operation on the array will turn those TRUE and FALSE values to numerical values – in this case because it is a **minus** sign they will turn to -1 and zero. _Abracadabra._  
\=-{ TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; FALSE, FALSE; FALSE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; TRUE, TRUE; FALSE, FALSE; FALSE, FALSE}

\={-1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; 0, 0; 0, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1 ,-1; -1, -1; -1, -1; -1, -1; 0, 0; 0, 0}

…which looks like this:  
[![Part 4 Array 4](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-4.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-4.png)

Note something interesting…the highlighted row above falls just before the string that we’re after. And it’s the _only_ row in the entire array that has a zero in the first column **and** a negative one in the second column. So if we can work out where that combination of zero and negative one falls, we know exactly where our desired substring starts.

### 6\. He magically multiplies the _first_ array column by one, and the _second_ array column by _minus_ one, then maniacally mashes them together en masse:

He does this by using the MMULT function with a 2nd argument of {1;-1}.  
\=MMULT(={-1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; 0, 0; 0, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1, -1; -1 ,-1; -1, -1; -1, -1; -1, -1; 0, 0; 0, 0},{1;-1})

\={0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0}

…which looks like this:  
[![Part 4 Array 5](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-5.png)](https://chandoo.org/wp/wp-content/uploads/2013/07/Part-4-Array-5.png)

MMULT is really hard to explain. It’s kind of like an 2-dimensional SUMPRODUCT. (Maybe it’s _exactly_ like a 2-dimensional SUMPRODUCT).  There’s a great visual explanation at Mike Girvin’s ExcelIsFun YouTube channel at [http://www.youtube.com/watch?v=qJnL5hFfcYo](http://www.youtube.com/watch?v=qJnL5hFfcYo)

Given our array in this instance has _two_ columns and our second argument of MMULT is {1;-1}, MMULT in this case effectively multiplies each number in the first column by _positive_ one, multiplies each number in that 2nd column by  _negative_ one –  and then adds the result together.  Multiplying the first array by positive one does nothing to it. Multiplying the second array by negative one changes any existing _negative_ values to _positive_. Adding the result together gets us back to a 1D array.

Now, as per the highlighted row above, the number that falls just before the string that we’re after is the _only_ line that has 1 in it. So while Sajan might have ditched sorcery for sword-play, there’s still yet an element of the dark arts in his repertoire.

### 7\. He secures his sharp scalpel for some exploratory surgery on our string:

Specifically, he uses the MATCH function to see what position that ‘1’ occurs at, and then adds 1.  
\=MATCH(1,{0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0},)+1

\=13

**Quick aside:** I never knew until another competitor in the challenge – Elias – posted a formula in the actual formula challenge thread that if the third argument of MATCH is a comma followed by nothing else, Excel interprets this the same as if that third argument was FALSE or Zero – that is, Excel is looking for an _exact_ match, not an _approximate_ one. So that’s a handy way to shorten a formula if you’re answering a challenge (although I’d actively put the FALSE in in a real-world situation).

So with a blank comma as the 3rd argument, all these are equivalent:  
\=MATCH(3,{1,2,4,5},)  
\=MATCH(3,{1,2,4,5},FALSE)  
\=MATCH(3,{1,2,4,5},0)  
\= #N/A

And without the comma, these are equivalent:  
\=MATCH(3,{1,2,4,5})  
\= MATCH(3,{1,2,4,5},TRUE)  
\= MATCH(3,{1,2,4,5},1)  
\= 2

Okay, back to the fight!

### 8\. He culminates all this cutting with a callous **_coup de grâce_** to the condemned creature:

\=MID(A1,13,6^6)

\=Australia41

That 6^6 bit is just a short way to write a long number. We need a number in that argument that’s long enough so that all possible substring lengths are covered. Sajan could use LEN(A1), but that would take 7 characters, whereas 6^6 is only three characters. The maximum amount of characters that Excel 2007 or later will let you put in a string is 32,767 so given that 6^6 = 46,656 this will be more than enough.

Huzzah! How’s that for swordsmanship, eh? Hardly a fair fight…our poor string never really stood a chance against our mighty Samurai.

Well, that wraps up the joust for today. But stay tuned…there’s two super-short excellent approaches that have been proposed since this series of posts began, that definitely have to be seen to be believed. I’ll cover them off in a future post.

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
| Written by Jeff Weir  <br>Tags: [ISERR()](https://chandoo.org/wp/tag/iserr/)<br>, [MATCH()](https://chandoo.org/wp/tag/match/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [MMult()](https://chandoo.org/wp/tag/mmult/)<br>, [OFFSET()](https://chandoo.org/wp/tag/offset/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 20 Responses to “Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 4.)”

1.  ![](https://secure.gravatar.com/avatar/0575c24503f5a5efd20ec37b052153619dcc24b875902c087beceaf478d97340?s=64&d=mm&r=g) [Christos Samaras](http://www.myengineeringworld.net/)
     says:
    
    [July 22, 2013 at 7:29 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440774)
    
    Assuming that Monaco7190Australia1484 is in A2, then in B2 we can write:
    
    \=MID(A2,MIN(IFERROR(SEARCH(CHAR(ROW($65:$90)),A2,MIN(IFERROR(FIND(CHAR(ROW($48:$57)),A2),””))+1),””)),LEN(A2))
    
    Of course it’s an array formula, so CTRL + SHIFT + ENTER is required…
    
    CHAR(48) to CHAR(57) returns the numbers 0 to 9.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440774)
    
2.  ![](https://secure.gravatar.com/avatar/1080332eaf44a559094c919c8c2bd28302ed30ac084671cbf5c12389941aa92c?s=64&d=mm&r=g) [ethoros](http://www.ethoros.blogspot.co.uk/)
     says:
    
    [July 22, 2013 at 8:08 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440778)
    
    Pure genius!  
    Well done Sajan, that is an amazing formula. Very impressed. 🙂
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440778)
    
3.  ![](https://secure.gravatar.com/avatar/50d08f5ff755effd757e5518c0f35d496555304cc2f61b64c4963b0aade7c96a?s=64&d=mm&r=g) Ian says:
    
    [July 22, 2013 at 8:27 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440782)
    
    I can't compete on the formula side of things, but are the strings at the top the number of times each side has won in matches between the 2 in rugby (union)?
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440782)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 22, 2013 at 8:56 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440785)
        
        You got it, Ian. And guess what country I'm in!
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440785)
        
4.  ![](https://secure.gravatar.com/avatar/1080332eaf44a559094c919c8c2bd28302ed30ac084671cbf5c12389941aa92c?s=64&d=mm&r=g) [ethoros](http://www.ethoros.blogspot.co.uk/)
     says:
    
    [July 22, 2013 at 9:09 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440786)
    
    Yay, one thing I can improve on is instead of 6^6 used 8^5  
    🙂
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440786)
    
5.  ![](https://secure.gravatar.com/avatar/0c71373bc01a0a1dc58d2ac7d3f84a0006fa472544e1c2ea12749672db247c6e?s=64&d=mm&r=g) ianamck says:
    
    [July 22, 2013 at 2:10 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440806)
    
    Bonus Question: Who can tell me what these numbers represent
    
    Rugby Union wins between competing countries
    
    EG New Zealand V Australia
    
    of the 140 matches New Zealand have won 99
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440806)
    
6.  ![](https://secure.gravatar.com/avatar/adc8cd46077158d9467fa8c33372c276925a01aaaac87980bd3bbbb9254d1cc7?s=64&d=mm&r=g) Dave S says:
    
    [July 22, 2013 at 4:33 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440823)
    
    Truly awesome! There is beauty in the elegance of these solutions.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440823)
    
7.  ![](https://secure.gravatar.com/avatar/92909560e4b88930acf04bfed1596f4f0d6ce2d5919f100630403ed70ed7d787?s=64&d=mm&r=g) [Jared](http://n/a)
     says:
    
    [July 22, 2013 at 4:42 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440825)
    
    Great posts on this challenge!
    
    Was space-delimited data a requirement? Adding a space to any string results in each of these solutions failing.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440825)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [July 22, 2013 at 6:53 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440837)
        
        No, it wasn't a requirement.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440837)
        
        *   ![](https://secure.gravatar.com/avatar/92909560e4b88930acf04bfed1596f4f0d6ce2d5919f100630403ed70ed7d787?s=64&d=mm&r=g) [Jared](http://n/a)
             says:
            
            [July 22, 2013 at 7:03 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440842)
            
            So how about a solution that handles strings with spaces? 🙂
            
            Although I am having hard enough time figuring out what the heck is going on with the existing solutions ...
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-440842)
            
8.  ![](https://secure.gravatar.com/avatar/486cc6bbc69dcacdfc0dd8e8d51413c8ee9185d9979842702f0137bb52111c6a?s=64&d=mm&r=g) Sulabh says:
    
    [July 31, 2013 at 6:23 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-441767)
    
    Just use VBA. Make life easier.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-441767)
    
9.  ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David Hager says:
    
    [August 9, 2013 at 10:23 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-442679)
    
    " I’ll cover them off in a future post."  
    How far in the future? 🙂
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-442679)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [August 9, 2013 at 10:59 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-442685)
        
        I'm having problems getting the DeLorian up to 88 mph, David 😉
        
        Just a question of time.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-442685)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [jeffreyweir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [August 9, 2013 at 11:11 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-442687)
            
            Forgot to say that that was a neat post at DDOE, David. Be sure to check out the challenge at [http://chandoo.org/forums/topic/formula-challenge-016-unique-items-in-a-delimited-string](http://chandoo.org/forums/topic/formula-challenge-016-unique-items-in-a-delimited-string)
             that I posted as a result...already some innovative approaches there.
            
            [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-442687)
            
10.  ![](https://secure.gravatar.com/avatar/2311edda0d6727565ee08a9a53d4e2f47e11c969b4c8a671f875b6211fda731f?s=64&d=mm&r=g) Chetan says:
    
    [August 14, 2013 at 8:11 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-443191)
    
    I have another approach "{=RIGHT(B3,LEN(B3)-MATCH("TRUETRUE",(IF(CODE(MID(B3,ROW(INDIRECT("1:"&LEN(B3))),1))64,TRUE,FALSE))),0))} "
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-443191)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [August 14, 2013 at 9:01 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-443197)
        
        Chetan, can you try reposting that.
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-443197)
        
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 14, 2013 at 1:39 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-443223)
        
        @Chetan
        
        WordPress doesn't like the use of > GT or < LT characters as they are assumed to be used for marking special code blocks
        
        Try using GT, LT, GTE, LTE etc and re-post the formula
        
        [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-443223)
        
11.  ![](https://secure.gravatar.com/avatar/e396b8922686d537e2b2452ff2a343b0fd32e877735909b52ce7c9dfacc90a1e?s=64&d=mm&r=g) Udit says:
    
    [January 17, 2014 at 3:49 pm](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-465806)
    
    Came back to this site after a long time.... can this be a shorter answer? just modified Sajan's.... {=MID(A1,MATCH(1,--(ISNUMBER(-MID(A1,ROW(OFFSET(A1,,,LEN(A1))),2))),)+2,6^6)}
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-465806)
    
12.  ![](https://secure.gravatar.com/avatar/972063af2c400657af575dc6e418c36692501c4a5571d5792243693be244e5bb?s=64&d=mm&r=g) Stephane says:
    
    [October 8, 2015 at 10:51 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-1058115)
    
    Hello all of you and thanks for this awesommmmme formulas,
    
    Just for the sake of beauty, here is a UDF with Regular Expressions (7 lines of codes) :
    
    Function test (rng As Range) As string
    
    Const strPattern As String = "\[A-Z\]+\\d+"  
    Dim Obj As Object  
    Dim temp As Variant  
    Dim result As String
    
    Set Obj = CreateObject("vbscript.regexp")
    
    With Obj  
    .Pattern = strPattern  
    .Global = True  
    .ignorecase = True  
    Set temp = .Execute(rng.Value)  
    End  
    result = temp.Item(1).Value  
    essai =
    
    End Function
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-1058115)
    
13.  ![](https://secure.gravatar.com/avatar/137dcf2c7d945494cf5957358b40b3282965c898aaa5090608dd5a0b3b3d992a?s=64&d=mm&r=g) Ray says:
    
    [March 23, 2016 at 10:17 am](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-1153054)
    
    Thanks for opening this challenge and the awesome formula.
    
    Can someone explain or give me some hints on the ROW(OFFSET(A$1,,,LEN(A19))) ?
    
    I have no idea how it instructs the string extraction in the form of consecutive 1~2 characters.
    
    Thanks very much, this challenge really opened my eyes.
    
    [Reply](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#comment-1153054)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-4/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Formula Challenge 001 – Return everything from a string after the first block of numbers (Part 3.)](https://chandoo.org/wp/formula-challenge-001-return-everything-from-a-string-after-the-first-block-of-numbers-part-3/) | [Details about upcoming Power Pivot course (and a bonus tip on dashboards)](https://chandoo.org/wp/advanced-power-pivot-course-details/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
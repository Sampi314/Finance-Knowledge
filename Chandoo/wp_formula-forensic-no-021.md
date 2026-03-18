# How do I find the 4th Slash in a text string?

**Source:** https://chandoo.org/wp/formula-forensic-no-021

---

Formula Forensic No. 021 – Find the 4th Slash !
===============================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 42 comments

  

Last week at the [Chandoo.org Forums](http://chandoo.org/forums/topic/what-is-the-simple-way-to-find-slash-in-given-example "Find Slash")
, **Senthilkumar\_rm** posed the question:

“I Have file name as

**D:\\Data\\Personal\\sramasam\\desktop\\Exceldata.xls**

I want to find the position of the 4th slash “\\”

What is a simple way ? ”

I proposed 3 answers being:

\=FIND("\\",A1,FIND("\\",A1,FIND("\\",A1,FIND("\\",A1)+1)+1)+1)

\=SEARCH("\\",A1,FIND("\\",A1,FIND("\\",A1,FIND("\\",A1)+1)+1)+1)

`=FIND(CHAR(135),SUBSTITUTE(G5,"\",CHAR(135),4))`

`and **Faseeh** proposed a 4th answer:`

`=(LARGE(((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")*ROW(INDIRECT("1:"&1024)),2))`

So today at Formula Forensics we will examine all these and see what and why they all work.

As usual at Formula Forensics you can follow along by downloading a [Sample File](https://chandoo.org/wp/wp-content/uploads/2012/05/Slash.xls "FF21")
.

Using the Find() function
-------------------------

The Initial formula I proposed was:

\=FIND("\\",A1,FIND("\\",A1,FIND("\\",A1,FIND("\\",A1)+1)+1)+1)

This uses the Excel Find() function repeatedly inside itself

The Excel Find() function uses the following syntax

[![](https://chandoo.org/wp/wp-content/uploads/2012/05/FS01.png "FS01")](https://chandoo.org/wp/wp-content/uploads/2012/05/FS01.png)

The second solution I proposed was the same as the Find solution except that it used the Excel Search( ) function.

[![](https://chandoo.org/wp/wp-content/uploads/2012/05/FS02.png "FS02")](https://chandoo.org/wp/wp-content/uploads/2012/05/FS02.png)

You can see above that Find and Search have exactly the same syntax.

**Why have 2 functions that are effectively similar ?**

**Search** is Case Insensitive.

eg: Chandoo = cHanDoo

**Find** is Case Sensitive.

eg: Chandoo <> cHanDoo

We will discuss the solution using:

\=FIND("\\",A1,FIND("\\",A1,FIND("\\",A1,FIND("\\",A1)+1)+1)+1)

But the solution and description are equally applicable to the search based solution:

\=SEARCH("\\",A1,FIND("\\",A1,FIND("\\",A1,FIND("\\",A1)+1)+1)+1)

So Find has the syntax: **\=Find( Text, Within Text, \[Start No.\])**

But our formula has 4 Find() functions, where do we start?

### Start in the Middle.

In our example: \=FIND(“\\”,A1,FIND(“\\”,A1,FIND(“\\”,A1,FIND(“\\”,A1)+1)+1)+1)

FIND("\\",A1)

**Text**:                      “\\”

**Within Text**:      A1

**Start No**:              Optional = 0

This will find the first \\ in out text string and return the value **3**.

Checkout Cell **D13**.

Stepping out one find \=FIND(“\\”,A1,FIND(“\\”,A1,FIND(“\\”,A1,3+1)+1)+1)

FIND("\\",A1,3+1)

**Text**:                      “\\”

**Within Text**:      A1

**Start No**:              3 + 1

This will find the Second \\ in out text string by starting at position 3 + 1 and hence return the value 8.

Checkout Cell **D15**.

Stepping out one more find \=FIND(“\\”,A1,FIND(“\\”,A1,8+1)+1)

FIND("\\",A1,8+1)

**Text**:                      “\\”

**Within Text**:      A1

**Start No**:              8 + 1

This will find the Third \\ in out text string by starting at position 8 + 1 and hence return the value 17.

Checkout Cell **D17**.

Finally we arrive at the outer Find, \=FIND(“\\”,A1,17+1)

\=FIND("\\",A1,17+1)

**Text**:                      “\\”

**Within Text**:      A1

**Start No**:              17 + 1

This will find the fourth \\ in out text string by starting at position 17 + 1 and hence return the answer of 26.

Checkout Cell **D19**.

### Advantages:

Relatively simple formula

### Disadvantage:

This formula must be manually re-made if you want to find either the 3rd, 5th or another occurrences.

Using the Find() & Substitute() functions
-----------------------------------------

`=FIND(CHAR(135),SUBSTITUTE(A1,"\",CHAR(135),4))`

Using the **Find()** & **Substitute()** formula shown above take a different approach to solving the problem to the pure **Find()** based solution.

This solution works by using a feature of the substitute function that allows for the substitution of the Nth chosen character with another character.

The Excel **Substitute()** function has the following syntax :

[![](https://chandoo.org/wp/wp-content/uploads/2012/05/FS04.png "FS04")](https://chandoo.org/wp/wp-content/uploads/2012/05/FS04.png)

In our example:

`=FIND(``CHAR(135)``,SUBSTITUTE(``A1``,``"\"``,``CHAR(135)``,``4``))`

**Text**`:             A1`

**Old\_Text**`:    "\"`

**New\_Text**`:   Char(135)`

**Instance\_Num**`:`     

So substitute will replace the 4th Slash with the character Ascii code 135. Char 135 or a **‡** character was chosen as it is unlikely to be used in normal text. If it is used another character code should be chosen.

The Find Function will then look for Char(135) in the Substituted text and return the position number of it.

Replacing the Char(135) with a Char(5) characters reduces this formula to 44 characters!

**Advantages:**

This is a very clear formula to understand

You can easily look for the 3rd or 5th character without changing the formula

**Disadvantage:**

If the Text String already contains the Char(135) character then another must be chosen or the formula will be wrong.

Using Faseeh’s Array Formula.
-----------------------------

`={(LARGE(((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")*ROW(INDIRECT("1:"&1024)),2))}`

`Faseeh’s Formula is based around the` **Large()** `function`

`=(LARGE(((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")*ROW(INDIRECT("1:"&1024)),2))` **Ctrl Shift Enter**

`The Excel` **Large()** `function has the following syntax:`

[![](https://chandoo.org/wp/wp-content/uploads/2012/05/FS03.png "FS03")](https://chandoo.org/wp/wp-content/uploads/2012/05/FS03.png)

-------------------------------------------------------------------------------------------------------------------------------------

`In Faseeh’s Formula we see`

`=LARGE(((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")*ROW(INDIRECT("1:"&1024)),2)`

`**Array**:` `((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")*ROW(INDIRECT("1:"&1024))`

`**K**:     2`

`So we can see that the Large() function is looking for the Second Largest value (`**K=2**`) in the array.`

`Lets pull the Array apart`

`The Array consists of two parts separated by a Multiplication sign.`

`((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")``*ROW(INDIRECT("1:"&1024))`

We can look at each part separately and then combine them at the end.

The first part `MID($A1,ROW(INDIRECT("1:"&1024)),1)="\"`

Consists of `MID($A1,ROW(INDIRECT("1:"&1024)),1)` `and an` `= "\"`

In a Blank cell Say **E25** enter \=`MID($A1,ROW(INDIRECT("1:"&1024)),1)` and press **F9** Not **Enter**

`Excel responds with an Array:` `=` `{"D";":";"\";"D";"a";"t";"a";"\";"P";"e";"r";"s";"o";"n";"a";"l";"\";"s";"r";"a";"m";"a";"s";"a";"m";"\";"d";"e";"s";"k";"t";"o";"p";"\";"E";"x";"c";"e";"l";"d";"a";"t";"a";".";"x";"l";"s";""; … ;"" ;""}`

We can see here that Excel has taken the value of cell A1 and broken it up as text and put each character into an element in the array.

So the whole line: `MID($A1,ROW(INDIRECT("1:"&1024)),1)="\"`

Is evaluating this array against a `"\"` and should return an array of True/False values

In a Blank cell **E27** put the following: \=MID($A1,ROW(INDIRECT(“1:”&1024)),1)=”\\” and press **F9** Not **Enter**

Excel responds with a an array of 1024 Falses

\={FALSE;FALSE;FALSE; …. ;FALSE;FALSE}

That’s not quite what we expected ?

The Function is \=MID($A1,ROW(INDIRECT(“1:”&1024)),1)=”\\”

Which is a Boolean way of saying if the Middle 1 Character of Cell A1 from position 1 to 1024  is = “\\” return an Array of the values.

What is going on here?

If we modify the formula slightly to =(MID($A1,ROW(INDIRECT(“1:”&1024)),1)=”\\”)\*1

And evaluate (F9) that in cell **E28**

Excel returns an Array \={0;0;1;0;0;0;0;1;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;1;0; … ;0;0}

The array consists of 1024 0’s except for the positions where the Array = “\\” where it has 1’s.

Lets go inside this part of the formula and see what is happening.

\=(MID($A1,ROW(INDIRECT(“1:”&1024)),1)

INDIRECT(“1:”&1024) returns a Reference of 1:1024 as Text which Indirect converts to a Range from row 1 to row 1024

\=(MID($A1,ROW(INDIRECT(“1:”&1024)),1)

Row() returns the row number of the array

\=(MID($A1,ROW(INDIRECT(“1:”&1024)),1)

Mid takes the Character from A1 starting at Position Row(INDIRECT(“1:”&1024)) and returns 1 character.

This effectively allows the array to retrieve each character from the Text of a1.

### The Second Part

`((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")``*``ROW(INDIRECT("1:"&1024))`

We have seen that the first part of the equation

`((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")`

Returns an Array of 1’s and 0’s where the formula matched the `"\"` character.

The second part of the equation: `ROW(INDIRECT("1:"&1024))` is used to return the position of the characters.

In a blank cell **E30** type

`=ROW(INDIRECT("1:"&1024))` and press **F9** Not **Enter**

Excel will respond with \={1;2;3;4;5;6;7;8; … ;1023;1024}

This is a list of the Rows from the Range 1:1024

We can now return to the original function

((MID($A1,ROW(INDIRECT(“1:”&1024)),1))=”\\”)\*ROW(INDIRECT(“1:”&1024))

In a blank cell say E32 type: =((MID($A1,ROW(INDIRECT(“1:”&1024)),1))=”\\”)\*ROW(INDIRECT(“1:”&1024)) and press **F9** Not **Enter**

Excel will respond with:

\={0;0;3;0;0;0;0;8;0;0;0;0;0;0;0;0;17;0;0;0;0;0;0;0;0;26;0;0;0;0;0;0;0;34;0; … ;0;0;0;0}

This array is the combination of the two arrays discussed above.

That is it is the 1’s and 0’s where the \\’s are multiplied by the Row Numbers.

We can see that the positions where the \\’s are have the position numbers listed

\={0;0;**3**;0;0;0;0;**8**;0;0;0;0;0;0;0;0;**17**;0;0;0;0;0;0;0;0;**26**;0;0;0;0;0;0;0;**34**;0; … ;0;0;0;0}

The Large Function in the original Formula:

`=LARGE(((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\")*ROW(INDIRECT("1:"&1024)),2)`

Then extracts the second largest number, which in this case is the value **26**

### `Advantages:`

`To assign the position number you need to know how many \’s are in the formula to start with`

### `Disadvantages:`

`This is an Array Formula which some people struggle with`

How the formula works is difficult to workout or explain.

Modified Formula
----------------

`With a small modification you can introduce a constant to allow a variable n’th character to be retrieved without knowing how many \’s there were originally.`

`=LARGE(((MID($A1,ROW(INDIRECT("1:"&LEN(A1))),1))="\")*ROW(INDIRECT("1:"&LEN(A1))),LEN(A1)-LEN(SUBSTITUTE(A1,"\",""))-**4**+1) Ctrl Shift Enter`

`**Or**`

`=LARGE(((MID($A1,ROW(INDIRECT("1:"&LEN(A1))),1))="\")*ROW(INDIRECT("1:"&LEN(A1))),LEN(A1)-LEN(SUBSTITUTE(A1,"\",""))-**B1**+1) **Ctrl Shift Enter**`

`Where cell **B1** contains 4`

`Where 4 is the 4th character you want to find the location for.`

`You can examine how the replacement of 2 with LEN(A1)-LEN(SUBSTITUTE(A1,"\",""))-**4**+1 works`

How Else Can You Solve Senthilkumar\_rm’s Problem?
--------------------------------------------------

Your task is to find the location of the 4th Slash `"\"` in the text string: D:\\Data\\Personal\\sramasam\\desktop\\Exceldata.xls

Can you solve **Senthilkumar\_rm’s** problem another way?

Can you beat my **44** characters ?

Let us know in the comments below:

Download
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/05/Slash.xls "Find Slash")
.

Formula Forensics “The Series”
------------------------------

This is the 21st post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "The Formula Forensics Series")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
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
| Written by Hui...  <br>Tags: [char()](https://chandoo.org/wp/tag/char/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [find](https://chandoo.org/wp/tag/find/)<br>, [INDIRECT()](https://chandoo.org/wp/tag/indirect/)<br>, [large](https://chandoo.org/wp/tag/large/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [search](https://chandoo.org/wp/tag/search/)<br>, [substitute()](https://chandoo.org/wp/tag/substitute/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 42 Responses to “Formula Forensic No. 021 – Find the 4th Slash !”

1.  ![](https://secure.gravatar.com/avatar/d058073adbcc7d555f218478582adce00f1e589d22df2eb785147b120925bfbd?s=64&d=mm&r=g) [Jamie Bull](http://oco-carbon.com/)
     says:
    
    [May 17, 2012 at 10:15 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-223996)
    
    I really like your substitute() method. Bearing in mind in the specific case here we know we're looking in a file path, you could replace the char(135) part with something that's not allowed in filenames.
    
    Something like =FIND("?",SUBSTITUTE(A1,"\\","?",4))
    
    Ok, it's nothing new and prone to breaking if used in a different situation but yay, shorter! 35 chars. 
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-223996)
    
2.  ![](https://secure.gravatar.com/avatar/aef106a0accda3a705cbe18ae7d54e92235d561f7af70e1f2278869903441570?s=64&d=mm&r=g) Sunil says:
    
    [May 17, 2012 at 11:11 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-224000)
    
    FIND("/",SUBSTITUTE(A1,"\\","/",4))
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224000)
    
3.  ![](https://secure.gravatar.com/avatar/a3b3b433f9b9a8993b23e8bcba44e3d4ee375fc15aca48c21023b489afa408bb?s=64&d=mm&r=g) [Myles](http://www.bespokeexceltraining.co.uk/)
     says:
    
    [May 17, 2012 at 2:00 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224004)
    
    I also really like the SUBSTITUTE() option. I've used the first option in the past, the SUBSTITUTE() option simplifies the formula nicely.
    
    I'm not a fan of arrays due to their complexity for other users to pick up. Certainly to be avoided when there is a much simpler solution.
    
    Think Sunil just won the prize for the shortest solution! 
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224004)
    
4.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [May 17, 2012 at 2:50 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224008)
    
    I personally liked Hui's Substitute() Option, but i believe that we should learn and understand every possible solution, might the concept apparently difficult be helpful somewhere else.  
    Regards,  
    Faseeh  
     
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224008)
    
    *   ![](https://secure.gravatar.com/avatar/a3b3b433f9b9a8993b23e8bcba44e3d4ee375fc15aca48c21023b489afa408bb?s=64&d=mm&r=g) [Myles](http://www.bespokeexceltraining.co.uk/)
         says:
        
        [May 17, 2012 at 3:41 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224009)
        
        Faseeh,
        
        I absolutely agree that it is always worth trying (and sharing) as many different options as possible as you never know when they might come in handy for something else. 
        
        My comment was not supposed to be a criticism (& apologies if it came across that way), I just wanted to raise the point that arrays should be used with caution.
        
        Myles 
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224009)
        
        *   ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
            
            [May 18, 2012 at 4:46 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-224064)
            
            [Myles,](http://www.bespokeexceltraining.co.uk/)
              
            Hey, no need for apologies! Happy to Help, 😀 Yes these formula should be used with caution.  
            Faseeh  
             
            
            [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224064)
            
5.  ![](https://secure.gravatar.com/avatar/8dfa03598c3af22071262812e2dc5ff43729b0f6e75fc34d1a2b516534237223?s=64&d=mm&r=g) Austinma says:
    
    [May 17, 2012 at 4:16 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224010)
    
    Hi
    
    Personally I really like the find/substitute method as it seems a logical and simple solution.
    
    Out of interest, I was wondering how this information/read out might be applied.
    
    Having got the answer 26 what can I do with it or to but it another why would I need to know what the character is at position 26?
    
    Apologies if **Senthilkumar\_rm** expanded on this in his original post.
    
    Keep up the good work.
    
    Regards
    
    Mark
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224010)
    
6.  ![](https://secure.gravatar.com/avatar/e8424002421c5e64ea8eb0d2e384914dd58716a8b3716255dd3393d45d246a34?s=64&d=mm&r=g) Ian Hinckley says:
    
    [May 17, 2012 at 4:59 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224011)
    
    haha, beaten to it
    
    \=FIND("\*",SUBSTITUTE(A1,"/","\*",4))
    
    if you want the last "/" rather than the 4th then use
    
    \=FIND("\*",SUBSTITUTE(A1,"/","\*",LEN(A1)-LEN(SUBSTITUTE(A1,"/",""))))
    
    Have fun
    
    Ian 
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224011)
    
7.  ![](https://secure.gravatar.com/avatar/a3b3b433f9b9a8993b23e8bcba44e3d4ee375fc15aca48c21023b489afa408bb?s=64&d=mm&r=g) [Myles](http://www.bespokeexceltraining.co.uk/)
     says:
    
    [May 17, 2012 at 5:12 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224013)
    
    Hi Mark,
    
    The position of a specific character is normally used to extract a specific piece of text from a text string.
    
    For eg. with D:\\Data\\Personal\\sramasam\\desktop\\Exceldata.xls in cell A1
    
    Use Hui's formula to pull out the position of the 4th "/" as 26
    
    Use the Len() function to find the full string length  =Len(A1) = 47
    
    Finally use the Right() function to extract the text after the 4th "/" =RIGHT(A1,47-26) =  desktop\\Exceldata.xls 
    
    Myles  
     
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224013)
    
    *   ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
        
        [May 17, 2012 at 6:03 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224016)
        
        Another way to extract a portion of a string is to create a giant gap, and then trim the excess:  
        \=TRIM(MID(SUBSTITUTE(A1,"\\",REPT(" ",999),4),999,999)) 
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224016)
        
    *   ![](https://secure.gravatar.com/avatar/8dfa03598c3af22071262812e2dc5ff43729b0f6e75fc34d1a2b516534237223?s=64&d=mm&r=g) Austinma says:
        
        [May 17, 2012 at 8:41 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224026)
        
        @ Myles,  
           
        Thanks for your message.  
           
        I'm actually pleased that I came up with a scenario similar to the one you mention using the =RIGHT function. I thought about perhaps using the =MID function to extract some or all of the text. For example:  
           
        \=MID(A1,26,9)  
           
        \=\\desktop\\  
           
        Thanks again,  
           
        Mark  
         
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224026)
        
8.  ![](https://secure.gravatar.com/avatar/7426eab78443c4e9359b02fd169b251fc5f528a999de075c6b79803498682152?s=64&d=mm&r=g) Mike86 says:
    
    [May 17, 2012 at 7:17 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224019)
    
    You could use the Small() function instead of Large().  That way finding the 4th smallest number is pretty straight forward.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224019)
    
    *   ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
        
        [May 17, 2012 at 8:27 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224024)
        
        Small would pull in the 0s returned in the array before returning the matches
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224024)
        
    *   ![](https://secure.gravatar.com/avatar/a426c18d505e6947a99292548c2a1beaa49097547bb29fb6bc7f6b0be1f5682b?s=64&d=mm&r=g) Joe says:
        
        [August 20, 2012 at 5:14 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-229037)
        
        A little late on this one, but I liked what you were going for.
        
        It bugged me that Faseed found the second to last \\ not really the fourth. Since the zeroes interfere with your suggestion to use the SMALL function, I tried finding the largest reciprocal like so:
        
        \=1/(LARGE(((MID($A1,ROW(INDIRECT("1:"&1024)),1))="\\")\*(1/(ROW(INDIRECT("1:"&1024)))),4))
        
        Only 88 characters, vs Chandoo's modification that used 121.
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-229037)
        
9.  ![](https://secure.gravatar.com/avatar/68322167fe7dd4ce3a5483d483f8a27d5ba29600a2c2166759fca0c2dce37181?s=64&d=mm&r=g) [Pedro Wave](http://pedrowave.blogspot.com/)
     says:
    
    [May 17, 2012 at 8:25 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224023)
    
    Why to use a normal character as "?" or "/" to substitute "\\"?  
    I prefer to use a special character, the newline or line break or end-of-line or EOL or LF or CHAR(10), inserted into a cell when you press Alt+Enter  
    The formula with only 33 visible chars:  
    <code>=FIND("  
    ",SUBSTITUTE(A1,"\\","  
    ",4))</code>
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224023)
    
    *   ![](https://secure.gravatar.com/avatar/d058073adbcc7d555f218478582adce00f1e589d22df2eb785147b120925bfbd?s=64&d=mm&r=g) [Jamie Bull](http://oco-carbon.com/)
         says:
        
        [May 17, 2012 at 11:31 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224036)
        
        Excel still counts Alt+Enter as a character though. Try putting a ' before the formula and using LEN(). Yours, mine and Sunil's versions all come out as 35 chars.
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224036)
        
        *   ![](https://secure.gravatar.com/avatar/68322167fe7dd4ce3a5483d483f8a27d5ba29600a2c2166759fca0c2dce37181?s=64&d=mm&r=g) [Pedro Wave](http://pedrowave.blogspot.com/)
             says:
            
            [May 23, 2012 at 9:26 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-224256)
            
            Jamie, I said that 33 chars are visible but, as you noted, really are 35 chars into my formula. The advantage is that the EOL character not often found among the chars to replace. Observe what happens if the "?" or any other substituting "\\" is included in the string.
            
            [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224256)
            
10.  ![](https://secure.gravatar.com/avatar/68322167fe7dd4ce3a5483d483f8a27d5ba29600a2c2166759fca0c2dce37181?s=64&d=mm&r=g) [Pedro Wave](http://pedrowave.blogspot.com/)
     says:
    
    [May 17, 2012 at 8:31 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224025)
    
    Write the last formula without <code> tags.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224025)
    
11.  ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
    
    [May 17, 2012 at 9:19 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224028)
    
    You can wrap the array portion of the LARGE function in Faseeh's formula in an INDEX function to remove the CSE requirement  
    so LARGE(INDEX(MID(.........),0,1),....)
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224028)
    
12.  ![](https://secure.gravatar.com/avatar/b5b3fe5b04a5efe893340f7c6a80c42ed27d6fd5e7446f4a261b8f4edefff453?s=64&d=mm&r=g) Ron Wallace says:
    
    [May 17, 2012 at 11:06 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224035)
    
    I like the substitute method since it can be modified to:
    
    \=IFERROR(FIND("/",SUBSTITUTE($G$5,$G$6,"/",$H$6)),"Not that many in the string!")  
       
    and then you enter the desired character in cell G6 with the repetition in cell H6 which allow the search without changing the formula.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224035)
    
13.  ![](https://secure.gravatar.com/avatar/bd38c9e007f4678d947ebf372bf8ef9ae5f8100975278a8bbfec8c1bac318963?s=64&d=mm&r=g) Rahul says:
    
    [May 18, 2012 at 2:28 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-224049)
    
    If I want to find first "/" from the right wether there are 4 "/" or 3 "/" or 8 "/" char available in a string. What should we use.  I mean that is there any formula exist which start searching from the right.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224049)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [May 18, 2012 at 3:01 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-224053)
        
        @Rahul
        
        This is the same as finding the last \\ from the left.
        
        The formula `LEN(G5)-LEN(SUBSTITUTE(G5,"\",""))`  
        Calculates the number of occurrences of the Character \\ in the string.
        
        `=FIND("*",SUBSTITUTE(G5,"\","*",LEN(G5)-LEN(SUBSTITUTE(G5,"\",""))))`  
        Will do what you want.
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224053)
        
        *   ![](https://secure.gravatar.com/avatar/bd38c9e007f4678d947ebf372bf8ef9ae5f8100975278a8bbfec8c1bac318963?s=64&d=mm&r=g) Rahul says:
            
            [May 19, 2012 at 4:02 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-224117)
            
            Thanks.
            
            [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224117)
            
14.  ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
    
    [May 18, 2012 at 4:03 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224107)
    
    Here is what I came up with:  
    "Character to Find" is in cell C1 - \\  
    "Occurrence" to Find is in cell C2  
    "Max Occurrences" is in cell C3 - formula (below)  
    "String to Search" is in cell C4  
       
    \=INDEX(SMALL(INDEX(LARGE(SplitChar\*SplitArray,kArray),,1),kArray),C2)  
    Names:  
    SplitChar  
    \=MID(Sheet1!$C$4,SplitArray,1)=Sheet1!$C$1  
    SplitArray  
    \=ROW(INDIRECT("1:"&LEN(Sheet1!$C$4)))  
    kArray  
    \=ROW(INDIRECT("1:"&Sheet1!$C$3))  
       
    and in cell C3 for max occurrences enter   
    \=SUMPRODUCT(--SplitCHar)  
       
    It is basically the same as Faseeh except 3 differences  
    1/I use the INDEX function to return arrays for the LARGE and SMALL functions, so the formula does not need to be CSE entered.  
    2/ I used Named Formulas to bypass CSE and for clarity  
    3/I added a SMALL function to invert the results of the LARGE function, so when you want to find the 1,2,3,n occurrences you would search with 1,2,3,n, not n,3,2,1
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224107)
    
    *   ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
        
        [May 18, 2012 at 4:05 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224108)
        
        \=SUMPRODUCT(- -SplitCHar) is the double negative not a single dash
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224108)
        
15.  ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
     says:
    
    [May 19, 2012 at 5:45 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-224122)
    
    My question is the same as was asked earlier... why do you want to find the 4th slash. If it is so you can use it as a starting point for pulling out the 5th delimited field, the I think this mini-blog article of my would be of interest...
    
    [Get Field from Delimited Text String](http://www.excelfox.com/forum/f22/get-field-delimited-text-string-333/)
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224122)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [May 19, 2012 at 3:31 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224128)
        
        @Rick
        
        That's a neat formula
        
        I may well plagiarize it soon.
        
        **Hui...**
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224128)
        
        *   ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
             says:
            
            [May 19, 2012 at 4:06 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224129)
            
            Hi Hui,
            
            I am glad you liked the formula... feel free to plagiarize it anytime
            
            If you haven't already done so, check out my other articles here....
            
            [Rick Rothstein's Corner](http://www.excelfox.com/forum/f22/)
            
            and perhaps you will find some other things to plariagize as well.
            
            Rick
            
            [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224129)
            
        *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
             says:
            
            [May 19, 2012 at 5:20 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224130)
            
            Lovely formula indeed. Bookmarked and will be using as needed 🙂
            
            [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224130)
            
            *   ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
                 says:
                
                [May 19, 2012 at 6:04 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-224131)
                
                @Chandoo,
                
                And I am glad you liked the formula as well. In case you or Hui (or anyone else reading this thread) missed the link at the bottom of my article, I just wanted to draw your attention to my related article title "[**Get "Reversed" Field from Delimited Text String**](http://www.excelfox.com/forum/f22/get-reversed-field-delimited-text-string-334/#post1157)
                " which allows you to easily get, say, the next to last field in a delimited string without needing to know how many total items are in the string. NOTE... be sure to read the whole thread as one of the responders offered a far better (more concise) formula than the one I posted in my article.
                
                Rick
                
                [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-224131)
                
                *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
                    
                    [October 23, 2012 at 11:11 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-275098)
                    
                    Ohhh....these just make my head hurt, Rick. How the heck do they work? Got me completely baffled.  
                    I have a much longer formula that like yours also returns the nth delimiter. It's like a light-year long:  
                    \=MID(input,FIND("|",SUBSTITUTE(Delimiter&input&Delimiter,Delimiter,"|",ROW(INDEX(A:A,Fieldnumber):INDEX(A:A,Fieldnumber+1)))),FIND("|",SUBSTITUTE(Delimiter&input&Delimiter,Delimiter,"|",ROW(INDEX(A:A,Fieldnumber):INDEX(A:A,Fieldnumber+1))+1))-1-FIND("|",SUBSTITUTE(Delimiter&input&Delimiter,Delimiter,"|",ROW(INDEX(A:A,Fieldnumber):INDEX(A:A,Fieldnumber+1)))))
                    
            *   ![](https://secure.gravatar.com/avatar/227cd9b40c22b97938f2e42774acccdd7c2defe85848de20d3a666ebf58c365a?s=64&d=mm&r=g) manish says:
                
                [July 16, 2012 at 8:29 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-227144)
                
                I didn't understand the  reason of using char(135).  
                Please ellaborate
                
                [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-227144)
                
                *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                     says:
                    
                    [July 16, 2012 at 8:49 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-227148)
                    
                    @Manish  
                    It is just a character that is unlikely to appear in "normal" Text  
                    You could just as easily have used an "e" if your text isn't going to contain an "e"
                    
16.  ![](https://secure.gravatar.com/avatar/227cd9b40c22b97938f2e42774acccdd7c2defe85848de20d3a666ebf58c365a?s=64&d=mm&r=g) manish says:
    
    [July 16, 2012 at 8:30 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-227145)
    
    Got it .. thanks
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-227145)
    
17.  [Extract file name from full path using formulas | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2012/10/23/extract-file-name-from-full-path-using-formulas/)
     says:
    
    [October 23, 2012 at 8:05 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-274975)
    
    \[...\] Of course there are many methods find where the last is. You can find a very excellent summary of these techniques in our formula forensics #21 – finding the 4th slash. \[...\]
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-274975)
    
18.  ![](https://secure.gravatar.com/avatar/9572142152f4e1936e46fc1b2e6d8fafba03664a21cfbd875a03efb6a040ddc5?s=64&d=mm&r=g) Achaibou Karim says:
    
    [May 1, 2013 at 1:44 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-428269)
    
    I have made a small VBA function which finds the last "char" in a text string. It can be easily adapted to give the nth location within the text string.
    
    `Function findLastChar(text As String, char As String)   For i = 1 To Len(text)   If Mid(text, i, 1) = char Then   findLastChar = i   End If   Next i   End Function`
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-428269)
    
19.  ![](https://secure.gravatar.com/avatar/d306cb2269ffeafd5f9a9c43f06b21b08f8167d5b26e19078396861536eac808?s=64&d=mm&r=g) JonB says:
    
    [January 23, 2015 at 8:06 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-898735)
    
    well I believe the goal is to find the name of the file ...
    
    \=MID(CELL("filename"),SEARCH("\[",CELL("filename"))+1, SEARCH("\]",CELL("filename"))-SEARCH("\[",CELL("filename"))-1)\
    \
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-898735)\
    \
20.  ![](https://secure.gravatar.com/avatar/b7ca90b3c2f8314453577beb18e367b3174c8e5d07540f7e525929f325b0c041?s=64&d=mm&r=g) [workbookwrench](http://none/)\
     says:\
    \
    [January 7, 2016 at 3:30 am](https://chandoo.org/wp/formula-forensic-no-021/#comment-1117079)\
    \
    How high do you want to go? For the 2nd you can use\
    \
    \=FIND("-",A1,FIND("-",A1)+1)\
    \
    but that would get longer for 3rd or 4th\
    \
    For 3rd you could use this\
    \
    \=FIND("^^",SUBSTITUTE(A1,"-","^^",3))\
    \
    change 3 to whatever instance you need\
    \
    from [http://www.mrexcel.com/forum/excel-questions/473844-find-second-dash-cell.html](http://www.mrexcel.com/forum/excel-questions/473844-find-second-dash-cell.html)\
    \
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-1117079)\
    \
    *   ![](https://secure.gravatar.com/avatar/5af84454d2fd0dfb3d555b8bfbd56f3933a96e14a661be5b74f6c9102c0bf301?s=64&d=mm&r=g) Cesar Ordonez says:\
        \
        [December 9, 2016 at 9:51 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-1363154)\
        \
        Worked like a charm for me! Thank you!\
        \
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-1363154)\
        \
21.  ![](https://secure.gravatar.com/avatar/ab28ccfcb57bcb8f0b1b9a2510e4a65988dea1d4e2aaaff40afdd3ab5b151f65?s=64&d=mm&r=g) Rahul Mangla says:\
    \
    [July 20, 2017 at 4:40 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-1482926)\
    \
    \=LEFT(G8,30) dflsfj\\rahul\\r\\RRWERWRE\\FSDFSDF\
    \
    \=LEN(G8)  \
    \=LEN(SUBSTITUTE(G8,"\\",""))  \
    \=G10-G11  \
    \=SUBSTITUTE(G8,"\\","\*",G12)  \
    \=MID(G13,FIND("\*",G13,1)+1,LEN(G13))\
    \
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-1482926)\
    \
22.  ![](https://secure.gravatar.com/avatar/ab28ccfcb57bcb8f0b1b9a2510e4a65988dea1d4e2aaaff40afdd3ab5b151f65?s=64&d=mm&r=g) Rahul Mangla says:\
    \
    [July 20, 2017 at 4:41 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-1482928)\
    \
    no array formauls required very easy question\
    \
    [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-1482928)\
    \
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)\
         says:\
        \
        [July 20, 2017 at 7:30 pm](https://chandoo.org/wp/formula-forensic-no-021/#comment-1482969)\
        \
        @Rahul\
        \
        Thanx for your comments\
        \
        here are a number of wasy of getting the 4th Slash when it is hard coded that the 4th slash is what you want.\
        \
        The technique I show above works for any Number of Slashes, eg The 8th or 13th Slash\
        \
        Please read the comments above as a number of people have also identified alternative solutions as well\
        \
        [Reply](https://chandoo.org/wp/formula-forensic-no-021/#comment-1482969)\
        \
\
### Leave a Reply\
\
[Click here to cancel reply.](https://chandoo.org/wp/formula-forensic-no-021/#respond)\
\
 Name (required)\
\
 Mail (will not be published) (required)\
\
 Website\
\
  \
\
 Notify me of when new comments are posted via e-mail\
\
Δ\
\
  \
\
|     |     |\
| --- | --- |\
| « [Please Enroll in our Excel & Dashboards Masterclass – Melbourne](https://chandoo.org/wp/excel-dashboards-masterclass-melbourne/) | [Catchup with Chandoo in Perth](https://chandoo.org/wp/catchup-with-chandoo-in-perth/)<br> » |\
\
**Meet Chandoo**\
\
![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  \
[Read my story](https://chandoo.org/wp/about/)\
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)\
.\
\
**Connect:**\
\
[Chandoo.org](https://www.pinterest.com/xlawesome/)
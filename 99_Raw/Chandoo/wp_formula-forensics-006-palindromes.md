# Formula Forensics looks at if a cell contains a palindrome.

**Source:** https://chandoo.org/wp/formula-forensics-006-palindromes

---

Formula Forensics 006. Palindromes
==================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 13 comments

  

Chandoo wrote a [post](http://chandoo.org/wp/2011/08/12/palindrome-check-excel-formula/ "Palindromes")
 in August 2011 where he looked at determining if a cell contained a [palindrome](http://en.wikipedia.org/wiki/Palindrome "Palindrome")
.

Chandoo presented a formula for determining if a cell; C1; contains a palindrome:

`=IF(SUMPRODUCT((MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)=MID(C1,LEN(C1)-ROW( OFFSET($A$1,,, LEN(C1) )) +1, 1))+0)=LEN(C1),"It’s a Palindrome","Nah!")`

And then Chandoo challenged everyone:

**_How does this formula work?_**

_Well, that is your weekend homework._

So today we’re going to complete our homework and pull apart the above formula and see what makes it tick.

**Palindrome Setup**
--------------------

Download the example file so you can follow along with a worked example, [Excel 97-2010](https://chandoo.org/wp/wp-content/uploads/2011/12/Palindrome.xls "Palindrome example")
.

In a blank worksheet enter

**C1**: “Chandoo” without the brackets

**D1**: `=IF(SUMPRODUCT((MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)=MID(C1,LEN(C1)-ROW( OFFSET($A$1 ,,, LEN(C1)))+1,1))+0)=LEN(C1),"It’s a Palindrome","Nah!")`

In the example below we will work on two words:

Firstly, “Chandoo” which is clearly not a Palindrome

and Secondly, “Radar” which is a Palindrome

**Non-Palindrome Analysis**
---------------------------

The main structure of this formula is that it is a simple If () function.

The Excel If() function is defined by 3 parts

\=If(Condition, Value if True, Value if False)

Our Formula is

`=IF(` `SUMPRODUCT(( MID(C1, ROW( OFFSET( $A$1,,,LEN(C1))), 1) = MID(C1, LEN(C1) - ROW( OFFSET( $A$1,,,LEN(C1))) + 1, 1)) + 0) = LEN(C1)``,` `"It’s a Palindrome"``,` `"Nah!"``)`

Condition:                 `SUMPRODUCT((MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1) = MID(C1, LEN(C1) - ROW(OFFSET($A$1,,,LEN(C1)))+1,1))+0)=LEN(C1)`

`Value if True:` `"It’s a Palindrome"`

`Value if False:` `"Nah!”`

Lets not waste time on the two Values if True/False as they are purely a message to the user, the real work happens in the Condition part of the If() function.

The Condition does all the work: `SUMPRODUCT((MID(C1,ROW( OFFSET($A$1,,, LEN(C1))),1) = MID(C1, LEN(C1)-ROW( OFFSET($A$1,,,LEN(C1)))+1,1))+0)``=``LEN(C1)`

`Is a Sumproduct and a Len`

`That is the formula is doing a calculation of the sumproduct of some inner calculations and comparing the answer to the length of the contents of cell: C1 in the example of "Chandoo" = Len(C1) = 7   `

`SUMPRODUCT((` `MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)``=` `MID(C1, LEN(C1)-ROW( OFFSET($A$1,,, LEN(C1)))+1,1)``)+0)``=LEN(C1)`

Lets now look at the two inner calculations:

`MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)`

Copy this calculation into E7

\= `MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)` `Don’t press Enter, press F9`

`(If using the example file goto cell E9, Press F2 and then F9)   `

`Excel will return {"C";"h";"a";"n";"d";"o";"o"} Don’t press Enter, press Esc when ready`

`It is an Array of the letters in the cell C1`

Now do the same for the second part of the equation:

Copy this calculation into E8

\= `MID(C1, LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1,1)` `Don’t press Enter, press F9`

`Excel will return` {“o”;”o”;”d”;”n”;”a”;”h”;”C”}

You will notice that this array is the reverse of the word in C1

We will come back to how these two equations work in a minute or two

But note that we now have

Sumproduct((`{"C";"h";"a";"n";"d";"o";"o"}=`{“o”;”o”;”d”;”n”;”a”;”h”;”C”})+0)

We can evaluate the inner part of this to see what happens

Copy this calculation into E10

`={"C";"h";"a";"n";"d";"o";"o"}=`{“o”;”o”;”d”;”n”;”a”;”h”;”C”} `Don’t press Enter, press F9`

`Excel will return an Array` {FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE}

This means that only the 4th letter or “n” in Chandoo is the same forward and backwards.

Looking at the next bit

Copy this calculation into E12

\=(`{"C";"h";"a";"n";"d";"o";"o"}=`{“o”;”o”;”d”;”n”;”a”;”h”;”C”})+0 `Don’t press Enter, press F9`

`Excel will return` {0;0;0;1;0;0;0}

Excel has converted the false/True array above into an array of 0’s and 1’s  

Finally in E14 evaluate:

\=Sumproduct({0;0;0;1;0;0;0})

Is evaluated and Excel adds up all the numbers returning a 1 as the answer.

So the original equation :

`=IF(``SUMPRODUCT((MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)=MID(C1,LEN(C1)- ROW( OFFSET($A$1,,, LEN(C1))) +1,1)) +0 )=LEN(C1)``,``"It’s a Palindrome"``,``"Nah!"``)`

Is simplified as

`=IF(` `1 = LEN(C1)``,``"It’s a Palindrome"``,``"Nah!"``)`

Now C1 has the Word “Chandoo “ in it which is 7 letters long

`=IF(` `1 = 7``,``"It’s a Palindrome"``,``"Nah!"``)`

So the If() function returns the False answer of “Nah!”

**Non-Palindrome Analysis**
---------------------------

If we place a Palindrome such as “Radar” in C1 and skip backwards to the

`SUMPRODUCT((` `MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)``=` `MID(C1, LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1,1)``)+0)``=LEN(C1)`

Section , Evaluating each part again we see

`E21: MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)`

`Evaluates to {"R";"a";"d";"a";"r"}`

`And`

`MID(C1, LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1,1)`

`Evaluates to: {"r";"a";"d";"a";"R"}`

`And`

`(` `MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)``=` `MID(C1, LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1,1)``)`

`Evaluates to: {TRUE;TRUE;TRUE;TRUE;TRUE}`

With

`SUMPRODUCT((` `MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)``=` `MID(C1, LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1,1)``)+0)`

`Evaluating to: 5`

`Which is clearly equal to the length of the word “Radar” and so the If() function returns “``It’s a Palindrome”`

A Minute Later
--------------

`But how do the middle bits`

`MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)`

`and`

`MID(C1, LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1,1)`

`Work?`

`The two equations are effectively the same`

`The first works left to right and extracts each letter one at a time`

`The second works right to left and extracts each letter one at a time`

`How Does`

`=MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1) F9`

`Evaluate to {"C";"h";"a";"n";"d";"o";"o"}`

`=MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1) F9`

Is a simple Mid() function which takes the `1` Character at position `ROW(OFFSET($A$1,,,LEN(C1))) from the contents of C1`

`What is` `ROW(OFFSET($A$1,,,LEN(C1)))`

`Is used to return an array of numbers from 1 to Len(C1) in this case 7`

`eg: {1;2;3;4;5;6;7}   `

`So in E16 enter =ROW(OFFSET($A$1,,,LEN(C1))) and press F9`

`Excel evaluates it to {1;2;3;4;5;6;7}`

So the function `=MID(C1,ROW(OFFSET($A$1,,,LEN(C1))),1)`

`Returns the 1st, 2nd. 3rd, 4th, 5th, 6th & 7th characters from C1 as an Array`

How Does `=ROW(OFFSET($A$1,,,LEN(C1))) work?`
---------------------------------------------

`=ROW(OFFSET($A$1,,,LEN(C1)))`

Takes the Row of the range defined by the Offset Function

Note that `OFFSET($A$1,,,LEN(C1)) is a simple Offset that sets up a range`

`The excel Offset Function is defined as`

`=Offset(Reference, Rows, Columns, [Height], [Width])`

In our example

`=OFFSET($A$1,,,LEN(C1))`

Will return a Range which is referenced to A1, has no Row or Column offset and is the length of cell the contents of Cell C1

Effectively returning a range A1:A7

Because this is all in an Sumproduct formula, Excel evaluates this formula for each value in the Range

And so

`=ROW(OFFSET($A$1,,,LEN(C1)))`

`evaluates it to`

`{1;2;3;4;5;6;7}`

Which is then used extract the characters from the word in C1 into an Array as `{"C";"h";"a";"n";"d";"o";"o"}`

`A similar process applies to the second half of the two equations`

`MID(C1, LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1,1)`

Except that it is evaluated from the Right to Left of the Word in C1 by use of the

`LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1`

`In the Mid Equation`

Summary
-------

So in summary we use Sumproduct to compare two Arrays, which contain the word and the word reversed, to each other. The Sumproduct counts the number of common matches and then this is compared to the length of the word.

If the two match the word is a Palindrome.

DOWNLOAD
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2011/12/Palindrome.xls "Palindrome Example File")
.

**OTHER POSTS IN THIS SERIES**
------------------------------

You can learn more about how to pull Excel Formulas apart in the following posts which are all included in the [Formula Forensic Series:](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics")

WE NEED YOUR HELP
-----------------

I am running out of ideas for Formula Forensics and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post as Luke did in [Formula Forensics 003](http://chandoo.org/wp/2011/11/18/formula-forensics-003/ "Lukes reward")
 or like above.

If you have a formula that you would like explained but don’t want to write a post also send it in to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
 or [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
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
| Written by Hui...  <br>Tags: [if()](https://chandoo.org/wp/tag/if/)<br>, [len()](https://chandoo.org/wp/tag/len/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [OFFSET()](https://chandoo.org/wp/tag/offset/)<br>, [Pailindrome](https://chandoo.org/wp/tag/pailindrome/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [sumproduct](https://chandoo.org/wp/tag/sumproduct/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 13 Responses to “Formula Forensics 006. Palindromes”

1.  ![](https://secure.gravatar.com/avatar/f3717c8926fc662d09f373c48a3c8935bbfd2f7cfc0e70e28a5c6090c52b67c1?s=64&d=mm&r=g) Jonas says:
    
    [December 15, 2011 at 10:42 am](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-216972)
    
    Nice post! I wonder if there is a way to utilise the = MID(C1, LEN(C1)-ROW(OFFSET($A$1,,,LEN(C1)))+1,1) formula to reverse a word? In other words, a formula that would give the result "oodnahC" if the input is "Chandoo".
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-216972)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [December 15, 2011 at 11:17 am](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-216982)
        
        @Jonas  
        Unfortunately there isn't any way to append the array elements together as you have correctly identified  
        If Microsoft had properly implemented Ranges as an input to the Concatenate function, as they rightfully should have, that should have been possible
        
        [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-216982)
        
2.  ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
    
    [December 15, 2011 at 1:54 pm](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217013)
    
    Excellent write-up Hui. Thanks for showing how to break up a word into the individual characters.
    
    @Jonas  
    As Hui said, you can't do it with native formulas. Here's a short UDF I use when I need to reverse a word.  
    Function Reverse(r As String) As String
    
    For i = Len(r) To 1 Step -1  
    Reverse = Reverse & Mid(r, i, 1)  
    Next i
    
    End Function
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217013)
    
3.  ![](https://secure.gravatar.com/avatar/f3717c8926fc662d09f373c48a3c8935bbfd2f7cfc0e70e28a5c6090c52b67c1?s=64&d=mm&r=g) Jonas says:
    
    [December 15, 2011 at 2:19 pm](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217018)
    
    Thanks for the UDF! Better than nothing 🙂 I have to agree with you Hui that it's a bit strange that Microsoft didn't implement it.
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217018)
    
4.  ![](https://secure.gravatar.com/avatar/b037d8d3f5f885d3b75da94796f676c78fc578ed2dce50a0950efee1e01c6fbb?s=64&d=mm&r=g) simchuck says:
    
    [December 15, 2011 at 7:49 pm](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217079)
    
    @Jonas:  
    I was just looking for this yesterday and found a nice concise UDF to concatenate a range...
    
    [http://www.vbaexpress.com/kb/getarticle.php?kb\_id=817](http://www.vbaexpress.com/kb/getarticle.php?kb_id=817)
    
    I agree that it should be part of the built-in function, but as long as you don't mind a little bit of VBA this will do the job nicely.
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217079)
    
5.  ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
     says:
    
    [December 15, 2011 at 11:39 pm](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217122)
    
    @Jonas, Simchuck  
    or: [http://chandoo.org/wp/2008/05/28/how-to-add-a-range-of-cells-in-excel-concat/](http://chandoo.org/wp/2008/05/28/how-to-add-a-range-of-cells-in-excel-concat/)
      
    there are several variations in the Comments as well
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217122)
    
6.  ![](https://secure.gravatar.com/avatar/cc6922bfe9c8bf7807cacee2312ef529e78bfbc438198ae52b6d5b495aa22855?s=64&d=mm&r=g) K Macdonald says:
    
    [December 18, 2011 at 3:09 am](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217494)
    
    The formulas are pretty awesome but I am also inclined to want to create a UDF and then compare the original to the reversed for a match. Admitted I can lift the concept from an already existing Library and tailor it to VBA in a fraction of the time it takes to understand a formula which runs out to 100 characters. I take the point that not every body is au fait with a programming language and you do introduce security concerns with macros
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217494)
    
7.  ![](https://secure.gravatar.com/avatar/1191cdc6129a6b74a227eae67974fbcb292e08f9c1ee9405dc92d6edceee3f74?s=64&d=mm&r=g) Chandrashekhar Joshi says:
    
    [December 20, 2011 at 7:02 am](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217698)
    
    Dear Chandoo & Hui,
    
    Nice one and very informative. as luke mentioned I always use VBA & helper column to check whether given string is pelindrom of not. here the code  
    Function pd(aa As String)  
    aa = Trim(aa)  
    aa = UCase(aa)  
    Dim tmp As String  
    Dim a As Integer  
    a = Len(aa)  
    For i = Len(aa) To 1 Step -1  
    tmp = tmp & Mid(aa, a, 1)  
    a = a - 1  
    Next i  
    pd = tmp  
    End Function  
    can u please explain if I want to use sub how can I return true or false?  
    THanks everyone
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217698)
    
8.  ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
     says:
    
    [December 20, 2011 at 9:07 am](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217715)
    
    Chandrashekhar  
    Try this function:  
    `Function pd(aa As String)   pd = False   If StrReverse(UCase(Trim(aa))) = UCase(Trim(aa)) Then pd = True   End Function`
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217715)
    
9.  ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
     says:
    
    [December 20, 2011 at 9:19 am](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217717)
    
    Chandrashekhar  
    Also I note that your original function only returns the Upper Case Trimmed reference  
    \=pd("Chandoo") = OODNAHC  
    .  
    It can be simplified as  
    .  
    `Function pd(aa As String)   pd = UCase(Trim(StrReverse(aa)))   End Function`
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217717)
    
10.  ![](https://secure.gravatar.com/avatar/cc6922bfe9c8bf7807cacee2312ef529e78bfbc438198ae52b6d5b495aa22855?s=64&d=mm&r=g) K Macdonald says:
    
    [December 20, 2011 at 10:52 am](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217729)
    
    Some very good comment on writing UDF's but some of us should have found the native StrReverse function by now! Mind you there are times that I find the standard string handling function set in VBA a little incomplete and may have started with a pre-conceived view.
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217729)
    
11.  ![](https://secure.gravatar.com/avatar/1191cdc6129a6b74a227eae67974fbcb292e08f9c1ee9405dc92d6edceee3f74?s=64&d=mm&r=g) Chandrashekhar Joshi says:
    
    [December 20, 2011 at 12:11 pm](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217737)
    
    Thanks Hui. You are real HELP. God bless you and chandoo.
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-217737)
    
12.  ![](https://secure.gravatar.com/avatar/5671034704d280c4a557ef7ac78e92a0ae9df0246d7eb707283548ec2c7af157?s=64&d=mm&r=g) SyedGJ says:
    
    [December 22, 2011 at 8:58 am](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-218198)
    
    Delicious!
    
    [Reply](https://chandoo.org/wp/formula-forensics-006-palindromes/#comment-218198)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-006-palindromes/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Shortcut for Long Models](https://chandoo.org/wp/shortcut-for-long-models/) | [Join Excel School & Become Awesome in Excel Today!](https://chandoo.org/wp/join-excel-school-become-awesome/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
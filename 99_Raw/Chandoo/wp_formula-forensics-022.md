# Sum the Odd Numbers between 1 and 100

**Source:** https://chandoo.org/wp/formula-forensics-022

---

Formula Forensics 022. Sum the Odd Numbers between 1 and 100
============================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 26 comments

  

Last week at the [Chandoo.org Forums](http://chandoo.org/forums/topic/how-to-find-sum-of-odd-numbers-in-a-range-of-1-100)
, **Sunita**, posed the question:

_“Please help me to find out the sum of odd numbers in a range of 1-100 numbers_

_Like 1+3+5+7+ … 97+ 99_

_How it will find through an excel formula?”_

I chipped in with two array formulas:

\=SUM(2\*ROW(OFFSET($A$1,,,100/2))-1) **Ctrl Shift Enter**

and  
\=SUM(ROW(1:100)\*MOD(ROW(1:100),2)) **Ctrl Shift Enter**

Lets look at each of these in turn.

As usual at Formula Forensics you can download a Sample File here and follow along [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2012/05/Count-Odd-Numbers.xls "FF 22.")
.

Formula 1: =SUM(2\*ROW(OFFSET($A$1,,,100/2))-1)
-----------------------------------------------

The first formula we will examine is:

\=SUM(2\*ROW(OFFSET($A$1,,,100/2))-1) **Ctrl Shift Enter**

This formula works on the principle of making an array of the odd numbers between 1 and 100 and the adding them up.

We can make an array of the odd numbers from 1 to 100 by:

1.  First make an array of all numbers from 1 to 50
2.  Second double the array values
3.  Subtract 1.
4.  Add up the values

### 1\. Make an Array from 1 to 50

The formula ROW(OFFSET($A$1,,,100/2)) can be used to make an array of the numbers from 1 to 50

In a spare cell, **D4**, type \=ROW(OFFSET($A$1,,,100/2)) then press **F9** not enter

Excel will respond with an array: \={1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50}

### How does this work?

Offset($A$1,,,100/2) sets up a Range from A1 with no Row or Column offset, but with a height of 100/2 = 50.

In a spare cell, **D6**, type \=OFFSET($A$1,,,100/2) then press **F9** not enter

Excel will respond with an array: \={0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0}

We can see that the array contains 50 Zero’s (You can count them to check).

True.

But it is 50 Rows of Zero’s. The **;**’s in the array separate Rows.

So the expanded formula: \=ROW(OFFSET($A$1,,,100/2))

Returns the Rows of the Array Elements, not the Array Values.

### 2\. Double the Values

The formula 2\*ROW(OFFSET($A$1,,,100/2)) is used to double the array values

In a spare cell, **D8**, type \=2\*ROW(OFFSET($A$1,,,100/2)) then press **F9** not enter

Excel will respond with an array:  \={2;4;6;8;10;12;14;16;18;20;22;24;26;28;30;32;34;36;38;40;42;44;46;48;50;52;54;56;58;60;62;64;66;68;70;72;74;76;78;80;82;84;86;88;90;92;94;96;98;100}

### 3\. Subtract 1

The formula 2\*ROW(OFFSET($A$1,,,100/2)) \-1 is used to subtract a value of a from the array values

In a spare cell, **D10**, type \=2\*ROW(OFFSET($A$1,,,100/2)) -1 then press **F9** not enter

Excel will respond with an array:  \={1;3;5;7;9;11;13;15;17;19;21;23;25;27;29;31;33;35;37;39;41;43;45;47;49;51;53;55;57;59;61;63;65;67;69;71;73;75;77;79;81;83;85;87;89;91;93;95;97;99}

### 4\. Add up the Values

The formula \=Sum(2\*ROW(OFFSET($A$1,,,100/2)) -1) is used to add up the array values

In a spare cell, **D12**, type \=Sum(2\*ROW(OFFSET($A$1,,,100/2)) -1) then press **F9** not enter

Excel will respond with a value of **\= 2500**, The Answer.  
 

Formula 2: =SUM(ROW(1:100)\*MOD(ROW(1:100),2))
----------------------------------------------

The second formula we will examine is:

\=SUM(ROW(1:100)\*MOD(ROW(1:100),2)) **Ctrl Shift Enter**

This formula works by constructing an array of values between 1 and 100 and then multiplying that Array by an Array of the Odd values between 1 and 100 and then adding up the resultant Array.

Lets start with: \=SUM(ROW(1:100)\*MOD(ROW(1:100),2))

Note that the Row(1:100) is used twice in the formula.

In a spare cell: **D17** type: \=Row(1:100) then press **F9** not enter

Excel will respond with an array:  \={1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60;61;62;63;64;65;66;67;68;69;70;71;72;73;74;75;76;77;78;79;80;81;82;83;84;85;86;87;88;89;90;91;92;93;94;95;96;97;98;99;100}

An array of the values from 1 to 100.

Next we will look at the Mod section \=SUM(ROW(1:100)\*MOD(ROW(1:100),2))

In a spare cell: **D19** type: \=Mod(Row(1:100),2) then press **F9** not enter

Excel will respond with an array:  \={1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0;1;0}

Mod returns the remainder after dividing the first parameter by the second

Eg: Mod(5,2)=1 5 divided by 2 = 2 Remainder **1**.

So in our example Mod( Array, 2 ) returns the value 1 for the Odd Values and 0 for the Even values.

Next we multiply the 2 arrays together: \=SUM(ROW(1:100)\*MOD(ROW(1:100),2))

This is the same as:

\={1;2;3;4;5; … ;97;98;99;100} \* {1;0;1;0;1; … ;1;0;1;0}

In a spare cell: **D21** type: \=ROW(1:100)\*MOD(ROW(1:100),2) then press **F9** not enter

Excel will respond with an array:  \={1;0;3;0;5;0;7;0;9;0;11;0;13;0;15;0;17;0;19;0;21;0;23;0;25;0;27;0;29;0;31;0;33;0;35;0;37;0;39;0;41;0;43;0;45;0;47;0;49;0;51;0;53;0;55;0;57;0;59;0;61;0;63;0;65;0;67;0;69;0;71;0;73;0;75;0;77;0;79;0;81;0;83;0;85;0;87;0;89;0;91;0;93;0;95;0;97;0;99;0}

Finally we can add up the array values: \=SUM(ROW(1:100)\*MOD(ROW(1:100),2))

In a spare cell: **D23** type: \=SUM(ROW(1:100)\*MOD(ROW(1:100),2)) then press **F9** not enter

Excel will respond with a value of **\= 2500**, The Answer.

Variation 1:
------------

In the above formula \=SUM(ROW(1:100)\*MOD(ROW(1:100),2)) we described a method of evaluating Array values as either Odd or Even using the Mod function.

Excel has a built in function for determining if a Value is Odd and that is Isodd()

We can modify the above equation to use Isodd() as follows

\=SUM(ROW(1:100)\*ISODD(ROW(1:100)))

You can check it in cell **D28**.

What if I want to Sum the Even numbers?
---------------------------------------

We can use the variation described above to quickly add up the even numbers between 1 and 100

\=SUM(ROW(1:100)\*ISEVEN(ROW(1:100)))

In a spare cell: **D21** type: \=SUM(ROW(1:100)\*ISEVEN(ROW(1:100)))  then press **F9** not enter

Excel will respond with a value of **\= 2550**, The Answer.

How Else Can You Solve Sunita’s Problem?
----------------------------------------

Can you solve Sunita’s problem another way?

Let us know in the comments below:

Download
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/05/Count-Odd-Numbers.xls "FF 22.")
.

Formula Forensics “The Series”
------------------------------

This is the 22nd post in the Formula Forensics series.

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
| Written by Hui...  <br>Tags: [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [iseven()](https://chandoo.org/wp/tag/iseven/)<br>, [IsOdd()](https://chandoo.org/wp/tag/isodd/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [MOD()](https://chandoo.org/wp/tag/mod/)<br>, [OFFSET()](https://chandoo.org/wp/tag/offset/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [sum()](https://chandoo.org/wp/tag/sum/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 26 Responses to “Formula Forensics 022. Sum the Odd Numbers between 1 and 100”

1.  ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
     says:
    
    [May 24, 2012 at 9:19 am](https://chandoo.org/wp/formula-forensics-022/#comment-224293)
    
    For those who might be interested, there is a direct formula (no arrays) to calculate the first N odd numbers. Assuming A1 contains the number (N), this formula will perform the desired calculation...
    
    \=A1\*(A1+1)/2-INT(A1/2)\*(INT(A1/2)+1)
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224293)
    
2.  ![](https://secure.gravatar.com/avatar/e78eedc35b72ba19453ba3f4eb65fee56e9d0653b88f41f84a131382b6900a37?s=64&d=mm&r=g) Chiquitin says:
    
    [May 24, 2012 at 9:23 am](https://chandoo.org/wp/formula-forensics-022/#comment-224294)
    
    Why not use the mathematical formulas that already exist?
    
    For an arithmetic progression, the sum of the n first terms (S) is:
    
    S = n\* (a_1_+a_n_)/2
    
    a_1_ is the first term of the progression and a_n_ is the _n_th term.
    
    S = 50\*(1+99)/2 for odd numbers
    
    S = 50\*(2+100)/2 for even numbers
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224294)
    
3.  ![](https://secure.gravatar.com/avatar/3439761d77dfbe03f13f2e132616b4006dbf57add5a7a0c15dbfee1a0017ce76?s=64&d=mm&r=g) Thyson says:
    
    [May 24, 2012 at 1:02 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224301)
    
    My suggestion:
    
    \=SUM(IF(MOD(A2:A10,2)=0,A2:A10))  **Ctrl Shift Enter**
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224301)
    
4.  ![](https://secure.gravatar.com/avatar/68322167fe7dd4ce3a5483d483f8a27d5ba29600a2c2166759fca0c2dce37181?s=64&d=mm&r=g) [Pedro Wave](http://pedrowave.blogspot.com/)
     says:
    
    [May 24, 2012 at 1:23 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224302)
    
    Assuming A1 contains the number (N)  
    Sum the first N numbers:  
    \=A1\*(1+A1)/2  
    Sum the first odd numbers:  
    \=POWER(TRUNC((A1+1)/2),2)  
    Sum the first even numbers:  
    \=POWER(TRUNC(A1/2),2)+TRUNC(A1/2)  
    \=TRUNC(A1/2)\*(1+TRUNC(A1/2))  
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224302)
    
5.  ![](https://secure.gravatar.com/avatar/d309cae04fc971e84a19db159ccc2dfa78b7a1949564de62d999cbebc5e7cf62?s=64&d=mm&r=g) Vishwa says:
    
    [May 24, 2012 at 2:39 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224304)
    
    This is replacing offset value  
    \=SUM(2\*ROW(1:50)-1)
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224304)
    
    *   ![](https://secure.gravatar.com/avatar/68322167fe7dd4ce3a5483d483f8a27d5ba29600a2c2166759fca0c2dce37181?s=64&d=mm&r=g) [Pedro Wave](http://pedrowave.blogspot.com/)
         says:
        
        [May 24, 2012 at 3:23 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224308)
        
        Vishwa, your formula assuming A1 contains the number (N)  
        \=SUM(2\*ROW(INDIRECT("1:"&TRUNC((A1+1)/2)))-1)  **Ctrl Shift Enter**
        
        [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224308)
        
6.  ![](https://secure.gravatar.com/avatar/293eedc4bcb5c15e88a7d20abdbbbef07a2cee284fbfa7dbf4b2d70dbbf5aac0?s=64&d=mm&r=g) [bruce mcpherson](http://ramblings.mcpher.com/)
     says:
    
    [May 24, 2012 at 5:19 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224310)
    
    You may as well  avoid a control.shift.enter using sumProduct().
    
    \=SUMPRODUCT(ROW(1:100)\*( ISODD(ROW(1:100) )))  
       
    Bruce 
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224310)
    
7.  ![](https://secure.gravatar.com/avatar/2ad7a09f161ab9242c0420e5e3fbf51bd5fd4124929080e9d36c0d8b2ed6516c?s=64&d=mm&r=g) Matthew Holbrook says:
    
    [May 24, 2012 at 5:26 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224311)
    
    \=SUMPRODUCT(ROW(1:100)\*ISODD(ROW(1:100)))
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224311)
    
8.  ![](https://secure.gravatar.com/avatar/96d0eca88eb30c7c94249bc37a42589af4a86fc4a993ae8b4b6a9a18abf6aa57?s=64&d=mm&r=g) [Orlando Mezquita](http://www.facebook.com/xltricks)
     says:
    
    [May 24, 2012 at 5:29 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224312)
    
    There's no need to use array formulas:  
    \=SUMPRODUCT(ROW(1:100)\*ISODD(ROW(1:100)))  
    
    Another way would be:  
    \=ROUNDUP(100/2,0)^2 
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224312)
    
9.  ![](https://secure.gravatar.com/avatar/6a34ec2dc66cc4288b3dc55c10b22905e2c3de672edf4b5e04da7969630cf41b?s=64&d=mm&r=g) Eric says:
    
    [May 24, 2012 at 6:22 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224315)
    
    The sum of the first n odd numbers is n squared (i.e., n^2).
    
    n = 1   => sum = 1         =1^2  
    n = 2   => 1 + 3 = 4       =2^2  
    n = 3   => 1 + 3 + 5 = 9 =3^2  
    etc
    
    The sum of the first n even (and positive) numbers is n \* (n+1)
    
    n = 1  => sum = 2            = 1 \* (1 + 1) = 1 \* 2 = 2  
    n = 2  => 2 + 4 = 6          = 2 \* (2 + 1) = 2 \* 3 = 6  
    n = 3  => 2 + 4 + 6 = 12  = 3 \* (3 + 1) = 3 \* 4 = 12  
    etc
    
    Not really an issue for using Excel... but an issue for using math skills.
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224315)
    
10.  ![](https://secure.gravatar.com/avatar/c638d3d8f47cc8fb120c59cdf467c4b75dacd3381250e5c1990c16a27e208c1c?s=64&d=mm&r=g) Eddie says:
    
    [May 24, 2012 at 9:56 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224318)
    
    Sum the uneven numbers :  
       
    \=SUM(ROW(1:100)\*ISODD(ROW(1:100))) ?  
       
    Or am I missing something ?  
    (just an amateur :))
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224318)
    
11.  ![](https://secure.gravatar.com/avatar/95a6eeccbf092cd7d207fa5f0a33b38dc29f27215bf9ac79a9a8c77284ec64ba?s=64&d=mm&r=g) Jason H says:
    
    [May 24, 2012 at 10:34 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224321)
    
    In the same vein as others who've pointed out this is a mathematical progression one way of producing the same result would be the following formula:
    
    \=ROUNDUP(n/2,0)^2
    
    This version should work for all cases of determining sum of odd number whether provided with an even or odd number to target (n).  
       
    I remember at schoold learning the the formula for the number triangle, i.e. 1+2+3+4+...n
    
    which is: 
    
    \=(n^2 + n)/2
    
    and this has a common basis, but I'm not a mathemetician so I could be wrong.
    
    Regards JH 
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224321)
    
    *   ![](https://secure.gravatar.com/avatar/402b91d51db55afda58efdfef93190f38849fa9a7fd12cd66c92337b14c7a505?s=64&d=mm&r=g) [Rick Rothstein (MVP - Excel)](http://www.excelfox.com/forum/f22/)
         says:
        
        [May 25, 2012 at 5:35 am](https://chandoo.org/wp/formula-forensics-022/#comment-224338)
        
        \> I remember at schoold learning the the formula for the number triangle,  
        \> i.e. 1+2+3+4+…n  
        \>  
        \> which is:  
        \>  
        \> =(n^2 + n)/2
        
        I have always found this easier to remember when written like this...
        
        \=n\*(n+1)/2
        
        written this way, it is easy to remember we are multiplying the number n by the number that follows it (n+1) and then dividing that product by 2. Since either the number or the number following it must be even, we see the division by 2 works with no remainder. Also thinking about this, you can almost do the calculation in your head. Sum of the first 20 numbers.... 20\*21/2... but performing 20/2 (yielding 10) is easy to do in your head and multiplying 21 by that resulting 10 is a snap... answer almost immediately is 210.     
        
        [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224338)
        
12.  ![](https://secure.gravatar.com/avatar/5f0f088cb3853e66c96169b0867aaea85d62b8b65d689e8317ab08fdae64cf33?s=64&d=mm&r=g) modeste says:
    
    [May 24, 2012 at 11:27 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224325)
    
    Hi folks...
    
    may be i'm nut  
       
    but i understand  to compute cells values either row number ??? 
    
    the sum of Oddvalue in a continues number serie  is a mathematical function  as Rick says.
    
    to compute Odd cells values i use : 
    
    \=SUMPRODUCT(Myrange\*(MOD(MyRange,2)=0))
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224325)
    
13.  ![](https://secure.gravatar.com/avatar/f473a4423ab5cfe5dc4d401ec60c8382c536fc5073639309ca32f68f12ce81be?s=64&d=mm&r=g) [Jelle-Jeroen Lamkamp](http://xlns.lamkamp.nl/)
     says:
    
    [May 25, 2012 at 11:08 am](https://chandoo.org/wp/formula-forensics-022/#comment-224361)
    
    Works for all positive integers
    
      =(2\*ROUND(100/2,0))^2/4
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224361)
    
14.  ![](https://secure.gravatar.com/avatar/462d7841cd293f60e7e26689ee69bc639096d4dd4a0afecbd96b74862d7aa071?s=64&d=mm&r=g) Sudhir Gawade says:
    
    [May 25, 2012 at 12:08 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224365)
    
    look at this without CSE  
    A1=N  
    \=(CEILING(A1,2)/2)^2
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224365)
    
15.  ![](https://secure.gravatar.com/avatar/f473a4423ab5cfe5dc4d401ec60c8382c536fc5073639309ca32f68f12ce81be?s=64&d=mm&r=g) [Jelle-Jeroen Lamkamp](http://xlns.lamkamp.nl/)
     says:
    
    [May 25, 2012 at 1:58 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224374)
    
    \=ROUND(F13/2,0)^2
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224374)
    
    *   ![](https://secure.gravatar.com/avatar/f6fb631cb5af8ef896c056c59eee762e3c8aebb9b7f99c46044a735449aaa449?s=64&d=mm&r=g) Jeanbar says:
        
        [May 26, 2012 at 2:09 pm](https://chandoo.org/wp/formula-forensics-022/#comment-224408)
        
        Or even shorter: (EVEN(F13)/2)^2
        
        [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224408)
        
        *   ![](https://secure.gravatar.com/avatar/f473a4423ab5cfe5dc4d401ec60c8382c536fc5073639309ca32f68f12ce81be?s=64&d=mm&r=g) [Jelle-Jeroen Lamkamp](http://xlns.lamkamp.nl/)
             says:
            
            [May 30, 2012 at 10:15 am](https://chandoo.org/wp/formula-forensics-022/#comment-224506)
            
            This must be the shortest way to do it in Excel ...?
            
            [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224506)
            
        *   ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
            
            [June 8, 2012 at 2:43 pm](https://chandoo.org/wp/formula-forensics-022/#comment-225171)
            
            JeanBar ... Thats Brilliant
            
            [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-225171)
            
            *   ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
                
                [June 13, 2012 at 7:01 am](https://chandoo.org/wp/formula-forensics-022/#comment-225420)
                
                JeanBar the Even is not required.  
                If A1 contains 100 then (A1/2)^2 works as well
                
                [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-225420)
                
                *   ![](https://secure.gravatar.com/avatar/f6fb631cb5af8ef896c056c59eee762e3c8aebb9b7f99c46044a735449aaa449?s=64&d=mm&r=g) Jeanbar says:
                    
                    [June 13, 2012 at 3:41 pm](https://chandoo.org/wp/formula-forensics-022/#comment-225454)
                    
                    Sam,  
                    The EVEN() function is necessary. Your formula works for 100 indeed but not with 99: the result would be 2450.25. You need to have an integer result whatsoever.
                    
16.  ![](https://secure.gravatar.com/avatar/a2273097ec21441d94ac0fef223210c1386a227ee9afefc2a19cdbbe0db46336?s=64&d=mm&r=g) [rags6](http://www.techtipsntricks.com/)
     says:
    
    [June 1, 2012 at 9:24 am](https://chandoo.org/wp/formula-forensics-022/#comment-224568)
    
    You are very creative at your side, a pretty nice way of computing values. Good job!  
    [http://www.techtipsntricks.com/](http://www.techtipsntricks.com/)
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-224568)
    
17.  ![](https://secure.gravatar.com/avatar/5cbb48df5a5677c25fd2e4d93beb22b4ddd74de1d50a260bb2e182ea251ca421?s=64&d=mm&r=g) %MakSo% says:
    
    [June 26, 2012 at 10:20 pm](https://chandoo.org/wp/formula-forensics-022/#comment-225936)
    
    If C28 is the cell where I have a number up to which I'll add up the odd natural numbers - I will use the following:  
    "=IF(ISEVEN(C28),C28\*(C28+1)/2-(C28/2)\*(C28/2+1),C28\*(C28+1)/2-((C28-1)/2)\*((C28-1)/2+1))"
    
    using the principle sum of first n natural numbers = n\*(n+1)/2
    
    when the value is even - such as 100, I sum up all natural numbers to 100 using  C28\*(C28+1)/2. Then, see the even numbers 2,4,...100 are nothing but double the sum of first 50 natural numbers. Thus I subtract 2\* (C28/2)\*(C28/2+1)/2.
    
    If the given number is odd, I follow the same way, except I figure out C28 - 1 to be the number up to which I'll sum the even natural number series.   
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-225936)
    
18.  ![](https://secure.gravatar.com/avatar/951aa45e9042ebc661132142bf5c5b625edd52c15bc6de8fb827ba53abc02331?s=64&d=mm&r=g) Malcolm says:
    
    [July 17, 2012 at 9:49 am](https://chandoo.org/wp/formula-forensics-022/#comment-227190)
    
    Simplest formula:
    
    \= 25 \* 100
    
    Surely this is a case where the cleverest solution is to think about it first and see you don't need a formula? Adding up the numbers 1,3,5,7....97,99 is easiest if you think of it as (1+99),(3+97),(5+95).... there are clearly 25 pairs of 100, giving the answer 2500 in the time it takes to just step back and think.
    
    Sometimes the simplest solution is the most elegant! 
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-227190)
    
19.  ![](https://secure.gravatar.com/avatar/ec5ffaf27cdc3d63c628c88cd91648afabc0b1dc72f2acffd7ddfda92cc45dee?s=64&d=mm&r=g) [Omalohoso](http://www.facebook.com/omalohosolungangaantoine)
     says:
    
    [August 17, 2012 at 8:42 am](https://chandoo.org/wp/formula-forensics-022/#comment-228894)
    
    May the Grace and peace from above abide with you all as you are trying to input some helpful notes in order to help other people around the World.
    
    [Reply](https://chandoo.org/wp/formula-forensics-022/#comment-228894)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-022/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Chandoo Visits Perth Australia](https://chandoo.org/wp/chandoo-visits-perth-australia/) | [Do you work on Excel? How much salary you make? \[Surveys\]](https://chandoo.org/wp/how-much-salary-excel-survey/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)
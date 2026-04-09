# Monday Morning Mulling: October 2018 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-october-2018-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: October 2018 Challenge

*   October 28, 2018

Monday Morning Mulling: October 2018 Challenge
==============================================

Monday Morning Mulling: October 2018 Challenge
==============================================

29 October 2018

_On the final Friday of each month, we set an Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution – or two as in this case. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

**_Final Friday Fix: October Challenge Recap_**

As explained on Friday, a positive integer (whole number) is said to be **prime** if and only if two different integers divide it: one (1) and itself. Therefore, 1 is not prime and 2 is the only even prime _etc._

The challenge this month was extremely straightforward:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-542.jpg)

All you had to do was write a formula in Excel to determine whether a number typed in _(as above)_ is prime or not. That was it – just no VBA (or JavaScript!) / user defined functions.

**_Suggested Solution(s)_**

This month’s query then is, how do I determine if a number is prime? You might think, I couldn’t care less. But please keep reading. This month’s article is not so much about getting the right formula but more about, er, getting the formula right _in general_.

**THE INTERNET LIES TO YOU.**

That’s right. Before you switch off, this month’s question raises a very important point that affects us all. Let me explain. I want to determine whether a number in a particular cell, let’s call it **Number**, is prime or not, _e.g_. _(as above)_

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-542.jpg)

Let’s do something different this month. I am going to search for a solution to this problem _on the internet_. I know, who would have thought? I bet you’ve never done it. It doesn’t take too much effort to locate one of two very popular solutions, either

**{=IF(Number=2,”Prime”,IF(AND(MOD(Number,ROW(INDIRECT(“2:”&ROUNDUP(SQRT(Number),0))))<>0),”Prime”,”Not Prime”))}**

or

**{=IF(Number=2,”Prime”,IF(AND(MOD(Number,ROW(OFFSET($A$2,,,ROUNDUP(SQRT(Number),0)-1)))<>0),”Prime”,”Not Prime”))}** 

They have four things in common:

1.  They are both array functions (_i.e._ entered using **CTRL + SHIFT + ENTER** – you do not try and type the braces (**{** and **}**) in
2.  These solutions are cited all over the internet, including on esteemed websites like Microsoft’s own _Excel Blog_
3.  They are both fairly incomprehensible upon initial inspection
4.  Neither actually _work_.

Yup, read point 4 again. They’re wrong. They don’t work in all situations – and yet they seem to be universally accepted. And that’s the point of today’s blog. When we don’t know how to do something, you head for your favourite search engine, hunt out the answer – and if you are wiser, check four or five sites to ensure they come to the same conclusion before accepting that answer.

These formulae would pass that sniff test. That’s my point. But they are still wrong.

To show they don’t work, simply download this month’s [attached Excel file](https://sumproduct.com/assets/blog-pictures/2018/challenges/10-oct/mmm/sp-prime-number-identifier-example.xlsm)
, then try these:

*   Apparently, 1.7 is prime
*   With the first formula, the value 0 (zero) gives _#REF!_
*   With the second formula, the value 1 gives _#REF!_
*   Negative numbers give _#NUM!_

Nobody tests anything anymore. We are all download drones. And this scares the living daylights out of me. People might try numbers like 2, 17, 59, _etc._ and see it seems to work and conclude everything is fine. But just because something is on page 1 of a well-known search engine page doesn’t make it true. If you don’t believe me, Google it.

For the record, I made an attempt in the past – which worked for a while, and then OFFSET changed its behaviour! So please find below my latest and greatest attempt at a solution:

**{=IF(AND(MOD(IF(OR(MOD(Number,1),Number<0),,Number-1\*(Number<=2)),ROW(OFFSET($A$2,,,MAX(ROUNDUP(SQRT(ABS(Number)),0)-1\*(Number>1),1))))<>0,Number<>0),”Prime”,”Not Prime”)}**

That’s right – it’s even worse than the other two. In the next section, I’ll explain how this formula works, but feel free to stop reading at this juncture. Showing off some horrendous calculation is not the objective of this article. It’s realising that you have to be careful when reading articles on how to solve things in Excel. Yes, that includes my articles too (because – as I said above – my original solution _no longer works_).

**_How the Formula Works_**

You don’t have to read this! If you are interested though, the formula

**{=IF(AND(MOD(IF(OR(MOD(Number,1),Number<0),,Number-1\*(Number<=2)),ROW(OFFSET($A$2,,,MAX(ROUNDUP(SQRT(ABS(Number)),0)-1\*(Number>1),1))))<>0,Number<>0),”Prime”,”Not Prime”)}**

needs to be picked apart. However, before I do that, I need to show you a quick way to check for a prime. Consider the divisors of 60:

![](<Base64-Image-Removed>)

Do you see the symmetry? Once you get to the middle – the square root – the factorisation reverses. Since the square root of 60 is slightly less than 8, I only need to test to see if the numbers 1 to 8 divide 60. Given 1 and **n** will always divide **n**, I really only need to test the numbers 2 to **ROUNDUP(SQRT(n),0)** (the square root of **n** rounded up to the next whole number), which is 8 here. This saves a lot of needless calculations!

This explains the element highlighted:

**{=IF(AND(MOD(IF(OR(MOD(Number,1),Number<0),,Number-1\*(Number<=2)),_ROW(OFFSET($A$2,,,_MAX(_ROUNDUP(SQRT(_ABS(_Number_)_),0)_\-1\*(Number>1),1))))<>0,Number<>0),”Prime”,”Not Prime”)}**

The function **OFFSET(Reference, Rows, Columns, \[Height\], \[Width\])** has been discussed previously (see the article [Onset of Offset](https://www.sumproduct.com/thought/onset-of-offset)
 for further details).

The formula **OFFSET($A$2,,,ROUNDUP(SQRT(Number),0)-1)** gives a range of **A2** to **A8** if **Number** were 60 (1 has to be subtracted otherwise with a height of 8, you would get the range **A2:A9**). Putting **ROW()** around this expression is a crafty way to convert to the numbers 2 to 8 inclusive. This is why cell **A2** must be a cell reference on row 2 in this example.

The next key element is **MOD(Number, Divisor)**. Again, I have discussed **MOD** before (please see [A Modicum of MOD](https://www.sumproduct.com/thought/a-modicum-of-mod)
 for further details): this provides the remainder after dividing **Number** by **Divisor**. So, if I divide **Number** by each **Divisor** for the numbers 2 to **ROUNDUP(SQRT(Number),0)** – which would be 2 to 8 if **Number** were 60 – and any division gives me zero, that would mean **Number** is divisible by **Divisor**, _i.e._ the number is not prime. If no division gives zero, it has to be prime so

**{= IF(AND(MOD(Number,ROW(OFFSET($A$2,,,ROUNDUP(SQRT(Number),0)-1)))<>0),”Prime”,”Not Prime”)}**

gives the appropriate prime / not prime identification in certain circumstances. This formula is both a variation of my proposed one and the second one identified as wrong earlier. Do note it is encapsulated in an **AND** function and is in an array formula. This forces Excel to perform all of the calculations from 2 to **ROUNDUP(SQRT(Number),0)** in one cell. That’s a useful way of using an array formula (for more on arrays, please see [Array of Light](https://www.sumproduct.com/thought/array-of-light)
).

The rest of my formula,

**{=IF(AND(MOD(_IF(OR(MOD(Number,1),Number<0),,Number-1\*(Number<=2)_),ROW(OFFSET($A$2,,,ROUNDUP(SQRT(_ABS(_Number_)_),0)-1_\*(Number>1)_)))<>0),”Prime”,”Not Prime”)}**

**{=IF(AND(MOD(_IF(OR(MOD(Number,1),Number<0),,Number-1\*(Number<=2)_),ROW(OFFSET($A$2,,,_MAX(_ROUNDUP(SQRT(_ABS(_Number_)_),0)-1_\*(Number>1),1)_)))<>0,Number<>0),”Prime”,”Not Prime”)}**

is made up of tweaks to ensure:

*   Non-integers are not prime
*   0 is neither prime nor an error
*   1 is neither prime nor an error
*   Negative numbers are neither prime nor an error.

My formula goes wrong eventually. 9 x 10200 is clearly not prime (it’s 3 x 10100 squared) but Excel cannot evaluate it because it’s too large. Meh, you can’t have everything!

Incidentally in the attached Excel file, as well as showing the oft-quoted – but wrong – solutions and my revised attempt above, I have added an alternative solution:

**\=IF(OR(Number<=0,MOD(Number,1)),”Not Prime”,IF(MIN(MOD(Number,1+SEQUENCE(ROUNDUP(SQRT(Number),0)))),”Prime”,”Not Prime”))**

This solution uses the brand new to Office 365 [Dynamic Arrays](https://www.sumproduct.com/news/article/getting-arrays-spilling-the-beans-on-seven-new-functions)
, using the **SEQUENCE** function to convert the consecutive numbers. Note it doesn’t require an array (**CTRL + SHIFT +** ENTER) formula. Please note for most people this formula will give rise to an error, as these functions and features are not yet Generally Available in Excel – but it’s worth noting for the future.

If it does work, my first solution will be revised using **SINGLE** and no longer require braces (‘**{**‘ and ‘**}**‘):

**\=IF(AND(MOD(IF(OR(MOD(Number,1),Number<0),,Number-1\*(Number<=2)),_SINGLE(_ROW(OFFSET($A$2,,,MAX(ROUNDUP(SQRT(ABS(Number)),0)-1\*(Number>1),1)))_)_)<>0,Number<>0),”Prime”,”Not Prime”)**

**_Word to the Wise_**

Keep reading these articles but stay cynical. I am as prone to mistakes as the next persona (that’s a joke!). By all means research, but convince yourself that it’s right. Take nothing at face value.

_The Final Friday Fix will return on Friday 30 November with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-october-2018-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-october-2018-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-october-2018-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-october-2018-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-october-2018-challenge/#0 "close")

top
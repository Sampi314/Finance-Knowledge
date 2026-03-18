# Final Friday Fix: February 2017 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-february-2017-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: February 2017 Challenge

*   February 23, 2017

Final Friday Fix: February 2017 Challenge
=========================================

Final Friday Fix: February 2017 Challenge
=========================================

24 February 2017

_On the final Friday of each month, we’re going to set Excel for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There’s no prizes at this stage, you’re playing for bragging rights only!_

**_There’s a Reason for the Exclamation Mark_**

Nice and simple explanation this Friday: I want to talk about factorials, denoted by **n!** where

**n! = n (n-1)!**

_i.e._ **n! = n (n-1) (n-2) … 3 x 2 x 1.**

For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. These numbers become astronomical (technical term) _very_ quickly. And it gets worse.

Excel has a function, **FACT**, which calculates factorials. Except it doesn’t. Consider the following summary:

![](<Base64-Image-Removed>)

Using Excel, 23! is 2.5852E+22 (Scientific notation), which when expanded is 25,852,016,738,885,000,000,000. Actually, 23! is really 25,852,016,738,884,976,640,000. Microsoft Excel can only calculate to 15 significant figures and then it starts rounding. Not good.

But it’s even worse than that. The **LEN** function in Excel counts how many characters there are in a text string. According to Excel, 22! has 20 digits whereas 23! has 19 digits. So 23! is _smaller_ than 22! (yeah, right). What on earth..?

We’ll revisit this on Monday.

**_The Challenge_**

Using Excel (unless you fancy a night of long multiplication), calculate 171! precisely (_i.e._ not just to 15 significant figures).

![](<Base64-Image-Removed>)

**_A clue…_**

Sound easy? Unless your surname is Gauss you might find this a little awkward. We’ll publish our suggested solution in Monday’s blog. Have a great weekend!

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-february-2017-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-february-2017-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-february-2017-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-february-2017-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-february-2017-challenge/#0 "close")

top
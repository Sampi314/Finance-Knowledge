# A to Z of Excel Functions: The RAND Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rand-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The RAND Function

*   May 26, 2024

A to Z of Excel Functions: The RAND Function
============================================

A to Z of Excel Functions: The RAND Function
============================================

27 May 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **RAND** function._

**The RAND function**

The **RAND** function returns an evenly distributed random real number greater than or equal to zero \[0\] and less than one \[1\]. This is a [volatile function](https://www.sumproduct.com/thought/volatile-functions-talk-dirty-to-me)
: a new random real number is returned every time the worksheet is calculated.

Since Excel 2010, Excel uses the Mersenne Twister algorithm to generate random numbers. This is a general purpose pseudo-random number generator (PRNG) developed in 1997 by Makoto Matsumoto and Takuji Nishimura. Its name derives from the fact that its period length is chosen to be a Mersenne prime.

Whether you understand this or not is not important: this Mersenne Twister was designed specifically to rectify most of the flaws found in older PRNGs which caused issues for many programmers. Excel just so happened to jump on the bandwagon, and employs the most commonly used version of the Mersenne Twister algorithm, which is based on the Mersenne prime

219937 − 1

This is known as the “standard implementation” (MT19937), using a 32-bit word length. Try not to get too excited now you know this.

The **RAND** syntax takes no arguments:

**\= RAND()** 

Please don’t take issue with this point – I accept no arguments.

It should be noted that:

*   to generate a random number between **a** and **b**, use:

**\=RAND() \* (b – a ) + a  
**

*   if you want to use **RAND** to generate a random number but don’t want the numbers to change every time the cell is calculated, you can enter **\=RAND()** in the Formula bar, and then press **F9** to change the formula to a random number. The formula will calculate and leave you with just a value.

Please see my examples below:

![](<Base64-Image-Removed>)

_  
We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rand-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rand-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rand-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rand-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rand-function/#0 "close")

top
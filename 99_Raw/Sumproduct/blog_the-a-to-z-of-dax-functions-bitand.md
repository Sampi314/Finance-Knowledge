# The A to Z of DAX Functions – BITAND

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitand/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – BITAND

*   March 29, 2022

The A to Z of DAX Functions – BITAND
====================================

Power Pivot Principles: The A to Z of DAX Functions – BITAND
============================================================

29 March 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **BITAND**._

**_The BITAND function_**

Welcome to Functions You’re Unlikely to Use This Side of Doomsday, Part 97.

The **BITAND** function returns a bitwise ‘AND’ of two numbers. For those of us without PhD’s in IT, this means that the value of each bit position (the corresponding number reading from right to left when represented in binary) is counted only if both parameter’s bits at that position are one \[1\].

The **BITAND** function employs the following syntax to operate:

**BITAND(number1, number2)**

The **BITAND** function has the following arguments:

*   **number1** and **number2:** these are required, represent any scalar expressions that return a number. If it is not an integer, it is truncated.

It should be further noted that:

*   **BITAND** returns a decimal number
*   the result is a bitwise ‘**AND**‘ of its parameters
*   the value of each bit position is counted only if both parameter’s bits at that position are 1
*   the values returned from the bit positions progress from right to left as powers of 2. The rightmost bit returns 1 (2^0), the bit to its left returns 2 (2^1), and so on
*   this function supports both positive and negative numbers.

Please see my example below:

![](<Base64-Image-Removed>)

In binary, since 13 is **1**10**1** and 11 is **1**01**1**, the value returned is **1**00**1** in binary, _i.e._ nine \[9\].

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitand/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitand/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitand/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitand/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitand/#0 "close")

top
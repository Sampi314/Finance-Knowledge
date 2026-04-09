# The A to Z of DAX Functions – BITOR

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitor/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – BITOR

*   April 12, 2022

The A to Z of DAX Functions – BITOR
===================================

Power Pivot Principles: The A to Z of DAX Functions – BITOR
===========================================================

12 April 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at BITOR._

**_The BITOR function_**

I’m starting to get used to these functions now, well a BIT anyway (get it?). This function returns a bitwise ‘OR’ of two numbers. In this variant, this means that the value of each bit position (the corresponding number reading from right to left when represented in binary) is counted if any of the parameter’s bits at that position are 1.

The **BITOR** function employs the following syntax to operate:

**BITOR(number1, number2)**

The **BITOR** function has the following arguments:

*   **number1** and **number2:** these are required and represent scalar expressions that return numbers. If they are not integers, they are truncated.

It should be noted that:

*   the result is a bitwise ‘**OR**‘ of its parameters
*   in the result, each bit position is 1 if any of the parameter’s bits at that position are 1
*   the values returned from the bit positions progress from right to left as powers of 2. The rightmost bit returns 1 (2^0), the bit to the left returns 2 (2^1), and so on
*   this function supports both positive and negative numbers.

Please see my example below:

![](<Base64-Image-Removed>)

In binary, since 9 is **1**00**1** and 10 is **1**0**1**0, the result is **1**0**11** in binary, which is 11 in decimal.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitor/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitor/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitor/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitor/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitor/#0 "close")

top
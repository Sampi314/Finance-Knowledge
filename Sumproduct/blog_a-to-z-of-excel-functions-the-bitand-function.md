# A to Z of Excel Functions: The BITAND Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitand-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The BITAND Function

*   February 12, 2017

A to Z of Excel Functions: The BITAND Function
==============================================

A to Z of Excel Functions: The BITAND Function
==============================================

13 February 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **BITAND** function._

**The BITAND function**

Now this is more like it. Finally, we get to functions used all of the time by your typical Excel user. Not.

This function returns a bitwise ‘AND’ of two numbers. For those of us without PhD’s in IT, this means that the value of each bit position (the corresponding number reading from right to left when represented in binary) is counted only if both parameter’s bits at that position are 1.

The **BITAND** function employs the following syntax to operate:

**BITAND(number1, number2)**

The **BITAND** function has the following arguments:

*   **number1:** this is required and must be in decimal form, greater than or equal to 0
*   **number2:** also required. This too must be in decimal form and greater than or equal to 0.

It should be further noted that:

*   **BITAND** returns a decimal number
*   the result is a bitwise ‘**AND**‘ of its parameters
*   the value of each bit position is counted only if both parameter’s bits at that position are 1
*   the values returned from the bit positions progress from right to left as powers of 2. The rightmost bit returns 1 (2^0), the bit to its left returns 2 (2^1), and so on
*   if either argument is less than 0, **BITAND** returns the _#NUM!_ error value
*   if either argument is a non-integer or is greater than (2^48)-1, **BITAND** returns the _#NUM!_ error value
*   if either argument is a non-numeric value, **BITAND** returns the _#VALUE!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitand-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitand-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitand-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitand-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitand-function/#0 "close")

top
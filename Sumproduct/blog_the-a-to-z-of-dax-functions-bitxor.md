# The A to Z of DAX Functions – BITXOR

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitxor/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – BITXOR

*   April 26, 2022

The A to Z of DAX Functions – BITXOR
====================================

Power Pivot Principles: The A to Z of DAX Functions – BITXOR
============================================================

26 April 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **BITXOR**._

**_The BITXOR function_**

This function returns a bitwise ‘**XOR**’ of two numbers (**XOR** was first introduced in Excel 2013 and at the current rate of publishing these articles we should get to this one by 2044). Essentially, **BITXOR** converts two numbers to binary expressions and compares the digits at each position from right to left. If the values are not equal, the function returns a 1 for that position (bit). For each 1, its position is ascertained and converted to a power of 2 (2^0 for the rightmost position, 2^1 for the value to its left, 2^2 for the value to the left of this and so on). These corresponding powers of two are then summed.

The **BITXOR** function employs the following syntax to operate:

**BITXOR(number1, number2)**

The **BITXOR** function has the following arguments:

*   **number1** and **number2:** these are required. These are any scalar expressions that return numbers. If these are not integers, they are truncated.

It should be further noted that:

*   **BITXOR** returns a decimal number that is the result of the sum of a bitwise ‘**XOR**‘ (exclusive **XOR**) of its parameters
*   this function supports both positive and negative numbers
*   in the result, each bit position is 1 if the values of the parameters at that bit position are not equal; in other words, one value is 0 and the other is 1. For example, using **BITXOR(**5**,**3**)**, 5 is expressed as 101 in binary and 3 as 11 in binary. To help with comparison, you can consider 3 as 011. From right to left, the bit values at the three positions in this example are the same (1) only at the rightmost position. A ‘not equal’ result returns a 1 for the second and third positions from the right, and an ‘equal’ result returns 0 for the rightmost position
*   values of 1 returned from the bit positions progress from right to left as powers of 2. The rightmost bit returns 1 (2^0), the bit to the left returns 2 (2^1), and so on
*   using the same example, 0 is returned for the rightmost bit position because it is a 0, 2 (2^1) is returned for the second bit position from the right (a 1 value), and 4 (2^2) is returned for the leftmost bit (also a 1 value). The total is 6, in decimal representation.

Please see my example below:

![](<Base64-Image-Removed>)

In binary, since 9 is 100**1** and 10 is 10**1**0, the result is 00**11** in binary, which is 3 in decimal.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitxor/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitxor/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitxor/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitxor/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitxor/#0 "close")

top
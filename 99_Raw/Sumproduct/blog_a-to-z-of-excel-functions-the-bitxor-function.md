# A to Z of Excel Functions: The BITXOR Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitxor-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The BITXOR Function

*   March 16, 2017

A to Z of Excel Functions: The BITXOR Function
==============================================

A to Z of Excel Functions: The BITXOR Function
==============================================

17 March 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **BITXOR** function._

**The BITXOR function**

This function returns a bitwise ‘**XOR**‘ of two numbers (**XOR** was first introduced in Excel 2013 and at the current rate of publishing these articles we should get to this one by 2044). Essentially, **BITXOR** converts two numbers to binary expressions and compares the digits at each position from right to left. If the values are not equal, the function returns a 1 for that position (bit). For each 1, its position is ascertained and converted to a power of 2 (2^0 for the rightmost position, 2^1 for the value to its left, 2^2 for the value to the left of this and so on). These corresponding powers of two are then summed.

The **BITXOR** function employs the following syntax to operate:

**BITXOR(number1, number2)**

The **BITXOR** function has the following arguments:

*   **number1:** this is required and must be greater than or equal to 0
*   **number2:** also required. This must be greater than or equal to 0.

It should be further noted that:

*   **BITXOR** returns a decimal number that is the result of the sum of a bitwise ‘**XOR**‘ (exclusive **XOR**) of its parameters
*   if either argument is outside its constraint, **BITXOR** returns the _#NUM!_ error value
*   if either argument is greater than (2^48)-1, **BITXOR** returns the _#NUM!_ error value
*   if either argument is a non-numeric value, **BITXOR** returns the _#VALUE!_ error value
*   in the result, each bit position is 1 if the values of the parameters at that bit position are not equal; in other words, one value is 0 and the other is 1. For example, using **BITXOR(**5**,**3**)**, 5 is expressed as 101 in binary and 3 as 11 in binary. To help with comparison, you can consider 3 as 011. From right to left, the bit values at the three positions in this example are the same (1) only at the rightmost position. A ‘not equal’ result returns a 1 for the second and third positions from the right, and an ‘equal’ result returns 0 for the rightmost position
*   values of 1 returned from the bit positions progress from right to left as powers of 2. The rightmost bit returns 1 (2^0), the bit to the left returns 2 (2^1), and so on
*   using the same example, 0 is returned for the rightmost bit position because it is a 0, 2 (2^1) is returned for the second bit position from the right (a 1 value), and 4 (2^2) is returned for the leftmost bit (also a 1 value). The total is 6, in decimal representation.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/2fe8c54530327b9e524f3b8a8c2db462.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitxor-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitxor-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitxor-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitxor-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-bitxor-function/#0 "close")

top